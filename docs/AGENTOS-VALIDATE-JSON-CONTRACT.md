---
type: canonical
module: m24
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# AgentOS Validate JSON Contract

## 1. Purpose
- JSON output is the machine-readable evidence format for AgentOS validation.
- JSON output supports CI, audit, and human review.
- JSON output is evidence, not approval.

## 2. Core Principle
JSON output is automation evidence, not approval.

## 3. Supported Commands
- `python scripts/agentos-validate.py scope --task tasks/active-task.md --json`
- `python scripts/agentos-validate.py execution-audit --json`
- `python scripts/agentos-validate.py all --json`

## 4. Top-Level JSON Contract
```json
{
  "result": "PASS",
  "commands_run": 0,
  "commands_passed": 0,
  "commands_failed": 0,
  "commands_warned": 0,
  "commands_not_run": 0,
  "human_action_required": false,
  "checks": []
}
```

## 5. Top-Level Field Meanings
- `result` = overall result
- `commands_run` = number of checks actually executed
- `commands_passed` = number of checks with PASS
- `commands_failed` = number of checks with FAIL or ERROR
- `commands_warned` = number of checks with WARN
- `commands_not_run` = number of checks skipped or not executed because prerequisites were missing
- `human_action_required` = true when human review is required
- `checks` = list of individual validation check results

## 6. Allowed Result Values
- PASS
- WARN
- FAIL
- ERROR
- NOT_RUN

## 7. Result Semantics
- PASS means validation completed successfully.
- WARN means validation completed with warnings.
- FAIL means one or more checks failed.
- ERROR means validation could not complete correctly.
- NOT_RUN means a required or expected check did not run.
- NOT_RUN is not PASS.
- ERROR requires human review.
- FAIL requires human review.

## 8. Check Object Contract
Each object inside `checks` must include only:
- `name`
- `command`
- `exit_code`
- `result`
- `output_summary`
- `human_action_required`

## 9. Check Field Meanings
- `name` = stable check name
- `command` = command executed or intended command
- `exit_code` = process exit code or 3 for NOT_RUN / ERROR where applicable
- `result` = PASS / WARN / FAIL / ERROR / NOT_RUN
- `output_summary` = last 500 characters of combined stdout and stderr
- `human_action_required` = true or false for this check

## 10. Counter Rules
- NOT_RUN must not be counted in commands_run.
- NOT_RUN must be counted in commands_not_run.
- ERROR must be counted in commands_failed.
- FAIL must be counted in commands_failed.
- WARN must be counted in commands_warned.
- PASS must be counted in commands_passed.
- commands_run must equal PASS + WARN + FAIL + ERROR checks.
- commands_not_run must equal NOT_RUN checks.

## 11. Exit Code Mapping
- PASS exits with 0.
- FAIL exits with 1.
- WARN exits with 2.
- ERROR exits with 3.
- NOT_RUN exits with 3.

## 12. JSON Output Rules
- JSON mode must output valid JSON only.
- JSON mode must not mix human-readable text with JSON.
- Child stdout and stderr must be captured, not streamed directly.
- Child output must be summarized inside output_summary.
- No extra top-level fields are allowed unless this contract is updated.

## 13. Human Review Rules
- JSON output does not approve work.
- PASS does not prove implementation correctness.
- WARN / FAIL / ERROR / NOT_RUN require review according to policy.
- Human reviewer remains responsible for acceptance.

## 14. Advisory Boundary
- M24 documents JSON evidence.
- M24 does not enforce required checks.
- M24 does not enforce protected branches.
- M24 does not block merges.
- M24 does not approve changes.
- M25 may use this JSON contract for enforced CI.
