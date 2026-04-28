# Detect Task State

## Purpose

`scripts/detect-task-state.py` is a read-only detector for task state evidence.
It inspects a task directory and related repository evidence paths and produces a JSON state report.
It does not validate transitions and does not execute transitions.

## Command

```bash
python3 scripts/detect-task-state.py tasks/{task-id}
```

## Inputs

The detector accepts one positional argument:

- path to a task directory

If the argument is missing or `--help` is requested, the detector prints usage and exits with code `2`.

## Outputs

The detector prints a JSON report to stdout.
The report includes the required fields used by the Task State Report schema:

- `task_id`
- `state`
- `evidence`
- `missing_evidence`
- `allowed_next_states`
- `blocked_reason`

Optional fields may include:

- `schema_version`
- `generated_at`
- `warnings`

## Read-Only Guarantee

The detector is read-only.
It only reads evidence and returns a JSON report.
It does not modify task files.
It does not create approval markers.
It does not create `tasks/failed/`.
It does not depend on `task-health.py`.

## state_conflict Behavior

`state_conflict` is used when evidence conflicts.
It is not a manual transition target.
The detector reports `state_conflict` as JSON and still exits `0` when the report is produced successfully.

## Evidence Paths

The detector checks evidence at:

- `{task_dir}/TASK.md`
- `{task_dir}/REVIEW.md`
- `{task_dir}/TRACE.md`
- `tasks/drafts/{task-id}-contract-draft.md`
- `approvals/`
- `tasks/active-task.md`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`

`tasks/failed/` is treated as a planned evidence path when the directory does not yet exist.
The detector does not create that directory.

## Exit Codes

- `0` - JSON report successfully produced
- `2` - CLI usage error or `--help`

## Safety Boundaries

The detector does not:

- validate transitions
- execute transitions
- modify task files
- create approval markers
- create `tasks/failed/`
- grant execution authority
- depend on `task-health.py`

## Example Usage

```bash
python3 scripts/detect-task-state.py tasks/task-123
python3 scripts/detect-task-state.py tasks/nonexistent-task
```
