# ACTIVATE-TASK

## Purpose

`activate-task.py` performs a controlled state activation in AgentOS MVP.
It supports only one executable transition: `approved_for_execution -> active`.

`activate-task.py` does not execute the task.
`activate-task.py` does not complete the task.
`activate-task.py` does not process the queue.
`activate-task.py` does not generate approval markers.

## Command Syntax

```bash
python3 scripts/activate-task.py <task_path> --approval <approval_path> --dry-run
python3 scripts/activate-task.py <task_path> --approval <approval_path> --approved
```

Mode rule:
- exactly one of `--dry-run` or `--approved` is required
- both flags together fail
- neither flag fails

## Dry-Run Example

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md \
  --dry-run
```

## Approved Example

```bash
python3 scripts/activate-task.py tasks/task-001 \
  --approval approvals/approval-task-001-execution.md \
  --approved
```

## Required Checks

1. validate CLI mode: exactly one of `--dry-run` or `--approved`
2. task path exists
3. approval path exists
4. call `scripts/detect-task-state.py <task_path>`
5. parse `detect-task-state.py` JSON output
6. call `scripts/validate-task-state.py <task_path>`
7. call `scripts/check-transition.py <task_path> --to active`
8. call `scripts/validate-approval-marker.py <approval_path> --task <task_id> --scope activate_task --transition approved_for_execution:active`
9. parse approval marker frontmatter
10. verify approval marker `task_id` matches requested task
11. verify approval marker `scope == activate_task`
12. verify approval marker `transition == approved_for_execution:active` if transition field exists
13. verify approval marker `status == approved`
14. verify approval marker is not revoked
15. verify approval marker is not expired
16. verify no `state_conflict`: `analysis_status != conflict`
17. verify `analysis_status != invalid`
18. verify source contract exists if declared in `related_contract`
19. verify `tasks/active-task.md` write target is safe
20. if `--dry-run`: print `ACTIVATION DRY-RUN PASS`, no write
21. if `--approved`: write `tasks/active-task.md`

## Approved Mode Rules

- `--approved` does not skip checks.
- `--approved` unlocks write only after all checks pass.
- approval marker alone is insufficient.
- dry-run PASS alone is insufficient.
- dry-run never writes.
- if any check fails, write is blocked.

## Files It May Change

- `tasks/active-task.md` only

## Files It Must Not Change

- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `approvals/`
- `reports/verification.md`
- `TASK.md`
- `REVIEW.md`
- `TRACE.md`
- contract drafts
- git state

## Failure Behavior

On any failed check:
- output `ACTIVATION FAIL`
- print specific `Reason: ...`
- print `No files changed.`
- return non-zero exit code

Fail-closed mode cases:
- missing mode flag (`--dry-run`/`--approved`)
- both mode flags passed
- validation or semantic checks failed
- unsafe overwrite (active task references another task)

## Examples of Rejected Activation

No mode flag:
- command has `--approval` but no `--dry-run` and no `--approved`

Both modes passed:
- command includes both `--dry-run` and `--approved`

Wrong approval scope:
- marker scope is not `activate_task`

Revoked marker:
- marker has `revoked_at` or `revoked_by`, or status is not `approved`

Expired marker:
- marker `expires_at` is in the past or cannot be parsed

Existing `active-task.md` references another task:
- current active task `task_id` is different from requested task
