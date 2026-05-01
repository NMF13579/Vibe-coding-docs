# Build Task Contract Manually

## Purpose

This guide explains how to manually convert an approved Task Brief into an executable Task Contract.

## Two Different Artifacts

### Approved Task Brief

`tasks/{task-id}/TASK.md` is a planning and approval document.

It explains:

- what the task is
- why it matters
- what result is expected
- what is out of scope
- what risks and dependencies exist

It is readable and useful for planning, but it is not executable.

### Executable Task Contract

`tasks/active-task.md` is the execution document.

It is the file used by the execution layer and validators.
It must match the existing execution template and schema.

Do not mix these two artifacts.

## Rule Set

**Rule 1 — Brief is not executable**  
`TASK.md` нельзя исполнять напрямую. Он должен быть сначала переведён в `tasks/active-task.md`.

**Rule 2 — Human approval required**  
Перед заменой `tasks/active-task.md` нужно явное подтверждение пользователя. Формулировка:
```
I prepared an executable Task Contract draft from the approved Task Brief.
Do you approve replacing tasks/active-task.md with this contract?
```
Без подтверждения не менять `tasks/active-task.md`.

**Rule 3 — Preserve scope**  
`in_scope` и `out_of_scope` должны быть явно связаны с Brief. Запрещено добавлять "заодно" файлы, цели или улучшения.

**Rule 4 — Risk must be explicit**  
Если риск неясен, использовать:
```
risk_level: MEDIUM
risk_reason: "Risk requires human review because the brief does not provide enough detail."
```
Не занижать риск автоматически.

**Rule 5 — Verification required**  
Executable Task Contract не готов, пока в нём нет `verification_plan`. Если verification unclear:
```
TODO: define verification command or manual verification step
```
Считать contract draft, а не ready.

**Rule 6 — Existing schema remains authority**  
Итоговый `tasks/active-task.md` должен соответствовать существующему шаблону и schema. Если bridge-шаблон конфликтует с `tasks/templates/task-contract.md` — приоритет у существующего execution template.

## Manual Conversion Flow

1. Choose the approved Task Brief in `tasks/{task-id}/TASK.md`.
2. Read the full brief before touching any execution file.
3. Open `tasks/templates/task-contract.md`.
4. Prepare a draft contract based on the brief.
5. Do not replace `tasks/active-task.md` until the user explicitly approves it.
6. After approval, copy the completed contract into `tasks/active-task.md`.
7. Only after that may someone run manual validation commands later.

## What To Read From TASK.md

Read these sections carefully:

- `Context`
- `User Story`
- `Expected Result`
- `Acceptance Criteria`
- `Out of Scope`
- `Dependencies`
- `Risks`
- `Rollback / Reversal Notes`

## How To Transfer Data

Use the approved brief as source material.

- `Expected Result` becomes `expected_result`
- `Acceptance Criteria` becomes `acceptance_criteria`
- `Out of Scope` becomes `out_of_scope`
- `Rollback / Reversal Notes` becomes `rollback_plan`
- `Risks` helps define `risk_level` and `risk_reason`
- `Dependencies` helps identify likely areas involved, but does not automatically define `in_scope`

## Fields That Must Be Filled Manually

These fields require explicit manual judgment:

- `in_scope`
- `files_or_areas`
- `risk_level`
- `risk_reason`
- `verification_plan`
- `owner_approval_proof` when needed

## Fields You Must Not Invent Without Confirmation

Do not invent without user confirmation:

- extra goals
- extra files
- extra modules
- extra rollout steps
- stronger or weaker risk assumptions than the brief supports
- verification commands that are not real or not available

## If The Brief Is Incomplete

If the brief does not provide enough detail:

- keep the contract as a draft
- use `TODO:` where clarification is required
- ask for confirmation before execution

Examples:

```yaml
risk_reason: "Risk requires human review because the brief does not provide enough detail."
verification_plan:
  - "TODO: define verification command or manual verification step"
```

## How To Check The Result Later

Do not run these as part of this bridge step automatically.
These are only manual commands someone may run later:

```bash
python3 scripts/validate-task.py tasks/active-task.md
bash scripts/run-all.sh
```

## Automated draft generation

```bash
python3 scripts/generate-task-contract.py tasks/{task-id}/TASK.md
```

- generator создаёт только draft в `tasks/drafts/`
- `tasks/drafts/` — ignored runtime artifacts, не коммитить
- generator не меняет `tasks/active-task.md`
- generator требует `REVIEW.md` рядом с `TASK.md`
- generator разрешён только при `review_status: READY` или `READY_WITH_EDITS`
- generator требует `execution_allowed: true`
- generator не перезаписывает существующий draft (exit 1)
- human approval обязателен перед заменой `tasks/active-task.md`

## Final Reminder

The approved brief is for planning.
The executable contract is for execution.
The existing execution template and schema remain the final authority.
