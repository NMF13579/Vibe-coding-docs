#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_FIELDS = [
    "approval_id",
    "approval_status",
    "related_task_id",
    "related_transition_id",
    "approved_by",
    "approved_at",
    "approval_scope",
    "approval_statement",
    "approval_source",
    "allowed_operation",
    "allowed_target_state",
    "expires_at",
    "supersedes",
    "notes",
]

REQUIRED_NON_EMPTY = {
    "approval_id",
    "approval_status",
    "related_task_id",
    "related_transition_id",
    "approved_by",
    "approved_at",
    "approval_scope",
    "approval_statement",
    "approval_source",
    "allowed_operation",
    "allowed_target_state",
}

ALLOWED_STATUS = {"active", "expired", "superseded", "revoked", "invalid"}
ALLOWED_SOURCE = {"chat-session", "written-statement", "external-document", "other"}
SUPPORTED_OPERATION = "complete-active"
SUPPORTED_TARGET_STATE = "completed"

APPROVED_BY_BLOCKLIST = {
    "agent",
    "ai",
    "automated-system",
    "automated_system",
    "system",
    "bot",
    "assistant",
    "claude",
    "gpt",
    "gpt-4",
    "gpt-4o",
    "copilot",
    "llm",
    "model",
    "openai",
    "anthropic",
}

GENERIC_SCOPE_VALUES = {"all", "everything", "any", "unlimited", "global", "full access", "full-access"}
VAGUE_VALUES = ["ok", "looks good", "continue", "дальше", "go ahead", "seems fine", "probably fine"]

BYPASS_SUBSTRINGS = [
    "bypass precondition",
    "bypass preconditions",
    "skip precondition",
    "skip preconditions",
    "bypass verification",
    "skip verification",
    "bypass readiness",
    "skip readiness",
    "bypass transition",
    "skip transition",
    "bypass apply",
    "skip apply",
    "bypass audit",
    "skip audit",
    "no precondition",
    "ignore precondition",
]


def strip_quotes(value: str) -> str:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
        return v[1:-1]
    return v


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, list[str]]:
    reasons: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, ["frontmatter is missing"]

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, ["frontmatter terminator is missing"]

    fm_lines = lines[1:end_idx]

    # Nested YAML detection path A.
    for i, line in enumerate(fm_lines):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            reasons.append("frontmatter uses nested YAML structure; flat format required")
            break
        if ":" not in line:
            reasons.append(f"frontmatter line is invalid: {line}")
            continue
        key, value = line.split(":", 1)
        if key.strip() == "approval" and value.strip() == "":
            reasons.append("frontmatter uses nested YAML structure; flat format required")
            break
        if value.strip() == "" and i + 1 < len(fm_lines):
            nxt = fm_lines[i + 1]
            if nxt.startswith(" ") or nxt.startswith("\t"):
                reasons.append("frontmatter uses nested YAML structure; flat format required")
                break

    fields: dict[str, str] = {}
    for line in fm_lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = strip_quotes(value)

    return fields, reasons


def parse_iso8601(value: str) -> datetime | None:
    t = value.strip()
    if not t:
        return None
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(t)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def validate(fields: dict[str, str]) -> list[str]:
    reasons: list[str] = []

    for f in REQUIRED_FIELDS:
        if f not in fields:
            reasons.append(f"required field missing or empty: {f}")
            continue
        if f in REQUIRED_NON_EMPTY and not fields[f].strip():
            reasons.append(f"required field missing or empty: {f}")

    approval_id = fields.get("approval_id", "")
    status = fields.get("approval_status", "")
    related_task_id = fields.get("related_task_id", "")
    related_transition_id = fields.get("related_transition_id", "")
    approved_by = fields.get("approved_by", "")
    approved_at = fields.get("approved_at", "")
    approval_scope = fields.get("approval_scope", "")
    approval_statement = fields.get("approval_statement", "")
    approval_source = fields.get("approval_source", "")
    allowed_operation = fields.get("allowed_operation", "")
    allowed_target_state = fields.get("allowed_target_state", "")
    expires_at = fields.get("expires_at", "")
    supersedes = fields.get("supersedes", "")

    if approval_id:
        if not re.match(r"^approval-\d{8}-[a-z0-9-]+-[a-z0-9-]+$", approval_id):
            reasons.append("approval_id format is invalid")
        if related_task_id and related_task_id not in approval_id:
            reasons.append("approval_id does not reference related_task_id")
        if allowed_operation and not approval_id.endswith("-" + allowed_operation):
            reasons.append("approval_id does not reference allowed_operation")

    if status:
        if status not in ALLOWED_STATUS:
            reasons.append("approval_status is not an allowed value")
        elif status == "expired":
            reasons.append("approval_status is expired")
        elif status == "superseded":
            reasons.append("approval_status is superseded")
        elif status == "revoked":
            reasons.append("approval_status is revoked")
        elif status == "invalid":
            reasons.append("approval_status is invalid")

    if related_task_id and not related_task_id.startswith("task-"):
        reasons.append("related_task_id format is invalid")

    if related_transition_id and not related_transition_id.startswith("transition-"):
        reasons.append("related_transition_id format is invalid")

    if approved_by:
        if approved_by.strip().lower() in APPROVED_BY_BLOCKLIST:
            reasons.append("approved_by identifies a known non-human identity")

    if approved_at and parse_iso8601(approved_at) is None:
        reasons.append("approved_at is not a valid ISO 8601 timestamp")

    if approval_scope:
        if approval_scope.strip().lower() in GENERIC_SCOPE_VALUES:
            reasons.append("approval_scope is too generic")

    if approval_statement:
        stmt_norm = approval_statement.strip().lower()
        for token in VAGUE_VALUES:
            if stmt_norm == token or stmt_norm.startswith(token):
                reasons.append("approval_statement is vague")
                break

        if related_task_id and related_task_id not in approval_statement:
            reasons.append("approval_statement does not reference related_task_id")
        if related_transition_id and related_transition_id not in approval_statement:
            reasons.append("approval_statement does not reference related_transition_id")

        stmt_low = approval_statement.lower()
        op_ok = bool(allowed_operation and allowed_operation in approval_statement) or ("complete-active" in stmt_low)
        if not op_ok:
            reasons.append("approval_statement does not reference allowed operation")

        target_ok = bool(allowed_target_state and allowed_target_state in approval_statement) or ("completed" in stmt_low)
        if not target_ok:
            reasons.append("approval_statement does not reference allowed target state")

        for bypass in BYPASS_SUBSTRINGS:
            if bypass in stmt_low:
                reasons.append("approval_statement contains bypass claim")
                break

    if approval_source and approval_source not in ALLOWED_SOURCE:
        reasons.append("approval_source is not an allowed value")

    if allowed_operation and allowed_operation != SUPPORTED_OPERATION:
        reasons.append("allowed_operation is not supported")

    if allowed_target_state and allowed_target_state != SUPPORTED_TARGET_STATE:
        reasons.append("allowed_target_state is not supported")

    if expires_at:
        expiry = parse_iso8601(expires_at)
        if expiry is None:
            reasons.append("expires_at is not a valid ISO 8601 timestamp")
        elif expiry <= datetime.now(timezone.utc):
            reasons.append("approval has expired")

    if supersedes and not supersedes.startswith("approval-"):
        reasons.append("supersedes does not look like a valid approval_id")

    # Deduplicate preserving order.
    out: list[str] = []
    for r in reasons:
        if r not in out:
            out.append(r)
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("Usage: python3 scripts/validate-human-approval.py <approval-record-file>")
        return 1

    path = Path(argv[0])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        print("BLOCKED")
        print("- approval record file is not readable")
        return 1

    fields, parse_reasons = parse_frontmatter(text)
    reasons = list(parse_reasons)
    if fields is None:
        reasons.append("frontmatter parse failed")
    else:
        reasons.extend(validate(fields))

    unique: list[str] = []
    for r in reasons:
        if r not in unique:
            unique.append(r)

    if unique:
        print("BLOCKED")
        for r in unique:
            print(f"- {r}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
