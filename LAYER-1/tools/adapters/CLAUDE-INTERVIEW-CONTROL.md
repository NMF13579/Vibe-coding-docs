> Trigger: интервью в Claude без отдельного guardian  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `LAYER-1/interview-system.md`

# Claude (Code / чат с репозиторием) — контроль интервью (self-check стража)

## Когда применять

Когда интервью ведётся через Claude с доступом к этому репозиторию и без OpenCode subagent «guardian». Проверка — **self-check** по тем же правилам, что в [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md).

## Читать перед интервью

1. [`llms.txt`](../../../llms.txt)
2. [`CLAUDE.md`](../../CLAUDE.md) — общий контракт сессии.
3. [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md)
4. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
5. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
6. [`LAYER-1/agent-contract.md`](../../../LAYER-1/agent-contract.md)

## Обязательный формат каждого ответа

1. Вопрос владельцу (один шаг по маршруту).
2. Блок **СТРАЖ**: таблица 7 пунктов из `LAYER-1/interview-system.md` с отметками и доказательствами.
3. Вердикт: `СТРАЖ: ✅` / `⚠️` / `❌`.
4. При **❌** — **stop-block**: только исправленный вопрос и снова чеклист; без следующего пункта `PROJECT-INTERVIEW.md`.

## Stop-block

См. раздел «Правило stop-block» в [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md).

## Журнал

[`LAYER-3/interview-session.md`](../../LAYER-3/interview-session.md); `control-mode: claude-self-check`.
