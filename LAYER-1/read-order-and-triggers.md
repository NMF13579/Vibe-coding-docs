> Trigger: старт, быстрые команды, маршрут по типу задачи  
> Read-time: ~4 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `START.md`, `llms.txt`

# Порядок чтения и триггеры

## Рекомендуемая цепочка (люди и общий ориентир)

- Для **людей**: `README.md` или [`START.md`](../START.md).
- Для **агента** при старте сессии: перечень файлов и порядок чтения задаются **только** в [`llms.txt`](../llms.txt); после загрузки — [`agent-rules.md`](./agent-rules.md) (раздел `# SESSION LOAD`).

Полный конвейер процесса: `LAYER-1/workflow.md`.

Перед реализацией: `LAYER-1/scope-guard.md`. Перед завершением: `LAYER-1/self-verification.md`.

При конфликте инструкций: `README.md` не подменяет `shared/priority-order.md` — следовать канону в `LAYER-1/instruction-priority.md`.

## Быстрые команды (Cursor)

- `/verify` → `LAYER-1/self-verification.md`
- `/rollback` → `LAYER-1/error-handling.md`, раздел «Процедура отката»
- `/scope-check` → `LAYER-1/scope-guard.md`
- `/audit` → `LAYER-1/audit.md`

Поведение и контракт: `LAYER-1/system-prompt.md`, `LAYER-1/agent-rules.md`.

## Маршрут по типу задачи

- Старт проекта → см. `llms.txt`; этап 0 процесса — `LAYER-1/workflow.md`
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
