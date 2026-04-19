<!-- ROLE: SESSION CONTRACT -->
<!-- AUTHORITY: SECONDARY — при конфликте проигрывает STATE.md -->
<!-- UPDATES: агент при завершении каждой сессии (Terminal Snapshot) -->
<!-- MUST CONTAIN: что сделано в сессии, первый шаг следующего агента,
     reference-поля как snapshot-контекст -->
<!-- MUST NOT CONTAIN: state-поля как source of truth,
     полная история сессий -->
<!-- WARNING: этот файл НЕ является источником состояния.
     Всегда использовать STATE.md как единственный source of truth. -->

# HANDOFF.md — Session Handoff Contract
<!-- Terminal Snapshot: перезаписывается агентом при каждом завершении сессии. -->
<!-- Session History: см. LAYER-3/session-log.md -->
<!-- Persistent Context: меняется редко, только при изменении архитектуры. -->
<!-- Историческое → CHANGELOG.md | Формальное состояние → LAYER-3/STATE.md -->

---

## Terminal Snapshot
<!-- Агент ПЕРЕЗАПИСЫВАЕТ этот блок при завершении каждой сессии -->

> ⚠️ HANDOFF.md не является источником состояния.
> Перед началом работы ОБЯЗАТЕЛЬНО прочитать:
> 1. `LAYER-3/STATE.md` — canonical state (primary)
> 2. Затем этот файл — session context (secondary)

Last event (reference, не canonical): ITERATION_3_COMPLETED
Last transition (reference, не canonical): DEVELOPMENT → MAINTENANCE (2026-04-19)

Что сделано в последней сессии:
- Разведены роли `LAYER-3/STATE.md` (formal control plane), `HANDOFF.md` (контракт сессии) и `LAYER-3/project-status.md` (нарратив); история сессий и бывшая летопись `project-status` перенесены в [`LAYER-3/session-log.md`](./LAYER-3/session-log.md) (append).
- Устранён dual-bootstrap в [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md): один `# BOOTSTRAP PROTOCOL`; исторический checklist — [`LAYER-1/deprecated/legacy-bootstrap.md`](./LAYER-1/deprecated/legacy-bootstrap.md) (архивирован, см. LAYER-1/deprecated/).
- В `dev` влита ветка `cursor/handoff-three-zone-restructure-e7fa`: разрешены конфликты в
  `HANDOFF.md`, `LAYER-3/STATE.md`, `LAYER-3/project-status.md`, `memory-bank/project-status.md`.
- Сохранён формальный `LAYER-3/STATE.md` (MAINTENANCE, guards, Transition Log).
- История шаблона до state layer — в [`CHANGELOG.md`](./CHANGELOG.md) (`## [2026-04-19] Pre-state-layer history` и связанные секции).

Что должен сделать следующий агент первым шагом:
1. Прочитать `LAYER-3/STATE.md` (canonical state)
2. Прочитать этот файл (`HANDOFF.md`) — контекст сессии
3. Прочитать `LAYER-3/project-status.md` — нарратив проекта
4. Прочитать `LAYER-3/roadmap.md` → найти TASK-001
5. Продолжить TASK-001 (State Layer Migration) по плану владельца

Blockers (reference, не canonical): нет

---

## Session History
> Полный лог сессий: `LAYER-3/session-log.md`

---

## Persistent Context
<!-- Меняется только при изменении архитектуры или стека -->

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)
Ключевые решения: LAYER-3/atomic-decisions.md
Архитектура: ARCHITECTURE.md
Критические зависимости: LAYER-1/ (28 файлов), LAYER-3/
Принцип: agent/IDE files — adapters only, вся логика — в LAYER-1/
