> Trigger: Роли агентов и синхронизация доков
> Read-time: ~10 min
> Filled-by: agent
> Needs-approval: no
> Next: LAYER-1/tools/template-sync-index.md

# AGENTS — карта ролей агентов

> Для многоагентной работы. При одиночной — агент совмещает все роли.

---

## Общие правила

1. Порядок чтения: CLAUDE.md → `llms.txt` / `LAYER-1/workflow.md` → `LAYER-2/specs/architecture.md` → `LAYER-1/security.md`
2. Не изменять архитектуру без явного запроса
3. Не писать код до подтверждения плана
4. После выполнения — обновлять LAYER-3/
5. При любом изменении файлов в `LAYER-1/` или `LAYER-2/` (навигационно значимых) — обновить `LAYER-1/tools/template-sync-index.md` в том же коммите.

---

## Правила сопровождения документации

### Обязательная синхронизация `LAYER-1/tools/template-sync-index.md`

`LAYER-1/tools/template-sync-index.md` — это обязательная карта и индекс документации в `LAYER-1/` и `LAYER-2/`.

При любом изменении документации агент обязан поддерживать `LAYER-1/tools/template-sync-index.md` в актуальном состоянии в рамках того же изменения.

Обязательные действия:
- Если создан новый навигационно значимый файл в `LAYER-1/` или `LAYER-2/` — добавить соответствующую строку в `LAYER-1/tools/template-sync-index.md`.
- Если файл документации переименован, перемещён или изменён его путь — обновить соответствующую строку в `LAYER-1/tools/template-sync-index.md`.
- Если файл документации удалён — удалить соответствующую строку из `LAYER-1/tools/template-sync-index.md`.
- Если у документа изменились смысл, статус, область применения или заголовок — обновить описание и связанные поля в `LAYER-1/tools/template-sync-index.md`.
- Нельзя оставлять такие изменения без синхронного обновления `LAYER-1/tools/template-sync-index.md` в том же коммите, патче или pull request.

Операционное правило:
- Любое изменение дерева документации считается незавершённым, пока не обновлён `LAYER-1/tools/template-sync-index.md`.
- Перед завершением задачи нужно проверить, что все актуальные документы отражены в `LAYER-1/tools/template-sync-index.md`.
- Нужно удалять устаревшие строки, которые ссылаются на несуществующие файлы.
- Нельзя откладывать обновление `LAYER-1/tools/template-sync-index.md` на потом.

Область действия:
- Правило применяется к созданию, переименованию, перемещению, удалению, разделению и объединению навигационно значимых файлов внутри `LAYER-1/` и `LAYER-2/`.
- Исключение допускается только если в задаче явно указано не изменять `LAYER-1/tools/template-sync-index.md`.

Проверка перед завершением:
- Все актуальные файлы документации перечислены в `LAYER-1/tools/template-sync-index.md`.
- В таблице нет строк для удалённых или перемещённых файлов.
- Пути, названия и описания актуальны.
- Обновление `LAYER-1/tools/template-sync-index.md` входит в то же изменение, что и правка документации.

---

## Роли

**Team Lead** — читает задачу, составляет план, распределяет подзадачи

**Developer** — реализует TASK-XXX.md, не меняет архитектуру без указания

**Database Agent** — схема БД, миграции, RLS, индексы

**Tester** — пишет тесты, проверяет критичные сценарии

**Reviewer** — проверяет по REVIEW-CHECKLIST.md, блокирует деплой при 🔴

**Docs Agent** — обновляет CHANGELOG, HANDOFF, LAYER-3/, LAYER-1/tools/template-sync-index.md

---

## Pipeline

```
[Владелец] → задача → [Team Lead] → план
    → [Developer] + [Database Agent] → код
    → [Tester] → тесты
    → [Reviewer] → чеклист
    → [Docs Agent] → документы
    → [Владелец] → деплой ОК
```

## Cursor Cloud specific instructions

This is a **documentation-only template** ("Vibe-coding-docs"). There is no application to build or run as a service. The `src/` directory is empty (placeholder for future product code).

### Executable components

Two Node.js utility scripts in `LAYER-1/tools/` use only built-in modules (no `npm install` needed):

- `LAYER-1/tools/setup.js` — interactive setup wizard (requires TTY; do **not** run non-interactively)
- `LAYER-1/tools/template-sync.js` — copies new template files from a source dir to a target project

Run with: `node LAYER-1/tools/template-sync.js <source> <target> [--dry-run]`

### No lint / test / build

There are no linters, test frameworks, or build steps configured. The only runtime requirement is **Node.js 14+** (pre-installed in Cloud VMs).

### GitHub Actions

A single workflow `.github/workflows/memory-sync.yml` checks HANDOFF.md freshness on push. It runs in CI only, nothing to invoke locally.
```