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

## Canonical role
`quality/MAIN.md` is the canonical routing entry for verification and quality decisions, but deep quality content is still distributed across legacy-backed sources.

## Transitional sources
- `LAYER-1/testing-guide.md`
- `CHECKLIST.md`
- `LAYER-2/qa/verification-criteria.md`
- `LAYER-2/qa/test-scenarios.md`
- `LAYER-1/audit.md`
- `LAYER-1/audit-quick.md`

## Canonical vs legacy boundary
- Canonical routing lives here.
- Deep quality logic is still partially legacy-backed.
- Legacy sources must not become an alternate bootstrap.

## Migration exit criteria
- Canonical quality map is complete.
- Deep checks are classified.
- Release, audit, and verification roles are clearly separated.
- Legacy sources are referenced as supporting material, not hidden authority.

## Current operational rule
- Start from `quality/MAIN.md`.
- Open only the deep sources needed by trigger.
- Use workflow to execute checks and this module to decide which checks matter.
