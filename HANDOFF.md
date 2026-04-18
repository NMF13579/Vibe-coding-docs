# HANDOFF — где мы остановились

## Project Name

<!--VIBE_DOCS_PROJECT_NAME-->

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.
> Агент обновляет этот файл после каждой сессии.

## Что мы делали в последний раз

**STATE.md** (2026-04-18):

- Добавлен [`LAYER-3/STATE.md`](./LAYER-3/STATE.md) — стартовое состояние проекта, сессии и задачи для агентов (INIT / BOOTSTRAP, guards, next allowed actions, transition log). PR: https://github.com/NMF13579/Vibe-coding-docs/pull/21

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

## Следующий лучший шаг

- На **своей копии** репозитория один раз прогнать сценарий из [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) (последний неотмеченный пункт — живой тест интервью → `accepted` в таблице этого файла).
- При следующем крупном изменении структуры — повторить скан внутренних ссылок и обновить счётчики в шапке [`llms.txt`](./llms.txt).
- По желанию: пройтись `rg` по репо на остаточные имена в ВЕРХНЕМ регистре в тексте (кроме истории в `CHANGELOG` / `project/archive/`).

## Риски и вопросы

- В [`LAYER-1/workflow.md`](./LAYER-1/workflow.md) по-прежнему описаны опциональные артефакты (`data-models` и др.) как шаги углублённого контура — это сценарий «создать по мере надобности», не обязательный набор файлов в исходном шаблоне.

## Применимые уроки

- Перед началом сессии: `LAYER-3/STATE.md` (если есть), `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
