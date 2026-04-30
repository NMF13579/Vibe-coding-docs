#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
PARTIAL = "PARTIAL"
NOT_RUN = "NOT RUN"

GATE_ORDER = [
    "active_task_exists",
    "execution_session_exists",
    "session_status_not_failed",
    "session_status_evidence_ready",
    "session_status_not_in_progress",
    "session_status_not_blocked",
    "scope_check_pass",
    "verification_runner_pass",
    "execution_evidence_report_pass",
    "source_contract_exists",
    "acceptance_criteria_present",
    "changed_files_known",
    "human_review_satisfied_if_required",
]

STOP_REASON_PRIORITY = [
    "active_task_missing",
    "session_missing",
    "watchdog_abort",
    "manual_abort",
    "scope_violation",
    "verification_fail",
    "evidence_report_fail",
    "source_contract_missing",
    "acceptance_criteria_missing",
    "changed_files_unknown",
    "changed_files_incomplete",
    "human_review_missing",
    "human_review_pending",
    "evidence_missing",
    "readiness_fail",
]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check completion readiness for controlled completion preparation."
    )
    parser.add_argument(
        "--session",
        default="",
        help="Execution session markdown file path.",
    )
    parser.add_argument(
        "--active-task",
        default="tasks/active-task.md",
        help="Active task markdown file path.",
    )
    return parser.parse_args(argv)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def resolve_path(repo_root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        return p
    return repo_root / p


def find_latest_session(session_dir: Path) -> Path | None:
    if not session_dir.is_dir():
        return None

    all_md = [p for p in session_dir.iterdir() if p.is_file() and p.suffix.lower() == ".md"]
    if not all_md:
        return None

    preferred = [
        p
        for p in all_md
        if p.name.startswith("session-") or p.name.startswith("execution-")
    ]
    pool = preferred if preferred else all_md

    def key_fn(p: Path) -> tuple[float, str]:
        try:
            ts = p.stat().st_mtime
        except OSError:
            ts = 0.0
        return (ts, p.name)

    return sorted(pool, key=key_fn, reverse=True)[0]


def normalize_scalar(value: str) -> str | None:
    v = value.strip()
    if not v:
        return None
    lowered = v.lower()
    if lowered in {'""', "''", "(empty)", "[]", "null", "none", "~"}:
        return None
    return v


def extract_field(text: str, patterns: list[str]) -> str | None:
    found: str | None = None
    lines = text.splitlines()
    for line in lines:
        for pattern in patterns:
            m = re.match(pattern, line)
            if not m:
                continue
            candidate = normalize_scalar(m.group(1) if m.groups() else "")
            if candidate is None:
                found = None
            else:
                found = candidate
    return found


def contains_value(text: str, patterns: list[str], value: str) -> bool:
    actual = extract_field(text, patterns)
    if actual is None:
        return False
    return actual.strip().upper() == value.strip().upper()


def extract_block_values(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    hits: list[tuple[int, int, str]] = []
    for idx, line in enumerate(lines):
        m = re.match(rf"^(\s*){re.escape(key)}\s*:\s*(.*)$", line)
        if m:
            hits.append((idx, len(m.group(1)), m.group(2)))
    if not hits:
        return []

    start, indent, tail = hits[-1]
    tail_norm = normalize_scalar(tail)
    if tail_norm is not None:
        return [tail_norm]

    out: list[str] = []
    for line in lines[start + 1 :]:
        if not line.strip():
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= indent:
            break
        stripped = line.strip()
        if stripped.startswith("- "):
            item = normalize_scalar(stripped[2:])
            if item is not None:
                out.append(item)
    return out


def detect_abort(text: str) -> str | None:
    matches = re.findall(
        r"(?im)^\s*abort_reason\s*:\s*(watchdog_abort|manual_abort)\s*$",
        text,
    )
    if not matches:
        return None
    return matches[-1]


def evaluate_active_task(path: Path) -> tuple[str | None, dict[str, str], dict[str, str]]:
    gates: dict[str, str] = {}
    hints: dict[str, str] = {}
    text = read_text(path)
    if text is None:
        gates["active_task_exists"] = NOT_RUN
        hints["active_task_missing"] = "1"
        return None, gates, hints

    gates["active_task_exists"] = PASS

    source_contract = extract_field(text, [r"(?im)^\s*source_contract\s*:\s*(.*)$"])
    if source_contract is None:
        gates["source_contract_exists"] = FAIL
        hints["source_contract_missing"] = "1"
    else:
        gates["source_contract_exists"] = PASS

    acceptance = extract_block_values(text, "acceptance_criteria")
    if not acceptance:
        gates["acceptance_criteria_present"] = FAIL
        hints["acceptance_criteria_missing"] = "1"
    else:
        gates["acceptance_criteria_present"] = PASS

    changed = extract_block_values(text, "changed_files")
    changed_scalar = extract_field(text, [r"(?im)^\s*changed_files\s*:\s*(.*)$"])
    if changed:
        partial_tokens = {"partial", "incomplete"}
        if any(any(t in item.lower() for t in partial_tokens) for item in changed):
            gates["changed_files_known"] = PARTIAL
            hints["changed_files_incomplete"] = "1"
        else:
            gates["changed_files_known"] = PASS
    else:
        if changed_scalar is not None and any(
            t in changed_scalar.lower() for t in ["partial", "incomplete"]
        ):
            gates["changed_files_known"] = PARTIAL
            hints["changed_files_incomplete"] = "1"
        else:
            gates["changed_files_known"] = FAIL
            hints["changed_files_unknown"] = "1"

    required = contains_value(
        text,
        [r"(?im)^\s*human_review_required\s*:\s*(.*)$"],
        "true",
    )
    status = extract_field(text, [r"(?im)^\s*human_review_status\s*:\s*(.*)$"])
    if required:
        if status is None:
            gates["human_review_satisfied_if_required"] = FAIL
            hints["human_review_missing"] = "1"
        elif status.lower() == "pending":
            gates["human_review_satisfied_if_required"] = PARTIAL
            hints["human_review_pending"] = "1"
        elif status.lower() == "satisfied":
            gates["human_review_satisfied_if_required"] = PASS
        else:
            gates["human_review_satisfied_if_required"] = FAIL
            hints["human_review_missing"] = "1"
    else:
        gates["human_review_satisfied_if_required"] = PASS

    return text, gates, hints


def evaluate_session(path: Path | None) -> tuple[str | None, dict[str, str], dict[str, str]]:
    gates: dict[str, str] = {}
    hints: dict[str, str] = {}

    if path is None:
        gates["execution_session_exists"] = NOT_RUN
        hints["session_missing"] = "1"
        return None, gates, hints

    text = read_text(path)
    if text is None:
        gates["execution_session_exists"] = NOT_RUN
        hints["session_missing"] = "1"
        return None, gates, hints

    gates["execution_session_exists"] = PASS

    abort_reason = detect_abort(text)
    if abort_reason == "watchdog_abort":
        gates["session_status_not_failed"] = FAIL
        hints["watchdog_abort"] = "1"
        return text, gates, hints
    if abort_reason == "manual_abort":
        gates["session_status_not_failed"] = FAIL
        hints["manual_abort"] = "1"
        return text, gates, hints

    status = extract_field(
        text,
        [
            r"(?im)^\s*session\.status\s*:\s*(.*)$",
            r"(?im)^\s*status\s*:\s*(.*)$",
        ],
    )

    if status is None:
        gates["session_status_not_failed"] = NOT_RUN
        gates["session_status_evidence_ready"] = NOT_RUN
        gates["session_status_not_in_progress"] = NOT_RUN
        gates["session_status_not_blocked"] = NOT_RUN
        hints["evidence_missing"] = "1"
        return text, gates, hints

    lowered = status.lower()
    if lowered == "failed":
        gates["session_status_not_failed"] = FAIL
        return text, gates, hints

    gates["session_status_not_failed"] = PASS

    if lowered == "evidence_ready":
        gates["session_status_evidence_ready"] = PASS
        gates["session_status_not_in_progress"] = PASS
        gates["session_status_not_blocked"] = PASS
    elif lowered == "in_progress":
        gates["session_status_evidence_ready"] = PARTIAL
        gates["session_status_not_in_progress"] = PARTIAL
        gates["session_status_not_blocked"] = PASS
    elif lowered == "blocked":
        gates["session_status_evidence_ready"] = FAIL
        gates["session_status_not_in_progress"] = PASS
        gates["session_status_not_blocked"] = FAIL
    else:
        gates["session_status_evidence_ready"] = PARTIAL
        gates["session_status_not_in_progress"] = PASS
        gates["session_status_not_blocked"] = PASS
        hints["evidence_missing"] = "1"

    if contains_value(text, [r"(?im)^\s*scope_result\s*:\s*(.*)$", r"(?im)^\s*scope_check\s*:\s*(.*)$"], "PASS"):
        gates["scope_check_pass"] = PASS
    else:
        raw_scope = extract_field(text, [r"(?im)^\s*scope_result\s*:\s*(.*)$", r"(?im)^\s*scope_check\s*:\s*(.*)$"])
        if raw_scope is None:
            gates["scope_check_pass"] = PARTIAL
            hints["evidence_missing"] = "1"
        else:
            gates["scope_check_pass"] = FAIL
            hints["scope_violation"] = "1"

    if contains_value(
        text,
        [r"(?im)^\s*verification_result\s*:\s*(.*)$", r"(?im)^\s*verification\s*:\s*(.*)$"],
        "PASS",
    ):
        gates["verification_runner_pass"] = PASS
    else:
        raw_ver = extract_field(
            text,
            [r"(?im)^\s*verification_result\s*:\s*(.*)$", r"(?im)^\s*verification\s*:\s*(.*)$"],
        )
        if raw_ver is None:
            gates["verification_runner_pass"] = PARTIAL
            hints["evidence_missing"] = "1"
        else:
            gates["verification_runner_pass"] = FAIL
            hints["verification_fail"] = "1"

    return text, gates, hints


def evaluate_evidence_report(path: Path) -> tuple[str | None, dict[str, str], dict[str, str]]:
    gates: dict[str, str] = {}
    hints: dict[str, str] = {}
    text = read_text(path)
    if text is None:
        gates["execution_evidence_report_pass"] = PARTIAL
        hints["evidence_missing"] = "1"
        return None, gates, hints

    value = extract_field(
        text,
        [
            r"(?im)^\s*evidence_report_result\s*:\s*(.*)$",
            r"(?im)^\s*execution_evidence_report\s*:\s*(.*)$",
            r"(?im)^\s*status\s*:\s*(.*)$",
        ],
    )
    if value is None:
        gates["execution_evidence_report_pass"] = PARTIAL
        hints["evidence_missing"] = "1"
    elif value.upper() == "PASS":
        gates["execution_evidence_report_pass"] = PASS
    else:
        gates["execution_evidence_report_pass"] = FAIL
        hints["evidence_report_fail"] = "1"
    return text, gates, hints


def merge_gates(*maps: dict[str, str]) -> dict[str, str]:
    out = {gate: NOT_RUN for gate in GATE_ORDER}
    for m in maps:
        for gate, status in m.items():
            out[gate] = status
    return out


def propagate_result(gates: dict[str, str]) -> str:
    values = [gates[g] for g in GATE_ORDER]
    if any(v == FAIL for v in values):
        return FAIL
    if any(v == PARTIAL for v in values):
        return PARTIAL
    if any(v == NOT_RUN for v in values):
        return NOT_RUN
    return PASS


def select_stop_reason(hints: dict[str, str], result: str) -> str:
    if result == PASS:
        return ""
    for reason in STOP_REASON_PRIORITY:
        if reason in hints:
            return reason
    return "readiness_fail"


def print_report(
    result: str,
    stop_reason: str,
    session_path: str,
    active_task_path: str,
    report_path: str,
    gates: dict[str, str],
) -> None:
    print("Completion Readiness Check")
    print()
    print(f"readiness_result: {result}")
    print(f"stop_reason: {stop_reason}")
    print(f"session: {session_path}")
    print(f"active_task: {active_task_path}")
    print(f"execution_evidence_report: {report_path}")
    print()
    print("Required Gates:")
    print(f"- active_task_exists:                 {gates['active_task_exists']}")
    print(f"- execution_session_exists:           {gates['execution_session_exists']}")
    print(f"- session_status_not_failed:          {gates['session_status_not_failed']}")
    print(f"- session_status_evidence_ready:      {gates['session_status_evidence_ready']}")
    print(f"- session_status_not_in_progress:     {gates['session_status_not_in_progress']}")
    print(f"- session_status_not_blocked:         {gates['session_status_not_blocked']}")
    print(f"- scope_check_pass:                   {gates['scope_check_pass']}")
    print(f"- verification_runner_pass:           {gates['verification_runner_pass']}")
    print(f"- execution_evidence_report_pass:     {gates['execution_evidence_report_pass']}")
    print(f"- source_contract_exists:             {gates['source_contract_exists']}")
    print(f"- acceptance_criteria_present:        {gates['acceptance_criteria_present']}")
    print(f"- changed_files_known:                {gates['changed_files_known']}")
    print(f"- human_review_satisfied_if_required: {gates['human_review_satisfied_if_required']}")
    print()
    print("Safety:")
    print("- script_is_read_only: YES")
    print("- lifecycle_mutated: NO")
    print("- completion_applied: NO")
    print("- transition_record_created: NO")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    active_path = resolve_path(repo_root, args.active_task)

    if args.session:
        session_path_obj: Path | None = resolve_path(repo_root, args.session)
    else:
        session_dir = repo_root / "reports" / "execution"
        session_path_obj = find_latest_session(session_dir)

    report_path_obj = repo_root / "reports" / "execution-evidence-report.md"

    hints: dict[str, str] = {}

    active_text, active_gates, active_hints = evaluate_active_task(active_path)
    hints.update(active_hints)

    if active_gates.get("active_task_exists") == NOT_RUN:
        gates = merge_gates(active_gates)
        result = propagate_result(gates)
        stop_reason = select_stop_reason(hints, result)
        print_report(
            result,
            stop_reason,
            str(session_path_obj) if session_path_obj else "missing",
            "missing",
            str(report_path_obj) if report_path_obj.is_file() else "missing",
            gates,
        )
        return 2 if result in {PARTIAL, NOT_RUN} else 1

    session_text, session_gates, session_hints = evaluate_session(session_path_obj)
    hints.update(session_hints)

    if session_gates.get("execution_session_exists") == NOT_RUN:
        gates = {gate: NOT_RUN for gate in GATE_ORDER}
        gates["active_task_exists"] = PASS
        gates["execution_session_exists"] = NOT_RUN
        result = propagate_result(gates)
        stop_reason = select_stop_reason(hints, result)
        print_report(
            result,
            stop_reason,
            "missing",
            str(active_path),
            str(report_path_obj) if report_path_obj.is_file() else "missing",
            gates,
        )
        return 2 if result in {PARTIAL, NOT_RUN} else 1

    report_text, report_gates, report_hints = evaluate_evidence_report(report_path_obj)
    hints.update(report_hints)

    gates = merge_gates(active_gates, session_gates, report_gates)

    if gates.get("session_status_not_failed") == FAIL:
        gates["session_status_evidence_ready"] = NOT_RUN
        gates["session_status_not_in_progress"] = NOT_RUN
        gates["session_status_not_blocked"] = NOT_RUN

    if session_text is None:
        hints.setdefault("evidence_missing", "1")
    if active_text is None:
        hints.setdefault("evidence_missing", "1")
    if report_text is None:
        hints.setdefault("evidence_missing", "1")

    result = propagate_result(gates)
    stop_reason = select_stop_reason(hints, result)

    session_out = str(session_path_obj) if session_path_obj is not None else "missing"
    report_out = str(report_path_obj) if report_path_obj.is_file() else "missing"

    print_report(result, stop_reason, session_out, str(active_path), report_out, gates)

    if result == PASS:
        return 0
    if result == FAIL:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
