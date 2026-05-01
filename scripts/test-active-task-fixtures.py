#!/usr/bin/env python3
"""Run negative fixtures for validate-active-task.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def expected_status_from_readme(readme_path: Path) -> str:
    text = readme_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.strip() == "- status: PARTIAL":
            return "PARTIAL"
    return "FAIL"


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    fixtures_root = repo_root / "tests" / "fixtures" / "negative" / "active-task"
    validator = repo_root / "scripts" / "validate-active-task.py"

    if not fixtures_root.is_dir():
        print("Active Task Negative Fixtures")
        print("PASS: 0")
        print("FAIL: 1")
        print("TOTAL: 0")
        print("Result: FAIL")
        print(f"Reason: missing fixture directory: {fixtures_root}")
        return 1

    if not validator.is_file():
        print("Active Task Negative Fixtures")
        print("PASS: 0")
        print("FAIL: 1")
        print("TOTAL: 0")
        print("Result: FAIL")
        print(f"Reason: missing validator: {validator}")
        return 1

    case_dirs = sorted(path for path in fixtures_root.iterdir() if path.is_dir())
    pass_count = 0
    fail_count = 0

    for case_dir in case_dirs:
        readme = case_dir / "README.md"
        if not readme.is_file():
            print(f"{case_dir.name}: FAIL")
            print("Reason: missing README.md")
            fail_count += 1
            continue

        expected_status = expected_status_from_readme(readme)
        active_task_path = case_dir / "active-task.md"
        active_task_arg = active_task_path.relative_to(repo_root).as_posix()

        try:
            completed = subprocess.run(
                [sys.executable, str(validator), "--active-task", active_task_arg],
                cwd=str(repo_root),
                capture_output=True,
                text=True,
            )
        except Exception as exc:  # pragma: no cover
            print(f"{case_dir.name}: FAIL")
            print(f"Reason: runner exception: {exc}")
            fail_count += 1
            continue

        output = (completed.stdout or "") + (completed.stderr or "")
        has_traceback = "Traceback" in output
        has_pass = "Active Task Validation: PASS" in output
        expected_header = f"Active Task Validation: {expected_status}"
        header_match = expected_header in output

        if completed.returncode == 1 and header_match and not has_traceback and not has_pass:
            print(f"{case_dir.name}: PASS")
            pass_count += 1
        else:
            print(f"{case_dir.name}: FAIL")
            print(
                "Reason: "
                f"exit={completed.returncode}, expected_status={expected_status}, "
                f"header_match={header_match}, traceback={has_traceback}, pass_header={has_pass}"
            )
            fail_count += 1

    total = pass_count + fail_count
    print("Active Task Negative Fixtures")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"TOTAL: {total}")
    print(f"Result: {'PASS' if fail_count == 0 else 'FAIL'}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
