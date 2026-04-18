# HANDOFF.md — Session Handoff Contract
<!-- Terminal Snapshot ПЕРЕЗАПИСЫВАЕТСЯ агентом при каждом завершении сессии -->
<!-- Session History ДОПИСЫВАЕТСЯ, не перезаписывается -->
<!-- Persistent Context МЕНЯЕТСЯ редко -->
<!-- Историческое → CHANGELOG.md | Формальное состояние → LAYER-3/STATE.md -->

---

## Terminal Snapshot
<!-- ПЕРЕЗАПИСЫВАЕТСЯ каждую сессию -->

Project state: MAINTENANCE
Session state: HANDOFF
Task state: ""
Active task: ""
Last event: ITERATION_3_COMPLETED
Last transition: DEVELOPMENT → MAINTENANCE

Next allowed actions:
- continue_iteration_1_state_machine

Blockers:
- ""

Что сделано в последней сессии:
- Добавлен [`LAYER-1/event-dictionary.md`](./LAYER-1/event-dictionary.md) — канон событий по доменам Project / Session / Task и запрещённые события; связка с [`state-transitions.md`](./LAYER-1/state-transitions.md)

Что должен сделать следующий агент первым шагом:
- Прочитать LAYER-3/STATE.md
- Выполнить промты итерации 1 state-machine migration

---

## Session History
<!-- ДОПИСЫВАЕТСЯ. Одна строка на сессию. -->

| Дата | Project state | Что сделано | Следующий шаг |
|---|---|---|---|
| 2026-04-18 | MAINTENANCE | Итерация 3 завершена | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | В ARCHITECTURE.md: State Control Plane + Принцип каноничности (роли файлов) | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | IDE entry points → указатели; новые модули LAYER-1/ для логики сессии, плана, этапов, приоритетов | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | `llms.txt` переписан: navigation index, bootstrap, situation routes | Итерация 1 state-machine |
| 2026-04-18 | MAINTENANCE | `event-dictionary.md`: канон событий для state-transitions | Итерация 1 state-machine |

---

## Persistent Context
<!-- МЕНЯЕТСЯ редко -->

Ключевые решения: LAYER-3/atomic-decisions.md
Архитектурные ограничения: ARCHITECTURE.md
Стек: документационный фреймворк для AI-агентов
Критические зависимости: LAYER-1/ (28 файлов), LAYER-2/, LAYER-3/
