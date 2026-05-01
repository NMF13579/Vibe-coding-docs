#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION = "1.0.0"


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def path_exists(path: Path) -> bool:
    return path.exists()


def check_files_exist(paths: list[str]) -> tuple[bool, list[str]]:
    missing: list[str] = []
    for rel in paths:
        if not path_exists(REPO_ROOT / rel):
            missing.append(rel)
    return (len(missing) == 0, missing)


def check_contains(path: str, required_strings: list[str]) -> tuple[bool, list[str]]:
    text = read_text(REPO_ROOT / path)
    if text is None:
        return (False, [f"missing file: {path}"])
    missing: list[str] = []
    for needle in required_strings:
        if needle not in text:
            missing.append(needle)
    return (len(missing) == 0, missing)


def check_any_doc_contains(docs: list[str], required_strings: list[str]) -> tuple[bool, list[str]]:
    texts: dict[str, str] = {}
    for rel in docs:
        text = read_text(REPO_ROOT / rel)
        if text is not None:
            texts[rel] = text

    missing: list[str] = []
    for needle in required_strings:
        found = any(needle in text for text in texts.values())
        if not found:
            missing.append(needle)

    return (len(missing) == 0, missing)


def check_non_equivalence_concept(docs: list[str]) -> tuple[bool, str]:
    direct = "applied transition record ≠ lifecycle mutation"
    fallback_any = [
        "does not automatically imply lifecycle mutation",
        "does not imply lifecycle mutation",
        "not lifecycle mutation",
        "is not lifecycle mutation",
    ]

    for rel in docs:
        text = read_text(REPO_ROOT / rel)
        if text is None:
            continue
        if direct in text:
            return (True, "")
        if "applied transition record" in text and any(fragment in text for fragment in fallback_any):
            return (True, "")

    return (
        False,
        "applied transition record non-equivalence not found in either integration document",
    )


def print_group(name: str, passed: bool, details: list[str]) -> None:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        for line in details:
            print(f"  {line}")


def main() -> int:
    print("Lifecycle Apply Validation")
    print(f"version: {VERSION}")
    print("checks: 8")
    print()

    all_passed = True

    m15_paths = [
        "docs/CONTROLLED-LIFECYCLE-MUTATION.md",
        "docs/APPLY-PRECONDITIONS.md",
        "docs/APPLIED-TRANSITION-RECORD.md",
        "docs/APPLY-PLAN.md",
        "docs/COMPLETION-TRANSITION.md",
        "templates/applied-transition-record.md",
        "templates/apply-plan.md",
        "templates/completion-transition.md",
        "scripts/check-apply-preconditions.py",
        "scripts/apply-transition.py",
    ]
    ok, missing = check_files_exist(m15_paths)
    details = [f"missing: {m}" for m in missing]
    print_group("Required M15 source-of-truth files", ok, details)
    all_passed = all_passed and ok

    m16_paths = [
        "docs/LIFECYCLE-INTEGRATION.md",
        "docs/APPLY-COMMAND-INTEGRATION.md",
    ]
    ok, missing = check_files_exist(m16_paths)
    details = [f"missing: {m}" for m in missing]
    print_group("Required M16 integration files", ok, details)
    all_passed = all_passed and ok

    fixture_paths = [
        "scripts/test-apply-transition-fixtures.py",
        "tests/fixtures/apply-transition",
    ]
    ok, missing = check_files_exist(fixture_paths)
    details = [f"missing: {m}" for m in missing]
    print_group("M15 fixture coverage presence", ok, details)
    all_passed = all_passed and ok

    lifecycle_hooks = [
        "lifecycle_integration:",
        "strict_sequence_required: true",
        "failure_semantics_defined: true",
        "evidence_chain_required: true",
        "human_approval_boundary_defined: true",
        "autonomous_lifecycle_authority: false",
        "complete-active",
    ]
    ok, missing = check_contains("docs/LIFECYCLE-INTEGRATION.md", lifecycle_hooks)
    details = [f"missing substring: {m}" for m in missing]
    print_group("Lifecycle integration machine hooks", ok, details)
    all_passed = all_passed and ok

    apply_hooks = [
        "apply_command_integration:",
        "command_surface: scripts/apply-transition.py",
        "strict_order_required: true",
        "command_non_equivalence_defined: true",
        "write_boundary_defined: true",
        "failure_semantics_defined: true",
        "autonomous_lifecycle_authority: false",
        "complete-active",
    ]
    ok, missing = check_contains("docs/APPLY-COMMAND-INTEGRATION.md", apply_hooks)
    details = [f"missing substring: {m}" for m in missing]
    print_group("Apply command integration machine hooks", ok, details)
    all_passed = all_passed and ok

    mode_surface = [
        "--dry-run",
        "--prepare",
        "--plan-out",
        "--apply",
        "--applied-record-out",
        "--complete-active-plan",
        "--complete-active",
    ]
    ok, missing = check_contains("scripts/apply-transition.py", mode_surface)
    details = [f"missing substring: {m}" for m in missing]
    print_group("Apply script mode surface", ok, details)
    all_passed = all_passed and ok

    preconditions_vocab = ["PASS", "BLOCKED"]
    ok, missing = check_contains("scripts/check-apply-preconditions.py", preconditions_vocab)
    details = [f"missing substring: {m}" for m in missing]
    print_group("Apply preconditions checker presence", ok, details)
    all_passed = all_passed and ok

    docs = ["docs/LIFECYCLE-INTEGRATION.md", "docs/APPLY-COMMAND-INTEGRATION.md"]
    concept_map = {
        "No autonomous lifecycle authority": "autonomous lifecycle authority",
        "Human approval boundary": "human approval",
        "Failure does not authorize mutation": "failure does not authorize lifecycle mutation",
        "Controlled mutation path": "complete-active",
    }

    details: list[str] = []
    ok_main = True

    ok_any, missing = check_any_doc_contains(docs, list(concept_map.values()))
    if not ok_any:
        ok_main = False
        missing_by_name = {v: k for k, v in concept_map.items()}
        for m in missing:
            details.append(f"missing concept: {missing_by_name.get(m, m)}")

    ok_non_eq, message = check_non_equivalence_concept(docs)
    if not ok_non_eq:
        ok_main = False
        details.append(message)

    print_group("Safety language coverage", ok_main, details)
    all_passed = all_passed and ok_main

    print()
    print(f"Result: {'PASS' if all_passed else 'FAIL'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
