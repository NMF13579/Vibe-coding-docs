# DOCS-MAP — два контура документов

Ниже — spec-driven цепочка: сначала понимаем проблему и процессы (контур 1), затем проектируем, строим, проверяем и выкатываем (контур 2).

**Цепочка во втором контуре (по смыслу):** `processes/*` → потоки в `ux/UX-FLOWS-*.md` → `ux/SCREEN-MAP.md` → внутреннее описание экранов и блоков в `ux/*` (порядок заполнения — `ux/ATOMIC-DECOMPOSITION.md`; ведёт агент, без отдельного «дизайн-фреймворка» для владельца) → `specs/VALIDATION-RULES.md`, `specs/ACCESS-RULES.md`, `specs/COMPONENT-STATES.md` → `specs/SPEC.md` → задачи в `tasks/` и QA в `qa/*` → деплой.

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
- `ux/ATOMIC-DECOMPOSITION.md`
- `ux/PAGES.md`
- `ux/TEMPLATES.md`
- `ux/ORGANISMS.md`
- `ux/MOLECULES.md`
- `ux/ATOMS.md`
- `ux/WIREFRAMES.md`
- `ux/UI-CHECKLIST.md`
- `ux/UX-GAP-REPORT.md`

---

## UX-стандарты и чеклисты

> Библиотека готовых чеклистов. Точка входа: `docs/standards/UX-CHECKLIST-INDEX.md`
> Агент использует при команде «Проверить UX».

| Файл | Когда использовать |
|------|--------------------|
| `docs/standards/UX-CHECKLIST-INDEX.md` | Всегда — навигация по всем чеклистам |
| `docs/standards/UX-CHECKLIST-DEFAULT.md` | Основная проверка любого интерфейса |
| `docs/standards/UX-CHECKLIST-MEDICAL.md` | Медицинские приложения |
| `docs/standards/UX-CHECKLIST-MOBILE.md` | Мобильный интерфейс |
| `docs/standards/UX-CHECKLIST-ACCESSIBILITY.md` | Доступность |
| `docs/standards/UX-PRESET-MODES.md` | Пресеты UX-режимов |

---

- `specs/VALIDATION-RULES.md`
- `specs/ACCESS-RULES.md`
- `specs/COMPONENT-STATES.md`
- `specs/SPEC.md`
- `specs/ARCHITECTURE.md`
- `specs/DECISIONS.md`
- `qa/TEST-SCENARIOS.md`
- `qa/RELEASE-BLOCKERS.md`

---

## Пользовательские сценарии

| Файл | Назначение |
|------|------------|
| `docs/USER-FLOWS.md` | Готовые сценарии тестирования: авторизация, CRUD, навигация, smoke-тест перед релизом |
| `docs/OWNER-CHEATSHEET.md` | Команды и подсказки для владельца проекта |
| `docs/cheatsheet.html` | Визуальная шпаргалка по процессу |

---

- `deploy/DEPLOY-CHECKLIST.md`
- `deploy/RELEASE-NOTES.md`
- `deploy/RUNBOOK.md`
- `docs/POST-LAUNCH-REVIEW.md`

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
| `ux/ATOMIC-DECOMPOSITION.md` | 2 | Связка процесс → экраны → блоки → спека (внутренний порядок для агента) |
| `ux/PAGES.md` | 2 | Экраны целиком, связь с картой и потоками |
| `ux/TEMPLATES.md` | 2 | Повторяемые раскладки экранов |
| `ux/ORGANISMS.md` | 2 | Крупные блоки интерфейса на экране |
| `ux/MOLECULES.md` | 2 | Малые составные блоки |
| `ux/ATOMS.md` | 2 | Мельчайшие повторяемые элементы UI |
| `ux/WIREFRAMES.md` | 2 | Схемы экранов (текстом или ссылками) |
| `ux/UI-CHECKLIST.md` | 2 | Проверка UX против процессов |
| `ux/UX-GAP-REPORT.md` | 2 | Пробелы между процессом и экранами |
| `specs/VALIDATION-RULES.md` | 2 | Правила проверки ввода и сообщения пользователю |
| `specs/ACCESS-RULES.md` | 2 | Кто что видит и что может (согласовать с ролями из процессов) |
| `specs/COMPONENT-STATES.md` | 2 | Состояния интерфейса: загрузка, пусто, ошибка и т.д. |
| `specs/SPEC.md` | 2 | Требования к продукту |
| `specs/ARCHITECTURE.md` | 2 | Устройство системы |
| `specs/DECISIONS.md` | 2 | Зафиксированные решения |
| `qa/TEST-SCENARIOS.md` | 2 | Сценарии проверки |
| `qa/RELEASE-BLOCKERS.md` | 2 | Критичные стопоры перед релизом |
| `docs/AGENTS.md` | 2 | Карта ролей агентов и правила многоагентной работы |
| `docs/ENV.md` | 2 | Описание переменных окружения и правила хранения секретов |
| `docs/MONITORING.md` | 2 | Базовый мониторинг после релиза и сигналы для отката |
| `docs/AUDIT-CHECKLIST.md` | 2 | Расширенный чеклист проверки качества и готовности |
| `docs/USER-FLOWS.md` | 2 | Ключевые пользовательские сценарии для smoke-теста |
| `deploy/DEPLOY-CHECKLIST.md` | 2 | Контроль перед выкладкой |
| `deploy/RELEASE-NOTES.md` | 2 | Содержание версии для людей |
| `deploy/RUNBOOK.md` | 2 | Эксплуатация и типовые сбои |
| `docs/POST-LAUNCH-REVIEW.md` | 2 | Разбор после запуска и фактов использования |
| `docs/ORPHAN-FILES-REPORT.md` | 2 | Отчёт о файлах без ссылок в навигации |

## Связь с Vibe-coding-docs

Папки `discovery` … `deploy` и этот файл — ваша **spec-driven** цепочка под продукт; общие правила шаблона (старт сессии, интервью, дорожная карта, аудит) по-прежнему живут в корне репозитория и в `docs/*` вроде `START.md`, `WORKFLOW.md`, `PM-DIALOG-STYLE.md` — они дополняют эти документы, но не заменяют их.
При UX-работе смотри также: `memory-bank/open-ui-questions.md`, `memory-bank/ui-inventory.md`, `memory-bank/atomic-decisions.md`, `memory-bank/PROJECT-MEMORY.md`.

**Деплой — смежная цепочка (онбординг и MCP):** `docs/deploy/SETUP-ALL.md` → `ENV-SETUP.md` / `MCP-SETUP.md` → `DEPLOY-MCP-UNIVERSAL.md` → `DEPLOY-TIMEWEB.md`; универсальные правила — `docs/DEPLOY.md`.

**Выбор платформы деплоя:**

| Платформа | Файл | Когда использовать |
|-----------|------|--------------------|
| Timeweb Cloud | `docs/platforms/timeweb-cloud.md` | VPS, App Platform в России |
| Vercel | `docs/platforms/vercel.md` | Фронтенд, Next.js, быстрый старт |

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
