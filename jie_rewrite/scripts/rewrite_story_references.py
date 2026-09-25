"""Rewrite concrete historical manuscript paths using the reviewed migration map."""
from __future__ import annotations
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote, quote

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT/'docs/STORY_STRUCTURE.json').read_text(encoding='utf-8'))
    aliases = data['legacy_aliases']
    original_sources = {c['source']:c['legacy_source'] for g in data['groups'] for c in g['chapters']}
    groups = data['groups']
    directory_targets = {}
    for old,new in aliases.items():
        directory_targets.setdefault(old.rsplit('/',1)[0],set()).add(new.rsplit('/',1)[0])
    directory_map = {old: next(iter(dest))+'/README.md' if len(dest)==1 else 'docs/STORY_STRUCTURE.md'
                     for old,dest in directory_targets.items()}
    directory_map.update({'novel/lower_realm_v2':'novel/第一時期：下界成根/README.md',
                         'novel/published/lower_realm_v2':'novel/published/第一時期：下界成根/README.md',
                         'novel/published/upper_realm_v2':'novel/published/第二時期：上界成道/README.md'})
    old_file_to_new = {**aliases}
    for directory,dest in directory_map.items():
        old_file_to_new[directory+'/README.md'] = dest
        old_file_to_new[directory+'/SOURCE_MANIFEST.md'] = 'docs/STORY_STRUCTURE.md'
        old_file_to_new[directory+'/CONTINUITY_PLAN.md'] = 'docs/STORY_STRUCTURE.md'
    origin = f"https://github.com/LarryTsai/Bearer-of-Calamity/blob/{data['baseline_commit']}/jie_rewrite/"
    retired_prefixes = ('novel/volume03a/','novel/volume04/','novel/published/volume03a/',
                        'novel/published/volume04/','novel/drafts/','novel/work_in_progress/')
    for old in data.get('retired_files',[]):
        old_file_to_new[old] = origin+quote(old,safe='/')
    changed = 0
    # Only concrete file links can be relocated without guessing chapter-range semantics.
    for path in sorted(ROOT.rglob('*.md')):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(('docs/archive/','docs/author_directives/','.claude/')):
            continue
        if any(rel.startswith(p) for p in retired_prefixes):
            continue
        if rel in aliases or rel in data.get('retired_files',[]):
            continue
        raw = path.read_bytes()
        text = raw.decode('utf-8-sig')
        original = text
        def link(match):
            label, target = match.groups()
            if re.match(r'^(?:https?:|mailto:|#)',target):
                return match[0]
            bare,sep,anchor = target.strip('<>').partition('#')
            prior_parent = (ROOT/original_sources[rel]).parent if rel in original_sources else path.parent
            old = (prior_parent/unquote(bare)).resolve()
            try:
                oldrel = old.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                return match[0]
            dest = old_file_to_new.get(oldrel) or directory_map.get(oldrel)
            if not dest:
                return match[0]
            newtarget = dest if dest.startswith('https:') else Path(os.path.relpath(ROOT/dest,path.parent)).as_posix()
            return f'[{label}]({quote(newtarget,safe="/:%")}{sep+anchor if sep else ""})'
        text = re.sub(r'\[([^\]\n]*)\]\(([^)\n]+)\)',link,text)
        # Backtick paths are project-root paths or unambiguous novel-relative paths.
        def code_path(match):
            content = match[1]
            trailing = content.endswith('/')
            value = content.rstrip('/')
            dest = old_file_to_new.get(value) or directory_map.get(value)
            if dest is None and not value.startswith(('novel/','docs/')):
                dest = old_file_to_new.get('novel/'+value) or directory_map.get('novel/'+value)
            if dest is None:
                return match[0]
            if dest.startswith('https:'):
                return f'[歷史素材]({dest})'
            return '`'+dest+'`'
        text = re.sub(r'`([^`\n]+)`',code_path,text)
        if text != original:
            path.write_bytes((b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'')+text.encode('utf-8'))
            changed += 1
    print(f'Updated concrete links and code paths in {changed} Markdown files.')


if __name__ == '__main__':
    main()
