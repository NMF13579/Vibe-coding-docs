# Agent Runner Protocol

## Purpose

Agent runner protocol is a safe path from queue candidate to possible execution.

It does not make AgentOS autonomous.

## Core Rule

Human checkpoints are mandatory.

Runner must not start execution, complete a task, or mark a task failed without explicit human approval.

## Artifact Flow

- `tasks/queue/` stores queue candidates
- `tasks/drafts/` stores contract drafts
- `tasks/active-task.md` is the only executable task contract
- `reports/verification.md` stores execution verification

Queue entry points to the reviewed planning artifacts.
Contract draft is still not executable by itself.

## Human Checkpoints

### Checkpoint 1 — Start approval

Before replacing `tasks/active-task.md` runner must get explicit approval.

Use this wording:

```text
I found the next queued task and prepared its contract draft.
Do you approve replacing tasks/active-task.md and starting execution?
```

Without approval:

```text
Do not modify tasks/active-task.md.
Do not run execution.
```

### Checkpoint 2 — Completion approval

After implementation and verification runner cannot complete the task by itself.

Use this wording:

```text
Verification is complete.
Do you approve marking this task as done?
```

Without approval:

```text
Do not move task to done.
Do not mark complete.
```

### Checkpoint 3 — Failure approval

If execution or verification fails:

```text
Execution or verification failed.
Do you approve marking this task as failed/blocked?
```

Without approval:

```text
Do not move task.
Do not mark failed.
```

## Status Transition Rules

Allowed transitions:

```text
queued → in_progress → done
queued → blocked
in_progress → done
in_progress → failed
in_progress → blocked
```

Rules:

- `queued → in_progress` only after Start approval
- `in_progress → done` only after Completion approval
- `in_progress → failed` only after Failure approval
- `queued → blocked` only if blocker is explicitly recorded
- runner must not silently change status

## What Runner Does Not Do

Runner does not:

- make AgentOS autonomous
- replace `tasks/active-task.md` without approval
- run `scripts/run-all.sh` in this milestone
- complete tasks without approval
- fail or block tasks without approval

## How Queue Entry Connects To Execution

Queue entry should point to:

- `source_task`
- `source_review`
- `source_trace`
- `source_contract_draft`

The contract draft may later become `tasks/active-task.md`, but only after explicit human approval.

## Future Scope

`agent-next`, `agent-complete`, and `agent-fail` are only safe skeletons in this milestone.

Real execution control belongs to a future milestone.

