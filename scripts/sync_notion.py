#!/usr/bin/env python3
"""Reconcile the eight public Content pages through OSM's public-only publisher."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

ENGINE = Path(__file__).resolve().parents[1]
CORE_COMMIT = 'caedb13fde5fc33315f97d4875e7a76e379b1737'
PUBLIC = 'https://gustavanderson.notion.site/'
REPO = 'https://github.com/onlinesourdough/OSM-Content'
GUIDES = {
    '40d6d2e17f5681219a81e13317a19339': 'docs/guide.notion.md',
    '40f6d2e17f56819ea683f45a30072086': 'docs/setup.md',
    '40f6d2e17f5681d68525d83503a457d5': 'docs/configuration.md',
}
TEMPLATES = {
    '40d6d2e17f5681578925cdc0774c6db5': 'content-setup',
    '40d6d2e17f5681c99020d85e3bc1ff4b': 'content-intake',
    '40d6d2e17f568141a2c9efa2d04c9268': 'content-prepare',
    '40d6d2e17f568122aa82f1dcf83500a7': 'content-produce',
    '40d6d2e17f5681c784c4d545814fd7a5': 'content-learn',
}
ALLOWED = set(GUIDES) | set(TEMPLATES)
SOURCE_NOTE = 'The v0.10.0 packet is a frozen export of public template edition 2026-11-05.1.'


class Held(RuntimeError):
    pass


def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()


def canonical(body):
    """Qualified soft-linebreak representation, preserving blocks and fenced code."""
    pieces = body.replace('\r\n', '\n').replace('\r', '\n').split('```')
    for i in range(0, len(pieces), 2):
        pieces[i] = pieces[i].replace('<br />', '\n')
        pieces[i] = re.sub(r'\n{3,}', '\n\n', '\n'.join(line.rstrip() for line in pieces[i].split('\n')))
    return '```'.join(pieces).strip()


def protected(body):
    return Counter(re.findall(r'<(?:page|database|file|pdf|image)\b[^>]*>', canonical(body)))


class Source:
    def __init__(self, root, ref):
        self.root = Path(root).resolve()
        self.ref = self.git('rev-parse', '--verify', ref + '^{commit}').strip()
        if not re.fullmatch(r'[0-9a-f]{40}', self.ref):
            raise Held('Source is not an exact commit')

    def git(self, *args):
        result = subprocess.run(['git', *args], cwd=self.root, capture_output=True, text=True)
        if result.returncode:
            raise Held('Required source revision is unavailable')
        return result.stdout

    def read(self, path, ref=None):
        return self.git('show', (ref or self.ref) + ':' + path)

    def ancestor(self, ref):
        return bool(re.fullmatch(r'[0-9a-f]{40}', ref)) and subprocess.run(
            ['git', 'merge-base', '--is-ancestor', ref, self.ref], cwd=self.root,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def source_property(name, ref, version):
    return (f'Frozen v0.10.0 Draft template, imported edition 2026-11-05.1. '
            f'Source: {REPO}/blob/{ref}/templates/{name}/SKILL.md . '
            f'Shared method: {version}. Original ZIP hashes and history retained; not a native personal installation.')


def note(name, ref, version):
    return (SOURCE_NOTE + ' Its files, hashes and earlier history are retained. '
            f'[Template source]({REPO}/blob/{ref}/templates/{name}/SKILL.md) lives in the separate OSM Content repository. '
            '[Current Content guide](https://app.notion.com/p/40d6d2e17f5681219a81e13317a19339) '
            f'and [short-post workflow]({REPO}/blob/{ref}/docs/post-workflow.md) describe the shared method. '
            f'Method {version} does not change this template\'s version or install a personal skill.')


def render(source, page_id, baselines, ref=None):
    ref = ref or source.ref
    version = source.read('VERSION', ref).strip()
    if page_id in GUIDES:
        path = GUIDES[page_id]
        body = source.read(path, ref)
        def link(match):
            label, href = match.groups()
            if urllib.parse.urlsplit(href).scheme or href.startswith('#'):
                # Pin source links for this repository; release links retain their own meaning.
                href = re.sub(re.escape(REPO) + r'/blob/(?:main|v' + re.escape(version) + r')/', REPO + '/blob/' + ref + '/', href)
                return f'[{label}]({href})'
            file, sep, fragment = href.partition('#')
            resolved = (Path(path).parent / file).as_posix()
            import posixpath
            resolved = posixpath.normpath(resolved)
            if resolved.startswith('../'):
                raise Held('A source link leaves the repository')
            return f'[{label}]({REPO}/blob/{ref}/{resolved}' + (sep + fragment if sep else '') + ')'
        body = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, body)
        body = canonical(body) + f'\n\n[Source revision {ref[:7]}]({REPO}/blob/{ref}/{path})'
        return {'body': body, 'source': None}
    name = TEMPLATES[page_id]
    baseline = baselines[page_id]
    old = next((p for p in baseline['body'].split('\n\n') if p.startswith(SOURCE_NOTE)), None)
    if not old or baseline['body'].count(old) != 1:
        raise Held('Template handoff does not contain exactly one source note')
    body = baseline['body'].replace(old, note(name, ref, version))
    return {'body': canonical(body), 'source': source_property(name, ref, version)}


def candidates(source, seen, baselines, page_id):
    """Recognize the explicit handoff or a reproducible earlier ancestor; never trust a marker alone."""
    if page_id in GUIDES:
        refs = set(re.findall(r'\[Source revision [0-9a-f]{7}\]\(' + re.escape(REPO) + r'/blob/([0-9a-f]{40})/' + re.escape(GUIDES[page_id]) + r'\)', seen['body']))
    else:
        refs = set(re.findall(r'\[Template source\]\(' + re.escape(REPO) + r'/blob/([0-9a-f]{40})/templates/' + re.escape(TEMPLATES[page_id]) + r'/SKILL\.md\)', seen['body']))
        refs.update(re.findall(r'Source: ' + re.escape(REPO) + r'/blob/([0-9a-f]{40})/templates/' + re.escape(TEMPLATES[page_id]) + r'/SKILL\.md', seen['source'] or ''))
    states = [baselines[page_id]]
    for ref in refs:
        if not source.ancestor(ref):
            raise Held('Live page names a newer or unrelated source; refusing downgrade')
        states.append(render(source, page_id, baselines, ref))
    return states


def plan(source, baselines, page_id, seen):
    wanted = render(source, page_id, baselines)
    states = candidates(source, seen, baselines, page_id) + [wanted]
    if not any(canonical(s['body']) == canonical(seen['body']) for s in states):
        raise Held('Live body differs from the handoff and reproducible accepted source')
    if page_id in TEMPLATES and seen['source'] not in {s['source'] for s in states}:
        raise Held('Template Source property has an unrecognized edit')
    if protected(seen['body']) != protected(wanted['body']):
        raise Held('Native child, catalogue, media or file references would change')
    return wanted


class API:
    def __init__(self, pub):
        self.pub = pub
        self.transport = pub.NotionTransport(None, bound={})
        self.last = 0
        self.write_requests = 0

    def request(self, method, path, payload=None):
        match = re.fullmatch(r'pages/([0-9a-f]{32})(/markdown(?:\?markdown_version=v2)?)?', path)
        if not match or match[1] not in ALLOWED or method not in {'GET', 'PATCH'}:
            raise Held('Request outside the eight public Content pages')
        time.sleep(max(0, 0.4 - (time.monotonic() - self.last)))
        self.last = time.monotonic()
        if method == 'PATCH':
            self.write_requests += 1
        return self.transport._request(method, path, payload, version='2026-03-11')

    def read(self, page_id):
        page = self.request('GET', 'pages/' + page_id)
        body = self.request('GET', 'pages/' + page_id + '/markdown?markdown_version=v2')
        if page.get('id', '').replace('-', '') != page_id or page.get('in_trash') or page.get('archived'):
            raise Held('Wrong or archived Notion identity')
        if (body.get('object') != 'page_markdown' or body.get('id', '').replace('-', '') != page_id
                or body.get('truncated') is not False or body.get('unknown_block_ids') != [] or body.get('warnings')
                or not isinstance(body.get('markdown'), str)):
            raise Held('Incomplete or unsupported Notion Markdown read')
        props = page.get('properties', {})
        source = None
        if page_id in TEMPLATES:
            if props.get('Source', {}).get('type') != 'rich_text':
                raise Held('Template Source property is not the bound text field')
            source = ''.join(t.get('plain_text', t.get('text', {}).get('content', '')) for t in props['Source']['rich_text'])
        # All non-managed properties must remain unchanged. File URLs expire; compare their immutable path/name.
        def stable(value):
            if isinstance(value, dict):
                return {k: stable(v) for k, v in value.items() if k != 'expiry_time'}
            if isinstance(value, list):
                return [stable(v) for v in value]
            if isinstance(value, str) and value.startswith('https://prod-files-secure.s3.'):
                url = urllib.parse.urlsplit(value)
                return url.scheme + '://' + url.netloc + url.path
            return value
        intrinsic = stable({k: v for k, v in props.items()
                            if not (page_id in TEMPLATES and k == 'Source')
                            and v.get('type') not in {'last_edited_time', 'last_edited_by'}})
        return {'body': canonical(self.pub.stable_notion_media(body['markdown'])), 'source': source,
                'intrinsic': intrinsic, 'edited': page.get('last_edited_time'), 'files': props.get('Files', {}).get('files', [])}

    def verify_packet(self, page_id, seen, expected):
        name = TEMPLATES[page_id] + '-v0.10.0-template.zip'
        files = [f for f in seen['files'] if f.get('name') == name]
        if len(files) != 1:
            raise Held('Frozen template download is missing or ambiguous')
        url = files[0].get('file', {}).get('url', '')
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme != 'https' or parsed.netloc != 'prod-files-secure.s3.us-west-2.amazonaws.com':
            raise Held('Unrecognized template file provider')
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *args, **kwargs):
                return None
        try:
            # The Notion credential never enters this download request.
            with urllib.request.build_opener(NoRedirect()).open(url, timeout=30) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000 or hashlib.sha256(content).hexdigest() != expected:
                raise Held('Frozen template download hash differs')
        except Held:
            raise
        except Exception:
            raise Held('Frozen template download could not be verified') from None

    def write_body(self, page_id, body):
        result = self.request('PATCH', 'pages/' + page_id + '/markdown', {
            'type': 'replace_content', 'markdown_version': 'v2', 'allow_async': False,
            'replace_content': {'new_str': body, 'allow_deleting_content': False}})
        if result.get('warnings') or result.get('truncated') or result.get('unknown_block_ids'):
            raise Held('Notion changed or could not return the complete write')

    def write_source(self, page_id, value):
        if page_id not in TEMPLATES:
            raise Held('Source property belongs only to the five template pages')
        self.request('PATCH', 'pages/' + page_id, {'properties': {'Source': {'rich_text': [{'text': {'content': value}}]}}})


def equal(seen, wanted):
    return canonical(seen['body']) == canonical(wanted['body']) and seen['source'] == wanted['source']


def observation(seen):
    return {k: seen[k] for k in ['body', 'source', 'intrinsic', 'edited']}


def reconcile(api, source, baselines, *, write=False, only=None, max_writes=8, record=None):
    plans = []
    # Whole-set preflight precedes every write; a conflict holds the whole attempt.
    for page_id in GUIDES | TEMPLATES:
        seen = api.read(page_id)
        if page_id in TEMPLATES:
            api.verify_packet(page_id, seen, baselines[page_id]['packet_sha256'])
        wanted = plan(source, baselines, page_id, seen)
        plans.append({'page_id': page_id, 'seen': seen, 'wanted': wanted})
    selected = [p for p in plans if not equal(p['seen'], p['wanted']) and (only is None or p['page_id'] == only)]
    if len(selected) > max_writes:
        raise Held('More pages need changes than this invocation permits')
    outcomes = []
    for p in plans:
        page_id, before, wanted = p['page_id'], p['seen'], p['wanted']
        row = {'page_id': page_id, 'state': 'pending', 'before_body_sha256': sha(before['body']),
               'desired_body_sha256': sha(wanted['body'])}
        outcomes.append(row)
        if record:
            record(outcomes)
        if equal(before, wanted):
            state = 'unchanged'
        elif p not in selected or not write:
            state = 'prepared'
        else:
            current = api.read(page_id)
            if observation(current) != observation(before):
                raise Held('Page changed after preflight; rerun from the new observation')
            for component in ['body', 'source']:
                if (canonical(current['body']) == canonical(wanted['body']) if component == 'body' else current['source'] == wanted['source']):
                    continue
                try:
                    if component == 'body':
                        api.write_body(page_id, wanted['body'])
                    else:
                        api.write_source(page_id, wanted['source'])
                except Exception:
                    # No write retry. Read once to distinguish an applied write from unknown/not-applied.
                    after = api.read(page_id)
                    applied = canonical(after['body']) == canonical(wanted['body']) if component == 'body' else after['source'] == wanted['source']
                    if not applied:
                        raise Held('Write not confirmed; no retry was sent') from None
                    current = after
                else:
                    current = api.read(page_id)
                if current['intrinsic'] != before['intrinsic'] or protected(current['body']) != protected(before['body']):
                    raise Held('Native references or non-managed properties changed')
                if component == 'body' and canonical(current['body']) != canonical(wanted['body']):
                    raise Held('Saved body differs from desired source')
                if component == 'source' and current['source'] != wanted['source']:
                    raise Held('Saved Source property differs')
            if not equal(current, wanted):
                raise Held('Final whole-page readback differs')
            state = 'written'
        row['state'] = state
        if record:
            record(outcomes)
    return outcomes


def visible_lines(body):
    # Collapsed diagram bodies are not visible. Their exact native references are checked by the API path.
    body = re.sub(r'<toggle>\s*([^\n]+)[\s\S]*?</toggle>', r'\1', body)
    body = re.sub(r'<(?:file|pdf)\s+source="[^"]*name=([^"&]+)[^"]*"\s*/>', lambda m: urllib.parse.unquote(m[1]), body)
    body = re.sub(r'<[^>]+>', '', body)
    body = re.sub(r'\[([^\]]+)\]\([^\s)]+\)', r'\1', body)
    lines = [re.sub(r'[^\w]|_', '', line, flags=re.UNICODE).lower() for line in body.splitlines()]
    return [line for line in lines if line]


def public_check(core_root, source, baselines, *, runner=None, page_ids=None):
    sys.path.insert(0, str(Path(core_root) / 'docs-publisher'))
    from browser_reader import run_browser
    runner = runner or run_browser
    requests = []
    page_ids = list(page_ids or GUIDES | TEMPLATES)
    for page_id in page_ids:
        markers = [v[i:i+500] for v in visible_lines(render(source, page_id, baselines)['body']) for i in range(0, len(v), 500)]
        requests.append({'url': PUBLIC + page_id, 'markers': markers})
        if page_id == next(iter(GUIDES)):
            requests[-1]['entries'] = [{'page': p, 'title': name} for p, name in TEMPLATES.items()]
    payload = {'allowedUrls': [r['url'] for r in requests], 'requests': requests}
    env = {k: v for k, v in os.environ.items() if k in {'PATH', 'HOME', 'TMPDIR', 'CI', 'PLAYWRIGHT_BROWSERS_PATH', 'XDG_CACHE_HOME'}}
    result = runner(['node', str(Path(core_root) / 'docs-publisher/public-browser-read.mjs')],
                    input=json.dumps(payload), text=True, capture_output=True, timeout=285, env=env)
    if len(result.stdout.encode()) > 16_100_000:
        raise Held('Oversized anonymous browser result')
    data = json.loads(result.stdout)
    if result.returncode != 0 or data.get('ok') is not True or not isinstance(data.get('results'), list) or len(data['results']) != len(page_ids):
        raise Held('Anonymous Content readback held; inspect the public-only result')
    rows, seen = [], set()
    for item in data['results']:
        url = item.get('url')
        expected = next((r for r in requests if r['url'] == url), None)
        final = urllib.parse.urlsplit(item.get('finalUrl', ''))
        if not expected or url in seen or item.get('ok') is not True or final.scheme != 'https' or final.netloc != 'gustavanderson.notion.site':
            raise Held('Unrecognized public page observation')
        if expected.get('entries') and item.get('entries') != expected['entries']:
            raise Held('Public catalogue does not show the five bound templates')
        page_id = url.rsplit('/', 1)[-1]
        if not re.search(page_id + r'(?:/|$)', final.path.replace('-', '')):
            raise Held('Public page identity differs')
        shown = re.sub(r'[^\w]|_', '', item.get('text', ''), flags=re.UNICODE).lower()
        at = 0
        for marker in expected['markers']:
            found = shown.find(marker, at)
            if found < 0:
                raise Held('Public text does not contain the complete expected lines in order')
            at = found + len(marker)
        seen.add(url)
        rows.append({'page_id': page_id, 'verified_at': item.get('observedAt'), 'expected_lines': len(expected['markers'])})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', required=True, type=Path)
    parser.add_argument('--source-ref', required=True)
    parser.add_argument('--core-root', required=True, type=Path)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--only-page', choices=sorted(ALLOWED))
    parser.add_argument('--max-writes', type=int, default=8)
    parser.add_argument('--public-read', action='store_true')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = {'ok': False, 'api': [], 'public': [], 'confirmed_pages_written': 0, 'write_requests_sent': 0}
    api = None
    def checkpoint(rows):
        report['api'] = list(rows)
        report['write_requests_sent'] = api.write_requests
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2) + '\n')
    try:
        core_ref = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=args.core_root, text=True).strip()
        if core_ref != CORE_COMMIT:
            raise Held('Core public transport/reader is not the reviewed pinned revision')
        sys.path.insert(0, str(args.core_root / 'docs-publisher'))
        import publisher as pub
        baselines = json.loads((ENGINE / 'sync/baselines.json').read_text())
        source = Source(args.source_root, args.source_ref)
        manifest = json.loads(source.read('release.json'))
        mapping = {t['page_id']: t.get('source') or t.get('template') for t in manifest['notion_targets']}
        if len(manifest['notion_targets']) != 8 or mapping != GUIDES | TEMPLATES or manifest['format'] != 'osm-content-method-release/1':
            raise Held('Source changes the reviewed public target map')
        provenance = json.loads((ENGINE / 'provenance.json').read_text())
        if manifest['template_version'] != '0.10.0' or json.loads(source.read('provenance.json')) != provenance:
            raise Held('Frozen template provenance changed; a reviewed template-version handoff is required')
        for template in provenance['templates']:
            for path, expected in template['files'].items():
                if sha(source.read(template['path'] + '/' + path)) != expected:
                    raise Held('Frozen template instructions changed without a new handoff')
        # The live source is data only: do not execute its Python or workflow files here.
        report['source_commit'] = source.ref
        api = API(pub)
        report['api'] = reconcile(api, source, baselines, write=args.write,
                                  only=args.only_page, max_writes=args.max_writes, record=checkpoint)
        if args.public_read:
            report['public'] = public_check(args.core_root, source, baselines,
                                            page_ids=[args.only_page] if args.only_page else None)
        report['complete'] = all(r['state'] in {'written', 'unchanged'} for r in report['api'])
        report['scope'] = 'bounded-one-page' if args.only_page else 'whole-set'
        chosen = [r for r in report['api'] if not args.only_page or r['page_id'] == args.only_page]
        report['ok'] = all(r['state'] in {'written', 'unchanged'} for r in chosen) and (not args.public_read or len(report['public']) == len(chosen))
    except Exception as error:
        # Never print transport payloads, tokens, signed URLs or raw third-party exceptions.
        report['reason'] = str(error) if isinstance(error, Held) else 'Public documentation operation failed; no automatic write retry'
        report['error_kind'] = type(error).__name__
    report['confirmed_pages_written'] = sum(r['state'] == 'written' for r in report['api'])
    report['write_requests_sent'] = api.write_requests if api else 0
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
