<!-- ROLE: CANONICAL_POLICY -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: полный протокол AUDIT-FULL (см. audit.md) -->

# Quick audit — ежедневная проверка (5–7 пунктов)

Короткий операционный чеклист. **Полный канонический аудит:** [`LAYER-1/audit.md`](./audit.md).

1. **State layer** — `LAYER-3/STATE.md` актуален, нет противоречий с guards и `next_allowed_actions`?
2. **Handoff** — `HANDOFF.md` отражает последнюю сессию (snapshot / следующий шаг), без дублирования канона из STATE?
3. **Critical links** — ключевые ссылки из `llms.txt` и активных маршрутов открываются (нет битых путей на canonical)?
4. **Shadow entrypoints** — адаптеры (IDE, Copilot, `.claude/agents`, корневые aliases) остаются pointer-only, без альтернативного bootstrap?
5. **Blockers / risks** — есть ли открытые блокеры в STATE или зафиксированные риски, требующие owner?
6. **Session log** — нужна ли запись в `LAYER-3/session-log.md` (существенные находки, смена фокуса)?
7. **Next step** — понятен ли следующий шаг для агента или владельца после проверки?

Если любой пункт «нет» или «неясно» — для глубины используй [`LAYER-1/audit.md`](./audit.md) и правила [`LAYER-1/document-governance.md`](./document-governance.md).

## Integrity quick checks
- links ok?
- metadata ok?
- bootstrap unique?
- adapters pure?
