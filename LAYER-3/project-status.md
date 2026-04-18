# Project Status

> Updated: 2026-04-18 (LAYER-3/STATE.md)

## Текущий этап

Шаблон документации Vibe-coding-docs — закрыт **Этап 5** для каркаса шаблона: финальная валидация ссылок и терминологии, релизные чеклисты и changelog синхронизированы, подготовлен итоговый `AUDIT-REPORT.md`, релизный статус `v1.1.0` зафиксирован.
Важно: это статус шаблона, а не статус конкретного продукта после копирования.

## Подтверждение ключевых артефактов (Discovery)

Статусы: `not-started` | `pending-approval` | `accepted`. Колонка **Approved by** заполняется только после явного «Да» по процедуре в [`LAYER-2/discovery/project-interview.md`](../LAYER-2/discovery/project-interview.md) (секция **Confirmation**).

| Артефакт | Статус | Approved by |
|----------|--------|-------------|
| `LAYER-2/discovery/interview-summary.md` | not-started | — |

## Слои

- Discovery: ❓
- Specs: ❓
- UX: ❓
- QA: ❓
- Deploy: ❓
- Lessons: ❓

Пояснение: знаки `❓` в исходном шаблоне ожидаемы до начала реального проекта.

## Последнее действие

2026-04-18 — **STATE.md:** добавлен [`STATE.md`](./STATE.md) — машиночитаемое состояние проекта/сессии/задачи и guards для агентов. Черновой PR: https://github.com/NMF13579/Vibe-coding-docs/pull/21. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Оптимизация ШАГ 1д + скан ссылок:** все UX-чеклисты в [`ux-checklist-core.md`](../LAYER-1/ux-checklist-core.md); удалены отдельные UX-файлы; скан относительных ссылок в `*.md` / `*.mdc` / `*.txt` — 0 битых. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Оптимизация ШАГ 1г:** чеклист аудита в [`audit.md`](../LAYER-1/audit.md); `audit-checklist.md` удалён. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Оптимизация ШАГ 1в:** prompt injection в [`security.md`](../LAYER-1/security.md); `PROMPT-SECURITY.md` удалён. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Оптимизация ШАГ 1б:** протокол отката в [`error-handling.md`](../LAYER-1/error-handling.md); `ROLLBACK.md` удалён. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Оптимизация ШАГ 1а:** [`agent-rules.md`](../LAYER-1/agent-rules.md) (merge bootstrap + contract); обновлены ссылки; удалены старые файлы в `LAYER-1/`. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Iteration 1:** цепочка в [`error-handling.md`](../LAYER-1/error-handling.md); [`HANDOFF-SHORT.md`](../HANDOFF-SHORT.md); алиас [`SYSTEM_PROMPT.md`](../SYSTEM_PROMPT.md); маршруты в [`llms.txt`](../llms.txt); user-блок в [`self-verification.md`](../LAYER-1/self-verification.md). См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **Merge:** без конфликт-маркеров в [`HANDOFF-SHORT.md`](../HANDOFF-SHORT.md) и [`SYSTEM_PROMPT.md`](../SYSTEM_PROMPT.md); содержимое объединено из веток. См. [`HANDOFF.md`](../HANDOFF.md).

2026-04-17 — **FIX-PLAN:** [`FIX-PLAN.md`](../FIX-PLAN.md); сверка `stages/` ↔ `40-stage-routing.mdc` — несовпадение имён/нумерации, ждём решения владельца. [`HANDOFF.md`](../HANDOFF.md), [`memory-bank/project-status.md`](../memory-bank/project-status.md).

2026-04-17 — **README / CLAUDE / anti-patterns:** таблицы в [`README.md`](../README.md) (Quick Start, Supported AI Tools); ссылка на скоуп в [`CLAUDE.md`](../CLAUDE.md) → [`LAYER-1/scope-guard.md`](../LAYER-1/scope-guard.md); AI-анти-паттерны в [`LAYER-1/anti-patterns.md`](../LAYER-1/anti-patterns.md). Обновлены [`HANDOFF.md`](../HANDOFF.md), [`memory-bank/project-status.md`](../memory-bank/project-status.md).

2026-04-17 — **Правила Cursor:** удалены дубли `.cursor/rules/` (`31-*`, `32-*`, `33-*`); канон в [`.cursor/rules/00-core.mdc`](../.cursor/rules/00-core.mdc); активны `40-stage-routing.mdc`, `50-doc-priority.mdc`, `60-scope-guard.mdc`. Обновлены [`HANDOFF.md`](../HANDOFF.md), [`AUDIT-REPORT-DEV.md`](../AUDIT-REPORT-DEV.md), [`memory-bank/project-status.md`](../memory-bank/project-status.md).

2026-04-16 — **Адаптеры интервью:** ядро в [`LAYER-1/tools/adapters/README.md`](../LAYER-1/tools/adapters/README.md#adapter-core), дельты в `*-INTERVIEW-CONTROL.md`; обновлены [`HANDOFF.md`](../HANDOFF.md) и [`memory-bank/project-status.md`](../memory-bank/project-status.md).

2026-04-16 — **TASK-001 + онбординг:** таблица подтверждений Discovery и **Approved by** в этом файле; усилены [`project-interview.md`](../LAYER-2/discovery/project-interview.md), [`audit.md`](../LAYER-1/audit.md) (протокол и чеклист); `START.md` в [`ONBOARDING-WIZARD.md`](../ONBOARDING-WIZARD.md), [`QUICK-START.md`](../QUICK-START.md), [`README.md`](../README.md), [`QUICK-START-NOVICE.md`](../QUICK-START-NOVICE.md); [`CHANGELOG.md`](../CHANGELOG.md); задача [`TASK-001`](../tasks/TASK-001-CONFIRMATION-INTERVIEW.md) — закрыта по шаблону.

2026-04-16 — **Финальная выверка маршрутов:** [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](../tasks/TASK-001-CONFIRMATION-INTERVIEW.md); [`LAYER-1/levels-guide.md`](../LAYER-1/levels-guide.md); [`LAYER-2/discovery/mvp-scope.md`](../LAYER-2/discovery/mvp-scope.md); [`LAYER-2/qa/post-launch-review.md`](../LAYER-2/qa/post-launch-review.md); обновлены [`HANDOFF.md`](../HANDOFF.md) и [`memory-bank/project-status.md`](../memory-bank/project-status.md).

2026-04-16 — **Уборка остаточного шума:** [`.cursor/rules/50-doc-priority.mdc`](../.cursor/rules/50-doc-priority.mdc) ↔ [`shared/priority-order.md`](../shared/priority-order.md); устаревшие имена в [`LAYER-1/system-prompt.md`](../LAYER-1/system-prompt.md), [`LAYER-1/interview-system.md`](../LAYER-1/interview-system.md), [`LAYER-1/tools/template-sync-index.md`](../LAYER-1/tools/template-sync-index.md), [`LAYER-1/workflow.md`](../LAYER-1/workflow.md), [`LAYER-1/agent-rules.md`](../LAYER-1/agent-rules.md), [`LAYER-1/dialog-style.md`](../LAYER-1/dialog-style.md); сжат чеклист в [`LAYER-1/audit.md`](../LAYER-1/audit.md); шапка [`llms.txt`](../llms.txt); адаптеры интервью: `project-interview.md`. Ранее: `AUDIT-REPORT-DEV.md`, дубли `31/32/33` (сняты 2026-04-17), `Next` в `LAYER-2/`, скан ссылок.
