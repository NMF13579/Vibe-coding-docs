#!/usr/bin/env python3
import fnmatch
import sys
from pathlib import Path

import yaml


def load_frontmatter(path_text):
    path = Path(path_text)
    if not path.exists():
        print("FAIL: risk check failed")
        print(f"missing file: {path_text}")
        return None

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print("FAIL: risk check failed")
        print("invalid frontmatter")
        return None

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        print("FAIL: risk check failed")
        print("invalid frontmatter")
        return None

    closing_index = -1
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index == -1:
        print("FAIL: risk check failed")
        print("invalid frontmatter")
        return None

    frontmatter = "\n".join(lines[1:closing_index])
    return yaml.safe_load(frontmatter)


def load_policy(path_text):
    path = Path(path_text)
    if not path.exists():
        print("FAIL: risk check failed")
        print(f"missing file: {path_text}")
        return None

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        print("FAIL: risk check failed")
        print("violation: invalid risk policy structure")
        return None

    risk_policy = data.get("risk_policy")
    if not isinstance(risk_policy, dict):
        print("FAIL: risk check failed")
        print("violation: invalid risk policy structure")
        return None

    high_risk_paths = risk_policy.get("high_risk_paths")
    critical_markers = risk_policy.get("critical_command_markers")
    if not isinstance(high_risk_paths, list) or not isinstance(critical_markers, list):
        print("FAIL: risk check failed")
        print("violation: invalid risk policy structure")
        return None

    return risk_policy


def matches_path_pattern(item, pattern):
    if pattern.endswith("/"):
        if item.startswith(pattern) or item == pattern.rstrip("/"):
            return True
        return fnmatch.fnmatch(item, pattern + "*")
    return fnmatch.fnmatch(item, pattern)


def has_real_text(value):
    return isinstance(value, str) and value.strip() != "" and value.strip() != "TODO"


def main():
    task_path = sys.argv[1] if len(sys.argv) > 1 else "tasks/active-task.md"
    policy_path = "policies/risk-policy.yml"

    task_data = load_frontmatter(task_path)
    if task_data is None:
        return 1

    risk_policy = load_policy(policy_path)
    if risk_policy is None:
        return 1

    task = task_data.get("task")
    violations = []

    if not isinstance(task, dict):
        print("FAIL: risk check failed")
        print("violation: invalid frontmatter")
        return 1

    files_or_areas = task.get("files_or_areas", [])
    in_scope = task.get("in_scope", [])
    risk_level = task.get("risk_level", "")
    requires_owner_approval = task.get("requires_owner_approval", False)
    owner_approval_proof = task.get("owner_approval_proof", "")
    rollback_plan = task.get("rollback_plan", "")
    risk_reason = task.get("risk_reason", "")

    for item in list(files_or_areas) + list(in_scope):
        if not isinstance(item, str):
            continue
        for pattern in risk_policy["high_risk_paths"]:
            if matches_path_pattern(item, pattern) and risk_level not in ("HIGH", "CRITICAL"):
                violations.append(f"high-risk path requires HIGH or CRITICAL risk_level: {item} matched {pattern}")

    text_fields = []
    for key in ("goal", "expected_result", "risk_reason", "rollback_plan"):
        value = task.get(key, "")
        if isinstance(value, str):
            text_fields.append(value)

    for key in ("acceptance_criteria", "verification_plan"):
        values = task.get(key, [])
        if isinstance(values, list):
            for value in values:
                if isinstance(value, str):
                    text_fields.append(value)

    for marker in risk_policy["critical_command_markers"]:
        marker_found = False
        for value in text_fields:
            if marker.lower() in value.lower():
                marker_found = True
                break
        if marker_found and risk_level != "CRITICAL":
            violations.append(f"critical command marker requires CRITICAL risk_level: {marker}")

    if risk_level in ("HIGH", "CRITICAL") and requires_owner_approval is not True:
        violations.append("HIGH/CRITICAL risk requires requires_owner_approval: true")

    if risk_level in ("HIGH", "CRITICAL") and not has_real_text(rollback_plan):
        violations.append("HIGH/CRITICAL risk requires rollback_plan not empty and not TODO")

    if requires_owner_approval is True and not has_real_text(owner_approval_proof):
        violations.append("requires_owner_approval true requires owner_approval_proof not empty and not TODO")

    if risk_level in ("MEDIUM", "HIGH", "CRITICAL") and not has_real_text(risk_reason):
        violations.append("MEDIUM/HIGH/CRITICAL risk requires risk_reason not empty and not TODO")

    if violations:
        print("FAIL: risk check failed")
        for violation in violations:
            print(f"violation: {violation}")
        return 1

    print("PASS: risk check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
