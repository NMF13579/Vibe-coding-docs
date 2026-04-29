#!/usr/bin/env python3
"""Controlled execution runner MVP: dry-run and start."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


DRY_RUN_PASS = 0
DRY_RUN_BLOCKED = 1
DRY_RUN_NOT_RUN = 2
STARTED = 0
START_BLOCKED = 1
START_NOT_RUN = 2


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AgentOS controlled execution runner (dry-run/start)."
    )
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--dry-run",
        action="store_true",
        help="Run readiness gate only and report whether execution could start.",
    )
    mode_group.add_argument(
        "--start",
        action="store_true",
        help="Create execution session/attempt record after readiness check.",
    )
    parser.add_argument(
        "--active-task",
        default="tasks/active-task.md",
        help="Path to active task pointer file (default: tasks/active-task.md)",
    )
    parser.add_argument(
        "--approval-dir",
        default=None,
        help="Optional approval directory override passed to readiness checker.",
    )
    return parser.parse_args(argv)


def has_parent_traversal(path_text: str) -> bool:
    return ".." in Path(path_text).parts


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sanitize_task_id(task_id: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", task_id.strip())
    cleaned = cleaned.strip("-._")
    return cleaned or "unknown-task"


def validate_active_task_arg(repo_root: Path, active_task_arg: str) -> tuple[bool, Path | None, str | None]:
    active_path = Path(active_task_arg)
    if has_parent_traversal(active_task_arg):
        return False, None, "invalid active task path: parent traversal is forbidden"
    if active_path.is_absolute():
        return False, None, "invalid active task path: absolute paths are forbidden"
    resolved = repo_root / active_path
    if not resolved.exists():
        return False, None, f"invalid active task path: file does not exist: {active_task_arg}"
    if not resolved.is_file():
        return False, None, f"invalid active task path: not a file: {active_task_arg}"
    return True, resolved, None


def validate_approval_dir(repo_root: Path, approval_dir_arg: str) -> tuple[bool, str | None, str | None]:
    if has_parent_traversal(approval_dir_arg):
        return False, "approval-dir contains parent traversal ('..')", None

    approval_path = Path(approval_dir_arg)
    if approval_path.is_absolute():
        if not approval_path.exists():
            return False, "absolute approval-dir does not exist", None
        if not approval_path.is_dir():
            return False, "absolute approval-dir exists but is not a directory", None
        return True, None, None

    repo_relative = repo_root / approval_path
    if repo_relative.exists() and not repo_relative.is_dir():
        return (
            False,
            "relative approval-dir exists but is not a directory",
            None,
        )
    if not repo_relative.exists():
        return True, None, (
            f"warning: relative approval-dir does not exist yet: {approval_dir_arg} "
            "(continuing as pass-through)"
        )
    return True, None, None


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    data: dict[str, str] = {}
    end_idx = None
    for idx, line in enumerate(lines[1:], start=1):
        stripped = line.strip()
        if stripped == "---":
            end_idx = idx
            break
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            return None, f"malformed frontmatter line: {line}"
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    if end_idx is None:
        return None, "missing YAML frontmatter terminator"
    return data, None


def shell_safe_display(parts: list[str]) -> str:
    return " ".join(parts)


def run_readiness(
    repo_root: Path,
    active_task_input: str,
    approval_dir: str | None,
) -> tuple[int | None, str | None, str, str]:
    command = [
        sys.executable,
        "scripts/check-execution-readiness.py",
        "--active-task",
        active_task_input,
    ]
    if approval_dir is not None:
        command.extend(["--approval-dir", approval_dir])
    cmd_text = shell_safe_display(command)
    try:
        completed = subprocess.run(
            command,
            cwd=str(repo_root),
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return None, f"subprocess error: {exc}", "", cmd_text
    output = ((completed.stdout or "") + (completed.stderr or "")).strip()
    return completed.returncode, None, output, cmd_text


def print_dry_run_report(
    *,
    active_task: str,
    readiness_command: str,
    readiness_result: str,
    would_create_session: str,
    would_allow_steps: str,
    result_label: str,
    reason: str | None = None,
    stop_reason_note: str | None = None,
    readiness_output: str | None = None,
    warning: str | None = None,
) -> None:
    print("AgentOS Controlled Execution Runner — Dry Run")
    print()
    print("Active task:")
    print(f"- {active_task}")
    print()
    print("Readiness command:")
    print(f"- {readiness_command}")
    print()
    print("Readiness result:")
    print(f"- {readiness_result}")
    if reason:
        print()
        print("Reason:")
        print(f"- {reason}")
    if stop_reason_note:
        print()
        print("Stop reason if recorded in future:")
        print(f"- {stop_reason_note}")
    print()
    print("Would create execution session:")
    print(f"- {would_create_session}")
    print()
    print("Would allow execution steps:")
    print(f"- {would_allow_steps}")
    print()
    print("Would modify files:")
    print("- no")
    if warning:
        print()
        print("Warning:")
        print(f"- {warning}")
    if readiness_output:
        print()
        print("Readiness output:")
        print(readiness_output.strip())
    print()
    print("Result:")
    print(f"- {result_label}")


def print_start_report(
    *,
    active_task: str,
    readiness_command: str,
    readiness_result: str,
    session: str,
    status: str,
    stop_reason: str,
    result_label: str,
    reason: str | None = None,
    readiness_output: str | None = None,
    warning: str | None = None,
) -> None:
    print("AgentOS Controlled Execution Runner — Start")
    print()
    print("Active task:")
    print(f"- {active_task}")
    print()
    print("Readiness command:")
    print(f"- {readiness_command}")
    print()
    print("Readiness result:")
    print(f"- {readiness_result}")
    print()
    print("Session:")
    print(f"- {session}")
    print()
    print("Status:")
    print(f"- {status}")
    print()
    print("Stop reason:")
    print(f"- {stop_reason}")
    if reason:
        print()
        print("Reason:")
        print(f"- {reason}")
    print()
    print("Execution steps allowed:")
    print("- yes, but this command did not execute the task" if status == "in_progress" else "- no")
    print()
    print("Task implementation performed:")
    print("- no")
    print()
    print("Verification run:")
    print("- no")
    if warning:
        print()
        print("Warning:")
        print(f"- {warning}")
    if readiness_output:
        print()
        print("Readiness output:")
        print(readiness_output.strip())
    print()
    print("Result:")
    print(f"- {result_label}")


def make_session_content(
    *,
    session_id: str,
    task_id: str,
    active_task: str,
    snapshot: dict[str, str],
    source_task: str,
    source_contract: str,
    readiness_result: str,
    readiness_checked_at: str,
    status: str,
    stop_reason: str,
    started_at: str,
    readiness_command: str,
    readiness_output: str,
    notes: list[str],
) -> str:
    safe_output = readiness_output.strip() if readiness_output else "No output."
    notes_text = "\n".join([f"- {item}" for item in notes]) if notes else "- none"
    return f"""---
session_id: "{session_id}"
task_id: "{task_id}"
active_task: "{active_task}"
active_task_snapshot:
  task_id: "{snapshot.get('task_id', '')}"
  state: "{snapshot.get('state', '')}"
  activated_at: "{snapshot.get('activated_at', '')}"
  activated_by: "{snapshot.get('activated_by', '')}"
  approval_id: "{snapshot.get('approval_id', '')}"
  source_task: "{snapshot.get('source_task', '')}"
  source_contract: "{snapshot.get('source_contract', '')}"
  transition: "{snapshot.get('transition', '')}"
source_task: "{source_task}"
source_contract: "{source_contract}"
readiness_result: "{readiness_result}"
readiness_checked_at: "{readiness_checked_at}"
status: "{status}"
stop_reason: "{stop_reason}"
started_at: "{started_at}"
started_by: "controlled-execution-runner"
changed_files: []
verification_evidence: []
---

# Execution Session

## Purpose
This file records a controlled execution session or blocked execution attempt.

## Active Task Snapshot
- task_id: `{snapshot.get('task_id', '')}`
- state: `{snapshot.get('state', '')}`
- activated_at: `{snapshot.get('activated_at', '')}`
- activated_by: `{snapshot.get('activated_by', '')}`
- approval_id: `{snapshot.get('approval_id', '')}`
- source_task: `{snapshot.get('source_task', '')}`
- source_contract: `{snapshot.get('source_contract', '')}`
- transition: `{snapshot.get('transition', '')}`

## Readiness Evidence
- command: `{readiness_command}`
- readiness_result: `{readiness_result}`
- readiness_checked_at: `{readiness_checked_at}`

Readiness output:
```text
{safe_output}
```

## Execution Log
No task implementation was performed by start command.

## Changed Files
None recorded by start command.

## Verification Evidence
No verification plan was run by start command.

## Stop Reason
{stop_reason if stop_reason else "empty"}

## Completion Boundary
This session does not complete the task.
Completion remains a separate lifecycle transition.

## Notes
{notes_text}
"""


def create_session_file_exclusive(
    repo_root: Path,
    task_id: str,
    content_factory,
) -> tuple[Path, str]:
    reports_dir = repo_root / "reports" / "execution"
    reports_dir.mkdir(parents=True, exist_ok=True)
    base = f"exec-{sanitize_task_id(task_id)}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    index = 0
    while True:
        suffix = "" if index == 0 else f"-{index:03d}"
        session_name = f"{base}{suffix}.md"
        path = reports_dir / session_name
        try:
            with path.open("x", encoding="utf-8") as file_obj:
                content = content_factory(path.stem)
                file_obj.write(content)
            return path, path.stem
        except FileExistsError:
            index += 1


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent
    active_task_input = args.active_task
    checker_path = repo_root / "scripts" / "check-execution-readiness.py"

    active_ok, active_task_path, active_err = validate_active_task_arg(repo_root, active_task_input)
    default_cmd = shell_safe_display(
        [sys.executable, "scripts/check-execution-readiness.py", "--active-task", active_task_input]
    )
    if not active_ok or active_task_path is None:
        if args.dry_run:
            print_dry_run_report(
                active_task=active_task_input,
                readiness_command=default_cmd,
                readiness_result="NOT RUN",
                reason=active_err or "invalid active task path",
                would_create_session="no",
                would_allow_steps="no",
                result_label="DRY_RUN_NOT_RUN",
            )
            return DRY_RUN_NOT_RUN
        print_start_report(
            active_task=active_task_input,
            readiness_command=default_cmd,
            readiness_result="NOT RUN",
            session="not created",
            status="blocked",
            stop_reason="readiness_fail",
            reason=active_err or "invalid active task path",
            result_label="START_NOT_RUN",
        )
        return START_NOT_RUN

    warning: str | None = None
    if args.approval_dir is not None:
        ok, err, warn = validate_approval_dir(repo_root, args.approval_dir)
        if not ok:
            cmd_with_approval = shell_safe_display(
                [
                    sys.executable,
                    "scripts/check-execution-readiness.py",
                    "--active-task",
                    active_task_input,
                    "--approval-dir",
                    args.approval_dir,
                ]
            )
            if args.dry_run:
                print_dry_run_report(
                    active_task=active_task_input,
                    readiness_command=cmd_with_approval,
                    readiness_result="NOT RUN",
                    reason=err,
                    would_create_session="no",
                    would_allow_steps="no",
                    result_label="DRY_RUN_NOT_RUN",
                )
                return DRY_RUN_NOT_RUN
            print_start_report(
                active_task=active_task_input,
                readiness_command=cmd_with_approval,
                readiness_result="NOT RUN",
                session="not created",
                status="blocked",
                stop_reason="readiness_fail",
                reason=err,
                result_label="START_NOT_RUN",
            )
            return START_NOT_RUN
        warning = warn

    code: int | None = None
    run_err: str | None = None
    readiness_output = ""
    readiness_command = default_cmd
    readiness_checked_at = utc_now_iso()

    if checker_path.is_file():
        code, run_err, readiness_output, readiness_command = run_readiness(
            repo_root, active_task_input, args.approval_dir
        )
        readiness_checked_at = utc_now_iso()
    else:
        run_err = "missing checker: scripts/check-execution-readiness.py"
        readiness_output = ""

    if args.dry_run:
        if run_err is not None:
            print_dry_run_report(
                active_task=active_task_input,
                readiness_command=readiness_command,
                readiness_result="NOT RUN",
                reason=run_err,
                would_create_session="no",
                would_allow_steps="no",
                result_label="DRY_RUN_NOT_RUN",
                warning=warning,
            )
            return DRY_RUN_NOT_RUN
        if code == 0:
            print_dry_run_report(
                active_task=active_task_input,
                readiness_command=readiness_command,
                readiness_result="PASS",
                would_create_session="yes, in future --start mode",
                would_allow_steps="yes, only after future --start creates a controlled execution session",
                result_label="DRY_RUN_PASS",
                readiness_output=readiness_output or None,
                warning=warning,
            )
            return DRY_RUN_PASS
        if code == 1:
            print_dry_run_report(
                active_task=active_task_input,
                readiness_command=readiness_command,
                readiness_result="BLOCKED",
                would_create_session="no in dry-run; future --start may create blocked attempt record",
                would_allow_steps="no",
                result_label="DRY_RUN_BLOCKED",
                stop_reason_note="readiness_fail",
                readiness_output=readiness_output or None,
                warning=warning,
            )
            return DRY_RUN_BLOCKED
        reason = (
            run_err
            if run_err is not None
            else f"unexpected readiness checker exit code {code}"
        )
        print_dry_run_report(
            active_task=active_task_input,
            readiness_command=readiness_command,
            readiness_result="NOT RUN",
            reason=reason,
            would_create_session="no",
            would_allow_steps="no",
            result_label="DRY_RUN_NOT_RUN",
            readiness_output=readiness_output or None,
            warning=warning,
        )
        return DRY_RUN_NOT_RUN

    # --start mode
    try:
        active_text = active_task_path.read_text(encoding="utf-8")
    except OSError:
        print_start_report(
            active_task=active_task_input,
            readiness_command=readiness_command,
            readiness_result="NOT RUN",
            session="not created",
            status="blocked",
            stop_reason="readiness_fail",
            reason="invalid or unreadable active task",
            result_label="START_NOT_RUN",
            warning=warning,
        )
        return START_NOT_RUN
    frontmatter, fm_err = parse_frontmatter(active_text)
    required = [
        "task_id",
        "state",
        "activated_at",
        "activated_by",
        "approval_id",
        "source_task",
        "source_contract",
        "transition",
    ]
    if fm_err is not None or frontmatter is None:
        print_start_report(
            active_task=active_task_input,
            readiness_command=readiness_command,
            readiness_result="NOT RUN",
            session="not created",
            status="blocked",
            stop_reason="readiness_fail",
            reason="invalid or unreadable active task",
            result_label="START_NOT_RUN",
            warning=warning,
        )
        return START_NOT_RUN
    missing = [k for k in required if not frontmatter.get(k, "").strip()]
    if missing:
        print_start_report(
            active_task=active_task_input,
            readiness_command=readiness_command,
            readiness_result="NOT RUN",
            session="not created",
            status="blocked",
            stop_reason="readiness_fail",
            reason=f"invalid or unreadable active task (missing fields: {', '.join(missing)})",
            result_label="START_NOT_RUN",
            warning=warning,
        )
        return START_NOT_RUN

    snapshot = {k: frontmatter.get(k, "") for k in required}
    task_id = snapshot["task_id"]
    source_task = snapshot["source_task"]
    source_contract = snapshot["source_contract"]

    if run_err is not None:
        readiness_result = "NOT RUN"
        status = "blocked"
        stop_reason = "readiness_fail"
        result_label = "START_NOT_RUN"
        exit_code = START_NOT_RUN
        reason = run_err
    elif code == 0:
        readiness_result = "PASS"
        status = "in_progress"
        stop_reason = ""
        result_label = "STARTED"
        exit_code = STARTED
        reason = None
    elif code == 1:
        readiness_result = "FAIL"
        status = "blocked"
        stop_reason = "readiness_fail"
        result_label = "START_BLOCKED"
        exit_code = START_BLOCKED
        reason = None
    elif code == 2:
        readiness_result = "NOT RUN"
        status = "blocked"
        stop_reason = "readiness_fail"
        result_label = "START_NOT_RUN"
        exit_code = START_NOT_RUN
        reason = "readiness checker returned NOT RUN"
    else:
        readiness_result = "NOT RUN"
        status = "blocked"
        stop_reason = "readiness_fail"
        result_label = "START_NOT_RUN"
        exit_code = START_NOT_RUN
        reason = f"unexpected readiness checker exit code {code}"

    notes: list[str] = []
    if warning:
        notes.append(warning)
    if reason:
        notes.append(reason)

    session_path, _session_id = create_session_file_exclusive(
        repo_root,
        task_id,
        lambda generated_session_id: make_session_content(
            session_id=generated_session_id,
            task_id=task_id,
            active_task=active_task_input,
            snapshot=snapshot,
            source_task=source_task,
            source_contract=source_contract,
            readiness_result=readiness_result,
            readiness_checked_at=readiness_checked_at,
            status=status,
            stop_reason=stop_reason,
            started_at=utc_now_iso(),
            readiness_command=readiness_command,
            readiness_output=readiness_output,
            notes=notes,
        ),
    )

    print_start_report(
        active_task=active_task_input,
        readiness_command=readiness_command,
        readiness_result=readiness_result,
        session=str(session_path.relative_to(repo_root)),
        status=status,
        stop_reason=stop_reason if stop_reason else "empty",
        result_label=result_label,
        reason=reason,
        readiness_output=readiness_output or None,
        warning=warning,
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
