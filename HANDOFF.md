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
- Устранён dual-bootstrap в [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md): один `# BOOTSTRAP PROTOCOL`; исторический checklist — [`LAYER-1/deprecated/legacy-bootstrap.md`](./LAYER-1/deprecated/legacy-bootstrap.md) (архивирован, см. deprecated/).
- В `dev` влита ветка `cursor/handoff-three-zone-restructure-e7fa`: разрешены конфликты в
  `HANDOFF.md`, `LAYER-3/STATE.md`, `LAYER-3/project-status.md`, `memory-bank/project-status.md`.
- Сохранён формальный `LAYER-3/STATE.md` (MAINTENANCE, guards, Transition Log).
- История шаблона до state layer — в [`CHANGELOG.md`](./CHANGELOG.md) (`## [2026-04-19] Pre-state-layer history` и связанные секции).

Что должен сделать следующий агент первым шагом:
1. Прочитать LAYER-3/STATE.md
2. Прочитать LAYER-3/project-status.md
3. Прочитать LAYER-3/roadmap.md → найти TASK-001
4. Продолжить TASK-001 (State Layer Migration) по плану владельца

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
| 2026-04-19 | MAINTENANCE | agent-rules: расширенный bootstrap + STATE AUTHORITY TABLE | TASK-001 |
| 2026-04-19 | MAINTENANCE | agent-bootstrap.md → DEPRECATED stub; мост в agent-rules *(исторически; checklist-bootstrap — [`LAYER-1/deprecated/legacy-bootstrap.md`](./LAYER-1/deprecated/legacy-bootstrap.md))* | TASK-001 |
| 2026-04-19 | MAINTENANCE | Унификация entry points + перенос логики .claude / CLAUDE-WORKFLOW в LAYER-1 | TASK-001 |
| 2026-04-19 | MAINTENANCE | Merge `cursor/handoff-three-zone-restructure-e7fa` → `dev` | TASK-001 |
| 2026-04-19 | MAINTENANCE | agent-rules: единый state-first bootstrap; legacy-bootstrap в deprecated | TASK-001 |

---

## Persistent Context
<!-- Меняется только при изменении архитектуры или стека -->

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)
Ключевые решения: LAYER-3/atomic-decisions.md
Архитектура: ARCHITECTURE.md
Критические зависимости: LAYER-1/ (28 файлов), LAYER-3/
Принцип: agent/IDE files — adapters only, вся логика — в LAYER-1/
