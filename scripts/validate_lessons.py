#!/usr/bin/env python3
"""
Validate lesson files for required frontmatter fields and simple formatting.

Usage:
  python3 scripts/validate_lessons.py

No external dependencies.
"""
from __future__ import annotations
import os
import re
import sys
from typing import Dict, List

REQUIRED_FIELDS = {
    "id",
    "title",
    "domain",
    "track",
    "level",
    "module",
    "duration",
    "prerequisites",
    "tags",
    "sources",
}

FRONTMATTER_START = re.compile(r"^---\s*$")
FIELD_RE = re.compile(r"^(?P<key>[a-zA-Z0-9_]+):\s*(?P<value>.*)$")
LIST_ITEM_RE = re.compile(r"^\s*-\s+.*$")


SKIP_DIR_NAMES = {"solutions", "challenges"}


def find_markdown_files(root: str) -> List[str]:
    files = []
    for base, _, names in os.walk(os.path.join(root, "library")):
        for n in names:
            if n.endswith(".md"):
                full = os.path.join(base, n)
                parts = full.replace("\\", "/").split("/")
                if any(skip in parts for skip in SKIP_DIR_NAMES):
                    continue
                files.append(full)
    return sorted(files)


def parse_frontmatter(path: str) -> Dict[str, str] | None:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not FRONTMATTER_START.match(lines[0]):
        return None

    fields: Dict[str, str] = {}
    i = 1
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if FRONTMATTER_START.match(line):
            break
        if not line.strip():
            i += 1
            continue
        m = FIELD_RE.match(line)
        if m:
            key = m.group("key").strip()
            value = m.group("value").strip()
            fields[key] = value
        else:
            # allow list-style continuation for arrays (e.g., sources/tags)
            if ":" in line:
                # malformed key/value; still record to help debugging
                parts = line.split(":", 1)
                fields[parts[0].strip()] = parts[1].strip()
        i += 1
    return fields


def validate_file(path: str) -> List[str]:
    errors: List[str] = []
    fm = parse_frontmatter(path)
    if fm is None:
        errors.append("Missing or malformed frontmatter (--- block at top)")
        return errors

    missing = REQUIRED_FIELDS - set(fm.keys())
    if missing:
        errors.append(f"Missing required fields: {', '.join(sorted(missing))}")

    # Basic checks
    if "id" in fm and not re.match(r"^[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-\d{3}$", fm["id"]):
        errors.append("id must match pattern AAA-BBB-CCC-000 (e.g., CYB-FND-BEG-001)")

    if "duration" in fm and not re.match(r"^(\d+m|\dh)$", fm["duration"]):
        errors.append("duration must be like 30m or 1h")

    return errors


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_files = find_markdown_files(repo_root)
    if not md_files:
        print("No markdown files found under library/", file=sys.stderr)
        return 1

    failed = 0
    for path in md_files:
        errs = validate_file(path)
        if errs:
            failed += 1
            rel = os.path.relpath(path, repo_root)
            print(f"[FAIL] {rel}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"[OK]   {os.path.relpath(path, repo_root)}")

    if failed:
        print(f"\n{failed} file(s) failed validation.", file=sys.stderr)
        return 2

    print("\nAll lesson files passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
