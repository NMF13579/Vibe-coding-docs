# State Transitions
<!-- Единственный источник правды о допустимых переходах. -->
<!-- Все события — из LAYER-1/event-dictionary.md. -->
<!-- Агент обязан проверять Guard перед каждым переходом. -->
<!-- При невыполненном Guard → блокировать и сообщить причину. -->

---

## Project State Machine

INIT → DISCOVERY → PLANNING → DEVELOPMENT → REVIEW → RELEASE_READY → MAINTENANCE
↑                                        |
└────────────── NEW_TASK_ACCEPTED ───────┘
любая → ERROR → (предыдущая после ROLLBACK_COMPLETED)


| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| INIT | INTERVIEW_STARTED | interview-session.md создан | DISCOVERY | Обновить STATE.md |
| DISCOVERY | INTERVIEW_CONFIRMED | все поля interview-session.md заполнены | PLANNING | Обновить project-status.md |
| PLANNING | PLAN_APPROVED | явное USER_APPROVED | DEVELOPMENT | Записать в atomic-decisions.md |
| DEVELOPMENT | TASK_IMPLEMENTED | self-verification пройдена | REVIEW | Запустить audit.md |
| REVIEW | AUDIT_PASSED | нет блокеров в audit.md | RELEASE_READY | Обновить HANDOFF.md |
| RELEASE_READY | DEPLOY_CONFIRMED | явное USER_APPROVED | MAINTENANCE | Обновить project-status.md |
| MAINTENANCE | NEW_TASK_ACCEPTED | задача в roadmap | DEVELOPMENT | Обновить Task в STATE.md |
| любая | ERROR_DETECTED | ошибка классифицирована | ERROR | Открыть incidents/ |
| ERROR | ROLLBACK_COMPLETED | причина зафиксирована | предыдущая | Дописать в incidents/ |

---

## Session State Machine

BOOTSTRAP → CONTEXT_LOADED → AWAITING_CONFIRMATION → EXECUTING → VERIFYING → HANDOFF
↓
INTERRUPTED → CONTEXT_LOADED


| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| BOOTSTRAP | CONTEXT_RESTORED | STATE.md + project-status.md прочитаны | CONTEXT_LOADED | Сформировать next_allowed_actions |
| CONTEXT_LOADED | PLAN_PRESENTED | план сформулирован | AWAITING_CONFIRMATION | — |
| AWAITING_CONFIRMATION | USER_APPROVED | явное "да" от пользователя | EXECUTING | Зафиксировать active_task в STATE.md |
| EXECUTING | EXECUTION_FINISHED | все шаги завершены | VERIFYING | Запустить self-verification |
| VERIFYING | VERIFICATION_PASSED | нет блокеров | HANDOFF | Обновить HANDOFF.md + STATE.md |
| EXECUTING | ERROR_DETECTED | ошибка классифицирована | INTERRUPTED | Открыть инцидент |
| INTERRUPTED | ROLLBACK_COMPLETED | откат выполнен | CONTEXT_LOADED | Записать в incidents/ |
| HANDOFF | SESSION_ENDED | HANDOFF.md обновлён | — | — |

---

## Task State Machine

DRAFT → PLANNED → IN_PROGRESS → REVIEW → DONE
↓
BLOCKED → IN_PROGRESS
↓
ROLLED_BACK


| From | Event | Guard | To | Side Effects |
|---|---|---|---|---|
| DRAFT | TASK_PLANNED | задача описана | PLANNED | Обновить roadmap |
| PLANNED | USER_APPROVED | явное подтверждение | IN_PROGRESS | Записать в session-log |
| IN_PROGRESS | TASK_IMPLEMENTED | реализация готова | REVIEW | Запустить self-verification |
| REVIEW | REVIEW_PASSED | нет замечаний | DONE | Обновить project-status.md |
| IN_PROGRESS | BLOCKER_FOUND | блокер зафиксирован | BLOCKED | Добавить в STATE.md forbidden |
| BLOCKED | BLOCKER_RESOLVED | блокер устранён | IN_PROGRESS | Убрать из forbidden |
| любая | ROLLBACK_TRIGGERED | подтверждение пользователя | ROLLED_BACK | Запустить error-handling.md |

---

## Illegal Transitions
<!-- Агент НИКОГДА не делает эти переходы, даже по просьбе пользователя -->

| Переход | Причина запрета |
|---|---|
| PLANNED → DONE | Нельзя закрыть без выполнения |
| BOOTSTRAP → EXECUTING | Нельзя действовать без загрузки контекста |
| BLOCKED → DONE | Нельзя закрыть заблокированную задачу |
| REVIEW → DEVELOPMENT | Только с фиксацией причины в session-log |
| RELEASE_READY → MAINTENANCE | Только после явного DEPLOY_CONFIRMED |
| ERROR → HANDOFF | Нельзя завершать сессию с открытым инцидентом |
| любая → EXECUTING | Только после явного USER_APPROVED |

---

## Правила агента при каждом переходе

1. Проверить Guard — если не выполнен, остановиться и назвать причину
2. Обновить STATE.md: нужный домен (state + last_event + last_updated)
3. Дописать строку в Transition Log
4. Выполнить все Side Effects из таблицы
5. Сообщить пользователю: "Переход: [Domain] From → To (событие: EVENT)"
