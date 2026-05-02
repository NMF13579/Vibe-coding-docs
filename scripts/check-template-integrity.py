#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

RESULT_PASS = "PASS"
RESULT_WARN = "WARN"
RESULT_FAIL = "FAIL"
RESULT_NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
RESULT_ERROR = "ERROR"

ALLOWED_RESULTS = {
    RESULT_PASS,
    RESULT_WARN,
    RESULT_FAIL,
    RESULT_NOT_IMPLEMENTED,
    RESULT_ERROR,
}

MINIMAL_DIR = Path("templates/agentos-minimal")
FULL_DIR = Path("templates/agentos-full")

MINIMAL_REQUIRED = [
    "README.md",
    "requirements.txt",
    "scripts/run-all.sh",
    "templates/task.md",
    "templates/verification.md",
]

FULL_REQUIRED = [
    "README.md",
    "requirements.txt",
    "scripts/run-all.sh",
    "templates/task.md",
    "templates/verification.md",
    "docs/architecture.md",
    "docs/guardrails.md",
    "docs/limitations.md",
    "docs/troubleshooting.md",
    "examples/",
]

MINIMAL_FORBIDDEN_FULL_ONLY = [
    "examples/",
    "prompts/",
    "docs/architecture.md",
    "docs/troubleshooting.md",
    "docs/limitations.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only template integrity checker")
    parser.add_argument("--strict", action="store_true", help="Exit 0 only for PASS")
    parser.add_argument("--json", action="store_true", dest="json_mode", help="Print JSON output")
    parser.add_argument("--root", default=".", help="Repository root to inspect")
    return parser.parse_args()


def is_empty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size == 0


def contains_terms(path: Path, terms: list[str]) -> bool:
    data = path.read_text(encoding="utf-8", errors="ignore").lower()
    return all(term in data for term in terms)


def evaluate(root: Path) -> dict:
    checks_run = 0
    checks_passed = 0
    checks_warned = 0
    checks_failed = 0
    checks_skipped = 0
    skipped_checks: list[str] = []

    minimal_root = root / MINIMAL_DIR
    full_root = root / FULL_DIR

    minimal_exists = minimal_root.exists() and minimal_root.is_dir()
    full_exists = full_root.exists() and full_root.is_dir()

    checks_run += 1
    if not minimal_exists and not full_exists:
        checks_passed += 1
        return {
            "check": "template-integrity",
            "result": RESULT_NOT_IMPLEMENTED,
            "checks_run": checks_run,
            "checks_passed": checks_passed,
            "checks_warned": checks_warned,
            "checks_failed": checks_failed,
            "checks_skipped": checks_skipped,
            "skipped_checks": skipped_checks,
            "reason": "Neither templates/agentos-minimal nor templates/agentos-full exists",
        }

    checks_run += 1
    if minimal_exists != full_exists:
        checks_failed += 1
        return {
            "check": "template-integrity",
            "result": RESULT_FAIL,
            "checks_run": checks_run,
            "checks_passed": checks_passed,
            "checks_warned": checks_warned,
            "checks_failed": checks_failed,
            "checks_skipped": checks_skipped,
            "skipped_checks": skipped_checks,
            "reason": "Only one template target exists; both or neither are required",
        }
    checks_passed += 1

    # Both exist: validate minimal required paths
    for rel in MINIMAL_REQUIRED:
        checks_run += 1
        p = minimal_root / rel
        if rel.endswith("/"):
            ok = p.exists() and p.is_dir()
        else:
            ok = p.exists() and p.is_file()
        if ok:
            checks_passed += 1
        else:
            checks_failed += 1

    # minimal must not include full-only paths
    for rel in MINIMAL_FORBIDDEN_FULL_ONLY:
        checks_run += 1
        p = minimal_root / rel
        if p.exists():
            checks_failed += 1
        else:
            checks_passed += 1

    # Full required paths
    for rel in FULL_REQUIRED:
        checks_run += 1
        p = full_root / rel
        if rel.endswith("/"):
            ok = p.exists() and p.is_dir()
        else:
            ok = p.exists() and p.is_file()
        if ok:
            checks_passed += 1
        else:
            checks_failed += 1

    # Empty required files fail
    for rel in MINIMAL_REQUIRED:
        if rel.endswith("/"):
            checks_skipped += 1
            skipped_checks.append(f"empty-file-check skipped for directory path: {rel}")
            continue
        checks_run += 1
        p = minimal_root / rel
        if p.exists() and p.is_file() and is_empty_file(p):
            checks_failed += 1
        else:
            checks_passed += 1

    for rel in FULL_REQUIRED:
        if rel.endswith("/"):
            checks_skipped += 1
            skipped_checks.append(f"empty-file-check skipped for directory path: {rel}")
            continue
        checks_run += 1
        p = full_root / rel
        if p.exists() and p.is_file() and is_empty_file(p):
            checks_failed += 1
        else:
            checks_passed += 1

    # Content checks for task.md and verification.md
    task_terms = ["task", "goal", "acceptance"]
    verification_terms = ["verification", "result", "evidence"]

    checks_run += 1
    min_task = minimal_root / "templates/task.md"
    if min_task.exists() and min_task.is_file() and not contains_terms(min_task, task_terms):
        checks_failed += 1
    else:
        checks_passed += 1

    checks_run += 1
    min_ver = minimal_root / "templates/verification.md"
    if min_ver.exists() and min_ver.is_file() and not contains_terms(min_ver, verification_terms):
        checks_failed += 1
    else:
        checks_passed += 1

    checks_run += 1
    full_task = full_root / "templates/task.md"
    if full_task.exists() and full_task.is_file() and not contains_terms(full_task, task_terms):
        checks_failed += 1
    else:
        checks_passed += 1

    checks_run += 1
    full_ver = full_root / "templates/verification.md"
    if full_ver.exists() and full_ver.is_file() and not contains_terms(full_ver, verification_terms):
        checks_failed += 1
    else:
        checks_passed += 1

    if checks_failed > 0:
        result = RESULT_FAIL
        reason = "Template structure validation failed"
    elif checks_warned > 0:
        result = RESULT_WARN
        reason = "Template structure valid with warnings"
    else:
        result = RESULT_PASS
        reason = "Template structure validation passed"

    return {
        "check": "template-integrity",
        "result": result,
        "checks_run": checks_run,
        "checks_passed": checks_passed,
        "checks_warned": checks_warned,
        "checks_failed": checks_failed,
        "checks_skipped": checks_skipped,
        "skipped_checks": skipped_checks,
        "reason": reason,
    }


def print_text(payload: dict) -> None:
    print("TEMPLATE_INTEGRITY_CHECK: run")
    print(f"TEMPLATE_INTEGRITY_RESULT: {payload['result']}")
    print(f"TEMPLATE_INTEGRITY_CHECKS_RUN: {payload['checks_run']}")
    print(f"TEMPLATE_INTEGRITY_CHECKS_PASSED: {payload['checks_passed']}")
    print(f"TEMPLATE_INTEGRITY_CHECKS_WARNED: {payload['checks_warned']}")
    print(f"TEMPLATE_INTEGRITY_CHECKS_FAILED: {payload['checks_failed']}")
    print(f"TEMPLATE_INTEGRITY_CHECKS_SKIPPED: {payload['checks_skipped']}")
    for item in payload["skipped_checks"]:
        print(f"SKIP: {item}")
    print(f"TEMPLATE_INTEGRITY_REASON: {payload['reason']}")


def exit_code(result: str, strict: bool) -> int:
    if strict:
        return 0 if result == RESULT_PASS else 1
    return 1 if result in {RESULT_FAIL, RESULT_ERROR} else 0


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    payload = evaluate(root)

    if payload["result"] not in ALLOWED_RESULTS:
        payload["result"] = RESULT_ERROR
        payload["reason"] = "Invalid internal result state"

    if args.json_mode:
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print_text(payload)

    return exit_code(payload["result"], args.strict)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        payload = {
            "check": "template-integrity",
            "result": RESULT_ERROR,
            "checks_run": 0,
            "checks_passed": 0,
            "checks_warned": 0,
            "checks_failed": 1,
            "checks_skipped": 0,
            "skipped_checks": [],
            "reason": f"Unhandled exception: {exc.__class__.__name__}",
        }
        args = sys.argv[1:]
        json_mode = "--json" in args
        if json_mode:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print("TEMPLATE_INTEGRITY_CHECK: run")
            print("TEMPLATE_INTEGRITY_RESULT: ERROR")
            print("TEMPLATE_INTEGRITY_CHECKS_RUN: 0")
            print("TEMPLATE_INTEGRITY_CHECKS_PASSED: 0")
            print("TEMPLATE_INTEGRITY_CHECKS_WARNED: 0")
            print("TEMPLATE_INTEGRITY_CHECKS_FAILED: 1")
            print("TEMPLATE_INTEGRITY_CHECKS_SKIPPED: 0")
            print(f"TEMPLATE_INTEGRITY_REASON: Unhandled exception: {exc.__class__.__name__}")
        sys.exit(1)
