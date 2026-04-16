> Trigger: интервью в Copilot  
> Read-time: ~5 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `LAYER-1/interview-system.md`

# GitHub Copilot — контроль интервью (self-check стража)

## Когда применять

Когда в среде с Copilot (VS Code, GitHub и т.д.) ведёте интервью по [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md). Отдельного сабагента стража нет — **self-check** в каждом ответе агента.

## Читать перед интервью

1. [`llms.txt`](../../../llms.txt)
2. [`LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md)
3. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
4. [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md)
5. [`LAYER-1/agent-contract.md`](../../../LAYER-1/agent-contract.md)

Учитывайте [`.github/copilot-instructions.md`](../../../.github/copilot-instructions.md).

## Обязательный формат каждого ответа

1. Вопрос владельцу (один смысловой шаг).
2. Блок **СТРАЖ** — полная таблица из 7 проверок [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md).
3. `СТРАЖ: ✅` / `⚠️` / `❌`.
4. Следующий шаг маршрута — **только** если нет **❌**. Иначе — исправление + повтор чеклиста (**stop-block**).

## Stop-block

Как в [`LAYER-1/interview-system.md`](../../../LAYER-1/interview-system.md): при **❌** не продвигаться по этапам интервью до исправления.

## Журнал

[`LAYER-3/interview-session.md`](../../../LAYER-3/interview-session.md); указывайте `control-mode: copilot-self-check`.
