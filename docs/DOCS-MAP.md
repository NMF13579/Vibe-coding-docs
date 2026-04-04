# DOCS-MAP — два контура документов

Ниже — spec-driven цепочка: сначала понимаем проблему и процессы (контур 1), затем проектируем, строим, проверяем и выкатываем (контур 2).

## Контур 1 — Discovery и решение проблемы

- `discovery/USER-PROFILE.md`
- `discovery/VISION.md`
- `discovery/HYPOTHESIS-RESEARCH.md`
- `discovery/INTERVIEW-SUMMARY.md`
- `discovery/MVP-SCOPE.md`
- `processes/PROCESSES.md`
- `processes/ROLES.md`

## Контур 2 — Delivery и реализация

- `ux/UX-DESIGN-GUIDE.md`
- `ux/UX-FLOWS-DESKTOP.md`
- `ux/UX-FLOWS-MOBILE.md`
- `ux/SCREEN-MAP.md`
- `ux/UI-CHECKLIST.md`
- `ux/UX-GAP-REPORT.md`
- `specs/SPEC.md`
- `specs/ARCHITECTURE.md`
- `specs/DECISIONS.md`
- `qa/TEST-SCENARIOS.md`
- `qa/RELEASE-BLOCKERS.md`
- `deploy/DEPLOY-CHECKLIST.md`
- `deploy/RELEASE-NOTES.md`
- `deploy/RUNBOOK.md`
- `POST-LAUNCH-REVIEW.md`

> см. `docs/POST-LAUNCH-REVIEW.md`

## Таблица: файл → контур → зачем

| Файл | Контур | Для чего |
|------|--------|----------|
| `discovery/USER-PROFILE.md` | 1 | Подстроить вопросы и язык под владельца |
| `discovery/VISION.md` | 1 | Идея, аудитория, боль, критерий успеха |
| `discovery/HYPOTHESIS-RESEARCH.md` | 1 | Проверка, стоит ли делать продукт |
| `discovery/INTERVIEW-SUMMARY.md` | 1 | Итог разговора: сроки, риски, чувствительные данные |
| `discovery/MVP-SCOPE.md` | 1 | Что в первой версии, что отложено |
| `processes/PROCESSES.md` | 1 | Как устроена работа шаг за шагом |
| `processes/ROLES.md` | 1 | Кто участвует и за что отвечает |
| `ux/UX-DESIGN-GUIDE.md` | 2 | Общие правила интерфейса |
| `ux/UX-FLOWS-DESKTOP.md` | 2 | Сценарии на компьютере |
| `ux/UX-FLOWS-MOBILE.md` | 2 | Сценарии на телефоне |
| `ux/SCREEN-MAP.md` | 2 | Карта экранов и переходов |
| `ux/UI-CHECKLIST.md` | 2 | Проверка UX против процессов |
| `ux/UX-GAP-REPORT.md` | 2 | Пробелы между процессом и экранами |
| `specs/SPEC.md` | 2 | Требования к продукту |
| `specs/ARCHITECTURE.md` | 2 | Устройство системы |
| `specs/DECISIONS.md` | 2 | Зафиксированные решения |
| `qa/TEST-SCENARIOS.md` | 2 | Сценарии проверки |
| `qa/RELEASE-BLOCKERS.md` | 2 | Критичные стопоры перед релизом |
| `deploy/DEPLOY-CHECKLIST.md` | 2 | Контроль перед выкладкой |
| `deploy/RELEASE-NOTES.md` | 2 | Содержание версии для людей |
| `deploy/RUNBOOK.md` | 2 | Эксплуатация и типовые сбои |
| `POST-LAUNCH-REVIEW.md` | 2 | Разбор после запуска и фактов использования |

## Связь с Vibe-coding-docs

Папки `discovery` … `deploy` и этот файл — ваша **spec-driven** цепочка под продукт; общие правила шаблона (старт сессии, интервью, дорожная карта, аудит) по-прежнему живут в корне репозитория и в `docs/*` вроде `START.md`, `WORKFLOW.md`, `PM-DIALOG-STYLE.md` — они дополняют эти документы, но не заменяют их.

**Деплой — смежная цепочка (онбординг и MCP):** `docs/deploy/SETUP-ALL.md` → `ENV-SETUP.md` / `MCP-SETUP.md` → `DEPLOY-MCP-UNIVERSAL.md` → `DEPLOY-TIMEWEB.md`; универсальные правила — `docs/DEPLOY.md`, платформа Timeweb — `docs/platforms/timeweb-cloud.md` (см. также таблицу артефактов в `DEPLOY.md`).

## Куда писать: шаблон или продукт?

| Файл | Для чего |
|---|---|
| `docs/DECISIONS.md` | Общие правила и принципы подхода (шаблон) |
| `docs/ARCHITECTURE.md` | Общая архитектура подхода (шаблон) |
| `docs/DEPLOY-CHECKLIST.md` | Общий чеклист деплоя (шаблон) |
| `docs/specs/DECISIONS.md` | Решения конкретного продукта |
| `docs/specs/ARCHITECTURE.md` | Архитектура конкретного продукта |
| `docs/deploy/DEPLOY-CHECKLIST.md` | Чеклист деплоя конкретного продукта |
| `docs/POST-LAUNCH-REVIEW.md` | Post-launch review конкретного продукта (единственное место) |

> Правило: всё, что относится к конкретному MVP — пишем в `docs/specs/`, `docs/deploy/`, `docs/POST-LAUNCH-REVIEW.md`.
> Корневые файлы `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `docs/DEPLOY-CHECKLIST.md` — это шаблонные заготовки подхода, не трогаем при работе над продуктом.
