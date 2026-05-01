#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass
class CheckResult:
    name: str
    status: str
    reasons: list[str]


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def has_phrase(text: str, phrase: str) -> bool:
    return phrase.lower() in text.lower()


def missing_required_phrases(text: str, phrases: list[str]) -> list[str]:
    out: list[str] = []
    for p in phrases:
        if not has_phrase(text, p):
            out.append(f'required phrase not found: "{p}"')
    return out


def present_forbidden_phrases(text: str, phrases: list[str]) -> list[str]:
    out: list[str] = []
    for p in phrases:
        if has_phrase(text, p):
            out.append(f'forbidden phrase present: "{p}"')
    return out


def check_phrase_group(text: str, group_name: str, options: list[str]) -> list[str]:
    if any(has_phrase(text, o) for o in options):
        return []
    return [
        f"phrase group not satisfied: {group_name}",
        f"  accepted alternatives: {', '.join(options)}",
    ]


def regex_hits(text: str, patterns: list[str]) -> list[str]:
    out: list[str] = []
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE | re.MULTILINE):
            out.append(f"write-risk regex matched: {pat}")
    return out


def list_missing(dir_path: Path, names: list[str]) -> list[str]:
    out: list[str] = []
    for n in names:
        if not (dir_path / n).exists():
            out.append(n)
    return out


def check_1() -> CheckResult:
    name = "Approval evidence model"
    path = REPO_ROOT / "docs" / "HUMAN-APPROVAL-EVIDENCE.md"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    required = [
        "file-based",
        "explicit",
        "not lifecycle mutation",
        "not task completion",
        "does not bypass preconditions",
        "unsupported operation",
        "unsupported target state",
        "vague",
        "inferred",
        "transition has been prepared",
    ]
    forbidden = [
        "approval can be inferred",
        "approval is inferred",
        "automatically approved",
        "auto-approve",
        "approval bypasses preconditions",
        "approval bypasses verification",
    ]

    reasons = []
    reasons.extend(missing_required_phrases(text, required))
    reasons.extend(present_forbidden_phrases(text, forbidden))
    return CheckResult(name, PASS if not reasons else FAIL, reasons)


def check_2() -> CheckResult:
    name = "Approval storage contract"
    path = REPO_ROOT / "docs" / "APPROVAL-EVIDENCE-STORAGE.md"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    required = [
        "approvals/",
        "flat YAML",
        "approval_id",
        "legacy",
        "protected",
        "authorization input",
        "does not bypass preconditions",
        "does not expand",
    ]
    forbidden = [
        "automatically create approval",
        "auto-create approval",
        "create approval record on apply",
        "approval bypasses",
    ]
    group_a = [
        "must not create",
        "must not be created",
        "validators must not create",
        "apply scripts must not create",
        "must not be auto-generated",
    ]
    group_b = [
        "apply scripts must not create",
        "apply-transition.py",
        "lifecycle mutation commands creating approval records",
    ]

    reasons = []
    reasons.extend(missing_required_phrases(text, required))
    reasons.extend(check_phrase_group(text, "approval creation prohibition", group_a))
    reasons.extend(check_phrase_group(text, "apply creation prohibition", group_b))
    reasons.extend(present_forbidden_phrases(text, forbidden))
    return CheckResult(name, PASS if not reasons else FAIL, reasons)


def check_3() -> CheckResult:
    name = "Approval template"
    path = REPO_ROOT / "templates" / "human-approval-record.md"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    fields = [
        "approval_id",
        "approval_status",
        "related_task_id",
        "related_transition_id",
        "approved_by",
        "approved_at",
        "approval_scope",
        "approval_statement",
        "approval_source",
        "allowed_operation",
        "allowed_target_state",
        "expires_at",
        "supersedes",
        "notes",
    ]
    reasons = missing_required_phrases(text, fields)
    if re.search(r"(?m)^approval:\s*$", text) or re.search(r"(?ms)^approval:\s*\n\s+approval_id:", text):
        reasons.append("nested approval YAML detected")
    return CheckResult(name, PASS if not reasons else FAIL, reasons)


def check_4() -> CheckResult:
    name = "Human approval validator"
    path = REPO_ROOT / "scripts" / "validate-human-approval.py"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    required = [
        "PASS",
        "BLOCKED",
        "approval_id",
        "approval_status",
        "related_task_id",
        "related_transition_id",
        "approved_by",
        "approved_at",
        "approval_scope",
        "approval_statement",
        "approval_source",
        "allowed_operation",
        "allowed_target_state",
        "complete-active",
        "completed",
        "vague",
    ]
    reasons = missing_required_phrases(text, required)
    write_risk = [
        r"open\([^)]*approval[^)]*,\s*[\"'][wa+]",
        r"Path\([^)]*approval[^)]*\)\.write_text",
        r"write_approval",
        r"create_approval",
        r"create_approval_record",
        r"os\.remove",
        r"os\.rename",
        r"shutil\.copy",
    ]
    reasons.extend(regex_hits(text, write_risk))
    if reasons:
        return CheckResult(name, FAIL, reasons)

    warn_reasons: list[str] = []
    if not any(has_phrase(text, p) for p in ["agent", "automated-system", "system", "bot"]):
        warn_reasons.append("approved_by blocklist phrases partially confirmable")
    if not any(has_phrase(text, p) for p in ["chat-session", "written-statement", "external-document"]):
        warn_reasons.append("approval_source allowed values partially confirmable")
    if warn_reasons:
        return CheckResult(name, WARN, warn_reasons)
    return CheckResult(name, PASS, [])


def check_5() -> CheckResult:
    name = "Human approval validator fixtures"
    d = REPO_ROOT / "tests" / "fixtures" / "human-approval"
    if not d.is_dir():
        return CheckResult(name, FAIL, [f"missing: {d.relative_to(REPO_ROOT)}"])

    core = [
        "valid-complete-active.md",
        "invalid-vague-approval.md",
        "invalid-missing-required-field.md",
        "invalid-unsupported-operation.md",
        "invalid-unsupported-target-state.md",
        "invalid-nested-yaml.md",
        "invalid-expired-status.md",
    ]
    missing_core = list_missing(d, core)
    if missing_core:
        return CheckResult(name, FAIL, ["missing core fixtures: " + ", ".join(missing_core)])

    expanded = [
        "invalid-approved-by-agent.md",
        "invalid-approved-by-openai-exact.md",
        "valid-approved-by-openai-substring.md",
        "invalid-generic-scope-all.md",
        "invalid-bypass-preconditions.md",
        "invalid-approval-id-task-mismatch.md",
        "invalid-approval-id-operation-mismatch.md",
        "invalid-related-task-id-format.md",
        "invalid-related-transition-id-format.md",
        "invalid-approved-at-format.md",
        "invalid-expires-at-format.md",
        "invalid-superseded-status.md",
        "invalid-revoked-status.md",
        "invalid-approval-status-invalid.md",
        "invalid-unknown-status.md",
        "invalid-unknown-approval-source.md",
        "invalid-supersedes-format.md",
    ]
    present = len(expanded) - len(list_missing(d, expanded))
    if present == 17:
        return CheckResult(name, PASS, [])
    missing = list_missing(d, expanded)
    if 14 <= present <= 16:
        return CheckResult(
            name,
            WARN,
            [
                f"{present} of 17 expanded fixtures present (threshold: 17 for PASS, 14 for WARN)",
                "missing: " + ", ".join(missing),
            ],
        )
    return CheckResult(
        name,
        FAIL,
        [
            f"{present} of 17 expanded fixtures present (threshold: 17 for PASS, 14 for WARN)",
            "missing: " + ", ".join(missing),
        ],
    )


def check_6() -> CheckResult:
    name = "Human approval fixture runner"
    path = REPO_ROOT / "scripts" / "test-human-approval-fixtures.py"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    required = [
        "CASES",
        "PASS",
        "BLOCKED",
        "valid-approved-by-openai-substring",
        "invalid-bypass-preconditions",
        "invalid-approval-id-task-mismatch",
        "invalid-approval-id-operation-mismatch",
    ]
    reasons = missing_required_phrases(text, required)
    if reasons:
        return CheckResult(name, FAIL, reasons)

    optional = ["reason", "expected_result", "expected_reason"]
    warn = [f'optional phrase not found: "{p}"' for p in optional if not has_phrase(text, p)]
    if warn:
        return CheckResult(name, WARN, warn)
    return CheckResult(name, PASS, [])


def check_7() -> CheckResult:
    name = "Approval-aware apply preconditions"
    dpath = REPO_ROOT / "docs" / "APPLY-PRECONDITIONS.md"
    spath = REPO_ROOT / "scripts" / "check-apply-preconditions.py"
    dtext = read_text(dpath)
    stext = read_text(spath)
    if dtext is None:
        return CheckResult(name, FAIL, [f"missing: {dpath.relative_to(REPO_ROOT)}"])
    if stext is None:
        return CheckResult(name, FAIL, [f"missing: {spath.relative_to(REPO_ROOT)}"])

    req_docs = [
        "approval_required",
        "--approval",
        "validate-human-approval",
        "does not bypass",
        "missing approval",
        "invalid approval",
        "never inferred",
        "never created",
    ]
    req_script = [
        "--approval",
        "approval_required",
        "validate-human-approval",
        "approval is required but no approval record",
        "approval validation failed",
    ]

    reasons = []
    reasons.extend(missing_required_phrases(dtext, req_docs))
    reasons.extend(missing_required_phrases(stext, req_script))
    write_risk = [
        r"open\([^)]*approval[^)]*,\s*[\"'][wa+]",
        r"Path\([^)]*approval[^)]*\)\.write_text",
        r"write_approval",
        r"create_approval",
        r"create_approval_record",
        r"os\.remove",
        r"os\.rename",
        r"shutil\.copy",
    ]
    reasons.extend(regex_hits(stext, write_risk))

    return CheckResult(name, PASS if not reasons else FAIL, reasons)


def check_8() -> CheckResult:
    name = "Controlled apply approval gate"
    path = REPO_ROOT / "scripts" / "apply-transition.py"
    text = read_text(path)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {path.relative_to(REPO_ROOT)}"])

    required = [
        "--approval",
        "approval_required",
        "validate-human-approval",
        "approval is required but no approval record",
        "approval validation failed",
        "complete-active",
    ]
    reasons = missing_required_phrases(text, required)

    write_risk = [
        r"open\([^)]*approval[^)]*,\s*[\"'][wa+]",
        r"Path\([^)]*approval[^)]*\)\.write_text",
        r"write_approval_record",
        r"create_approval",
        r"create_approval_record",
        r"os\.remove",
        r"os\.rename",
        r"shutil\.copy",
    ]
    reasons.extend(regex_hits(text, write_risk))

    if reasons:
        return CheckResult(name, FAIL, reasons)

    scope_phrases = ["--complete-active", "complete-active mode", "controlled complete-active"]
    if not any(has_phrase(text, p) for p in scope_phrases):
        return CheckResult(name, WARN, ["scope isolation phrase not found"]) 

    return CheckResult(name, PASS, [])


def check_9() -> CheckResult:
    name = "Approval enforcement fixtures"
    runner = REPO_ROOT / "scripts" / "test-approval-fixtures.py"
    d = REPO_ROOT / "tests" / "fixtures" / "approval-enforcement"
    if not runner.is_file():
        return CheckResult(name, FAIL, [f"missing: {runner.relative_to(REPO_ROOT)}"])
    if not d.is_dir():
        return CheckResult(name, FAIL, [f"missing: {d.relative_to(REPO_ROOT)}"])

    required_files = [
        "approval-required-transition.md",
        "approval-not-required-transition.md",
        "approval-required-mutation-plan.md",
        "valid-approval.md",
        "invalid-vague-approval.md",
        "task-mismatch-approval.md",
        "transition-mismatch-approval.md",
        "unsupported-operation-approval.md",
        "unsupported-target-state-approval.md",
    ]
    missing = list_missing(d, required_files)
    if missing:
        return CheckResult(name, FAIL, ["missing fixtures: " + ", ".join(missing)])

    text = read_text(runner)
    if text is None:
        return CheckResult(name, FAIL, [f"missing: {runner.relative_to(REPO_ROOT)}"])

    required = [
        "tempfile",
        "CASES",
        "Case 1",
        "Case 2",
        "Case 3",
        "Case 4",
        "Case 5",
        "Case 6",
        "Case 7",
        "Case 8",
        "Case 9",
        "PASS",
        "BLOCKED",
        "approvals/",
    ]
    reasons = missing_required_phrases(text, required)
    for p in ["tempfile", "temp"]:
        if not has_phrase(text, p):
            reasons.append(f'temp workspace safety phrase missing: "{p}"')
    for p in ["approvals/", "hash"]:
        if not has_phrase(text, p):
            reasons.append(f'protected path guard phrase missing: "{p}"')
    if reasons:
        return CheckResult(name, FAIL, reasons)

    optional = ["sys.executable", "hashlib", "before_state", "after_state"]
    warn = [f'optional phrase not found: "{p}"' for p in optional if not has_phrase(text, p)]
    if warn:
        return CheckResult(name, WARN, warn)
    return CheckResult(name, PASS, [])


def check_10(previous_checks_ok: bool) -> CheckResult:
    name = "Safety boundaries"
    files = [
        REPO_ROOT / "docs" / "HUMAN-APPROVAL-EVIDENCE.md",
        REPO_ROOT / "docs" / "APPROVAL-EVIDENCE-STORAGE.md",
        REPO_ROOT / "docs" / "APPLY-PRECONDITIONS.md",
    ]
    texts: dict[Path, str] = {}
    missing: list[str] = []
    for p in files:
        t = read_text(p)
        if t is None:
            missing.append(str(p.relative_to(REPO_ROOT)))
        else:
            texts[p] = t

    if missing and not previous_checks_ok:
        return CheckResult(name, WARN, ["dependency missing from earlier checks; skipped strict safety phrase scan"])

    if missing:
        return CheckResult(name, WARN, ["missing docs: " + ", ".join(missing)])

    forbidden = [
        "approval can be inferred",
        "approval is inferred from",
        "automatically approved",
        "auto-approve",
        "approval bypasses preconditions",
        "approval bypasses verification",
        "approval bypasses readiness",
        "approval bypasses mutation plan",
        "approval permits autonomous apply",
        "approval permits hidden completion",
        "approval expands supported operations",
        "approval authorizes unsupported",
    ]

    reasons: list[str] = []
    for path, text in texts.items():
        for p in forbidden:
            if has_phrase(text, p):
                reasons.append(f"{path.relative_to(REPO_ROOT)} contains forbidden phrase: {p}")

    model = texts[REPO_ROOT / "docs" / "HUMAN-APPROVAL-EVIDENCE.md"]
    for p in ["explicit", "file-based", "does not bypass"]:
        if not has_phrase(model, p):
            reasons.append(f"required safety phrase missing in HUMAN-APPROVAL-EVIDENCE.md: {p}")

    return CheckResult(name, PASS if not reasons else FAIL, reasons)


def main() -> int:
    checks = [
        check_1,
        check_2,
        check_3,
        check_4,
        check_5,
        check_6,
        check_7,
        check_8,
        check_9,
    ]

    results: list[CheckResult] = [c() for c in checks]
    previous_ok = all(r.status != FAIL for r in results)
    results.append(check_10(previous_ok))

    print("Approval Boundary Audit")
    any_fail = False
    any_warn = False
    for r in results:
        print(f"{r.name}: {r.status}")
        for reason in r.reasons:
            print(f"- {reason}")
        if r.status == FAIL:
            any_fail = True
        if r.status == WARN:
            any_warn = True

    if any_fail:
        print("Result: FAIL")
        print("Exit code: 1 (PASS or WARN = 0, FAIL = 1)")
        return 1
    if any_warn:
        print("Result: WARN")
        print("Exit code: 0 (PASS or WARN = 0, FAIL = 1)")
        return 0
    print("Result: PASS")
    print("Exit code: 0 (PASS or WARN = 0, FAIL = 1)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
