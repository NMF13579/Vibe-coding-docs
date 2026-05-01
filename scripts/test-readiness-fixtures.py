#!/usr/bin/env python3
"""Run readiness fixtures for check-execution-readiness.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def parse_readme(readme_path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    text = readme_path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- status:"):
            data["status"] = line.split(":", 1)[1].strip()
        elif line.startswith("- exit code:"):
            data["exit_code"] = line.split(":", 1)[1].strip()
        elif line.startswith("- note contains:"):
            data["note_contains"] = line.split(":", 1)[1].strip()
        elif line.startswith("- reason:"):
            data["reason"] = line.split(":", 1)[1].strip()
    return data


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    fixtures_root = repo_root / "tests" / "fixtures" / "negative" / "readiness"
    checker = repo_root / "scripts" / "check-execution-readiness.py"

    if not fixtures_root.is_dir():
        print("Readiness Fixtures")
        print("PASS: 0")
        print("FAIL: 1")
        print("SKIPPED: 0")
        print("TOTAL: 0")
        print("Result: FAIL")
        print(f"Reason: missing fixture directory: {fixtures_root}")
        return 1

    pass_count = 0
    fail_count = 0
    skipped_count = 0
    pass_with_limitations_cases = 0

    for case_dir in sorted(p for p in fixtures_root.iterdir() if p.is_dir()):
        readme = case_dir / "README.md"
        if not readme.is_file():
            print(f"{case_dir.name}: FAIL")
            print("Reason: missing README.md")
            fail_count += 1
            continue

        expected = parse_readme(readme)
        status = expected.get("status", "")

        if status == "SKIPPED":
            reason = expected.get("reason", "")
            if not reason:
                print(f"{case_dir.name}: FAIL")
                print("Reason: SKIPPED case missing reason in README")
                fail_count += 1
            else:
                print(f"{case_dir.name}: SKIPPED")
                print(f"Reason: {reason}")
                skipped_count += 1
            continue

        if status not in {"FAIL", "PARTIAL", "PASS"} or "exit_code" not in expected:
            print(f"{case_dir.name}: FAIL")
            print("Reason: malformed README expected block (status/exit code required)")
            fail_count += 1
            continue

        if status == "PASS" and "note_contains" not in expected:
            print(f"{case_dir.name}: FAIL")
            print("Reason: PASS case missing 'note contains' requirement")
            fail_count += 1
            continue

        active_task = case_dir / "active-task.md"
        approval_dir = case_dir / "approvals"
        active_task_arg = active_task.relative_to(repo_root).as_posix()
        approval_dir_arg = approval_dir.relative_to(repo_root).as_posix()

        try:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(checker),
                    "--active-task",
                    active_task_arg,
                    "--approval-dir",
                    approval_dir_arg,
                ],
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
        expected_exit = int(expected["exit_code"])
        expected_header = f"Execution Readiness: {status}"
        header_ok = expected_header in output
        exit_ok = completed.returncode == expected_exit
        note_ok = True
        if status == "PASS":
            note_ok = expected["note_contains"] in output

        if exit_ok and header_ok and note_ok and not has_traceback:
            print(f"{case_dir.name}: PASS")
            pass_count += 1
            if status == "PASS":
                pass_with_limitations_cases += 1
        else:
            print(f"{case_dir.name}: FAIL")
            print(
                "Reason: "
                f"expected_status={status}, expected_exit={expected_exit}, "
                f"actual_exit={completed.returncode}, header_ok={header_ok}, "
                f"note_ok={note_ok}, traceback={has_traceback}"
            )
            fail_count += 1

    total = pass_count + fail_count + skipped_count
    print("Readiness Fixtures")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"SKIPPED: {skipped_count}")
    print(f"TOTAL: {total}")
    if pass_with_limitations_cases:
        print(f"PASS_WITH_LIMITATIONS_CASES: {pass_with_limitations_cases}")
    print(f"Result: {'PASS' if fail_count == 0 else 'FAIL'}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
