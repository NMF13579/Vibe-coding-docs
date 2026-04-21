# memory-bank/project-status.md

> **Каталог `memory-bank/`** — только **legacy compatibility** (см. [`README.md`](./README.md) в этой папке). Не использовать как основной источник памяти.
> Формальный канон состояния: `LAYER-3/STATE.md` (primary).
> Нарратив проекта: `LAYER-3/project-status.md` (tertiary).

## Статус

Смотри [`LAYER-3/STATE.md`](../LAYER-3/STATE.md), затем [`HANDOFF.md`](../HANDOFF.md), затем [`LAYER-3/project-status.md`](../LAYER-3/project-status.md) (разведение ролей; см. [`HANDOFF.md`](../HANDOFF.md)).

Последнее: Adapter scripts (2026-04-20) — `scripts/validate-adapters.sh`, `fix-adapters.sh`, `run-all.sh`, `scripts/ADAPTER-SPEC.md`, `README-INSTALL.md`, `.cursor/rules/governed-repo.mdc`, `.rules`; выровнены корневые адаптеры и Copilot. Ранее: Adapter governance (2026-04-20) — в `llms.txt` раздел про адаптеры и ссылка на `LAYER-1/adapter-registry.md`; добавлены `LAYER-1/adapter-registry.md`, `LAYER-1/templates/adapter-template.md`, `LAYER-1/adapters/ANTIGRAVITY.md`. Ранее: Doc Integrity Layer (2026-04-20) — добавлены `tools/doc-tests/*` (check-links/check-metadata/check-bootstrap + launcher), `tools/doc-tests/README.md`, workflow `.github/workflows/doc-integrity.yml`, точечные additions в `LAYER-1/audit.md`, `LAYER-1/audit-quick.md`, `LAYER-1/document-governance.md` и строка enforcement в `README.md`; baseline прогон `node tools/doc-tests/run-doc-tests.js` зафиксировал FAIL=7 (требует ручного устранения владельцем в документах). Ранее: Hardening Pass (2026-04-20) — HANDOFF до session contract; shadow-entrypoints pointer-only; registry дополнен `shared/`, `tasks/`, `stages/`, `memory-bank/`, `incidents/`, `audit-quick.md`; STATE — `current_milestone: stabilization-hardening`; blind walkthrough в `LAYER-3/session-log.md`. Ранее: этап 3 — канон мед. UX; этап 2 — README → `START.md`; агент — `llms.txt` + `agent-rules.md`.
