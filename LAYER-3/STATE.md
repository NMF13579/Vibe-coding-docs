# STATE.md — Формальное состояние системы
<!-- АГЕНТ ЧИТАЕТ ЭТОТ ФАЙЛ ПЕРВЫМ при каждом старте сессии. -->
<!-- Обновляется агентом при каждом переходе состояния. -->
<!-- Не редактировать вручную без крайней необходимости. -->
<!-- При конфликте с project-status.md → этот файл имеет приоритет. -->

---

## Project
state: MAINTENANCE
last_event: ITERATION_3_COMPLETED
last_updated: 2026-04-19

## Session
state: BOOTSTRAP
last_event: ""

## Task
active_task: ""
state: ""
risk: ""

## Guards
forbidden:
  - execute_without_explicit_approval
  - write_code_before_planning
  - release_without_audit
  - skip_self_verification
  - close_task_without_review

next_allowed_actions:
  - read_HANDOFF.md
  - read_project_status
  - start_new_task_from_roadmap

## Transition Log
<!-- Формат: YYYY-MM-DD | Domain | Event | From → To -->
- 2026-04-19 | Project | ITERATION_3_COMPLETED | DEVELOPMENT → MAINTENANCE
