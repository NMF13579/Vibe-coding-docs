> Trigger: интервью в Gemini  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `LAYER-1/interview-system.md`

# Gemini — контроль интервью (self-check стража)

## Когда применять

Когда интервью ведётся через Gemini с этим репозиторием как контекстом. Отдельного агента-стража нет — выполняйте **self-check** по [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md) в каждом ответе.

## Читать перед интервью

1. [`llms.txt`](../../../llms.txt)
2. [`GEMINI.md`](../../../GEMINI.md) — ориентир для Gemini в корне репозитория.
3. [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md)
4. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
5. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
6. [`LAYER-1/agent-contract.md`](../../../LAYER-1/agent-contract.md)

## Обязательный формат каждого ответа

1. Один вопрос (или резюме + «Правильно понимаю?»).
2. Блок **СТРАЖ** — таблица из 7 строк по `LAYER-1/interview-system.md`.
3. `СТРАЖ: ✅` / `⚠️` / `❌`.
4. Дальше по маршруту — только если не **❌**; при **❌** — stop-block и исправление.

## Stop-block

Без следующего вопроса по `project-interview.md`, пока критический **❌** не устранён повторной проверкой.

## Журнал

[`LAYER-3/interview-session.md`](../../../LAYER-3/interview-session.md); `control-mode: gemini-self-check`.
