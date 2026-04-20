# shared/ — общие правила (все этапы)

Файлы здесь задают поведение агента **на любом** этапе `stages/0X-*`.

## Порядок чтения (обычно)

> Это порядок для Claude Code workflow, не агентский bootstrap. Canonical bootstrap: llms.txt

1. `project/PROJECT.md` — живое ТЗ (источник истины по продукту).
2. `shared/scope-guard.md` — что нельзя делать, одна задача за раз.
3. `shared/agent-contract.md` — базовый контракт агента.
4. `shared/workflow.md` — жизненный цикл и план.
5. `shared/task-protocol.md` — формат задач и ревью.

## Связь с LAYER-*

Этот репозиторий-шаблон также содержит полные версии многих правил в `LAYER-1/`, `LAYER-2/`, `LAYER-3/`.  
В `shared/*.md` — **сжатая выжимка** для Claude Code; подробности и примеры — по ссылкам внутри файлов.

## Приоритет при конфликте

Как правило: **`stages/*/BOOT.md` (frontmatter `priority`)** > `shared/scope-guard.md` > `shared/agent-contract.md` > локальный документ этапа > `shared/workflow.md` > остальное.

Уточнение всегда в актуальном `BOOT.md` текущего этапа.
