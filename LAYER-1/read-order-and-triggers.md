> Trigger: старт, быстрые команды, маршрут по типу задачи  
> Read-time: ~4 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `START.md`, `llms.txt`

# Порядок чтения и триггеры

## Рекомендуемая цепочка (Cursor / общий ориентир)

1. `README.md` или `START.md` (см. карту для вашей среды).
2. `llms.txt`.
3. `LAYER-3/STATE.md`, затем `HANDOFF.md`, затем при необходимости `LAYER-3/project-status.md` (нарратив).

Детали: `LAYER-1/agent-rules.md`, полный конвейер: `LAYER-1/workflow.md`.

Перед реализацией: `LAYER-1/scope-guard.md`. Перед завершением: `LAYER-1/self-verification.md`.

При конфликте инструкций: `README.md` не подменяет `shared/priority-order.md` — следовать канону в `LAYER-1/instruction-priority.md`.

## Быстрые команды (Cursor)

- `/verify` → `LAYER-1/self-verification.md`
- `/rollback` → `LAYER-1/error-handling.md`, раздел «Процедура отката»
- `/scope-check` → `LAYER-1/scope-guard.md`
- `/audit` → `LAYER-1/audit.md`

Поведение и контракт: `LAYER-1/system-prompt.md`, `LAYER-1/agent-rules.md`.

## Маршрут по типу задачи

- Старт проекта → `llms.txt`, `LAYER-1/workflow.md` (этап 0), `LAYER-1/agent-rules.md`
- Стиль → `dialog-style.md`, `glossary.md`
- Планирование → `LAYER-2/specs/planning.md`, `roadmap.md`
- Архитектура продукта → `LAYER-2/specs/architecture.md`, `stack-presets.md`
- Ревью → `task-protocol.md`
- Аудит → `audit.md`
- Безопасность → `security.md`, при необходимости `LAYER-3/security.md`
- Идеи → `feature-radar.md`, `LAYER-3/features.md`
- Путаница → `context-recovery.md`

## Интервью (Copilot / Gemini / OpenCode)

- Канон: `LAYER-2/discovery/project-interview.md`, `LAYER-1/interview-system.md`.
- Дельта среды: `LAYER-1/tools/adapters/README.md` и соответствующий `*-INTERVIEW-CONTROL.md`.
