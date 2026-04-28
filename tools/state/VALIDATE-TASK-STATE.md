# Validate Task State

## Purpose

`scripts/validate-task-state.py` is a read-only validator for task state consistency.
It checks whether the current state reported by `scripts/detect-task-state.py` matches the available evidence.
It does not check requested transitions.
It does not execute transitions.

## Command

```bash
python3 scripts/validate-task-state.py tasks/{task-id}
```

## Inputs

The validator accepts one positional argument:

- path to a task directory

If the argument is missing or `--help` is requested, the validator prints usage and exits with code `2`.

## Outputs

The validator prints a human-readable report to stdout:

- `TASK STATE VALIDATION`
- `Task: ...`
- `Detected state: ...`
- `Result: PASS` or `Result: FAIL`
- `Reasons:` when validation fails

## Exit Codes

- `0` - validation passed
- `1` - validation failed
- `2` - CLI usage error

## Relationship with detect-task-state.py

The validator calls `scripts/detect-task-state.py` via subprocess and reads its JSON report.
It does not duplicate detection logic.
It only checks consistency between the detected state and the evidence in the report.

## Validation Rules

The validator checks state consistency only.
It does not validate requested transitions.
It does not execute transitions.
It does not modify task files.
It does not create approval markers.
It does not create `tasks/failed/`.

State-specific checks include:

- `state_conflict` fails
- `review_ready` requires `REVIEW.md`, `execution_allowed: true`, and `READY` or `READY_WITH_EDITS`
- `review_blocked` requires `REVIEW.md` and a blocked review status
- `trace_written` requires `TRACE.md` and `REVIEW.md`
- `contract_drafted` requires a valid contract draft and `TRACE.md`
- `approved_for_execution` requires a valid approval marker and contract draft
- `active` requires `tasks/active-task.md` reference and no terminal evidence
- `completed` requires `tasks/done/` evidence and no active/failed/dropped evidence
- `failed` requires `tasks/failed/` evidence and no active/completed/dropped evidence
- `dropped` requires `tasks/dropped/` evidence and no active/completed/failed evidence

`planned` evidence for `tasks/failed/` is not treated as a failure by itself when the task is not failed.

## state_conflict Behavior

If the detector reports `state_conflict`, the validator fails.
Conflicting evidence is treated as a consistency error until a human resolves it.

## Read-Only Guarantee

The validator is read-only.
It only reads the detector output and evaluates consistency.
It does not modify task files.
It does not modify detector output.
It does not grant execution authority.

## Safety Boundaries

The validator does not:

- execute transitions
- create approval markers
- replace `tasks/active-task.md`
- move queue entries
- create `tasks/failed/`
- modify task files
- modify detector output
- grant execution authority

## Example Usage

```bash
python3 scripts/validate-task-state.py tasks/task-123
python3 scripts/validate-task-state.py tasks/nonexistent-task
```
