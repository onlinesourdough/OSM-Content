#!/usr/bin/env python3
"""Validate the method source and optionally compare saved Notion projections."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()




def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notion-snapshots', type=Path,
                        help='JSON: page id -> {page_id, body, read_at, reader}; compares supplied reads, not network access')
    parser.add_argument('--source-ref', default='HEAD', help='Exact Git revision represented by supplied snapshots')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'release.json').read_text())
    errors = []
    version = (ROOT / 'VERSION').read_text().strip()
    if manifest['method_version'] != version:
        errors.append('VERSION differs from method_version')
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        errors.append('Invalid method version')
    tag = os.environ.get('GITHUB_REF', '')
    if tag.startswith('refs/tags/') and tag != 'refs/tags/v' + version:
        errors.append('Release tag differs from VERSION')
    declared = manifest['source_sha256']
    actual_paths = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
                    if p.is_file() and not set(p.relative_to(ROOT).parts) &
                    {'.git', 'dist', '__pycache__', '.DS_Store'}
                    and p.name != 'release.json'}
    if set(declared) != actual_paths:
        errors.append('Source inventory differs: ' + str(sorted(set(declared) ^ actual_paths)))
    for name, expected in declared.items():
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append('Missing or unsafe source: ' + name)
        elif digest(path) != expected:
            errors.append('Source hash differs: ' + name)
    for name in sorted(actual_paths):
        path = ROOT / name
        if path.suffix != '.md':
            continue
        for linked_version in (re.findall(r'OSM-Content/(?:blob|releases/tag)/v(\d+\.\d+\.\d+)', path.read_text())
                               if name in {'README.md', 'docs/guide.notion.md'} else []):
            if linked_version != version:
                errors.append('Stale method-version link: ' + name)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', path.read_text()):
            if urlsplit(href).scheme or href.startswith('#'):
                continue
            target = (path.parent / unquote(href.split('#')[0])).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {href}')
    provenance = json.loads((ROOT / 'provenance.json').read_text())
    # In a source checkout, anchor the unchanged import to its historical commit.
    # A source archive has no Git history; its result explicitly records that limit.
    anchor_checked = False
    if (ROOT / '.git').exists():
        anchor = manifest['template_import_commit']
        try:
            original = subprocess.check_output(['git', 'show', anchor + ':provenance.json'], cwd=ROOT)
            if original != (ROOT / 'provenance.json').read_bytes():
                errors.append('Import provenance differs from historical commit')
            names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', anchor, 'templates'], cwd=ROOT, text=True).splitlines()
            for name in names:
                if not (ROOT / name).is_file() or subprocess.check_output(['git', 'show', anchor + ':' + name], cwd=ROOT) != (ROOT / name).read_bytes():
                    errors.append('Template import differs from historical commit: ' + name)
            current_names = {str(p.relative_to(ROOT)) for p in (ROOT / 'templates').rglob('*') if p.is_file()}
            if current_names != set(names):
                errors.append('Template import file set differs from historical commit')
            anchor_checked = True
        except subprocess.CalledProcessError:
            errors.append('Historical import unavailable; fetch full Git history before checking this checkout')
    for template in provenance['templates']:
        for name, expected in template['files'].items():
            path = ROOT / template['path'] / name
            if not path.is_file() or digest(path) != expected:
                errors.append(f'Frozen template changed: {template["name"]}/{name}')
    targets = manifest['notion_targets']
    ids = [item['page_id'] for item in targets]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate Notion target')
    for item in targets:
        if item.get('source') and item['source'] not in declared:
            errors.append('Unlisted projection source: ' + item['source'])
        if item.get('template') and item['template'] not in {t['name'] for t in provenance['templates']}:
            errors.append('Unknown template target: ' + item['template'])
    compared_pages = []
    if args.notion_snapshots:
        from sync_notion import Source, render, canonical
        source = Source(ROOT, args.source_ref)
        baselines = json.loads((ROOT / 'sync/baselines.json').read_text())
        snapshots = json.loads(args.notion_snapshots.read_text())
        for item in targets:
            if not item.get('source'):
                continue
            readback = snapshots.get(item['page_id'])
            saved = readback.get('body') if isinstance(readback, dict) else None
            expected = render(source, item['page_id'], baselines)['body']
            if saved is None or readback.get('page_id') != item['page_id'] or not readback.get('read_at') or not readback.get('reader'):
                errors.append('Missing supplied readback or identity/provenance: ' + item['page_id'])
                continue
            # Preserve paragraphs, lists, headings and tables; trim trailing space only.
            if canonical(saved) != canonical(expected):
                errors.append('Saved projection differs: ' + item['page_id'])
            fences = lambda s: re.findall(r'```[^\n]*\n(.*?)```', s, re.S)
            if [s.strip() for s in fences(saved)] != [s.strip() for s in fences(expected)]:
                errors.append('Saved code block differs: ' + item['page_id'])
            compared_pages.append(item['page_id'])
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(json.dumps({'method_version': version, 'source_files': len(declared),
                      'frozen_templates': len(provenance['templates']),
                      'historical_import_checked': anchor_checked,
                      'mapped_notion_pages': len(targets),
                      'provided_readbacks_compared': compared_pages,
                      'template_page_readbacks_not_compared': [x['page_id'] for x in targets if x.get('template')],
                      'anonymous_public_checked': False}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
