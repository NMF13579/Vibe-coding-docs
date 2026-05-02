#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

FINAL_PASS = "PASS"
FINAL_WARN = "WARN"
FINAL_FAIL = "FAIL"
FINAL_ERROR = "ERROR"

CHECK_PASS = "PASS"
CHECK_WARN = "WARN"
CHECK_FAIL = "FAIL"
CHECK_NOT_RUN = "NOT_RUN"
CHECK_NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
CHECK_ERROR = "ERROR"

BOUNDARY_1 = "Audit PASS does not mean AgentOS is MVP-ready."
BOUNDARY_2 = "M21 template packaging audit does not override M19/M20 safety gates."


class Check:
    def __init__(self, name: str, status: str, reason: str):
        self.name = name
        self.status = status
        self.reason = reason

    def to_json(self):
        return {"name": self.name, "status": self.status, "reason": self.reason}


def run_cmd(cmd):
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return proc.returncode, proc.stdout
    except Exception as exc:
        return None, f"exception: {exc.__class__.__name__}: {exc}"


def check_file(path: Path, name: str):
    if path.is_file():
        return Check(name, CHECK_PASS, "file exists")
    return Check(name, CHECK_FAIL, f"missing file: {path}")


def forbidden_phrase_checks(root: Path):
    phrases = [
        "AgentOS is autonomous",
        "guarantees bug-free",
        "template integrity means MVP readiness",
        "template integrity pass means",
        "example project means MVP readiness",
        "example project pass means",
        "quickstart means MVP readiness",
        "quickstart pass means",
        "usage means MVP readiness",
        "usage pass means",
        "MVP_READY",
    ]
    targets = [
        root / "templates/agentos-minimal",
        root / "templates/agentos-full",
        root / "examples/simple-project",
        root / "docs/quickstart.md",
        root / "docs/usage.md",
    ]
    for phrase in phrases:
        for target in targets:
            if target.is_dir():
                for p in target.rglob("*"):
                    if p.is_file():
                        try:
                            text = p.read_text(encoding="utf-8", errors="ignore")
                        except Exception:
                            continue
                        if phrase.lower() in text.lower():
                            return Check("forbidden_phrases", CHECK_FAIL, f'found "{phrase}" in {p}')
            elif target.is_file():
                text = target.read_text(encoding="utf-8", errors="ignore")
                if phrase.lower() in text.lower():
                    return Check("forbidden_phrases", CHECK_FAIL, f'found "{phrase}" in {target}')
    return Check("forbidden_phrases", CHECK_PASS, "no forbidden phrases found")


def boundary_text_check(path: Path, name: str, required_substrings):
    if not path.is_file():
        return Check(name, CHECK_FAIL, f"missing file: {path}")
    text = path.read_text(encoding="utf-8", errors="ignore")
    for needle in required_substrings:
        if needle not in text:
            return Check(name, CHECK_FAIL, f"missing boundary substring: {needle}")
    return Check(name, CHECK_PASS, "all required boundaries found")


def compute_result(checks, strict: bool):
    statuses = [c.status for c in checks]
    if any(s == CHECK_ERROR for s in statuses):
        return FINAL_ERROR
    if any(s == CHECK_FAIL for s in statuses):
        return FINAL_FAIL
    if strict and any(s in (CHECK_WARN, CHECK_NOT_RUN, CHECK_NOT_IMPLEMENTED) for s in statuses):
        return FINAL_FAIL
    if any(s in (CHECK_WARN, CHECK_NOT_RUN, CHECK_NOT_IMPLEMENTED) for s in statuses):
        return FINAL_WARN
    return FINAL_PASS


def build_checks(root: Path):
    checks = []

    # Template presence
    required_template_files = [
        "templates/agentos-minimal/README.md",
        "templates/agentos-minimal/requirements.txt",
        "templates/agentos-minimal/scripts/run-all.sh",
        "templates/agentos-minimal/templates/task.md",
        "templates/agentos-minimal/templates/verification.md",
        "templates/agentos-full/README.md",
        "templates/agentos-full/requirements.txt",
        "templates/agentos-full/scripts/run-all.sh",
        "templates/agentos-full/templates/task.md",
        "templates/agentos-full/templates/verification.md",
        "templates/agentos-full/docs/architecture.md",
        "templates/agentos-full/docs/guardrails.md",
        "templates/agentos-full/docs/limitations.md",
        "templates/agentos-full/docs/troubleshooting.md",
        "templates/agentos-full/examples/README.md",
    ]
    for rel in required_template_files:
        checks.append(check_file(root / rel, f"template_presence:{rel}"))

    # Template integrity
    integrity_script = root / "scripts/check-template-integrity.py"
    if not integrity_script.is_file():
        checks.append(Check("template_integrity", CHECK_FAIL, "missing scripts/check-template-integrity.py"))
        checks.append(Check("template_integrity_strict", CHECK_FAIL, "missing scripts/check-template-integrity.py"))
    else:
        rc, out = run_cmd(["python3", str(integrity_script)])
        if rc is None:
            checks.append(Check("template_integrity", CHECK_ERROR, out.strip()))
        elif rc == 0 and "TEMPLATE_INTEGRITY_RESULT: PASS" in out:
            checks.append(Check("template_integrity", CHECK_PASS, "check-template-integrity PASS"))
        elif rc == 0:
            checks.append(Check("template_integrity", CHECK_WARN, "command succeeded without PASS marker"))
        else:
            checks.append(Check("template_integrity", CHECK_FAIL, "check-template-integrity failed"))

        rc, out = run_cmd(["python3", str(integrity_script), "--strict"])
        if rc is None:
            checks.append(Check("template_integrity_strict", CHECK_ERROR, out.strip()))
        elif rc == 0 and "TEMPLATE_INTEGRITY_RESULT: PASS" in out:
            checks.append(Check("template_integrity_strict", CHECK_PASS, "check-template-integrity --strict PASS"))
        elif rc == 0:
            checks.append(Check("template_integrity_strict", CHECK_WARN, "strict command succeeded without PASS marker"))
        else:
            checks.append(Check("template_integrity_strict", CHECK_FAIL, "check-template-integrity --strict failed"))

    # Install smoke
    install_smoke = root / "scripts/test-install.sh"
    if not install_smoke.is_file():
        checks.append(Check("install_smoke", CHECK_FAIL, "missing scripts/test-install.sh"))
    else:
        rc, out = run_cmd(["bash", str(install_smoke)])
        if rc is None:
            checks.append(Check("install_smoke", CHECK_ERROR, out.strip()))
        elif rc == 0 and "PASS: install smoke test passed" in out:
            checks.append(Check("install_smoke", CHECK_PASS, "install smoke passed"))
        elif rc == 0:
            checks.append(Check("install_smoke", CHECK_WARN, "command succeeded without expected PASS marker"))
        else:
            checks.append(Check("install_smoke", CHECK_FAIL, "install smoke failed"))

    # Example presence
    required_example_files = [
        "examples/simple-project/README.md",
        "examples/simple-project/run-example.sh",
    ]
    for rel in required_example_files:
        checks.append(check_file(root / rel, f"example_presence:{rel}"))

    # Example smoke
    example_smoke = root / "scripts/test-example-project.sh"
    if not example_smoke.is_file():
        checks.append(Check("example_smoke", CHECK_FAIL, "missing scripts/test-example-project.sh"))
    else:
        rc, out = run_cmd(["bash", str(example_smoke)])
        if rc is None:
            checks.append(Check("example_smoke", CHECK_ERROR, out.strip()))
        elif rc == 0 and "PASS: example project validation passed" in out:
            checks.append(Check("example_smoke", CHECK_PASS, "example project smoke passed"))
        elif rc == 0:
            checks.append(Check("example_smoke", CHECK_WARN, "command succeeded without expected PASS marker"))
        else:
            checks.append(Check("example_smoke", CHECK_FAIL, "example project smoke failed"))

    # Docs presence
    checks.append(check_file(root / "docs/quickstart.md", "docs_presence:docs/quickstart.md"))
    checks.append(check_file(root / "docs/usage.md", "docs_presence:docs/usage.md"))

    # Boundary checks
    checks.append(
        boundary_text_check(
            root / "docs/quickstart.md",
            "quickstart_boundaries",
            [
                "does not mean AgentOS is MVP-ready",
            ],
        )
    )
    checks.append(
        boundary_text_check(
            root / "docs/usage.md",
            "usage_boundaries",
            [
                "does not mean AgentOS is MVP-ready",
            ],
        )
    )

    checks.append(forbidden_phrase_checks(root))

    return checks


def main():
    parser = argparse.ArgumentParser(description="Read-only M21 template packaging audit")
    parser.add_argument("--json", action="store_true", dest="json_mode", help="JSON output")
    parser.add_argument("--strict", action="store_true", help="Strict mode")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    checks = build_checks(root)
    result = compute_result(checks, args.strict)

    payload = {
        "result": result,
        "strict": bool(args.strict),
        "checks": [c.to_json() for c in checks],
        "boundaries": [BOUNDARY_1, BOUNDARY_2],
    }

    if args.json_mode:
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print("TEMPLATE_PACKAGING_AUDIT_START")
        for c in checks:
            print(f"TEMPLATE_PACKAGING_AUDIT_CHECK: {c.name} {c.status} {c.reason}")
        print(f"TEMPLATE_PACKAGING_AUDIT_RESULT: {result}")
        print(f"TEMPLATE_PACKAGING_AUDIT_BOUNDARY: {BOUNDARY_1}")
        print(f"TEMPLATE_PACKAGING_AUDIT_BOUNDARY: {BOUNDARY_2}")

    return 0 if result in (FINAL_PASS, FINAL_WARN) and not args.strict or result == FINAL_PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
