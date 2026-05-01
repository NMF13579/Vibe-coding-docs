#!/usr/bin/env python3
"""Validate active task integrity (Milestone 12 Layer 1)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "task_id",
    "state",
    "activated_at",
    "activated_by",
    "approval_id",
    "source_task",
    "source_contract",
    "transition",
]

ALLOWED_ACTIVATED_BY = {"human-approved-command"}
ACTIVATED_AT_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate tasks/active-task.md integrity (read-only)."
    )
    parser.add_argument(
        "--active-task",
        default="tasks/active-task.md",
        help="Path to active task pointer file (default: tasks/active-task.md)",
    )
    return parser.parse_args(argv)


def read_text(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, str(exc)


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    frontmatter: dict[str, str] = {}
    end_index = None

    for idx, line in enumerate(lines[1:], start=1):
        stripped = line.strip()
        if stripped == "---":
            end_index = idx
            break
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            return None, f"malformed frontmatter line: {line}"
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip("'\"")

    if end_index is None:
        return None, "missing YAML frontmatter terminator"
    return frontmatter, None


def is_repo_relative_safe(path_text: str) -> bool:
    if not path_text.strip():
        return False
    path = Path(path_text)
    if path.is_absolute():
        return False
    return ".." not in path.parts


def extract_task_id_from_text(text: str) -> str | None:
    patterns = [
        r"(?im)^\s*task_id\s*:\s*['\"]?([A-Za-z0-9._-]+)['\"]?\s*$",
        r"(?im)^\s*task\.id\s*:\s*['\"]?([A-Za-z0-9._-]+)['\"]?\s*$",
        r"(?ims)^\s*task\s*:\s*$.*?^\s+id\s*:\s*['\"]?([A-Za-z0-9._-]+)['\"]?\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return None


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent
    active_path = Path(args.active_task)
    if not active_path.is_absolute():
        active_path = repo_root / active_path

    failures: list[str] = []
    partials: list[str] = []

    checks: list[tuple[str, str]] = []

    if not active_path.is_file():
        failures.append(f"active-task file not found: {args.active_task}")
        checks.append(("active-task exists", "FAIL"))
        print("Active Task Validation: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1
    checks.append(("active-task exists", "PASS"))

    active_text, read_error = read_text(active_path)
    if read_error or active_text is None:
        print("Active Task Validation: FAIL")
        print("Failures:")
        print(f"- cannot read active-task.md: {read_error}")
        print("Exit: 1")
        return 1

    active_fm, fm_error = parse_frontmatter(active_text)
    if fm_error or active_fm is None:
        print("Active Task Validation: FAIL")
        print("Failures:")
        print(f"- frontmatter parse error: {fm_error}")
        print("Exit: 1")
        return 1
    checks.append(("frontmatter", "PASS"))

    # Required fields
    for field in REQUIRED_FIELDS:
        if not active_fm.get(field, "").strip():
            failures.append(f"missing required field: {field}")
    checks.append(("required fields", "PASS" if not failures else "FAIL"))

    # Required values
    state = active_fm.get("state", "")
    if state != "active":
        failures.append(f'state must equal "active", got "{state}"')

    transition = active_fm.get("transition", "")
    if transition != "approved_for_execution:active":
        failures.append(
            'transition must equal "approved_for_execution:active", '
            f'got "{transition}"'
        )

    activated_by = active_fm.get("activated_by", "")
    if activated_by not in ALLOWED_ACTIVATED_BY:
        failures.append(
            "activated_by must be one of "
            f"{sorted(ALLOWED_ACTIVATED_BY)}, got \"{activated_by}\""
        )
    checks.append(("required values", "PASS" if not failures else "FAIL"))

    # activated_at pattern
    activated_at = active_fm.get("activated_at", "")
    if not ACTIVATED_AT_RE.search(activated_at):
        failures.append(
            "activated_at must match timestamp-like pattern "
            "YYYY-MM-DDTHH:MM"
        )
        checks.append(("activated_at", "FAIL"))
    else:
        checks.append(("activated_at", "PASS"))

    # source paths checks
    source_task_rel = active_fm.get("source_task", "")
    source_contract_rel = active_fm.get("source_contract", "")
    path_ok = True
    if not is_repo_relative_safe(source_task_rel):
        failures.append(f"source_task path is unsafe: {source_task_rel}")
        path_ok = False
    if not is_repo_relative_safe(source_contract_rel):
        failures.append(f"source_contract path is unsafe: {source_contract_rel}")
        path_ok = False
    checks.append(("source paths", "PASS" if path_ok else "FAIL"))

    source_task_path = repo_root / source_task_rel if source_task_rel else None
    source_contract_path = repo_root / source_contract_rel if source_contract_rel else None

    source_task_exists = bool(source_task_path and source_task_path.is_file())
    source_contract_exists = bool(source_contract_path and source_contract_path.is_file())
    if not source_task_exists:
        failures.append(f"source_task does not exist: {source_task_rel}")
    if not source_contract_exists:
        failures.append(f"source_contract does not exist: {source_contract_rel}")
    checks.append(("source_task exists", "PASS" if source_task_exists else "FAIL"))
    checks.append(("source_contract exists", "PASS" if source_contract_exists else "FAIL"))

    active_task_id = active_fm.get("task_id", "")

    # Consistency: task_id from source files
    source_task_match = "FAIL"
    if source_task_exists and source_task_path is not None:
        source_task_text, err = read_text(source_task_path)
        if err or source_task_text is None:
            failures.append(f"cannot read source_task: {source_task_rel}")
        else:
            source_task_id = extract_task_id_from_text(source_task_text)
            if not source_task_id:
                partials.append("source_task task_id could not be determined")
                source_task_match = "PARTIAL"
            elif source_task_id != active_task_id:
                failures.append(
                    "task_id mismatch with source_task: "
                    f'active "{active_task_id}" vs source_task "{source_task_id}"'
                )
            else:
                source_task_match = "PASS"
    checks.append(("source_task task_id match", source_task_match))

    source_contract_match = "FAIL"
    if source_contract_exists and source_contract_path is not None:
        source_contract_text, err = read_text(source_contract_path)
        if err or source_contract_text is None:
            failures.append(f"cannot read source_contract: {source_contract_rel}")
        else:
            source_contract_id = extract_task_id_from_text(source_contract_text)
            if not source_contract_id:
                partials.append("source_contract task_id could not be determined")
                source_contract_match = "PARTIAL"
            elif source_contract_id != active_task_id:
                failures.append(
                    "task_id mismatch with source_contract: "
                    f'active "{active_task_id}" vs source_contract "{source_contract_id}"'
                )
            else:
                source_contract_match = "PASS"
    checks.append(("source_contract task_id match", source_contract_match))

    # approval resolver intentionally skipped in 12.2.1
    resolver_note = "approval marker resolver: SKIPPED"

    if failures:
        print("Active Task Validation: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    if partials:
        print("Active Task Validation: PARTIAL")
        print("Failures:")
        for item in partials:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    print("Active Task Validation: PASS")
    print("Checked:")
    for name, status in checks:
        print(f"- {name}: {status}")
    print("Notes:")
    print(f"- {resolver_note}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:  # pragma: no cover - safety net
        print("Active Task Validation: FAIL")
        print("Failures:")
        print(f"- implementation failure: {exc}")
        print("Exit: 1")
        raise SystemExit(1)
