"""Build the reviewed upper-realm v2 reading volumes without changing development files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "novel/published/upper_realm_v2"
VOLUMES = (
    (4, "volume02_v2", 1, 38),
    (5, "volume02_v2", 39, 64),
    (6, "volume02_v2", 65, 82),
    (6, "ancient_battlefield_deep_v2", 1, 19),
    (7, "ancient_battlefield_deep_v2", 20, 40),
    (7, "volume02_v2", 83, 89),
    (8, "volume03a_v2", 1, 28),
    (9, "volume03_v2", 1, 39),
    (10, "volume03_v2", 40, 69),
)
DIGITS = "零一二三四五六七八九"


def chinese_number(value: int) -> str:
    if value < 10:
        return DIGITS[value]
    if value == 10:
        return "十"
    if value < 20:
        return "十" + DIGITS[value - 10]
    tens, ones = divmod(value, 10)
    return DIGITS[tens] + "十" + (DIGITS[ones] if ones else "")


def clean_source(path: Path) -> tuple[str, list[str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing chapter heading: {path}")
    heading = lines[0]
    start = 1
    while start < len(lines) and (not lines[start].strip() or lines[start].startswith(">")):
        start += 1
    end = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == "## 一致性自檢":
            end = min(end, i)
            break
        if line.strip() == "---":
            after = i + 1
            while after < len(lines) and not lines[after].strip():
                after += 1
            if after < len(lines) and lines[after].startswith("## "):
                end = min(end, i)
    body = lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    if not body:
        raise ValueError(f"Missing prose: {path}")
    return heading, body


def build_plan() -> tuple[dict[Path, bytes], list[str]]:
    expected: dict[Path, bytes] = {}
    manifest = [
        "# 上界 v2 閱讀版逐章來源表",
        "",
        "卷四至十依 `docs/V2_VOLUME_READING_MAP.md` 編排。來源為開發稿；本表記錄卷內新章號與原施工章號，不表示宏綱篇號改變。由 `scripts/build_upper_realm_reading_v2.py` 產生。",
        "",
        "| 閱讀卷章 | 標題 | 開發稿來源 |",
        "| --- | --- | --- |",
    ]
    chapter_counts: dict[int, int] = {}
    for volume, source_dir, first, last in VOLUMES:
        for original_number in range(first, last + 1):
            new_number = chapter_counts.get(volume, 0) + 1
            chapter_counts[volume] = new_number
            source_rel = f"novel/{source_dir}/chapter{original_number:03}.md"
            source = ROOT / source_rel
            heading, body = clean_source(source)
            match = re.fullmatch(r"#\s*(?:古戰域深層篇·)?第[^\s]+?章\s+(.+)", heading)
            if not match:
                raise ValueError(f"Unexpected chapter heading: {source}: {heading}")
            title = match.group(1)
            if title.startswith("〈") or title.endswith("〉"):
                raise ValueError(f"Unnormalized title brackets: {source}: {title}")
            published_source = ROOT / f"novel/published/{source_dir}/chapter{original_number:03}.md"
            if published_source.exists():
                published_lines = published_source.read_text(encoding="utf-8-sig").splitlines()
                if published_lines != [heading, "", *body]:
                    raise ValueError(f"Development and published prose differ: {source_rel}")
            relative = f"volume{volume:02}/chapter{new_number:03}.md"
            destination = OUTPUT / relative
            new_heading = f"# 第{chinese_number(new_number)}章 {title}"
            expected[destination] = (new_heading + "\r\n\r\n" + "\r\n".join(body) + "\r\n").encode("utf-8")
            manifest.append(
                f"| [卷{volume} 第{new_number}章]({relative}) | {title.replace('|', '\\|')} | `{source_rel}` |"
            )
    if len(expected) != 226:
        raise ValueError(f"Expected 226 chapters, got {len(expected)}")
    expected[OUTPUT / "SOURCE_MANIFEST.md"] = ("\n".join(manifest) + "\n").encode("utf-8")
    return expected, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated files without writing")
    args = parser.parse_args()
    expected, _ = build_plan()
    existing = {path for path in OUTPUT.glob("volume[0-9][0-9]/chapter[0-9][0-9][0-9].md")}
    obsolete = sorted(existing - set(expected))
    if args.check:
        mismatches = [str(path.relative_to(ROOT)) for path, data in expected.items() if not path.exists() or path.read_bytes() != data]
        mismatches.extend(f"obsolete: {path.relative_to(ROOT)}" for path in obsolete)
        if mismatches:
            raise SystemExit("Missing or outdated reading files:\n" + "\n".join(mismatches))
        print("Verified 226 chapters and source manifest across volumes 04–10.")
        return
    for path in obsolete:
        path.unlink()
    for path, data in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print("Built 226 chapters and source manifest across volumes 04–10.")


if __name__ == "__main__":
    main()
