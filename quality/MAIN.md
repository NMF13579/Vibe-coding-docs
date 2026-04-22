---
type: canonical
module: quality
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Quality

## Purpose
Optional entry for verification, testing, and release-quality checks.
Used when implementation, release, or risk level requires explicit validation.

## When to read
- Before declaring task done.
- Before merge/release checks.
- When owner asks for audit/quality pass.

## Verification scope (current)
- Manual verification steps and expected outcomes.
- Smoke checks after deploy.
- Audit and quick-audit control checks.

## Active legacy quality sources
- `LAYER-1/testing-guide.md`
- `CHECKLIST.md`
- `LAYER-2/qa/verification-criteria.md`
- `LAYER-2/qa/test-scenarios.md`
- `LAYER-1/audit.md` and `LAYER-1/audit-quick.md`

## Relation to workflow and done
- Workflow defines execution order; quality validates result.
- Done requires completed checks relevant to risk/scope.
- If checks are incomplete, task remains not done.

## Known gaps
- Quality rules are still split across several legacy files.
- Unified deep quality playbook migration is pending.

## Routing
- Read this module when verification trigger matches.
- Start from `LAYER-1/testing-guide.md`; add release checks via `CHECKLIST.md`.
- For full health check, route to `LAYER-1/audit.md`.
