<!-- ROLE: REFERENCE -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: runtime state, policy rules, routing logic -->

# DECISIONS

Этот файл фиксирует архитектурные решения системы.
Цель: предотвратить повторные обсуждения закрытых вопросов.
Агент должен проверять этот файл перед предложением изменений,
если изменения затрагивают архитектуру или governance.

---

## Формат записи

## Decision: [короткое имя]
Date: YYYY-MM-DD
Status: active | deprecated
### Context
Почему возникла задача
### Decision
Что выбрали и почему
### Alternatives rejected
Что отвергли и почему
### Consequences
Что это меняет в системе
### Links
Связанные файлы

---

## Success metrics
- DECISIONS.md используется как справочник прошлых решений
- повторных предложений по закрытым решениям без проверки DECISIONS.md: 0
- архитектурные изменения при необходимости фиксируются здесь

---

## Recorded decisions

## ADR-001 — Canonical bootstrap: `llms.txt` как единственный navigation entrypoint
Date: 2026-04-20
Status: active
### Context
Нужен один порядок чтения для агента без конкурирующих «вторых bootstrap».
### Decision
- Единственный **каноничный navigation bootstrap** для агента — корневой [`llms.txt`](../llms.txt): в нём заданы порядок старта и маршруты; в заголовке явно сказано, что поведение после загрузки — в [`LAYER-1/agent-rules.md`](../LAYER-1/agent-rules.md) (отдельная роль, не дублировать политику в `llms.txt`).
- Файлы IDE/платформ не задают read order и не являются альтернативным bootstrap (см. ADR-003).
### Alternatives rejected
- Несколько равноправных entrypoint (README, адаптер IDE, отдельный «стартовый» markdown) — усиливает drift и конфликт инструкций.
### Consequences
Любой агентский сценарий должен начинаться с чтения `llms.txt` по списку **Required at every start**, затем `agent-rules.md` по контракту из `llms.txt`.
### Links
[`llms.txt`](../llms.txt), [`LAYER-1/agent-rules.md`](../LAYER-1/agent-rules.md), [`ARCHITECTURE.md`](../ARCHITECTURE.md) (принцип каноничности)

## ADR-002 — State authority: `LAYER-3/STATE.md` = formal state canon
Date: 2026-04-20
Status: active
### Context
Состояние проекта/сессии/задачи не должно рассыпаться по narrative-файлам без приоритета.
### Decision
- [`LAYER-3/STATE.md`](./STATE.md) — **единственный** formal control plane и canonical source of truth для Project / Session / Task, guards и `next_allowed_actions`.
- [`HANDOFF.md`](../HANDOFF.md) — вторичный session contract / snapshot; при конфликте с `STATE.md` выигрывает `STATE.md` (зафиксировано в комментариях к обоим файлам).
### Alternatives rejected
- Делать HANDOFF или `project-status.md` источником формального state — дубли и расхождения.
### Consequences
Переходы состояния и семантика событий — только по machine/policy слоям (`event-dictionary.md`, `state-transitions.md` в LAYER-1) и обновлению `STATE.md`.
### Links
[`LAYER-3/STATE.md`](./STATE.md), [`HANDOFF.md`](../HANDOFF.md), [`LAYER-1/event-dictionary.md`](../LAYER-1/event-dictionary.md), [`LAYER-1/state-transitions.md`](../LAYER-1/state-transitions.md)

## ADR-003 — Adapter model: тонкие entrypoints, без политики и без альтернативного bootstrap
Date: 2026-04-20
Status: active
### Context
Платформенные файлы (Cursor rules, Copilot, и т.д.) не должны подменять governance или порядок чтения.
### Decision
- Адаптеры — **короткие** указания: сначала `llms.txt`, затем поведение из `LAYER-1/agent-rules.md`; без самостоятельного обхода файлов и без выдумывания структуры (пример: [`AGENTS.md`](../AGENTS.md), [`CLAUDE.md`](../CLAUDE.md), [`.cursor/rules`](../.cursor/rules/) entrypoints).
- Адаптеры **не** являются источником политики, authority или альтернативным bootstrap; реестр [`LAYER-1/adapter-registry.md`](../LAYER-1/adapter-registry.md) — только инвентаризация (как в `llms.txt`).
### Alternatives rejected
- «Умные» адаптеры с копией правил и логикой внутри IDE-файлов — неаудируемо и ломает единый bootstrap.
### Consequences
Изменения поведения агента вносятся в LAYER-1/core и `llms.txt`, а не в раздувание адаптеров; валидация адаптеров опирается на [`scripts/ADAPTER-SPEC.md`](../scripts/ADAPTER-SPEC.md) там, где это задано адаптерами.
### Links
[`llms.txt`](../llms.txt), [`LAYER-1/adapter-registry.md`](../LAYER-1/adapter-registry.md), [`AGENTS.md`](../AGENTS.md), [`scripts/ADAPTER-SPEC.md`](../scripts/ADAPTER-SPEC.md)

## ADR-004 — Лимит обязательного старта агента (≤ 7 файлов)
Date: 2026-04-20
Status: active
### Context
Нужен верхний предел обязательных чтений при старте, чтобы не раздувать контекст.
### Decision
В [`llms.txt`](../llms.txt) в секции **Required at every start** перечислено ровно **3** обязательных пункта плюс **не более 1** условного (файл задачи, если в `STATE.md` непустой `active_task`). Итого **не более 4** обязательных файлов на старт, что удовлетворяет инварианту **≤ 7**.
### Alternatives rejected
- Делать DECISIONS / INTENT / прочие support-файлы обязательными на каждый старт — противоречит секции «Read only if needed» в `llms.txt`.
### Consequences
Новые обязательные пункты в default startup добавляются только осознанно и с пересмотром этого ADR при приближении к лимиту 7.
### Links
[`llms.txt`](../llms.txt)

## ADR-005 — CI: Doc Integrity (структура документации)
Date: 2026-04-20
Status: active
### Context
Структурный drift в документации (ссылки, метаданные, bootstrap-граф) плохо ловится ревью вручную.
### Decision
- Workflow [`.github/workflows/doc-integrity.yml`](../.github/workflows/doc-integrity.yml): триггеры **`pull_request`** и **`push`** в ветку **`main`**.
- Единственный шаг проверки в job: `node tools/doc-tests/run-doc-tests.js` — пакет проверок из [`tools/doc-tests/`](../tools/doc-tests/) (ссылки, метаданные, bootstrap).
### Alternatives rejected
- Только ручной чеклист без CI — регрессии проходят незаметно.
### Consequences
Изменения в корневых navigation-файлах и графе bootstrap должны проходить зелёный Doc Integrity на защищённом потоке **main** (или осознанный bypass по решению владельца вне CI). Дополнительные CI-проверки (например identity drift) вводятся отдельным изменением workflow и при необходимости отдельным ADR или обновлением этого пункта.
### Links
[`.github/workflows/doc-integrity.yml`](../.github/workflows/doc-integrity.yml), [`tools/doc-tests/run-doc-tests.js`](../tools/doc-tests/run-doc-tests.js)
