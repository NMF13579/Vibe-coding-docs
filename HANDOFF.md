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

- Добавлены адаптер-пайплайн: `.cursor/rules/governed-repo.mdc`, единый текст для `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `.github/copilot-instructions.md` / `.rules`, скрипты `scripts/validate-adapters.sh`, `fix-adapters.sh`, `run-all.sh`, справка `README-INSTALL.md`, каталог кодов `scripts/ADAPTER-SPEC.md`.

- Добавлена governance-модель для платформенных адаптеров в `llms.txt` (один bootstrap, «тупые» адаптеры, реестр только для discovery). Созданы `LAYER-1/adapter-registry.md`, `LAYER-1/templates/adapter-template.md`, `LAYER-1/adapters/ANTIGRAVITY.md`.

---

## Что должен сделать следующий агент первым шагом

1. Прочитать `llms.txt` и выполнить загрузку контекста по `LAYER-1/agent-rules.md` (# SESSION LOAD).
2. Свериться с `LAYER-3/STATE.md`, `LAYER-3/roadmap.md` и командой владельца.

---

## Persistent Context

Тип проекта: AgentOS — agent control system, governed workspace for AI-agent-driven development.  
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)  
Ключевые решения: `LAYER-3/atomic-decisions.md`  
Архитектура: `ARCHITECTURE.md`  
Критические зависимости: `LAYER-1/`, `LAYER-3/`  
Принцип: agent/IDE files — adapters only; логика — в `LAYER-1/`.

---

## Update (2026-04-20)

- Внедрён минимальный doc-integrity layer: `tools/doc-tests/` (3 проверки + launcher), CI workflow `.github/workflows/doc-integrity.yml`, policy-добавления в `LAYER-1/audit.md` и `LAYER-1/audit-quick.md`.

---

## Recovery baseline (2026-04-21)

Точка восстановления после прохода governance / identity / adapters / state / CI (серия PR в `dev`; мерж по очереди владельца):

- **Identity drift:** CI может требовать явную историческую пометку на строке при упоминании старого имени продукта в ключевых файлах (`scripts/check-identity-drift.sh` + шаг в `.github/workflows/doc-integrity.yml`, если вмержено).
- **ADR:** `LAYER-3/DECISIONS.md` — ADR-001…005 согласованы с фактической системой (`llms.txt`, `STATE.md`, doc-integrity).
- **Adapters:** `LAYER-1/adapter-registry.md` и `scripts/ADAPTER-SPEC.md` выровнены под реальные файлы и `scripts/validate-adapters.sh`.
- **State:** жизненный цикл TASK-001 в `LAYER-3/STATE.md` / `LAYER-3/roadmap.md` приведён к state machine (см. Transition Log).
- **Bootstrap / CI:** проверка существования узлов графа из `llms.txt` — `scripts/check-llms-graph-files.sh` в doc-integrity (если вмержено); в `llms.txt` уточнены примеры адаптеров и маршрут Antigravity (если вмержено).
- **memory-bank:** роль каталога зафиксирована как **legacy compatibility** — `memory-bank/README.md`, строки в `ARCHITECTURE.md` и `LAYER-1/document-governance.md` (если вмержено).

Следующая сессия: `llms.txt` → `LAYER-3/STATE.md` → этот файл; затем по `active_task` и команде владельца.
