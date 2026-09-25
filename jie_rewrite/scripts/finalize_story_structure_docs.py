"""One-time update of entry points and compatibility commands after the outline migration."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def write(rel,text):
    (ROOT/rel).write_text(text.rstrip()+'\n',encoding='utf-8')


def main():
    write('README.md', '''# 《劫》

[開始閱讀](novel/published/README.md) · [正文工作區](novel/README.md) · [故事大綱](docs/MACRO_OUTLINE.md) · [逐章對照](docs/STORY_STRUCTURE.md)

正文依「時期 → 篇章／插段 → 章節」排列，資料夾直接採大綱名稱。每篇與插段各自從001起算，檔名為 `001_章名.md`；第十九篇的戰後收束另在子目錄從001起算。

現有新版867章。古界尚未完成N-2末段與N-3；第二十篇〈萬古獨行〉是可選容器，目前沒有正文。目錄與章數不代表故事已全部定稿。

`novel/` 是帶開發註記的唯一正文來源；`novel/published/` 是同一新版的乾淨閱讀鏡像。修改來源後執行：

```powershell
python scripts/build_story.py
python scripts/build_story.py --check
```

`docs/STORY_STRUCTURE.json` 管理時期、篇名、順序與章目錄；`docs/MACRO_OUTLINE.md` 管理故事內容與篇界，兩者須一起更新。新章先登記manifest，再生成目錄和閱讀版。舊施工章號對照保留在manifest與逐章表，不再用舊volume編號判斷閱讀順序。

開發共同前提：[作者硬需求](docs/AUTHOR_CORE_REQUIREMENTS.md)、[仙人視角與境界差異](docs/XIANXIA_PERSPECTIVE_CHARTER.md)。每階段完成、驗證後由PM commit並push。產線進度見[狀態板](docs/PIPELINE_STATUS.md)。
''')
    write('docs/V2_VOLUME_READING_MAP.md', '''# 現行篇章對照入口

2026-09-25依作者確認，改採「時期 → 篇章 → 章節」，各篇章號從001起算。舊十卷閱讀包裝已退出現行目錄；本檔保留入口相容性，不再維護第二份卷冊映射。

- [故事大綱與篇界](MACRO_OUTLINE.md)
- [現行逐章對照](STORY_STRUCTURE.md)
- [單一結構清單](STORY_STRUCTURE.json)
- [新版閱讀入口](../novel/published/README.md)

史料中的volume/chapter略記是原施工座標，須透過逐章表轉換；不得直接當作現行章號。第十篇027～030為命藏過渡，第十一之二篇041～047為雷魂篇尾；兩者沒有新增篇號。
''')
    master = ROOT/'docs/MASTER_TABLE_OF_CONTENTS.md'
    text = master.read_text(encoding='utf-8-sig')
    marker = '> **2026-09-25 現行檔案分層**：'
    if marker not in text:
        first,rest=text.split('\n',1)
        text=first+'\n\n'+marker+'正文改依大綱時期／篇章排列，各篇001起算；完整現行檔名與章數以[逐章對照](STORY_STRUCTURE.md)及[主大綱](MACRO_OUTLINE.md)為準。以下內容所留施工卷號、原章號及歷史引用只作溯源，不是第二套閱讀順序。\n'+rest
        write('docs/MASTER_TABLE_OF_CONTENTS.md',text)
    wrapper = '''"""Compatibility entry point; current layout is managed by build_story.py."""
import sys
from build_story import main

if __name__ == '__main__':
    raise SystemExit(main())
'''
    for name in ('build_upper_realm_reading_v2.py','build_v2_reading_index.py'):
        write('scripts/'+name,wrapper)
    write('scripts/audit_story_mirrors.py', '''"""Validate current reading copies; --sync regenerates them from current sources."""
import sys
from build_story import main

if __name__ == '__main__':
    if '--sync' in sys.argv:
        sys.argv.remove('--sync')
    elif '--check' not in sys.argv:
        sys.argv.append('--check')
    raise SystemExit(main())
''')
    write('scripts/build_lower_realm_v2.ps1', '''# Compatibility entry point for the current outline-based publication workflow.
param([switch]$Check, [switch]$AllowLegacy)
$taskBuildArgs = @((Join-Path $PSScriptRoot 'build_story.py'))
if ($Check) { $taskBuildArgs += '--check' }
if ($AllowLegacy) { $taskBuildArgs += '--allow-legacy' }
& python @taskBuildArgs
exit $LASTEXITCODE
''')
    # These two retired utilities encode the removed paths/footer bug. Keep a clear fail-fast message.
    write('scripts/make_clean_copy.pl', '''use strict;
use warnings;
die "Retired: run python scripts/build_story.py (see README.md).\\n";
''')
    write('scripts/_scan_footer_bug.py', '''"""Compatibility audit: current builder preserves ordinary Markdown sections."""
import sys
from build_story import main
if __name__ == '__main__':
    if '--check' not in sys.argv:
        sys.argv.append('--check')
    raise SystemExit(main())
''')
    # Keep machine manifest compact and deterministic after PowerShell processing.
    manifest=ROOT/'docs/STORY_STRUCTURE.json'
    data=json.loads(manifest.read_text(encoding='utf-8-sig'))
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
