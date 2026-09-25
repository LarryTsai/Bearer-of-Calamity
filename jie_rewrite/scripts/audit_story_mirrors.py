"""Audit existing reading mirrors; --sync updates direct/lower mirrors from dev.

Upper reading volumes are audited here but rebuilt only by their official builder.
No development files, indexes, or chapter mappings are changed.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "novel/published"
FOOTER = re.compile(r"^##\s*(?:一致性自檢|本章自檢|修訂記錄|待確認提案|章末自檢|自檢)")


def prose(path: Path) -> tuple[str, list[str]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing heading: {path}")
    start = 1
    while start < len(lines) and (not lines[start].strip() or lines[start].startswith(">")):
        start += 1
    end = next((i for i in range(start, len(lines)) if FOOTER.match(lines[i].strip())), len(lines))
    while end > start and not lines[end - 1].strip():
        end -= 1
    if end > start and lines[end - 1].strip() == "---":
        end -= 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[0], lines[start:end]


def pairs():
    for directory in sorted(PUBLISHED.iterdir()):
        if not directory.is_dir() or directory.name in {"lower_realm_v2", "upper_realm_v2"}:
            continue
        for mirror in sorted(directory.glob("chapter*.md")):
            source = ROOT / "novel" / directory.name / mirror.name
            yield "direct", source, mirror
    for kind in ("lower", "upper"):
        directory = PUBLISHED / f"{kind}_realm_v2"
        manifest = directory / "SOURCE_MANIFEST.md"
        for line in manifest.read_text(encoding="utf-8-sig").splitlines():
            match = re.search(r"\]\((volume\d+/chapter\d+\.md)\).*`(novel/[^`]+\.md)`", line)
            if match:
                yield kind, ROOT / match[2], directory / match[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true")
    args = parser.parse_args()
    count = differences = changed = 0
    for kind, source, mirror in pairs():
        count += 1
        if not source.exists() or not mirror.exists():
            print(f"MISSING {source.relative_to(ROOT)} -> {mirror.relative_to(ROOT)}")
            differences += 1
            continue
        heading, body = prose(source)
        mirror_heading, mirror_body = prose(mirror)
        raw = mirror.read_bytes()
        bad_newlines = b"\r\r\n" in raw
        if body == mirror_body and (kind != "direct" or heading == mirror_heading) and not bad_newlines:
            continue
        differences += 1
        print(f"DIFF {kind} {source.relative_to(ROOT)} -> {mirror.relative_to(ROOT)}")
        if args.sync and kind != "upper":
            newline = "\r\n" if b"\r\n" in raw else "\n"
            text = newline.join([heading if kind == "direct" else mirror_heading, "", *body, ""])
            encoded = text.encode("utf-8")
            if raw.startswith(b"\xef\xbb\xbf"):
                encoded = b"\xef\xbb\xbf" + encoded
            mirror.write_bytes(encoded)
            assert prose(mirror)[1] == body
            changed += 1
    print(f"Audited {count} pairs; differences={differences}; synchronized={changed}.")
    if differences and not args.sync:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
