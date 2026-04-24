---
type: canonical
module: architecture
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Operating Rules (Post-migration)

## Purpose
Practical rules to keep modular architecture stable after migration.

## Document placement rules
- Create a new **module** only when it introduces a new routing domain.
- Otherwise add a **secondary doc** under an existing module.
- Do not create new root-level entry files without explicit owner approval.

## Canonical authority rules
- Agent bootstrap authority: `llms.txt`.
- Human entry authority: `START.md`.
- Routing hub authority: `ROUTES-REGISTRY.md`.
- Module authority: module `MAIN.md` files.
- Entry docs outside modules are pointer-only and are non-authority.

## Deprecation rules
- Remove retired routes once a real successor module entry exists.
- Keep only active canonical paths in the working tree.
- Any replacement note must include the canonical successor path.

## Anti-drift rules
- Do not introduce alternate bootstrap in pointer docs or root docs.
- Do not route primary onboarding through removed or retired docs.
- Keep `ROUTES-REGISTRY.md` concise and aligned with actual module status.

## Maintenance rule
- Run `bash scripts/validate-architecture.sh` before merge for route/metadata/link guardrails.
