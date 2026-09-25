"""Build current story reading copies and indexes from docs/STORY_STRUCTURE.json."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "docs/STORY_STRUCTURE.json"
META = re.compile(r"^>\s*(?:定位|時間|唯一來源依據|來源依據|章節定位|原章號|狀態)[：:]")
FOOTER = re.compile(r"^#{2,3}\s+(?:一致性自檢|本章自檢|章末自檢|自檢|修訂記錄|修訂紀錄|待確認提案)(?:\s.*|[（(:：].*)?$")
CHAPTER = re.compile(r"^#\s+(?:[^\s]*·)?第[零〇一二三四五六七八九十百千兩\d]+章(?:\s|$)")


def checked_path(root: Path, value: str) -> Path:
    """Reject traversal, absolute paths, Windows alternate streams and symlinks."""
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"Invalid relative path: {value!r}")
    parts = value.split("/")
    if any(p in ("", ".", "..") or re.search(r'[<>:"|?*\x00-\x1f]', p)
           or p.endswith((" ", ".")) for p in parts):
        raise ValueError(f"Unsafe path: {value}")
    path = root.joinpath(*parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes project: {value}")
    node = root
    for part in parts:
        node /= part
        if node.is_symlink() or getattr(node, "is_junction", lambda: False)():
            raise ValueError(f"Linked path is not allowed: {value}")
    return path


def clean_body(text: str) -> str:
    """Keep ordinary sections and blockquotes; strip only explicit build metadata."""
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Missing chapter heading")
    start = 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start < len(lines) and META.match(lines[start]):
        while start < len(lines) and lines[start].startswith(">"):
            start += 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    end = len(lines)
    for i in range(start, end):
        if FOOTER.fullmatch(lines[i].strip()):
            end = i
            j = i - 1
            while j >= start and not lines[j].strip():
                j -= 1
            if j >= start and lines[j].strip() == "---":
                end = j
            break
    while end > start and not lines[end - 1].strip():
        end -= 1
    body = "\n".join(lines[start:end])
    if not body.strip():
        raise ValueError("Chapter has no prose")
    return body


def label(text: str) -> str:
    return str(text).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def link(title: str, target: str) -> str:
    return f"[{label(title)}]({quote(target, safe='/')})"


def chapter_filename(number: int, title: str) -> str:
    safe_title = title.translate(str.maketrans('<>:"/\\|?*', '＜＞：＂／＼｜？＊')).rstrip(" .")
    if not safe_title:
        raise ValueError("Chapter title has no usable filename")
    return f"{number:03}_{safe_title}.md"


def build_plan(root: Path = ROOT, allow_legacy: bool = False) -> dict[Path, bytes]:
    data = json.loads(checked_path(root, MANIFEST).read_text(encoding="utf-8-sig"))
    if data.get("schema_version") != 1 or not isinstance(data.get("groups"), list):
        raise ValueError("Expected schema_version 1 and groups array")
    expected, sources, publications, groups, ids = {}, set(), set(), {}, set()
    nodes: dict[str, list[str]] = {"": []}
    rows = ["# 故事篇章與正文對照", "", "由 STORY_STRUCTURE.json 依大綱順序產生。",
            "歷史路徑只供溯源，不是現行閱讀入口；搬遷雜湊保留作稽核基線，不鎖住日後改稿。", "",
            "| 時期／篇章 | 章號 | 章名 | 開發稿 | 閱讀版 | 歷史路徑 |",
            "| --- | --- | --- | --- | --- | --- |"]

    def put(relative: str, content: str) -> None:
        path = checked_path(root, relative)
        if path in expected or path in sources:
            raise ValueError(f"Output collision: {relative}")
        expected[path] = (content.rstrip("\n") + "\n").encode("utf-8")

    for group in data["groups"]:
        gid, title, relative = group["id"], group["title"], group["path"]
        chapters = group["chapters"]
        if not gid or gid in ids or relative in groups or not title or not group["status"]:
            raise ValueError(f"Invalid or duplicate group: {gid}")
        if not isinstance(chapters, list) or len(PurePosixPath(relative).parts) < 2:
            raise ValueError(f"Group must be under a period: {relative}")
        checked_path(root, "novel/" + relative)
        if relative.split("/")[0] == "published":
            raise ValueError("Development group cannot be under published")
        groups[relative] = group
        ids.add(gid)
        parent = ""
        for part in relative.split("/"):
            child = f"{parent}/{part}".lstrip("/")
            if child not in nodes:
                nodes[child] = []
                nodes[parent].append(child)
            parent = child
        for number, chapter in enumerate(chapters, 1):
            if type(chapter["number"]) is not int or chapter["number"] != number:
                raise ValueError(f"Non-contiguous chapter numbers: {relative}")
            name = chapter["title"]
            if not isinstance(name, str) or not name.strip() or "\n" in name or "\r" in name:
                raise ValueError(f"Invalid chapter title: {relative}/{number}")
            filename = chapter_filename(number, name)
            source_rel, pub_rel = f"novel/{relative}/{filename}", f"novel/published/{relative}/{filename}"
            if chapter["source"] != source_rel or chapter["published"] != pub_rel:
                raise ValueError(f"Chapter path/name does not match manifest: {relative}/{number}")
            source, published = checked_path(root, source_rel), checked_path(root, pub_rel)
            if source in sources or published in publications or source in expected:
                raise ValueError(f"Duplicate chapter path: {source_rel}")
            if not source.is_file():
                raise ValueError(f"Missing source: {source_rel}")
            sources.add(source)
            publications.add(published)
            text = source.read_text(encoding="utf-8-sig")
            if text.splitlines()[:1] != [f"# 第{number:03}章 {name}"]:
                raise ValueError(f"Source heading does not match manifest: {source_rel}")
            body = clean_body(text)
            put(pub_rel, f"# 第{number:03}章 {name}\n\n{body}\n")
            rows.append(f"| {label(relative)} | {number:03} | {label(name)} | "
                        f"{link('正文', '../' + source_rel)} | {link('閱讀', '../' + pub_rel)} | "
                        f"{label(chapter.get('legacy_source', ''))} |")
        if not chapters:
            rows.append(f"| {label(relative)} | — | 待開發 | — | — | — |")

    for base in ("novel", "novel/published"):
        for relative, children in nodes.items():
            if children != sorted(children):
                raise ValueError(f"Directory names do not sort in reading order: {relative}")
            group = groups.get(relative)
            title = group["title"] if group else (relative.rsplit("/", 1)[-1] if relative else "《劫》正文目錄")
            lines = [f"# {title}", "", "依大綱時期與篇章排列；各篇章號從 001 起算。", ""]
            if group:
                lines += [f"狀態：{group['status']}", ""]
                if not group["chapters"]:
                    lines += ["待開發：本篇尚無正文。", ""]
                for chapter in group["chapters"]:
                    filename = chapter_filename(chapter['number'], chapter['title'])
                    caption = f"{chapter['number']:03}_{chapter['title']}"
                    lines.append(f"- {link(caption, filename)}")
                lines.append("")
            for child in children:
                caption = groups[child]["title"] if child in groups else child.rsplit("/", 1)[-1]
                tail = child[len(relative):].lstrip("/")
                lines.append(f"- {link(caption, tail + '/README.md')}")
            put("/".join(filter(None, (base, relative, "README.md"))), "\n".join(lines))
    put("docs/STORY_STRUCTURE.md", "\n".join(rows))

    # The authored outline and the machine index must agree, not just the reading copies.
    outline = (root / 'docs/MACRO_OUTLINE.md').read_text(encoding='utf-8-sig')
    positions = []
    for group in data['groups']:
        heading = list(re.finditer(r'^#{3,4} ' + re.escape(group['title']) + r'[ \t]*$', outline, re.M))
        if len(heading) != 1:
            raise ValueError(f"Outline heading missing or duplicated: {group['title']}")
        positions.append(heading[0].start())
        section = outline[heading[0].end():].split('\n#', 1)[0]
        current = re.findall(r'^\*\*現行正文\*\*：[^\n]*', section, re.M)
        if len(current) != 1:
            raise ValueError(f"Outline requires one current chapter-count row: {group['title']}")
        if '../novel/' + group['path'] + '/README.md' not in current[0]:
            raise ValueError(f"Outline link does not match: {group['title']}")
        count = len(group['chapters'])
        declared = re.search(r'現有\s*(\d+)\s*章', current[0])
        if declared is None or int(declared[1]) != count:
            raise ValueError(f"Outline chapter count does not match: {group['title']}")
    if positions != sorted(positions):
        raise ValueError('Outline order does not match manifest')

    # Each directory is visited once; nested groups do not rescan parent chapters.
    novel = checked_path(root, "novel")
    directories = [novel, *(p for p in novel.rglob("*") if p.is_dir())]
    for directory in directories:
        for path in directory.glob("*.md"):
            if path in sources or path in publications or path in expected:
                continue
            if allow_legacy and path.relative_to(root).as_posix() in set(data.get("legacy_aliases", {})) | set(data.get("retired_files", [])):
                continue
            checked_path(root, path.relative_to(root).as_posix())
            first = path.read_text(encoding="utf-8-sig").splitlines()[:1]
            if re.match(r"^(?:\d{3,}_|chapter\d)", path.name, re.I) or (first and CHAPTER.match(first[0])):
                raise ValueError(f"Unlisted chapter: {path.relative_to(root)}")
    return expected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate generated files without writing")
    parser.add_argument("--allow-legacy", action="store_true", help="Migration only: tolerate explicitly inventoried legacy files pending retirement")
    args = parser.parse_args()
    try:
        expected = build_plan(allow_legacy=args.allow_legacy)
        if args.check:
            stale = [str(p.relative_to(ROOT)) for p, content in expected.items()
                     if not p.is_file() or p.read_bytes() != content]
            if stale:
                raise ValueError("Missing or outdated generated files:\n" + "\n".join(stale))
        else:
            for path, content in expected.items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
        print(f"{'Verified' if args.check else 'Built'} {len(expected)} story files.")
        if args.allow_legacy:
            print("Legacy retirement is NOT verified in this migration mode.")
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Story build failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
