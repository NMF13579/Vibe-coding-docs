<!-- ROLE: DEPRECATED -->
<!-- AUTHORITY: NON-AUTHORITY -->
<!-- STATUS: DEPRECATED -->
<!-- TYPE: ARCHIVAL / NON-RUNTIME -->
<!-- REPLACED_BY: LAYER-1/agent-rules.md (# BOOTSTRAP PROTOCOL, state-first) -->
<!-- DO NOT USE FOR: bootstrap, runtime decisions, state transitions -->
<!-- Archived: 2026-04 -->

# BOOTSTRAP PROTOCOL
<!-- Выполняется строго до любых других действий -->

## Шаги (порядок строгий):
1. Прочитать LAYER-3/STATE.md
   → определить Project / Session / Task state
   → проверить forbidden и next_allowed_actions
2. Прочитать LAYER-3/project-status.md
3. Прочитать LAYER-3/session-log.md
4. Прочитать LAYER-3/atomic-decisions.md
5. Прочитать активную задачу (если active_task не пустой)
6. Сообщить пользователю:
   - текущий Project state
   - текущий Task state
   - next_allowed_actions
   - блокеры (если есть)
7. Перевести Session state: BOOTSTRAP → CONTEXT_LOADED
8. [BOOTSTRAP COMPLETE] — только теперь начинать работу

---

## 1. Инициализация агента (bootstrap)

### С чего начинает агент (bootstrap)

> **Уровень 0:** bootstrap опционален — запускай только при потере контекста или неожиданной поломке.
> **Уровень 1 и выше:** выполнять перед первой задачей в проекте.
> **Любой уровень:** выполнять при симптомах потери контекста (см. `LAYER-1/context-recovery.md`).

Перед началом работы агент должен:

1. Следовать порядку из `shared/priority-order.md`.
   Обязательный минимум для старта:
   - `project/PROJECT.md` (или `README.md` если PROJECT не существует)
   - `HANDOFF.md`
   - `LAYER-3/project-status.md`
   - `llms.txt` / `LAYER-1/workflow.md`

2. Если сессия не первая — заглянуть в:
   - `LAYER-3/lessons.md` — применимые уроки
   - `LAYER-3/fixes.md` — повторяемые фиксы
   - `LAYER-3/features.md` — список фич

3. В зависимости от того, через какой инструмент идёт работа:
   - Claude Code → учесть правила из `CLAUDE.md` и доступные `.claude/agents/*`
   - Cursor → учитывать `.cursor/rules/*`
   - GitHub Copilot → учитывать `.github/copilot-instructions.md`
   - Gemini → учитывать `GEMINI.md`

4. Кратко пересказать владельцу:
   - что сейчас с проектом;
   - где мы остановились;
   - какие 1–3 варианта есть для следующего шага.

### Порядок работы с чеклистом

1. Проверить все файлы из чеклиста
2. Заполнить отчёт честно (отсутствует = отсутствует)
3. Задать вопросы для заполнения пробелов (по одному)
4. Предложить следующие шаги

### Чеклист

#### Критичные (все уровни)
- [ ] /llms.txt — точка входа для агента
- [ ] /LAYER-1/workflow.md — конвейер и уровни
- [ ] /CLAUDE.md — заполнен стек?
- [ ] /HANDOFF.md
- [ ] /LAYER-1/anti-patterns.md — прочитать перед выбором подхода к решению

#### Критичные (Уровень 1 и выше)
- [ ] /LAYER-2/specs/roadmap.md — заполнена цель и текущий этап?
- [ ] /LAYER-2/specs/architecture.md — заполнены разделы 1–4?
- [ ] /LAYER-1/security.md (если данные чувствительные)

#### Важные
- [ ] /shared/ai-failure-modes.md — сбои LLM-агентов: диагностика и действия
- [ ] /LAYER-2/specs/planning.md
- [ ] /LAYER-1/task-protocol.md
- [ ] /LAYER-1/dialog-style.md — стиль диалога и тон общения с владельцем
- [ ] /LAYER-1/decision-guide.md — справочник развилок: что выбрать и почему
- [ ] /LAYER-1/glossary.md — словарь терминов простым языком
- [ ] /LAYER-1/error-handling.md — классификация ошибок: тип → действие
- [ ] /LAYER-1/stack-presets.md — готовые наборы инструментов по типу проекта
- [ ] /LAYER-2/discovery/project-interview.md — протокол интервью при старте нового проекта
- [ ] /LAYER-2/specs/validation.md — объективная проверка: работает / не работает
- [ ] /LAYER-1/testing-guide.md — чеклист проверки после каждой задачи
- [ ] /LAYER-2/ux/user-flows.md — ключевые сценарии для smoke-теста перед релизом
- [ ] /LAYER-3/project-status.md
- [ ] /LAYER-3/languages.md
- [ ] /LAYER-3/integrations.md

### Формат отчёта

```
## Отчёт о состоянии проекта

Проект: [название или «не определено»]
Тип: [web / mobile / bot / «не определено»]
Стек: [или «не заполнен»]

Готово и заполнено: [список]
Есть, но пустое: [файл — что пустое]
Отсутствует: [список]

Текущий этап ROADMAP: [этап X]
Последнее действие: [из HANDOFF.md]
Следующий шаг: [из ROADMAP]
```

### Вопросы для пробелов

**Стек не заполнен:**
> «Какие сервисы используешь? Supabase, Vercel, Lovable, Telegram?»

**Тип не определён:**
> «Это сайт, мобильное приложение или Telegram-бот?»

**HANDOFF пустой (не новый проект):**
> «Что делали в последний раз? На чём остановились?»

### Предложение следующих шагов

```
## Предлагаемые следующие шаги

Немедленно:
1. [действие] — [почему критично]

В ближайшей сессии:
2. [действие]

***
[BOOTSTRAP COMPLETE]
Контекст загружен. Готов принимать задачи.
Что начнём прямо сейчас?
```

> **Правило:** агент не принимает задачи к выполнению ДО момента вывода `[BOOTSTRAP COMPLETE]`.
> Если владелец даёт задачу до завершения bootstrap — агент отвечает:
> «Одну секунду — заканчиваю диагностику состояния проекта.
> [BOOTSTRAP COMPLETE] — теперь готов. Итак, твоя задача: [повторить].»

Только после этого переходить к конкретной задаче.

---
