# Scenario 04 — Validation Only

## Situation

A user wants to verify the repository health without starting or executing any task.

## User Input

Check whether this AgentOS template is structurally sound and release-ready.

## AgentOS Flow

1. No `/spec` is required.
2. No task contract is required.
3. Run validation commands only.
4. Review reports and failures.
5. Create follow-up tasks only if needed.

## Expected Artifacts

- `reports/task-health.md` if task-health is run separately
- `reports/negative-fixtures-smoke.md`
- `reports/guard-failures-smoke.md`
- `reports/audit.md`
- `reports/audit-smoke.md`

## Human Approval Points

- approval before creating follow-up implementation tasks
- approval before modifying `tasks/active-task.md`
- approval before treating an audit result as a release decision

## Validation Commands

- `python3 scripts/check-template-integrity.py --strict`
- `python3 scripts/test-template-integrity.py`
- `python3 scripts/test-negative-fixtures.py`
- `python3 scripts/test-guard-failures.py`
- `python3 scripts/audit-agentos.py`

## What Must Not Happen Automatically

- no task execution
- no task contract generation unless explicitly requested
- no queue movement
- no runner protocol execution
- no release approval

## Notes

This scenario is the read-only path: inspect health, read the reports, and stop before any execution starts.
