"""Verify migration body preservation, unique coverage, and safe duplicate retirements."""
from __future__ import annotations
import json
from pathlib import Path
from migrate_story_structure import body, digest, safe_path

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT/'docs/STORY_STRUCTURE.json').read_text(encoding='utf-8'))
    chapters = [c for g in manifest['groups'] for c in g['chapters']]
    assert len({c['source'] for c in chapters}) == len(chapters)
    for c in chapters:
        source = safe_path(c['source']).read_text(encoding='utf-8-sig')
        published = safe_path(c['published']).read_text(encoding='utf-8-sig')
        assert digest(body(source).encode('utf-8')) == c['body_sha256'], c['source']
        assert body(source) == body(published), c['published']
        assert source.splitlines()[0] == published.splitlines()[0] == f"# 第{c['number']:03}章 {c['title']}"
    retired = []
    by_old = {c['legacy_source']:c for c in chapters}
    current_chapter_paths = {c[k] for c in chapters for k in ('source','published')}
    for old,new in manifest['legacy_aliases'].items():
        if new not in current_chapter_paths:
            continue
        original, replacement = safe_path(old), safe_path(new)
        if not original.exists():
            continue
        if old in by_old:
            assert digest(original.read_bytes()) == by_old[old]['source_sha256'], old
        assert body(original.read_text(encoding='utf-8-sig')) == body(replacement.read_text(encoding='utf-8-sig')), old
        retired.append(dict(old=old,new=new,old_sha256=digest(original.read_bytes())))
    (ROOT/'docs/STORY_VERIFIED_RELOCATIONS.json').write_text(json.dumps(retired,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Verified {len(chapters)} current chapters, identical prose, matching reading copies; {len(retired)} exact legacy duplicates may be removed.')


if __name__ == '__main__':
    main()
