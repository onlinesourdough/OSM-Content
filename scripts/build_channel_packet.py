#!/usr/bin/env python3
"""Build the portable catalogue projection from one exact public source commit."""
import argparse
import gzip
import hashlib
import io
import json
import posixpath
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

REPO = 'https://github.com/onlinesourdough/OSM-Content'
FILES = {
    'SKILL.md': 'templates/content-channel/SKILL.md',
    'references/adaptation.md': 'templates/content-channel/references/adaptation.md',
    'references/channel-skills.md': 'docs/channel-skills.md',
    'references/quality-gate.md': 'templates/channel-quality-gate/SKILL.md',
    'references/schedule.md': 'templates/content-schedule/SKILL.md',
    'references/release-contract.md': 'templates/content-produce/references/release-contract.md',
    'references/gate-prompts.md': 'templates/knowledge-entries/quality-gate.md',
    'references/setup.md': 'docs/setup.md',
    'references/configuration.md': 'docs/configuration.md',
    'references/post-workflow.md': 'docs/post-workflow.md',
    'references/reference-library.md': 'docs/reference-library.md',
    'references/writing-voice.md': 'docs/writing-voice.md',
    'references/voice-profile.md': 'templates/knowledge-entries/voice-profile.md',
    'references/red-thread.md': 'templates/knowledge-entries/red-thread.md',
    'references/channel-format.md': 'templates/knowledge-entries/channel-format.md',
    'references/cadence.md': 'templates/knowledge-entries/cadence.md',
    'references/setup-interview.md': 'templates/knowledge-entries/setup-interview.md',
    'LICENSE': 'LICENSE',
}


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root)


def build(root, ref):
    ref = git(root, 'rev-parse', '--verify', ref + '^{commit}').decode().strip()
    if not re.fullmatch('[0-9a-f]{40}', ref):
        raise ValueError('An exact source commit is required')
    reverse = {v: k for k, v in FILES.items()}
    result, sources = {}, {}
    for target, source in FILES.items():
        original = git(root, 'show', ref + ':' + source)
        sources[source] = hashlib.sha256(original).hexdigest()
        text = original.decode()

        def link(match):
            label, href = match.groups()
            if re.match(r'[a-z][a-z0-9+.-]*:', href, re.I) or href.startswith('#'):
                return match[0]
            path, sep, fragment = href.partition('#')
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
            if resolved.startswith('../') or resolved.startswith('/'):
                raise ValueError('A resource link leaves the selected repository')
            if resolved in reverse:
                mapped = posixpath.relpath(reverse[resolved], posixpath.dirname(target) or '.')
                return f'[{label}]({mapped}{sep}{fragment})'
            # Optional examples remain exact public source links, never guessed local files.
            kind = 'tree' if not posixpath.splitext(resolved)[1] else 'blob'
            return f'[{label}]({REPO}/{kind}/{ref}/{resolved}{sep}{fragment})'

        if target.endswith('.md'):
            text = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, text)
        result[target] = text.encode()
    result['SOURCE.json'] = (json.dumps({
        'kind': 'generated portable public template; not an installed personal workflow',
        'source_repository': REPO,
        'source_commit': ref,
        'template': 'content-channel',
        'source_files': sources,
        'resource_projection': FILES,
        'transformation': 'Only relative Markdown links are mapped to included resources or exact public source links.',
    }, indent=2, sort_keys=True) + '\n').encode()
    return result


def archives(files):
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        for name, content in sorted(files.items()):
            entry = tarfile.TarInfo(name)
            entry.size, entry.mode, entry.mtime = len(content), 0o644, 0
            archive.addfile(entry, io.BytesIO(content))
    compressed = io.BytesIO()
    with gzip.GzipFile(filename='', mode='wb', fileobj=compressed, mtime=0) as stream:
        stream.write(raw.getvalue())
    tar = compressed.getvalue()
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system, entry.external_attr = 3, 0o100644 << 16
            entry.compress_type = zipfile.ZIP_STORED
            archive.writestr(entry, content)
    return tar, out.getvalue()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-root', default=str(Path(__file__).resolve().parents[1]))
    p.add_argument('--source-ref', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    files = build(args.source_root, args.source_ref)
    tar, zipped = archives(files)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'content-channel-v0.14.0.tar.gz').write_bytes(tar)
    (out / 'content-channel-v0.14.0-template.zip').write_bytes(zipped)
    (out / 'packet-manifest.json').write_text(json.dumps({
        'tar_sha256': hashlib.sha256(tar).hexdigest(),
        'zip_sha256': hashlib.sha256(zipped).hexdigest(),
        'files': {k: hashlib.sha256(v).hexdigest() for k, v in sorted(files.items())},
    }, indent=2) + '\n')
    print(json.dumps({'files': len(files), 'tar_bytes': len(tar), 'zip_bytes': len(zipped)}))


if __name__ == '__main__':
    main()
