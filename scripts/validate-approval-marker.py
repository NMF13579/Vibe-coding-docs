#!/usr/bin/env python3
"""Read-only approval marker validator for AgentOS."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ALLOWED_APPROVAL_TYPES = {
    "brief",
    "review",
    "trace",
    "contract",
    "execution",
    "drop",
    "restart",
}

ALLOWED_SCOPES = {
    "approve_brief",
    "approve_contract",
    "activate_task",
    "mark_completed",
    "mark_failed",
    "drop_task",
    "restart_task",
}

ALLOWED_STATUS_VALUES = {"approved", "revoked", "expired", "superseded"}

TRANSITION_TO_SCOPE = {
    "contract_drafted:approved_for_execution": "approve_contract",
    "approved_for_execution:active": "activate_task",
    "active:completed": "mark_completed",
    "active:failed": "mark_failed",
    "active:dropped": "drop_task",
    "failed:brief_draft": "restart_task",
    "brief_draft:brief_approved": "approve_brief",
}

MARKER_SCAN_LIMIT = 200


@dataclass
class ValidationResult:
    ok: bool
    reasons: list[str]
    warnings: list[str]


def usage() -> None:
    print(
        "Usage: python3 scripts/validate-approval-marker.py "
        "approvals/{approval-id}.md --task task-001 --scope activate_task "
        "[--transition from:to]"
    )


def parse_args(argv: list[str]) -> tuple[str, str, str, str | None] | None:
    if not argv or any(arg in {"-h", "--help"} for arg in argv):
        return None

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("marker_path", nargs="?")
    parser.add_argument("--task")
    parser.add_argument("--scope")
    parser.add_argument("--transition")
    try:
        args, extras = parser.parse_known_args(argv)
    except SystemExit:
        return None

    if extras:
        return None
    if not args.marker_path or not args.task or not args.scope:
        return None
    return args.marker_path, args.task, args.scope, args.transition


def strip_quotes(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and ((text[0] == text[-1] == '"') or (text[0] == text[-1] == "'")):
        return text[1:-1]
    return text


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    frontmatter: dict[str, str] = {}
    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None, f"invalid frontmatter line: {line}"
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = strip_quotes(value)

    if end_index is None:
        return None, "missing YAML frontmatter terminator"
    return frontmatter, None


def parse_iso_timestamp(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def current_utc() -> datetime:
    return datetime.now(timezone.utc)


def marker_task_id_from_related_contract(path: str) -> set[str]:
    return set(re.findall(r"task-[A-Za-z0-9]+", path))


def read_marker_file(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, str(exc)


def scan_for_conflicts(marker_path: Path, marker: dict[str, str]) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    reasons: list[str] = []

    marker_dir = marker_path.parent
    if not marker_dir.exists() or not marker_dir.is_dir():
        return reasons, warnings

    current_approval_id = marker.get("approval_id", "")
    current_task_id = marker.get("task_id", "")
    current_scope = marker.get("scope", "")

    md_files = sorted(marker_dir.glob("*.md"))
    scanned = 0
    for other_path in md_files:
        if other_path.resolve() == marker_path.resolve():
            continue
        scanned += 1
        if scanned > MARKER_SCAN_LIMIT:
            warnings.append(
                f"marker scan stopped after {MARKER_SCAN_LIMIT} files in {marker_dir}"
            )
            break
        other_text, read_error = read_marker_file(other_path)
        if read_error:
            warnings.append(f"skipped {other_path}: {read_error}")
            continue
        other_marker, parse_error = parse_frontmatter(other_text or "")
        if parse_error or other_marker is None:
            warnings.append(f"skipped {other_path}: {parse_error}")
            continue

        if other_marker.get("task_id") != current_task_id:
            continue
        if other_marker.get("scope") != current_scope:
            continue
        if other_marker.get("status") != "approved":
            continue
        if other_marker.get("approval_id", "") == current_approval_id:
            continue

        reasons.append(
            f"conflicting approval marker found: {other_path.name} ({other_marker.get('approval_id', 'missing approval_id')})"
        )

    return reasons, warnings


def validate_marker(path_text: str, task_id: str, scope: str, transition: str | None) -> ValidationResult:
    path = Path(path_text)
    reasons: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return ValidationResult(False, ["marker file does not exist"], warnings)
    if not path.is_file():
        return ValidationResult(False, ["marker path is not a file"], warnings)

    text, read_error = read_marker_file(path)
    if read_error or text is None:
        return ValidationResult(False, [f"cannot read marker: {read_error}"], warnings)

    marker, parse_error = parse_frontmatter(text)
    if parse_error or marker is None:
        return ValidationResult(False, [parse_error or "missing YAML frontmatter"], warnings)

    required_fields = [
        "approval_id",
        "task_id",
        "approval_type",
        "approved_by",
        "approved_at",
        "status",
        "scope",
    ]
    for field in required_fields:
        if field not in marker or not marker[field].strip():
            reasons.append(f"missing required field: {field}")

    approval_type = marker.get("approval_type", "").strip()
    marker_status = marker.get("status", "").strip()
    marker_scope = marker.get("scope", "").strip()
    marker_task_id = marker.get("task_id", "").strip()
    approval_id = marker.get("approval_id", "").strip()

    if marker_task_id != task_id:
        reasons.append("task_id does not match requested task")
    if marker_scope != scope:
        reasons.append("scope does not match requested scope")
    if marker_status not in ALLOWED_STATUS_VALUES:
        reasons.append(f"unknown status: {marker_status or 'missing'}")
    elif marker_status != "approved":
        reasons.append(f"marker status is {marker_status}")
    if approval_type not in ALLOWED_APPROVAL_TYPES:
        reasons.append(f"unknown approval_type: {approval_type or 'missing'}")
    if marker_scope not in ALLOWED_SCOPES:
        reasons.append(f"unknown scope: {marker_scope or 'missing'}")

    if not marker.get("approved_by", "").strip():
        reasons.append("approved_by is missing or empty")

    approved_at = parse_iso_timestamp(marker.get("approved_at", ""))
    if approved_at is None:
        reasons.append("approved_at is not a parseable ISO 8601 timestamp with timezone")

    expires_raw = marker.get("expires_at", "")
    if expires_raw.strip():
        expires_at = parse_iso_timestamp(expires_raw)
        if expires_at is None:
            reasons.append("expires_at is malformed")
        elif expires_at <= current_utc():
            reasons.append("marker expired")

    if marker_status == "revoked":
        reasons.append("marker revoked")
    if marker.get("revoked_at", "").strip():
        reasons.append("marker revoked")
    if marker.get("revoked_by", "").strip():
        reasons.append("marker revoked")

    if marker_status == "superseded":
        reasons.append("marker superseded")
    if marker.get("superseded_by", "").strip():
        reasons.append("marker superseded")

    if approval_type == "execution" or marker_scope in {"activate_task", "approve_contract"}:
        related_contract = marker.get("related_contract", "").strip()
        if not related_contract:
            reasons.append("related_contract is required")
        else:
            related_contract_path = Path(related_contract)
            if not related_contract_path.is_absolute():
                related_contract_path = Path.cwd() / related_contract_path
            if not related_contract_path.exists():
                reasons.append("related_contract file does not exist")

            task_ids = marker_task_id_from_related_contract(related_contract)
            for candidate in task_ids:
                if candidate != task_id:
                    reasons.append("related_contract points to the wrong task")
                    break

    if transition:
        transition_scope = TRANSITION_TO_SCOPE.get(transition)
        if transition_scope is None:
            reasons.append("unknown transition")
        elif transition_scope != marker_scope:
            reasons.append("transition scope does not match marker scope")
    elif marker_scope != scope:
        reasons.append("scope does not match requested scope")

    conflict_reasons, conflict_warnings = scan_for_conflicts(path, marker)
    reasons.extend(conflict_reasons)
    warnings.extend(conflict_warnings)

    return ValidationResult(not reasons, reasons, warnings)


def print_result(path_text: str, task_id: str, scope: str, result: ValidationResult) -> None:
    print("APPROVAL MARKER VALIDATION")
    print(f"Marker: {path_text}")
    print(f"Task: {task_id}")
    print(f"Scope: {scope}")
    print(f"Result: {'PASS' if result.ok else 'FAIL'}")
    if result.reasons:
        print("Reasons:")
        for reason in result.reasons:
            print(f"- {reason}")
    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"- {warning}")
    print("Transition executed: no")
    print("Approval granted by validator: no")


def main(argv: list[str]) -> int:
    parsed = parse_args(argv)
    if parsed is None:
        usage()
        return 2

    marker_path, task_id, scope, transition = parsed
    result = validate_marker(marker_path, task_id, scope, transition)
    print_result(marker_path, task_id, scope, result)
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
