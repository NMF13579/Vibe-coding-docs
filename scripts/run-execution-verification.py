#!/usr/bin/env python3
"""Execution verification runner MVP."""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VERIFICATION_PASS = 0
VERIFICATION_FAIL = 1
VERIFICATION_PARTIAL_OR_NOT_RUN = 2

ALLOWED_EXECUTABLES = {"python3", "python", "bash", "git"}
ALLOWED_GIT_SUBCOMMANDS = {"diff", "status", "log", "show", "ls-files"}
SHELL_OPERATORS = {"|", "&&", "||", ";", ">", ">>", "<", "`", "$("}
LIFECYCLE_FLAGS = {"--complete", "--fail", "--drop", "--rollback", "--approve"}
PATHLIKE_EXTS = (".py", ".sh", ".md", ".txt", ".json", ".yaml", ".yml")
MAX_SUMMARY_CHARS = 4000
MAX_SUMMARY_LINES = 20
DEFAULT_TIMEOUT_SECONDS = 30


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run verification commands from source_contract.")
    parser.add_argument("--session", required=True, help="Execution session file path (repository-relative).")
    parser.add_argument("--dry-run", action="store_true", help="Preview verification commands without execution.")
    return parser.parse_args(argv)


def now_iso_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    data: dict[str, object] = {}
    current_key: str | None = None
    idx = 1
    while idx < len(lines):
        line = lines[idx]
        if line.strip() == "---":
            return data, None

        if not line.strip() or line.strip().startswith("#"):
            idx += 1
            continue

        if line.startswith((" ", "\t")):
            stripped = line.strip()
            if current_key and stripped.startswith("- "):
                current_val = data.get(current_key)
                if not isinstance(current_val, list):
                    current_val = []
                    data[current_key] = current_val
                current_val.append(strip_quotes(stripped[2:].strip()))
            idx += 1
            continue

        if ":" not in line:
            return None, f"malformed frontmatter line: {line}"

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        current_key = key

        if value == "":
            data[key] = []
        elif value == "[]":
            data[key] = []
        else:
            data[key] = strip_quotes(value)
        idx += 1

    return None, "missing YAML frontmatter terminator"


def path_is_safe_rel(path_text: str) -> bool:
    if not path_text.strip():
        return False
    p = Path(path_text)
    if p.is_absolute():
        return False
    if ".." in p.parts:
        return False
    return True


def validate_repo_file_path(repo_root: Path, path_text: str) -> tuple[bool, Path | None, str | None]:
    if not path_is_safe_rel(path_text):
        return False, None, "invalid path: must be repository-relative and without parent traversal"
    p = repo_root / Path(path_text)
    if not p.exists():
        return False, None, "path does not exist"
    if not p.is_file():
        return False, None, "path is not a file"
    return True, p, None


def parse_verification_from_markdown(text: str) -> list[str]:
    commands: list[str] = []
    mode = False
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        if lower in {"## verification plan", "### verification plan", "## verification", "### verification"}:
            mode = True
            continue
        if stripped.startswith("#"):
            mode = False
            continue
        if mode and stripped.startswith("- "):
            cmd = strip_quotes(stripped[2:].strip())
            if cmd:
                commands.append(cmd)
    return commands


def extract_verification_plan(contract_text: str) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    plan: list[str] = []
    fm, fm_err = parse_frontmatter(contract_text)
    if fm_err is None and fm is not None:
        v = fm.get("verification_plan")
        if isinstance(v, list):
            plan.extend([str(x).strip() for x in v if str(x).strip()])
        elif isinstance(v, str) and v.strip():
            plan.append(v.strip())
    else:
        warnings.append("source_contract frontmatter not parseable; using markdown heading fallback")

    if not plan:
        plan = parse_verification_from_markdown(contract_text)
    return plan, warnings


def summarize_output(text: str) -> str:
    if not text:
        return ""
    clipped = text[:MAX_SUMMARY_CHARS]
    lines = clipped.splitlines()[:MAX_SUMMARY_LINES]
    return "\n".join(lines).strip()


def looks_pathlike(token: str) -> bool:
    t = token.strip()
    if not t:
        return False
    if "/" in t:
        return True
    return t.endswith(PATHLIKE_EXTS)


def has_shell_operators(raw_command: str, tokens: list[str]) -> bool:
    for op in SHELL_OPERATORS:
        if op in raw_command:
            return True
    for t in tokens:
        if t in SHELL_OPERATORS:
            return True
    return False


def command_is_lifecycle_mutation(tokens: list[str]) -> bool:
    if len(tokens) < 2:
        return False
    normalized = [t.strip() for t in tokens]
    if "scripts/run-active-task.py" not in normalized:
        return False
    return any(flag in normalized for flag in LIFECYCLE_FLAGS)


def check_command_safety(command: str) -> tuple[bool, str | None, list[str] | None]:
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False, "command parse error", None

    if not tokens:
        return False, "command parse error", None

    exe = tokens[0].strip()
    if Path(exe).is_absolute() or ".." in Path(exe).parts:
        return False, "unsafe executable path", tokens
    if exe not in ALLOWED_EXECUTABLES:
        return False, "unsupported executable", tokens

    if exe == "git":
        if len(tokens) < 2:
            return False, "unsupported git subcommand", tokens
        subcmd = tokens[1].strip()
        if subcmd not in ALLOWED_GIT_SUBCOMMANDS:
            return False, "unsupported git subcommand", tokens

    if has_shell_operators(command, tokens):
        return False, "unsupported verification command format: shell operators not allowed", tokens

    for arg in tokens[1:]:
        if looks_pathlike(arg):
            if not arg.strip():
                return False, "unsafe path-like argument in verification command", tokens
            p = Path(arg)
            if p.is_absolute() or ".." in p.parts:
                return False, "unsafe path-like argument in verification command", tokens

    if command_is_lifecycle_mutation(tokens):
        return False, "lifecycle mutation command is not supported by verification runner", tokens

    return True, None, tokens


def print_not_run(
    *,
    session: str,
    source_contract: str,
    reason: str,
    verification_plan: list[str] | None = None,
    dry_run: bool = False,
) -> None:
    title = "AgentOS Execution Verification Runner — Dry Run" if dry_run else "AgentOS Execution Verification Runner"
    print(title)
    print()
    print("Session:")
    print(f"- {session}")
    print()
    print("Source contract:")
    print(f"- {source_contract}")
    if dry_run:
        print()
        print("Would run:")
        if verification_plan:
            for cmd in verification_plan:
                print(f"- {cmd}")
        else:
            print("- none")
        print()
        print("Would modify files:")
        print("- no")
    print()
    print("Reason:")
    print(f"- {reason}")
    print()
    print("Result:")
    print("- NOT RUN")


def print_result(
    *,
    session: str,
    source_contract: str,
    verification_plan: list[str],
    command_results: list[dict[str, object]],
    warnings: list[str],
    result: str,
) -> None:
    print("AgentOS Execution Verification Runner")
    print()
    print("Session:")
    print(f"- {session}")
    print()
    print("Source contract:")
    print(f"- {source_contract}")
    print()
    print("Verification plan:")
    if verification_plan:
        for cmd in verification_plan:
            print(f"- {cmd}")
    else:
        print("- none")
    print()
    print("Commands run:")
    ran_any = False
    for entry in command_results:
        if bool(entry.get("ran")):
            ran_any = True
            print(f"- command: {entry['command']}")
            print(f"  status: {entry['status']}")
            print(f"  exit_code: {entry['exit_code']}")
    if not ran_any:
        print("- none")

    print()
    print("Verification evidence:")
    for entry in command_results:
        print(f"- command: {entry['command']}")
        print(f"  status: {entry['status']}")
        print(f"  exit_code: {entry['exit_code']}")
        if entry.get("reason"):
            print(f"  reason: {entry['reason']}")
        if entry.get("ran_at"):
            print(f"  ran_at: {entry['ran_at']}")
        if entry.get("stdout_summary"):
            print("  stdout_summary:")
            print("    " + str(entry["stdout_summary"]).replace("\n", "\n    "))
        if entry.get("stderr_summary"):
            print("  stderr_summary:")
            print("    " + str(entry["stderr_summary"]).replace("\n", "\n    "))

    print()
    print("Warnings:")
    if warnings:
        for w in warnings:
            print(f"- {w}")
    else:
        print("- none")
    print()
    print("Result:")
    print(f"- {result}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    ok, session_path, err = validate_repo_file_path(repo_root, args.session)
    if not ok or session_path is None:
        print_not_run(session=args.session, source_contract="unknown", reason=f"invalid session path: {err}")
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    try:
        session_text = session_path.read_text(encoding="utf-8")
    except OSError as exc:
        print_not_run(
            session=args.session,
            source_contract="unknown",
            reason=f"cannot read session file: {exc}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    session_fm, fm_err = parse_frontmatter(session_text)
    if fm_err or session_fm is None:
        print_not_run(
            session=args.session,
            source_contract="unknown",
            reason=f"unreadable session frontmatter: {fm_err}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    required = [
        "session_id",
        "task_id",
        "source_contract",
        "status",
        "readiness_result",
        "changed_files",
        "verification_evidence",
    ]
    missing = [k for k in required if k not in session_fm]
    if missing:
        print_not_run(
            session=args.session,
            source_contract=str(session_fm.get("source_contract", "unknown")),
            reason=f"missing required session fields: {', '.join(missing)}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    status = str(session_fm.get("status", "")).strip().strip('"')
    source_contract_rel = str(session_fm.get("source_contract", "")).strip().strip('"')
    if status == "blocked":
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            reason="blocked session cannot run verification",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN
    if status == "stopped":
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            reason="stopped session requires separate review before verification",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN
    if status not in {"in_progress", "evidence_ready"}:
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            reason=f"unsupported session status for verification: {status or 'empty'}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    ok_sc, source_contract_path, sc_err = validate_repo_file_path(repo_root, source_contract_rel)
    if not ok_sc or source_contract_path is None:
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel or "unknown",
            reason=f"invalid or missing source_contract: {sc_err}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    try:
        contract_text = source_contract_path.read_text(encoding="utf-8")
    except OSError as exc:
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel,
            reason=f"cannot read source_contract: {exc}",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    verification_plan, warnings = extract_verification_plan(contract_text)
    if not verification_plan:
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel,
            reason="verification_plan missing in source_contract",
            dry_run=args.dry_run,
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    if args.dry_run:
        print_not_run(
            session=args.session,
            source_contract=source_contract_rel,
            reason="dry-run preview only",
            verification_plan=verification_plan,
            dry_run=True,
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    command_results: list[dict[str, object]] = []
    any_fail = False
    any_partial = False
    any_ran = False

    for command in verification_plan:
        entry: dict[str, object] = {
            "command": command,
            "status": "PARTIAL",
            "exit_code": "",
            "stdout_summary": "",
            "stderr_summary": "",
            "ran_at": "",
            "reason": "",
            "ran": False,
        }

        safe, reason, tokens = check_command_safety(command)
        if not safe or tokens is None:
            entry["status"] = "PARTIAL"
            entry["reason"] = reason or "unsupported verification command"
            entry["exit_code"] = ""
            any_partial = True
            command_results.append(entry)
            continue

        try:
            result = subprocess.run(
                tokens,
                cwd=str(repo_root),
                capture_output=True,
                text=True,
                timeout=DEFAULT_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired as exc:
            entry["status"] = "PARTIAL"
            entry["reason"] = f"command timed out after {DEFAULT_TIMEOUT_SECONDS} seconds"
            entry["exit_code"] = ""
            entry["stdout_summary"] = summarize_output((exc.stdout or ""))
            entry["stderr_summary"] = summarize_output((exc.stderr or ""))
            entry["ran_at"] = now_iso_utc()
            any_partial = True
            command_results.append(entry)
            continue
        except OSError as exc:
            entry["status"] = "PARTIAL"
            entry["reason"] = f"subprocess could not start: {exc}"
            entry["exit_code"] = ""
            any_partial = True
            command_results.append(entry)
            continue

        any_ran = True
        entry["ran"] = True
        entry["ran_at"] = now_iso_utc()
        entry["exit_code"] = result.returncode
        entry["stdout_summary"] = summarize_output(result.stdout or "")
        entry["stderr_summary"] = summarize_output(result.stderr or "")
        if result.returncode == 0:
            entry["status"] = "PASS"
        else:
            entry["status"] = "FAIL"
            any_fail = True
        command_results.append(entry)

    if not any_ran:
        print_result(
            session=args.session,
            source_contract=source_contract_rel,
            verification_plan=verification_plan,
            command_results=command_results,
            warnings=warnings + ["no commands run"],
            result="NOT RUN",
        )
        return VERIFICATION_PARTIAL_OR_NOT_RUN

    if any_fail:
        overall = "FAIL"
        code = VERIFICATION_FAIL
    elif any_partial:
        overall = "PARTIAL"
        code = VERIFICATION_PARTIAL_OR_NOT_RUN
    else:
        overall = "PASS"
        code = VERIFICATION_PASS

    print_result(
        session=args.session,
        source_contract=source_contract_rel,
        verification_plan=verification_plan,
        command_results=command_results,
        warnings=warnings,
        result=overall,
    )
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
