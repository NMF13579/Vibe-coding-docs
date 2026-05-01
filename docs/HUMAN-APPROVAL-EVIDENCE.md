# Human Approval Evidence

## Purpose
Этот документ задаёт модель доказательства человеческого одобрения (approval evidence) для Milestone 17.

Approval evidence — это явный файл-артефакт авторизации.
Approval evidence is file-based and stored as a durable record under approvals/.
Approval is never inferred from conversation, command output, or implicit context.

- evidence is not approval auto-inference
- command success is not approval
- validation PASS is not approval
- approval must be explicit when required by lifecycle rules

## Approval Boundary
Human approval — отдельный артефакт авторизации.
Он не создаётся автоматически из:

- verification PASS
- completion readiness PASS
- prepared transition
- apply preconditions PASS
- dry-run success
- apply plan creation
- applied transition record creation
- mutation plan creation
- fixture success
- audit PASS
- validator PASS
- vague user confirmation

## Representation Rule
Для совместимости с текущей папкой `approvals/` используется Markdown с **flat YAML frontmatter** (плоские поля верхнего уровня).

Вложенный YAML вида `approval: { ... }` для M17 approval records запрещён.

## Canonical Approval Fields
M17 approval record должен использовать плоские поля:

- `approval_id`
- `approval_status`
- `related_task_id`
- `related_transition_id`
- `approved_by`
- `approved_at`
- `approval_scope`
- `approval_statement`
- `approval_source`
- `allowed_operation`
- `allowed_target_state`
- `expires_at`
- `supersedes`
- `notes`

## Required Field Semantics
### approval_id
Уникальный идентификатор.

Формат:

`approval-<YYYYMMDD>-<task-id>-<operation>`

Пример:

`approval-20260430-task-17-1-1-complete-active`

UUID v4 может быть добавлен только отдельной будущей задачей.

### approval_status
Допустимые начальные значения:

- active
- expired
- superseded
- revoked
- invalid

По умолчанию при создании: `active`.

### related_task_id
Идентификатор конкретной задачи, для которой выдано одобрение.
Обязательное поле.

### related_transition_id
Идентификатор уже подготовленного transition.
Обязательное поле.

Одобрение не может ссылаться на отсутствующий или гипотетический transition.

### approved_by
Кто одобрил.
Должен указывать на человека, а не на агента/систему.

### approved_at
Время одобрения в ISO 8601.
Пример: `2026-04-30T10:00:00Z`.

### approval_scope
Граница одобрения: что именно разрешено.
Должно быть конкретным и ограниченным.

### approval_statement
Явный текст разрешения, который привязан к:

- конкретной задаче
- конкретному prepared transition
- конкретной операции
- конкретному target state

### approval_source
Источник одобрения.
Начальные допустимые значения:

- chat-session
- written-statement
- external-document
- other

### allowed_operation
Разрешённая операция.
Начальное допустимое значение:

- complete-active

### allowed_target_state
Разрешённый target state.
Начальное допустимое значение:

- completed

### expires_at
Необязательное поле срока истечения в ISO 8601.
Пустое значение означает, что авто-истечения нет.

### supersedes
Необязательная ссылка на предыдущий `approval_id`, который заменяется этим одобрением.

### notes
Необязательные пояснения.
Notes не являются авторизацией.

## Allowed Initial Values
- `approval_status`: active | expired | superseded | revoked | invalid
- `allowed_operation`: complete-active
- `allowed_target_state`: completed
- `approval_source`: chat-session | written-statement | external-document | other

Новые значения добавляются только отдельными задачами и не предполагаются автоматически.

## Canonical Filename and Storage
Approval records хранятся в:

`approvals/`

Каноническое имя нового M17 record:

`approvals/<approval_id>.md`

Пример:

`approvals/approval-20260430-task-17-1-1-complete-active.md`

`approval_id` должен быть уникальным в пределах `approvals/`.

## Transition Preparation Boundary
Одобрение для controlled lifecycle mutation нельзя выдавать до подготовки transition.

Approval cannot be issued before a transition has been prepared.
Approval cannot authorize hypothetical or missing transitions.

## Vague Approval Boundary
Нечёткие фразы недопустимы как approval evidence:

- ok
- looks good
- continue
- дальше
- go ahead
- seems fine
- probably fine

Пример валидного намерения:

`I approve controlled complete-active lifecycle mutation for task <task_id> to target state completed using transition <transition_id>.`

Точное wording не фиксируется, но обязательны:

- explicit authorization
- explicit operation
- explicit task reference
- explicit prepared transition reference
- explicit target state

## Required Safety Statements
- approval evidence is not lifecycle mutation
- approval evidence is not task completion
- approval evidence is not verification evidence
- approval evidence is not readiness evidence
- approval evidence is not an apply plan
- approval evidence is not an applied transition record
- approval evidence is not a mutation plan
- approval evidence does not bypass preconditions
- approval evidence does not authorize unsupported operations
- approval evidence does not authorize unsupported target states
- approval evidence does not permit hidden completion
- approval evidence does not permit autonomous apply
- approval cannot be issued before a transition has been prepared
- approval cannot authorize hypothetical or missing transitions
- approval cannot expand the supported lifecycle operation surface
- approval cannot make unsupported mutation paths supported

## Legacy Approval Boundary
Старые approval файлы (до M17) могут не иметь полный набор полей.

- этот документ не переписывает legacy файлы
- этот документ не переименовывает legacy файлы
- этот документ не нормализует legacy файлы

Legacy records не считаются валидными M17 lifecycle mutation approvals, пока явно не соответствуют M17-модели.

## Non-Goals
Этот документ:

- не внедряет approval enforcement
- не внедряет approval validation script
- не меняет lifecycle mutation behavior
- не меняет существующие файлы в `approvals/`

## Final Rule
Human approval is valid only when it is explicit, scope-bound, durable, inspectable, and required by the applicable lifecycle rule. No validation result, command success, evidence artifact, or vague user confirmation may substitute for explicit approval.
