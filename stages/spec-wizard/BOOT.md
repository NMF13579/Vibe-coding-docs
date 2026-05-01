# Spec Wizard Boot

## Роль этапа

Этот этап помогает превратить идею в approved Task Brief.

## Что проверить в начале

1. Убедись, что есть `project/PROJECT.md`.
2. Убедись, что `SECTION:discovery` имеет `LOCKED:true`.
3. Если `discovery` не закрыт, остановись и попроси пользователя сначала пройти `/init`.

## Что спросить у пользователя

Прими идею задачи и уточни:

1. Кто пользователь?
2. Какой ожидаемый результат?
3. Какие ограничения есть?
4. Что не входит в задачу?
5. Какие зависимости есть?
6. Какие риски есть?

## Context Check

Если есть `repo-map.md`, используй его для проверки контекста.

Проверь:

- не слишком ли задача маленькая
- не слишком ли задача большая
- нет ли дубля или пересечения с существующими specs
- нет ли конфликта с ограничениями проекта

Если задача слишком широкая, сначала предложи Candidate Tasks.

## Draft Task Brief

Сначала сформируй Draft Task Brief только в чате.

Не создавай файл до подтверждения пользователя.

## После подтверждения

1. Создай `tasks/{task-id}/TASK.md`
2. Используй формат `task-YYYYMMDD-short-slug`
3. В `TASK.md` обязательно укажи:
   - `status: APPROVED`
   - `executable: false`
4. Обнови `SECTION:specs` в `project/PROJECT.md`

## Важное пояснение в TASK.md

Обязательно явно напиши:

This file is an approved Task Brief.
It is not an executable Task Contract.
To execute this task, create tasks/active-task.md from tasks/templates/task-contract.md.

## Запрещено

- менять `tasks/active-task.md`
- менять `reports/verification.md`
- запускать execution pipeline
- автоматически создавать executable Task Contract
- добавлять очередь задач
- добавлять `agent-next`
- добавлять `agent-complete`

## Candidate Decomposition

Перед созданием `TASK.md` Spec Wizard обязан проверить идею и присвоить ей один из статусов:

1. `TOO_BROAD`
2. `TOO_SMALL`
3. `DUPLICATE`
4. `BLOCKED`
5. `READY_FOR_BRIEF`

### Classification Rules

#### `TOO_BROAD`

Идея слишком широкая, если:

- содержит несколько независимых результатов
- требует изменений в нескольких не связанных областях
- не может быть проверена одним понятным acceptance checklist
- звучит как большая функциональная область, а не как одна конкретная задача
- включает формулировки: "сделать систему", "реализовать личный кабинет", "улучшить весь процесс", "добавить управление задачами", "сделать полноценный модуль"

Если статус `TOO_BROAD`:

- не создавать `TASK.md`
- предложить от 2 до 7 Candidate Tasks
- дождаться, пока пользователь выберет один вариант

#### `TOO_SMALL`

Идея слишком маленькая, если:

- не имеет самостоятельной ценности
- является микроправкой формулировки
- лучше входит в уже существующую задачу
- не требует отдельного review / trace / contract flow
- не имеет meaningful acceptance criteria

Если статус `TOO_SMALL`:

- не создавать отдельный `TASK.md`
- предложить варианты обработки: merge, Required Edit, note, drop

#### `DUPLICATE`

Идея потенциальный дубль, если:

- похожая задача уже есть в `SECTION:specs` проекта
- похожий `tasks/{task-id}/TASK.md` уже существует
- задача повторяет уже выполненную работу
- задача отличается только формулировкой, но результат тот же

Для duplicate-check проверять только:

- индекс задач в `project/PROJECT.md SECTION:specs`
- task-директории формата `tasks/task-*/TASK.md`

Не обходить весь репозиторий рекурсивно.

Если статус `DUPLICATE`:

- показать похожие задачи
- коротко объяснить сходство
- спросить владельца, это новая задача, обновление старой или отказ от идеи
- не создавать `TASK.md` без подтверждения

#### `BLOCKED`

Идея заблокирована, если:

- не хватает архитектурного решения или решения владельца
- нет доступа к нужным ресурсам
- есть конфликт с `project/PROJECT.md` constraints / non-goals
- невозможно определить expected result

Если статус `BLOCKED`:

- не создавать `TASK.md`
- сформировать список blocker questions
- предложить сначала принять решение или обновить discovery/context

#### `READY_FOR_BRIEF`

Идея готова к Task Brief, если:

- результат понятен
- scope можно ограничить
- acceptance criteria можно сформулировать
- риски хотя бы предварительно понятны
- нет явных дублей
- задача не `TOO_SMALL` и не `TOO_BROAD`

Только в этом случае Spec Wizard может формировать Draft Task Brief.

### Candidate Task Format

```markdown
## Candidate Tasks

### Candidate 1 — {short title}
candidate_id:
suggested_task_id:
classification: READY_FOR_BRIEF
goal:
expected_result:
why_separate:
acceptance_focus:
out_of_scope:
risk_hint:
dependencies:
recommended_priority: high | normal | low

### Candidate 2 — {short title}
...
```

Правила:

- Candidate Task не является `TASK.md`
- Candidate Task не является executable contract
- Candidate Task не создаётся как файл автоматически
- пользователь должен выбрать одну candidate task
- только выбранная candidate task может быть превращена в Draft Task Brief

### Decomposition Output Rules

Если статус `TOO_BROAD`:

```markdown
# Decomposition Required
The idea is too broad for one Task Brief.

## Reason
...

## Candidate Tasks
...

## Recommended First Task
...

## User Decision Needed
Please choose one candidate task to turn into Draft Task Brief.
```

Если статус `TOO_SMALL`:

```markdown
# Task Too Small
This idea may not need a separate Task Brief.

## Reason
...

## Suggested Handling
- Merge into:
- Add as Required Edit:
- Keep as note:
- Drop:

## User Decision Needed
```

Если статус `DUPLICATE`:

```markdown
# Potential Duplicate

## Similar Existing Tasks
...

## Difference Check
...

## User Decision Needed
Is this a new task, an update to an existing task, or should it be dropped?
```

Если статус `BLOCKED`:

```markdown
# Task Blocked

## Blockers
...

## Questions Needed
...

## User Decision Needed
Resolve blockers before creating Task Brief.
```

### Example Cases

**Example 1 — `TOO_BROAD`**

Input:

```text
Сделать систему управления задачами для AgentOS.
```

Expected:

```text
TOO_BROAD → split into candidate tasks:
1. Define task queue folder structure
2. Define task status lifecycle
3. Define priority and blocked_by fields
4. Define manual queue selection rules
```

**Example 2 — `TOO_SMALL`**

Input:

```text
Переименовать один заголовок в README.
```

Expected:

```text
TOO_SMALL → suggest merging into docs cleanup task or handle manually.
```

**Example 3 — `READY_FOR_BRIEF`**

Input:

```text
Добавить правило, что Spec Wizard не создаёт TASK.md до подтверждения пользователя.
```

Expected:

```text
READY_FOR_BRIEF → create Draft Task Brief after confirmation.
```
