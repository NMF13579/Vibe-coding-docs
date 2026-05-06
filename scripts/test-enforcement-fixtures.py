#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess
import sys


ENFORCEMENT_READY = "ENFORCEMENT_READY"
READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
NEEDS_REVIEW = "NEEDS_REVIEW"
NOT_READY = "NOT_READY"

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "enforcement"
AUDIT_SCRIPT = REPO_ROOT / "scripts" / "audit-enforcement.py"

EXPECTED_CASES = {
    "valid": {
        "enforced-workflow": ENFORCEMENT_READY,
    },
    "invalid": {
        "missing-required-check-name": NOT_READY,
        "failure-hidden-with-true": NOT_READY,
        "artifact-not-preserved": NOT_READY,
        "auto-merge-present": NOT_READY,
        "auto-approval-present": NOT_READY,
        "contents-write": NOT_READY,
        "no-platform-evidence": NEEDS_REVIEW,
        "required-checks-not-documented": NOT_READY,
    },
}


def discover_case_dirs(category: str) -> list[Path]:
    base = FIXTURE_ROOT / category
    if not base.is_dir():
        return []
    return sorted(path for path in base.iterdir() if path.is_dir())


def parse_result(output: str) -> str | None:
    match = re.search(r"^Result:\s*([A-Z_]+)\s*$", output, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def run_audit(fixture_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", "scripts/audit-enforcement.py", "--root", str(fixture_root)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def expected_exit_code(result: str) -> int:
    if result in (ENFORCEMENT_READY, READY_WITH_WARNINGS):
        return 0
    return 1


def main() -> int:
    failures = 0
    print("AgentOS Enforcement Fixture Tests")

    discovered = {
        "valid": {path.name for path in discover_case_dirs("valid")},
        "invalid": {path.name for path in discover_case_dirs("invalid")},
    }

    for category, expected_map in EXPECTED_CASES.items():
        expected_names = set(expected_map.keys())
        actual_names = discovered[category]
        if actual_names != expected_names:
            failures += 1
            missing = sorted(expected_names - actual_names)
            extra = sorted(actual_names - expected_names)
            if missing:
                print(f"FAIL {category}: missing fixture directories: {', '.join(missing)}")
            if extra:
                print(f"FAIL {category}: unexpected fixture directories: {', '.join(extra)}")

    for category, expected_map in EXPECTED_CASES.items():
        for name, expected in sorted(expected_map.items()):
            fixture_root = FIXTURE_ROOT / category / name
            proc = run_audit(fixture_root)
            actual = parse_result(proc.stdout)
            code_ok = proc.returncode == expected_exit_code(expected)
            result_ok = actual == expected

            if result_ok and code_ok:
                print(f"PASS {category}/{name} -> {actual}")
            else:
                failures += 1
                actual_display = actual if actual is not None else "MISSING_RESULT"
                print(
                    f"FAIL {category}/{name} -> expected {expected}, actual {actual_display}, exit {proc.returncode}"
                )
                if proc.stdout.strip():
                    print(proc.stdout.rstrip())
                if proc.stderr.strip():
                    print(proc.stderr.rstrip())

    print()
    print(f"Result: {'PASS' if failures == 0 else 'FAIL'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
