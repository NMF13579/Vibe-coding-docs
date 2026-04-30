# Complete Active Task

## Purpose

This command is the controlled completion interface.
In Task 14.6.1 it supports dry-run and prepare.

Main question:
Would completion be allowed?

It never applies lifecycle mutation in M14.

## Commands

```bash
python3 scripts/complete-active-task.py --dry-run
```

```bash
python3 scripts/complete-active-task.py --dry-run \
  --session reports/execution/<session-id>.md
```

```bash
python3 scripts/complete-active-task.py --dry-run \
  --active-task tasks/active-task.md
```

```bash
python3 scripts/complete-active-task.py --prepare
```

```bash
python3 scripts/complete-active-task.py --prepare \
  --session reports/execution/<session-id>.md
```

## M14.6.1 Supported Modes

- `--dry-run`
- `--prepare`

## Forbidden Mode

- `--apply`

`--apply` is forbidden in M14.

## Result Meaning

`DRY_RUN_PASS`

Completion would be allowed for a future preparation step.
No transition is applied.

`DRY_RUN_BLOCKED`

Completion would not be allowed.
No transition is applied.

`PREPARE_CREATED`

Readiness is `PASS` and a transition evidence record is created with
`status: prepared`.
No lifecycle state is changed.

`PREPARE_BLOCKED`

Readiness is `FAIL`, `PARTIAL`, or `NOT RUN` and a transition evidence
record is created with `status: blocked`.
No lifecycle state is changed.

`PREPARE_ERROR`

Checker timeout, checker execution error, checker parse error,
or invalid mode/arguments. No transition record is created.

## Exit Codes

- `0` = readiness pass path (`DRY_RUN_PASS` or `PREPARE_CREATED`)
- `1` = blocked path (`DRY_RUN_BLOCKED` or `PREPARE_BLOCKED`)
- `2` = error/unsupported mode

## Safety Boundary

- command does not complete task
- command does not move queue
- command does not mutate active-task.md
- command does not apply lifecycle transition
- command does not create approval records
- command does not modify execution evidence
- readiness semantics belong to `check-completion-readiness.py`
- `status: applied` must never be created in M14

## Relationship to Future Tasks

- Task 14.6.1 adds `--prepare` evidence creation
- M15 may later add controlled lifecycle apply

## Non-goals

- no completion
- no transition apply
- no queue advancement
- no approval generation
