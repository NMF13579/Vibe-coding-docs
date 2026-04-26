# Scenario 04 — Validation Only

## Situation

A user wants to verify the repository health without starting or executing any task.

## User Input

Check whether this AgentOS template is structurally sound and release-ready.

## AgentOS Flow

No /spec is required.

## Expected Artifacts

- `reports/audit-smoke.md`

## Human Approval Points

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
