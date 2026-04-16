# OpenCode — контроль интервью (self-check стража)

> Trigger: интервью в OpenCode по `LAYER-2/discovery/project-interview.md`  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `LAYER-1/interview-system.md`

## Когда применять

Когда интервью ведётся через OpenCode (терминальный CLI-агент) по [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md). Отдельного subagent «guardian» нет — проверку делает **тот же агент** в каждом ответе (**self-check**).

## Точка входа

OpenCode при старте автоматически читает файлы в следующем порядке приоритета:

1. `AGENTS.md` в корне проекта (если есть)
2. `CLAUDE.md` в корне проекта (fallback)
3. `~/.config/opencode/AGENTS.md` — глобальный файл пользователя

В этом репозитории используется **`CLAUDE.md`** как основной контракт сессии.

## Читать перед интервью

1. [`CLAUDE.md`](../../../CLAUDE.md) — общий контракт сессии (загружается автоматически).
2. [`llms.txt`](../../../llms.txt) — этап 0, уровень проекта.
3. [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md) — маршрут вопросов.
4. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) — протокол и формат сообщения.
5. [`LAYER-1/agent-contract.md`](../../../LAYER-1/agent-contract.md) — принципы и модули.

## Специфика OpenCode

- OpenCode — **терминальный агент**, работает через CLI без графического интерфейса.
- Поддерживает кастомных агентов через `.opencode/agents/*.md` (для специализированных ролей).
- При необходимости выделить guardian в отдельного агента — создайте `.opencode/agents/guardian.md` с протоколом из [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md).

## Обязательный формат каждого ответа

1. Вопрос владельцу (один шаг по маршруту).
2. Блок **СТРАЖ** — таблица из [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) (все 7 строк с колонками ✅/⚠️/❌ и кратким доказательством).
3. Строка вердикта: `СТРАЖ: ✅` / `СТРАЖ: ⚠️` / `СТРАЖ: ❌`.
4. Если **не ❌** — можно следующий шаг или уточнение. Если **❌** — только исправленный один вопрос и снова полный блок СТРАЖ (**stop-block**: без следующего вопроса по маршруту).

## Stop-block

При **❌** по критическим пунктам (1, 2, 3, 6, 7) в [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md): не задавать следующий вопрос из `project-interview.md` до исправления и нового прохода чеклиста.

## Журнал

После каждого ответа владельца — запись в [`LAYER-3/interview-session.md`](../../../LAYER-3/interview-session.md); в поле вердикта укажите `control-mode: opencode-self-check`.
