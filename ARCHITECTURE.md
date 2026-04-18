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

## State Control Plane — Ядро управления состоянием

Фреймворк использует гибридную архитектуру:
- **Функциональный слой (LAYER-1)** — правила, инструкции, независимые от состояния
- **State layer (LAYER-3)** — живое состояние проекта, сессии и задачи

### Компоненты Control Plane

| Файл | Роль | Тип |
|---|---|---|
| `LAYER-1/state-transitions.md` | Модель переходов: событие + guard + side effect | Политика |
| `LAYER-3/STATE.md` | Текущее состояние: Project + Session + Task | Runtime snapshot |
| `LAYER-1/agent-rules.md` | Bootstrap protocol + State authority | Правила агента |
| `HANDOFF.md` | Terminal session snapshot | Передача контекста |
| `LAYER-1/audit.md` | Проверка консистентности state | Аудит |

### Три домена состояния

```text
Project State:  INIT → DISCOVERY → PLANNING → DEVELOPMENT → REVIEW → RELEASE_READY → MAINTENANCE
Session State:  BOOTSTRAP → CONTEXT_LOADED → AWAITING_CONFIRMATION → EXECUTING → VERIFYING → HANDOFF
Task State:     DRAFT → PLANNED → IN_PROGRESS → REVIEW → DONE
                           ↓              ↓
                        BLOCKED      ROLLED_BACK
```

### Поток гибридной модели

```text
СТАРТ СЕССИИ
  → STATE.md (фаза? блокеры? next actions?)
  → project-status.md (детали)
  → выбрать документы LAYER-1 под текущую фазу
  → выполнить задачу через разрешённые переходы
  → обновить STATE.md + session-log.md
  → HANDOFF terminal snapshot
КОНЕЦ СЕССИИ
```

---

## Таблица компонентов

| Файл | Назначение | Для кого | Связь с другими |
|---|---|---|---|
| `README.md` | Главная навигация по системе | Все роли | Ведёт в quick start, карту документов и ключевые модули |
| `ONBOARDING-WIZARD.md` | Пошаговый старт без терминала | Новичок/врач | Использует `QUICK-START.md`, `error-handling.md` (в т.ч. откат) |
| `QUICK-START.md` | Короткий GUI-старт | Новичок | Ссылается на onboarding и advanced setup |
| `ADVANCED-SETUP.md` | Глубокая настройка среды и интеграций | Продвинутый пользователь | Связан с `CLAUDE.md`, `.cursor/rules/` |
| `LAYER-1/system-prompt.md` | Базовое поведение агента | Архитектор/лид | Опирается на контракт, scope и security |
| `LAYER-1/agent-rules.md` | Bootstrap, контракт, границы | Архитектор/лид | Связан с `scope-guard.md`, `task-protocol.md` |
| `LAYER-1/task-protocol.md` | Формат задач и уровни риска | Команда разработки | Получает риск-теги из интервью и решений |
| `LAYER-1/scope-guard.md` | Контроль границ задачи | Все роли | При нарушении — см. откат в `error-handling.md` |
| `LAYER-1/self-verification.md` | Превентивная проверка до выполнения | Агент/ревьюер | Дополняет `error-handling.md` |
| `LAYER-1/error-handling.md` | Ошибки, классификация и откат | Агент/ревьюер | Включает раздел «Процедура отката»; связан с аудитом и инцидентами |
| `LEARNING-LOOP.md` | Обучение на инцидентах | Лид/команда | Использует `incidents/` и чеклист в `LAYER-1/audit.md` |
| `incidents/incident-template.md` | Структурированная запись инцидента | Лид/ревьюер | Влияет на обновление правил и чеклистов |
| `LAYER-3/project-status.md` | Текущее состояние проекта | Все роли | Читается на старте каждой сессии |
| `HANDOFF.md` | Передача контекста между сессиями | Все роли | Обязателен при завершении задачи |

---

## Ключевые документы по слоям

### LAYER-1 (правила и контроль)
- [`workflow.md`](./LAYER-1/workflow.md)
- [`agent-rules.md`](./LAYER-1/agent-rules.md)
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
