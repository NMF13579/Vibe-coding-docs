#!/usr/bin/env python3
"""Read-only validator for derived data/index.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_TYPE = {
    "canonical", "template", "task", "report", "audit", "verification",
    "example", "memory", "handoff", "derived", "unknown"
}
ALLOWED_STATUS = {"draft", "active", "canonical", "archived", "deprecated", "unknown"}
ALLOWED_AUTHORITY = {"canonical", "supporting", "derived", "context", "unknown"}
REQUIRED_TOP = ("schema_version", "generated_at", "source", "entries")
REQUIRED_ENTRY = ("path", "type", "module", "status", "authority", "created", "last_validated")
UNSAFE_FIELDS = {
    "approval_decision", "completion_decision", "release_decision", "approved", "completed",
    "release_ready", "human_decision_authority", "self_heal_authority", "sqlite_authority",
    "rag_authority", "backend_authority", "autonomous_execution_authority"
}
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}|unknown)$")


class UsageError(Exception):
    pass


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate derived index")
    p.add_argument("--index", default="data/index.json", help="Index file path")
    p.add_argument("--root", default=".", help="Root for resolving entry paths")
    return p.parse_args(argv)


def load_json(path: Path):
    if not path.is_file():
        raise UsageError(f"index file not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise UsageError(f"invalid JSON: {exc}") from exc


def validate_index(doc: object, root: Path) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []

    if not isinstance(doc, dict):
        fails.append("top-level must be object")
        return fails, warns

    for k in REQUIRED_TOP:
        if k not in doc:
            fails.append(f"missing top-level field: {k}")

    if fails:
        return fails, warns

    if not isinstance(doc["schema_version"], str) or not doc["schema_version"]:
        fails.append("schema_version must be non-empty string")
    if not isinstance(doc["generated_at"], str) or not doc["generated_at"]:
        fails.append("generated_at must be non-empty string")
    if doc["source"] != "markdown_frontmatter":
        fails.append("source must equal markdown_frontmatter")
    if not isinstance(doc["entries"], list):
        fails.append("entries must be a list")
        return fails, warns

    seen_paths: set[str] = set()
    for i, entry in enumerate(doc["entries"]):
        prefix = f"entry[{i}]"
        if not isinstance(entry, dict):
            fails.append(f"{prefix} must be object")
            continue

        for bad in UNSAFE_FIELDS:
            if bad in entry:
                fails.append(f"{prefix} contains unsafe field: {bad}")

        for k in REQUIRED_ENTRY:
            if k not in entry:
                fails.append(f"{prefix} missing required field: {k}")

        if any(k not in entry for k in REQUIRED_ENTRY):
            continue

        path = entry["path"]
        if not isinstance(path, str) or not path:
            fails.append(f"{prefix} path must be non-empty string")
        else:
            if path in seen_paths:
                fails.append(f"duplicate entry path: {path}")
            seen_paths.add(path)
            abs_path = (root / path).resolve()
            if not abs_path.exists():
                fails.append(f"{prefix} path does not exist: {path}")
            elif abs_path.suffix.lower() != ".md":
                fails.append(f"{prefix} path is not markdown: {path}")

        t = entry["type"]
        s = entry["status"]
        a = entry["authority"]
        m = entry["module"]
        c = entry["created"]
        lv = entry["last_validated"]

        if t not in ALLOWED_TYPE:
            fails.append(f"{prefix} invalid type: {t}")
        if s not in ALLOWED_STATUS:
            fails.append(f"{prefix} invalid status: {s}")
        if a not in ALLOWED_AUTHORITY:
            fails.append(f"{prefix} invalid authority: {a}")
        if not isinstance(m, str) or not m.strip():
            fails.append(f"{prefix} module must be non-empty string")
        if not isinstance(c, str) or DATE_RE.fullmatch(c) is None:
            fails.append(f"{prefix} invalid created: {c}")
        if not isinstance(lv, str) or DATE_RE.fullmatch(lv) is None:
            fails.append(f"{prefix} invalid last_validated: {lv}")

        for field_name in ("type", "module", "status", "authority", "created", "last_validated"):
            if entry.get(field_name) == "unknown":
                warns.append(f"{prefix} unknown metadata: {field_name}")

        if "warnings" in entry:
            warns.append(f"{prefix} has warnings field")

    return fails, warns


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        index_path = Path(args.index)
        root = Path(args.root).resolve()
        if not root.exists() or not root.is_dir():
            raise UsageError(f"root not found or not directory: {root}")

        doc = load_json(index_path)
        fails, warns = validate_index(doc, root)

        for f in fails:
            print(f"FAIL: {f}")
        for w in warns:
            print(f"WARN: {w}")

        if fails:
            print(f"SUMMARY: PASS=0 WARN={len(warns)} FAIL={len(fails)} ERROR=0")
            return 1

        if warns:
            print(f"SUMMARY: PASS=1 WARN={len(warns)} FAIL=0 ERROR=0")
            return 0

        print("PASS: index is valid")
        print("SUMMARY: PASS=1 WARN=0 FAIL=0 ERROR=0")
        return 0

    except UsageError as exc:
        print(f"ERROR: {exc}")
        return 2
    except Exception as exc:
        print(f"ERROR: unexpected: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
