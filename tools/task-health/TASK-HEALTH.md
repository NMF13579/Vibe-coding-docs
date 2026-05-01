# Task Health Metrics

## Purpose

Task Health Metrics is a small read-only report about the current state of task briefs, reviews, traces, queue entries, and contract drafts.

It helps the owner quickly see:

- how many task briefs exist
- which ones are ready for contract generation
- which ones need attention
- where review, trace, queue, or draft gaps still exist

## Important Limits

This script is read-only.

It does not:

- choose the next task
- start execution
- change `tasks/active-task.md`
- change queue entries
- replace review
- replace runner scripts

## How To Run

```bash
python3 scripts/task-health.py --output reports/task-health.md
```

## How To Run On Fixtures

```bash
python3 scripts/task-health.py \
  --tasks-dir tests/fixtures/task-health/tasks \
  --output tests/fixtures/task-health/task-health.md
```

## How To Read The Report

### Tasks without review

These tasks still do not have `REVIEW.md`.
They are not ready for safe contract generation.

### Tasks without trace

These tasks still do not have `TRACE.md`.
This means decision history is missing.

### Blocked queue entries

These entries are present in queue, but they cannot move forward yet.

### `TODO:` in contract draft

If a draft contract still contains `TODO:`, it still needs human clarification.

### Ready for contract generation

A task is considered ready when:

- `TASK.md` exists
- `REVIEW.md` exists
- `review_status` is `READY` or `READY_WITH_EDITS`
- `execution_allowed: true`

### Requiring attention

This is a list of task IDs with reasons, for example:

- no review
- no trace
- blocked review
- blocked queue entry
- `TODO:` still present in draft contract

