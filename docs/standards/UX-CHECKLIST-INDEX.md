# UX-CHECKLIST-INDEX.md

Оглавление UX-чек-листов для проекта.
Помогает агенту и человеку выбрать нужный набор под конкретный проект.

## 1. Базовые чек-листы

Эти чек-листы составляют основу большинства проектов.

- `UX-CHECKLIST-DEFAULT.md`  
  Стандартный набор UX-решений для типового web-интерфейса (структура экранов, формы, списки, empty states, ошибки).

- `UX-CHECKLIST-MINIMAL.md`  
  Упрощённый интерфейс без лишних блоков, когда нужен максимально простой UI.

- `UX-CHECKLIST-ACCESSIBILITY.md`  
  Базовая доступность: контраст, клавиатура, screen reader, мобильная доступность.

- `UX-CHECKLIST-MOBILE.md`  
  Mobile-first и мобильные интерфейсы: touch targets, навигация, формы, ошибки.

- `UX-CHECKLIST-EMPTY-STATES.md`  
  Пустые состояния: “нет данных”, “ничего не найдено”, первый вход, ошибка загрузки.

## 2. Домены и роли

Эти чек-листы включаются при специфических типах систем.

- `UX-CHECKLIST-MEDICAL.md`  
  Для медицинских и около-медицинских проектов: безопасность, снижение риска ошибок, ясные статусы.

- `UX-CHECKLIST-ROLE-BASED-UX.md`  
  Для систем с разными ролями (врач, пациент, администратор, оператор и т.п.).

- `UX-CHECKLIST-DASHBOARDS.md`  
  Для дашбордов и обзорных экранов: KPI, статусы, очереди, критичные события.

## 3. Состояния и взаимодействия

- `UX-CHECKLIST-NOTIFICATIONS.md`  
  Уведомления: success, error, warning, info, напоминания, приоритеты.

- `UX-CHECKLIST-TABLES-AND-BULK-ACTIONS.md`  
  Таблицы и массовые действия: списки, пагинация, выбор нескольких элементов.

- `UX-CHECKLIST-SEARCH-FILTERS.md`  
  Поиск, фильтры, сортировка, сброс параметров, поведение “ничего не найдено”.

- `UX-CHECKLIST-HISTORY-AND-AUDIT.md`  
  История изменений и аудит: кто что сделал и когда, особенно важно для медицины и B2B.

## 4. Поддержка и тексты

- `UX-CHECKLIST-HELP-AND-SUPPORT.md`  
  Помощь, центр справки, связь с поддержкой.

- `UX-CHECKLIST-MICROCOPY.md`  
  Микротекст: кнопки, ошибки, подсказки, тон общения.

## 5. Как агент выбирает чек-листы под проект

Агент должен использовать этот файл совместно с `UX-CHECKLIST-LEGEND.md`.

### 5.1. По типу проекта

- Простой кабинет / MVP:
  - Обязательно: `DEFAULT`, `MINIMAL`, `ACCESSIBILITY`, `EMPTY-STATES`.
  - При необходимости: `MOBILE`, `SEARCH-FILTERS`, `TABLES-AND-BULK-ACTIONS`.

- Внутренний сервис / админка / B2B:
  - Обязательно: `DEFAULT`, `ACCESSIBILITY`, `EMPTY-STATES`, `SEARCH-FILTERS`, `TABLES-AND-BULK-ACTIONS`.
  - Часто нужно: `DASHBOARDS`, `HISTORY-AND-AUDIT`, `NOTIFICATIONS`.

- Медицинский/околомедицинский сервис:
  - Обязательно: `MEDICAL`, `ACCESSIBILITY`, `EMPTY-STATES`, `NOTIFICATIONS`, `HISTORY-AND-AUDIT`, `ROLE-BASED-UX`.
  - При наличии дашбордов: `DASHBOARDS`.
  - При мобильном сценарии: `MOBILE`.

- Публичный личный кабинет / пациентский портал:
  - Обязательно: `DEFAULT`, `MOBILE`, `ACCESSIBILITY`, `EMPTY-STATES`.
  - Для медицины: плюс `MEDICAL`, `ROLE-BASED-UX`, `NOTIFICATIONS`.

### 5.2. По уровню сложности

- Минимальный интерфейс:
  - `UX-CHECKLIST-MINIMAL.md`
  - `UX-CHECKLIST-EMPTY-STATES.md`
  - `UX-CHECKLIST-ACCESSIBILITY.md`

- Продвинутый интерфейс:
  - Всё из Default-блока + доменные и специализированные чек-листы по необходимости.

Агент должен явно указывать, какой набор чек-листов он использует для данного проекта.
