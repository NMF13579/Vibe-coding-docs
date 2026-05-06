#!/usr/bin/env python3
import sys
import re
from pathlib import Path


RESULT_PASS = "PASS"
RESULT_FAIL = "FAIL"
RESULT_ERROR = "ERROR"

REQUIRED_INVALID = [
    "missing-agentos-validate.yml",
    "missing-json-output.yml",
    "missing-artifact-upload.yml",
    "missing-artifact-if-always.yml",
    "json-not-preserved-after-failure.yml",
    "uses-secrets.yml",
    "pushes-commits.yml",
    "deploys.yml",
    "releases.yml",
    "auto-approves.yml",
    "merges.yml",
    "write-permissions.yml",
    "silent-ignore-failures.yml",
]

FORBIDDEN_PATTERNS = [
    r"secrets\.",
    r"git\s+push",
    r"gh\s+pr\s+merge",
    r"gh\s+pr\s+review\s+--approve",
    r"auto-merge",
    r"merge pull request",
    r"deployment",
    r"deploy",
    r"release",
    r"protected branch",
    r"required check",
    r"branch protection",
    r"codeowners enforcement",
    r"approval token",
    r"write-all permissions",
]

WRITE_PERM_PATTERNS = [
    r"contents:\s*write",
    r"pull-requests:\s*write",
    r"issues:\s*write",
    r"actions:\s*write",
    r"checks:\s*write",
    r"permissions:\s*write-all",
]


def clean_executable_lines(text):
    lines = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        stripped = raw.lstrip()
        if stripped.startswith("#"):
            continue
        if "#" in raw:
            raw = raw.split("#", 1)[0]
        if raw.strip():
            lines.append(raw.rstrip())
    return lines


def find_step_blocks(lines):
    blocks = []
    current = []
    in_steps = False
    for line in lines:
        if re.match(r"^\s*steps\s*:\s*$", line):
            in_steps = True
            continue
        if not in_steps:
            continue
        if re.match(r"^\s*-\s+name\s*:", line) or re.match(r"^\s*-\s+uses\s*:", line) or re.match(r"^\s*-\s+run\s*:", line):
            if current:
                blocks.append("\n".join(current))
            current = [line]
        else:
            if current:
                current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def has_case_insensitive(lines, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    for line in lines:
        if regex.search(line):
            return True
    return False


def index_of_line(lines, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    for i, line in enumerate(lines):
        if regex.search(line):
            return i
    return -1


def validate_workflow_file(path):
    failures = []
    warnings = []

    if not path.is_file():
        return RESULT_ERROR, [f"missing workflow file: {path}"], warnings

    text = path.read_text(encoding="utf-8")
    lines = clean_executable_lines(text)
    lower_blob = "\n".join(lines).lower()

    required_checks = [
        (r"\bpull_request\s*:", "missing pull_request trigger"),
        (r"\bpush\s*:", "missing push trigger"),
        (r"branches\s*:", "missing push trigger for dev"),
        (r"actions/checkout", "missing actions/checkout"),
        (r"actions/setup-python", "missing actions/setup-python"),
        (r"python\s+-m\s+py_compile\s+scripts/agentos-validate\.py", "missing py_compile command"),
        (r"python\s+scripts/agentos-validate\.py\s+all(\s|$)", "missing human-readable all command"),
        (r"python\s+scripts/agentos-validate\.py\s+all\s+--json", "missing json all command"),
        (r"reports/ci/agentos-validate\.json", "missing json artifact path write"),
        (r"actions/upload-artifact", "missing artifact upload"),
        (r"agentos-validation-evidence", "missing artifact name"),
    ]

    for pattern, message in required_checks:
        if not has_case_insensitive(lines, pattern):
            failures.append(message)

    has_dev_branch = has_case_insensitive(lines, r"-\s*dev\b") or has_case_insensitive(lines, r"\[\s*dev\s*\]")
    if not has_dev_branch:
        failures.append("missing push trigger for dev")

    blocks = find_step_blocks(lines)
    upload_has_if_always = False
    for b in blocks:
        if re.search(r"actions/upload-artifact", b, re.IGNORECASE):
            if re.search(r"\bif\s*:\s*always\(\)", b, re.IGNORECASE):
                upload_has_if_always = True
    if not upload_has_if_always:
        failures.append("artifact upload step missing explicit if: always()")

    human_idx = index_of_line(lines, r"python\s+scripts/agentos-validate\.py\s+all(\s|$)")
    json_idx = index_of_line(lines, r"python\s+scripts/agentos-validate\.py\s+all\s+--json")
    if human_idx == -1 or json_idx == -1:
        failures.append("cannot verify JSON evidence generation sequencing")
    else:
        human_continue = False
        for b in blocks:
            if re.search(r"python\s+scripts/agentos-validate\.py\s+all(\s|$)", b, re.IGNORECASE):
                if re.search(r"continue-on-error\s*:\s*true", b, re.IGNORECASE):
                    human_continue = True
        if not (json_idx > human_idx and human_continue):
            failures.append("JSON evidence generation can be skipped after human validation failure")

    if "|| true" in lower_blob:
        failures.append("silent unconditional || true detected")

    any_continue = has_case_insensitive(lines, r"continue-on-error\s*:\s*true")
    has_outcome_report = has_case_insensitive(lines, r"steps\.[a-z0-9_-]+\.outcome")
    if any_continue and not has_outcome_report:
        warnings.append("continue-on-error used without later outcome reporting")

    for pattern in FORBIDDEN_PATTERNS:
        if has_case_insensitive(lines, pattern):
            failures.append(f"forbidden pattern detected: {pattern}")

    for pattern in WRITE_PERM_PATTERNS:
        if has_case_insensitive(lines, pattern):
            failures.append(f"write permission detected: {pattern}")

    if failures:
        return RESULT_FAIL, failures, warnings
    return RESULT_PASS, failures, warnings


def main():
    repo_root = Path.cwd()
    workflow_path = repo_root / ".github/workflows/agentos-validate.yml"
    fixtures_root = repo_root / "tests/fixtures/ci-advisory"
    valid_dir = fixtures_root / "valid"
    invalid_dir = fixtures_root / "invalid"

    try:
        if not fixtures_root.is_dir() or not valid_dir.is_dir() or not invalid_dir.is_dir():
            print("Final result: ERROR")
            print("Missing fixture directories")
            return 3

        valid_file = valid_dir / "advisory-workflow.yml"
        if not valid_file.is_file():
            print("Final result: ERROR")
            print("Missing required valid fixture: advisory-workflow.yml")
            return 3

        missing_invalid = [name for name in REQUIRED_INVALID if not (invalid_dir / name).is_file()]
        if missing_invalid:
            print("Final result: ERROR")
            print("Missing required invalid fixtures:")
            for name in missing_invalid:
                print(f"- {name}")
            return 3

        real_result, real_failures, real_warnings = validate_workflow_file(workflow_path)

        valid_checked = 0
        valid_failed = []

        vr, vf, vw = validate_workflow_file(valid_file)
        valid_checked += 1
        if vr != RESULT_PASS:
            valid_failed.append((valid_file.name, vf))

        invalid_checked = 0
        invalid_failed = []
        for fixture in sorted(invalid_dir.glob("*.yml")):
            invalid_checked += 1
            ir, ifails, iwarns = validate_workflow_file(fixture)
            if ir != RESULT_FAIL:
                invalid_failed.append((fixture.name, ir, ifails, iwarns))

        failures = []
        if real_result != RESULT_PASS:
            failures.append("real workflow failed advisory checks")
        if valid_failed:
            failures.append("valid fixture failed")
        if invalid_failed:
            failures.append("one or more invalid fixtures passed")

        print(f"Real workflow result: {real_result}")
        print(f"Valid fixtures checked: {valid_checked}")
        print(f"Invalid fixtures checked: {invalid_checked}")
        print(f"Warnings: {len(real_warnings)}")

        if real_failures:
            print("Real workflow failures:")
            for item in real_failures:
                print(f"- {item}")

        if real_warnings:
            print("Warnings detail:")
            for item in real_warnings:
                print(f"- {item}")

        if valid_failed:
            print("Valid fixture failures:")
            for name, errs in valid_failed:
                print(f"- {name}")
                for err in errs:
                    print(f"  - {err}")

        if invalid_failed:
            print("Invalid fixtures that did not fail:")
            for name, result, errs, warns in invalid_failed:
                print(f"- {name}: {result}")

        if failures:
            print("Final result: FAIL")
            print("Failures:")
            for item in failures:
                print(f"- {item}")
            return 1

        print("Final result: PASS")
        print("Confirmation: no enforcement behavior detected")
        print("Confirmation: no write-permission behavior detected")
        return 0
    except Exception as exc:
        print("Final result: ERROR")
        print(f"Internal exception: {exc}")
        return 3


if __name__ == "__main__":
    sys.exit(main())
