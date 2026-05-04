#!/usr/bin/env python3
"""Read-only metadata consistency audit for derived index."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

UNSAFE_FIELDS = {
    "approval_decision",
    "completion_decision",
    "release_decision",
    "approved",
    "completed",
    "release_ready",
    "human_decision_authority",
    "self_heal_authority",
    "sqlite_authority",
    "rag_authority",
    "backend_authority",
    "autonomous_execution_authority",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class UsageError(Exception):
    pass


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Audit metadata consistency using derived index")
    p.add_argument("--index", default="data/index.json", help="Index file path")
    p.add_argument("--root", default=".", help="Root path for entry path resolution")
    return p.parse_args(argv)


def load_index(index_path: Path):
    if not index_path.is_file():
        return None, "NOT_FOUND", [f"index file not found: {index_path}"]
    try:
        doc = json.loads(index_path.read_text(encoding="utf-8"))
        return doc, "OK", []
    except json.JSONDecodeError as exc:
        return None, "ERROR", [f"invalid JSON: {exc}"]


def audit(doc: object, root: Path) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []

    if not isinstance(doc, dict):
        return ["top-level index must be object"], warns

    required = ("schema_version", "generated_at", "source", "entries")
    for key in required:
        if key not in doc:
            fails.append(f"missing top-level field: {key}")

    if fails:
        return fails, warns

    if doc.get("source") != "markdown_frontmatter":
        fails.append("top-level source must equal markdown_frontmatter")

    generated_at = doc.get("generated_at")
    if not isinstance(generated_at, str) or not generated_at:
        fails.append("generated_at must be non-empty string")
    elif DATE_RE.fullmatch(generated_at) is None:
        warns.append("generated_at format is non-standard")
    else:
        try:
            ts = datetime.strptime(generated_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            age = datetime.now(timezone.utc) - ts
            if age.days > 30:
                warns.append("generated_at appears stale (>30 days)")
        except Exception:
            warns.append("generated_at parse warning")

    entries = doc.get("entries")
    if not isinstance(entries, list):
        fails.append("entries must be a list")
        return fails, warns

    seen_paths: set[str] = set()
    unknown_count = 0
    warning_field_count = 0

    for idx, entry in enumerate(entries):
        prefix = f"entry[{idx}]"
        if not isinstance(entry, dict):
            fails.append(f"{prefix} must be object")
            continue

        for unsafe in UNSAFE_FIELDS:
            if unsafe in entry:
                fails.append(f"{prefix} contains unsafe field: {unsafe}")

        path = entry.get("path")
        if not isinstance(path, str) or not path:
            fails.append(f"{prefix} missing or invalid path")
        else:
            if path in seen_paths:
                fails.append(f"duplicate path: {path}")
            seen_paths.add(path)

            resolved = (root / path).resolve()
            if not resolved.exists():
                fails.append(f"{prefix} path does not exist: {path}")
            elif resolved.suffix.lower() != ".md":
                fails.append(f"{prefix} path is not markdown: {path}")

        for key in ("type", "module", "status", "authority", "created", "last_validated"):
            value = entry.get(key)
            if value == "unknown":
                unknown_count += 1

        if "warnings" in entry:
            warning_field_count += 1

    if unknown_count > 0:
        warns.append(f"entries contain unknown metadata values: {unknown_count}")
    if warning_field_count > 0:
        warns.append(f"entries contain warnings fields: {warning_field_count}")

    return fails, warns


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        index_path = Path(args.index)
        root = Path(args.root).resolve()
        if not root.exists() or not root.is_dir():
            raise UsageError(f"root path not found or not directory: {root}")

        doc, state, problems = load_index(index_path)

        if state == "NOT_FOUND":
            print("NOT_FOUND: index file missing")
            for p in problems:
                print(f"  - {p}")
            print("SUMMARY: PASS=0 WARN=0 FAIL=1 ERROR=0 NOT_FOUND=1")
            return 1

        if state == "ERROR":
            print("ERROR: index loading failed")
            for p in problems:
                print(f"  - {p}")
            print("SUMMARY: PASS=0 WARN=0 FAIL=0 ERROR=1 NOT_FOUND=0")
            return 2

        fails, warns = audit(doc, root)

        if fails:
            for f in fails:
                print(f"FAIL: {f}")
        if warns:
            for w in warns:
                print(f"WARN: {w}")

        total_entries = len(doc.get("entries", [])) if isinstance(doc, dict) else 0
        print(f"PASS: index_exists=True")
        print(f"PASS: total_entries={total_entries}")

        if fails:
            print(f"SUMMARY: PASS=1 WARN={len(warns)} FAIL={len(fails)} ERROR=0 NOT_FOUND=0")
            return 1

        if warns:
            print(f"SUMMARY: PASS=1 WARN={len(warns)} FAIL=0 ERROR=0 NOT_FOUND=0")
            return 0

        print("SUMMARY: PASS=1 WARN=0 FAIL=0 ERROR=0 NOT_FOUND=0")
        return 0

    except UsageError as exc:
        print(f"ERROR: {exc}")
        return 2
    except Exception as exc:
        print(f"ERROR: unexpected: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
