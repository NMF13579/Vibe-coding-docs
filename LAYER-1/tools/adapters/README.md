# Адаптеры IDE — контроль интервью

> Trigger: настройка self-check стража под свою IDE  
> Read-time: ~8 min  
> Filled-by: agent / user  
> Needs-approval: no  
> Next: [`../../interview-system.md`](../../interview-system.md)

Канонический протокол один: [`../../interview-system.md`](../../interview-system.md).  
Файлы ниже — только **дельты по среде** (что прочитать сверх ядра и как подписать журнал).

| Среда | Дельта |
|-------|--------|
| Cursor | [CURSOR-INTERVIEW-CONTROL.md](./CURSOR-INTERVIEW-CONTROL.md) |
| GitHub Copilot | [COPILOT-INTERVIEW-CONTROL.md](./COPILOT-INTERVIEW-CONTROL.md) |
| Claude (Code / чат с репо) | [CLAUDE-INTERVIEW-CONTROL.md](./CLAUDE-INTERVIEW-CONTROL.md) |
| Gemini | [GEMINI-INTERVIEW-CONTROL.md](./GEMINI-INTERVIEW-CONTROL.md) |
| OpenCode | [OPENCODE-INTERVIEW-CONTROL.md](./OPENCODE-INTERVIEW-CONTROL.md) |

---

<a id="adapter-core"></a>

## Общее ядро (все среды)

### Идея

Отдельного внешнего «стража» в типичном сценарии нет: **тот же агент** в каждом ответе выполняет **self-check** по [`../../interview-system.md`](../../interview-system.md).

### Порядок чтения перед интервью

1. [`../../../START.md`](../../../START.md) и [`../../../llms.txt`](../../../llms.txt) — единый вход и карта маршрутов (новая сессия).
2. [`../../../LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md) — маршрут вопросов и этапов.
3. [`../../interview-system.md`](../../interview-system.md) — формат сообщения, таблица **СТРАЖ** (7 пунктов), **stop-block**.
4. [`../../agent-rules.md`](../../agent-rules.md) — bootstrap и модули; [`../../agent-contract.md`](../../agent-contract.md) — локальный entrypoint контракта (source of truth: `shared/agent-contract.md`).

Среда может требовать **дополнительный** файл — см. дельту в таблице выше.

### Обязательный формат каждого ответа

1. **Один** смысловой шаг владельцу: один вопрос **или** краткое резюме + «Правильно понимаю?».
2. Блок **СТРАЖ** — полная таблица из **7 строк** по [`../../interview-system.md`](../../interview-system.md) с колонками ✅ / ⚠️ / ❌ и кратким доказательством по каждой строке.
3. Строка вердикта: `СТРАЖ: ✅` / `СТРАЖ: ⚠️` / `СТРАЖ: ❌`.
4. При **❌** — **stop-block**: не продвигаться по [`project-interview.md`](../../../LAYER-2/discovery/project-interview.md); только исправление одного шага и снова полный СТРАЖ. Критические пункты — **1, 2, 3, 6, 7** (как в `interview-system.md`).
5. При отсутствии **❌** — можно следующий шаг по маршруту или уточнение.

### Журнал

Вести [`../../../LAYER-3/interview-session.md`](../../../LAYER-3/interview-session.md).  
Поле **`control-mode`** задаётся в дельте адаптера для вашей среды.
