# FAQ — частые ситуации

## Агент не понимает задачу

→ Напиши: «Объясни, что ты понял» — агент пересформулирует  
→ Если не помогло: открой [LAYER-1/context-recovery.md](./LAYER-1/context-recovery.md)

## Контекст потерян между сессиями

→ Напиши: «Восстанови контекст»  
→ Агент читает `llms.txt` → `LAYER-3/STATE.md` → `HANDOFF.md` → `LAYER-3/project-status.md`  
→ Если открываешь файлы сам: [`llms.txt`](./llms.txt) → [`LAYER-3/STATE.md`](./LAYER-3/STATE.md) → [`HANDOFF.md`](./HANDOFF.md) → [`LAYER-3/project-status.md`](./LAYER-3/project-status.md)

## Что-то пошло не так, нужен откат

→ Напиши: «Всё сломалось»  
→ Агент читает [LAYER-1/error-handling.md](./LAYER-1/error-handling.md)

## Задача начала расползаться

→ Напиши: «Проверь скоуп»  
→ Агент читает [LAYER-1/scope-guard.md](./LAYER-1/scope-guard.md)

## Не знаю, что написать агенту

→ Открой [LAYER-1/owner.md](./LAYER-1/owner.md) — шпаргалка с командами

## Хочу начать новый проект с нуля

→ Напиши: «Начнём» — агент проведёт через интервью (см. [LAYER-1/interview-system.md](./LAYER-1/interview-system.md))

## Как сохранить прогресс перед закрытием

→ Напиши: «Сохрани контекст»  
→ Агент обновит `HANDOFF.md` и `LAYER-3/session-log.md`

## Агент предлагает слишком много сразу

→ Напиши: «Один шаг» — агент вернётся к режиму одного вопроса

## Нужно выбрать технологии для проекта

→ Напиши: «Помоги выбрать стек»  
→ Агент читает [LAYER-1/stack-presets.md](./LAYER-1/stack-presets.md)

## Хочу проверить готовность к релизу

→ Напиши: «Проверь готовность к релизу»  
→ Агент читает [LAYER-1/task-protocol.md](./LAYER-1/task-protocol.md) и [LAYER-2/qa/](./LAYER-2/qa/)
