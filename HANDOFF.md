# HANDOFF.md — Session Handoff Contract
<!-- Terminal Snapshot: перезаписывается агентом при каждом завершении сессии. -->
<!-- Session History: только дозапись, одна строка на сессию. -->
<!-- Persistent Context: меняется редко, только при изменении архитектуры. -->
<!-- Историческое → CHANGELOG.md | Формальное состояние → LAYER-3/STATE.md -->

---

## Terminal Snapshot
<!-- Агент ПЕРЕЗАПИСЫВАЕТ этот блок при завершении каждой сессии -->

Project state: MAINTENANCE
Session state: HANDOFF
Task state: PLANNED
Active task: TASK-001 State Layer Migration
Last event: ITERATION_3_COMPLETED
Last transition: DEVELOPMENT → MAINTENANCE (2026-04-19)

Что сделано в последней сессии:
- Итерация 3 завершена: audit-checklist (7 направлений), dialog-style медблок,
  rollback-protocol-post-deploy, decision-guide развилки 15-17

Что должен сделать следующий агент первым шагом:
1. Прочитать LAYER-3/STATE.md
2. Прочитать LAYER-3/project-status.md
3. Прочитать LAYER-3/roadmap.md → найти TASK-001
4. Выполнить П-7 … П-10 этой последовательности промтов

Next allowed actions:
- continue TASK-001 (State Layer Migration)

Blockers: нет

---

## Session History
<!-- Дозапись. Одна строка на сессию. Не редактировать старые записи. -->

| Дата | Project state | Что сделано | Следующий шаг |
|---|---|---|---|
| 2026-04-18 | MAINTENANCE | Итерация 3 завершена | State Layer Migration |
| 2026-04-19 | MAINTENANCE | Архитектурный анализ, план итерации 1 | TASK-001 |
| 2026-04-19 | MAINTENANCE | `state-transitions.md`: полные машины Project/Session/Task + illegal | TASK-001 |
| 2026-04-19 | MAINTENANCE | `atomic-decisions.md`: журнал атомарных решений (шаблон + статусы) | TASK-001 |

---

## Persistent Context
<!-- Меняется только при изменении архитектуры или стека -->

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)
Ключевые решения: LAYER-3/atomic-decisions.md
Архитектура: ARCHITECTURE.md
Критические зависимости: LAYER-1/ (28 файлов), LAYER-3/
Принцип: agent/IDE files — adapters only, вся логика — в LAYER-1/
