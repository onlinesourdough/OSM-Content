"""Exercise the actual workflow resolver without a credential or network."""
import base64
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
WORKFLOW=(ROOT/'.github/workflows/sync-notion.yml').read_text()
START=WORKFLOW.index('          import base64,')
GUARD='\n'.join(line[10:] for line in WORKFLOW[START:].split('\n          PY',1)[0].splitlines())
A,B,C='a'*40,'b'*40,'c'*40
IDS=[r['page_id'] for r in json.loads((ROOT/'release.json').read_text())['notion_targets']]


class SourceSelectionTests(unittest.TestCase):
    def resolve(self, *, head_version='0.13.0', artifacts=None, event='release', mode='all', attempt=3, paginated=False, validation_override=None, server_status_filter_empty=False):
        artifacts=artifacts or [('content-tag-pass-1',True)]
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);old=os.getcwd();os.chdir(root)
            payload={'release':{'id':12},'workflow_run':{'head_sha':C},'inputs':{'mode':mode}}
            (root/'event.json').write_text(json.dumps(payload))
            env={'GITHUB_REPOSITORY':'owner/repo','GITHUB_EVENT_NAME':event,'GITHUB_EVENT_PATH':str(root/'event.json'),
                 'GITHUB_OUTPUT':str(root/'output'),'GITHUB_STEP_SUMMARY':str(root/'summary'),
                 'GITHUB_RUN_ID':'12345','GITHUB_RUN_ATTEMPT':str(attempt)}
            downloads=[]
            def api(args,**kwargs):
                url=args[-1]
                if url.endswith('/commits/main'):data={'sha':C}
                elif url.endswith('/releases/latest'):data={'id':12,'tag_name':'v0.12.0','draft':False,'prerelease':False}
                elif '/contents/VERSION?ref=' in url:
                    ref=url.split('ref=')[-1];version=head_version if ref==C else '0.12.0'
                    data={'content':base64.b64encode(version.encode()).decode()}
                elif url.endswith('/commits/v0.12.0'):data={'sha':A}
                elif '/compare/' in url:data={'status':'ahead'}
                elif '/actions/workflows/validate.yml/runs?' in url:
                    sha=re.search('head_sha=([a-f0-9]+)',url)[1]
                    row={'head_sha':sha,'event':'push','head_branch':'main','conclusion':'success','head_repository':{'full_name':'owner/repo'}}
                    row.update(validation_override or {})
                    data={'workflow_runs':[] if server_status_filter_empty and '&status=' in url else [row]}
                elif '/artifacts?' in url:
                    items=[{'name':name,'expired':False} for name,_ in artifacts]
                    if paginated and url.endswith('page=1'):items=[{'name':'other-'+str(i),'expired':False} for i in range(100)]
                    data={'artifacts':items}
                else:raise AssertionError('Unexpected endpoint: '+url)
                return json.dumps(data)
            def download(args):
                name=args[args.index('--name')+1];downloads.append(name)
                good=dict(artifacts)[name];dest=Path(args[args.index('--dir')+1])
                rows=[{'page_id':p,'state':'written'} for p in IDS]
                if not good:rows[-1]=rows[0]
                receipt={'ok':True,'complete':True,'scope':'whole-set','source_commit':A,'api':rows,'public':[{'page_id':p,'verified_at':'2026-11-20T20:00:00.000Z','expected_lines':3} for p in IDS]}
                if good=='missing-observation':receipt['public']=[{'page_id':p} for p in IDS]
                (dest/'content-sync.json').write_text('{' if good=='truncated' else json.dumps(receipt))
                (dest/'publication-plan.json').write_text(json.dumps({'tag_source':A,'catchup_source':B}))
            try:
                with patch.dict(os.environ,env),patch('subprocess.check_output',side_effect=api),patch('subprocess.check_call',side_effect=download):
                    exec(compile(GUARD,'workflow-source-resolver','exec'),{})
                outputs=dict(line.split('=',1) for line in (root/'output').read_text().splitlines())
                return outputs,downloads
            finally:os.chdir(old)

    def test_attempt_three_recovers_attempt_one_after_main_bumps_version(self):
        result,downloads=self.resolve()
        self.assertEqual('true',result['resume']);self.assertEqual(B,result['catchup']);self.assertEqual(A,result['sha'])
        self.assertEqual(['content-tag-pass-1'],downloads)

    def test_invalid_newer_receipt_falls_back_to_latest_valid_earlier_one(self):
        result,downloads=self.resolve(artifacts=[('content-tag-pass-2',False),('content-tag-pass-1',True)],paginated=True)
        self.assertEqual('true',result['resume']);self.assertEqual(B,result['catchup'])
        self.assertEqual(['content-tag-pass-2','content-tag-pass-1'],downloads)

    def test_truncated_newer_artifact_does_not_hide_valid_older_receipt(self):
        result,_=self.resolve(artifacts=[('content-tag-pass-2','truncated'),('content-tag-pass-1',True)])
        self.assertEqual('true',result['resume']);self.assertEqual(B,result['catchup'])

    def test_public_ids_without_observation_evidence_do_not_authorize_resume(self):
        result,_=self.resolve(artifacts=[('content-tag-pass-1','missing-observation')])
        self.assertEqual('false',result['resume'])

    def test_duplicate_api_identity_does_not_authorize_resume(self):
        result,_=self.resolve(artifacts=[('content-tag-pass-1',False)])
        self.assertEqual('false',result['resume']);self.assertEqual('',result['catchup'])

    def test_unpublished_manual_write_does_not_substitute_an_old_release(self):
        result,downloads=self.resolve(event='workflow_dispatch',mode='one-page',attempt=1)
        self.assertEqual('false',result['current']);self.assertEqual(C,result['sha']);self.assertEqual([],downloads)

    def test_readonly_uses_exact_success_when_server_status_filter_is_empty(self):
        result,_=self.resolve(event='workflow_dispatch',mode='read-only',attempt=1,server_status_filter_empty=True)
        self.assertEqual('true',result['current']);self.assertEqual(C,result['sha'])

    def test_readonly_still_rejects_unsuccessful_wrong_source_or_fork(self):
        for override in ({'conclusion':'failure'},{'conclusion':None},{'head_sha':A},
                         {'event':'pull_request'},{'head_branch':'other'},
                         {'head_repository':{'full_name':'other/repo'}}):
            with self.subTest(override=override),self.assertRaisesRegex(SystemExit,'no successful main'):
                self.resolve(event='workflow_dispatch',mode='read-only',attempt=1,validation_override=override)

    def test_release_receipt_is_durable_before_catchup_can_write(self):
        self.assertLess(WORKFLOW.index('name: content-tag-pass-${{ github.run_attempt }}'),WORKFLOW.index('name: Catch up validated main'))


if __name__=='__main__':unittest.main()
