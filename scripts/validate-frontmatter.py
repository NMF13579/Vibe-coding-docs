#!/usr/bin/env python3
"""Read-only frontmatter validator (MVP)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_TYPE = {
    "canonical",
    "template",
    "task",
    "report",
    "audit",
    "verification",
    "example",
    "memory",
    "handoff",
    "derived",
    "unknown",
}

ALLOWED_STATUS = {
    "draft",
    "active",
    "canonical",
    "archived",
    "deprecated",
    "unknown",
}

ALLOWED_AUTHORITY = {
    "canonical",
    "supporting",
    "derived",
    "context",
    "unknown",
}

REQUIRED_FIELDS = (
    "type",
    "module",
    "status",
    "authority",
    "created",
    "last_validated",
)

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class UsageError(Exception):
    pass


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing frontmatter opening delimiter"

    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break

    if end is None:
        return {}, "missing frontmatter closing delimiter"

    data: dict[str, str] = {}
    for raw in lines[1:end]:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return {}, f"invalid frontmatter line: {raw}"
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            return {}, "empty frontmatter key"
        if value == "":
            return {}, f"empty value for field: {key}"
        data[key] = value

    return data, None


def validate_doc(path: Path) -> tuple[str, list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return "ERROR", [f"cannot read file: {exc}"]

    fields, parse_err = parse_frontmatter(text)
    if parse_err is not None:
        return "FAIL", [parse_err]

    issues: list[str] = []
    warns: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in fields:
            issues.append(f"missing required field: {field}")

    if issues:
        return "FAIL", issues

    if fields["type"] not in ALLOWED_TYPE:
        issues.append(f"invalid type: {fields['type']}")
    if fields["status"] not in ALLOWED_STATUS:
        issues.append(f"invalid status: {fields['status']}")
    if fields["authority"] not in ALLOWED_AUTHORITY:
        issues.append(f"invalid authority: {fields['authority']}")

    module_val = fields["module"]
    if not isinstance(module_val, str) or module_val.strip() == "":
        issues.append("module must be a non-empty string")

    for date_field in ("created", "last_validated"):
        value = fields[date_field]
        if value != "unknown" and DATE_PATTERN.fullmatch(value) is None:
            issues.append(f"invalid {date_field}: {value}")

    for key in REQUIRED_FIELDS:
        if fields.get(key) == "unknown":
            warns.append(f"unknown value used for {key}")

    if issues:
        return "FAIL", issues
    if warns:
        return "WARN", warns
    return "PASS", ["frontmatter valid"]


def collect_markdown_paths(target: Path) -> list[Path]:
    if not target.exists():
        raise UsageError(f"path not found: {target}")

    if target.is_file():
        if target.suffix.lower() != ".md":
            raise UsageError("file input must be a .md file")
        return [target]

    if target.is_dir():
        return sorted([p for p in target.rglob("*.md") if p.is_file()])

    raise UsageError(f"unsupported path type: {target}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("ERROR: usage: python3 scripts/validate-frontmatter.py <file-or-directory>")
        return 2

    target = Path(argv[1])

    try:
        files = collect_markdown_paths(target)
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

    for path in files:
        status, details = validate_doc(path)
        counts[status] += 1
        rel = str(path)
        print(f"{status}: {rel}")
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
