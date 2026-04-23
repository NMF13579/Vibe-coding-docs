# Architecture validators

Minimal guardrail layer for the modular routing architecture.

## Local run

```bash
bash scripts/validate-architecture.sh
```

Or run separately:

```bash
python3 scripts/validate-docs.py
python3 scripts/validate-route.py
python3 scripts/check-links.py
```

## What is checked

- `validate-docs.py`
  - module `MAIN.md` exists for core and optional modules
  - frontmatter exists and required fields are present
  - `when_to_read` is `always` for core and `conditional` for optional
- `validate-route.py`
  - `llms.txt` remains canonical bootstrap and includes modular primary route
  - `START.md` remains human entry and points to `ROUTES-REGISTRY.md`
  - adapter entry docs point to canonical route
  - primary route does not reference deprecated legacy docs
  - `ROUTES-REGISTRY.md` line limit (<=150)
- `check-links.py`
  - local markdown links are valid in primary-route files

## Intentionally not checked

- Full-repository semantic link graph (kept scope narrow to reduce false positives)
- Automatic content fixing or auto-migration
- Full policy linting across all legacy docs
