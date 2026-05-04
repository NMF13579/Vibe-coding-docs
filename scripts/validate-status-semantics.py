#!/usr/bin/env python3
"""Read-only status semantics validator (MVP)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_MARKERS = {
    "PASS",
    "FAIL",
    "WARN",
    "NOT_RUN",
    "ERROR",
    "READY",
    "NEEDS_REVIEW",
    "APPROVED",
    "BLOCKED",
    "COMPLETED",
    "FAILED",
}

DISALLOWED_MARKERS = {
    "SUCCESS",
    "OK",
    "DONE",
    "SKIPPED",
    "APPROVE",
    "APPROVES",
    "SAFE",
    "CORRECT",
    "VALIDATED",
    "ACCEPTED",
}

UNSAFE_PHRASES = {
    "validation guarantees correctness",
    "evidence means approval",
    "audit approves release",
    "pass means completed",
    "ready means approved",
    "completed means correct",
    "index is source of truth",
    "script can make human decision",
}

MARKER_PATTERN = re.compile(r"\b[A-Z_]{2,}\b")


class UsageError(Exception):
    pass


def collect_markdown_files(target: Path) -> list[Path]:
    if not target.exists():
        raise UsageError(f"path not found: {target}")

    if target.is_file():
        if target.suffix.lower() != ".md":
            raise UsageError("file input must be a .md file")
        return [target]

    if target.is_dir():
        return sorted([p for p in target.rglob("*.md") if p.is_file()])

    raise UsageError(f"unsupported path type: {target}")


def validate_file(path: Path) -> tuple[str, list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return "ERROR", [f"cannot read file: {exc}"]

    issues: list[str] = []

    found_markers = set(MARKER_PATTERN.findall(text))
    disallowed_found = sorted(found_markers.intersection(DISALLOWED_MARKERS))
    for marker in disallowed_found:
        issues.append(f"disallowed marker found: {marker}")

    lowered = text.lower()
    for phrase in sorted(UNSAFE_PHRASES):
        if phrase in lowered:
            issues.append(f"unsafe claim found: {phrase}")

    if issues:
        return "FAIL", issues

    return "PASS", ["status semantics valid"]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("ERROR: usage: python3 scripts/validate-status-semantics.py <file-or-directory>")
        return 2

    target = Path(argv[1])

    try:
        files = collect_markdown_files(target)
    except UsageError as exc:
        print(f"ERROR: {exc}")
        return 2
    except Exception as exc:
        print(f"ERROR: unexpected: {exc}")
        return 2

    if not files:
        print("WARN: no markdown files found")
        print("SUMMARY: PASS=0 WARN=0 FAIL=0 ERROR=0")
        return 0

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "ERROR": 0}

    for file_path in files:
        status, details = validate_file(file_path)
        counts[status] += 1
        print(f"{status}: {file_path}")
        for detail in details:
            print(f"  - {detail}")

    print(
        "SUMMARY: "
        f"PASS={counts['PASS']} "
        f"WARN={counts['WARN']} "
        f"FAIL={counts['FAIL']} "
        f"ERROR={counts['ERROR']}"
    )

    if counts["FAIL"] > 0:
        return 1
    if counts["ERROR"] > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
