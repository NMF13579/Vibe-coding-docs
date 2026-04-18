# State Transitions — политика переходов

Формальные переходы состояния описывают **событие + guard + side effect**; без выполненного guard переход не выполняется. При каждом допустимом переходе агент обновляет **`LAYER-3/STATE.md`**.

## Где смотреть детали

- **Канонические имена событий** — [`event-dictionary.md`](./event-dictionary.md) (все `Event` в таблицах переходов должны совпадать с этим словарём).
- **Три домена** (Project / Session / Task) и состав control plane — [`ARCHITECTURE.md`](../ARCHITECTURE.md), раздел **State Control Plane**.
- **Bootstrap, STATE AUTHORITY, HANDOFF** — [`agent-rules.md`](./agent-rules.md) (начало файла).
- **Жизненный цикл сессии** (старт, конец задачи, напоминания, аудит, фичи) — [`session-lifecycle.md`](./session-lifecycle.md).
- **Plan gate, scope, СТОП** — [`plan-and-scope-gate.md`](./plan-and-scope-gate.md).
- **Этапы `stages/*`** — [`stage-routing.md`](./stage-routing.md).
- **Приоритет источников** — [`instruction-priority.md`](./instruction-priority.md).

Полные таблицы переходов (Domain / From / Event / Guard / To / Side effects) при необходимости расширяются в этом файле по мере стабилизации схемы в `STATE.md`; до этого ориентир — домены и guards в `LAYER-3/STATE.md` и протоколы выше.
