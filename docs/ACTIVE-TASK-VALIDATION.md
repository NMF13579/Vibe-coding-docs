# Active Task Validation (Milestone 12.1.1)

## Purpose

This document defines Active Task Integrity validation rules for Milestone 12.
It describes how to validate `tasks/active-task.md` as an activation pointer.

Validator scope in this stage:
- `validate-active-task.py` (future) validates active-task integrity only.
- It does not validate execution readiness.

## Layer Separation

Milestone 12 uses two different layers:

1. Layer 1: Active Task Integrity
2. Layer 2: Execution Readiness

This document defines only Layer 1.

Required separation:
- `validate-active-task.py` = checks that `active-task.md` is a correct activation pointer.
- `check-execution-readiness.py` = checks whether execution may start.

`check-execution-readiness.py` is out of scope for 12.1.1.

## What active-task.md Is

`tasks/active-task.md` is:
- current active task pointer
- activation traceability record
- controlled-write output

`tasks/active-task.md` is not:
- proof of completion
- approval marker
- verification report
- execution log
- task contract replacement
- source of approval
- queue state mutation
- execution command

## Expected Minimum Format

```yaml
---
task_id: task-001
state: active
activated_at: 2026-04-28T10:00:00Z
activated_by: human-approved-command
approval_id: approval-task-001-execution
source_task: tasks/task-001
source_contract: tasks/drafts/task-001-contract-draft.md
transition: approved_for_execution:active
---
```

## Required Fields

Validator must require all fields:
- `task_id`
- `state`
- `activated_at`
- `activated_by`
- `approval_id`
- `source_task`
- `source_contract`
- `transition`

## Required Values

- `state` must equal `active`.
- `transition` must equal `approved_for_execution:active`.

### activated_by allowlist (v1)

Allowed values:
- `human-approved-command`

Extension rule:
- future milestones may add new values only by explicit update of this spec
- validator must FAIL on unknown `activated_by`
- validator must not silently ignore unknown values

## activated_at Validation

`activated_at` must be machine-parseable date-time.

Recommended shape:
- `YYYY-MM-DDTHH:MM:SSZ`

Valid example:
- `2026-04-28T10:00:00Z`

Invalid examples:
- `today`
- `yesterday`
- `28-04-2026`
- `not-a-date`

M12 v1 note:
- no complex timezone logic is required
- goal is automatic parseability, not free-text date

## Source Path Rules

Validator must check for both:
- `source_task` exists
- `source_contract` exists

Path requirements:
- repository-relative paths only
- absolute paths are forbidden
- parent traversal is forbidden

Forbidden examples:
- `/etc/passwd`
- `/home/user/file.md`
- `../../somewhere/task.md`

Approval marker resolver note:
- `approval_id` SHOULD be resolvable by existing approval marker conventions
- resolver is outside M12.1 scope
- validator is not required to implement approval marker resolver in this milestone

## Consistency Checks

Required checks:
- `active.state == "active"`
- `active.transition == "approved_for_execution:active"`
- `source_task` exists
- `source_contract` exists
- `source_task` path is repository-relative
- `source_contract` path is repository-relative
- `source_task` path has no parent traversal
- `source_contract` path has no parent traversal
- `active.task_id == source_task.task_id`
- `active.task_id == source_contract.task_id`

If task_id cannot be reliably extracted from source files:
- validator must return `FAIL` or `PARTIAL` based on confidence
- unknown consistency must not be treated as PASS

## What Active Task Validator Must NOT Check

`validate-active-task.py` must not decide:
- whether task is ready for execution
- whether all verification plans are runnable
- whether approval marker is still non-expired
- whether `analysis_status` is invalid/conflict
- whether transition is still allowed today
- whether runner can start
- whether source task is semantically good
- whether implementation should proceed

These belong to Execution Readiness Gate (`docs/EXECUTION-READINESS.md`).

## Allowed Reads

Validator may read:
- `tasks/active-task.md`
- `source_task` referenced in `active-task.md`
- `source_contract` referenced in `active-task.md`
- approval marker location only if resolver already exists

## Forbidden Writes

`validate-active-task.py` must be read-only.

It must not modify:
- `tasks/active-task.md`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `reports/`
- `approvals/`
- git state

## Result Statuses and Exit Codes

| Status | Meaning | Exit code |
|---|---|---:|
| `PASS` | `active-task.md` exists and required integrity checks passed | 0 |
| `FAIL` | file missing, malformed, inconsistent, or required linked files missing | 1 |
| `PARTIAL` | structure is valid but some resolver-dependent/consistency checks not fully provable | 1 |
| `NOT RUN` | validator was not executed | 2 |

Important:
- `PARTIAL` must not be treated as execution-ready.
- `PARTIAL` is incomplete validation, not success.

## Future Negative Fixtures (12.3.1)

- `missing-active-task`
- `missing-frontmatter`
- `missing-task-id`
- `missing-state`
- `state-not-active`
- `missing-activated-at`
- `invalid-activated-at`
- `missing-activated-by`
- `activated-by-unknown-value`
- `missing-approval-id`
- `missing-source-task`
- `missing-source-contract`
- `missing-transition`
- `wrong-transition`
- `source-task-missing`
- `source-contract-missing`
- `source-task-absolute-path`
- `source-contract-absolute-path`
- `source-task-parent-traversal`
- `source-contract-parent-traversal`
- `task-id-mismatch-source-task`
- `task-id-mismatch-source-contract`
- `malformed-yaml`
- `extra-dangerous-execution-claim`

## Safety Boundaries

- Active task validation is not task execution.
- Active task validation does not grant permission to execute.
- A valid `active-task.md` does not mean execution-ready.
- Execution readiness requires a separate gate.
- Human approval remains required for controlled transitions.

## Non-goals (12.1.1)

This task does not add:
- `validate-active-task.py`
- `check-execution-readiness.py`
- negative fixtures
- CLI integration
- pre-execution report
- runner
- task execution
- queue movement
- auto-completion
- auto-failure
- rollback
- approval marker generation
- approval marker resolver
