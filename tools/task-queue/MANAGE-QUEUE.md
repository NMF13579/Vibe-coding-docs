# Manage Task Queue Manually

## Purpose

Task Queue is a manual waiting line for tasks that are already described and reviewed.

Queue does not start execution.

## What Queue Entry Is

A queue entry is a reference document.

It is not:

- `TASK.md`
- `REVIEW.md`
- `TRACE.md`
- executable contract

It only points to those files and helps a person choose what to do next.

## Queue Lifecycle

Queue folders:

- `tasks/queue/`
- `tasks/done/`
- `tasks/dropped/`

In Milestone 6.4 do not move real tasks into these folders.

## Queue Statuses

### `queued`

The task is waiting for manual selection.

Use only when:

- `REVIEW.md` exists
- `review_status` is `READY` or `READY_WITH_EDITS`
- `execution_allowed: true`
- `blocked_by: []`

In Milestone 6.4 do not move real tasks into this status.

### `blocked`

The task exists in the queue but cannot be selected yet.

Use when:

- blockers still exist
- `blocked_by` is not empty
- review does not allow execution
- owner decision is still needed

In Milestone 6.4 do not move real tasks into this status.

### `in_progress`

The task was selected for work.

This status is for a later milestone with human-approved runner flow.

In Milestone 6.4 do not move real tasks into this status.

### `done`

The task is completed and can later be moved to `tasks/done/`.

In Milestone 6.4 do not move real tasks into this status.
Do not move files.

### `dropped`

The task is cancelled or no longer needed and can later be moved to `tasks/dropped/`.

In Milestone 6.4 do not move real tasks into this status.
Do not move files.

## Priority Rules

Allowed values:

- `high`
- `normal`
- `low`

### `high`

Use when the task:

- unblocks other tasks
- reduces system risk
- is needed for the next milestone
- fixes a critical workflow

### `normal`

Default value.

### `low`

Use when the task:

- is cosmetic
- does not block other tasks
- can wait
- is a documentation improvement without risk

## blocked_by Rules

Use `blocked_by` as a list of IDs:

```yaml
blocked_by:
  - task-20260426-example
  - decision-20260426-owner-approval
```

Rules:

- empty list means no blockers
- if `blocked_by` is not empty, `queue_status` must be `blocked`
- if `queue_status: queued`, `blocked_by` must be empty
- do not use free text instead of IDs
- explain blocker details in `## Blockers`

## How To Create Queue Entry

Create a queue entry only from a reviewed Task Brief.

Fill in:

- `source_task`
- `source_review`
- `source_trace`
- `source_contract_draft`
- `priority`
- `blocked_by`
- `execution_allowed`

## How To Decide Between queued and blocked

Use `queued` when:

- review allows execution
- no blocker remains
- task can be selected manually

Use `blocked` when:

- owner decision is missing
- review still blocks execution
- dependencies are unresolved

## Manual Selection Rules

A task may be selected manually only if:

```yaml
queue_status: queued
execution_allowed: true
blocked_by: []
```

Recommended order:

1. highest priority first: `high` → `normal` → `low`
2. if priority is equal, use the oldest `queued_at`
3. if the task blocks the next milestone, choose it earlier
4. if there is doubt, the human owner decides

There is no automatic selector in this milestone.
`agent-next` will be a separate milestone later.

## Safety Reminder

Queue does not replace approval.

Do not change `tasks/active-task.md` without human approval.

