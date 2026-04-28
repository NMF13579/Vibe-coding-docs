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

SUITES = {
    "template": ["scripts/check-template-integrity.py", "--strict"],
    "negative": ["scripts/test-negative-fixtures.py"],
    "guard": ["scripts/test-guard-failures.py"],
    "audit": ["scripts/audit-agentos.py"],
    "queue": ["scripts/validate-queue.py"],
    "runner": ["scripts/validate-runner-protocol.py"],
    "state-fixtures": ["scripts/test-state-fixtures.py"],
    "approval-fixtures": ["scripts/test-approval-marker-fixtures.py"],
}

ORDER = ["template", "negative", "guard", "audit", "queue", "runner"]


def resolve_command(repo_root: Path, suite: str) -> tuple[list[str], Path]:
    command = SUITES[suite]
    script_path = repo_root / command[0]
    return [sys.executable, *command], script_path


def run_command(repo_root: Path, command: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(command, cwd=repo_root, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


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
    status = suite_status(exit_code, stdout, stderr)
    return {
        "name": suite,
        "result": status,
        "exit_code": exit_code,
        "error": None,
        "stdout": stdout,
        "stderr": stderr,
    }


def print_text_suite_result(suite_result: dict) -> None:
    if suite_result["result"] == MISSING:
        print(f"[MISSING] {suite_result['name']}")
        return

    message = suite_result["error"]
    print_suite_result(suite_result["name"], suite_result["result"], message)
    if suite_result["stdout"]:
        print(suite_result["stdout"], end="" if suite_result["stdout"].endswith("\n") else "\n")
    if suite_result["stderr"]:
        print(suite_result["stderr"], end="" if suite_result["stderr"].endswith("\n") else "\n", file=sys.stderr)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/agentos-validate.py <template|negative|guard|audit|queue|runner|state-fixtures|approval-fixtures|all>", file=sys.stderr)
        return 2

    target = sys.argv[1]
    if target not in SUITES and target != "all":
        print(f"FAIL: unknown command: {target}", file=sys.stderr)
        return 2

    if target != "all":
        suite_result = run_suite(repo_root, target)
        print_text_suite_result(suite_result)
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
