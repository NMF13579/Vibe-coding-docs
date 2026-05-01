#!/usr/bin/env python3
import pathlib
import sys

import yaml

TASK_PATH = pathlib.Path("tasks/active-task.md")
VERIFICATION_PATH = pathlib.Path("reports/verification.md")
VALID_RISK_LEVELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
VALID_GATE_STATUSES = {"PASS", "FAIL", "SKIPPED", "TODO"}


def load_frontmatter(path):
    if not path.exists():
        print("FAIL: PR quality check failed")
        print(f"missing file: {path.as_posix()}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print("FAIL: PR quality check failed")
        print(f"invalid frontmatter: {path.as_posix()}")
        sys.exit(1)

    lines = text.splitlines()
    try:
        closing_index = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        print("FAIL: PR quality check failed")
        print(f"invalid frontmatter: {path.as_posix()}")
        sys.exit(1)

    for line in lines[closing_index + 1 :]:
        if line.strip() == "---":
            print("FAIL: PR quality check failed")
            print(f"invalid frontmatter: {path.as_posix()}")
            sys.exit(1)

    data = yaml.safe_load("\n".join(lines[1:closing_index]))
    if not isinstance(data, dict):
        print("FAIL: PR quality check failed")
        print(f"invalid frontmatter: {path.as_posix()}")
        sys.exit(1)
    return data


def non_empty_string(value):
    return isinstance(value, str) and value.strip() != ""


def main():
    task_data = load_frontmatter(TASK_PATH)
    verification_data = load_frontmatter(VERIFICATION_PATH)
    violations = []

    if "task" not in task_data:
        violations.append("missing task root")
        task = {}
    else:
        task = task_data.get("task")
        if not isinstance(task, dict):
            task = {}

    if "verification" not in verification_data:
        violations.append("missing verification root")
        verification = {}
    else:
        verification = verification_data.get("verification")
        if not isinstance(verification, dict):
            verification = {}

    task_id = task.get("id")
    if not non_empty_string(task_id):
        violations.append("missing task.id")
    elif not task_id.startswith("task-"):
        violations.append("task.id must start with task-")

    verification_task_id = verification.get("task_id")
    if not non_empty_string(verification_task_id):
        violations.append("missing verification.task_id")
    elif non_empty_string(task_id) and verification_task_id != task_id:
        violations.append("verification.task_id does not match task.id")

    acceptance_criteria = task.get("acceptance_criteria")
    if not isinstance(acceptance_criteria, list):
        violations.append("task.acceptance_criteria must be a non-empty list")
    elif len(acceptance_criteria) == 0:
        violations.append("task.acceptance_criteria must not be empty")

    verification_plan = task.get("verification_plan")
    if not isinstance(verification_plan, list):
        violations.append("task.verification_plan must be a non-empty list")
    elif len(verification_plan) == 0:
        violations.append("task.verification_plan must not be empty")

    risk_level = task.get("risk_level")
    if not non_empty_string(risk_level):
        violations.append("missing task.risk_level")
    elif risk_level not in VALID_RISK_LEVELS:
        violations.append("invalid task.risk_level")

    if risk_level in {"HIGH", "CRITICAL"}:
        if task.get("requires_owner_approval") is not True:
            violations.append("HIGH/CRITICAL risk requires owner approval")
        owner_approval_proof = task.get("owner_approval_proof")
        if not non_empty_string(owner_approval_proof) or owner_approval_proof == "TODO":
            violations.append("HIGH/CRITICAL risk requires owner_approval_proof")

    for gate_name in ["gate_1", "gate_2", "gate_3", "gate_4", "gate_5"]:
        gate = verification.get(gate_name)
        if not isinstance(gate, dict):
            violations.append(f"missing verification.{gate_name}")
            continue

        status = gate.get("status")
        if not non_empty_string(status):
            violations.append(f"missing verification.{gate_name}.status")
            continue
        if status not in VALID_GATE_STATUSES:
            violations.append(f"invalid verification.{gate_name}.status")
            continue

        if status in {"PASS", "FAIL"}:
            proof = gate.get("proof")
            if not non_empty_string(proof) or proof == "TODO":
                violations.append(f"verification.{gate_name}.proof required for PASS/FAIL")

        if status == "SKIPPED":
            skipped_reason = gate.get("skipped_reason")
            if not non_empty_string(skipped_reason) or skipped_reason == "TODO":
                violations.append(f"verification.{gate_name}.skipped_reason required for SKIPPED")

    if violations:
        print("FAIL: PR quality check failed")
        for violation in violations:
            print(f"violation: {violation}")
        return 1

    print("PASS: PR quality check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
