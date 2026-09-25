"""One-time outline migration: plan first, copy only after source hashes agree.

Original directory removal is a separate, path-checked PowerShell operation.
The manifest retains historical paths and hashes for lossless migration checks.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/STORY_STRUCTURE.json'
P1 = '第一時期：下界成根'
P2 = '第二時期：上界成道'
P3 = '第三時期：邊荒承劫'
FOOTER = re.compile(r'^##\s*(?:一致性自檢|本章自檢|修訂記錄|待確認提案|章末自檢|自檢)')


def body(text):
    lines = text.splitlines()
    start = 1
    while start < len(lines) and (not lines[start].strip() or lines[start].startswith('>')):
        start += 1
    end = next((i for i in range(start, len(lines)) if FOOTER.match(lines[i].strip())), len(lines))
    while end > start and not lines[end-1].strip():
        end -= 1
    if end > start and lines[end-1].strip() == '---':
        end -= 1
    while end > start and not lines[end-1].strip():
        end -= 1
    return '\n'.join(lines[start:end])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise ValueError(f'Outside project: {relative}')
    return path


def chapter_title(text):
    heading = text.splitlines()[0]
    match = re.match(r'^#\s+(?:古戰域深層篇·)?第\S+?章(?:之一)?\s+(.+)', heading)
    if not match:
        raise ValueError(f'Unsupported heading: {heading}')
    return match[1].strip().removeprefix('〈').removesuffix('〉')


def plan():
    groups = []
    def add(gid, period, title, segments, status='現行正文', parent=None):
        path = '/'.join([period, *([parent] if parent else []), title])
        sources = []
        for directory, first, last in segments:
            candidates = sorted((ROOT / 'novel' / directory).glob('chapter*.md'))
            sources.extend(p for p in candidates if first <= int(re.search(r'chapter(\d+)', p.name)[1]) <= last)
        rows = []
        for n, source in enumerate(sources, 1):
            raw = source.read_bytes()
            text = raw.decode('utf-8-sig')
            title_text = chapter_title(text)
            filename_title = title_text.translate(str.maketrans({'<':'＜','>':'＞',':':'：','"':'＂','/':'／','\\':'＼','|':'｜','?':'？','*':'＊'})).rstrip(' .')
            rel = f'{path}/{n:03}_{filename_title}.md'
            rows.append(dict(number=n, title=title_text, source='novel/'+rel,
                             published='novel/published/'+rel,
                             legacy_source=source.relative_to(ROOT).as_posix(),
                             source_sha256=digest(raw), body_sha256=digest(body(text).encode('utf-8'))))
        groups.append(dict(id=gid,title=title,path=path,status=status,chapters=rows))
    lower = [('prologue','序篇：命落大荒'),('arc01_body_foundation','第一篇：凡軀立命'),
             ('arc02_enter_mountain','第二篇：入山問道'),('arc03_void_spirit_realm','第三篇：虛神界'),
             ('arc04_taixuan_forging','第四篇：太玄閣鑄身'),('arc05_hundred_broken_mountain','第五篇：百斷山'),
             ('arc06_false_commission','第六篇：真假委託'),('bridge_north_sea','北海橋段'),
             ('arc07_lower_realm_storm','第七篇：下界風暴')]
    for directory,title in lower:
        add(directory,P1,title,[(f'lower_realm_v2/{directory}',1,999)])
    for gid,title,lo,hi in [('arc08','第八篇：界隙照命',1,11),('arc09','第九篇：太玄宗・鎮岳入門',12,38),
                           ('arc10','第十篇：七峰大比',39,68),('arc11','第十一篇：百宗盟試',69,92)]:
        add(gid,P2,title,[('volume02_v2',lo,hi)])
    add('arc11b',P2,'第十一之二篇：古戰域深層',[('ancient_battlefield_deep_v2',1,40),('volume02_v2',93,99)])
    add('arc12',P2,'第十二篇：禁都與萬禁會',[('volume03a_v2',1,24)])
    add('wen_family',P2,'插段：文家遭難',[('volume03a_v2',25,28)])
    add('arc13',P2,'第十三篇：三千州爭鋒',[('volume03',1,69)])
    add('arc14',P2,'第十四篇：界潮與古界',[('volume04_v2',1,999)],'開發中：N2-7／N2-8及N-3尚未落筆')
    add('arc15',P2,'第十五篇：無兵雷域',[('volume05',1,18)])
    add('arc16',P2,'第十六篇：天神書院',[('volume06',1,53)])
    add('ancient_world',P2,'新增卷：古世雙界遠行',[('volume06b',1,53)])
    for gid,title,directory in [('arc17','第十七篇：帝關初戰','volume07'),
                               ('foreign_domain','插段：異域同行與帝關守路','volume08'),
                               ('arc18','第十八篇：十凶血路','volume09'),
                               ('long_breath','銜接段：長息','volume10'),
                               ('arc19','第十九篇：大劫決裂','volume11')]:
        add(gid,P3,title,[(directory,1,999)])
    add('home',P3,'戰後收束：萬劫沉封域・劫後有家',[('volume12',1,32)],parent='第十九篇：大劫決裂')
    add('arc20','可選終篇・番外','第二十篇：萬古獨行',[],'可選容器，尚無正文')
    rows = [c for g in groups for c in g['chapters']]
    for key in ('legacy_source','source','published'):
        assert len({r[key] for r in rows}) == len(rows), key
    expected = {p.relative_to(ROOT).as_posix() for p in (ROOT/'novel').glob('*/chapter*.md')
                if p.parent.name not in {'volume03a','volume04'}}
    expected |= {p.relative_to(ROOT).as_posix() for p in (ROOT/'novel/lower_realm_v2').glob('*/chapter*.md')}
    assert expected == {r['legacy_source'] for r in rows}, expected.symmetric_difference({r['legacy_source'] for r in rows})
    aliases = {r['legacy_source']:r['source'] for r in rows}
    legacy_to_row = {r['legacy_source']:r for r in rows}
    for old,row in legacy_to_row.items():
        direct = old.replace('novel/','novel/published/',1)
        if (ROOT/direct).exists():
            aliases[direct] = row['published']
    for realm in ('lower','upper'):
        base = ROOT/f'novel/published/{realm}_realm_v2'
        for line in (base/'SOURCE_MANIFEST.md').read_text(encoding='utf-8-sig').splitlines():
            match = re.search(r'\]\((volume\d+/chapter\w+\.md)\).*`(novel/[^`]+\.md)`',line)
            if match:
                aliases[(base/match[1]).relative_to(ROOT).as_posix()] = legacy_to_row[match[2]]['published']
    legacy_directories = [p.relative_to(ROOT).as_posix() for p in (ROOT/'novel').iterdir() if p.is_dir() and p.name != 'published']
    legacy_directories += [p.relative_to(ROOT).as_posix() for p in (ROOT/'novel/published').iterdir() if p.is_dir()]
    # Every removed file must already exist in Git. No uncommitted material is retired.
    tracked = set(subprocess.check_output(['git','ls-files','--full-name'],cwd=ROOT,text=True,encoding='utf-8').splitlines())
    old_files = [p for directory in legacy_directories for p in (ROOT/directory).rglob('*') if p.is_file()]
    for p in old_files:
        assert 'jie_rewrite/'+p.relative_to(ROOT).as_posix() in tracked, f'Untracked file: {p}'
    retired = [p.relative_to(ROOT).as_posix() for p in old_files if p.relative_to(ROOT).as_posix() not in aliases]
    data = dict(schema_version=1, baseline_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                groups=groups, legacy_aliases=aliases, legacy_directories=legacy_directories,
                retired_files=retired)
    MANIFEST.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Planned {len(groups)} groups, {len(rows)} chapters, {len(aliases)} historical paths.')


def copy_sources():
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    rows = [c for g in data['groups'] for c in g['chapters']]
    for row in rows:
        assert digest(safe_path(row['legacy_source']).read_bytes()) == row['source_sha256'], row['legacy_source']
        assert not safe_path(row['source']).exists(), row['source']
    for row in rows:
        raw = safe_path(row['legacy_source']).read_bytes()
        bom = raw.startswith(b'\xef\xbb\xbf')
        text = raw.decode('utf-8-sig')
        newline = '\r\n' if '\r\n' in text else '\n'
        rest = text.split('\n',1)[1]
        updated = f"# 第{row['number']:03}章 {row['title']}"+newline+rest
        assert digest(body(updated).encode('utf-8')) == row['body_sha256']
        dest = safe_path(row['source'])
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes((b'\xef\xbb\xbf' if bom else b'')+updated.encode('utf-8'))
    print(f'Copied {len(rows)} chapters; every prose hash unchanged. Original files retained pending verification.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['plan','copy'])
    args = p.parse_args()
    plan() if args.action == 'plan' else copy_sources()
