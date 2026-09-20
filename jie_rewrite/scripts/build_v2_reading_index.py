"""Build the single entry point for the reviewed v2 reading edition."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "novel" / "published"
OUTPUT = PUBLISHED / "README.md"
SOURCES = (
    ("下界", PUBLISHED / "lower_realm_v2" / "SOURCE_MANIFEST.md"),
    ("上界", PUBLISHED / "upper_realm_v2" / "SOURCE_MANIFEST.md"),
)
ROW = re.compile(r"^\| \[卷(\d+) 第(\d+)章\]\((volume\d{2}/chapter\d{3}\.md)\) \| ([^|]+) \|")
VOLUME_TITLES = {
    1: "活到選路之前",
    2: "能承住的人",
    3: "守住眼前",
    4: "上界入門",
    5: "七峰成軍",
    6: "百宗盟試・古戰域初探",
    7: "古戰域深層・雷魂",
    8: "禁都與文家",
    9: "三千州前段",
    10: "三千州後段",
}
SECTION_HEADINGS = {
    1: "下界（序篇～第七篇）",
    4: "上界宗門（第八～十一篇）",
    7: "古戰域深層與雷魂域（第十一篇後）",
    8: "禁都與文家（第十二篇及插段）",
    9: "三千州爭鋒（第十三篇）",
}
ARC_ENTRIES = (
    ("序篇〈命落大荒〉", 1, 1),
    ("第一篇〈凡軀立命〉", 1, 8),
    ("第二篇〈入山問道〉", 1, 14),
    ("第三篇〈虛神界〉", 2, 1),
    ("第四篇〈太玄閣鑄身〉", 2, 9),
    ("第五篇〈百斷山〉", 2, 19),
    ("第六篇〈真假委託〉", 3, 1),
    ("北海橋段", 3, 8),
    ("第七篇〈下界風暴〉", 3, 12),
    ("第八篇〈界隙照命〉", 4, 1),
    ("第九篇〈太玄宗・鎮岳入門〉", 4, 12),
    ("第十篇〈七峰大比〉", 5, 1),
    ("命藏過渡", 5, 23),
    ("第十一篇〈百宗盟試〉", 6, 1),
    ("第十一篇後插段〈古戰域深層〉", 6, 19),
    ("古戰域深層後段", 7, 1),
    ("雷魂域過渡", 7, 22),
    ("第十二篇〈禁都與萬禁會〉", 8, 1),
    ("文家遭難（第十二、十三篇間）", 8, 25),
    ("第十三篇〈三千州爭鋒〉", 9, 1),
    ("第十三篇後段", 10, 1),
)


def build() -> str:
    lines = [
        "# 《劫》v2 正文閱讀總目錄",
        "",
        "從卷一第一章開始，依序讀至卷十。每卷章號重新從第一章起算；以下連結是閱讀版正文。開發稿及舊版卷冊不屬於這條閱讀順序。",
        "",
        "本目錄由 `scripts/build_v2_reading_index.py` 依兩份 `SOURCE_MANIFEST.md` 生成；正文修訂後請先重建各卷，再重建本目錄。",
        "",
        "## 依大綱篇章閱讀",
        "",
        "篇名依[全書大篇章骨架](../../docs/MACRO_OUTLINE.md)；點篇名旁的起點即可讀正文。卷號只是閱讀版的裝訂位置，篇與卷不必一對一。",
        "",
        "| 大綱故事段落 | 閱讀卷 | 從這裡開始 |",
        "| --- | --- | --- |",
    ]
    for arc_title, volume, chapter in ARC_ENTRIES:
        realm = "lower_realm_v2" if volume <= 3 else "upper_realm_v2"
        chapter_path = f"{realm}/volume{volume:02d}/chapter{chapter:03d}.md"
        if not (PUBLISHED / chapter_path).is_file():
            raise ValueError(f"篇章入口不存在：{arc_title}: {chapter_path}")
        lines.append(f"| {arc_title} | 卷{volume} | [第{chapter}章]({chapter_path}) |")
    lines += [
        "| **第十四篇〈界潮與古界〉（開發中）** | 閱讀卷號未定 | **[古界第一章](../volume04_v2/chapter001.md)** |",
        "",
        "## 開發稿、大綱與閱讀卷對照",
        "",
        "| 故事段落 | 閱讀版 | 從這裡開始 | 對應開發稿與大綱 |",
        "| --- | --- | --- | --- |",
        "| 下界 | 卷1～3 | [卷1 第一章](lower_realm_v2/volume01/chapter001.md) | [卷冊對照](../../docs/V2_VOLUME_READING_MAP.md) |",
        "| 上界宗門、百宗盟試 | 卷4～6 | [卷4 第一章](upper_realm_v2/volume04/chapter001.md) | `novel/volume02_v2/` · [上界大綱](../../docs/outlines/OUTLINE_VOLUME02_V2_UPPER_REALM.md) |",
        "| **古戰域深層、雷魂域** | **卷6～7** | **[古戰域深層第一章](upper_realm_v2/volume06/chapter019.md)** | `novel/ancient_battlefield_deep_v2/` · [深層大綱](../../docs/outlines/OUTLINE_ANCIENT_BATTLEFIELD_DEEP_V2.md) |",
        "| **禁都、萬禁會、文家遭難** | **卷8** | **[禁都第一章](upper_realm_v2/volume08/chapter001.md)** | `novel/volume03a_v2/` · [禁都大綱](../../docs/outlines/OUTLINE_VOLUME03A_V2_FORBIDDEN_CAPITAL.md) |",
        "| 三千州 | 卷9～10 | [卷9 第一章](upper_realm_v2/volume09/chapter001.md) | `novel/volume03_v2/` · [三千州大綱](../../docs/outlines/OUTLINE_THREE_THOUSAND_STATES.md) |",
        "| 古界（開發中） | 閱讀卷號未定 | [古界第一章](../volume04_v2/chapter001.md) | `novel/volume04_v2/` · [古界全篇大綱](../../docs/outlines/OUTLINE_ANCIENT_REALM_EXPANDED.md) |",
        "",
        "**卷10 之後接古界開發稿。** 古界完稿並審定卷界後，才會編入閱讀版；目前不要按舊版 `volume04` 的卷號接讀。",
        "",
    ]
    expected_volume = 1
    total = 0
    arc_starts = {(volume, chapter): title for title, volume, chapter in ARC_ENTRIES}
    for _, manifest in SOURCES:
        current_volume = None
        expected_chapter = 1
        for line in manifest.read_text(encoding="utf-8-sig").splitlines():
            match = ROW.match(line)
            if not match:
                continue
            volume, chapter = map(int, match.group(1, 2))
            local_path, title = (value.strip() for value in match.group(3, 4))
            if volume != current_volume:
                if volume != expected_volume or chapter != 1:
                    raise ValueError(f"卷章順序錯誤：{manifest}: 卷{volume} 第{chapter}章")
                if current_volume is not None:
                    lines.append("")
                if volume in SECTION_HEADINGS:
                    lines += [f"## {SECTION_HEADINGS[volume]}", ""]
                lines += [f"### 卷{volume}〈{VOLUME_TITLES[volume]}〉", ""]
                current_volume = volume
                expected_volume += 1
                expected_chapter = 1
            if chapter != expected_chapter:
                raise ValueError(f"章號中斷：{manifest}: 卷{volume} 第{chapter}章")
            chapter_path = manifest.parent / local_path
            heading = chapter_path.read_text(encoding="utf-8-sig").splitlines()[0]
            if not re.fullmatch(r"# 第[^ ]+章 " + re.escape(title), heading):
                raise ValueError(f"來源表與章名不符：{chapter_path}: {heading!r}")
            relative_path = chapter_path.relative_to(PUBLISHED).as_posix()
            if (volume, chapter) in arc_starts:
                lines += ["", f"#### {arc_starts[(volume, chapter)]}", ""]
            lines.append(f"- [第{chapter}章　{title}]({relative_path})")
            expected_chapter += 1
            total += 1
        if current_volume is None:
            raise ValueError(f"來源表沒有章節：{manifest}")
        lines.append("")
    if expected_volume != 11 or total != 291:
        raise ValueError(f"卷章總數異常：{expected_volume - 1} 卷、{total} 章")
    lines += [
        "## 下一段：古界（第十四篇，開發中）",
        "",
        "接[古界第一章](../volume04_v2/chapter001.md)；本篇尚未編入閱讀卷冊，開發進度與場景對照見[古界全篇大綱](../../docs/outlines/OUTLINE_ANCIENT_REALM_EXPANDED.md)及[Act5 大綱](../../docs/outlines/OUTLINE_ANCIENT_REALM_ACT5.md)。",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify that the index is current")
    args = parser.parse_args()
    generated = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != generated:
            raise SystemExit("v2 閱讀總目錄需要重新生成")
        print("v2 reading index verified: 10 volumes, 291 chapters")
    else:
        OUTPUT.write_text(generated, encoding="utf-8")
        print("v2 reading index built: 10 volumes, 291 chapters")


if __name__ == "__main__":
    main()
