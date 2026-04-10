# Cursor — контроль интервью (self-check стража)

> Trigger: интервью в Cursor по `LAYER-2/discovery/project-interview.md`  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `LAYER-1/interview-system.md`

## Когда применять

Когда в Cursor ведёте интервью по [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md) (новый проект, сбор контекста). Отдельного агента `@guardian` в Cursor нет — проверку делает **тот же агент** в каждом ответе.

## Читать перед интервью

1. [`llms.txt`](../../../llms.txt) — этап 0, уровень проекта.
2. [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md) — маршрут вопросов.
3. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) — протокол и формат сообщения.
4. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) — чеклист из 7 пунктов.
5. [`LAYER-1/agent-contract.md`](../../../LAYER-1/agent-contract.md) — принципы и модули.

Соблюдайте также `.cursor/rules/10-communication.mdc` (один вопрос, entry flow).

## Обязательный формат каждого ответа

1. Вопрос владельцу (или резюме + «Правильно понимаю?» — один шаг).
2. Блок **СТРАЖ** — таблица из [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) (все 7 строк с колонками ✅/⚠️/❌ и кратким доказательством).
3. Строка вердикта: `СТРАЖ: ✅` / `СТРАЖ: ⚠️` / `СТРАЖ: ❌`.
4. Если **не ❌** — можно следующий шаг или уточнение. Если **❌** — только исправленный один вопрос и снова полный блок СТРАЖ (**stop-block**: без следующего вопроса по маршруту).

## Stop-block

При **❌** по критическим пунктам (1, 2, 3, 6, 7) в [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md): не задавать следующий вопрос из `PROJECT-INTERVIEW.md` до исправления и нового прохода чеклиста.

## Журнал

После каждого ответа владельца (когда ведёте журнал) — запись в [`LAYER-3/interview-session.md`](../../LAYER-3/interview-session.md); в поле вердикта укажите `control-mode: cursor-self-check`.
