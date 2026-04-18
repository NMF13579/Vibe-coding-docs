# State Transitions — Политика переходов состояний

Агент обязан обновлять LAYER-3/STATE.md при каждом переходе.
Переход = событие + guard + side effect. Без guard'а переход не выполняется.

---

## Project State Transitions

| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| INIT | INTERVIEW_STARTED | interview-session.md создан | DISCOVERY | Обновить STATE.md |
| DISCOVERY | INTERVIEW_CONFIRMED | все поля interview-session.md заполнены | PLANNING | Обновить project-status.md |
| PLANNING | PLAN_APPROVED | явное подтверждение пользователя | DEVELOPMENT | Записать в atomic-decisions.md |
| DEVELOPMENT | TASK_IMPLEMENTED | self-verification пройдена | REVIEW | Запустить audit.md |
| REVIEW | AUDIT_PASSED | нет блокеров в audit.md | RELEASE_READY | Обновить HANDOFF.md |
| RELEASE_READY | DEPLOY_CONFIRMED | явное подтверждение пользователя | MAINTENANCE | Обновить project-status.md |
| MAINTENANCE | NEW_TASK_ACCEPTED | task добавлен в roadmap | DEVELOPMENT | Обновить Task State |
| любая | ERROR_DETECTED | ошибка классифицирована | ERROR | Запустить error-handling.md, открыть инцидент |
| ERROR | ROLLBACK_COMPLETED | причина устранена, откат зафиксирован | предыдущая | Записать в incidents/ |

---

## Session State Transitions

| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| BOOTSTRAP | CONTEXT_RESTORED | STATE.md + project-status.md прочитаны | CONTEXT_LOADED | Сформировать next allowed actions |
| CONTEXT_LOADED | PLAN_PRESENTED | план существует | AWAITING_CONFIRMATION | Записать snapshot плана |
| AWAITING_CONFIRMATION | USER_APPROVED | явное "да" от пользователя | EXECUTING | Зафиксировать active task |
| EXECUTING | EXECUTION_FINISHED | реализация завершена | VERIFYING | Запустить self-verification.md |
| VERIFYING | VERIFICATION_PASSED | нет блокеров | HANDOFF | Обновить HANDOFF.md + project-status.md |
| EXECUTING | ERROR_DETECTED | ошибка классифицирована | INTERRUPTED | Открыть инцидент |
| INTERRUPTED | ROLLBACK_COMPLETED | откат выполнен | CONTEXT_LOADED | Записать в incidents/ |

---

## Task State Transitions

| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| DRAFT | TASK_PLANNED | задача описана в roadmap | PLANNED | Обновить Task State в STATE.md |
| PLANNED | USER_APPROVED | явное подтверждение | IN_PROGRESS | Зафиксировать в session-log.md |
| IN_PROGRESS | TASK_IMPLEMENTED | код/артефакт создан | REVIEW | Запустить self-verification |
| REVIEW | REVIEW_PASSED | нет замечаний | DONE | Обновить project-status.md |
| IN_PROGRESS | BLOCKER_FOUND | блокер зафиксирован | BLOCKED | Записать в STATE.md → blockers |
| BLOCKED | BLOCKER_RESOLVED | блокер устранён | IN_PROGRESS | Убрать из blockers |
| любая | ROLLBACK_TRIGGERED | откат подтверждён | ROLLED_BACK | Запустить error-handling.md |

---

## Запрещённые переходы (Illegal Transitions)

Агент НИКОГДА не выполняет эти переходы, даже если пользователь просит:

- `PLANNED → DONE` — задача не может быть завершена без выполнения
- `BOOTSTRAP → EXECUTING` — нельзя начать работу без загрузки контекста
- `BLOCKED → DONE` — нельзя закрыть заблокированную задачу
- `REVIEW → DEVELOPMENT` — нельзя вернуться без фиксации причины в session-log.md
- `RELEASE_READY → MAINTENANCE` — нельзя без DEPLOY_CONFIRMED от пользователя
- `ERROR → HANDOFF` — нельзя завершать сессию с активным инцидентом
- `любая → EXECUTING` — без явного USER_APPROVED

---

## Правила агента при каждом переходе

1. Проверить guard — если не выполнен, переход заблокирован
2. Обновить поле `state` в нужном домене STATE.md
3. Обновить поле `last_event` и `last_updated`
4. Дописать запись в `Transition Log` в STATE.md
5. Выполнить все Side Effects из таблицы
6. Сообщить пользователю: "Переход: X → Y (событие: EVENT)"
