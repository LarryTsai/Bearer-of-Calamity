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


def build() -> str:
    lines = [
        "# 《劫》v2 正文閱讀總目錄",
        "",
        "從卷一第一章開始，依序讀至卷九。每卷章號重新從第一章起算；以下連結是閱讀版正文。開發稿及舊版卷冊不屬於這條閱讀順序。",
        "",
        "本目錄由 `scripts/build_v2_reading_index.py` 依兩份 `SOURCE_MANIFEST.md` 生成；正文修訂後請先重建各卷，再重建本目錄。",
        "",
    ]
    expected_volume = 1
    total = 0
    for realm, manifest in SOURCES:
        lines += [f"## {realm}", ""]
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
                lines += [f"### 卷{volume}", ""]
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
            lines.append(f"- [第{chapter}章　{title}]({relative_path})")
            expected_chapter += 1
            total += 1
        if current_volume is None:
            raise ValueError(f"來源表沒有章節：{manifest}")
        lines.append("")
    if expected_volume != 10 or total != 251:
        raise ValueError(f"卷章總數異常：{expected_volume - 1} 卷、{total} 章")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify that the index is current")
    args = parser.parse_args()
    generated = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != generated:
            raise SystemExit("v2 閱讀總目錄需要重新生成")
        print("v2 reading index verified: 9 volumes, 251 chapters")
    else:
        OUTPUT.write_text(generated, encoding="utf-8")
        print("v2 reading index built: 9 volumes, 251 chapters")


if __name__ == "__main__":
    main()
