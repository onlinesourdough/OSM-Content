import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import tarfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
def module(name, path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result
b=module('packet','scripts/build_channel_packet.py')
s=module('sync_packet','scripts/sync_notion.py')

class PacketTests(unittest.TestCase):
    def test_archive_roundtrip_and_reproducibility(self):
        files=b.build(ROOT,'HEAD')
        first=b.archives(files);self.assertEqual(first,b.archives(files))
        with tarfile.open(fileobj=io.BytesIO(first[0]),mode='r:gz') as archive:
            self.assertTrue(all(m.isfile() and m.mode==0o644 for m in archive))
            self.assertEqual(files,{m.name:archive.extractfile(m).read() for m in archive})
        with zipfile.ZipFile(io.BytesIO(first[1])) as archive:
            self.assertEqual(files,{n:archive.read(n) for n in archive.namelist()})
        self.assertEqual(19,len(files))
    def test_portable_relative_links_resolve_inside_packet(self):
        files=b.build(ROOT,'HEAD')
        import posixpath
        for name,data in files.items():
            if not name.endswith('.md'):continue
            for href in re.findall(r'\[[^\]]+\]\(([^\s)]+)\)',data.decode()):
                if re.match(r'[a-z][a-z0-9+.-]*:',href,re.I) or href.startswith('#'):continue
                target=posixpath.normpath(posixpath.join(posixpath.dirname(name),href.split('#')[0]))
                self.assertIn(target,files,(name,href))
    def test_manifest_provenance_hashes_unmodified_sources(self):
        files=b.build(ROOT,'HEAD');meta=json.loads(files['SOURCE.json'])
        for path,expected in meta['source_files'].items():
            self.assertEqual(expected,hashlib.sha256(b.git(ROOT,'show',meta['source_commit']+':'+path)).hexdigest())
    def test_cross_repo_and_private_targets_never_reach_transport(self):
        api=object.__new__(s.API)
        for page in ['a'*32,'40d6d2e17f568124af82ceb93dabf77a','3fe6d2e17f568160996bcab0f9d6e196']:
            with self.assertRaises(s.Held):api.request('PATCH','pages/'+page,{})
    def test_identity_requires_exact_key_area_and_draft(self):
        page=next(iter(s.CURRENT_TEMPLATES))
        props={'Key':{'type':'rich_text','rich_text':[{'plain_text':'content-draft:content-channel'}]},'Area':{'select':{'name':'Optional Content'}},'Status':{'select':{'name':'Draft'}}}
        s.verify_current_identity(page,props)
        for field,value in [('Area','Work'),('Status','Released reference')]:
            bad=copy.deepcopy(props);bad[field]['select']['name']=value
            with self.assertRaises(s.Held):s.verify_current_identity(page,bad)
        bad=copy.deepcopy(props);bad['Key']['rich_text'][0]['plain_text']='osm:core'
        with self.assertRaises(s.Held):s.verify_current_identity(page,bad)
    def test_cleared_identity_fields_hold_explicitly(self):
        page=next(iter(s.CURRENT_TEMPLATES))
        for props in [{}, {'Key':None}, {'Area':{'select':None},'Status':{'select':None}}, {'Key':{'type':'rich_text','rich_text':None}}]:
            with self.assertRaises(s.Held):s.verify_current_identity(page,props)

    def test_actual_current_sources_match_the_native_packet_handoff(self):
        base=json.loads((ROOT/'sync/baselines.json').read_text())
        s.verify_current_inputs(s.Source(ROOT,'HEAD'),base)
        handoff=base[next(iter(s.CURRENT_TEMPLATES))]
        self.assertEqual(handoff['packet_sha256'],hashlib.sha256(b.archives(b.build(ROOT,handoff['packet_source_commit']))[1]).hexdigest())

    def test_changed_packet_inputs_require_new_handoff(self):
        page=next(iter(s.CURRENT_TEMPLATES));data='existing procedure'
        class Source:
            def read(self,path):return data
        base={page:{'packet_inputs_sha256':{'SKILL.md':s.sha(data)}}}
        s.verify_current_inputs(Source(),base)
        base[page]['packet_inputs_sha256']['SKILL.md']=s.sha('changed procedure')
        with self.assertRaises(s.Held):s.verify_current_inputs(Source(),base)
        with self.assertRaises(s.Held):s.verify_current_inputs(Source(),{page:{}})

if __name__=='__main__':unittest.main()
