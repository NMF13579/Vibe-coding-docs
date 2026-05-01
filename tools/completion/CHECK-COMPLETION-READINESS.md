# Check Completion Readiness

## Purpose

This command checks whether a task is ready for controlled completion preparation.
It does not complete the task.

## Commands

```bash
python3 scripts/check-completion-readiness.py
```

```bash
python3 scripts/check-completion-readiness.py \
  --session reports/execution/<session-id>.md
```

```bash
python3 scripts/check-completion-readiness.py \
  --active-task tasks/active-task.md
```

## Exit Codes

- `0` = `COMPLETION_READINESS_PASS`
- `1` = `COMPLETION_READINESS_FAIL`
- `2` = `COMPLETION_READINESS_PARTIAL_OR_NOT_RUN`

`PARTIAL` and `NOT RUN` both return exit code `2`.
Use `stop_reason` in stdout to distinguish them.

## Safety Boundary

- command is read-only
- command does not complete tasks
- command does not move queue
- command does not mutate active-task.md
- command does not create transition records
- command does not create approvals
- command does not apply lifecycle transition
- command does not create reports/completion/
- command does not modify execution evidence
- command does not create cache/temp/log files

## Required Evidence

Required gates:

- active_task_exists
- execution_session_exists
- session_status_not_failed
- session_status_evidence_ready
- session_status_not_in_progress
- session_status_not_blocked
- scope_check_pass
- verification_runner_pass
- execution_evidence_report_pass
- source_contract_exists
- acceptance_criteria_present
- changed_files_known
- human_review_satisfied_if_required

## Abort Detection

If the session file contains `abort_reason: watchdog_abort` or
`abort_reason: manual_abort`, the script maps this to:

- `session_status_not_failed: FAIL`

Matching is keyed: only `abort_reason: <value>` is matched.
Bare words in prose are ignored.

If abort is detected, remaining session status gates are set to `NOT RUN`,
because the session ended abnormally.

## Result Meaning

`PASS`:
Task may be prepared for completion transition in a future step.

`FAIL`:
Task must not be prepared for completion transition.

`PARTIAL`:
Evidence is incomplete; task is not completion-ready.
`stop_reason` shows what is incomplete.

`NOT RUN`:
Readiness could not be checked.
`stop_reason` shows why, for example `session_missing` or `active_task_missing`.

## Distinguishing PARTIAL from NOT RUN

Both `PARTIAL` and `NOT RUN` return exit code `2`.
Read `stop_reason` in stdout:

- `stop_reason: session_missing` -> `NOT RUN`
- `stop_reason: active_task_missing` -> `NOT RUN`
- `stop_reason: human_review_pending` -> `PARTIAL`
- `stop_reason: changed_files_incomplete` -> `PARTIAL`

## Non-goals

- no completion
- no transition preparation
- no transition application
- no lifecycle mutation
- no approval generation
