#!/usr/bin/env python3
"""Check local Markdown, HTML, and JSON file references in the recreation pack.

Run from any directory: python3 suno_recreation/evidence/check_references.py
The check resolves the current workspace, including ignored local evidence assets;
a fresh clone may lack those untracked audio/image assets.
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

PACK = Path(__file__).resolve().parents[1]
REPO = PACK.parent
TEXT_SUFFIXES = {'.md', '.html', '.json'}
PATH_KEYS = {'repository_file', 'current_file', 'plot', 'audio', 'output', 'path'}
MD_LINK = re.compile(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)')


def local_target(raw: str) -> str | None:
    raw = unquote(raw.strip())
    if not raw or raw.startswith('#'):
        return None
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc:
        return None
    return parsed.path


def candidates(ref: str, base: Path) -> list[Path]:
    path = Path(ref)
    if path.is_absolute():
        return [path]
    choices = [base / path, REPO / path, PACK / path]
    if ref.startswith('suno_recreation/'):
        choices.append(REPO / path)
    elif ref.startswith('evidence/') or ref.startswith('tracks/') or ref.startswith('source_videos/'):
        choices.append(PACK / path)
    return choices


def exists_ref(ref: str, base: Path) -> bool:
    return any(p.exists() for p in candidates(ref, base))


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__(); self.refs: list[str] = []
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                self.refs.append(value)


def walk_json(value, base: Path, where: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in PATH_KEYS and isinstance(child, str):
                ref = local_target(child)
                # Job output fields describe files a later inference run will
                # create. Validate their parent directory, not the not-yet-run output.
                output_ok = key == 'output' and ref and any(p.parent.is_dir() for p in candidates(ref, base))
                if ref and not output_ok and not exists_ref(ref, base):
                    errors.append(f'{where}: missing JSON {key} reference {child!r}')
            walk_json(child, base, where, errors)
    elif isinstance(value, list):
        for child in value:
            walk_json(child, base, where, errors)


def main() -> int:
    errors: list[str] = []
    files = [p for p in PACK.rglob('*') if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES]
    for file in files:
        try:
            text = file.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        if file.suffix.lower() == '.md':
            for match in MD_LINK.finditer(text):
                raw = match.group(1) or match.group(2) or ''
                ref = local_target(raw)
                if ref and not exists_ref(ref, file.parent):
                    line = text.count('\n', 0, match.start()) + 1
                    errors.append(f'{file.relative_to(REPO)}:{line}: missing Markdown reference {raw!r}')
        elif file.suffix.lower() == '.html':
            parser = Links(); parser.feed(text)
            for raw in parser.refs:
                ref = local_target(raw)
                if ref and not exists_ref(ref, file.parent):
                    errors.append(f'{file.relative_to(REPO)}: missing HTML reference {raw!r}')
        elif file.suffix.lower() == '.json':
            try:
                walk_json(json.loads(text), file.parent, str(file.relative_to(REPO)), errors)
            except json.JSONDecodeError as e:
                errors.append(f'{file.relative_to(REPO)}: invalid JSON ({e})')
    if errors:
        print('\n'.join(errors)); print(f'FAILED: {len(errors)} reference error(s) across {len(files)} text files.')
        return 1
    print(f'PASS: local references resolve across {len(files)} Markdown/HTML/JSON files.')
    print('Scope: current workspace, including ignored local evidence; a fresh clone may not contain ignored audio/image assets.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
