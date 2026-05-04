#!/usr/bin/env python3
"""Build derived Markdown/frontmatter index (read-only for source files)."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

REQUIRED_FIELDS = (
    "type",
    "module",
    "status",
    "authority",
    "created",
    "last_validated",
)

DEFAULT_SCAN_DIRS = (
    "docs",
    "templates",
    "reports",
    "tasks",
    "examples",
    "core-rules",
    "policies",
    "quality",
)


class BuildUsageError(Exception):
    pass


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build data/index.json from Markdown/frontmatter")
    parser.add_argument("--output", default="data/index.json", help="Output index path")
    parser.add_argument("--root", default=".", help="Repository root to scan")
    return parser.parse_args(argv)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    warnings: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["missing_frontmatter"]

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        return {}, ["missing_frontmatter_closing_delimiter"]

    fields: dict[str, str] = {}
    for raw in lines[1:end]:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            warnings.append("invalid_frontmatter_line")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key:
            fields[key] = value

    return fields, warnings


def collect_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for dirname in DEFAULT_SCAN_DIRS:
        base = root / dirname
        if not base.is_dir():
            continue
        files.extend([p for p in base.rglob("*.md") if p.is_file()])

    files.extend([p for p in root.glob("*.md") if p.is_file()])

    unique = sorted({p.resolve() for p in files})
    return [Path(p) for p in unique]


def build_entry(root: Path, path: Path) -> tuple[dict[str, object], int]:
    rel_path = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")

    fm, fm_warnings = parse_frontmatter(text)

    warnings: list[str] = list(fm_warnings)

    entry: dict[str, object] = {
        "path": rel_path,
        "type": "unknown",
        "module": "unknown",
        "status": "unknown",
        "authority": "unknown",
        "created": "unknown",
        "last_validated": "unknown",
    }

    for key in REQUIRED_FIELDS:
        value = fm.get(key)
        if value is None or value == "":
            if "missing_frontmatter" not in warnings and "missing_frontmatter_closing_delimiter" not in warnings:
                warnings.append(f"missing_field:{key}")
            continue
        entry[key] = value

    if warnings:
        entry["warnings"] = warnings

    return entry, len(warnings)


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        root = Path(args.root).resolve()
        if not root.exists() or not root.is_dir():
            raise BuildUsageError(f"root path not found or not directory: {root}")

        out_path = Path(args.output)
        if not out_path.is_absolute():
            out_path = (root / out_path).resolve()

        md_files = collect_markdown_files(root)
        entries: list[dict[str, object]] = []
        warning_count = 0

        for md in md_files:
            try:
                entry, count = build_entry(root, md)
                entries.append(entry)
                warning_count += count
            except Exception as exc:
                entries.append(
                    {
                        "path": md.relative_to(root).as_posix(),
                        "type": "unknown",
                        "module": "unknown",
                        "status": "unknown",
                        "authority": "unknown",
                        "created": "unknown",
                        "last_validated": "unknown",
                        "warnings": [f"read_error:{exc}"]
                    }
                )
                warning_count += 1

        payload = {
            "schema_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": "markdown_frontmatter",
            "entries": entries,
        }

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        marker = "PASS" if warning_count == 0 else "WARN"
        print(f"{marker}: scanned_markdown={len(md_files)}")
        print(f"{marker}: indexed_entries={len(entries)}")
        print(f"{marker}: warning_count={warning_count}")
        print(f"{marker}: output={out_path}")

        return 0 if warning_count == 0 else 1

    except BuildUsageError as exc:
        print(f"ERROR: {exc}")
        return 2
    except Exception as exc:
        print(f"ERROR: unexpected: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
