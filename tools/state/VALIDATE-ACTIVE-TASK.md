# VALIDATE-ACTIVE-TASK

## Purpose

`scripts/validate-active-task.py` validates Active Task Integrity (Layer 1) only.
It checks that `tasks/active-task.md` is a correct activation pointer.

Source of truth:
- `docs/ACTIVE-TASK-VALIDATION.md`

## Command Usage

Default path:

```bash
python3 scripts/validate-active-task.py
```

Explicit path (fixture compatibility):

```bash
python3 scripts/validate-active-task.py --active-task tasks/active-task.md
```

## What It Checks

- active-task file exists
- YAML frontmatter exists and is parseable
- required fields exist and are non-empty
- required values:
  - `state == active`
  - `transition == approved_for_execution:active`
  - `activated_by` is in allowlist (`human-approved-command` in v1)
- `activated_at` matches timestamp-like pattern `YYYY-MM-DDTHH:MM`
- `source_task` and `source_contract` paths are repository-relative
- `source_task` and `source_contract` paths do not use parent traversal
- `source_task` and `source_contract` files exist
- task_id consistency with source files (when extractable)

## What It Does Not Check

- execution readiness
- task semantic quality
- whether runner can start
- whether transition should be executed now
- approval marker resolver (if not already implemented elsewhere)

## Allowed Reads

- `tasks/active-task.md` (or path from `--active-task`)
- `source_task` from active-task frontmatter
- `source_contract` from active-task frontmatter
- optional read-only approval marker location only if external resolver exists

## Forbidden Writes

Validator is read-only.

It must not modify:
- `tasks/active-task.md`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `reports/`
- `approvals/`
- git state

## Statuses

- `PASS`: all required integrity checks passed
- `FAIL`: missing/malformed/inconsistent required data
- `PARTIAL`: structure valid, but some required consistency could not be fully proven
- `NOT RUN`: validator was not executed

## Exit Codes

- `PASS` -> `0`
- `FAIL` -> `1`
- `PARTIAL` -> `1`
- `NOT RUN` -> `2`

Important:
- `PARTIAL` is not success.
- `PARTIAL` is not execution-ready.

## Examples

PASS example:

```text
Active Task Validation: PASS
Checked:
- active-task exists: PASS
- frontmatter: PASS
- required fields: PASS
- required values: PASS
- activated_at: PASS
- source paths: PASS
- source_task exists: PASS
- source_contract exists: PASS
- source_task task_id match: PASS
- source_contract task_id match: PASS
Notes:
- approval marker resolver: SKIPPED
```

FAIL example:

```text
Active Task Validation: FAIL
Failures:
- state must equal "active", got "queued"
Exit: 1
```

PARTIAL example:

```text
Active Task Validation: PARTIAL
Failures:
- source_contract task_id could not be determined
Exit: 1
```

## Expected Validation Failure vs Implementation Failure

Expected validation failure:
- validator runs correctly
- input state is invalid
- controlled output: `FAIL` with clear reason
- exit code: `1`

Implementation failure:
- crash/traceback/uncontrolled exception
- validator behavior not controlled by validation logic
- this is a bug and must be fixed

## Safety Boundaries

- Active task validation is not task execution.
- Active task validation does not grant execution permission.
- A valid `active-task.md` does not mean execution-ready.
- Execution readiness requires a separate gate.
