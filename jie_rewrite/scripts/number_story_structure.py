"""Apply the author's sortable, locally restarted three-digit directory numbers."""
from pathlib import Path
import json
import re
from urllib.parse import quote
from migrate_story_structure import body, digest

ROOT=Path(__file__).resolve().parents[1]


def main():
    manifest=ROOT/'docs/STORY_STRUCTURE.json'
    data=json.loads(manifest.read_text(encoding='utf-8'))
    period_map={}
    directory_map={}
    label_map={}
    counters={}
    path_map={}
    copies=[]
    former_generated=[]
    for group in data['groups']:
        old=group['path']
        parts=old.split('/')
        period=parts[0]
        if period not in period_map:
            period_map[period]=f"{len(period_map)+1:03}_"+period.split('：')[-1]
            label_map[period]=period_map[period]
        old_parent='/'.join(parts[:-1])
        parent=period_map[period] if len(parts)==2 else directory_map[old_parent]
        number=counters.get(old_parent,0 if group['id']=='prologue' else 1)
        counters[old_parent]=number+1
        caption=group['title'].split('：',1)[-1]
        title=f'{number:03}_{caption}'
        new=parent+'/'+title
        directory_map[old]=new
        label_map[group['title']]=title
        group['historical_outline_title']=group['title']
        group['title']=title
        group['path']=new
        for chapter in group['chapters']:
            old_source=chapter['source']
            new_source='novel/'+new+'/'+old_source.rsplit('/',1)[1]
            old_pub=chapter['published']
            new_pub='novel/published/'+new+'/'+old_pub.rsplit('/',1)[1]
            path_map[old_source]=new_source
            path_map[old_pub]=new_pub
            chapter['source']=new_source
            chapter['published']=new_pub
            copies.append((old_source,new_source))
    for old,new in {**period_map,**directory_map}.items():
        for prefix in ('novel/','novel/published/'):
            old_readme=prefix+old+'/README.md'
            path_map[old_readme]=prefix+new+'/README.md'
            if (ROOT/old_readme).exists():
                former_generated.append(old_readme)
    for old,new in copies:
        source=ROOT/old
        dest=ROOT/new
        assert source.exists() and not dest.exists(), (old,new)
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(source.read_bytes())
        assert dest.read_bytes()==source.read_bytes()
    data['legacy_aliases']={k:path_map.get(v,v) for k,v in data['legacy_aliases'].items()}
    data['legacy_aliases'].update(path_map)
    # Keep an explicit inventory of generated intermediate paths for the migration verifier.
    data['intermediate_generated_files']=former_generated
    data['numbering']='Each directory level restarts at 001; prologue uses 000; chapters restart at 001.'
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    replacements={}
    for old,new in path_map.items():
        replacements[old]=new
        replacements[quote(old,safe='/')]=quote(new,safe='/')
        # Relative Markdown paths contain the same suffix without novel/.
        if old.startswith('novel/'):
            replacements[old[6:]]=new[6:]
            replacements[quote(old[6:],safe='/')]=quote(new[6:],safe='/')
    for old,new in {**period_map,**directory_map}.items():
        replacements[old+'/']=new+'/'
        replacements[quote(old+'/',safe='/')]=quote(new+'/',safe='/')
    regex=re.compile('|'.join(re.escape(k) for k in sorted(replacements,key=len,reverse=True)))
    skip=set(data['legacy_aliases'])|set(data['retired_files'])
    for file in ROOT.rglob('*.md'):
        rel=file.relative_to(ROOT).as_posix()
        if rel in skip or rel.startswith(('docs/archive/','docs/author_directives/','.claude/')):
            continue
        raw=file.read_bytes()
        text=raw.decode('utf-8-sig')
        updated=regex.sub(lambda m:replacements[m[0]],text)
        if rel=='docs/MACRO_OUTLINE.md':
            for old,new in label_map.items():
                updated=re.sub(r'^(#{2,4}\s+)'+re.escape(old)+r'\s*$',lambda m:m[1]+new,updated,flags=re.M)
            updated=updated.replace('各節現行資料夾、章數與章號','各層以三位數順序編號，序篇000、其餘001起；各節現行資料夾、章數與章號')
        if updated!=text:
            file.write_bytes((b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'')+updated.encode('utf-8'))
    print(f'Numbered {len(data["groups"])} groups and copied {len(copies)} chapters byte-for-byte; previous paths retained until verification.')


if __name__=='__main__':
    main()
