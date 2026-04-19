<!-- ROLE: FORMAL STATE -->
<!-- AUTHORITY: PRIMARY — при конфликте этот файл выигрывает -->
<!-- UPDATES: агент при каждом переходе состояния -->
<!-- MUST CONTAIN: Project state, Session state, Task state,
     next_allowed_actions, forbidden_actions, blockers -->
<!-- MUST NOT CONTAIN: narrative, session history, changelog -->

> **Правило:** state-поля (Project state, Session state, Task state,
> next_allowed_actions, forbidden_actions) могут существовать
> как source of truth только в этом файле.
> Любое появление этих полей как canonical в других файлах —
> архитектурная ошибка, требующая немедленного исправления.
>
> Исключение: reference-поля (Last transition, Last event, Blockers)
> допустимы в HANDOFF.md как snapshot-контекст, если они явно
> не объявлены каноническими и не противоречат STATE.md.

# STATE.md — Формальное состояние системы
<!-- АГЕНТ ЧИТАЕТ ЭТОТ ФАЙЛ ПЕРВЫМ при каждом старте сессии. -->
<!-- Обновляется агентом при каждом переходе состояния. -->
<!-- Не редактировать вручную без крайней необходимости. -->
<!-- При конфликте с HANDOFF.md или project-status.md → этот файл имеет приоритет. -->

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
