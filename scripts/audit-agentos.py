#!/usr/bin/env python3
"""
AgentOS Audit Runner.

Aggregates existing release-readiness checks into one command.
Read-only orchestration/reporting layer over existing checks.
"""

import sys
import subprocess
from pathlib import Path

PASS = "PASS"
PASS_WITH_WARNINGS = "PASS_WITH_WARNINGS"
FAIL = "FAIL"
WARN = "WARN"


def suite_status(exit_code, stdout, stderr):
    if exit_code != 0:
        return FAIL
    merged = f"{stdout}\n{stderr}".upper()
    if "RESULT: PASS_WITH_WARNINGS" in merged:
        return PASS_WITH_WARNINGS
    return PASS


def run_suite(name, cmd, repo_root):
    """
    Run a single audit suite.
    Returns (exit_code, stdout, stderr).
    """
    try:
        result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def main():
    repo_root = Path(__file__).resolve().parent.parent

    # Define suites: (name, command_list, script_path, optional_if_missing)
    suites = [
        (
            "template-integrity-strict",
            [sys.executable, "scripts/check-template-integrity.py", "--strict"],
            repo_root / "scripts/check-template-integrity.py",
            False,
        ),
        (
            "template-integrity-self-test",
            [sys.executable, "scripts/test-template-integrity.py"],
            repo_root / "scripts/test-template-integrity.py",
            False,
        ),
        (
            "negative-fixtures",
            [sys.executable, "scripts/test-negative-fixtures.py"],
            repo_root / "scripts/test-negative-fixtures.py",
            False,
        ),
        (
            "guard-failures",
            [sys.executable, "scripts/test-guard-failures.py"],
            repo_root / "scripts/test-guard-failures.py",
            True,
        ),
    ]

    skipped = [
        ("release checklist", "future milestone"),
        ("full docs hardening", "future milestone"),
        ("example scenarios", "future milestone"),
        ("prompt packs", "future milestone"),
    ]

    results = {}
    has_failures = False
    has_warnings = False

    # Run all suites (do not stop after first failure)
    for name, cmd, script_path, optional_if_missing in suites:
        if optional_if_missing and not script_path.is_file():
            results[name] = {
                "status": WARN,
                "cmd": cmd,
                "exit_code": None,
                "stdout": "",
                "stderr": "",
                "note": f"{script_path.as_posix()} not found",
            }
            has_warnings = True
            continue

        exit_code, stdout, stderr = run_suite(name, cmd, repo_root)
        status = suite_status(exit_code, stdout, stderr)
        results[name] = {
            "status": status,
            "cmd": cmd,
            "exit_code": exit_code,
            "stdout": stdout,
            "stderr": stderr,
            "note": "",
        }
        if status == FAIL:
            has_failures = True
        elif status == PASS_WITH_WARNINGS:
            has_warnings = True

    # Print console output.
    print("AgentOS Audit")
    for name, _cmd, _script_path, _optional in suites:
        suite_result = results[name]
        status = suite_result["status"]
        if status == WARN:
            print(f"{name}: WARN - {suite_result['note']}")
            continue

        print(f"{name}: {status}")
        if status == FAIL:
            cmd = suite_result["cmd"]
            exit_code = suite_result["exit_code"]
            stdout = suite_result["stdout"]
            stderr = suite_result["stderr"]
            print(f"  - Command: {' '.join(cmd)}")
            print("  - Expected exit code: 0")
            print(f"  - Actual exit code: {exit_code}")
            excerpt = (stdout + stderr)[:250] if stdout or stderr else ""
            if excerpt:
                print("  - Output excerpt:")
                for line in excerpt.split("\n")[:4]:
                    if line:
                        print(f"    {line}")

    print("Skipped:")
    for suite_name, reason in skipped:
        print(f"  {suite_name}: SKIPPED - {reason}")

    if has_failures:
        result_status = FAIL
    elif has_warnings:
        result_status = PASS_WITH_WARNINGS
    else:
        result_status = PASS
    print(f"Result: {result_status}")

    # Build markdown report
    md_lines = [
        "# AgentOS Audit Report",
        "",
        "## Command",
        "",
        "```",
        "python3 scripts/audit-agentos.py",
        "```",
        "",
        "## Result",
        "",
        result_status,
        "",
        "## Suites",
        "",
        "| Suite | Command | Expected | Actual | Result | Notes |",
        "|---|---|---|---|---|---|",
    ]

    for name, cmd, _script_path, _optional in suites:
        suite_result = results[name]
        status = suite_result["status"]
        cmd_str = " ".join(cmd).replace(sys.executable, "python3")
        if status == WARN:
            md_lines.append(
                f"| {name} | `{cmd_str}` | script exists | missing | WARN | {suite_result['note']} |"
            )
            continue
        md_lines.append(
            f"| {name} | `{cmd_str}` | exit 0 | exit {suite_result['exit_code']} | {status} | |"
        )

    md_lines.extend([
        "",
        "## Skipped",
        "",
    ])
    
    for suite_name, reason in skipped:
        md_lines.append(f"- {suite_name}: {reason}")
    
    md_lines.extend([
        "",
        "## Failure Details",
        "",
    ])

    if not has_failures:
        md_lines.append("No failures.")
    else:
        for name, _cmd, _script_path, _optional in suites:
            suite_result = results[name]
            if suite_result["status"] != FAIL:
                continue
            cmd = suite_result["cmd"]
            exit_code = suite_result["exit_code"]
            stdout = suite_result["stdout"]
            stderr = suite_result["stderr"]
            md_lines.extend(
                [
                    f"**{name}:**",
                    f"- Command: {' '.join(cmd)}",
                    "- Expected exit code: 0",
                    f"- Actual exit code: {exit_code}",
                    "- Output excerpt:",
                ]
            )
            excerpt = (stdout + stderr)[:300]
            if excerpt:
                for line in excerpt.split("\n")[:5]:
                    if line:
                        md_lines.append(f"  {line}")
            md_lines.append("")

        md_lines.extend(["Recommended follow-up task: Debug the failed suite.", ""])

    md_lines.extend([
        "## Safety Notes",
        "",
        "- Audit runner is read-only except for writing this report.",
        "- No tasks were executed.",
        "- Runner protocol scripts were not executed directly.",
        "- tasks/active-task.md was not modified intentionally.",
        "- Queue items were not moved.",
        "- No validators were created.",
        "- No release checklist was created.",
    ])
    
    # Write report
    audit_report = repo_root / "reports" / "audit.md"
    audit_report.parent.mkdir(parents=True, exist_ok=True)
    audit_report.write_text("\n".join(md_lines) + "\n")

    # Exit code: 1 only if there is at least one FAIL.
    return 1 if has_failures else 0


if __name__ == "__main__":
    sys.exit(main())
