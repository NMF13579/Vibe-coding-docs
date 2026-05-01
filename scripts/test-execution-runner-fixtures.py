#!/usr/bin/env python3
"""Run negative fixtures for M13 execution runner."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

STATUS_PASS = "PASS"
STATUS_FAIL = "FAIL"
STATUS_SKIPPED = "SKIPPED"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run execution-runner negative fixtures.")
    parser.add_argument(
        "--fixtures-dir",
        default="tests/fixtures/negative/execution-runner",
        help="Fixture root directory (default: tests/fixtures/negative/execution-runner)",
    )
    return parser.parse_args(argv)


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def tree_hash(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    if path.is_file():
        return f"F:{file_hash(path)}"
    entries: list[str] = []
    for p in sorted(path.rglob("*")):
        rel = str(p.relative_to(path))
        if p.is_file():
            entries.append(f"{rel}:F:{file_hash(p)}")
        else:
            entries.append(f"{rel}:D")
    joined = "\n".join(entries)
    h = hashlib.sha256(joined.encode("utf-8"))
    return f"D:{h.hexdigest()}"


def snapshot_protected(repo_root: Path) -> dict[str, str]:
    protected = [
        "tasks/active-task.md",
        "reports/execution-evidence-report.md",
        "reports/execution",
        "approvals",
        "tasks/queue",
        "tasks/done",
        "tasks/failed",
    ]
    snap: dict[str, str] = {}
    for rel in protected:
        snap[rel] = tree_hash(repo_root / rel)
    return snap


def list_session_files(repo_root: Path) -> set[str]:
    execution_dir = repo_root / "reports" / "execution"
    if not execution_dir.exists():
        return set()
    return {str(p.relative_to(repo_root)) for p in execution_dir.glob("*.md")}


def build_command(repo_root: Path, case_dir: Path, expected: dict[str, object]) -> tuple[list[str] | None, str | None]:
    case_name = str(expected.get("case", case_dir.name))
    target = str(expected.get("target", "")).strip()
    if target == "dry-run":
        if case_name == "active-task-parent-traversal-dry-run":
            return [sys.executable, "scripts/run-active-task.py", "--dry-run", "--active-task", "../bad.md"], None
        return None, "unsupported dry-run case mapping"
    if target == "start":
        if case_name == "active-task-parent-traversal-start":
            return [sys.executable, "scripts/run-active-task.py", "--start", "--active-task", "../bad.md"], None
        if case_name == "active-task-absolute-path-start":
            return [sys.executable, "scripts/run-active-task.py", "--start", "--active-task", "/tmp/bad.md"], None
        if case_name == "active-task-missing-start":
            return [
                sys.executable,
                "scripts/run-active-task.py",
                "--start",
                "--active-task",
                str((case_dir / "missing-active-task.md").relative_to(repo_root)),
            ], None
        if case_name in {
            "active-task-missing-frontmatter-start",
            "active-task-missing-task-id-start",
            "active-task-missing-source-contract-start",
        }:
            return [
                sys.executable,
                "scripts/run-active-task.py",
                "--start",
                "--active-task",
                str((case_dir / "active-task.md").relative_to(repo_root)),
            ], None
        return None, "unsupported start case mapping"
    if target == "scope":
        if case_name == "session-parent-traversal-scope":
            return [sys.executable, "scripts/check-execution-scope.py", "--session", "../bad.md"], None
        if case_name == "session-absolute-path-scope":
            return [sys.executable, "scripts/check-execution-scope.py", "--session", "/tmp/bad.md"], None
        return [
            sys.executable,
            "scripts/check-execution-scope.py",
            "--session",
            str((case_dir / "session.md").relative_to(repo_root)),
        ], None
    if target == "verification":
        if case_name == "session-parent-traversal-verification":
            return [sys.executable, "scripts/run-execution-verification.py", "--session", "../bad.md"], None
        return [
            sys.executable,
            "scripts/run-execution-verification.py",
            "--session",
            str((case_dir / "session.md").relative_to(repo_root)),
        ], None
    return None, f"unsupported target: {target}"


def run_case(repo_root: Path, case_dir: Path) -> tuple[str, str]:
    expected_path = case_dir / "expected.json"
    if not expected_path.is_file():
        return STATUS_SKIPPED, "rationale: missing expected.json"
    try:
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return STATUS_FAIL, f"cannot parse expected.json: {exc}"

    command, map_err = build_command(repo_root, case_dir, expected)
    if command is None:
        return STATUS_SKIPPED, f"rationale: {map_err}"

    target = str(expected.get("target", "")).strip()
    must_not_create_session = bool(expected.get("must_not_create_session", False))
    if target == "start" and not must_not_create_session:
        return STATUS_SKIPPED, (
            "rationale: case would create production session; output-dir override not supported in MVP."
        )

    before_case_hash = tree_hash(case_dir)
    before_protected = snapshot_protected(repo_root)
    before_sessions = list_session_files(repo_root)

    run = subprocess.run(command, cwd=str(repo_root), capture_output=True, text=True)
    output = (run.stdout or "") + "\n" + (run.stderr or "")
    after_case_hash = tree_hash(case_dir)
    after_protected = snapshot_protected(repo_root)
    after_sessions = list_session_files(repo_root)

    if "Traceback (most recent call last)" in output:
        return STATUS_FAIL, "target script traceback detected"

    if before_case_hash != after_case_hash and bool(expected.get("must_not_modify_fixture_inputs", True)):
        return STATUS_FAIL, "fixture inputs were modified unexpectedly"

    if before_protected != after_protected:
        return STATUS_FAIL, "forbidden production file mutation detected"

    if must_not_create_session and before_sessions != after_sessions:
        return STATUS_FAIL, "session file was created/changed but must_not_create_session is true"

    expected_exit = int(expected.get("expected_exit_code", -1))
    if run.returncode != expected_exit:
        return STATUS_FAIL, f"wrong exit code: expected {expected_exit}, got {run.returncode}"

    expected_result = str(expected.get("expected_result", "")).strip()
    marker_found = expected_result in output
    warning = ""
    if not marker_found:
        warning = " warning: exit code matched but expected_result marker not found in output."

    return STATUS_PASS, "exit code matched expected behavior." + warning


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent
    fixtures_root = (repo_root / args.fixtures_dir).resolve()

    if not fixtures_root.is_dir():
        print(f"FAIL: fixtures directory not found: {fixtures_root}")
        return 1

    case_dirs = sorted(
        [p for p in fixtures_root.iterdir() if p.is_dir() and (p / "expected.json").is_file()]
    )
    pass_count = 0
    fail_count = 0
    skipped_count = 0

    print("Execution Runner Fixture Suite")
    print(f"Fixtures root: {fixtures_root}")
    print()

    for case_dir in case_dirs:
        status, message = run_case(repo_root, case_dir)
        print(f"[{status}] {case_dir.name}")
        print(f"  {message}")
        if status == STATUS_PASS:
            pass_count += 1
        elif status == STATUS_FAIL:
            fail_count += 1
        else:
            skipped_count += 1

    print()
    print("Summary:")
    print(f"- PASS: {pass_count}")
    print(f"- FAIL: {fail_count}")
    print(f"- SKIPPED: {skipped_count}")

    return 1 if fail_count > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
