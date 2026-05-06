#!/usr/bin/env python3

import argparse
from pathlib import Path
import re
import sys


ENFORCEMENT_READY = "ENFORCEMENT_READY"
READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
NEEDS_REVIEW = "NEEDS_REVIEW"
NOT_READY = "NOT_READY"

WARNING_PREFIX = "WARNING"

DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = DEFAULT_REPO_ROOT

HARD_REQUIRED_FILES = [
    Path("docs/ENFORCED-REQUIRED-CHECKS.md"),
    Path("docs/REQUIRED-CHECK-NAMES.md"),
    Path("docs/BRANCH-PROTECTION-SETUP.md"),
    Path("templates/platform-enforcement-evidence.md"),
    Path("reports/platform-required-checks-evidence.md"),
    Path(".github/workflows/agentos-validate.yml"),
]

ADVISORY_FILES = [Path("templates/enforcement-review.md")]

WORKFLOW_FILE = REPO_ROOT / ".github/workflows/agentos-validate.yml"
REQUIRED_CHECK_NAMES_FILE = REPO_ROOT / "docs/REQUIRED-CHECK-NAMES.md"
ENFORCED_REQUIRED_CHECKS_FILE = REPO_ROOT / "docs/ENFORCED-REQUIRED-CHECKS.md"
BRANCH_PROTECTION_SETUP_FILE = REPO_ROOT / "docs/BRANCH-PROTECTION-SETUP.md"
PLATFORM_EVIDENCE_TEMPLATE_FILE = REPO_ROOT / "templates/platform-enforcement-evidence.md"
PLATFORM_EVIDENCE_REPORT_FILE = REPO_ROOT / "reports/platform-required-checks-evidence.md"
ENFORCEMENT_REVIEW_TEMPLATE_FILE = REPO_ROOT / "templates/enforcement-review.md"

EXPECTED_REQUIRED_CHECK = "AgentOS Validate / agentos-validate"
EXPECTED_WORKFLOW_NAME = "AgentOS Validate"
EXPECTED_JOB_ID = "agentos-validate"
EXPECTED_JOB_DISPLAY_NAME = "agentos-validate"
BLOCKING_RESULTS = ["WARN", "FAIL", "ERROR", "NOT_RUN", "INCOMPLETE"]


def read_text(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def is_comment_line(line: str) -> bool:
    return bool(re.match(r"^\s*#", line))


def non_comment_lines_with_numbers(text: str):
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not is_comment_line(line):
            yield lineno, line


def search_non_comment_lines(text: str, pattern: str):
    regex = re.compile(pattern)
    return [(lineno, line) for lineno, line in non_comment_lines_with_numbers(text) if regex.search(line)]


def file_status(path: Path):
    return "PRESENT" if path.exists() else "MISSING"


def extract_enforcement_step_body(workflow_text: str):
    lines = workflow_text.splitlines()
    step_indexes = []

    for idx, line in enumerate(lines):
        if is_comment_line(line):
            continue
        if re.match(r"^\s*-\s+name:\s*Enforce AgentOS validation result\s*$", line):
            step_indexes.append(idx)

    if len(step_indexes) != 1:
        return None, "enforcement step cannot be isolated safely"

    step_idx = step_indexes[0]
    step_indent = len(lines[step_idx]) - len(lines[step_idx].lstrip(" "))

    run_idx = None
    run_indent = None

    for idx in range(step_idx + 1, len(lines)):
        line = lines[idx]
        stripped = line.strip()

        if stripped and not is_comment_line(line):
            indent = len(line) - len(line.lstrip(" "))
            if re.match(r"^\s*-\s+name:\s*", line) and indent <= step_indent:
                break

        if re.match(r"^\s*run:\s*\|\s*$", line):
            run_idx = idx
            run_indent = len(line) - len(line.lstrip(" "))
            break

    if run_idx is None:
        return None, "enforcement step cannot be isolated safely"

    body = []
    for idx in range(run_idx + 1, len(lines)):
        line = lines[idx]
        stripped = line.strip()
        if stripped:
            indent = len(line) - len(line.lstrip(" "))
            if indent <= run_indent and not is_comment_line(line):
                break
        body.append((idx + 1, line))

    if not body:
        return None, "enforcement step cannot be isolated safely"

    return body, None


def find_line_hits(text: str, pattern: str):
    return search_non_comment_lines(text, pattern)


def first_line_hit(text: str, pattern: str):
    hits = find_line_hits(text, pattern)
    return hits[0] if hits else None


def line_has_any_non_comment(text: str, patterns):
    for pattern in patterns:
        if first_line_hit(text, pattern):
            return True
    return False


def report_line_value(text: str, key: str):
    pattern = rf"^\s*[-*]\s+{re.escape(key)}:\s*(.+?)\s*$"
    hit = first_line_hit(text, pattern)
    if not hit:
        return None
    _, line = hit
    value = line.split(":", 1)[1].strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        value = value[1:-1].strip()
    return value


def section_text(text: str, heading: str):
    pattern = rf"^## {re.escape(heading)}\s*$"
    lines = text.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if re.match(pattern, line):
            start = idx
            break
    if start is None:
        return None

    end = len(lines)
    for idx in range(start + 1, len(lines)):
        if re.match(r"^##\s+", lines[idx]):
            end = idx
            break

    return "\n".join(lines[start:end])


def section_first_value(text: str, heading: str):
    section = section_text(text, heading)
    if section is None:
        return None

    lines = section.splitlines()[1:]
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("##"):
            continue
        if stripped.startswith("- "):
            stripped = stripped[2:].strip()
        return stripped.strip("`").strip()

    return None


def bullet_value(line: str, key: str):
    match = re.match(rf"^\s*-\s*{re.escape(key)}:\s*(.*)$", line)
    if not match:
        return None
    return match.group(1).strip()


def body_non_comment_text(body):
    return "\n".join(line for _, line in body if not is_comment_line(line))


def allow_or_enable_match(line: str):
    topic = re.search(r"\b(auto[- ]merge|automatic approval)\b", line, re.IGNORECASE)
    if not topic:
        return False

    safe_negation = re.search(
        r"\b("
        r"forbidden|forbid|forbids|forbidding|"
        r"does not authorize|do not authorize|doesn't authorize|don't authorize|"
        r"not authorize|not authorized|not allowed|is not allowed|"
        r"not automatic approval|not auto-merge|not auto merge|"
        r"cannot|can't|must not|prohibited|prohibit|prohibits|"
        r"disallowed|disallow|disallows|blocked|block|blocks|"
        r"no auto-merge|no automatic approval|"
        r"auto-merge is forbidden|automatic approval is forbidden"
        r")\b",
        line,
        re.IGNORECASE,
    )
    if safe_negation:
        return False

    allowance = re.search(
        r"\b("
        r"allowed|allow|allows|allowing|"
        r"enabled|enable|enables|enabling|"
        r"authorize|authorizes|authorized|authorizing|"
        r"require|requires|required|requiring|"
        r"permit|permits|permitted|permitting|"
        r"may|can"
        r")\b",
        line,
        re.IGNORECASE,
    )
    return bool(allowance)


def release_gate_match(line: str):
    if not re.search(r"\b(deployment|release gate|release-gate)\b", line, re.IGNORECASE):
        return False
    if not re.search(r"\b(M25|enforcement)\b", line, re.IGNORECASE):
        return False
    if re.search(r"\b(forbidden|forbid|not|never|no)\b", line, re.IGNORECASE):
        return False
    return True


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Read-only audit for M25 enforcement readiness.")
    parser.add_argument(
        "--root",
        default=str(DEFAULT_REPO_ROOT),
        help="Repository root to audit (default: current repository root).",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    repo_root = Path(args.root).resolve()

    WORKFLOW_FILE = repo_root / ".github/workflows/agentos-validate.yml"
    REQUIRED_CHECK_NAMES_FILE = repo_root / "docs/REQUIRED-CHECK-NAMES.md"
    ENFORCED_REQUIRED_CHECKS_FILE = repo_root / "docs/ENFORCED-REQUIRED-CHECKS.md"
    BRANCH_PROTECTION_SETUP_FILE = repo_root / "docs/BRANCH-PROTECTION-SETUP.md"
    PLATFORM_EVIDENCE_TEMPLATE_FILE = repo_root / "templates/platform-enforcement-evidence.md"
    PLATFORM_EVIDENCE_REPORT_FILE = repo_root / "reports/platform-required-checks-evidence.md"
    ENFORCEMENT_REVIEW_TEMPLATE_FILE = repo_root / "templates/enforcement-review.md"

    warnings = []
    failures = []
    platform_report_missing = False

    required_file_lines = []
    for rel_path in HARD_REQUIRED_FILES:
        abs_path = repo_root / rel_path
        status = file_status(abs_path)
        required_file_lines.append(f"- {rel_path.as_posix()}: {status}")
        if status == "MISSING":
            if rel_path == Path("reports/platform-required-checks-evidence.md"):
                platform_report_missing = True
            else:
                failures.append(f"Missing hard-required file: {rel_path.as_posix()}")

    advisory_lines = []
    for rel_path in ADVISORY_FILES:
        abs_path = repo_root / rel_path
        status = file_status(abs_path)
        advisory_lines.append(f"- {rel_path.as_posix()}: {status}")
        if status == "MISSING":
            warnings.append(
                f"{WARNING_PREFIX}: advisory template {rel_path.as_posix()} is missing; review handling stays human-led."
            )

    workflow_text = read_text(WORKFLOW_FILE)
    workflow_check_lines = []
    workflow_safe = True
    workflow_body = None
    workflow_body_error = None
    workflow_permissions_write = False

    if workflow_text is None:
        failures.append("Missing workflow file: .github/workflows/agentos-validate.yml")
        workflow_safe = False
        workflow_check_lines.append("- workflow file: MISSING")
    else:
        workflow_check_lines.append("- workflow file: PRESENT")

        if find_line_hits(workflow_text, rf"^\s*name:\s*{re.escape(EXPECTED_WORKFLOW_NAME)}\s*$"):
            workflow_check_lines.append(f"- workflow name is {EXPECTED_WORKFLOW_NAME}: PASS")
        else:
            workflow_check_lines.append(f"- workflow name is {EXPECTED_WORKFLOW_NAME}: FAIL")
            failures.append(f"Workflow name is not {EXPECTED_WORKFLOW_NAME}.")

        if find_line_hits(workflow_text, rf"^\s*{re.escape(EXPECTED_JOB_ID)}:\s*$"):
            workflow_check_lines.append(f"- job ID {EXPECTED_JOB_ID} exists: PASS")
        else:
            workflow_check_lines.append(f"- job ID {EXPECTED_JOB_ID} exists: FAIL")
            failures.append(f"Job ID {EXPECTED_JOB_ID} is missing.")

        if find_line_hits(workflow_text, rf"^\s*name:\s*{re.escape(EXPECTED_JOB_DISPLAY_NAME)}\s*$"):
            workflow_check_lines.append(f"- job display name {EXPECTED_JOB_DISPLAY_NAME} exists: PASS")
        else:
            workflow_check_lines.append(f"- job display name {EXPECTED_JOB_DISPLAY_NAME} exists: FAIL")
            failures.append(f"Job display name {EXPECTED_JOB_DISPLAY_NAME} is missing.")

        if line_has_any_non_comment(
            workflow_text,
            [
                r"actions/upload-artifact@v4",
                r"Upload validation artifact",
            ],
        ):
            workflow_check_lines.append("- workflow includes evidence upload behavior: PASS")
        else:
            workflow_check_lines.append("- workflow includes evidence upload behavior: FAIL")
            failures.append("Workflow does not include evidence upload behavior.")

        if find_line_hits(workflow_text, r"if:\s*always\(\)"):
            workflow_check_lines.append("- workflow includes if: always(): PASS")
        else:
            workflow_check_lines.append("- workflow includes if: always(): FAIL")
            failures.append("Workflow does not include if: always().")

        if find_line_hits(workflow_text, r"Enforce AgentOS validation result"):
            workflow_check_lines.append("- workflow includes an enforcement step: PASS")
        else:
            workflow_check_lines.append("- workflow includes an enforcement step: FAIL")
            failures.append("Workflow does not include the enforcement step.")

        workflow_body, workflow_body_error = extract_enforcement_step_body(workflow_text)
        if workflow_body is None:
            workflow_safe = False
            workflow_check_lines.append(f"- enforcement step isolation: FAIL ({workflow_body_error})")
        else:
            workflow_check_lines.append("- enforcement step isolation: PASS")

            body_text = body_non_comment_text(workflow_body)
            blocking_hits = [token for token in BLOCKING_RESULTS if re.search(rf"\b{re.escape(token)}\b", body_text)]
            if len(blocking_hits) == len(BLOCKING_RESULTS):
                workflow_check_lines.append(
                    "- workflow blocks WARN/FAIL/ERROR/NOT_RUN/INCOMPLETE: PASS"
                )
            else:
                missing = ", ".join(token for token in BLOCKING_RESULTS if token not in blocking_hits)
                workflow_check_lines.append(
                    f"- workflow blocks WARN/FAIL/ERROR/NOT_RUN/INCOMPLETE: FAIL (missing {missing})"
                )
                failures.append(f"Workflow enforcement step is missing blocking result token(s): {missing}.")

            if re.search(r"if not path\.exists\(\):", body_text) and re.search(
                r"Blocking merge due to missing result\.", body_text
            ) and re.search(r"if result == \"\"", body_text) and re.search(
                r"if result != \"PASS\":", body_text
            ):
                workflow_check_lines.append(
                    "- workflow handles missing or invalid result as failure: PASS"
                )
            else:
                workflow_check_lines.append(
                    "- workflow handles missing or invalid result as failure: FAIL"
                )
                failures.append("Workflow does not clearly fail closed on missing or invalid AgentOS results.")

            if re.search(r"continue-on-error:\s*true", body_text, re.IGNORECASE) or re.search(
                r"\|\|\s*true", body_text
            ):
                workflow_check_lines.append(
                    "- workflow does not hide enforcement failure with continue-on-error: true: FAIL"
                )
                failures.append(
                    "Enforcement step body contains failure-masking text: continue-on-error: true."
                )
            else:
                workflow_check_lines.append(
                    "- workflow does not hide enforcement failure with continue-on-error: true: PASS"
                )

            if re.search(r"\|\|\s*true", body_text):
                workflow_check_lines.append("- workflow does not hide enforcement failure with || true: FAIL")
                failures.append("Enforcement step body contains failure-masking text: || true.")
            else:
                workflow_check_lines.append("- workflow does not hide enforcement failure with || true: PASS")

        if find_line_hits(workflow_text, r"^\s*contents:\s*write\s*$"):
            workflow_permissions_write = True
            workflow_check_lines.append("- workflow does not allow contents: write: FAIL")
            failures.append("Workflow allows contents: write.")
        else:
            workflow_check_lines.append("- workflow does not allow contents: write: PASS")

    required_check_lines = []
    required_check_text = read_text(REQUIRED_CHECK_NAMES_FILE)
    if required_check_text is None:
        failures.append("Missing required check names document: docs/REQUIRED-CHECK-NAMES.md")
        required_check_lines.append("- AgentOS Validate / agentos-validate documented: FAIL")
    else:
        if find_line_hits(required_check_text, re.escape(EXPECTED_REQUIRED_CHECK)):
            required_check_lines.append(
                f"- {EXPECTED_REQUIRED_CHECK} documented: PASS"
            )
        else:
            required_check_lines.append(
                f"- {EXPECTED_REQUIRED_CHECK} documented: FAIL"
            )
            failures.append(
                f"Required check name {EXPECTED_REQUIRED_CHECK} is not documented."
            )

    if read_text(ENFORCED_REQUIRED_CHECKS_FILE) is None:
        failures.append("Missing enforced required checks contract document: docs/ENFORCED-REQUIRED-CHECKS.md")
    if read_text(BRANCH_PROTECTION_SETUP_FILE) is None:
        failures.append("Missing branch protection setup guide: docs/BRANCH-PROTECTION-SETUP.md")
    if read_text(PLATFORM_EVIDENCE_TEMPLATE_FILE) is None:
        failures.append("Missing platform evidence template: templates/platform-enforcement-evidence.md")

    platform_lines = []
    platform_text = read_text(PLATFORM_EVIDENCE_REPORT_FILE)
    platform_status = None
    human_verifier = None
    dev_section_ok = False
    main_section_ok = False
    repo_platform_distinction_ok = False
    placeholder_violation = False
    bypass_exposure = False

    if platform_text is None:
        platform_report_missing = True
        warnings.append(
            "Platform evidence report is missing; enforcement cannot be confirmed safely."
        )
        platform_lines.append("- platform evidence report: MISSING")
    else:
        platform_lines.append("- platform evidence report: PRESENT")
        repo_platform_distinction_ok = (
            "Repository state = files in repo." in platform_text
            and "Platform state = GitHub branch protection / required checks settings." in platform_text
            and "Repository files alone are not proof of platform enforcement." in platform_text
        )
        platform_lines.append(
            f"- repository state vs platform state distinction: {'PASS' if repo_platform_distinction_ok else 'FAIL'}"
        )
        if not repo_platform_distinction_ok:
            failures.append("Platform evidence does not clearly separate repository state from platform state.")

        dev_section_ok = "## Branch evidence: dev" in platform_text
        main_section_ok = "## Branch evidence: main" in platform_text
        platform_lines.append(f"- dev branch evidence block present: {'PASS' if dev_section_ok else 'FAIL'}")
        platform_lines.append(f"- main branch evidence block present: {'PASS' if main_section_ok else 'FAIL'}")
        if not dev_section_ok:
            failures.append("Platform evidence is missing the dev branch evidence block.")
        if not main_section_ok:
            failures.append("Platform evidence is missing the main branch evidence block.")

        platform_status = report_line_value(platform_text, "Final platform enforcement status")
        human_verifier = section_first_value(platform_text, "Human verifier")

        if platform_status is None:
            platform_lines.append("- final platform enforcement status: MISSING")
            warnings.append(
                "Platform evidence final status is missing; enforcement cannot be classified safely."
            )
        else:
            platform_lines.append(f"- final platform enforcement status: {platform_status}")

        if human_verifier is None:
            platform_lines.append("- human verifier: MISSING")
            warnings.append("Human verifier is missing from the platform evidence report.")
        else:
            platform_lines.append(f"- human verifier: {human_verifier}")

        if platform_status == "PLATFORM_ENFORCED":
            placeholder_patterns = [
                r":\s*YES / NO / UNKNOWN",
                r":\s*NONE / list / UNKNOWN",
                r":\s*PLATFORM_ENFORCED / PARTIAL_PLATFORM_ENFORCEMENT / NOT_ENFORCED / NEEDS_REVIEW",
                r"\bUNKNOWN\b",
            ]
            placeholder_hits = []
            for pattern in placeholder_patterns:
                placeholder_hits.extend(search_non_comment_lines(platform_text, pattern))
            placeholder_violation = bool(placeholder_hits)

            if placeholder_violation:
                failures.append(
                    "Platform evidence claims PLATFORM_ENFORCED while unresolved placeholders or UNKNOWN values remain."
                )

            exposure_hits = []
            for lineno, line in non_comment_lines_with_numbers(platform_text):
                bypass_value = bullet_value(line, "Bypass permissions")
                if bypass_value is not None and bypass_value not in {"NONE", "UNKNOWN"}:
                    exposure_hits.append(f"{lineno}: {line.strip()}")

                admin_bypass_value = bullet_value(line, "Admin bypass allowed")
                if admin_bypass_value == "YES":
                    exposure_hits.append(f"{lineno}: {line.strip()}")
            bypass_exposure = bool(exposure_hits)
            if bypass_exposure:
                failures.append(
                    "Platform evidence claims PLATFORM_ENFORCED while bypass or admin bypass exposure is present."
                )

            if not placeholder_violation and not bypass_exposure:
                platform_lines.append(
                    "- PLATFORM_ENFORCED consistency check: PASS"
                )
            else:
                platform_lines.append(
                    "- PLATFORM_ENFORCED consistency check: FAIL"
                )
        elif platform_status == "PARTIAL_PLATFORM_ENFORCEMENT":
            warnings.append("Platform evidence is PARTIAL_PLATFORM_ENFORCEMENT and needs follow-up review.")
            platform_lines.append("- platform evidence classification: PARTIAL_PLATFORM_ENFORCEMENT")
        elif platform_status == "NEEDS_REVIEW":
            warnings.append("Platform evidence is NEEDS_REVIEW.")
            platform_lines.append("- platform evidence classification: NEEDS_REVIEW")
        elif platform_status == "NOT_ENFORCED":
            failures.append("Platform evidence is NOT_ENFORCED.")
            platform_lines.append("- platform evidence classification: NOT_ENFORCED")
        else:
            warnings.append("Platform evidence final status is unknown or malformed.")
            platform_lines.append("- platform evidence classification: UNKNOWN")

        if platform_text:
            dev_section = section_text(platform_text, "Branch evidence: dev")
            main_section = section_text(platform_text, "Branch evidence: main")
            if dev_section is not None:
                platform_lines.append(
                    f"- dev required check observed field present: {'PASS' if 'Required check observed:' in dev_section else 'FAIL'}"
                )
            else:
                platform_lines.append("- dev required check observed field present: FAIL")
            if main_section is not None:
                platform_lines.append(
                    f"- main required check observed field present: {'PASS' if 'Required check observed:' in main_section else 'FAIL'}"
                )
            else:
                platform_lines.append("- main required check observed field present: FAIL")

    forbidden_lines = []
    forbidden_targets = [
        ENFORCED_REQUIRED_CHECKS_FILE,
        REQUIRED_CHECK_NAMES_FILE,
        BRANCH_PROTECTION_SETUP_FILE,
        PLATFORM_EVIDENCE_TEMPLATE_FILE,
        PLATFORM_EVIDENCE_REPORT_FILE,
        WORKFLOW_FILE,
        ENFORCEMENT_REVIEW_TEMPLATE_FILE,
    ]

    allowance_hits = []
    release_gate_hits = []

    for path in forbidden_targets:
        text = read_text(path)
        if text is None:
            continue
        for lineno, line in non_comment_lines_with_numbers(text):
            if allow_or_enable_match(line):
                allowance_hits.append(f"{path.as_posix()}:{lineno}: {line.strip()}")
            if release_gate_match(line):
                release_gate_hits.append(f"{path.as_posix()}:{lineno}: {line.strip()}")

    if allowance_hits:
        failures.append("Forbidden auto-merge or automatic approval allowance wording found.")

    if release_gate_hits:
        failures.append("M25 enforcement text introduces a deployment or release gate.")

    forbidden_lines.append(
        f"- auto-merge allowance wording: {'FAIL' if allowance_hits else 'PASS'}"
    )
    forbidden_lines.append(
        f"- automatic approval allowance wording: {'FAIL' if allowance_hits else 'PASS'}"
    )
    forbidden_lines.append(
        f"- deployment/release gate as M25 enforcement: {'FAIL' if release_gate_hits else 'PASS'}"
    )

    if workflow_body_error is not None:
        warnings.append(workflow_body_error)
        workflow_safe = False

    result = ENFORCEMENT_READY

    if failures:
        result = NOT_READY
    else:
        if workflow_body_error is not None or platform_report_missing or platform_status in (None, "NEEDS_REVIEW"):
            result = NEEDS_REVIEW
        elif platform_status == "NOT_ENFORCED":
            result = NOT_READY
        elif platform_status == "PARTIAL_PLATFORM_ENFORCEMENT":
            result = READY_WITH_WARNINGS
        elif warnings:
            result = READY_WITH_WARNINGS
        else:
            result = ENFORCEMENT_READY

    if result == ENFORCEMENT_READY and warnings:
        result = READY_WITH_WARNINGS

    if result == NEEDS_REVIEW and not warnings:
        if platform_status == "NEEDS_REVIEW":
            warnings.append("Platform evidence final status is NEEDS_REVIEW.")
        if human_verifier is None or str(human_verifier).strip().upper() in {"", "UNKNOWN"}:
            warnings.append("Human verifier is missing or unknown.")

    print("AgentOS Enforcement Audit")
    print()

    print("Required files:")
    for line in required_file_lines:
        print(line)
    print()

    print("Advisory files:")
    for line in advisory_lines:
        print(line)
    print()

    print("Workflow checks:")
    for line in workflow_check_lines:
        print(line)
    print()

    print("Required check names:")
    for line in required_check_lines:
        print(line)
    print()

    print("Platform evidence:")
    for line in platform_lines:
        print(line)
    print()

    print("Forbidden behavior checks:")
    for line in forbidden_lines:
        print(line)
    print()

    print("Warnings:")
    if warnings:
        for item in warnings:
            print(f"- {item}")
    else:
        print("- none")
    print()

    print("Failures:")
    if failures:
        for item in failures:
            print(f"- {item}")
    else:
        print("- none")
    print()

    print(f"Result: {result}")
    if result == ENFORCEMENT_READY:
        print("Reason: repository enforcement artifacts and platform evidence are complete.")
    elif result == READY_WITH_WARNINGS:
        print("Reason: enforcement artifacts are present, but non-blocking review items remain.")
    elif result == NEEDS_REVIEW:
        print("Reason: platform evidence is ambiguous or incomplete, so enforcement cannot be confirmed safely.")
    else:
        print("Reason: required enforcement evidence is missing or the workflow is not safely enforcing the gate.")

    if result in (ENFORCEMENT_READY, READY_WITH_WARNINGS):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
