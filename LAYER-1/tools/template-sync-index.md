> Trigger: Справочник инструмента синхронизации шаблонов (не маршрут агента)
> Read-time: ~30 min
> Filled-by: both
> Needs-approval: no
> Location: LAYER-1/tools/template-sync-index.md

# TEMPLATE SYNC — Индекс инструмента

> ⚠️ **Это не общий индекс репозитория.**
> Этот файл — индекс инструмента синхронизации шаблонов (template-sync).
> Навигацию по документации смотри в `README.md`, `llms.txt` или `LAYER-1/workflow.md`.
>
> **Статус доп. документации:**
> `template-sync.md` и `template-sync.md (раздел «Интеграция с агентами»)` — **не созданы** (запланированы).
> До их создания используй `LAYER-1/tools/template-sync.md` как основную документацию.

# 📚 TEMPLATE SYNC TOOLSET — Полный индекс

> **Начни отсюда.** Этот файл объясняет какие файлы нужны и в каком порядке их использовать.

---

## 🎯 Что ты хочешь сделать?

### Я новичок и хочу просто добавить файлы из шаблона

**Файлы которые нужны:**
1. **setup.js** — интерактивный мастер
2. **QUICK-START.md** — инструкция

**Процесс:** 3 минуты
```bash
node setup.js
```
**Готово!** ✨

---

### Я уже использовал setup.js и хочу синхронизировать заново

**Команда:**
```bash
npm run sync-template:check    # проверить что будет
npm run sync-template          # выполнить
```

**Документация:** template-sync.md раздел "Использование"

---

### Я разработчик и хочу понять как это работает

**Файлы в порядке чтения:**
1. **QUICK-START.md** (5 минут) — Общее описание
2. **template-sync.md** (15 минут) — Архитектура инструмента
3. **template-sync.js** — Исходный код (350 строк)

---

### Я использую Claude Code / Cursor / агента

**Файл:** template-sync.md (раздел «Интеграция с агентами»)

**Что там:**
- Как агент должен использовать инструмент
- 4 сценария
- Как интегрировать в CLAUDE.md

---

## 📁 Все файлы в этом пакете

### ✅ Основные файлы (НУЖНЫ)

| Файл | Размер | Для кого | Что делает |
|------|--------|----------|-----------|
| **setup.js** | 8 KB | Все | Интерактивный мастер - спрашивает вопросы и делает всё сам |
| **template-sync.js** | 7.6 KB | Все | Основной инструмент синхронизации (запускается через setup.js) |

### 📖 Документация (ЧИТАЙ В ЭТОМ ПОРЯДКЕ)

| Файл | Длина | Для кого | Когда читать |
|------|-------|----------|--------------|
| **QUICK-START.md** | 2 мин | Все | Если ты спешишь |
| **template-sync.md** | 10 мин | Пользователи | Полная инструкция с примерами |
| **template-sync.md (раздел «Интеграция с агентами»)** | 15 мин | Агенты (Claude Code) | Как агент должен использовать |

---

## 🚀 Рекомендуемый путь использования

### День 1: Первая синхронизация

```bash
# Шаг 1: Скопировать файлы в проект
cp setup.js template-sync.js /path/to/my-project/

# Шаг 2: Запустить мастер
cd /path/to/my-project
node setup.js

# Готово! 🎉
```

**Время:** 2-3 минуты
**Результат:** Проект синхронизирован с Vibe Docs

---

### День 2 и позже: Повторная синхронизация

```bash
npm run sync-template:check    # Проверить
npm run sync-template          # Выполнить
```

**Время:** 30 секунд

---

### Когда нужна помощь

**Быстрая помощь:** QUICK-START.md
**Подробная документация:** template-sync.md
**Работа с агентом:** template-sync.md (раздел «Интеграция с агентами»)
**Техническое понимание:** template-sync.md

---

## 📋 Что нужно установить

### Минимум

- **Node.js 14+** (скачать: https://nodejs.org)

Проверить:
```bash
node --version
```

### Опционально

- **Git** (для коммитов)
- **npm** или **yarn** (обычно идёт с Node.js)

---

## 🎯 Главное правило

> **При первом запуске всегда используй `node setup.js`**

Это интерактивный мастер который:
- Проверит что нужно
- Спросит 2 вопроса
- Сделает всё остальное сам

Не нужно помнить команды и флаги.

---

## ❓ Частые вопросы

**В: С какого файла начать?**
О: Если ты новичок → `node setup.js`
О: Если хочешь читать → QUICK-START.md

**В: Какие файлы скопировать в проект?**
О: Только `setup.js` и `template-sync.js`
О: Остальные — документация для чтения

**В: Нужны ли все эти документы?**
О: Нет. Достаточно QUICK-START.md
О: Остальные — для понимания и справки

**В: Где найти примеры?**
О: template-sync.md раздел "Примеры использования"

**В: Что если что-то сломается?**
О: `git reset --hard HEAD~1` откатит изменения

---

## 🎓 Полный путь обучения

### Уровень 0 — Абсолютный новичок (5 мин)
```
QUICK-START.md → node setup.js → готово ✓
```

### Уровень 1 — Пользователь (15 мин)
```
QUICK-START.md → template-sync.md → использование ✓
```

### Уровень 2 — Разработчик (30 мин)
```
Все документы → template-sync.md → модификация скрипта ✓
```

### Уровень 3 — Агент/CI (20 мин)
```
template-sync.md (раздел «Интеграция с агентами») → интеграция в CI/CD ✓
```

---

## 🔗 Связи между файлами

```
setup.js (интерактивный мастер)
    ↓ запускает
    └→ template-sync.js (инструмент синхронизации)

INDEX.md (ты здесь)
    ├→ QUICK-START.md (2 минуты)
    ├→ template-sync.md (10 минут)
    ├→ template-sync.md (раздел «Интеграция с агентами») (для агентов)
    └→ template-sync.md (для разработчиков — подробное описание)
```

---

## ✨ Итого

**Для первого запуска:**
- Скопировать: `setup.js` + `template-sync.js`
- Запустить: `node setup.js`
- Время: 2-3 минуты

**Для повторных запусков:**
- Команда: `npm run sync-template:check` → `npm run sync-template`
- Время: 30 секунд

**Для понимания:**
- Читать: QUICK-START.md + template-sync.md
- Время: 15 минут

**Для агентов:**
- Читать: template-sync.md (раздел «Интеграция с агентами»)
- Время: 10 минут

---

## 🚀 Начни прямо сейчас

```bash
node setup.js
```

Вопросы в пути, ответы в конце. **Очень просто.**

---

**Версия:** 1.0.0  
**Обновлено:** 2026-04-03  
**Статус:** ✅ Готово к использованию


---

# DOCS-MAP

# DOCS-MAP — как устроены документы проекта

> Этот файл — **центральная карта**.  
> Отвечает на вопросы: *где читать инструкции*, *где заполнять данные проекта*, *в каком порядке двигаться*.

---

## 1. Типы документов

Каждый файл в этом репо относится к одному из трёх типов:

- **Instruction** — постоянные правила и подходы.
  - Пишется один раз автором репо.
  - Не редактируется под конкретный продукт.
  - Примеры: `WORKFLOW.md`, `FEATURE-RADAR.md`, UX-чеклисты.

- **Template** — шаблон/каркас для проекта.
  - Определяет, *что именно* надо собрать.
  - Агент может копировать структуру, но не должен превращать этот файл в проектный черновик.
  - Примеры: `LAYER-2/specs/architecture.md`, `LAYER-2/specs/decisions.md`, `LAYER-1/deploy-guide.md`.

- **Project record** — живые документы проекта.
  - Заполняются для конкретного продукта.
  - Должны отражать текущую реальность, а не намерения.
  - Примеры: файлы в `LAYER-2/specs/`, `LAYER-2/discovery/`, `LAYER-2/ux/`, `LAYER-2/qa/`, `LAYER-3/`.

Для удобства в начале каждого важного файла рекомендуется явно указывать:

```markdown
> Role: instruction / template / project-record  
> Filled by: agent / user / both  
> Needs approval: yes / no  
> Next: [следующий документ/этап]
```

---

## 2. Общий маршрут заполнения

Маршрут построен по слоям — от смысла к реализации:

### 1. Discovery (`LAYER-2/discovery/`)

- `VISION.md` — зачем этот проект.
- `MVP-SCOPE.md` — что входит в первую версию, что сознательно откладываем.
- `HYPOTHESIS-RESEARCH.md` — есть ли смысл делать продукт (рынок, конкуренты, незакрытая боль).
- `INTERVIEW-SUMMARY.md` — итог разговора с заказчиком/пользователем.
- `USER-PROFILE.md` — кто реальный пользователь.

**Правило:**
- Исследование может инициировать пользователь или агент.
- Если фактов не хватает — агент формулирует запросы/бриф для внешнего поиска, а не придумывает рынок.
- `INTERVIEW-SUMMARY.md` заполняется агентом, **затем обязательно показывается пользователю**.
- Только после явного согласия пользователя этот файл считается подтверждённым.

**Процедура подтверждения интервью (`PROJECT-INTERVIEW.md` → секция Confirmation):**
- После Этапа 5 агент **останавливается** (STOP-блок) и показывает саммари — не фиксирует файл без ответа.
- Агент задаёт вопрос подтверждения и ждёт ответа:
  - **«Да»** → статус `accepted`, поле `Approved by` заполняется, файл считается источником истины.
  - **«Нет / правки»** → агент принимает корректировки и повторяет саммари для повторного подтверждения.
- Статус `accepted` и поле `Approved by` отражаются в `PROJECT-STATUS.md` (колонка **Approved by**, таблица Discovery) и в `HEALTH-SCORE.md` (светофор: `accepted` → 🟢).

### 2. Specs (`LAYER-2/specs/`)

- `ARCHITECTURE.md` — архитектура именно этого проекта (стек, сущности, потоки).
- `DECISIONS.md` — журнал ключевых решений.
- `SPEC.md` — спецификация фич/модулей.
- `ACCESS-RULES.md` — правила доступа и роли.
- `COMPONENT-STATES.md`, `VALIDATION-RULES.md` — состояния и валидация.

**Правило:**
- Эти файлы заполняются **после** того, как согласованы discovery-документы.
- Агент предлагает вариант, пользователь подтверждает или правит.
- Любое решение, влияющее на архитектуру/данные/безопасность, дублируется в `DECISIONS.md`.

### 3. UX (`LAYER-2/ux/` и `LAYER-1/ux-checklist-*.md`)

- `SCREEN-MAP.md` — карта экранов и переходов.
- `PAGES.md`, `ATOMS.md`, `MOLECULES.md`, `ORGANISMS.md`, `TEMPLATES.md` — реестр UI.
- `UX-FLOWS-*.md` — пользовательские сценарии.
- UX-чеклисты (instruction) — в `LAYER-1/ux-checklist-core.md`, `ux-checklist-accessibility.md`, `ux-checklist-medical.md`, `ux-checklist-interactions.md`; не заполняются данными проекта как ТЗ.

**Правило:**
- Сначала `PAGES.md` и `SCREEN-MAP.md`, затем детализация по атомам/модулям.
- UX-файлы отражают **фактический** интерфейс, а не только планы.

### 4. QA и релиз (`LAYER-2/qa/`, `LAYER-1/tools/deploy/`)

- `TEST-SCENARIOS.md` — как и что проверяем.
- `RELEASE-BLOCKERS.md` — список стопорящих багов.
- `LAYER-1/tools/deploy/DEPLOY-*.md`, `RUNBOOK.md`, `RELEASE-NOTES.md` — сценарии выкладки и истории релизов.

**Правило:**
- `TEST-SCENARIOS.md` и `RELEASE-BLOCKERS.md` заполняются на основе уже согласованных specs и UX.
- `RUNBOOK.md` — конкретные операционные шаги, как действовать в жизни.

### 5. Мониторинг состояния (`HEALTH-SCORE.md`, `FEATURE-RADAR.md`, `LAYER-3/`)

- `HEALTH-SCORE.md` — светофор состояния слоёв проекта.
- `FEATURE-RADAR.md` — что уместно предлагать на текущем этапе.
- `LAYER-3/*` — оперативная память проекта для агента.

**Правило:**
- Эти файлы можно пересматривать по мере изменения проекта, они не фиксируются "раз и навсегда".

---

## 3. Кто за что отвечает

- **Пользователь (владелец проекта):**
  - подтверждает `INTERVIEW-SUMMARY.md`;
  - согласует `VISION`, `MVP-SCOPE`, ключевые архитектурные решения;
  - может исправлять любые project-record файлы.

- **Агент:**
  - предлагает структуру и черновики на основе шаблонов;
  - формирует брифы для исследования, если данных не хватает;
  - не считает документ "истиной", пока пользователь явно не согласился.

- **Исследование (интернет/другие источники):**
  - попадает в `HYPOTHESIS-RESEARCH.md` и частично в specs;
  - всегда отделяется от личного опыта пользователя.

---

## 4. Прогресс и статусы

Для ощущения прогресса агент использует шкалу для каждого ключевого файла:

- `not-started` — файл существует, но не заполнен;
- `draft` — есть черновик от агента;
- `pending-approval` — черновик показан пользователю, ждём подтверждения;
- `accepted` — пользователь согласен, файл считается источником истины;
- `outdated` — устарело после изменений стратегии/объёма.

Статус указывается в шапке самого файла (`> Status: draft`) или сводится в `HEALTH-SCORE.md`.

---

## 5. Вспомогательные файлы (instruction — только для чтения)

Эти файлы — постоянные инструкции для агента. Не редактируются под конкретный продукт.  
Агент читает их при необходимости, не при каждом шаге.

| Файл | Тип | Когда читать |
|------|-----|-------------|
| `LAYER-1/agent-bootstrap.md` | instruction | При старте новой сессии или потере контекста — **читать первым** |
| `LAYER-1/context-recovery.md` | instruction | При симптомах потери контекста агентом |
| `LAYER-1/anti-patterns.md` | instruction | При сомнении в выборе подхода — чего не делать |
| `LAYER-1/decision-guide.md` | instruction | При архитектурных развилках — что выбрать и почему |
| `LAYER-1/glossary.md` | instruction | При непонимании терминов проекта |
| `LAYER-1/stack-presets.md` | instruction | При выборе технологического стека |
| `LAYER-1/dialog-style.md` | instruction | При ведении диалога с владельцем проекта |
| `LAYER-1/task-protocol.md` | template | При создании задач |
| `LAYER-1/task-protocol.md` | instruction | При проверке выполненных задач перед закрытием |
| `LAYER-1/testing-guide.md` | instruction | При написании тестов и проверке после задачи |
| `LAYER-2/specs/validation.md` | instruction | При написании правил валидации |
| `LAYER-1/error-handling.md` | instruction | При классификации ошибок: тип → действие |
| `LAYER-1/error-handling.md` | instruction | При откате релиза («всё сломалось») |
| `LAYER-1/task-protocol.md` | instruction | Перед каждым релизом |
| `LAYER-1/security.md` | instruction | При работе с персональными данными и доступами |
| `LAYER-2/specs/roadmap.md` | project-record | После принятия MVP-решений — дорожная карта |
| `LAYER-1/audit.md` | instruction | При проведении аудита проекта |
| `LAYER-1/audit.md` | instruction | Расширенный чеклист качества и готовности |
| `LAYER-1/tools/adapters/` | instruction | При работе в Cursor / Copilot / Claude / Gemini — IDE-специфичный self-check |

---

***

Ниже — spec-driven цепочка: сначала понимаем проблему и процессы (контур 1), затем проектируем, строим, проверяем и выкатываем (контур 2).

**Цепочка во втором контуре (по смыслу):** `processes/*` → потоки в `ux/UX-FLOWS-*.md` → `ux/SCREEN-MAP.md` → внутреннее описание экранов и блоков в `ux/*` (порядок заполнения — `ux/ATOMIC-DECOMPOSITION.md`; ведёт агент, без отдельного «дизайн-фреймворка» для владельца) → `specs/VALIDATION-RULES.md`, `specs/ACCESS-RULES.md`, `specs/COMPONENT-STATES.md` → `specs/SPEC.md` → задачи в `tasks/` и QA в `qa/*` → деплой.

---

## Контур 1 — Discovery и решение проблемы

- `discovery/USER-PROFILE.md`
- `discovery/VISION.md`
- `discovery/HYPOTHESIS-RESEARCH.md`
- `discovery/INTERVIEW-SUMMARY.md`
- `discovery/MVP-SCOPE.md`
- `LAYER-2/discovery/processes.md`, `LAYER-2/discovery/roles.md`

### Стартовое интервью и кросс-IDE контроль (до заполнения discovery)

| Артефакт | Назначение |
|----------|------------|
| [`PROJECT-INTERVIEW.md`](PROJECT-INTERVIEW.md) | Маршрут вопросов и этапов интервью |
| [`LAYER-1/interview-system.md`](../LAYER-1/interview-system.md) | Единый чеклист стража (7 пунктов); **stop-block** при критическом ❌ |
| [`adapters/README.md`](adapters/README.md) | Индекс адаптеров: self-check в Cursor / Copilot / Claude / Gemini |
| `adapters/CURSOR-INTERVIEW-CONTROL.md` и др. | Обязательный формат ответа и self-check без subagent |
| `LAYER-3/interview-session.md` | **Сырой журнал** ответов по шагам (канон для черновика интервью); поле `control-mode` |
| `LAYER-3/project-context-draft.md` | Устаревшее имя — редирект на `interview-session.md` |
| Корень: `llms.txt`, `LAYER-1/agent-contract.md`, `LAYER-1/interview-system.md`, `opencode.json`, `LAYER-1/navigation.md` | Вход, контракт, OpenCode (опционально), карта размещения |

**Режимы контроля:** **OpenCode** — отдельный агент `guardian` или `@guardian`. **Остальные IDE** — тот же чеклист как **self-check** в каждом ответе интервьюера (см. `LAYER-1/tools/adapters/*`).

**Поток данных:** сырой лог в `interview-session.md` → после подтверждения резюме (см. `PROJECT-INTERVIEW.md`) → структурированные файлы **контура 1** (`discovery/USER-PROFILE.md`, `discovery/VISION.md`, `discovery/INTERVIEW-SUMMARY.md` и т.д.).  
`discovery/INTERVIEW-SUMMARY.md` — это **итог/выжимка** для цепочки discovery, а не замена журналу `interview-session.md`.

---

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

> Библиотека готовых чеклистов. Точки входа: `LAYER-1/ux-checklist-core.md`, `ux-checklist-accessibility.md`, `ux-checklist-medical.md`, `ux-checklist-interactions.md` (оглавление — в последнем, раздел INDEX).  
> Агент использует при команде «Проверить UX».

| Файл | Когда использовать |
|------|-------------------|
| `LAYER-1/ux-checklist-core.md` | Базовые стандарты, легенда, fallback, MINIMAL |
| `LAYER-1/ux-checklist-accessibility.md` | Доступность, мобильный UX, empty states, онбординг |
| `LAYER-1/ux-checklist-medical.md` | Медицина, роли, права, дашборды |
| `LAYER-1/ux-checklist-interactions.md` | Уведомления, таблицы, поиск, история, микротекст, INDEX |

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
| `LAYER-2/ux/user-flows.md` | Готовые сценарии тестирования: авторизация, CRUD, навигация, smoke-тест перед релизом |
| `LAYER-1/owner.md` | Команды и подсказки для владельца проекта |
| `FAQ.md` | Частые ситуации для владельца |

---

- `deploy/DEPLOY-CHECKLIST.md`
- `deploy/RELEASE-NOTES.md`
- `deploy/RUNBOOK.md`
- `LAYER-2/qa/post-launch-review.md`

> см. `LAYER-2/qa/post-launch-review.md`

---

## Таблица: файл → контур → тип → зачем

| Файл | Контур | Тип | Для чего |
|------|--------|-----|----------|
| `LAYER-3/interview-session.md` | 1 (черновик) | project-record | Пошаговый журнал интервью до переноса в discovery |
| `discovery/USER-PROFILE.md` | 1 | project-record | Подстроить вопросы и язык под владельца |
| `discovery/VISION.md` | 1 | project-record | Идея, аудитория, боль, критерий успеха |
| `discovery/HYPOTHESIS-RESEARCH.md` | 1 | project-record | Проверка, стоит ли делать продукт |
| `discovery/INTERVIEW-SUMMARY.md` | 1 | project-record | Итог разговора: сроки, риски, чувствительные данные |
| `discovery/MVP-SCOPE.md` | 1 | project-record | Что в первой версии, что отложено |
| `LAYER-2/discovery/processes.md` | 1 | project-record | Как устроена работа шаг за шагом |
| `LAYER-2/discovery/roles.md` | 1 | project-record | Роли участников продукта |
| `ux/UX-DESIGN-GUIDE.md` | 2 | instruction | Общие правила интерфейса |
| `ux/UX-FLOWS-DESKTOP.md` | 2 | project-record | Сценарии на компьютере |
| `ux/UX-FLOWS-MOBILE.md` | 2 | project-record | Сценарии на телефоне |
| `ux/SCREEN-MAP.md` | 2 | project-record | Карта экранов и переходов |
| `ux/ATOMIC-DECOMPOSITION.md` | 2 | instruction | Связка процесс → экраны → блоки → спека (внутренний порядок для агента) |
| `ux/PAGES.md` | 2 | project-record | Экраны целиком, связь с картой и потоками |
| `ux/TEMPLATES.md` | 2 | project-record | Повторяемые раскладки экранов |
| `ux/ORGANISMS.md` | 2 | project-record | Крупные блоки интерфейса на экране |
| `ux/MOLECULES.md` | 2 | project-record | Малые составные блоки |
| `ux/ATOMS.md` | 2 | project-record | Мельчайшие повторяемые элементы UI |
| `ux/WIREFRAMES.md` | 2 | project-record | Схемы экранов (текстом или ссылками) |
| `ux/UI-CHECKLIST.md` | 2 | instruction | Проверка UX против процессов |
| `ux/UX-GAP-REPORT.md` | 2 | project-record | Пробелы между процессом и экранами |
| `specs/VALIDATION-RULES.md` | 2 | project-record | Правила проверки ввода и сообщения пользователю |
| `specs/ACCESS-RULES.md` | 2 | project-record | Кто что видит и что может |
| `specs/COMPONENT-STATES.md` | 2 | project-record | Состояния интерфейса: загрузка, пусто, ошибка и т.д. |
| `specs/SPEC.md` | 2 | project-record | Требования к продукту |
| `specs/ARCHITECTURE.md` | 2 | project-record | Устройство системы |
| `specs/DECISIONS.md` | 2 | project-record | Зафиксированные решения |
| `qa/TEST-SCENARIOS.md` | 2 | project-record | Сценарии проверки |
| `qa/RELEASE-BLOCKERS.md` | 2 | project-record | Критичные стопоры перед релизом |
| `LAYER-1/agents.md` | 2 | instruction | Карта ролей агентов и правила многоагентной работы |
| `LAYER-1/deploy-guide.md` | 2 | project-record | Описание переменных окружения и правила хранения секретов |
| `LAYER-1/deploy-guide.md` | 2 | instruction | Базовый мониторинг после релиза и сигналы для отката |
| `LAYER-1/audit.md` | 2 | instruction | Расширенный чеклист проверки качества и готовности |
| `LAYER-2/ux/user-flows.md` | 2 | instruction | Ключевые пользовательские сценарии для smoke-теста |
| `deploy/DEPLOY-CHECKLIST.md` | 2 | template | Контроль перед выкладкой |
| `deploy/RELEASE-NOTES.md` | 2 | project-record | Содержание версии для людей |
| `deploy/RUNBOOK.md` | 2 | project-record | Эксплуатация и типовые сбои |
| `LAYER-2/qa/post-launch-review.md` | 2 | project-record | Разбор после запуска и фактов использования |
| `LAYER-1/agent-bootstrap.md` | 0 | instruction | Диагностика и старт агента — читать первым |
| `LAYER-1/context-recovery.md` | 0 | instruction | Восстановление после потери контекста |
| `LAYER-1/anti-patterns.md` | 0 | instruction | Чего не делать при выборе решений |
| `LAYER-1/decision-guide.md` | 0 | instruction | Справочник развилок: что выбрать и почему |
| `LAYER-1/glossary.md` | 0 | instruction | Словарь терминов простым языком |
| `LAYER-1/stack-presets.md` | 0 | instruction | Готовые наборы инструментов по типу проекта |
| `LAYER-1/dialog-style.md` | 0 | instruction | Стиль диалога с владельцем |
| `LAYER-1/task-protocol.md` | 0 | template | Шаблон задачи |
| `LAYER-1/task-protocol.md` | 0 | instruction | Протокол проверки перед закрытием задачи |
| `LAYER-1/testing-guide.md` | 0 | instruction | Чеклист проверки после каждой задачи |
| `LAYER-2/specs/validation.md` | 0 | instruction | Объективная проверка: работает / не работает |
| `LAYER-1/error-handling.md` | 0 | instruction | Классификация ошибок: тип → действие |
| `LAYER-1/error-handling.md` | 0 | instruction | Инструкция при «всё сломалось» / «откати» |
| `LAYER-1/task-protocol.md` | 0 | instruction | Чеклист перед каждым релизом |
| `LAYER-1/security.md` | 0 | instruction | Безопасность и работа с чувствительными данными |
| `LAYER-2/specs/roadmap.md` | 0 | project-record | Дорожная карта после принятия MVP-решений |
| `LAYER-1/audit.md` | 0 | instruction | Руководство по проведению аудита |
| `LAYER-1/tools/adapters/` | 0 | instruction | IDE-специфичный self-check для Cursor / Copilot / Claude / Gemini |

> **Контур 0** — базовые инструкции агента, читаются до начала любой работы.

---

## Связь с Vibe-coding-docs

Папки `LAYER-2/discovery` … `LAYER-1/tools/deploy` и этот файл — ваша **spec-driven** цепочка под продукт; общие правила шаблона (старт сессии, интервью, дорожная карта, аудит) живут в корне (`llms.txt`, `HANDOFF.md`) и в `LAYER-1/` (`workflow.md`, `dialog-style.md`, `audit.md` и др.) — они дополняют эти документы, но не заменяют их.  
При UX-работе смотри также: `LAYER-3/open-questions.md`, `LAYER-3/ui-inventory.md`, `LAYER-3/atomic-decisions.md`, `LAYER-3/PROJECT-MEMORY.md`.

**Деплой — смежная цепочка (онбординг и MCP):** `LAYER-1/tools/deploy/SETUP-ALL.md` → `ENV-SETUP.md` / `MCP-SETUP.md` → `DEPLOY-MCP-UNIVERSAL.md` → `DEPLOY-TIMEWEB.md`; универсальные правила — `LAYER-1/deploy-guide.md`.

**Выбор платформы деплоя:**

| Платформа | Файл | Когда использовать |
|-----------|------|-------------------|
| Timeweb Cloud | `LAYER-1/tools/deploy/timeweb-cloud.md` | VPS, App Platform в России |
| Vercel | `LAYER-1/tools/deploy/vercel.md` | Фронтенд, Next.js, быстрый старт |

---

## Куда писать: шаблон или продукт?

| Файл | Для чего |
|------|----------|
| `LAYER-2/specs/decisions.md` | Общие правила и принципы подхода (шаблон) |
| `LAYER-2/specs/architecture.md` | Общая архитектура подхода (шаблон) |
| `LAYER-1/deploy-guide.md` | Общий чеклист деплоя (шаблон) |
| `LAYER-2/specs/DECISIONS.md` | Решения конкретного продукта |
| `LAYER-2/specs/ARCHITECTURE.md` | Архитектура конкретного продукта |
| `LAYER-1/tools/deploy/DEPLOY-CHECKLIST.md` | Чеклист деплоя конкретного продукта |
| `LAYER-2/qa/post-launch-review.md` | Post-launch review конкретного продукта (единственное место) |

> **Правило:** всё, что относится к конкретному MVP — пишем в `LAYER-2/specs/`, `LAYER-1/tools/deploy/`, `LAYER-2/qa/post-launch-review.md`.  
> Корневые файлы `LAYER-2/specs/decisions.md`, `LAYER-2/specs/architecture.md`, `LAYER-1/deploy-guide.md` — это шаблонные заготовки подхода, не трогаем при работе над продуктом.
