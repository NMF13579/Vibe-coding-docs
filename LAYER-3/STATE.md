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
current_milestone: stabilization-hardening
last_event: ITERATION_3_COMPLETED
last_updated: 2026-04-21

## Session
state: HANDOFF
last_event: SESSION_ENDED

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
  - read_roadmap_for_next_task
  - start_new_task_from_roadmap

blockers:
  - none

## Transition Log
<!-- Формат: YYYY-MM-DD | Domain | Event | From → To -->
- 2026-04-19 | Project | ITERATION_3_COMPLETED | DEVELOPMENT → MAINTENANCE
- 2026-04-20 | Project | MILESTONE_SET | MAINTENANCE → MAINTENANCE (current_milestone: stabilization-hardening)
- 2026-04-21 | Session | SESSION_ENDED | HANDOFF → HANDOFF
- 2026-04-21 | Task | USER_APPROVED | PLANNED → IN_PROGRESS (TASK-001)
- 2026-04-21 | Task | TASK_IMPLEMENTED | IN_PROGRESS → REVIEW (TASK-001)
- 2026-04-21 | Task | REVIEW_PASSED | REVIEW → DONE (TASK-001)
