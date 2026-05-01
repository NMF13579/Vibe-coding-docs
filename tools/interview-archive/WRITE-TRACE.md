# Write Decision Trace Manually

## Purpose

Decision Trace keeps the reasoning history behind an approved Task Brief.

It helps answer:

- what the original idea was
- what questions were asked
- what decisions were made
- what options were rejected
- what assumptions remain
- what questions are still open

## Why TRACE.md Exists

`TRACE.md` preserves the path from interview to brief.

It is useful when someone later needs to understand:

- why the task was scoped this way
- why one option was chosen over another
- what was still uncertain at the time

## What TRACE.md Is Not

- `TRACE.md` does not execute the task
- `TRACE.md` does not replace `TASK.md`
- `TRACE.md` does not replace `REVIEW.md`
- `TRACE.md` is not an executable contract
- an agent must not execute a task from `TRACE.md`

## When To Create Trace

Create trace after the interview or spec discussion is complete, when there is enough context to preserve key decisions.

Use it when:

- the task involved several clarifying questions
- important options were rejected
- assumptions may matter later
- the reasoning behind the brief could be forgotten

## Who Creates Trace

Trace may be written by:

- a human
- an agent under direct human control

## Which Task To Use

1. Choose an approved Task Brief in `tasks/{task-id}/TASK.md`
2. Read the brief fully
3. Gather the interview notes, chat, or summary that led to this brief

## How To Create TRACE.md Later

Create:

`tasks/{task-id}/TRACE.md`

using:

`templates/task-decision-trace.md`

## What To Record

Record:

- original user idea
- clarifying questions and answers
- decisions made
- rejected options
- assumptions
- open questions
- scope notes
- risk notes
- links to the related brief and review

## Rejected Options

If an option was discussed and not chosen, save it in `## Rejected Options`.
This helps prevent the same rejected idea from quietly returning later.

## Assumptions

If the brief relies on an assumption, write it explicitly in `## Assumptions`.

## Open Questions

If something is still unknown, write it explicitly in `## Open Questions`.
Do not hide uncertainty.

## Linking Trace To Brief And Review

- `source_task` should point to the related `TASK.md`
- `source_review` should point to `REVIEW.md` if it exists
- if no review exists yet, use:

```text
source_review: pending
```

## trace_author

`trace_author` should be a name or a role.

Examples:

- `human`
- `spec-wizard-assisted`
- `owner`

## Trace Statuses

### COMPLETE

```text
trace_status: COMPLETE
```

Use if the trace explains the origin of the Task Brief well enough and all key decisions are recorded.

### PARTIAL

```text
trace_status: PARTIAL
```

Use if part of the interview or decisions is unknown or lost, but the trace is still useful.

### NEEDS_UPDATE

```text
trace_status: NEEDS_UPDATE
```

Use if the brief changed after review or clarification and the trace no longer fully matches the current brief.

## Rules

**Rule 1 — Trace is not execution**  
`TRACE.md` не исполняет задачу и не меняет код.

**Rule 2 — Trace is not source of execution truth**  
`TRACE.md` не является executable contract. Агент не должен исполнять задачу по `TRACE.md`.

**Rule 3 — TASK.md remains task source**  
Итоговая задача фиксируется в `tasks/{task-id}/TASK.md`. Trace только объясняет, почему brief был сформулирован именно так.

**Rule 4 — REVIEW.md remains readiness source**  
Готовность к manual bridge фиксируется в `tasks/{task-id}/REVIEW.md`. Trace не выставляет READY / BLOCKED.

**Rule 5 — Preserve rejected options**  
Если во время интервью были отклонённые варианты — сохранять в `## Rejected Options`, чтобы агент не возвращался к ним позже.

**Rule 6 — Assumptions must be explicit**  
Если brief содержит предположение — явно записать в `## Assumptions`.

**Rule 7 — Open questions must not be hidden**  
Если вопрос остался открытым — записать в `## Open Questions`.

## Manual usage

1. Открыть `tasks/{task-id}/TASK.md`
2. Открыть связанный чат / заметки интервью, если есть
3. Создать `tasks/{task-id}/TRACE.md` из `templates/task-decision-trace.md`
4. Заполнить: decisions, assumptions, rejected options, open questions
5. Не менять `TASK.md`, `REVIEW.md`, `active-task.md` без отдельной команды

## Manual Commands Available Later

Do not run these now:

```bash
python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md
python3 scripts/validate-task.py tasks/active-task.md
bash scripts/run-all.sh
```
