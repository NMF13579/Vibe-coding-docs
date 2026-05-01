#!/usr/bin/env python3
"""Unified validation wrapper for existing AgentOS validators."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PASS = "PASS"
PASS_WITH_WARNINGS = "PASS_WITH_WARNINGS"
FAIL = "FAIL"
MISSING = "MISSING"
SEVERITY_CRITICAL = "CRITICAL"
SEVERITY_WARNING = "WARNING"
SEVERITY_INFO = "INFO"

SUITES = {
    "template": ["scripts/check-template-integrity.py", "--strict"],
    "negative": ["scripts/test-negative-fixtures.py"],
    "guard": ["scripts/test-guard-failures.py"],
    "audit": ["scripts/audit-agentos.py"],
    "queue": ["scripts/validate-queue.py"],
    "runner": ["scripts/validate-runner-protocol.py"],
    "state-fixtures": ["scripts/test-state-fixtures.py"],
    "approval-fixtures": ["scripts/test-approval-marker-fixtures.py"],
    "activation-fixtures": ["scripts/test-activation-fixtures.py"],
    "active-task": ["scripts/validate-active-task.py"],
    "active-task-fixtures": ["scripts/test-active-task-fixtures.py"],
    "execution-readiness": ["scripts/check-execution-readiness.py"],
    "readiness-fixtures": ["scripts/test-readiness-fixtures.py"],
}

# Milestone 12 policy:
# all runs only readiness-related fixture suites.
# all does not run live checks and does not run legacy runner suites.
ORDER = ["active-task-fixtures", "readiness-fixtures"]

WARNING_PATTERNS = (
    "approval marker resolver: skipped",
    "source_task change detection: not available",
    "source_contract change detection: not available",
    "git hooks not installed",
    "hooks not installed",
)


def available_commands() -> str:
    commands = [*SUITES.keys(), "all"]
    return "|".join(commands)


def resolve_command(repo_root: Path, suite: str) -> tuple[list[str], Path]:
    command = SUITES[suite]
    script_path = repo_root / command[0]
    return [sys.executable, *command], script_path


def run_command(repo_root: Path, command: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(command, cwd=repo_root, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def detect_warning_only_condition(stdout: str, stderr: str) -> bool:
    merged = f"{stdout}\n{stderr}".lower()
    return any(pattern in merged for pattern in WARNING_PATTERNS)


def classify_severity(exit_code: int, stdout: str, stderr: str) -> str:
    if exit_code == 0:
        return SEVERITY_WARNING if detect_warning_only_condition(stdout, stderr) else SEVERITY_INFO

    merged = f"{stdout}\n{stderr}".lower()
    if detect_warning_only_condition(stdout, stderr) and "traceback" not in merged:
        return SEVERITY_WARNING
    return SEVERITY_CRITICAL


def suite_status(exit_code: int, stdout: str, stderr: str) -> str:
    if exit_code != 0:
        return FAIL
    merged = f"{stdout}\n{stderr}"
    if PASS_WITH_WARNINGS in merged:
        return PASS_WITH_WARNINGS
    return PASS


def print_suite_result(name: str, status: str, message: str | None = None) -> None:
    if message:
        print(f"[{status}] {name} - {message}")
    else:
        print(f"[{status}] {name}")


def run_suite(repo_root: Path, suite: str) -> dict:
    command, script_path = resolve_command(repo_root, suite)
    if not script_path.is_file():
        message = f"missing script: {script_path.as_posix()}"
        return {
            "name": suite,
            "result": MISSING,
            "exit_code": 1,
            "error": message,
            "stdout": "",
            "stderr": "",
        }

    exit_code, stdout, stderr = run_command(repo_root, command)
    severity = classify_severity(exit_code, stdout, stderr)
    effective_exit_code = 1 if severity == SEVERITY_CRITICAL else 0
    status = suite_status(effective_exit_code, stdout, stderr)
    return {
        "name": suite,
        "result": status,
        "exit_code": effective_exit_code,
        "raw_exit_code": exit_code,
        "severity": severity,
        "error": None,
        "stdout": stdout,
        "stderr": stderr,
    }


def print_text_suite_result(suite_result: dict) -> None:
    if suite_result["result"] == MISSING:
        message = suite_result["error"] or "missing script"
        print(f"[MISSING] {suite_result['name']} - {message}")
        return

    message = suite_result["error"]
    if (
        suite_result.get("severity") == SEVERITY_WARNING
        and suite_result.get("raw_exit_code", 0) != suite_result.get("exit_code", 0)
    ):
        print(f"[{SEVERITY_WARNING}] {suite_result['name']} - non-critical condition downgraded")
    print_suite_result(suite_result["name"], suite_result["result"], message)
    if suite_result["stdout"]:
        print(suite_result["stdout"], end="" if suite_result["stdout"].endswith("\n") else "\n")
    if suite_result["stderr"]:
        print(suite_result["stderr"], end="" if suite_result["stderr"].endswith("\n") else "\n", file=sys.stderr)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print(
            f"Usage: python3 scripts/agentos-validate.py <{available_commands()}>",
            file=sys.stderr,
        )
        print("Available commands:", file=sys.stderr)
        for name in [*SUITES.keys(), "all"]:
            print(f"  {name}", file=sys.stderr)
        return 2

    target = sys.argv[1]
    if target not in SUITES and target != "all":
        print(f"FAIL: unknown command: {target}", file=sys.stderr)
        return 2

    if target != "all":
        command, _ = resolve_command(repo_root, target)
        print(f"AgentOS Validate: {target}")
        print(f"Running: {' '.join(command)}")
        print()
        suite_result = run_suite(repo_root, target)
        print_text_suite_result(suite_result)
        if suite_result.get("severity") == SEVERITY_WARNING:
            print("Result: PARTIAL")
        else:
            print(f"Result: {'PASS' if suite_result['exit_code'] == 0 else 'FAIL'}")
        return suite_result["exit_code"]

    overall_fail = False
    overall_warn = False

    for suite in ORDER:
        suite_result = run_suite(repo_root, suite)
        print_text_suite_result(suite_result)
        if suite_result["exit_code"] != 0:
            overall_fail = True
        elif suite_result["result"] == PASS_WITH_WARNINGS:
            overall_warn = True

    if overall_fail:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
