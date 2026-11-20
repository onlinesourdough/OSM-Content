import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('sync', Path(__file__).resolve().parents[1] / 'scripts/sync_notion.py')
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)
A, B = 'a' * 40, 'b' * 40


class Source:
    ref = B
    def read(self, path, ref=None):
        if path == 'VERSION':
            return '0.12.0\n'
        return '## Reader\n\nA useful explanation.\n\n<page url="https://app.notion.com/p/123">\nChild\n</page>\n'
    def ancestor(self, ref):
        return ref in {A, B}


class API:
    def __init__(self, baselines):
        self.rows = {p: {**copy.deepcopy(b), 'intrinsic': {'Files': ['unchanged']}, 'edited': 'old', 'files': []} for p, b in baselines.items()}
        self.calls = []
        self.lost_answer = False
        self.reject = False
        self.mutate = None
        self.reads = {}
        self.write_requests = 0
    def read(self, page):
        self.reads[page] = self.reads.get(page, 0) + 1
        if self.mutate == page and self.reads[page] == 2:
            self.rows[page]['body'] += '\nHuman edit'
        return copy.deepcopy(self.rows[page])
    def verify_packet(self, *args):
        pass
    def write_body(self, page, before, body):
        self.calls.append(('body', page));self.write_requests += 1
        if self.reject:
            raise OSError('rejected')
        self.rows[page]['body'] = body
        self.rows[page]['edited'] = 'new'
        if self.lost_answer:
            raise OSError('answer lost after applied')


def baselines():
    rows = {p: {'body': Source().read(path).strip(), 'source': None} for p, path in s.GUIDES.items()}
    for p in s.TEMPLATES:
        rows[p] = {'body': '## Instructions\n\nKeep the owner\'s voice.\n\n' + s.SOURCE_NOTE + ' Old source note.\n\n<file source="notion-file-block://abc/archive?name=source.zip" />', 'source': 'Old property', 'packet_sha256': 'frozen'}
    return rows


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.base = baselines();self.api = API(self.base);self.source = Source()
    def test_full_write_then_exact_replay_has_zero_writes(self):
        first = s.reconcile(self.api, self.source, self.base, write=True)
        self.assertEqual(8, sum(r['state']=='written' for r in first))
        self.api.calls.clear()
        again = s.reconcile(self.api, self.source, self.base, write=True)
        self.assertTrue(all(r['state']=='unchanged' for r in again));self.assertEqual([], self.api.calls)
    def test_one_page_does_not_write_seven_other_pages(self):
        selected = next(iter(s.GUIDES))
        result = s.reconcile(self.api, self.source, self.base, write=True, only=selected, max_writes=1)
        self.assertEqual([('body', selected)], self.api.calls)
        self.assertEqual(7, sum(r['state']=='prepared' for r in result))
    def test_human_edit_holds_whole_preflight(self):
        self.api.rows[next(iter(s.TEMPLATES))]['body'] += '\nOwner edit'
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True)
        self.assertEqual([], self.api.calls)
    def test_edit_between_preflight_and_write_is_kept(self):
        self.api.mutate = next(iter(s.GUIDES))
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True)
        self.assertEqual([], self.api.calls)
    def test_lost_write_answer_is_read_back_and_not_repeated(self):
        self.api.lost_answer = True
        result = s.reconcile(self.api, self.source, self.base, write=True)
        self.assertTrue(all(r['state']=='written' for r in result))
        self.assertEqual(8, len([c for c in self.api.calls if c[0]=='body']))
    def test_rejected_write_is_not_retried(self):
        self.api.reject = True;checkpoint=[]
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True, record=lambda rows:checkpoint.extend(copy.deepcopy(rows)))
        self.assertEqual(1, len(self.api.calls));self.assertEqual('pending', checkpoint[-1]['state'])
    def test_read_only_preflight_prepares_without_writes(self):
        result=s.reconcile(self.api,self.source,self.base)
        self.assertTrue(all(r['state']=='prepared' for r in result))
        self.assertEqual([],self.api.calls)
    def test_hyperlink_destination_cannot_change_behind_plain_text(self):
        p=next(iter(s.TEMPLATES))
        self.api.rows[p]['source_links']=[{'text':'https://github.com/accepted','url':'https://example.com/changed'}]
        with self.assertRaises(s.Held):s.reconcile(self.api,self.source,self.base,write=True)
        self.assertEqual([],self.api.calls)
    def test_source_property_changed_during_body_write_is_preserved(self):
        p=next(iter(s.TEMPLATES)); original=self.api.write_body
        def concurrent(page,before,body):
            original(page,before,body)
            self.api.rows[page]['source']='Concurrent human source edit'
        self.api.write_body=concurrent
        with self.assertRaises(s.Held):s.reconcile(self.api,self.source,self.base,write=True,only=p)
        self.assertEqual('Concurrent human source edit',self.api.rows[p]['source'])
        self.assertEqual([('body',p)],self.api.calls)
    def test_api_uses_observed_match_instead_of_unconditional_replace(self):
        api=object.__new__(s.API);sent=[]
        api.request=lambda method,path,payload: sent.append(payload) or {}
        api.write_body(next(iter(s.GUIDES)),{'raw_body':'Human observed body'},'Desired body')
        self.assertEqual('update_content',sent[0]['type'])
        self.assertEqual([{'old_str':'Human observed body','new_str':'Desired body'}],sent[0]['update_content']['content_updates'])
    def test_template_patch_selects_only_the_source_note(self):
        p=next(iter(s.TEMPLATES));api=object.__new__(s.API);sent=[]
        api.request=lambda method,path,payload: sent.append(payload) or {}
        api.write_body(p,{'raw_body':self.base[p]['body']},s.render(self.source,p,self.base)['body'])
        edit=sent[0]['update_content']['content_updates'][0]
        self.assertTrue(edit['old_str'].startswith(s.SOURCE_NOTE))
        self.assertNotIn('<file',edit['new_str'])
    def test_unchanged_approved_source_hyperlink_is_accepted(self):
        p=next(iter(s.TEMPLATES));url='https://github.com/accepted'
        self.base[p]['source']=f'[{url}]({url})'
        self.api=API(self.base);self.api.rows[p]['source_links']=[{'text':url,'url':url}]
        s.reconcile(self.api,self.source,self.base)
    def test_media_signatures_are_excluded_from_matched_prose(self):
        api=object.__new__(s.API);sent=[]
        api.request=lambda method,path,payload:sent.append(payload) or {}
        raw='Old prose\n\n<image source="https://signed/A" />\n\nOld tail'
        desired='New prose\n\n<image source="notion-file-block://stable" />\n\nNew tail'
        api.write_body(next(iter(s.GUIDES)),{'raw_body':raw},desired)
        edits=sent[0]['update_content']['content_updates']
        self.assertEqual(2,len(edits));self.assertNotIn('signed',str(edits));self.assertNotIn('<image',str(edits))
    def test_partial_prose_update_can_resume_with_native_media_unchanged(self):
        p=next(iter(s.GUIDES));media='\n\n<image source="stable" />\n\n'
        self.base[p]['body']='Old prefix'+media+'Old suffix'
        class WithMedia(Source):
            def read(self,path,ref=None):
                if path=='VERSION':return '0.12.0'
                return 'New prefix'+media+'New suffix'
        source=WithMedia();wanted=s.render(source,p,self.base)['body']
        seen={**self.api.rows[p],'body':'New prefix'+media+'Old suffix'}
        self.assertEqual(wanted,s.plan(source,self.base,p,seen)['body'])
        seen['body']='Human prefix'+media+'Old suffix'
        with self.assertRaises(s.Held):s.plan(source,self.base,p,seen)
    def test_list_item_break_is_not_a_second_list_item(self):
        self.assertNotEqual(s.canonical('- First<br />- Second'),s.canonical('- First\n- Second'))
    def test_later_partial_update_recovers_old_segment_revision(self):
        p=next(iter(s.GUIDES));media='\n\n<image source="stable" />\n\n'
        class RevisionLinks(Source):
            def read(self,path,ref=None):
                if path=='VERSION':return '0.12.0'
                ref=ref or self.ref
                return '[Link]('+s.REPO+'/blob/'+ref+'/docs/setup.md)'+media+'Tail '+ref
        source=RevisionLinks()
        self.base[p]['body']='Initial prefix'+media+'Initial tail'
        old=s.render(source,p,self.base,A)['body'];wanted=s.render(source,p,self.base)['body']
        mixed=s.chunks(old);mixed[-1]=s.chunks(wanted)[-1]
        seen={**self.api.rows[p],'body':''.join(mixed)}
        self.assertEqual(wanted,s.plan(source,self.base,p,seen)['body'])
    def test_native_media_order_change_holds_before_any_write(self):
        p=next(iter(s.GUIDES));a='<image source="first" />';b='<image source="second" />'
        self.base[p]['body']='Prose\n'+b+'\n'+a
        class Images(Source):
            def read(self,path,ref=None):
                return '0.12.0' if path=='VERSION' else 'Prose\n'+a+'\n'+b
        seen={**self.api.rows[p],'body':'Prose\n'+b+'\n'+a}
        with self.assertRaisesRegex(s.Held,'Native child'):s.plan(Images(),self.base,p,seen)
    def test_inline_breaks_cannot_create_block_boundaries(self):
        for actual,expected in [('First<br /><br />-','First\n\n-'),('First<br />---','First\n---'),('First<br />1.','First\n1.')]:
            self.assertNotEqual(s.canonical(actual),s.canonical(expected))
    def test_authored_nonancestor_link_is_not_a_revision_marker(self):
        p=next(iter(s.GUIDES))
        class Authored(Source):
            def read(self,path,ref=None):
                if path=='VERSION':return '0.12.0'
                return '[Authored reference]('+s.REPO+'/blob/'+'c'*40+'/docs/example.md)'
        source=Authored();wanted=s.render(source,p,self.base)
        seen={**self.api.rows[p],**wanted}
        self.assertEqual(wanted,s.plan(source,self.base,p,seen))
    def test_only_the_qualified_legacy_paragraph_normalizes_soft_breaks(self):
        import json
        baseline=json.loads((s.ENGINE/'sync/baselines.json').read_text())['40f6d2e17f5681d68525d83503a457d5']['body']
        self.assertNotEqual(s.canonical(baseline),s.canonical(baseline.replace('<br />','\n')))
        for text in ['First<br />_ _ _','First<br />~~~']:
            self.assertNotEqual(s.canonical(text),s.canonical(text.replace('<br />','\n')))
    def test_inline_marker_shaped_citation_is_not_the_generated_footer(self):
        p=next(iter(s.GUIDES))
        class Citation(Source):
            def read(self,path,ref=None):
                if path=='VERSION':return '0.12.0'
                return 'An authored [Source revision aaaaaaa]('+s.REPO+'/blob/'+'c'*40+'/'+s.GUIDES[p]+') citation.'
        source=Citation();wanted=s.render(source,p,self.base)
        self.assertEqual(wanted,s.plan(source,self.base,p,{**self.api.rows[p],**wanted}))
    def test_legacy_exception_never_changes_tilde_fenced_literals(self):
        import json
        body=json.loads((s.ENGINE/'sync/baselines.json').read_text())['40f6d2e17f5681d68525d83503a457d5']['body']
        legacy=next(l for l in body.splitlines() if '<br />' in l)
        self.assertNotEqual(s.canonical('~~~\n'+legacy+'\n~~~'),s.canonical('~~~\n'+legacy.replace('<br />','\n')+'\n~~~'))
    def test_generated_marker_inside_unclosed_blocks_is_not_strict(self):
        p=next(iter(s.GUIDES));marker='[Source revision ccccccc]('+s.REPO+'/blob/'+'c'*40+'/'+s.GUIDES[p]+')'
        for prefix in ['~~~\n','<!--\n','<toggle>\n']:
            class Literal(Source):
                def read(self,path,ref=None):
                    return '0.12.0' if path=='VERSION' else prefix+'Example\n\n'+marker
            source=Literal();wanted=s.render(source,p,self.base)
            self.assertEqual(wanted,s.plan(source,self.base,p,{**self.api.rows[p],**wanted}))
    def test_hard_linebreak_spacing_and_blank_blocks_are_preserved(self):
        self.assertNotEqual(s.canonical('one  \ntwo'),s.canonical('one\ntwo'))
        self.assertNotEqual(s.canonical('one\n\n\ntwo'),s.canonical('one\n\ntwo'))
    def test_api_plain_source_labels_preserve_mcp_link_provenance(self):
        p=next(iter(s.TEMPLATES));url='https://github.com/accepted'
        self.base[p]['source']=f'Frozen source: [{url}]({url})'
        seen={**self.api.rows[p],'source':'Frozen source: '+url,'source_links':[{'text':url,'url':url}]}
        wanted=s.plan(self.source,self.base,p,seen)
        self.assertEqual(seen['source'],wanted['source'])
    def test_full_newer_render_is_held_without_trusting_a_marker(self):
        p=next(iter(s.GUIDES));seen={**self.api.rows[p],**s.render(self.source,p,self.base,'c'*40)}
        with self.assertRaises(s.Held):s.plan(self.source,self.base,p,seen)
    def test_public_markers_follow_visible_lists_and_code_text(self):
        lines=s.visible_lines('1. First step\n2. Next step\n\n```txt\n1. Literal code\n```')
        self.assertEqual(['firststep','nextstep','1literalcode'],lines)
    def test_public_markers_keep_prose_with_inline_backtick_span(self):
        self.assertEqual(['foosetsthemode'],s.visible_lines('```foo``` sets the mode'))
    def test_public_markers_handle_tilde_and_longer_fences(self):
        self.assertEqual(['1literal','2other','next'],s.visible_lines('~~~txt\n1. Literal\n~~~\n````txt\n```\n2. Other\n````\n1) Next'))
    def test_unclosed_code_fence_does_not_strip_literal_numbers(self):
        self.assertEqual(['3literal'],s.visible_lines('```txt\n3. Literal'))
    def test_newer_or_unrelated_live_revision_is_not_downgraded(self):
        p=next(iter(s.GUIDES));self.api.rows[p]['body'] += '\n['+'newer'+']('+s.REPO+'/blob/'+'c'*40+'/docs/setup.md)'
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True)
        self.assertEqual([], self.api.calls)
    def test_structural_change_is_not_whitespace_equivalent(self):
        self.assertNotEqual(s.canonical('## Title\n\nA paragraph'),s.canonical('## Title A paragraph'))
        self.assertNotEqual(s.canonical('one<br />two'),s.canonical('one\ntwo'))
        self.assertNotEqual(s.canonical('```\none<br />two\n```'),s.canonical('```\none\ntwo\n```'))
    def test_unbound_private_page_is_refused_before_transport(self):
        api=object.__new__(s.API)
        with self.assertRaises(s.Held):api.request('GET','pages/'+'f'*32)
    def test_source_property_edit_is_not_overwritten(self):
        self.api.rows[next(iter(s.TEMPLATES))]['source']='Owner edited this source property'
        with self.assertRaises(s.Held):s.reconcile(self.api,self.source,self.base,write=True)
        self.assertEqual([],self.api.calls)
    def test_write_limit_is_checked_before_mutation(self):
        with self.assertRaises(s.Held):s.reconcile(self.api,self.source,self.base,write=True,max_writes=1)
        self.assertEqual([],self.api.calls)
    def test_file_reference_change_holds_the_whole_set(self):
        page=next(iter(s.TEMPLATES))
        self.api.rows[page]['body']=self.api.rows[page]['body'].replace('source.zip','different.zip')
        with self.assertRaises(s.Held):s.reconcile(self.api,self.source,self.base,write=True)
        self.assertEqual([],self.api.calls)


if __name__ == '__main__':
    unittest.main()
