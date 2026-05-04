#!/usr/bin/env python3
"""Read-only boundary claims validator (MVP)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

FORBIDDEN_CLAIMS = [
    "validation guarantees correctness",
    "validation proves correctness",
    "pass means completed",
    "pass means correct",
    "evidence means approval",
    "evidence approves",
    "audit approves release",
    "audit makes final decision",
    "ready means approved",
    "completed means correct",
    "index is source of truth",
    "data index json is source of truth",
    "script can approve",
    "script can make human decision",
    "validator decides release readiness",
    "self heal can change policy",
    "sqlite replaces markdown",
    "rag replaces markdown",
]


class UsageError(Exception):
    pass


def normalize(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return lowered


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

    normalized = normalize(text)
    issues: list[str] = []

    for claim in FORBIDDEN_CLAIMS:
        if claim in normalized:
            issues.append(f"forbidden claim found: {claim}")

    if issues:
        return "FAIL", issues
    return "PASS", ["no forbidden boundary claims found"]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("ERROR: usage: python3 scripts/validate-boundary-claims.py <file-or-directory>")
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
        print("SUMMARY: PASS=0 WARN=1 FAIL=0 ERROR=0")
        return 0

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "ERROR": 0}

    for path in files:
        status, details = validate_file(path)
        counts[status] += 1
        print(f"{status}: {path}")
        for item in details:
            print(f"  - {item}")

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
