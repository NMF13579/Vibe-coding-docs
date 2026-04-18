# State Transitions — Политика переходов состояний
<!-- Переход = событие + guard + side effect. -->
<!-- Без выполненного guard'а переход заблокирован. -->
<!-- Агент обновляет LAYER-3/STATE.md при каждом переходе. -->

---

## Project State Transitions

| Domain  | From          | Event               | Guard                                   | To            | Side Effects                         |
|---------|---------------|---------------------|-----------------------------------------|---------------|--------------------------------------|
| Project | INIT          | INTERVIEW_STARTED   | interview-session.md создан             | DISCOVERY     | Обновить STATE.md                    |
| Project | DISCOVERY     | INTERVIEW_CONFIRMED | все поля interview-session.md заполнены | PLANNING      | Обновить project-status.md           |
| Project | PLANNING      | PLAN_APPROVED       | явное подтверждение пользователя        | DEVELOPMENT   | Записать в atomic-decisions.md       |
| Project | DEVELOPMENT   | TASK_IMPLEMENTED    | self-verification пройдена              | REVIEW        | Запустить audit.md                   |
| Project | REVIEW        | AUDIT_PASSED        | нет блокеров в audit.md                 | RELEASE_READY | Обновить HANDOFF.md                  |
| Project | RELEASE_READY | DEPLOY_CONFIRMED    | явное подтверждение пользователя        | MAINTENANCE   | Обновить project-status.md           |
| Project | MAINTENANCE   | NEW_TASK_ACCEPTED   | задача добавлена в roadmap              | DEVELOPMENT   | Обновить Task State в STATE.md       |
| Project | любая         | ERROR_DETECTED      | ошибка классифицирована                 | ERROR         | Запустить error-handling.md          |
| Project | ERROR         | ROLLBACK_COMPLETED  | причина устранена, откат зафиксирован   | предыдущая    | Записать в incidents/                |

---

## Session State Transitions

| Domain  | From                  | Event               | Guard                                   | To                    | Side Effects                         |
|---------|-----------------------|---------------------|-----------------------------------------|-----------------------|--------------------------------------|
| Session | BOOTSTRAP             | CONTEXT_RESTORED    | STATE.md + project-status.md прочитаны | CONTEXT_LOADED        | Сформировать next_allowed_actions    |
| Session | CONTEXT_LOADED        | PLAN_PRESENTED      | план существует                         | AWAITING_CONFIRMATION | Записать snapshot плана              |
| Session | AWAITING_CONFIRMATION | USER_APPROVED       | явное "да" от пользователя              | EXECUTING             | Зафиксировать active_task в STATE.md |
| Session | EXECUTING             | EXECUTION_FINISHED  | реализация завершена                    | VERIFYING             | Запустить self-verification.md       |
| Session | VERIFYING             | VERIFICATION_PASSED | нет блокеров                            | HANDOFF               | Обновить HANDOFF.md + project-status |
| Session | EXECUTING             | ERROR_DETECTED      | ошибка классифицирована                 | INTERRUPTED           | Открыть инцидент                     |
| Session | INTERRUPTED           | ROLLBACK_COMPLETED  | откат выполнен                          | CONTEXT_LOADED        | Записать в incidents/                |

---

## Task State Transitions

| Domain | From        | Event            | Guard                    | To          | Side Effects                   |
|--------|-------------|------------------|--------------------------|-------------|--------------------------------|
| Task   | DRAFT       | TASK_PLANNED     | задача описана в roadmap | PLANNED     | Обновить Task State в STATE.md |
| Task   | PLANNED     | USER_APPROVED    | явное подтверждение      | IN_PROGRESS | Зафиксировать в session-log.md |
| Task   | IN_PROGRESS | TASK_IMPLEMENTED | код/артефакт создан      | REVIEW      | Запустить self-verification    |
| Task   | REVIEW      | REVIEW_PASSED    | нет замечаний            | DONE        | Обновить project-status.md     |
| Task   | IN_PROGRESS | BLOCKER_FOUND    | блокер зафиксирован      | BLOCKED     | Записать в STATE.md → forbidden|
| Task   | BLOCKED     | BLOCKER_RESOLVED | блокер устранён          | IN_PROGRESS | Убрать из forbidden в STATE.md |
| Task   | любая       | ROLLBACK_TRIGGERED | откат подтверждён      | ROLLED_BACK | Запустить error-handling.md    |

---

## Illegal Transitions
<!-- Агент НИКОГДА не выполняет эти переходы, даже если пользователь просит -->

- PLANNED → DONE (без выполнения)
- BOOTSTRAP → EXECUTING (без загрузки контекста)
- BLOCKED → DONE (нельзя закрыть заблокированную задачу)
- REVIEW → DEVELOPMENT (без фиксации причины в session-log.md)
- RELEASE_READY → MAINTENANCE (без DEPLOY_CONFIRMED от пользователя)
- ERROR → HANDOFF (нельзя завершать сессию с активным инцидентом)
- любая → EXECUTING (без явного USER_APPROVED)

---

## Правила агента при каждом переходе

1. Проверить Guard — если не выполнен, заблокировать и сообщить причину
2. Обновить state в нужном домене LAYER-3/STATE.md
3. Обновить last_event и last_updated
4. Дописать в Transition Log: YYYY-MM-DD: EVENT → STATE CHANGE
5. Выполнить Side Effects из таблицы
6. Сообщить пользователю: "Переход: [Domain] X → Y (событие: EVENT)"
