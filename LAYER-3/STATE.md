# STATE.md — Текущее состояние проекта
<!-- Обновляется агентом при каждом переходе. Не редактировать вручную. -->
<!-- Агент обязан прочитать этот файл ПЕРВЫМ при старте каждой сессии. -->

---

## Project
state: MAINTENANCE
sub_state: iteration-1-state-machine
last_event: ITERATION_3_COMPLETED
last_updated: 2026-04-18

## Session
state: BOOTSTRAP
last_event: ""
mode: ""

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
next_allowed_actions:
  - read_HANDOFF.md
  - continue_iteration_1_state_machine

## Transition Log
- 2026-04-18: ITERATION_3_COMPLETED → MAINTENANCE
