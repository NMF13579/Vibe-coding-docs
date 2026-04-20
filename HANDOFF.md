<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: formal state как canonical (см. LAYER-3/STATE.md), полная история сессий -->

# HANDOFF.md — Session Handoff Contract

---

## Terminal Snapshot

> HANDOFF не является источником состояния. Канон: `LAYER-3/STATE.md`. Порядок старта агента: `llms.txt`.

- Last event (reference): `ITERATION_3_COMPLETED` — см. `LAYER-3/STATE.md` Transition Log.
- Blockers (reference): нет.

---

## Что сделано в последней сессии

- Hardening Pass: очищен HANDOFF до контракта сессии; sweep shadow-entrypoints; сверка registry с `shared/`, `tasks/`, `stages/`, `memory-bank/`, `incidents/`; в `STATE.md` добавлен `current_milestone`; создан `LAYER-1/audit-quick.md`; зафиксирован blind walkthrough в `LAYER-3/session-log.md`.

---

## Что должен сделать следующий агент первым шагом

1. Прочитать `llms.txt` и выполнить загрузку контекста по `LAYER-1/agent-rules.md` (# SESSION LOAD).
2. Свериться с `LAYER-3/STATE.md`, `LAYER-3/roadmap.md` и командой владельца.

---

## Persistent Context

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)  
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)  
Ключевые решения: `LAYER-3/atomic-decisions.md`  
Архитектура: `ARCHITECTURE.md`  
Критические зависимости: `LAYER-1/`, `LAYER-3/`  
Принцип: agent/IDE files — adapters only; логика — в `LAYER-1/`.
