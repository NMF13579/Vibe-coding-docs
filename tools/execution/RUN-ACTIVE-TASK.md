# Run Active Task

## Purpose

`scripts/run-active-task.py` is the controlled runner entry command for Milestone 13.
It can check readiness (`--dry-run`) and start an execution session record (`--start`).
It does not execute the task implementation itself.

## Modes

### Dry Run

`--dry-run` checks whether start would be allowed based on execution readiness.
It does not create session files.

### Start

`--start` runs readiness check and creates an execution session / attempt record in `reports/execution/`.
If readiness is PASS, session status is `in_progress`.
If readiness is non-PASS, session status is `blocked` and stop reason is `readiness_fail`.

`--dry-run` and `--start` are mutually exclusive and cannot be used together.

## Command Examples

```bash
python3 scripts/run-active-task.py --dry-run
python3 scripts/run-active-task.py --start
python3 scripts/run-active-task.py --dry-run --active-task tasks/active-task.md
python3 scripts/run-active-task.py --start --active-task tasks/active-task.md
python3 scripts/run-active-task.py --dry-run --approval-dir approvals
python3 scripts/run-active-task.py --start --approval-dir approvals
```

`--active-task` validation applies to both modes before file reading:

- no parent traversal (`..`)
- no absolute paths
- file must exist
- path must point to a file

## What Start Creates

`--start` may create:

- `reports/execution/<session_id>.md`

Session record includes:

- `active_task_snapshot` from `active-task.md` frontmatter
- `readiness_result`
- `readiness_checked_at` (time readiness subprocess returned)
- `started_at` (time session file was written)
- `changed_files: []`
- `verification_evidence: []`

`readiness_checked_at` and `started_at` are separate UTC timestamps and may differ.

## What Start Does Not Do

`--start` does not:

- execute task steps
- run verification plan
- complete the task
- fail/drop the task
- move queue state
- generate approvals
- perform rollback
- modify `tasks/active-task.md`
- modify `source_task` or `source_contract`
- modify `reports/execution/.gitkeep`

Completion remains a separate lifecycle transition.

## Exit Codes

Dry-run exit codes:

- `0` = `DRY_RUN_PASS`
- `1` = `DRY_RUN_BLOCKED`
- `2` = `DRY_RUN_NOT_RUN`

Start exit codes:

- `0` = `STARTED` (session created with `status: in_progress`)
- `1` = `START_BLOCKED` (blocked attempt record created with `status: blocked`)
- `2` = `START_NOT_RUN` (start could not be evaluated or active task could not be read)

Readiness checker mapping:

- readiness exit `0` -> PASS
- readiness exit `1` -> FAIL (blocked behavior)
- readiness exit `2` -> NOT RUN (blocked behavior for start when snapshot is available)
- any readiness exit other than `0` or `1` -> NOT RUN

Readiness checker is called with `sys.executable` and an argument list.
`shell=True` is not used.

## Safety Boundaries

- execution steps are allowed only after readiness PASS
- start mode creates only session/attempt record, not execution
- blocked readiness may still be recorded for auditability
- no verification commands are run by this command
- no queue or lifecycle transitions are performed

## Future Work

Future tasks may add execution and verification commands after session start.
This file currently documents only `--dry-run` and `--start`.
