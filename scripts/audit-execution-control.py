#!/usr/bin/env python3
import json
import subprocess
import sys
import argparse
import os
from pathlib import Path


RESULT_CONTROL_READY = "CONTROL_READY"
RESULT_READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
RESULT_NEEDS_REVIEW = "NEEDS_REVIEW"

ARTIFACTS = [
    "docs/SCOPE-COMPLIANCE.md",
    "templates/task-scope.md",
    "scripts/check-scope-compliance.py",
    "tests/fixtures/scope-compliance",
    "scripts/test-scope-compliance-fixtures.py",
    "docs/SCOPE-SUMMARY.md",
    "docs/REQUIRED-EVIDENCE-POLICY.md",
    "templates/scope-verification.md",
    "docs/GUARDRAIL-EXECUTION-CHECKLIST.md",
]


class CliParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def parse_args(argv):
    parser = CliParser(add_help=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def run_command(command, repo_root):
    try:
        proc = subprocess.run(
            command,
            cwd=str(repo_root),
            text=True,
            capture_output=True,
        )
        output = proc.stdout.strip()
        if not output:
            output = proc.stderr.strip()
        return proc.returncode, output
    except Exception as exc:
        return 127, str(exc)


def check_artifacts(repo_root):
    missing = []
    for rel in ARTIFACTS:
        if not (repo_root / rel).exists():
            missing.append(rel)
    return missing


def append_check(checks, name, command, exit_code, output_summary, result):
    checks.append(
        {
            "name": name,
            "result": result,
            "command": command,
            "exit_code": exit_code,
            "output_summary": output_summary,
        }
    )


def audit(repo_root):
    checks = []
    warnings = []
    failed_checks = []

    missing_artifacts = check_artifacts(repo_root)

    scope_validator = repo_root / "scripts/check-scope-compliance.py"
    fixture_runner = repo_root / "scripts/test-scope-compliance-fixtures.py"

    if scope_validator.exists():
        cmd = "python -m py_compile scripts/check-scope-compliance.py"
        code, out = run_command(["python", "-m", "py_compile", "scripts/check-scope-compliance.py"], repo_root)
        result = "PASS" if code == 0 else "FAIL"
        append_check(checks, "scope-validator-syntax", cmd, code, out, result)
        if code != 0:
            failed_checks.append("scope-validator-syntax")
    else:
        append_check(checks, "scope-validator-syntax", "python -m py_compile scripts/check-scope-compliance.py", -1, "missing file", "NOT_RUN")

    if fixture_runner.exists():
        cmd = "python -m py_compile scripts/test-scope-compliance-fixtures.py"
        code, out = run_command(["python", "-m", "py_compile", "scripts/test-scope-compliance-fixtures.py"], repo_root)
        result = "PASS" if code == 0 else "FAIL"
        append_check(checks, "scope-fixture-runner-syntax", cmd, code, out, result)
        if code != 0:
            failed_checks.append("scope-fixture-runner-syntax")

        cmd = "python scripts/test-scope-compliance-fixtures.py"
        code, out = run_command(["python", "scripts/test-scope-compliance-fixtures.py"], repo_root)
        result = "PASS" if code == 0 else "FAIL"
        append_check(checks, "scope-fixture-runner", cmd, code, out, result)
        if code != 0:
            failed_checks.append("scope-fixture-runner")
    else:
        append_check(checks, "scope-fixture-runner-syntax", "python -m py_compile scripts/test-scope-compliance-fixtures.py", -1, "missing file", "NOT_RUN")
        append_check(checks, "scope-fixture-runner", "python scripts/test-scope-compliance-fixtures.py", -1, "missing file", "NOT_RUN")

    checks_run = 0
    checks_passed = 0
    checks_failed = 0
    for item in checks:
        if item["result"] == "NOT_RUN":
            continue
        checks_run += 1
        if item["result"] == "PASS":
            checks_passed += 1
        elif item["result"] == "FAIL":
            checks_failed += 1

    result = RESULT_CONTROL_READY
    if missing_artifacts or checks_failed > 0:
        result = RESULT_NEEDS_REVIEW
    elif warnings:
        result = RESULT_READY_WITH_WARNINGS

    payload = {
        "result": result,
        "artifacts_checked": len(ARTIFACTS),
        "artifacts_missing": len(missing_artifacts),
        "checks_run": checks_run,
        "checks_passed": checks_passed,
        "checks_failed": checks_failed,
        "warnings_count": len(warnings),
        "human_action_required": result != RESULT_CONTROL_READY,
        "missing_artifacts": missing_artifacts,
        "failed_checks": failed_checks,
        "warnings": warnings,
        "checks": checks,
    }
    return payload


def print_human(payload):
    print(f"M23 Execution Control Audit: {payload['result']}")
    print(f"Artifacts checked: {payload['artifacts_checked']}")
    print(f"Artifacts missing: {payload['artifacts_missing']}")
    print(f"Checks run: {payload['checks_run']}")
    print(f"Checks passed: {payload['checks_passed']}")
    print(f"Checks failed: {payload['checks_failed']}")
    print(f"Warnings: {payload['warnings_count']}")
    print(f"Human action required: {'YES' if payload['human_action_required'] else 'NO'}")

    print("Missing artifacts:")
    if payload["missing_artifacts"]:
        for item in payload["missing_artifacts"]:
            print(f"- {item}")
    else:
        print("NONE")

    print("Failed checks:")
    if payload["failed_checks"]:
        for item in payload["failed_checks"]:
            print(f"- {item}")
    else:
        print("NONE")

    print("Warnings list:")
    if payload["warnings"]:
        for item in payload["warnings"]:
            print(f"- {item}")
    else:
        print("NONE")


def main(argv):
    try:
        args = parse_args(argv)
    except Exception:
        payload = {
            "result": RESULT_NEEDS_REVIEW,
            "artifacts_checked": 0,
            "artifacts_missing": 0,
            "checks_run": 0,
            "checks_passed": 0,
            "checks_failed": 0,
            "warnings_count": 0,
            "human_action_required": True,
            "missing_artifacts": [],
            "failed_checks": ["cli-arguments"],
            "warnings": [],
            "checks": [],
        }
        print_human(payload)
        return 2

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        payload = {
            "result": RESULT_NEEDS_REVIEW,
            "artifacts_checked": 0,
            "artifacts_missing": 0,
            "checks_run": 0,
            "checks_passed": 0,
            "checks_failed": 1,
            "warnings_count": 0,
            "human_action_required": True,
            "missing_artifacts": [],
            "failed_checks": ["invalid-repo-root"],
            "warnings": [],
            "checks": [],
        }
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 2

    payload = audit(repo_root)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_human(payload)

    if payload["result"] == RESULT_CONTROL_READY:
        return 0
    if payload["result"] == RESULT_READY_WITH_WARNINGS:
        return 1
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception:
        fallback = {
            "result": RESULT_NEEDS_REVIEW,
            "artifacts_checked": 0,
            "artifacts_missing": 0,
            "checks_run": 0,
            "checks_passed": 0,
            "checks_failed": 1,
            "warnings_count": 0,
            "human_action_required": True,
            "missing_artifacts": [],
            "failed_checks": ["unexpected-error"],
            "warnings": [],
            "checks": [],
        }
        print_human(fallback)
        sys.exit(2)
