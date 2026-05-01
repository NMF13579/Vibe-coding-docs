# Approval Flow Smoke Fixtures

Purpose:
- Synthetic fixture set for approval-gate smoke checks in temp workspace.
- Verifies valid approval path and missing-approval negative path via existing scripts.

Synthetic IDs:
- `task-fixture-approval-smoke`
- `transition-fixture-approval-smoke`
- `approval-20260430-task-fixture-approval-smoke-complete-active`

Temp workspace layout used by smoke runner:
- `tasks/`
- `reports/`
- `transitions/`
- `approvals/`
- `plans/`

Intended subprocesses:
- `scripts/validate-human-approval.py`
- `scripts/check-apply-preconditions.py`
- `scripts/apply-transition.py`

Known limitation:
- Complete-active may still stop on non-approval checks depending on current apply requirements.
