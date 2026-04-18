# Event Dictionary
<!-- Канонический список событий системы. -->
<!-- Все переходы в state-transitions.md используют только эти события. -->
<!-- Добавлять новые события → только через обновление этого файла. -->

---

## Project Domain

| Event | Триггер | Инициатор |
|---|---|---|
| INTERVIEW_STARTED | Начало интервью с новым проектом | агент |
| INTERVIEW_CONFIRMED | Все поля interview-session.md заполнены | агент |
| PLAN_APPROVED | Явное "да" от пользователя на план | пользователь |
| TASK_IMPLEMENTED | Код / артефакт создан и прошёл self-verification | агент |
| AUDIT_PASSED | Нет блокеров в audit.md | агент |
| DEPLOY_CONFIRMED | Явное "да" от пользователя на деплой | пользователь |
| NEW_TASK_ACCEPTED | Задача добавлена в roadmap | пользователь |
| ERROR_DETECTED | Ошибка обнаружена и классифицирована | агент |
| ROLLBACK_COMPLETED | Откат выполнен, причина зафиксирована | агент |

## Session Domain

| Event | Триггер | Инициатор |
|---|---|---|
| CONTEXT_RESTORED | STATE.md и project-status.md прочитаны | агент |
| PLAN_PRESENTED | Агент сформулировал план действий | агент |
| USER_APPROVED | Явное "да" / "давай" / "продолжай" от пользователя | пользователь |
| EXECUTION_FINISHED | Все шаги плана выполнены | агент |
| VERIFICATION_PASSED | self-verification без блокеров | агент |
| SESSION_ENDED | Агент завершает сессию | агент |
| ERROR_DETECTED | Ошибка в ходе выполнения | агент |
| ROLLBACK_COMPLETED | Откат выполнен | агент |

## Task Domain

| Event | Триггер | Инициатор |
|---|---|---|
| TASK_PLANNED | Задача описана в roadmap | пользователь/агент |
| USER_APPROVED | Явное подтверждение начать задачу | пользователь |
| TASK_IMPLEMENTED | Реализация завершена | агент |
| REVIEW_PASSED | Нет замечаний после проверки | агент |
| BLOCKER_FOUND | Обнаружен блокер | агент |
| BLOCKER_RESOLVED | Блокер устранён | агент/пользователь |
| ROLLBACK_TRIGGERED | Откат подтверждён пользователем | пользователь |

---

## Запрещённые события (никогда не используются)
- TASK_DONE_ASSUMED — задача закрыта без проверки
- AUTO_APPROVED — агент сам себя подтвердил
- SKIP_AUDIT — аудит пропущен
