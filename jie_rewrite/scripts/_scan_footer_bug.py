"""One-off scanner (not part of the pipeline): for each paired novel/<volume>/ +
novel/published/<volume>/ directory, apply the FIXED make_clean_copy.pl logic to
every dev chapter file and diff the result against the actual published file.
Read-only — writes nothing, just reports.
"""
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

VOLUMES = [
    "volume03a",
    "volume04",
    "volume05",
    "volume06",
    "volume06b",
    "volume07",
    "volume08",
    "volume09",
    "volume10",
    "volume11",
    "volume12",
]


def clean_source(lines: list[str]) -> tuple[str, list[str]] | None:
    if not lines:
        return None
    lines = list(lines)
    lines[0] = lines[0].lstrip("﻿")
    if not lines[0].startswith("#"):
        return None
    title = lines[0]
    start = 1
    while start < len(lines) and (not lines[start].strip() or lines[start].startswith(">")):
        start += 1
    footer_heading = re.compile(r"^##\s*(一致性自檢|本章自檢|修訂記錄|待確認提案)")
    footer_idx = -1
    for j, line in enumerate(lines):
        if footer_heading.match(line.strip()):
            k = j - 1
            while k >= 0 and not lines[k].strip():
                k -= 1
            footer_idx = k if (k >= 0 and lines[k].strip() == "---") else j
            break
    end = footer_idx if footer_idx >= 0 else len(lines)
    body = lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    return title, body


def read_lines(path: Path) -> list[str]:
    # Read raw bytes and decode WITHOUT Python's universal-newline translation
    # (Path.read_text/open(mode='r') would otherwise silently split a stray
    # "\r\r\n" byte run into two separate line breaks, one for the lone '\r'
    # and one for the trailing '\r\n', double-counting lines before we ever
    # see them). Decode manually, then collapse any run of '\r' (optionally
    # followed by '\n') into a single '\n' ourselves.
    data = path.read_bytes()
    text = data.decode("utf-8-sig")
    text = re.sub(r"\r+\n?", "\n", text)
    return text.split("\n")[:-1] if text.endswith("\n") else text.split("\n")


def main():
    total_pairs = 0
    mismatches = []
    skipped = []
    for volume in VOLUMES:
        dev_dir = ROOT / "novel" / volume
        pub_dir = ROOT / "novel" / "published" / volume
        if not dev_dir.is_dir() or not pub_dir.is_dir():
            skipped.append((volume, "missing dev or published dir"))
            continue
        dev_files = sorted(dev_dir.glob("chapter*.md"))
        for dev_path in dev_files:
            pub_path = pub_dir / dev_path.name
            if not pub_path.exists():
                mismatches.append((volume, dev_path.name, "published file MISSING"))
                continue
            total_pairs += 1
            try:
                dev_lines = read_lines(dev_path)
            except Exception as e:
                skipped.append((f"{volume}/{dev_path.name}", f"read error: {e}"))
                continue
            cleaned = clean_source(dev_lines)
            if cleaned is None:
                skipped.append((f"{volume}/{dev_path.name}", "no title heading"))
                continue
            title, body = cleaned
            expected = [title, ""] + body
            try:
                pub_lines = read_lines(pub_path)
            except Exception as e:
                skipped.append((f"{volume}/{dev_path.name}", f"pub read error: {e}"))
                continue
            if pub_lines != expected:
                kind = "unknown"
                if len(pub_lines) > len(expected):
                    extra = pub_lines[len(expected):] if pub_lines[:len(expected)] == expected else None
                    if extra is not None and any("一致性自檢" in l for l in extra):
                        kind = "footer leaked into published (extra tail)"
                    else:
                        kind = "published longer than expected"
                elif len(pub_lines) < len(expected):
                    kind = "published shorter than expected (possible truncation)"
                else:
                    kind = "same length, content differs"
                mismatches.append((volume, dev_path.name, kind, len(expected), len(pub_lines)))
    print(f"Checked {total_pairs} pairs across {len(VOLUMES)} candidate volumes.")
    print(f"\nMISMATCHES: {len(mismatches)}")
    for m in mismatches:
        print(" ", m)
    print(f"\nSKIPPED: {len(skipped)}")
    for s in skipped:
        print(" ", s)


if __name__ == "__main__":
    main()
