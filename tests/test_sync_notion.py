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
        self.property_failure = False
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
    def write_body(self, page, body):
        self.calls.append(('body', page));self.write_requests += 1
        if self.reject:
            raise OSError('rejected')
        self.rows[page]['body'] = body
        self.rows[page]['edited'] = 'new'
        if self.lost_answer:
            raise OSError('answer lost after applied')
    def write_source(self, page, value):
        self.calls.append(('source', page));self.write_requests += 1
        if self.property_failure:
            raise OSError('source property not applied')
        self.rows[page]['source'] = value


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
    def test_partial_body_property_write_can_resume(self):
        selected = next(iter(s.TEMPLATES));self.api.property_failure = True
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True, only=selected)
        self.api.property_failure = False;self.api.calls.clear()
        s.reconcile(self.api, self.source, self.base, write=True, only=selected)
        self.assertEqual([('source', selected)], self.api.calls)
    def test_newer_or_unrelated_live_revision_is_not_downgraded(self):
        p=next(iter(s.GUIDES));self.api.rows[p]['body'] += '\n['+'newer'+']('+s.REPO+'/blob/'+'c'*40+'/docs/setup.md)'
        with self.assertRaises(s.Held):s.reconcile(self.api, self.source, self.base, write=True)
        self.assertEqual([], self.api.calls)
    def test_structural_change_is_not_whitespace_equivalent(self):
        self.assertNotEqual(s.canonical('## Title\n\nA paragraph'),s.canonical('## Title A paragraph'))
        self.assertEqual(s.canonical('one<br />two'),s.canonical('one\ntwo'))
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
