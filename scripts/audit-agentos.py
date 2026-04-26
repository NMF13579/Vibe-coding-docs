#!/usr/bin/env python3
"""
AgentOS Audit Runner.

Aggregates existing release-readiness checks into one command.
Read-only orchestration/reporting layer over existing checks.
"""

import sys
import subprocess
from pathlib import Path


def read_guard_failures_smoke_result():
    """
    Read the ## Actual Result section from guard-failures-smoke.md.
    Returns the value of the section or None if not found.
    """
    repo_root = Path(__file__).resolve().parent.parent
    smoke_file = repo_root / "reports" / "guard-failures-smoke.md"
    
    if not smoke_file.exists():
        return None
    
    try:
        content = smoke_file.read_text()
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            if line.strip() == "## Actual Result":
                # Find the next non-empty line
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line:
                        return next_line
                return None
        return None
    except Exception:
        return None


def run_suite(name, cmd, repo_root):
    """
    Run a single audit suite.
    Returns (exit_code, stdout, stderr).
    """
    try:
        result = subprocess.run(
            cmd,
            cwd=repo_root,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def main():
    repo_root = Path(__file__).resolve().parent.parent
    
    # Prerequisite guard: check guard-failures-smoke.md
    guard_result = read_guard_failures_smoke_result()
    if guard_result != "PASS":
        print("AgentOS Audit Report")
        print("Prerequisite check failed: guard-failures-smoke.md ## Actual Result != PASS")
        print("Result: FAIL")
        
        # Write failure report
        audit_report = repo_root / "reports" / "audit.md"
        audit_report.parent.mkdir(parents=True, exist_ok=True)
        audit_report.write_text(
            "# AgentOS Audit Report\n\n"
            "## Failure Details\n\n"
            "Prerequisite guard failed: guard-failures-smoke.md ## Actual Result must be PASS.\n\n"
            "Recommended follow-up task: Complete Milestone 7.2 (Guard Failure Runner).\n"
        )
        return 1
    
    # Define suites: (name, command_list)
    suites = [
        ("template-integrity-strict", [sys.executable, "scripts/check-template-integrity.py", "--strict"]),
        ("template-integrity-self-test", [sys.executable, "scripts/test-template-integrity.py"]),
        ("negative-fixtures", [sys.executable, "scripts/test-negative-fixtures.py"]),
        ("guard-failures", [sys.executable, "scripts/test-guard-failures.py"]),
    ]
    
    skipped = [
        ("release checklist", "future milestone"),
        ("full docs hardening", "future milestone"),
        ("example scenarios", "future milestone"),
        ("prompt packs", "future milestone"),
    ]
    
    results = {}
    failed = False
    
    # Run all suites (don't stop after first failure)
    for name, cmd in suites:
        exit_code, stdout, stderr = run_suite(name, cmd, repo_root)
        results[name] = (exit_code, stdout, stderr)
        if exit_code != 0:
            failed = True
    
    # Print console output
    print("AgentOS Audit Report")
    print("Suites:")
    for name, cmd in suites:
        exit_code, stdout, stderr = results[name]
        if exit_code == 0:
            print(f"  {name}: PASS")
        else:
            print(f"  {name}: FAIL")
            print(f"    - Command: {' '.join(cmd)}")
            print(f"    - Expected exit code: 0")
            print(f"    - Actual exit code: {exit_code}")
            # Print concise excerpt
            excerpt = (stdout + stderr)[:200] if stdout or stderr else ""
            if excerpt:
                print(f"    - output excerpt:")
                for line in excerpt.split('\n')[:3]:
                    if line:
                        print(f"      {line}")
    
    print("Skipped:")
    for suite_name, reason in skipped:
        print(f"  {suite_name}: SKIPPED — {reason}")
    
    result_status = "FAIL" if failed else "PASS"
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
        "| Suite | Command | Expected | Actual | Result |",
        "|---|---|---|---|---|",
    ]
    
    for name, cmd in suites:
        exit_code, _, _ = results[name]
        result_str = "PASS" if exit_code == 0 else "FAIL"
        cmd_str = " ".join(cmd).replace(sys.executable, "python3")
        md_lines.append(
            f"| {name} | `{cmd_str}` | exit 0 | exit {exit_code} | {result_str} |"
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
    
    if not failed:
        md_lines.append("No failures.")
    else:
        for name, cmd in suites:
            exit_code, stdout, stderr = results[name]
            if exit_code != 0:
                md_lines.extend([
                    f"**{name}:**",
                    f"- Command: {' '.join(cmd)}",
                    f"- Expected exit code: 0",
                    f"- Actual exit code: {exit_code}",
                    f"- Output excerpt:",
                ])
                excerpt = (stdout + stderr)[:300]
                if excerpt:
                    for line in excerpt.split('\n')[:5]:
                        if line:
                            md_lines.append(f"  {line}")
                md_lines.append("")
        
        md_lines.extend([
            "Recommended follow-up task: Debug the failed suite.",
            "",
        ])
    
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
    
    # Exit code: 0 if all pass, 1 if any fail
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
