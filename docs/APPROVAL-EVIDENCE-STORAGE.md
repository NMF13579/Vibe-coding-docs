# Approval Evidence Storage

## Purpose
Этот документ задаёт контракт хранения approval evidence в Milestone 17.

Цель: approval records должны быть обнаруживаемыми, проверяемыми и аудируемыми.

## Canonical Storage Directory
Каноническая директория:

`approvals/`

Канонический путь нового M17 record:

`approvals/<approval_id>.md`

Где `approval_id`:

`approval-<YYYYMMDD>-<task-id>-<operation>`

Пример:

`approvals/approval-20260430-task-17-1-1-complete-active.md`

## Required Storage Representation
Approval record хранится как Markdown-файл с **flat YAML frontmatter**.

Допустимая структура (flat):

```yaml
---
approval_id: "approval-20260430-task-17-1-1-complete-active"
approval_status: "active"
related_task_id: "task-17-1-1"
related_transition_id: "transition-task-17-1-1-completed"
approved_by: "human"
approved_at: "2026-04-30T10:00:00Z"
approval_scope: "Authorize controlled complete-active lifecycle mutation only."
approval_statement: "I approve controlled complete-active lifecycle mutation for task task-17-1-1 to target state completed using transition transition-task-17-1-1-completed."
approval_source: "chat-session"
allowed_operation: "complete-active"
allowed_target_state: "completed"
expires_at: ""
supersedes: ""
notes: ""
---
```

Вложенная структура для M17 запрещена:

```yaml
---
approval:
  approval_id: "approval-20260430-task-17-1-1-complete-active"
---
```

## Required Storage Rules
### 1. One Approval Record Per File
Один файл = одна approval запись.
Нельзя объединять в одном файле несколько несвязанных задач/операций/target states.

### 2. Filename Must Match approval_id
Для новых M17 records:

`<filename-without-.md> == approval_id`

### 3. Approval Records Must Be Explicit
Approval record не может быть выведен косвенно из:

- chat message
- command success
- validator/audit PASS
- transition/apply-plan/mutation-plan existence

### 4. Approval Records Must Link to Existing Lifecycle Artifacts
Новый M17 record обязан явно ссылаться на:

- related_task_id
- related_transition_id
- allowed_operation
- allowed_target_state

Transition должен существовать заранее.

### 5. Approval Records Are Authorization Inputs
Approval record — вход авторизации.
Это не:

- lifecycle mutation
- task completion
- verification/readiness evidence
- apply plan
- applied transition record
- mutation plan
- audit report

### 6. Approval Records Must Not Bypass Other Gates
Approval не обходит:

- verification
- readiness
- prepared transition requirements
- apply preconditions
- dry-run
- apply plan
- applied transition record
- mutation plan
- validation
- audit
Approval evidence does not bypass preconditions and does not bypass lifecycle evidence requirements.

### 7. Approval Records Must Not Expand Supported Operations
На текущем этапе:

- supported operation: complete-active
- supported target state: completed

Approval file не делает неподдерживаемые операции/состояния поддерживаемыми.
Approval evidence does not expand supported lifecycle operations.

## Approval Status Storage Rules
Разрешённые начальные `approval_status`:

- active
- expired
- superseded
- revoked
- invalid

Смысл:

- active: может рассматриваться как пригодный только при прохождении всех остальных gate-проверок
- expired: нельзя использовать для новой мутации
- superseded: заменён более поздним одобрением
- revoked: явно отозван
- invalid: некорректен/непригоден

Статус сам по себе не авторизует мутацию.

## Legacy Approval Boundary
Старые (pre-M17) approval файлы могут иметь другой формат.

- не переписывать
- не переименовывать
- не нормализовать

Legacy approvals не считаются валидными M17 lifecycle mutation approvals, пока явно не удовлетворяют M17-модели.

## Protected Paths
Protected path:

`approvals/`

Правила:

- существующие approval files нельзя менять молча
- нельзя перезаписывать по умолчанию
- lifecycle mutation команды не должны удалять approval files
- `apply-transition.py` не должен создавать approval files как побочный эффект
- валидаторы/аудиты не должны автогенерировать approval files

## Allowed Write Behavior
Будущая запись approval допустима только когда:

- есть явное человеческое одобрение
- scope привязан к конкретной задаче
- scope привязан к конкретному prepared transition
- scope ограничен поддерживаемой операцией
- scope ограничен поддерживаемым target state
- запись хранится в `approvals/`
- используется flat YAML frontmatter
- filename совпадает с approval_id

В этом task запись approval **не реализуется**.

## Disallowed Write Behavior
Явно запрещено:

- validator создаёт approval record
- audit script создаёт approval record
- apply script создаёт approval record
- validators must not create approval records
- apply scripts must not create approval records
- lifecycle mutation команда создаёт approval record
- агент создаёт approval сам для себя
- inferred/hidden approval records
- overwrite/delete/move approval files как часть lifecycle mutation
- считать vague user text доказательством approval

## Future Validator Expectations
Будущий validator должен проверять:

- файл лежит в `approvals/`
- flat YAML frontmatter
- есть approval_id
- filename == approval_id
- approval_status допустим
- related_task_id есть
- related_transition_id есть
- transition уже подготовлен
- approved_by указывает на человека
- approved_at в ISO 8601
- approval_source допустим
- allowed_operation поддерживается
- allowed_target_state поддерживается
- approval_statement явный и не vague
- expires_at пустой или ISO 8601
- expired/superseded/revoked/invalid блокируются
- нет заявлений про bypass preconditions/evidence
- нет заявлений про неподдерживаемые operation/target states

## Non-Goals
Документ не внедряет:

- approval validator
- approval enforcement
- approval creation flow
- lifecycle mutation behavior change

## Final Rule
Этот контракт задаёт только хранение approval evidence. Он не внедряет validation/enforcement/creation и не меняет lifecycle mutation behavior.
