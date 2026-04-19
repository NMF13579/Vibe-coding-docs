<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: formal state как canonical (см. LAYER-3/STATE.md), полная история сессий -->

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
> 1. `LAYER-3/STATE.md` — canonical state (**PRIMARY**)
> 2. Затем этот файл — session context (**SECONDARY**)

> **State (canonical):** см. `LAYER-3/STATE.md` — Project / Session / Task, `next_allowed_actions`, `forbidden`, `blockers`.

Last event (reference, не canonical): ITERATION_3_COMPLETED
Last transition (reference, не canonical): DEVELOPMENT → MAINTENANCE (2026-04-19)

Что сделано в последней сессии:
- Миграция фаз 2–4: разведены STATE / HANDOFF / project-status; session-log append; state-aware + document governance audit в `audit.md`; `document-governance.md`; единый bootstrap в `agent-rules.md`.
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
