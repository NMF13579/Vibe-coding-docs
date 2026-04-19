<!-- ROLE: RUNTIME_STATE -->
<!-- AUTHORITY: PRIMARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent -->
<!-- SOURCE_OF_TRUTH: yes -->
<!-- MUST_NOT_CONTAIN: narrative, session history, duplicate policy -->

# STATE.md — Формальное состояние системы
<!-- АГЕНТ ЧИТАЕТ ЭТОТ ФАЙЛ ПЕРВЫМ при каждом старте сессии. -->
<!-- Обновляется агентом при каждом переходе состояния. -->
<!-- Не редактировать вручную без крайней необходимости. -->
<!-- При конфликте с HANDOFF.md или project-status.md → этот файл имеет приоритет. -->

> **Правило:** этот файл — **единственный canonical source of truth** по состоянию
> (Project / Session / Task, guards, `next_allowed_actions`, `blockers`).
> При конфликте с любым другим файлом **STATE.md выигрывает**.

---

## Project
state: MAINTENANCE
last_event: ITERATION_3_COMPLETED
last_updated: 2026-04-19

## Session
state: HANDOFF
last_event: ""

## Task
active_task: TASK-001 State Layer Migration
state: PLANNED
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

blockers:
  - none

## Transition Log
<!-- Формат: YYYY-MM-DD | Domain | Event | From → To -->
- 2026-04-19 | Project | ITERATION_3_COMPLETED | DEVELOPMENT → MAINTENANCE
