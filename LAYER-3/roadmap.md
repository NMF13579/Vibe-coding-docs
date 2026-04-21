# Roadmap
<!-- Формальный список задач. Единственный источник правды о том, что планируется. -->
<!-- Агент обновляет статус при переходах Task State Machine. -->
<!-- Пользователь добавляет новые задачи. -->

---

## Формат задачи

TASK-NNN: Название
State: DRAFT | PLANNED | IN_PROGRESS | BLOCKED | REVIEW | DONE | ROLLED_BACK
Priority: HIGH | MEDIUM | LOW
Added: YYYY-MM-DD
Started: YYYY-MM-DD (заполняет агент)
Completed: YYYY-MM-DD (заполняет агент)
Blocker: "" (заполняет агент при BLOCKED)
Description: краткое описание задачи


---

## Backlog

(пусто — следующая задача добавляется владельцем)

---

## Done

### TASK-001: State Layer Migration
State: DONE
Priority: HIGH
Added: 2026-04-19
Started: 2026-04-21
Completed: 2026-04-21
Blocker: ""
Description: Внедрить STATE.md, state-transitions.md, event-dictionary.md,
обновить HANDOFF.md, agent-rules.md, ARCHITECTURE.md, минимизировать adapter files
