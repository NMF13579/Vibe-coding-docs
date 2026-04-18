# CHANGELOG

> История изменений. Агент добавляет запись после каждого релиза или значимого этапа.

## Инструкция для агента

После завершения задачи или достижения версионного рубежа:
1. Добавить новую запись **вверху** раздела «История» (новые записи всегда сверху)
2. Использовать формат ниже
3. Не изменять старые записи

## Формат записи
[версия] — YYYY-MM-DD
Добавлено

-

Изменено

-

Исправлено

-

text

Пропустить раздел если изменений в нём нет.

## Версионирование

- `0.1.0` — первый рабочий прототип
- `0.x.y` — x = новая функция, y = исправление
- `1.0.0` — публичный релиз

---

## История

## [ide-entry-points-unified] — 2026-04-19
### Изменено
- Корневые и IDE entry: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/*.mdc`, `.cursor/CLAUDE-WORKFLOW.md`, `.claude/agents/*.md` — единый шаблон (Navigation: `llms.txt`).
- `LAYER-1/audit.md` — блок эквивалента audit-agent; `session-lifecycle.md` — session-guard + детали feature-advisor; новый `cursor-auto-actions.md` — таблица из старого `CLAUDE-WORKFLOW.md`.

## [agent-bootstrap-deprecated-stub] — 2026-04-19
### Изменено
- `LAYER-1/agent-bootstrap.md`: stub DEPRECATED → канон в `agent-rules.md`; мост «Наследие agent-bootstrap.md» в `agent-rules.md` после STATE AUTHORITY TABLE.

## [agent-rules-bootstrap-v3] — 2026-04-19
### Добавлено
- `LAYER-1/agent-rules.md`: префикс BOOTSTRAP (event-dictionary / state-transitions, roadmap, CONTEXT_RESTORED), блок при отсутствии `STATE.md`, таблица **STATE AUTHORITY TABLE** (ответственность за файлы).

## [HANDOFF-reset-2026-04-19b] — 2026-04-19
### Изменено
- `HANDOFF.md`: сброс Session History до двух строк шаблона; предыдущая версия с расширенной таблицей — в конце файла под `## [2026-04-19] Pre-state-layer history` (подраздел «Снимок HANDOFF от 2026-04-19»).

## [STATE-formal-v2] — 2026-04-19
### Изменено
- `LAYER-3/STATE.md`: формальный канон состояния (приоритет над `project-status.md`), Session BOOTSTRAP после старта, guard `close_task_without_review`, формат Transition Log `Domain | Event | From → To`.

## [state-transitions-full] — 2026-04-19
### Изменено
- `LAYER-1/state-transitions.md`: единый источник переходов — диаграммы и таблицы Project / Session / Task, illegal transitions, правила агента; события из `event-dictionary.md`.

## [atomic-decisions] — 2026-04-19
### Добавлено
- `LAYER-3/atomic-decisions.md`: журнал решений по развилкам из `decision-guide.md`, шаблон строки, статусы ACTIVE / SUPERSEDED / REVERTED.

## [roadmap-formal] — 2026-04-19
### Изменено
- `LAYER-3/roadmap.md`: формальный roadmap с форматом задачи, Backlog (TASK-001), секция Done.

## [2026-04-19] — 2026-04-19
### Изменено
- `HANDOFF.md`: новый Terminal Snapshot (TASK-001), Session History, Persistent Context; предыдущая версия — в конце файла под `## [2026-04-19] Pre-state-layer history`.
- `LAYER-3/STATE.md`, `LAYER-3/roadmap.md`: выровнено под TASK-001 State Layer Migration.

## [HANDOFF-restructure] — 2026-04-18
### Изменено
- `HANDOFF.md`: трёхзонная структура (Terminal Snapshot, Session History, Persistent Context); прежний накопленный журнал и хронология перенесены в конец этого файла (раздел «Архив из HANDOFF.md»).
- `LAYER-3/STATE.md`: выровнено под текущий снимок (MAINTENANCE, iteration-1-state-machine, ITERATION_3_COMPLETED).

## [ARCHITECTURE-state-plane] — 2026-04-18
### Добавлено
- `ARCHITECTURE.md`: раздел **State Control Plane** (компоненты control plane, три домена состояния) и **Принцип каноничности** (роли `llms.txt`, `STATE.md`, `project-status.md`, `HANDOFF.md`; правило нового правила).

## [adapter-canonicalization] — 2026-04-18
### Изменено
- `CLAUDE.md`, `.github/copilot-instructions.md`, `GEMINI.md`, `AGENTS.md`, `.cursor/rules/*.mdc`: только entry point (bootstrap + canonical sources).
- `LAYER-1/`: добавлены `session-lifecycle.md`, `plan-and-scope-gate.md`, `stage-routing.md`, `instruction-priority.md`, `read-order-and-triggers.md`, `state-transitions.md`; в `audit.md` — блок «Фокус: аудит здоровья / готовности»; в `agent-rules.md` — ссылки на эти модули.

## [llms-navigation-index] — 2026-04-18
### Изменено
- `llms.txt`: полностью заменён на навигационный индекс (не policy source): bootstrap, таблица situation routes, canonical sources.

## [event-dictionary] — 2026-04-18
### Добавлено
- `LAYER-1/event-dictionary.md`: канонический словарь событий (Project / Session / Task) и запрещённые события; связка с `state-transitions.md`.

## [1.1.1] - 2026-04-17
### Изменено
- Чеклист аудита объединён с протоколом AUDIT-FULL: раздел «Чеклист аудита» в `LAYER-1/audit.md`; файл `LAYER-1/audit-checklist.md` удалён; маршруты (`llms.txt`, README, правила IDE и др.) обновлены.
- UX-чеклисты объединены в `LAYER-1/ux-checklist-core.md`; удалены `LAYER-1/ux-checklist-accessibility.md`, `ux-checklist-medical.md`, `ux-checklist-interactions.md`; `stages/02-ux/` — указатель на канон; обновлены `llms.txt`, `install.sh`, карта шаблона и перекрёстные ссылки.

## [1.1.0] - 2026-04-16
### 🔴 Критические исправления
- Устранено противоречие «новичок vs терминал» (#1)
- Внедрён модуль соответствия 152-ФЗ (#2)
- Добавлена защита от prompt-injection (#3)
- Унифицирована роль агента (#4)
- Внедрён протокол отката (`ROLLBACK.md`) (#5)

### 🟡 Улучшения
- Система тегирования задач по риску `[HIGH/MEDIUM/LOW]` (#6)
- Углублена медицинская специфика в UX (#7)
- Расширены анти-паттерны процессуальными сценариями (#8)
- Decision-guide сделан автономным (#9)
- Добавлен интерактивный онбординг (`ONBOARDING-WIZARD.md`) (#10)

### 🟢 Экосистема
- Внедрён цикл обучения на ошибках (`LEARNING-LOOP.md`) (#11)
- Создан адаптер под другие домены (`DOMAIN-ADAPTER.md`) (#12)
- Добавлены правила для IDE (`.cursor/rules/`) (#13)
- Созданы `GLOSSARY.md` и `ARCHITECTURE.md` (#14)

### 📚 Документация
- Все файлы добавлены в навигацию `README.md`
- Проведена сквозная проверка ссылок и терминологии
- Закреплена связка Discovery: stop-point и Confirmation в `LAYER-2/discovery/project-interview.md`, таблица подтверждений с **Approved by** в `LAYER-3/project-status.md`, правила HEALTH-SCORE в `LAYER-1/audit.md` и `LAYER-1/audit-checklist.md`
- GUI-онбординг и быстрый старт: в шаблонах запроса первым читается `START.md`, затем `llms.txt` (`ONBOARDING-WIZARD.md`, `QUICK-START.md`, `README.md`, `QUICK-START-NOVICE.md`)

[0.3.2] — 2026-04-10
Изменено

- Аудит разделён: протокол AUDIT-FULL остаётся в `LAYER-1/audit.md`, чек-лист и HEALTH-SCORE вынесены в `LAYER-1/audit-checklist.md`
- В `llms.txt` добавлен маршрут «Проверка пакета в новой AI-среде» → `audit-checklist.md`
- Обновлены перекрёстные ссылки: README, CLAUDE.md, system-prompt, copilot-instructions, cursor rules, audit-agent, template-sync-index

[0.3.1] — 2026-04-10
Добавлено
- [`.cursor/CLAUDE-WORKFLOW.md`](./.cursor/CLAUDE-WORKFLOW.md) — для Cursor: ссылка на [`CLAUDE.md`](./CLAUDE.md) и этапы `stages/*/BOOT.md`.

Изменено
- [`README.md`](./README.md) — в блоке AI-сред упоминание `CLAUDE-WORKFLOW.md`.

[0.3.0] — 2026-04-10
Добавлено
- Поток **Claude Code**: единое ТЗ [`project/PROJECT.md`](./project/PROJECT.md), этапы [`stages/01-interview`](./stages/01-interview/BOOT.md) … [`stages/04-deploy`](./stages/04-deploy/BOOT.md) с `BOOT.md`, общие правила [`shared/`](./shared/README.md).
- [`CLAUDE-CODE-FLOW.md`](./CLAUDE-CODE-FLOW.md) — краткий обзор потока по этапам; [`CHECKLIST.md`](./CHECKLIST.md) — чеклист перед деплоем.
- [`CLAUDE.md`](./CLAUDE.md) переписан под Plan → Confirm → Execute, `LOCKED`, `❓ НЕ ОПРЕДЕЛЕНО`, smoke-test и приоритет источников.

Изменено
- [`llms.txt`](./llms.txt) — блок маршрутов Claude Code к `project/`, `stages/`, `shared/`, `CHECKLIST.md`.
- [`README.md`](./README.md) — строка про Claude Code; ссылки `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md`.

[0.2.1] — 2026-04-10
Исправлено
- 8 битых UPPERCASE-ссылок в `project-interview.md` → строчные имена файлов.
- 6 устаревших ссылок на `memory-bank/*` и `docs/*` в SYSTEM_PROMPT.md, RELEASE-CHECKLIST.md, ROLLBACK-PROTOCOL.md, agents.md.
- Embedded-дубли в `architecture.md` и `decisions.md` — убраны, оставлены чистые шаблоны.
- `LAYER-1/navigation.md` переименован → `LAYER-1/tools/template-sync-index.md`; ссылки на TEMPLATE-SYNC-*.md исправлены.

Добавлено
- 9 маршрутов в `llms.txt`: workflow, anti-patterns, security, glossary, feature-radar, testing-guide, decision-guide, owner, agent-bootstrap.
- Платформенный контекст в `START.md` и `SYSTEM_PROMPT.md` (deprecated-заголовки для Lovable/Bolt).

Удалено
- Директория `docs/` (21 legacy-файл); 2 уникальных перенесены: `ROLLBACK-PROTOCOL.md` → `LAYER-1/tools/deploy/`, `RELEASE-CHECKLIST.md` → `tasks/`.
- `SCOPE-CREEP-GUARD.md` (дубль scope-guard.md).
- `opencode.json`.

[0.2.0] — 2026-04-10
Добавлено
- Слои `LAYER-1/` (инструкции агента), `LAYER-2/` (ТЗ), `LAYER-3/` (память); точка входа `llms.txt`.
- `FAQ.md`, `LICENSE` (MIT), `LAYER-3/session-log.md`.

Изменено
- Документация перенесена из `docs/` и `memory-bank/` в LAYER-*; корень очищен.
- Скрипты `setup.js` и `template-sync.js` — в `LAYER-1/tools/`.

Исправлено
- Ссылки в README, CLAUDE, GEMINI, правилах Cursor, Copilot, OpenCode, workflow.

---

## Архив из HANDOFF.md (перенос 2026-04-18)

Ниже — прежние секции **«Что мы делали в последний раз»** (включая описания патчей и итераций) и **хронология** из старого `HANDOFF.md` до реструктуризации на три зоны (Terminal Snapshot / Session History / Persistent Context). Актуальный handoff — в корневом [`HANDOFF.md`](./HANDOFF.md).

### Секция «Что мы делали в последний раз» (как было)

**agent-rules.md — BOOTSTRAP / STATE AUTHORITY / HANDOFF** (2026-04-18):

- В начало [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md) добавлены **BOOTSTRAP PROTOCOL** (STATE.md, forbidden / next_allowed_actions, session-log, atomic-decisions, handoff в STATE и Terminal Snapshot в HANDOFF), **STATE AUTHORITY**, **HANDOFF PROTOCOL**.

**Оптимизация документов — ШАГ 1д** (2026-04-17):

- Содержимое `LAYER-1/ux-checklist-accessibility.md`, `ux-checklist-medical.md`, `ux-checklist-interactions.md` перенесено в [`LAYER-1/ux-checklist-core.md`](./LAYER-1/ux-checklist-core.md); три отдельных файла удалены; [`stages/02-ux/ux-checklist-core.md`](./stages/02-ux/ux-checklist-core.md) — указатель на канон; ссылки и `install.sh` обновлены.
- Проверка относительных markdown-ссылок по `*.md`, `*.mdc`, `*.txt`: **0** битых целей (внешние URL и якоря не проверялись).

**Оптимизация документов — ШАГ 1г** (2026-04-17):

- Содержимое `LAYER-1/audit-checklist.md` перенесено в [`LAYER-1/audit.md`](./LAYER-1/audit.md) (раздел **«Чеклист аудита»**); файл `audit-checklist.md` удалён; ссылки по репозиторию обновлены.

**Оптимизация документов — ШАГ 1в** (2026-04-17):

- Содержимое `LAYER-1/PROMPT-SECURITY.md` перенесено в [`LAYER-1/security.md`](./LAYER-1/security.md) (разделы «Защита от prompt injection», «Минимальные права агента»); файл `PROMPT-SECURITY.md` удалён; ссылки обновлены.

**Оптимизация документов — ШАГ 1б** (2026-04-17):

- Содержимое `LAYER-1/ROLLBACK.md` перенесено в [`LAYER-1/error-handling.md`](./LAYER-1/error-handling.md) (разделы «Процедура отката», «Когда откатывать vs исправлять на месте»); файл `ROLLBACK.md` удалён; ссылки обновлены.

**Оптимизация документов — ШАГ 1а** (2026-04-17):

- Слияние `LAYER-1/agent-bootstrap.md` + `LAYER-1/agent-contract.md` → [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md); ссылки обновлены по репозиторию; [`shared/agent-contract.md`](./shared/agent-contract.md) указывает на полную версию в `LAYER-1/`.

**Единая точка входа** (2026-04-17):

- [`START.md`](./START.md) — одна точка входа для людей и явный блок для AI; таблица «кто ты → куда идти».
- [`README.md`](./README.md) Quick Start: ссылка только на `START.md`; убраны верхние бейджи на `QUICK-START-NOVICE` / `QUICK-START` (маршруты остаются в Docs Map и др. разделах).

**Iteration 1** (2026-04-17):

- В [`LAYER-1/error-handling.md`](./LAYER-1/error-handling.md) добавлена цепочка реагирования: self-verification → error-handling → протокол отката (тот же файл, раздел «Процедура отката»).
- Создан [`HANDOFF-SHORT.md`](./HANDOFF-SHORT.md) — быстрый блок контекста для вставки в чат.
- [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) заменён на алиас → канон [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md), таблица куда вставлять промпт.
- [`llms.txt`](./llms.txt): дата шапки 2026-04-17; маршруты v1.1.0 (LEGAL-152FZ, prompt injection → `security.md`, откат → `error-handling`, ARCHITECTURE, GLOSSARY корня, DOMAIN-ADAPTER, HANDOFF-SHORT).
- В [`LAYER-1/self-verification.md`](./LAYER-1/self-verification.md) — user-facing фразы для некорректного поведения агента.

Патч **«Этап 5 — финальная валидация и релиз v1.1.0»**:

- Проведена сквозная проверка ссылок и терминологии в ключевых релизных документах.
- Обновлены `CHECKLIST.md` и чеклист аудита в `LAYER-1/audit.md` под критерии Этапов 1–4 и финальную релиз-валидацию.
- Обновлён `CHANGELOG.md` записью версии `v1.1.0`.
- Обновлён `README.md`: статус стабильной версии и блок «Что нового в v1.1.0».
- Создан `AUDIT-REPORT.md` с итогами всех этапов и рейтингами качества.

Патч **«Этап 4 — онбординг, learning loop и экосистема»**:

- Создан `ONBOARDING-WIZARD.md` с GUI-потоком для новичков.
- Создан `LEARNING-LOOP.md` и шаблон `incidents/incident-template.md`.
- Создан `DOMAIN-ADAPTER.md` для адаптации в другие профессиональные домены.
- Создан `.cursor/rules/vibe-coding-rules.mdc` с быстрыми командами `/verify`, `/rollback`, `/scope-check`, `/audit`.
- Созданы `GLOSSARY.md` и `ARCHITECTURE.md` для не-технических пользователей.
- Обновлены `QUICK-START.md`, `LAYER-1/audit.md`, `CLAUDE.md`, `README.md` под новую структуру и навигацию.

Патч **«Этап 3 — медицинская доменная специализация»**:

- Обновлён медицинский блок UX (ныне раздел `# UX-CHECKLIST-MEDICAL.md` в [`LAYER-1/ux-checklist-core.md`](./LAYER-1/ux-checklist-core.md)): убраны дубли с core, усилена клиническая специфика, добавлена секция `⚕️ Клинические сценарии`, усилены ссылки на `LEGAL-152FZ.md`.
- Обновлён `LAYER-1/interview-system.md`: добавлен медицинский блок интервью (тип данных, МИС/ЕГИСЗ, клинрекомендации, ответственное лицо) и авто-правило ` [РИСК: HIGH] + 152-ФЗ`.
- Обновлён `LAYER-1/anti-patterns.md`: добавлена секция процессуальных/коммуникационных анти-паттернов для vibe-coding с последствиями и привязкой к протоколам.
- Обновлён `LAYER-1/decision-guide.md`: добавлены встроенные определения терминов, матрица решений, развёрнутые медицинские сценарии и fallback-блок `🆘 Если не уверен`.
- Проверены устаревшие доменные пути по репозиторию — отсутствуют.

Патч **«Этап 2 — отказоустойчивость и риск-контур»**:

- Создан `LAYER-1/ROLLBACK.md` с GUI-совместимым протоколом отката (Stop/`/cancel`, фиксация, возврат через Git/UI, логирование, перезапуск).
- Обновлён `LAYER-1/error-handling.md`: добавлено реактивное дерево решений и явная граница с `self-verification.md`; для неустранимых/повторяющихся сбоев — обязательный `ROLLBACK.md`.
- Обновлён `LAYER-1/audit.md`: обязательная фиксация каждого отката (причина, объект отката, принятое решение).
- Обновлён `LAYER-1/scope-guard.md`: добавлена процедура реакции на выход за границы и примеры IN SCOPE vs OUT OF SCOPE.
- Обновлён `LAYER-1/agent-rules.md`: обязательная остановка при несоответствии контракту, ссылки на `scope-guard.md` и откат в `error-handling.md`.
- Обновлён `LAYER-1/task-protocol.md`: введены теги риска `[РИСК: HIGH/MEDIUM/LOW]` и привязка уровня проверок.
- В чеклист аудита добавлен раздел «📊 Аудит по уровням риска» — ныне в [`LAYER-1/audit.md`](./LAYER-1/audit.md) (ранее отдельный `audit-checklist.md`).
- Обновлён `LAYER-1/self-verification.md`: усилен превентивный фокус (до выполнения/до коммита), добавлены критерии и граница с error-handling.

Патч **«Этап 1 — входная точка, 152-ФЗ, prompt-security, унификация роли»**:

- Создан `ADVANCED-SETUP.md` как техническое приложение (.claude/.cursor, LLM, CLI, MCP).
- Переписан `QUICK-START.md` на GUI-first запуск без терминала.
- Обновлён `README.md`: GUI quick start и навигация на `ADVANCED-SETUP.md`, `LAYER-1/LEGAL-152FZ.md`, `LAYER-1/PROMPT-SECURITY.md`.
- `CLAUDE.md` сокращён до манифеста правил, дубли настройки убраны, добавлена ссылка на `ADVANCED-SETUP.md`.
- Созданы `LAYER-1/LEGAL-152FZ.md` и `LAYER-1/PROMPT-SECURITY.md`.
- Обновлён медицинский блок UX в [`LAYER-1/ux-checklist-core.md`](./LAYER-1/ux-checklist-core.md): медицинская специфика без дублирования core + секция «⚖️ Комплаенс 152-ФЗ».
- Обновлён `LAYER-1/security.md`: раздел «🛡️ Защита от Prompt Injection», least privilege и защита от privilege escalation.
- Обновлён `LAYER-1/system-prompt.md`: единая роль и 4 фазы выполнения.
- Обновлён `LAYER-1/agent-rules.md`: синхронизация обязательств и human-in-the-loop дисклеймер.

Патч **«Итерация 3 — Опыт и масштабирование»**:

- `LAYER-1/audit.md` (раздел чеклиста) — деградация документов (Процесс, Навигация), **Направление 7 — Свежесть документов**, строка в HEALTH-SCORE; чеклист направлений переименован в **семь**.
- `LAYER-1/dialog-style.md` — медицинский домен (принципы, примеры, формула стопа) и блок **Before/After** (сценарии A/B/C).
- `LAYER-1/tools/deploy/ROLLBACK-PROTOCOL-POST-DEPLOY.md` — протокол отката после неудачного деплоя в проде.
- `llms.txt` — маршрут на новый rollback-файл.
- `LAYER-1/deploy-guide.md` — раздел «Откат после неудачного деплоя» со ссылкой на протокол.
- `LAYER-1/tools/template-sync-index.md` — строка для rollback-протокола; описание чеклиста аудита уточнено (7 направлений).
- `LAYER-1/decision-guide.md` — развилки **15–17** (мульти-агент, переход уровней, дробление задач).

Ранее: итерации 1–2 (priority-order, конфликт задач, SEMANTIC ERROR, AI-security, медразвилки 11–14, bootstrap complete, медблок интервью, ai-failure-modes).

### Хронология и статус (как было в конце старого HANDOFF)

## Где мы остановились

Этап 5 закрыт для **исходного шаблона**: выполнена финальная валидация каркаса, синхронизация маршрутов и подготовка релизного комплекта `v1.1.0`.
Пустые product-record файлы (`LAYER-2/*`, `LAYER-3/*`, `project/PROJECT.md`) в исходнике считаются нормой до копирования в конкретный проект.

2026-04-17 — **FIX-PLAN и сверка этапов:** создан [`FIX-PLAN.md`](./FIX-PLAN.md) (журнал исправлений по аудиту 2026-04); сверка `stages/` и [`.cursor/rules/40-stage-routing.mdc`](./.cursor/rules/40-stage-routing.mdc) — расхождения зафиксированы, правки маршрутизации без подтверждения владельца не вносились.

2026-04-17 — **Онбординг README и риски:** в [`README.md`](./README.md) — таблица «Не знаешь с чего начать?» под Quick Start и таблица IDE под Supported AI Tools; в [`CLAUDE.md`](./CLAUDE.md) ограничение по скоупу ведёт на [`LAYER-1/scope-guard.md`](./LAYER-1/scope-guard.md); в [`LAYER-1/anti-patterns.md`](./LAYER-1/anti-patterns.md) — блок AI-специфичных анти-паттернов.

2026-04-17 — **Слияние веток:** разрешены конфликты в [`HANDOFF-SHORT.md`](./HANDOFF-SHORT.md) и [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) — единый шаблон восстановления контекста, таблица команд агента, блок Lovable/Bolt с шагом `START.md`, исправлена опечатка в тексте алиаса.

2026-04-17 — **Правила Cursor:** удалены дублирующие `.mdc` (`31-stage-routing`, `32-document-priority`, `33-scope-guard`); в [`.cursor/rules/00-core.mdc`](./.cursor/rules/00-core.mdc) зафиксированы единственные источники: `40-stage-routing.mdc`, `50-doc-priority.mdc`, `60-scope-guard.mdc`. Ссылка в [`AUDIT-REPORT-DEV.md`](./AUDIT-REPORT-DEV.md) ведёт на `50-doc-priority.mdc`.

2026-04-16 — Исправлены внутренние ссылки по репозиторию (автопроверка markdown: **0** битых целей). Добавлен корневой [`GEMINI.md`](./GEMINI.md). Выровнены относительные пути в адаптерах интервью, деплой-файлах в `LAYER-1/tools/deploy/`, [`LAYER-1/interview-system.md`](./LAYER-1/interview-system.md), [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md), примерах в `tasks/`.

2026-04-16 — Проверка на остаточные **конфликты инструкций**: уточнён блок «что читать» в [`START.md`](./START.md); выровнен порядок чтения в [`.cursor/rules/00-core.mdc`](./.cursor/rules/00-core.mdc) и точка входа в [`.cursor/rules/10-communication.mdc`](./.cursor/rules/10-communication.mdc) с `START.md` + `llms.txt`; приоритет в [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md) явно отсылает к [`shared/priority-order.md`](./shared/priority-order.md).

2026-04-16 — **Минимальная стабилизация шаблона:** закреплён [`AUDIT-REPORT-DEV.md`](./AUDIT-REPORT-DEV.md); выровнен [`.cursor/rules/50-doc-priority.mdc`](./.cursor/rules/50-doc-priority.mdc) с [`shared/priority-order.md`](./shared/priority-order.md); поля `Next` и отсылки в ключевых файлах `LAYER-2/` приведены к реальным путям; в [`llms.txt`](./llms.txt) добавлен маршрут на отчёт dev.

2026-04-16 — **Уборка остаточного шума:** [`.cursor/rules/50-doc-priority.mdc`](./.cursor/rules/50-doc-priority.mdc) приведён к канону [`shared/priority-order.md`](./shared/priority-order.md); устаревшие имена файлов вычищены в [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md), [`LAYER-1/interview-system.md`](./LAYER-1/interview-system.md), [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md), точечно в [`LAYER-1/workflow.md`](./LAYER-1/workflow.md), [`LAYER-1/agent-rules.md`](./LAYER-1/agent-rules.md), [`LAYER-1/dialog-style.md`](./LAYER-1/dialog-style.md); сжаты пересечения в чеклисте [`LAYER-1/audit.md`](./LAYER-1/audit.md); обновлена шапка и пример поиска в [`llms.txt`](./llms.txt).

2026-04-16 — **TASK-001 и онбординг:** усилены STOP и Confirmation в [`LAYER-2/discovery/project-interview.md`](./LAYER-2/discovery/project-interview.md); в [`LAYER-3/project-status.md`](./LAYER-3/project-status.md) добавлена таблица подтверждения `interview-summary.md` с **Approved by**; в [`LAYER-1/audit.md`](./LAYER-1/audit.md) (протокол и чеклист) — правила для 🟢 по оси подтверждённого интервью; [`ONBOARDING-WIZARD.md`](./ONBOARDING-WIZARD.md), [`QUICK-START.md`](./QUICK-START.md), [`README.md`](./README.md), [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) выровнены под чтение `START.md` первым; [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) отмечен как выполненный в шаблоне (остался ручной тест на копии проекта).

2026-04-16 — **Финальная выверка маршрутов:** обновлены [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) (терминология `interview-summary.md`); [`LAYER-1/levels-guide.md`](./LAYER-1/levels-guide.md) приведён к реальным путям шаблона (`discovery/`, `ux/`, `specs/decisions.md`); в [`LAYER-2/discovery/mvp-scope.md`](./LAYER-2/discovery/mvp-scope.md) и [`LAYER-2/qa/post-launch-review.md`](./LAYER-2/qa/post-launch-review.md) выровнены текстовые отсылки на `vision.md` / `mvp-scope.md`.

2026-04-16 — **Адаптеры интервью:** общее ядро собрано в [`LAYER-1/tools/adapters/README.md`](./LAYER-1/tools/adapters/README.md) (якорь `#adapter-core`); файлы `*-INTERVIEW-CONTROL.md` — короткие дельты со ссылкой на ядро.

## Следующий лучший шаг (из старого HANDOFF)

- На **своей копии** репозитория один раз прогнать сценарий из [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) (последний неотмеченный пункт — живой тест интервью → `accepted` в таблице этого файла).
- При следующем крупном изменении структуры — повторить скан внутренних ссылок и обновить счётчики в шапке [`llms.txt`](./llms.txt).
- По желанию: пройтись `rg` по репо на остаточные имена в ВЕРХНЕМ регистре в тексте (кроме истории в `CHANGELOG` / `project/archive/`).

## Риски и вопросы (из старого HANDOFF)

- В [`LAYER-1/workflow.md`](./LAYER-1/workflow.md) по-прежнему описаны опциональные артефакты (`data-models` и др.) как шаги углублённого контура — это сценарий «создать по мере надобности», не обязательный набор файлов в исходном шаблоне.

## Применимые уроки (из старого HANDOFF)

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.

## [2026-04-19] Pre-state-layer history

Снимок содержимого [`HANDOFF.md`](./HANDOFF.md) **до** замены на контракт от 2026-04-19 (TASK-001):

```markdown
# HANDOFF.md — Session Handoff Contract
<!-- Terminal Snapshot ПЕРЕЗАПИСЫВАЕТСЯ агентом при каждом завершении сессии -->
<!-- Session History ДОПИСЫВАЕТСЯ, не перезаписывается -->
<!-- Persistent Context МЕНЯЕТСЯ редко -->
<!-- Историческое → CHANGELOG.md | Формальное состояние → LAYER-3/STATE.md -->

---

## Terminal Snapshot
<!-- ПЕРЕЗАПИСЫВАЕТСЯ каждую сессию -->

Project state: MAINTENANCE
Session state: HANDOFF
Task state: ""
Active task: ""
Last event: ITERATION_3_COMPLETED
Last transition: DEVELOPMENT → MAINTENANCE

Next allowed actions:
- continue_iteration_1_state_machine

Blockers:
- ""

Что сделано в последней сессии:
- Добавлен [`LAYER-1/event-dictionary.md`](./LAYER-1/event-dictionary.md) — канон событий по доменам Project / Session / Task и запрещённые события; связка с [`state-transitions.md`](./LAYER-1/state-transitions.md)

Что должен сделать следующий агент первым шагом:
- Прочитать LAYER-3/STATE.md
- Выполнить промты итерации 1 state-machine migration

---

## Session History
<!-- ДОПИСЫВАЕТСЯ. Одна строка на сессию. -->

| Дата | Project state | Что сделано | Следующий шаг |
|---|---|---|---|
| 2026-04-18 | MAINTENANCE | Итерация 3 завершена | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | В ARCHITECTURE.md: State Control Plane + Принцип каноничности (роли файлов) | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | IDE entry points → указатели; новые модули LAYER-1/ для логики сессии, плана, этапов, приоритетов | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | `llms.txt` переписан: navigation index, bootstrap, situation routes | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | `event-dictionary.md`: канон событий для state-transitions | Итерация 1 state-machine |

---

## Persistent Context
<!-- МЕНЯЕТСЯ редко -->

Ключевые решения: LAYER-3/atomic-decisions.md
Архитектурные ограничения: ARCHITECTURE.md
Стек: документационный фреймворк для AI-агентов
Критические зависимости: LAYER-1/ (28 файлов), LAYER-2/, LAYER-3/
```

### Снимок HANDOFF от 2026-04-19 (перед повторной заменой на шаблон TASK-001)

```markdown
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
| 2026-04-19 | MAINTENANCE | `roadmap.md`: формальный список задач, TASK-001 в Backlog | TASK-001 |

---

## Persistent Context
<!-- Меняется только при изменении архитектуры или стека -->

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)
Ключевые решения: LAYER-3/atomic-decisions.md
Архитектура: ARCHITECTURE.md
Критические зависимости: LAYER-1/ (28 файлов), LAYER-3/
Принцип: agent/IDE files — adapters only, вся логика — в LAYER-1/
```

