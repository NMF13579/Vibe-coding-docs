#!/usr/bin/env python3
"""Negative fixture runner for AgentOS approval markers."""
# Expected rejection is PASS for this suite.

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = REPO_ROOT / "scripts" / "validate-approval-marker.py"
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "negative" / "approval-markers"
PLACEHOLDER = "__FIXTURE_DIR__"
MAX_FILES = 200


def usage() -> None:
    print("Usage: python3 scripts/test-approval-marker-fixtures.py [fixture-root]")


def load_fixture_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def copy_fixture(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, dirs_exist_ok=True)
    for file_path in dst.rglob("*"):
        if not file_path.is_file():
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if PLACEHOLDER in text:
            file_path.write_text(text.replace(PLACEHOLDER, str(dst)), encoding="utf-8")


def run_validator(marker: Path, task: str, scope: str, transition: str | None) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(VALIDATOR),
        str(marker),
        "--task",
        task,
        "--scope",
        scope,
    ]
    if transition:
        cmd.extend(["--transition", transition])
    return subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )


def summarize_output(output: str) -> str:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if not lines:
        return "no output"
    return lines[-1]


def main(argv: list[str]) -> int:
    if len(argv) > 1 or any(arg in {"-h", "--help"} for arg in argv):
        usage()
        return 2  # usage error -> exit 2

    fixture_root = Path(argv[0]) if argv else FIXTURE_ROOT
    if not VALIDATOR.exists():
        print("APPROVAL MARKER FIXTURES TEST")
        print("Result: FAIL")
        print("Reason: scripts/validate-approval-marker.py not found")
        return 2  # usage error -> exit 2
    if not fixture_root.exists() or not fixture_root.is_dir():
        print("APPROVAL MARKER FIXTURES TEST")
        print(f"Result: FAIL")
        print(f"Reason: fixture directory missing: {fixture_root}")
        return 2  # usage error -> exit 2

    fixture_dirs = sorted(path for path in fixture_root.iterdir() if path.is_dir())
    if not fixture_dirs:
        print("APPROVAL MARKER FIXTURES TEST")
        print("Result: FAIL")
        print("Reason: no fixture directories found")
        return 2

    overall_ok = True
    print("APPROVAL MARKER FIXTURES TEST")
    for fixture_dir in fixture_dirs:
        fixture_json_path = fixture_dir / "fixture.json"
        if not fixture_json_path.exists():
            print(f"{fixture_dir.name}: FAIL (missing fixture.json)")
            return 2  # usage error -> exit 2
        try:
            fixture = load_fixture_json(fixture_json_path)
        except Exception as exc:
            print(f"{fixture_dir.name}: FAIL (unreadable fixture.json: {exc})")
            return 2  # usage error -> exit 2

        marker_rel = fixture.get("marker")
        task = fixture.get("task")
        scope = fixture.get("scope")
        transition = fixture.get("transition")
        expected_exit = fixture.get("expected_exit")
        expected_result = fixture.get("expected_result", "FAIL")

        if not isinstance(marker_rel, str) or not isinstance(task, str) or not isinstance(scope, str):
            print(f"{fixture_dir.name}: FAIL (fixture.json missing required fields)")
            overall_ok = False
            continue

        with tempfile.TemporaryDirectory(prefix=f"approval-fixture-{fixture_dir.name}-") as temp_root_text:
            temp_root = Path(temp_root_text)
            temp_fixture = temp_root / fixture_dir.name
            copy_fixture(fixture_dir, temp_fixture)
            marker_path = temp_fixture / marker_rel
            if not marker_path.exists():
                print(f"{fixture_dir.name}: FAIL (marker file missing in temp workspace)")
                overall_ok = False
                continue

            completed = run_validator(marker_path, task, scope, transition)
            actual_exit = completed.returncode
            actual_result = "PASS" if actual_exit == 0 else "FAIL"

            if actual_result != expected_result:
                fixture_ok = False
            elif expected_exit is not None and actual_exit != expected_exit:
                fixture_ok = False
            elif actual_exit == 0:
                fixture_ok = False
            else:
                fixture_ok = True

            status = "PASS" if fixture_ok else "FAIL"
            print(f"{fixture_dir.name}: {status}")
            if not fixture_ok:
                overall_ok = False
                print("  Validator output:")
                for line in completed.stdout.splitlines():
                    print(f"  {line}")
                if completed.stderr.strip():
                    print("  Stderr:")
                    for line in completed.stderr.splitlines():
                        print(f"  {line}")

    print(f"Result: {'PASS' if overall_ok else 'FAIL'}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
