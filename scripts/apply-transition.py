#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DRY_RUN_PASS = "DRY_RUN_PASS"
DRY_RUN_BLOCKED = "DRY_RUN_BLOCKED"
APPLY_PLAN_PREPARED = "APPLY_PLAN_PREPARED"
APPLY_PLAN_BLOCKED = "APPLY_PLAN_BLOCKED"
APPLY_EVIDENCE_CREATED = "APPLY_EVIDENCE_CREATED"
APPLY_EVIDENCE_BLOCKED = "APPLY_EVIDENCE_BLOCKED"
COMPLETE_ACTIVE_PLAN_READY = "COMPLETE_ACTIVE_PLAN_READY"
COMPLETE_ACTIVE_PLAN_BLOCKED = "COMPLETE_ACTIVE_PLAN_BLOCKED"
COMPLETE_ACTIVE_APPLIED = "COMPLETE_ACTIVE_APPLIED"
COMPLETE_ACTIVE_BLOCKED = "COMPLETE_ACTIVE_BLOCKED"

SAFETY_STATEMENT = "Apply transition dry-run is read-only and must not mutate lifecycle state."
APPLY_EVIDENCE_SAFETY = "Controlled apply evidence does not mutate lifecycle folders or task files."
COMPLETE_ACTIVE_PLAN_SAFETY = "Complete-active mutation plan does not mutate lifecycle folders or task files."
COMPLETE_ACTIVE_MUTATION_SAFETY = (
    "Complete-active lifecycle mutation is allowed only with prepared transition, apply plan, applied evidence, mutation plan, and passing preconditions."
)

PROTECTED_PREFIXES = ("docs/", "tasks/", "reports/", "templates/")

PROTECTED_EXACT = {
    "docs/CONTROLLED-LIFECYCLE-MUTATION.md",
    "docs/APPLY-PRECONDITIONS.md",
    "docs/APPLIED-TRANSITION-RECORD.md",
    "docs/APPLY-PLAN.md",
    "docs/COMPLETION-TRANSITION.md",
    "templates/applied-transition-record.md",
    "templates/apply-plan.md",
    "templates/completion-transition.md",
    "scripts/check-apply-preconditions.py",
    "scripts/complete-active-task.py",
}

# Approval-gate phrase markers for audit compatibility:
# --approval <file>
# validate-human-approval
# approval is required but no approval record
# approval validation failed


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Controlled apply command with dry-run, apply-plan, apply evidence, complete-active-plan, and complete-active modes."
    )
    parser.add_argument("--transition", required=True, help="Prepared transition markdown file path.")
    parser.add_argument("--dry-run", action="store_true", help="Run read-only dry-run check.")
    parser.add_argument("--prepare", action="store_true", help="Prepare apply plan file (no lifecycle mutation).")
    parser.add_argument("--apply", action="store_true", help="Create applied transition evidence (no lifecycle mutation).")
    parser.add_argument("--complete-active-plan", action="store_true", help="Prepare complete-active mutation plan only.")
    parser.add_argument("--complete-active", action="store_true", help="Apply complete-active lifecycle mutation.")
    parser.add_argument("--plan-out", default="", help="Output path for apply plan file (required with --prepare).")
    parser.add_argument("--plan", default="", help="Apply plan file path (required with --apply, --complete-active-plan, --complete-active).")
    parser.add_argument("--applied-record-out", default="", help="Output path for applied transition evidence record (required with --apply).")
    parser.add_argument("--applied-record", default="", help="Existing applied transition evidence file (required with --complete-active-plan and --complete-active).")
    parser.add_argument("--mutation-plan", default="", help="Existing complete-active mutation plan file (required with --complete-active).")
    parser.add_argument("--policy", default="", help="Policy case file path for controlled complete-active gate.")
    parser.add_argument(
        "--approval",
        default="",
        help="Human approval record file path (required when approval_required: true).",
    )
    parser.add_argument("--active-task", default="tasks/active-task.md", help="Active task markdown file path.")
    parser.add_argument("--json", action="store_true", help="Output result as JSON.")
    return parser.parse_args(argv)


def resolve_path(repo_root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        return p
    return repo_root / p


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def sha256_or_empty(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def extract_field(text: str | None, key: str) -> str | None:
    if text is None:
        return None
    matches = re.findall(rf"(?im)^\s*{re.escape(key)}\s*:\s*(.*?)\s*$", text)
    if not matches:
        return None
    value = matches[-1].strip()
    if value in {"", '""', "''", "[]", "null", "None", "none", "~", "<path-or-missing>", "missing"}:
        return None
    return value


def extract_list_block(text: str | None, key: str) -> list[str]:
    if text is None:
        return []
    lines = text.splitlines()
    start = None
    indent = 0
    for i, line in enumerate(lines):
        m = re.match(rf"^(\s*){re.escape(key)}\s*:\s*$", line)
        if m:
            start = i
            indent = len(m.group(1))
    if start is None:
        return []

    out: list[str] = []
    for line in lines[start + 1 :]:
        if not line.strip():
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= indent:
            break
        stripped = line.strip()
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            if value and value not in {"<path-or-missing>", "missing"}:
                out.append(value)
    return out


def has_task_id(value: object) -> bool:
    if value is None:
        return False
    if not isinstance(value, str):
        value = str(value)
    return value.strip() != ""


def is_yes_value(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().upper() in {"YES", "TRUE", "1"}


def check_apply_preconditions(repo_root: Path, transition_path: Path, active_task_path: Path) -> tuple[str, dict[str, object], list[str]]:
    script_path = repo_root / "scripts" / "check-apply-preconditions.py"
    if not script_path.is_file():
        return ("BLOCKED", {}, ["missing_preconditions_checker"])

    cmd = [
        "python3",
        str(script_path),
        "--transition",
        str(transition_path),
        "--active-task",
        str(active_task_path),
        "--json",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)

    payload: dict[str, object] = {}
    parse_errors: list[str] = []
    try:
        payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    except json.JSONDecodeError:
        parse_errors.append("preconditions_output_unreadable")

    result = str(payload.get("result", "BLOCKED"))
    if result not in {"PASS", "BLOCKED"}:
        result = "BLOCKED"
        parse_errors.append("preconditions_result_invalid")

    return result, payload, parse_errors


def run_policy_aware_preconditions_gate(
    repo_root: Path,
    transition_path: Path,
    active_task_path: Path,
    policy: str,
    approval: str,
) -> tuple[int, str]:
    script_path = repo_root / "scripts" / "check-apply-preconditions.py"
    cmd = [
        "python3",
        str(script_path),
        "--transition",
        str(transition_path),
        "--active-task",
        str(active_task_path),
    ]
    if policy:
        cmd.extend(["--policy", policy])
    if approval:
        cmd.extend(["--approval", approval])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout


def validate_output_path(repo_root: Path, out_raw: str, missing_reason: str, protected_reason: str, outside_reason: str) -> tuple[bool, str, Path | None]:
    if not out_raw:
        return (False, missing_reason, None)

    out_path = resolve_path(repo_root, out_raw)

    if out_path.is_absolute() and str(out_path).startswith("/tmp/"):
        return (True, "", out_path)

    rel: str | None
    try:
        rel = out_path.relative_to(repo_root).as_posix()
    except ValueError:
        rel = None

    if rel is None:
        if "/apply-plans/" in out_path.as_posix() or "/applied-transition/" in out_path.as_posix():
            return (True, "", out_path)
        return (False, outside_reason, None)

    if rel in PROTECTED_EXACT:
        return (False, protected_reason, None)

    for prefix in PROTECTED_PREFIXES:
        if rel.startswith(prefix):
            return (False, protected_reason, None)

    if "/apply-plans/" in rel or "/applied-transition/" in rel:
        return (True, "", out_path)

    return (False, outside_reason, None)


def build_base_report(repo_root: Path, transition_path: Path, active_task_path: Path) -> dict[str, object]:
    transition_text = read_text(transition_path)
    blocked_reasons: list[str] = []

    task_id = extract_field(transition_text, "task_id")
    previous_state = extract_field(transition_text, "previous_state") or extract_field(transition_text, "state")
    target_state = extract_field(transition_text, "target_state") or extract_field(transition_text, "new_state") or extract_field(transition_text, "candidate_outcome")

    if transition_text is None:
        blocked_reasons.append("missing_prepared_transition")

    pre_result = "BLOCKED"
    pre_payload: dict[str, object] = {}

    if transition_text is not None:
        pre_result, pre_payload, pre_errors = check_apply_preconditions(repo_root, transition_path, active_task_path)
        blocked_reasons.extend(pre_errors)
        payload_reasons = pre_payload.get("blocked_reasons", [])
        if isinstance(payload_reasons, list):
            for reason in payload_reasons:
                if isinstance(reason, str) and reason not in blocked_reasons:
                    blocked_reasons.append(reason)

    if pre_result != "PASS" and "preconditions_not_passed" not in blocked_reasons:
        blocked_reasons.append("preconditions_not_passed")

    safe_task = task_id if task_id else "unknown-task"
    would_record = str(repo_root / "reports" / "applied-transition" / f"applied-{safe_task}-<timestamp>.md")

    return {
        "transition_text": transition_text,
        "task_id": task_id,
        "previous_state": previous_state,
        "target_state": target_state,
        "preconditions_result": pre_result,
        "blocked_reasons": blocked_reasons,
        "approval_required": pre_payload.get("approval_required"),
        "approval_ref": pre_payload.get("approval_ref"),
        "preconditions_checked_by": pre_payload.get("checked_by", "check-apply-preconditions.py"),
        "would_create_applied_transition_record": would_record,
    }


def write_apply_plan(plan_path: Path, transition_path: Path, base: dict[str, object]) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    task_id = base.get("task_id") or "unknown-task"
    apply_plan_id = f"apply-plan-{task_id}-{ts}"

    blocked_reasons = base.get("blocked_reasons", [])
    blocked_lines = "\n".join([f"  - {r}" for r in blocked_reasons]) if blocked_reasons else "  -"

    content = (
        "---\n"
        f"apply_plan_id: {apply_plan_id}\n"
        f"source_prepared_transition: {transition_path}\n"
        f"task_id: {base.get('task_id') or ''}\n"
        f"previous_state: {base.get('previous_state') or ''}\n"
        f"target_state: {base.get('target_state') or ''}\n"
        f"preconditions_result: {base.get('preconditions_result')}\n"
        "would_mutate: YES\n"
        "planned_operations:\n"
        "  - validate final controlled apply gate\n"
        "  - require explicit human approval boundary\n"
        "  - create applied transition record only after real apply\n"
        f"approval_required: {base.get('approval_required')}\n"
        f"approval_ref: {base.get('approval_ref') or ''}\n"
        "applied_record_template_ref: templates/applied-transition-record.md\n"
        "blocked_reasons:\n"
        f"{blocked_lines}\n"
        f"prepared_at: {ts}\n"
        "prepared_by: apply-transition.py\n"
        "result: APPLY_PLAN_PREPARED\n"
        "reason: preconditions_passed\n"
        "---\n"
    )

    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(content, encoding="utf-8")


def write_applied_record(record_path: Path, transition_path: Path, plan_path: Path, base: dict[str, object]) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    task_id = base.get("task_id") or "unknown-task"
    applied_id = f"applied-transition-{task_id}-{ts}"

    content = (
        "---\n"
        f"applied_transition_id: {applied_id}\n"
        f"source_prepared_transition: {transition_path}\n"
        f"task_id: {base.get('task_id') or ''}\n"
        f"previous_state: {base.get('previous_state') or ''}\n"
        f"new_state: {base.get('target_state') or ''}\n"
        f"applied_at: {ts}\n"
        "applied_by: apply-transition.py\n"
        f"approval_required: {base.get('approval_required')}\n"
        f"approval_ref: {base.get('approval_ref') or ''}\n"
        f"preconditions_result_ref: {base.get('preconditions_checked_by')}\n"
        "evidence_refs:\n"
        f"  - {transition_path}\n"
        f"  - {plan_path}\n"
        "result: APPLY_EVIDENCE_CREATED\n"
        "blocked_reasons:\n"
        "  -\n"
        "reason: controlled_apply_evidence_only_no_lifecycle_mutation\n"
        "---\n"
    )

    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(content, encoding="utf-8")


def discover_completion_destination(repo_root: Path) -> tuple[Path | None, str | None]:
    for candidate in [repo_root / "tasks" / "done", repo_root / "tasks" / "completed"]:
        if candidate.is_dir():
            return (candidate, None)
    return (None, "completion_destination_missing")


def build_allowed_task_paths(active_text: str | None, destination_path: Path | None, task_id: str | None) -> list[str]:
    paths: list[str] = ["tasks/active-task.md"]
    src_task = extract_field(active_text, "source_task")
    src_contract = extract_field(active_text, "source_contract")
    if src_task:
        paths.append(src_task)
    if src_contract:
        paths.append(src_contract)
    if destination_path and task_id:
        paths.append((destination_path / f"{task_id}.md").as_posix())
    return paths


def print_dry_run(report: dict[str, object]) -> None:
    print("Apply Transition Dry-Run")
    print()
    print(f"result: {report['result']}")
    print(f"transition_file: {report['transition_file']}")
    print(f"task_id: {report['task_id']}")
    print(f"previous_state: {report['previous_state']}")
    print(f"target_state: {report['target_state']}")
    print(f"preconditions_result: {report['preconditions_result']}")
    print(f"would_apply: {report['would_apply']}")
    print("blocked_reasons: " + (", ".join(report["blocked_reasons"]) if report["blocked_reasons"] else "none"))
    print(f"applied_transition_record_path_future_mode: {report['would_create_applied_transition_record']}")
    print(SAFETY_STATEMENT)
    print("No files were written.")


def print_prepare(report: dict[str, object]) -> None:
    print("Apply Transition Prepare-Plan")
    print()
    print(f"result: {report['result']}")
    print(f"transition_file: {report['transition_file']}")
    print(f"task_id: {report['task_id']}")
    print(f"previous_state: {report['previous_state']}")
    print(f"target_state: {report['target_state']}")
    print(f"preconditions_result: {report['preconditions_result']}")
    print(f"would_apply: {report['would_apply']}")
    print(f"plan_out: {report['plan_out']}")
    print("blocked_reasons: " + (", ".join(report["blocked_reasons"]) if report["blocked_reasons"] else "none"))
    print(f"applied_transition_record_path_future_mode: {report['would_create_applied_transition_record']}")
    print("Apply plan is not lifecycle mutation.")
    print("Apply plan does not create applied transition records.")


def print_apply(report: dict[str, object]) -> None:
    print("Apply Transition Evidence")
    print()
    print(f"result: {report['result']}")
    print(f"transition_file: {report['transition_file']}")
    print(f"plan_file: {report['plan_file']}")
    print(f"task_id: {report['task_id']}")
    print(f"previous_state: {report['previous_state']}")
    print(f"target_state: {report['target_state']}")
    print(f"preconditions_result: {report['preconditions_result']}")
    print(f"would_apply: {report['would_apply']}")
    print(f"applied_record_out: {report['applied_record_out']}")
    print("blocked_reasons: " + (", ".join(report["blocked_reasons"]) if report["blocked_reasons"] else "none"))
    print(APPLY_EVIDENCE_SAFETY)


def print_complete_active_plan(report: dict[str, object]) -> None:
    print("Complete Active Mutation Plan")
    print()
    print(f"result: {report['result']}")
    print(f"task_id: {report['task_id']}")
    print(f"previous_state: {report['previous_state']}")
    print(f"target_state: {report['target_state']}")
    print(f"completion_destination: {report['completion_destination']}")
    print(f"completion_operation: {report['completion_operation']}")
    print(f"allowed_task_paths: {', '.join(report['allowed_task_paths'])}")
    print(f"preconditions_result: {report['preconditions_result']}")
    print(f"apply_plan_result: {report['apply_plan_result']}")
    print(f"applied_evidence_result: {report['applied_evidence_result']}")
    print(f"would_mutate: {report['would_mutate']}")
    print("blocked_reasons: " + (", ".join(report["blocked_reasons"]) if report["blocked_reasons"] else "none"))
    print(COMPLETE_ACTIVE_PLAN_SAFETY)
    print("No files were written.")


def print_complete_active(report: dict[str, object]) -> None:
    print("Complete Active Lifecycle Mutation")
    print()
    print(f"result: {report['result']}")
    print(f"task_id: {report['task_id']}")
    print(f"target_state: {report['target_state']}")
    print(f"completion_destination: {report['completion_destination']}")
    print(f"modified_task_paths: {', '.join(report['modified_task_paths']) if report['modified_task_paths'] else 'none'}")
    print("blocked_reasons: " + (", ".join(report["blocked_reasons"]) if report["blocked_reasons"] else "none"))
    print(COMPLETE_ACTIVE_MUTATION_SAFETY)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    modes = [args.dry_run, args.prepare, args.apply, args.complete_active_plan, args.complete_active]
    if modes.count(True) != 1:
        print("ERROR: choose exactly one mode: --dry-run, --prepare, --apply, --complete-active-plan, or --complete-active")
        return 2

    if args.prepare and not args.plan_out:
        print("ERROR: --plan-out is required when --prepare is used")
        return 2

    if args.apply and not args.plan:
        print("ERROR: --plan is required when --apply is used")
        return 2

    if args.apply and not args.applied_record_out:
        print("ERROR: --applied-record-out is required when --apply is used")
        return 2

    if args.complete_active_plan and not args.plan:
        print("ERROR: --plan is required when --complete-active-plan is used")
        return 2

    if args.complete_active_plan and not args.applied_record:
        print("ERROR: --applied-record is required when --complete-active-plan is used")
        return 2

    if args.complete_active and not args.policy:
        print("CONTROLLED_APPLY_POLICY_GATE: BLOCKED")
        print("PRECONDITIONS_RESULT: BLOCKED")
        print("APPLY_RESULT: BLOCKED")
        print("blocked_reason: missing_policy_for_complete_active")
        return 1

    transition_path = resolve_path(repo_root, args.transition)
    active_task_path = resolve_path(repo_root, args.active_task)
    active_hash_before = sha256_or_empty(active_task_path)

    base = build_base_report(repo_root, transition_path, active_task_path)

    if args.dry_run:
        dry_result = DRY_RUN_PASS if (base["transition_text"] is not None and base["preconditions_result"] == "PASS") else DRY_RUN_BLOCKED
        report = {
            "result": dry_result,
            "transition_file": str(transition_path),
            "task_id": base["task_id"],
            "previous_state": base["previous_state"],
            "target_state": base["target_state"],
            "preconditions_result": base["preconditions_result"],
            "would_apply": "YES" if dry_result == DRY_RUN_PASS else "NO",
            "blocked_reasons": base["blocked_reasons"],
            "would_create_applied_transition_record": base["would_create_applied_transition_record"],
            "files_written": "NO",
        }
        if args.json:
            print(json.dumps(report, ensure_ascii=True, indent=2))
        else:
            print_dry_run(report)
        return 0 if dry_result == DRY_RUN_PASS else 1

    if args.prepare:
        ok_plan_out, plan_out_error, plan_path = validate_output_path(
            repo_root,
            args.plan_out,
            "missing_plan_out",
            "plan_out_targets_protected_path",
            "plan_out_outside_allowed_locations",
        )
        blocked_reasons = list(base["blocked_reasons"])
        if not ok_plan_out and plan_out_error not in blocked_reasons:
            blocked_reasons.append(plan_out_error)

        prepared = base["transition_text"] is not None and base["preconditions_result"] == "PASS" and ok_plan_out
        prepare_result = APPLY_PLAN_PREPARED if prepared else APPLY_PLAN_BLOCKED

        if prepared and plan_path is not None:
            write_apply_plan(plan_path, transition_path, base)

        report = {
            "result": prepare_result,
            "transition_file": str(transition_path),
            "task_id": base["task_id"],
            "previous_state": base["previous_state"],
            "target_state": base["target_state"],
            "preconditions_result": base["preconditions_result"],
            "would_apply": "YES" if prepared else "NO",
            "plan_out": str(plan_path) if plan_path else args.plan_out,
            "blocked_reasons": blocked_reasons,
            "would_create_applied_transition_record": base["would_create_applied_transition_record"],
            "files_written": "YES" if prepared else "NO",
        }
        if args.json:
            print(json.dumps(report, ensure_ascii=True, indent=2))
        else:
            print_prepare(report)
        return 0 if prepare_result == APPLY_PLAN_PREPARED else 1

    if args.apply:
        plan_path = resolve_path(repo_root, args.plan)
        plan_text = read_text(plan_path)
        active_task_text = read_text(active_task_path)
        active_task_id = extract_field(active_task_text, "task_id")

        ok_out, out_error, record_path = validate_output_path(
            repo_root,
            args.applied_record_out,
            "missing_applied_record_out",
            "applied_record_out_targets_protected_path",
            "applied_record_out_outside_allowed_locations",
        )

        blocked_reasons = list(base["blocked_reasons"])

        if plan_text is None:
            blocked_reasons.append("missing_apply_plan")
        else:
            plan_result = extract_field(plan_text, "result")
            if plan_result != APPLY_PLAN_PREPARED:
                blocked_reasons.append("apply_plan_not_prepared")

        if not has_task_id(base["task_id"]) or not has_task_id(active_task_id) or str(base["task_id"]) != str(active_task_id):
            blocked_reasons.append("task_identity_mismatch")

        if base["target_state"] != "completed":
            blocked_reasons.append("invalid_target_state")

        if not ok_out and out_error not in blocked_reasons:
            blocked_reasons.append(out_error)

        created = (
            base["transition_text"] is not None
            and base["preconditions_result"] == "PASS"
            and plan_text is not None
            and extract_field(plan_text, "result") == APPLY_PLAN_PREPARED
            and base["target_state"] == "completed"
            and base["task_id"] is not None
            and active_task_id is not None
            and str(base["task_id"]) == str(active_task_id)
            and ok_out
            and record_path is not None
        )

        apply_result = APPLY_EVIDENCE_CREATED if created else APPLY_EVIDENCE_BLOCKED

        if created and record_path is not None:
            write_applied_record(record_path, transition_path, plan_path, base)

        report = {
            "result": apply_result,
            "transition_file": str(transition_path),
            "plan_file": str(plan_path),
            "task_id": base["task_id"],
            "previous_state": base["previous_state"],
            "target_state": base["target_state"],
            "preconditions_result": base["preconditions_result"],
            "would_apply": "YES" if created else "NO",
            "applied_record_out": str(record_path) if record_path else args.applied_record_out,
            "blocked_reasons": blocked_reasons,
            "files_written": "YES" if created else "NO",
            "safety_statement": APPLY_EVIDENCE_SAFETY,
        }
        if args.json:
            print(json.dumps(report, ensure_ascii=True, indent=2))
        else:
            print_apply(report)
        return 0 if apply_result == APPLY_EVIDENCE_CREATED else 1

    if args.complete_active_plan:
        plan_path = resolve_path(repo_root, args.plan)
        applied_record_path = resolve_path(repo_root, args.applied_record)
        plan_text = read_text(plan_path)
        applied_text = read_text(applied_record_path)
        active_text = read_text(active_task_path)

        blocked_reasons = list(base["blocked_reasons"])

        if active_text is None:
            blocked_reasons.append("active_task_missing")
        if plan_text is None:
            blocked_reasons.append("missing_apply_plan")
        if applied_text is None:
            blocked_reasons.append("missing_applied_record")

        apply_plan_result = extract_field(plan_text, "result") or "BLOCKED"
        if apply_plan_result != APPLY_PLAN_PREPARED:
            blocked_reasons.append("apply_plan_not_prepared")

        applied_evidence_result = extract_field(applied_text, "result") or "BLOCKED"
        if applied_evidence_result != APPLY_EVIDENCE_CREATED:
            blocked_reasons.append("applied_evidence_not_created")

        active_task_id = extract_field(active_text, "task_id")
        plan_task_id = extract_field(plan_text, "task_id")
        applied_task_id = extract_field(applied_text, "task_id")

        if not active_task_id or not base["task_id"] or not plan_task_id or not applied_task_id:
            blocked_reasons.append("task_identity_missing")
        elif not (str(active_task_id) == str(base["task_id"]) == str(plan_task_id) == str(applied_task_id)):
            blocked_reasons.append("task_identity_mismatch")

        if base["target_state"] != "completed":
            blocked_reasons.append("invalid_target_state")

        completion_destination_path, destination_err = discover_completion_destination(repo_root)
        if destination_err:
            blocked_reasons.append(destination_err)

        completion_destination = completion_destination_path.as_posix() if completion_destination_path else None
        completion_operation = (
            "copy_active_task_to_completion_destination_and_mark_active_task_completed"
            if completion_destination
            else None
        )
        if completion_operation is None:
            blocked_reasons.append("completion_operation_undetermined")

        allowed_task_paths = build_allowed_task_paths(active_text, completion_destination_path, base.get("task_id"))

        ready = len(blocked_reasons) == 0
        result = COMPLETE_ACTIVE_PLAN_READY if ready else COMPLETE_ACTIVE_PLAN_BLOCKED

        report = {
            "result": result,
            "task_id": base["task_id"],
            "previous_state": base["previous_state"],
            "target_state": base["target_state"],
            "completion_destination": completion_destination,
            "completion_operation": completion_operation,
            "allowed_task_paths": allowed_task_paths,
            "preconditions_result": base["preconditions_result"],
            "apply_plan_result": apply_plan_result,
            "applied_evidence_result": applied_evidence_result,
            "would_mutate": "YES" if ready else "NO",
            "blocked_reasons": blocked_reasons,
            "files_written": "NO",
            "safety_statement": COMPLETE_ACTIVE_PLAN_SAFETY,
        }

        if active_hash_before != sha256_or_empty(active_task_path):
            report["result"] = COMPLETE_ACTIVE_PLAN_BLOCKED
            report["would_mutate"] = "NO"
            if "active_task_changed_during_plan" not in report["blocked_reasons"]:
                report["blocked_reasons"].append("active_task_changed_during_plan")

        if args.json:
            print(json.dumps(report, ensure_ascii=True, indent=2))
        else:
            print_complete_active_plan(report)
        return 0 if report["result"] == COMPLETE_ACTIVE_PLAN_READY else 1

    # complete-active mutation mode
    pre_rc, pre_stdout = run_policy_aware_preconditions_gate(
        repo_root=repo_root,
        transition_path=transition_path,
        active_task_path=active_task_path,
        policy=args.policy,
        approval=args.approval,
    )
    if pre_stdout.strip():
        print(pre_stdout.rstrip())
    pre_blocked = pre_rc != 0 or ("PRECONDITIONS_RESULT: BLOCKED" in pre_stdout)
    if pre_blocked:
        print("CONTROLLED_APPLY_POLICY_GATE: BLOCKED")
        print("APPLY_RESULT: BLOCKED")
        return 1

    if not args.plan:
        print("ERROR: --plan is required when --complete-active is used")
        return 2

    if not args.applied_record:
        print("ERROR: --applied-record is required when --complete-active is used")
        return 2

    if not args.mutation_plan:
        print("ERROR: --mutation-plan is required when --complete-active is used")
        return 2

    plan_path = resolve_path(repo_root, args.plan)
    applied_record_path = resolve_path(repo_root, args.applied_record)
    mutation_plan_path = resolve_path(repo_root, args.mutation_plan)

    plan_text = read_text(plan_path)
    applied_text = read_text(applied_record_path)
    mutation_plan_text = read_text(mutation_plan_path)
    active_text = read_text(active_task_path)

    blocked_reasons = [
        r
        for r in base["blocked_reasons"]
        if r not in {"missing_required_approval", "preconditions_not_passed"}
    ]
    modified_task_paths: list[str] = []

    if active_text is None:
        blocked_reasons.append("active_task_missing")
    if plan_text is None:
        blocked_reasons.append("missing_apply_plan")
    if applied_text is None:
        blocked_reasons.append("missing_applied_record")
    if mutation_plan_text is None:
        blocked_reasons.append("missing_mutation_plan")

    apply_plan_result = extract_field(plan_text, "result") or "BLOCKED"
    if apply_plan_result != APPLY_PLAN_PREPARED:
        blocked_reasons.append("apply_plan_not_prepared")

    applied_evidence_result = extract_field(applied_text, "result") or "BLOCKED"
    if applied_evidence_result != APPLY_EVIDENCE_CREATED:
        blocked_reasons.append("applied_evidence_not_created")

    mutation_plan_result = extract_field(mutation_plan_text, "result") or "BLOCKED"
    if mutation_plan_result != COMPLETE_ACTIVE_PLAN_READY:
        blocked_reasons.append("mutation_plan_not_ready")
    mutation_plan_would_mutate = extract_field(mutation_plan_text, "would_mutate")
    if not is_yes_value(mutation_plan_would_mutate):
        if "mutation_plan_would_mutate_false" not in blocked_reasons:
            blocked_reasons.append("mutation_plan_would_mutate_false")

    active_task_id = extract_field(active_text, "task_id")
    plan_task_id = extract_field(plan_text, "task_id")
    applied_task_id = extract_field(applied_text, "task_id")
    mutation_plan_task_id = extract_field(mutation_plan_text, "task_id")

    if (
        not has_task_id(active_task_id)
        or not has_task_id(base["task_id"])
        or not has_task_id(plan_task_id)
        or not has_task_id(applied_task_id)
        or not has_task_id(mutation_plan_task_id)
    ):
        blocked_reasons.append("task_identity_missing")
    elif not (
        str(active_task_id)
        == str(base["task_id"])
        == str(plan_task_id)
        == str(applied_task_id)
        == str(mutation_plan_task_id)
    ):
        blocked_reasons.append("task_identity_mismatch")

    if base["target_state"] != "completed":
        blocked_reasons.append("invalid_target_state")

    destination_path, destination_err = discover_completion_destination(repo_root)
    if destination_err:
        blocked_reasons.append(destination_err)

    completion_destination = destination_path.as_posix() if destination_path else None
    mutation_plan_destination = extract_field(mutation_plan_text, "completion_destination")
    if completion_destination and mutation_plan_destination and completion_destination != mutation_plan_destination:
        blocked_reasons.append("completion_destination_mismatch")

    if not mutation_plan_destination:
        blocked_reasons.append("mutation_plan_destination_missing")

    mutation_allowed_paths = extract_list_block(mutation_plan_text, "allowed_task_paths")
    if not mutation_allowed_paths:
        blocked_reasons.append("mutation_plan_allowed_paths_missing")

    destination_file = None
    if destination_path and active_task_id:
        destination_file = destination_path / f"{active_task_id}.md"

    required_mutation_paths: list[str] = []
    if destination_file:
        required_mutation_paths.append(destination_file.as_posix())
        required_mutation_paths.append("tasks/active-task.md")

    for rp in required_mutation_paths:
        if rp not in mutation_allowed_paths:
            blocked_reasons.append("mutation_path_not_allowed")
            break

    transition_text = base.get("transition_text")
    approval_required_raw = extract_field(mutation_plan_text, "approval_required")
    approval_is_required = str(approval_required_raw).strip().lower() == "true"
    approval_validation_passed = False

    if approval_is_required and not args.approval:
        # approval is required but no approval record
        blocked_reasons.append("approval is required but no approval record was provided")
    elif args.approval:
        approval_path = resolve_path(repo_root, args.approval)
        approval_text = read_text(approval_path)
        if approval_text is None:
            # approval is required but no approval record
            blocked_reasons.append("approval is required but no approval record was provided")
        else:
            # validate-human-approval
            validator_path = repo_root / "scripts" / "validate-human-approval.py"
            validator = subprocess.run(
                [sys.executable, str(validator_path), str(approval_path)],
                capture_output=True,
                text=True,
            )
            if validator.returncode != 0:
                # approval validation failed
                blocked_reasons.append("approval validation failed")
                for line in (validator.stdout or "").splitlines():
                    line = line.strip()
                    if line:
                        blocked_reasons.append(line)
            else:
                approval_validation_passed = True

            if approval_validation_passed:
                def norm(value: str | None) -> str:
                    if value is None:
                        return ""
                    v = str(value).strip()
                    if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
                        v = v[1:-1].strip()
                    return v

                approval_task_id = norm(extract_field(approval_text, "related_task_id"))
                approval_transition_id = norm(extract_field(approval_text, "related_transition_id"))
                approval_operation = norm(extract_field(approval_text, "allowed_operation"))
                approval_target_state = norm(extract_field(approval_text, "allowed_target_state"))

                transition_id = norm(extract_field(transition_text, "transition_id"))
                task_id = norm(str(base["task_id"]))
                target_state = norm(str(base["target_state"]))

                if approval_task_id != task_id:
                    blocked_reasons.append("approval related_task_id does not match lifecycle task_id")
                if approval_transition_id != transition_id:
                    blocked_reasons.append("approval related_transition_id does not match lifecycle transition_id")
                if approval_operation != "complete-active":
                    blocked_reasons.append("approval allowed_operation does not match lifecycle operation")
                if approval_target_state != target_state:
                    blocked_reasons.append("approval allowed_target_state does not match lifecycle target_state")

    can_apply = len(blocked_reasons) == 0 and destination_file is not None and active_text is not None

    if can_apply:
        # Minimal convention: archive current active-task pointer into completion destination,
        # then keep active-task as completion marker state.
        destination_file.write_text(active_text, encoding="utf-8")
        modified_task_paths.append(destination_file.as_posix())

        completed_marker = (
            f"---\n"
            f"task_id: {active_task_id}\n"
            "state: completed\n"
            f"completed_at: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
            "completed_by: apply-transition.py\n"
            f"source_transition: {transition_path}\n"
            f"source_plan: {plan_path}\n"
            f"source_applied_record: {applied_record_path}\n"
            f"source_mutation_plan: {mutation_plan_path}\n"
            "---\n\n"
            f"# Active Task Completed: {active_task_id}\n"
        )
        active_task_path.write_text(completed_marker, encoding="utf-8")
        modified_task_paths.append("tasks/active-task.md")

    result = COMPLETE_ACTIVE_APPLIED if can_apply else COMPLETE_ACTIVE_BLOCKED

    report = {
        "result": result,
        "task_id": base["task_id"],
        "target_state": base["target_state"],
        "approval_ref": args.approval or "",
        "completion_destination": completion_destination,
        "modified_task_paths": modified_task_paths,
        "blocked_reasons": blocked_reasons,
        "safety_statement": COMPLETE_ACTIVE_MUTATION_SAFETY,
    }

    if not can_apply and active_hash_before != sha256_or_empty(active_task_path):
        report["result"] = COMPLETE_ACTIVE_BLOCKED
        if "active_task_changed_while_blocked" not in report["blocked_reasons"]:
            report["blocked_reasons"].append("active_task_changed_while_blocked")

    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2))
    else:
        print_complete_active(report)

    return 0 if report["result"] == COMPLETE_ACTIVE_APPLIED else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
