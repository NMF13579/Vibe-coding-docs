#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_READINESS = {"PASS", "FAIL", "PARTIAL", "NOT RUN"}


def parse_args(argv: list[str]) -> tuple[argparse.Namespace, list[str]]:
    parser = argparse.ArgumentParser(
        description="Controlled completion command (M14): dry-run and prepare modes."
    )
    parser.add_argument("--dry-run", action="store_true", help="Run dry-run readiness decision")
    parser.add_argument("--prepare", action="store_true", help="Create transition evidence record")
    parser.add_argument("--apply", action="store_true", help="Not implemented in M14")
    parser.add_argument("--session", default="", help="Forwarded to readiness checker")
    parser.add_argument("--active-task", default="", help="Forwarded to readiness checker")
    return parser.parse_known_args(argv)


def parse_readiness_output(stdout: str) -> dict[str, str]:
    out = {
        "readiness_result": "UNKNOWN",
        "stop_reason": "",
        "session": "missing",
        "active_task": "missing",
    }
    for raw_line in stdout.splitlines():
        line = raw_line.strip()
        if line.startswith("readiness_result:"):
            value = line.split(":", 1)[1].strip()
            out["readiness_result"] = value or "UNKNOWN"
        elif line.startswith("stop_reason:"):
            out["stop_reason"] = line.split(":", 1)[1].strip()
        elif line.startswith("session:"):
            out["session"] = line.split(":", 1)[1].strip() or "missing"
        elif line.startswith("active_task:"):
            out["active_task"] = line.split(":", 1)[1].strip() or "missing"

    if out["readiness_result"] not in ALLOWED_READINESS:
        out["readiness_result"] = "UNKNOWN"
    return out


def build_readiness_command(checker_path: Path, args: argparse.Namespace) -> list[str]:
    command = [sys.executable, str(checker_path)]
    if args.active_task:
        command.extend(["--active-task", args.active_task])
    if args.session:
        command.extend(["--session", args.session])
    return command


def run_readiness_checker(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        shell=False,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


def read_task_id(active_task_path: Path) -> str:
    try:
        text = active_task_path.read_text(encoding="utf-8")
    except OSError:
        return "unknown"

    task_id = "unknown"
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("task_id:"):
            value = line.split(":", 1)[1].strip().strip('"').strip("'")
            task_id = value or "unknown"
    return task_id


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def unique_record_path(directory: Path, transition_id: str) -> Path:
    base = directory / f"{transition_id}.md"
    if not base.exists():
        return base

    index = 2
    while True:
        candidate = directory / f"{transition_id}-{index}.md"
        if not candidate.exists():
            return candidate
        index += 1


def format_record(
    transition_id: str,
    task_id: str,
    status: str,
    readiness_result: str,
    stop_reason: str,
    created_at: str,
) -> str:
    final_stop = "none" if readiness_result == "PASS" else (stop_reason or "readiness_fail")
    lines = [
        f"transition_id: {transition_id}",
        f"task_id: {task_id}",
        f"status: {status}",
        f"completion_readiness_result: {readiness_result}",
        f"stop_reason: {final_stop}",
        f"created_at: {created_at}",
        "created_by: controlled-completion-gate",
        "notes:",
        "  - evidence only",
        "  - lifecycle not mutated",
        "  - status applied is forbidden in M14",
        "",
    ]
    return "\n".join(lines)


def print_dry_run_report(
    dry_run_result: str,
    completion_allowed: str,
    would_prepare_transition: str,
    readiness_result: str,
    stop_reason: str,
    message: str,
    session: str,
    active_task: str,
    command_text: str,
    checker_exit_code: str,
) -> None:
    print("Complete Active Task Dry Run")
    print(f"dry_run_result: {dry_run_result}")
    print(f"completion_allowed: {completion_allowed}")
    print(f"would_prepare_transition: {would_prepare_transition}")
    print("would_apply_transition: NO")
    print(f"readiness_result: {readiness_result}")
    print(f"stop_reason: {stop_reason}")
    print(f"message: {message}")
    print(f"session: {session}")
    print(f"active_task: {active_task}")
    print("Readiness Checker:")
    print(f"- command: {command_text}")
    print(f"- exit_code: {checker_exit_code}")
    print("Safety:")
    print("- script_is_read_only: YES")
    print("- active_task_mutated: NO")
    print("- queue_mutated: NO")
    print("- task_moved_to_done: NO")
    print("- task_moved_to_failed: NO")
    print("- completion_applied: NO")
    print("- transition_record_created: NO")
    print("- approval_record_created: NO")


def print_prepare_report(
    prepare_result: str,
    transition_record: str,
    transition_status: str,
    readiness_result: str,
    stop_reason: str,
) -> None:
    print("Complete Active Task Prepare")
    print(f"prepare_result: {prepare_result}")
    print(f"transition_record: {transition_record}")
    print(f"transition_status: {transition_status}")
    print(f"completion_readiness_result: {readiness_result}")
    print(f"stop_reason: {stop_reason}")
    print("Decision:")
    if prepare_result == "PREPARE_CREATED":
        print("- completion_transition_prepared: YES")
        print("- completion_transition_blocked: NO")
    elif prepare_result == "PREPARE_BLOCKED":
        print("- completion_transition_prepared: NO")
        print("- completion_transition_blocked: YES")
    else:
        print("- completion_transition_prepared: NO")
        print("- completion_transition_blocked: NO")
    print("- lifecycle_mutation_applied: NO")


def handle_usage_error(stop_reason: str, message: str) -> int:
    print_dry_run_report(
        dry_run_result="ERROR",
        completion_allowed="NO",
        would_prepare_transition="NO",
        readiness_result="UNKNOWN",
        stop_reason=stop_reason,
        message=message,
        session="missing",
        active_task="missing",
        command_text="NOT RUN",
        checker_exit_code="NOT RUN",
    )
    return 2


def execute_checker(repo_root: Path, args: argparse.Namespace) -> tuple[str, int, dict[str, str], str]:
    checker_path = repo_root / "scripts" / "check-completion-readiness.py"
    if not checker_path.is_file():
        return "MISSING", 2, {
            "readiness_result": "UNKNOWN",
            "stop_reason": "readiness_checker_missing",
            "session": "missing",
            "active_task": "missing",
        }, "NOT RUN"

    command = build_readiness_command(checker_path, args)
    command_text = " ".join(command)

    try:
        proc = run_readiness_checker(command)
    except subprocess.TimeoutExpired:
        return "TIMEOUT", 2, {
            "readiness_result": "UNKNOWN",
            "stop_reason": "checker_timeout",
            "session": "missing",
            "active_task": "missing",
        }, command_text
    except (OSError, subprocess.SubprocessError):
        return "ERROR", 2, {
            "readiness_result": "UNKNOWN",
            "stop_reason": "checker_error",
            "session": "missing",
            "active_task": "missing",
        }, command_text

    parsed = parse_readiness_output(proc.stdout)
    if parsed["readiness_result"] == "UNKNOWN":
        if proc.returncode == 0:
            return "PARSE_ERROR", 2, {
                "readiness_result": "UNKNOWN",
                "stop_reason": "checker_parse_error",
                "session": parsed["session"],
                "active_task": parsed["active_task"],
            }, command_text
        return "BLOCKED_PARSE_ERROR", 1, {
            "readiness_result": "UNKNOWN",
            "stop_reason": "checker_parse_error",
            "session": parsed["session"],
            "active_task": parsed["active_task"],
        }, command_text

    parsed["checker_exit_code"] = str(proc.returncode)
    return "OK", proc.returncode, parsed, command_text


def run_dry_run(repo_root: Path, args: argparse.Namespace) -> int:
    state, checker_exit, parsed, command_text = execute_checker(repo_root, args)

    if state == "MISSING":
        print_dry_run_report("ERROR", "NO", "NO", "UNKNOWN", "readiness_checker_missing", "scripts/check-completion-readiness.py not found", "missing", "missing", "NOT RUN", "NOT RUN")
        return 2
    if state == "TIMEOUT":
        print_dry_run_report("ERROR", "NO", "NO", "UNKNOWN", "readiness_checker_timeout", "readiness checker timed out", "missing", "missing", command_text, "NOT RUN")
        return 2
    if state == "ERROR":
        print_dry_run_report("ERROR", "NO", "NO", "UNKNOWN", "readiness_checker_error", "readiness checker execution failed", "missing", "missing", command_text, "NOT RUN")
        return 2
    if state == "PARSE_ERROR":
        print_dry_run_report("ERROR", "NO", "NO", "UNKNOWN", "readiness_checker_parse_error", "checker exit 0 without explicit readiness_result: PASS", parsed["session"], parsed["active_task"], command_text, "0")
        return 2
    if state == "BLOCKED_PARSE_ERROR":
        print_dry_run_report("DRY_RUN_BLOCKED", "NO", "NO", "UNKNOWN", "readiness_checker_parse_error", "checker output missing or unrecognized readiness_result", parsed["session"], parsed["active_task"], command_text, str(checker_exit))
        return 1

    readiness_result = parsed["readiness_result"]
    stop_reason = parsed["stop_reason"]
    session = parsed["session"]
    active_task = parsed["active_task"]

    if checker_exit == 0 and readiness_result == "PASS":
        print_dry_run_report("DRY_RUN_PASS", "YES", "YES", "PASS", "", "", session, active_task, command_text, str(checker_exit))
        return 0

    if readiness_result in {"FAIL", "PARTIAL", "NOT RUN"}:
        print_dry_run_report("DRY_RUN_BLOCKED", "NO", "NO", readiness_result, stop_reason, "", session, active_task, command_text, str(checker_exit))
        return 1

    print_dry_run_report("ERROR", "NO", "NO", "UNKNOWN", "readiness_checker_parse_error", "readiness result mapping failed", session, active_task, command_text, str(checker_exit))
    return 2


def run_prepare(repo_root: Path, args: argparse.Namespace) -> int:
    state, checker_exit, parsed, _command_text = execute_checker(repo_root, args)

    if state == "MISSING":
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "readiness_checker_missing")
        return 2
    if state == "TIMEOUT":
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "checker_timeout")
        return 2
    if state == "ERROR":
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "checker_error")
        return 2
    if state == "PARSE_ERROR":
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "checker_parse_error")
        return 2
    if state == "BLOCKED_PARSE_ERROR":
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "checker_parse_error")
        return 2

    readiness_result = parsed["readiness_result"]
    stop_reason = parsed["stop_reason"]

    if readiness_result == "PASS":
        status = "prepared"
        prepare_result = "PREPARE_CREATED"
        exit_code = 0
    elif readiness_result in {"FAIL", "PARTIAL", "NOT RUN"}:
        status = "blocked"
        prepare_result = "PREPARE_BLOCKED"
        exit_code = 1
    else:
        print_prepare_report("PREPARE_ERROR", "none", "none", "ERROR", "checker_parse_error")
        return 2

    completion_dir = repo_root / "reports" / "completion"
    completion_dir.mkdir(parents=True, exist_ok=True)

    active_task_arg = args.active_task or "tasks/active-task.md"
    active_task_path = Path(active_task_arg)
    if not active_task_path.is_absolute():
        active_task_path = repo_root / active_task_path
    task_id = read_task_id(active_task_path)

    transition_id = f"completion-{task_id}-{utc_timestamp()}"
    record_path = unique_record_path(completion_dir, transition_id)
    record_text = format_record(
        transition_id=record_path.stem,
        task_id=task_id,
        status=status,
        readiness_result=readiness_result,
        stop_reason=stop_reason,
        created_at=utc_iso(),
    )
    record_path.write_text(record_text, encoding="utf-8")

    print_prepare_report(
        prepare_result=prepare_result,
        transition_record=str(record_path),
        transition_status=status,
        readiness_result=readiness_result,
        stop_reason=("none" if readiness_result == "PASS" else (stop_reason or "readiness_fail")),
    )
    return exit_code


def main(argv: list[str]) -> int:
    args, unknown = parse_args(argv)

    if unknown:
        return handle_usage_error("invalid_arguments", f"unsupported argument: {unknown[0]}")

    if args.apply:
        return handle_usage_error("APPLY_NOT_IMPLEMENTED_IN_M14", "--apply is forbidden in M14")

    if args.dry_run and args.prepare:
        return handle_usage_error("MODE_CONFLICT", "only one mode may be specified at a time")

    if not args.dry_run and not args.prepare:
        return handle_usage_error("USAGE_ERROR", "pass --dry-run or --prepare")

    repo_root = Path(__file__).resolve().parent.parent

    if args.dry_run:
        return run_dry_run(repo_root, args)

    return run_prepare(repo_root, args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
