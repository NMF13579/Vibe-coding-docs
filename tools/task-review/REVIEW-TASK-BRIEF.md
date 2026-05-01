# Review Task Brief Manually

## Purpose

This guide explains how to manually review an approved Task Brief before anyone tries to convert it into an executable Task Contract.

## What Is A Task Brief

`tasks/{task-id}/TASK.md` is an approved Task Brief.

It describes:

- what the task is
- why it matters
- what result is expected
- what is out of scope
- which dependencies and risks exist

It is a planning artifact, not an execution artifact.

## Why Quality Review Exists

Quality Review answers one simple question:

Can this Task Brief be safely translated into an executable Task Contract?

If the answer is unclear, the brief should not move forward yet.

## When To Run Review

Run review after `TASK.md` is approved and before anyone prepares `tasks/active-task.md`.

Do not wait until execution starts.

## Who Can Review

Review may be done by:

- a human
- an AI agent under direct human control

The reviewer checks clarity and safety. The reviewer does not execute the task.

## Review Is Not Execution

Quality Review does not execute the task and does not change code.
Quality Review does not change `tasks/active-task.md`.

## How To Choose A Brief

1. Open the approved brief in `tasks/{task-id}/TASK.md`.
2. Read the whole file before deciding anything.
3. Focus on context, expected result, acceptance criteria, scope, risks, dependencies, and rollback notes.

## How To Create REVIEW.md Later

When review is actually needed for a task, create:

`tasks/{task-id}/REVIEW.md`

Use:

`templates/task-brief-review.md`

Review must stay next to the brief it evaluates.

## Review Statuses

### READY

```text
review_status: READY
execution_allowed: true
```

Use only if all key fields are clear, acceptance criteria are testable, scope is explicit, risks are identified, and no blockers remain.

### READY_WITH_EDITS

```text
review_status: READY_WITH_EDITS
execution_allowed: true
```

Use if there are small issues, but scope is still clear and no critical question blocks execution. Required edits must be listed explicitly.

### NEEDS_CLARIFICATION

```text
review_status: NEEDS_CLARIFICATION
execution_allowed: false
```

Use if expected result is unclear, acceptance criteria are not testable, open questions remain, or verification cannot be defined safely.

### TOO_BROAD

```text
review_status: TOO_BROAD
execution_allowed: false
```

Use if the task contains several independent tasks or scope cannot be limited safely. Recommendation: decompose into several Task Briefs.

### TOO_SMALL

```text
review_status: TOO_SMALL
execution_allowed: false
```

Use if the task does not justify a separate execution cycle or has no standalone value. Recommendation: merge it with a related `tasks/{task-id}/TASK.md`.

### DUPLICATE

```text
review_status: DUPLICATE
execution_allowed: false
```

Use if a similar task already exists in `SECTION:specs`, a similar `tasks/{task-id}/TASK.md` already exists, or the work duplicates something already done.

### BLOCKED

```text
review_status: BLOCKED
execution_allowed: false
```

Use if owner decision, access, architecture decision, or project constraints block progress.

## Rules

**Rule 1 — Review is not execution**  
Quality Review не исполняет задачу и не меняет код.

**Rule 2 — REVIEW.md stays near TASK.md**  
Review создаётся рядом с brief: `tasks/{task-id}/REVIEW.md`

**Rule 3 — REVIEW.md controls bridge readiness**  
Manual bridge из 6.1a можно запускать только если `review_status: READY` или `review_status: READY_WITH_EDITS`. Если статус другой — сначала исправить brief или разбить задачу.

**Rule 4 — No silent approval**  
Нельзя ставить READY, если acceptance criteria или verification неясны.

**Rule 5 — Execution allowed must match status**  
```text
READY / READY_WITH_EDITS          → execution_allowed: true
NEEDS_CLARIFICATION / TOO_BROAD /
TOO_SMALL / DUPLICATE / BLOCKED   → execution_allowed: false
```

**Rule 6 — Human checkpoint remains required**  
Даже если `review_status: READY`, перед заменой `tasks/active-task.md` всё равно требуется human approval из Milestone 6.1a.

## What To Do For Each Status

- `READY`: allowed to prepare a manual contract draft later
- `READY_WITH_EDITS`: fix listed edits, then continue manually
- `NEEDS_CLARIFICATION`: ask the listed questions first
- `TOO_BROAD`: split the task into smaller briefs
- `TOO_SMALL`: merge into a related task
- `DUPLICATE`: reuse or close the overlapping brief
- `BLOCKED`: wait for owner or architecture decision

## Manual Commands Available Later

Do not run these as part of this review step now.

```bash
python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md
python3 scripts/validate-task.py tasks/active-task.md
bash scripts/run-all.sh
```

The Task Brief validator checks only structure.
It does not evaluate task quality.
It does not assign `review_status`.
It does not create `REVIEW.md`.
It does not create or change `tasks/active-task.md`.
