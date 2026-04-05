# AGENTS — карта ролей агентов

> Для многоагентной работы. При одиночной — агент совмещает все роли.

---

## Общие правила

1. Порядок чтения: CLAUDE.md → START.md → `docs/ARCHITECTURE.md` → `docs/SECURITY_POLICY.md`
2. Не изменять архитектуру без явного запроса
3. Не писать код до подтверждения плана
4. После выполнения — обновлять memory-bank/
5. При любом изменении файлов в `docs/` — обновить `docs/DOCS-MAP.md` в том же коммите.

---

## Правила сопровождения документации

### Обязательная синхронизация `docs/DOCS-MAP.md`

`docs/DOCS-MAP.md` — это обязательная карта и индекс документации в каталоге `docs/`.

При любом изменении документации агент обязан поддерживать `docs/DOCS-MAP.md` в актуальном состоянии в рамках того же изменения.

Обязательные действия:
- Если в `docs/` создан новый файл документации — добавить соответствующую строку в `docs/DOCS-MAP.md`.
- Если файл документации переименован, перемещён или изменён его путь — обновить соответствующую строку в `docs/DOCS-MAP.md`.
- Если файл документации удалён — удалить соответствующую строку из `docs/DOCS-MAP.md`.
- Если у документа изменились смысл, статус, область применения или заголовок — обновить описание и связанные поля в `docs/DOCS-MAP.md`.
- Нельзя оставлять изменения в `docs/` без синхронного обновления `docs/DOCS-MAP.md` в том же коммите, патче или pull request.

Операционное правило:
- Любое изменение дерева документации считается незавершённым, пока не обновлён `docs/DOCS-MAP.md`.
- Перед завершением задачи нужно проверить, что все актуальные документы отражены в `docs/DOCS-MAP.md`.
- Нужно удалять устаревшие строки, которые ссылаются на несуществующие файлы.
- Нельзя откладывать обновление `docs/DOCS-MAP.md` на потом.

Область действия:
- Правило применяется к созданию, переименованию, перемещению, удалению, разделению и объединению файлов внутри `docs/`.
- Исключение допускается только если в задаче явно указано не изменять `docs/DOCS-MAP.md`.

Проверка перед завершением:
- Все актуальные файлы документации перечислены в `docs/DOCS-MAP.md`.
- В таблице нет строк для удалённых или перемещённых файлов.
- Пути, названия и описания актуальны.
- Обновление `docs/DOCS-MAP.md` входит в то же изменение, что и правка документации.

---

## Роли

**Team Lead** — читает задачу, составляет план, распределяет подзадачи

**Developer** — реализует TASK-XXX.md, не меняет архитектуру без указания

**Database Agent** — схема БД, миграции, RLS, индексы

**Tester** — пишет тесты, проверяет критичные сценарии

**Reviewer** — проверяет по REVIEW-CHECKLIST.md, блокирует деплой при 🔴

**Docs Agent** — обновляет CHANGELOG, HANDOFF, memory-bank/, DOCS-MAP.md

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

Two Node.js utility scripts in the repo root use only built-in modules (no `npm install` needed):

- `setup.js` — interactive setup wizard (requires TTY; do **not** run non-interactively)
- `template-sync.js` — copies new template files from a source dir to a target project

Run with: `node template-sync.js <source> <target> [--dry-run]`

### No lint / test / build

There are no linters, test frameworks, or build steps configured. The only runtime requirement is **Node.js 14+** (pre-installed in Cloud VMs).

### GitHub Actions

A single workflow `.github/workflows/memory-sync.yml` checks HANDOFF.md freshness on push. It runs in CI only, nothing to invoke locally.
```