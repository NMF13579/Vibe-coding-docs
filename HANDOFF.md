# HANDOFF — где мы остановились

## Project Name

<!--VIBE_DOCS_PROJECT_NAME-->

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.
> Агент обновляет этот файл после каждой сессии.

## Что мы делали в последний раз

Патч **«Этап 5 — финальная валидация и релиз v1.1.0»**:

- Проведена сквозная проверка ссылок и терминологии в ключевых релизных документах.
- Обновлены `CHECKLIST.md` и `LAYER-1/audit-checklist.md` под критерии Этапов 1–4 и финальную релиз-валидацию.
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

- Обновлён `LAYER-1/ux-checklist-medical.md`: убраны дубли с core, усилена клиническая специфика, добавлена секция `⚕️ Клинические сценарии`, усилены ссылки на `LEGAL-152FZ.md`.
- Обновлён `LAYER-1/interview-system.md`: добавлен медицинский блок интервью (тип данных, МИС/ЕГИСЗ, клинрекомендации, ответственное лицо) и авто-правило ` [РИСК: HIGH] + 152-ФЗ`.
- Обновлён `LAYER-1/anti-patterns.md`: добавлена секция процессуальных/коммуникационных анти-паттернов для vibe-coding с последствиями и привязкой к протоколам.
- Обновлён `LAYER-1/decision-guide.md`: добавлены встроенные определения терминов, матрица решений, развёрнутые медицинские сценарии и fallback-блок `🆘 Если не уверен`.
- Проверены устаревшие доменные пути по репозиторию — отсутствуют.

Патч **«Этап 2 — отказоустойчивость и риск-контур»**:

- Создан `LAYER-1/ROLLBACK.md` с GUI-совместимым протоколом отката (Stop/`/cancel`, фиксация, возврат через Git/UI, логирование, перезапуск).
- Обновлён `LAYER-1/error-handling.md`: добавлено реактивное дерево решений и явная граница с `self-verification.md`; для неустранимых/повторяющихся сбоев — обязательный `ROLLBACK.md`.
- Обновлён `LAYER-1/audit.md`: обязательная фиксация каждого отката (причина, объект отката, принятое решение).
- Обновлён `LAYER-1/scope-guard.md`: добавлена процедура реакции на выход за границы и примеры IN SCOPE vs OUT OF SCOPE.
- Обновлён `LAYER-1/agent-contract.md`: обязательная остановка при несоответствии контракту, ссылки на `scope-guard.md` и `ROLLBACK.md`.
- Обновлён `LAYER-1/task-protocol.md`: введены теги риска `[РИСК: HIGH/MEDIUM/LOW]` и привязка уровня проверок.
- Обновлён `LAYER-1/audit-checklist.md`: добавлен раздел «📊 Аудит по уровням риска».
- Обновлён `LAYER-1/self-verification.md`: усилен превентивный фокус (до выполнения/до коммита), добавлены критерии и граница с error-handling.

Патч **«Этап 1 — входная точка, 152-ФЗ, prompt-security, унификация роли»**:

- Создан `ADVANCED-SETUP.md` как техническое приложение (.claude/.cursor, LLM, CLI, MCP).
- Переписан `QUICK-START.md` на GUI-first запуск без терминала.
- Обновлён `README.md`: GUI quick start и навигация на `ADVANCED-SETUP.md`, `LAYER-1/LEGAL-152FZ.md`, `LAYER-1/PROMPT-SECURITY.md`.
- `CLAUDE.md` сокращён до манифеста правил, дубли настройки убраны, добавлена ссылка на `ADVANCED-SETUP.md`.
- Созданы `LAYER-1/LEGAL-152FZ.md` и `LAYER-1/PROMPT-SECURITY.md`.
- Обновлён `LAYER-1/ux-checklist-medical.md`: медицинская специфика без дублирования core + секция «⚖️ Комплаенс 152-ФЗ».
- Обновлён `LAYER-1/security.md`: раздел «🛡️ Защита от Prompt Injection», least privilege и защита от privilege escalation.
- Обновлён `LAYER-1/system-prompt.md`: единая роль и 4 фазы выполнения.
- Обновлён `LAYER-1/agent-contract.md`: синхронизация обязательств и human-in-the-loop дисклеймер.

Патч **«Итерация 3 — Опыт и масштабирование»**:

- `LAYER-1/audit-checklist.md` — деградация документов (Процесс, Навигация), **Направление 7 — Свежесть документов**, строка в HEALTH-SCORE; чеклист направлений переименован в **семь**.
- `LAYER-1/dialog-style.md` — медицинский домен (принципы, примеры, формула стопа) и блок **Before/After** (сценарии A/B/C).
- `LAYER-1/tools/deploy/ROLLBACK-PROTOCOL-POST-DEPLOY.md` — протокол отката после неудачного деплоя в проде.
- `llms.txt` — маршрут на новый rollback-файл.
- `LAYER-1/deploy-guide.md` — раздел «Откат после неудачного деплоя» со ссылкой на протокол.
- `LAYER-1/tools/template-sync-index.md` — строка для rollback-протокола; описание audit-checklist уточнено (7 направлений).
- `LAYER-1/decision-guide.md` — развилки **15–17** (мульти-агент, переход уровней, дробление задач).

Ранее: итерации 1–2 (priority-order, конфликт задач, SEMANTIC ERROR, AI-security, медразвилки 11–14, bootstrap complete, медблок интервью, ai-failure-modes).

## Где мы остановились

Этап 5 закрыт для **исходного шаблона**: выполнена финальная валидация каркаса, синхронизация маршрутов и подготовка релизного комплекта `v1.1.0`.
Пустые product-record файлы (`LAYER-2/*`, `LAYER-3/*`, `project/PROJECT.md`) в исходнике считаются нормой до копирования в конкретный проект.

2026-04-16 — Исправлены внутренние ссылки по репозиторию (автопроверка markdown: **0** битых целей). Добавлен корневой [`GEMINI.md`](./GEMINI.md). Выровнены относительные пути в адаптерах интервью, деплой-файлах в `LAYER-1/tools/deploy/`, [`LAYER-1/interview-system.md`](./LAYER-1/interview-system.md), [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md), примерах в `tasks/`.

2026-04-16 — Проверка на остаточные **конфликты инструкций**: уточнён блок «что читать» в [`START.md`](./START.md); выровнен порядок чтения в [`.cursor/rules/00-core.mdc`](./.cursor/rules/00-core.mdc) и точка входа в [`.cursor/rules/10-communication.mdc`](./.cursor/rules/10-communication.mdc) с `START.md` + `llms.txt`; приоритет в [`LAYER-1/agent-contract.md`](./LAYER-1/agent-contract.md) явно отсылает к [`shared/priority-order.md`](./shared/priority-order.md).

2026-04-16 — **Минимальная стабилизация шаблона:** закреплён [`AUDIT-REPORT-DEV.md`](./AUDIT-REPORT-DEV.md); выровнен [`.cursor/rules/32-document-priority.mdc`](./.cursor/rules/32-document-priority.mdc) с [`shared/priority-order.md`](./shared/priority-order.md); поля `Next` и отсылки в ключевых файлах `LAYER-2/` приведены к реальным путям; в [`llms.txt`](./llms.txt) добавлен маршрут на отчёт dev.

2026-04-16 — **Уборка остаточного шума:** [`.cursor/rules/50-doc-priority.mdc`](./.cursor/rules/50-doc-priority.mdc) приведён к канону [`shared/priority-order.md`](./shared/priority-order.md); устаревшие имена файлов вычищены в [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md), [`LAYER-1/interview-system.md`](./LAYER-1/interview-system.md), [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md), точечно в [`LAYER-1/workflow.md`](./LAYER-1/workflow.md), [`LAYER-1/agent-contract.md`](./LAYER-1/agent-contract.md), [`LAYER-1/dialog-style.md`](./LAYER-1/dialog-style.md); сжаты пересечения в [`LAYER-1/audit-checklist.md`](./LAYER-1/audit-checklist.md); обновлена шапка и пример поиска в [`llms.txt`](./llms.txt).

2026-04-16 — **Финальная выверка маршрутов:** обновлены [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) (терминология `interview-summary.md`); [`LAYER-1/levels-guide.md`](./LAYER-1/levels-guide.md) приведён к реальным путям шаблона (`discovery/`, `ux/`, `specs/decisions.md`); в [`LAYER-2/discovery/mvp-scope.md`](./LAYER-2/discovery/mvp-scope.md) и [`LAYER-2/qa/post-launch-review.md`](./LAYER-2/qa/post-launch-review.md) выровнены текстовые отсылки на `vision.md` / `mvp-scope.md`.

## Следующий лучший шаг

- Выполнить по согласованию владельца шаги из [`tasks/TASK-001-CONFIRMATION-INTERVIEW.md`](./tasks/TASK-001-CONFIRMATION-INTERVIEW.md) (stop-point и Confirmation в `project-interview.md`), если это ещё не сделано в копии проекта.
- При следующем крупном изменении структуры — повторить скан внутренних ссылок и обновить счётчики в шапке [`llms.txt`](./llms.txt).
- По желанию: пройтись `rg` по репо на остаточные имена в ВЕРХНЕМ регистре в тексте (кроме истории в `CHANGELOG` / `project/archive/`).

## Риски и вопросы

- В [`LAYER-1/workflow.md`](./LAYER-1/workflow.md) по-прежнему описаны опциональные артефакты (`data-models` и др.) как шаги углублённого контура — это сценарий «создать по мере надобности», не обязательный набор файлов в исходном шаблоне.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
