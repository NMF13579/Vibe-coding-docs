# INDEX-SCHEMA

## Purpose

AgentOS нужен `data/index.json`, чтобы быстрее находить релевантные Markdown-файлы и их метаданные без полного сканирования репозитория.
Это снижает ошибки контекста у агента и ускоряет deterministic checks.

Главный принцип:
- Markdown остаётся источником смысла (source of truth).
- Frontmatter остаётся контрактом метаданных.
- Index — только производная навигация.

## Why Derived Index Is Needed

- Большой репозиторий содержит много файлов и семейств документов.
- Индекс позволяет строить быстрые выборки по `type/module/status/authority`.
- Индекс уменьшает риск, что агент читает нерелевантные файлы первым.

## Derived-Only Rules

`data/index.json`:
- navigation only;
- rebuildable from Markdown/frontmatter;
- must not become hidden source of truth;
- must not store approval/completion/release/human decisions as authority;
- stale or missing index must not override Markdown;
- future scripts must be able to delete and rebuild the index.

## Required Top-Level Shape

```json
{
  "schema_version": "1.0.0",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "source": "markdown_frontmatter",
  "entries": []
}
```

## Required Entry Fields

Each entry must include:
- `path`
- `type`
- `module`
- `status`
- `authority`
- `created`
- `last_validated`

Optional fields:
- `tags`
- `source_of_truth`
- `derived_from`
- `summary`
- `warnings`

Entry fields align with `docs/FRONTMATTER-STANDARD.md`.

## Allowed Value Sets

Allowed `type` values:
- `canonical`
- `template`
- `task`
- `report`
- `audit`
- `verification`
- `example`
- `memory`
- `handoff`
- `derived`
- `unknown`

Allowed `status` values:
- `draft`
- `active`
- `canonical`
- `archived`
- `deprecated`
- `unknown`

Allowed `authority` values:
- `canonical`
- `supporting`
- `derived`
- `context`
- `unknown`

## Boundary Rules

| Boundary | Rule | Risk if Violated |
|---|---|---|
| index vs Markdown | Markdown remains source of truth | index drift may mislead agents |
| index vs frontmatter | index is derived from frontmatter | index may become second metadata owner |
| index vs approval | index must not approve anything | machine authority may replace human decision |
| index vs completion | index must not mark work correct | completion may be confused with correctness |
| index vs release | index must not decide release readiness | audit/release boundary may be bypassed |
| index vs self-healing | index rebuild is allowed later; policy repair is not | structural repair may become semantic mutation |

## Future Script Implications

| Future Script | Use of Schema | Must Not Do |
|---|---|---|
| `scripts/build-index.py` | generate `data/index.json` from Markdown/frontmatter | must not invent metadata or decisions |
| `scripts/validate-index.py` | validate generated index against schema and file existence | must not rewrite Markdown |
| `scripts/audit-metadata-consistency.py` | compare Markdown/frontmatter/index consistency | must not approve changes |

## Do Not Store in Index

Future `data/index.json` must not store as authority:
- approval decisions
- completion review decisions
- release readiness decisions
- ambiguous policy interpretation
- ambiguous risk classification
- active-task mutation authority
- self-healing authority
- SQLite authority
- vector RAG authority
- backend/service authority
- autonomous execution authority

## Non-Goals

This task does not:
- create `data/index.json`
- create `scripts/build-index.py`
- create `scripts/validate-index.py`
- migrate existing files
- change workflow/lifecycle behavior
