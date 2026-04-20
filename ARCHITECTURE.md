# 🏗️ Архитектура фреймворка Vibe-coding-docs

---

## Схема слоёв и уровней

```text
Пользовательские уровни зрелости

Level 0  -> Быстрый старт (минимум документов)
Level 1  -> Стандартный MVP (структурированный процесс)
Level 2  -> Production MVP (расширенный контроль рисков)
Level 3  -> Поддержка и масштабирование

Слои документации

LAYER-1  -> Правила, протоколы, безопасность, поведение агента
LAYER-2  -> Продуктовые материалы: discovery, UX, specs, QA
LAYER-3  -> Память проекта: статус, уроки, инциденты, фиксы
```

---

## Карта папок и артефактов

| Папка / файл | Назначение | Читать новичку? |
|---|---|---|
| `LAYER-1/` | Policy, rules, guides | По маршруту из [`START.md`](./START.md) |
| `LAYER-2/` | Product, UX | По необходимости |
| `LAYER-3/` | State, memory | Только агент |
| `stages/` | Stage flow | По необходимости |
| `shared/` | Shared helpers | По необходимости |
| `tasks/` | Task artifacts | По необходимости |
| `memory-bank/` | Project memory | Только агент |
| `incidents/` | Incident log | По необходимости |

Подробнее о слоях LAYER-*: разделы ниже и [`START.md`](./START.md).

---

## Поток данных и решений

```text
Задача
  ->
Интервью и уточнение контекста
  ->
Контракт и границы (scope/risk)
  ->
Работа агента
  ->
Проверка (self-verification + audit)
  ->
Результат и фиксация контекста
```

## State Control Plane

### Компоненты

| Файл | Роль | Тип |
|---|---|---|
| LAYER-1/event-dictionary.md | Канон имён событий (Project / Session / Task) | Политика |
| LAYER-1/state-transitions.md | Переходы: Domain / Event / Guard / Side effects | Политика |
| LAYER-3/STATE.md | Единственный formal control plane: Project + Session + Task, guards | Формальный state (primary) |
| LAYER-1/agent-rules.md | Поведение после чтения `llms.txt`; `# SESSION LOAD`; State authority | Правила агента |
| HANDOFF.md | Контракт сессии (что сделано, следующий шаг; reference snapshot) | Контекст сессии (secondary) |
| LAYER-1/audit.md | Документный аудит и **State Consistency Audit** + **Document Governance Audit** (правила переходов не дублируются) | Аудит |

### Три домена состояния

Project:  INIT → DISCOVERY → PLANNING → DEVELOPMENT → REVIEW → RELEASE_READY → MAINTENANCE
Session:  BOOTSTRAP → CONTEXT_LOADED → AWAITING_CONFIRMATION → EXECUTING → VERIFYING → HANDOFF
Task:     DRAFT → PLANNED → IN_PROGRESS → REVIEW → DONE
                                ↓               ↓
                             BLOCKED       ROLLED_BACK

---

## Принцип каноничности

**Agent/IDE files are adapters, not policy sources.**

### Роли файлов

| Файл | Роль | Что НЕ должно быть |
|---|---|---|
| llms.txt | Navigation layer | Policy, принципы агента, ручной реестр |
| LAYER-3/STATE.md | Current formal state (primary) | Нарратив, история |
| LAYER-3/project-status.md | Project narrative (tertiary) | Формальный state, датированная история сессий |
| HANDOFF.md | Session contract / snapshot (secondary) | Канон state, полный session log |

Классификация документов (роль, статус, authority, lifecycle): [`LAYER-1/document-governance.md`](./LAYER-1/document-governance.md) — канон; не дублировать таблицы здесь.

### Правило нового правила
- Если логика относится к проекту → LAYER-1/
- Если к конкретной IDE → в adapter file

---

## Таблица компонентов

| Файл | Назначение | Для кого | Связь с другими |
|---|---|---|---|
| `README.md` | Главная навигация по системе | Все роли | Ведёт в quick start, карту документов и ключевые модули |
| `ONBOARDING-WIZARD.md` | Пошаговый старт без терминала | Новичок/врач | Использует `QUICK-START.md`, `error-handling.md` (в т.ч. откат) |
| `QUICK-START.md` | Короткий GUI-старт | Новичок | Ссылается на onboarding и advanced setup |
| `ADVANCED-SETUP.md` | Глубокая настройка среды и интеграций | Продвинутый пользователь | Связан с `CLAUDE.md`, `.cursor/rules/` |
| `LAYER-1/system-prompt.md` | Базовое поведение агента | Архитектор/лид | Опирается на контракт, scope и security |
| `LAYER-1/agent-rules.md` | Session load после `llms.txt`, контракт, границы | Архитектор/лид | Связан с `scope-guard.md`, `task-protocol.md` |
| `LAYER-1/task-protocol.md` | Формат задач и уровни риска | Команда разработки | Получает риск-теги из интервью и решений |
| `LAYER-1/scope-guard.md` | Контроль границ задачи | Все роли | При нарушении — см. откат в `error-handling.md` |
| `LAYER-1/self-verification.md` | Превентивная проверка до выполнения | Агент/ревьюер | Дополняет `error-handling.md` |
| `LAYER-1/error-handling.md` | Ошибки, классификация и откат | Агент/ревьюер | Включает раздел «Процедура отката»; связан с аудитом и инцидентами |
| `LEARNING-LOOP.md` | Обучение на инцидентах | Лид/команда | Использует `incidents/` и чеклист в `LAYER-1/audit.md` |
| `incidents/incident-template.md` | Структурированная запись инцидента | Лид/ревьюер | Влияет на обновление правил и чеклистов |
| `LAYER-3/project-status.md` | Нарратив проекта (этап, цели, риски) | Все роли | После `STATE.md` и `HANDOFF.md`; не источник формального state |
| `HANDOFF.md` | Контракт сессии и снимок контекста | Все роли | После `STATE.md`; не дублировать state как канон |

---

## Ключевые документы по слоям

### LAYER-1 (правила и контроль)
- [`workflow.md`](./LAYER-1/workflow.md)
- [`agent-rules.md`](./LAYER-1/agent-rules.md)
- [`document-governance.md`](./LAYER-1/document-governance.md)
- [`scope-guard.md`](./LAYER-1/scope-guard.md)
- [`security.md`](./LAYER-1/security.md)
- [`self-verification.md`](./LAYER-1/self-verification.md)
- [`error-handling.md`](./LAYER-1/error-handling.md) (ошибки и процедура отката)

### LAYER-2 (продукт и UX)
- [`project-interview.md`](./LAYER-2/discovery/project-interview.md)
- [`roadmap.md`](./LAYER-2/specs/roadmap.md)
- [`validation.md`](./LAYER-2/specs/validation.md)
- [`UX-DESIGN-GUIDE.md`](./LAYER-2/ux/UX-DESIGN-GUIDE.md)

### LAYER-3 (память и улучшения)
- [`project-status.md`](./LAYER-3/project-status.md)
- [`lessons.md`](./LAYER-3/lessons.md)
- [`fixes.md`](./LAYER-3/fixes.md)
