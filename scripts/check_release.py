#!/usr/bin/env python3
"""Validate the method source and optionally compare saved Notion projections."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render_notion(path, tag):
    """Resolve local Markdown links against the frozen source, retaining native tags."""
    body = path.read_text()
    def rewrite(match):
        label, href = match.groups()
        if urlsplit(href).scheme or href.startswith('#'):
            return match.group(0)
        relative, separator, fragment = href.partition('#')
        target = (path.parent / unquote(relative)).resolve().relative_to(ROOT)
        suffix = '#' + fragment if separator else ''
        return f'[{label}](https://github.com/onlinesourdough/OSM-Content/blob/{tag}/{target}{suffix})'
    return re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', rewrite, body).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notion-snapshots', type=Path,
                        help='JSON of exact mapped page ids to saved body strings')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'release.json').read_text())
    errors = []
    version = (ROOT / 'VERSION').read_text().strip()
    if manifest['method_version'] != version:
        errors.append('VERSION differs from method_version')
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
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', path.read_text()):
            if urlsplit(href).scheme or href.startswith('#'):
                continue
            target = (path.parent / unquote(href.split('#')[0])).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {href}')
    provenance = json.loads((ROOT / 'provenance.json').read_text())
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
    if args.notion_snapshots:
        snapshots = json.loads(args.notion_snapshots.read_text())
        for item in targets:
            if not item.get('source'):
                continue
            saved = snapshots.get(item['page_id'])
            expected = render_notion(ROOT / item['source'], 'v' + version)
            if saved is None:
                errors.append('Missing saved page: ' + item['page_id'])
                continue
            # Notion may reflow prose; compare all tokens and code payloads separately.
            if ' '.join(saved.split()) != ' '.join(expected.split()):
                errors.append('Saved projection differs: ' + item['page_id'])
            fences = lambda s: re.findall(r'```[^\n]*\n(.*?)```', s, re.S)
            if [s.strip() for s in fences(saved)] != [s.strip() for s in fences(expected)]:
                errors.append('Saved code block differs: ' + item['page_id'])
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(json.dumps({'method_version': version, 'source_files': len(declared),
                      'frozen_templates': len(provenance['templates']),
                      'mapped_notion_pages': len(targets),
                      'saved_projection_checked': bool(args.notion_snapshots)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
