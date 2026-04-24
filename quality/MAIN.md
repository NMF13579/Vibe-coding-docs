---
type: canonical
module: quality
status: transitional
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Quality

## Purpose
Canonical entry for verification, testing, release-readiness, and audit routing.
This module surfaces the operational quality backbone while deeper detail still lives in approved legacy sources during migration.

## When to read
- Before declaring task done.
- Before merge or release checks.
- When the owner asks for verification, audit, or risk review.
- When a change needs explicit proof, not just a claim.
- When checks are likely to branch into deeper audit or incident follow-up.

## Verification scope (current)
- Routine checks cover manual verification, smoke checks, and evidence-backed readiness checks.
- Audit depth is chosen by trigger: quick audit for a short pass, full audit when risk or scope is broader.
- Use the smallest check set that can prove the change, then escalate only if something is unclear.
- Quality decides which checks matter; workflow executes the checks.

## Quality routing and triggers
- Enter quality when the task is about proof, readiness, release safety, or audit.
- Use `LAYER-1/testing-guide.md` for the basic "how to verify" flow and error reporting.
- Use `LAYER-1/audit-quick.md` for a short health check when you only need a quick pass.
- Use `LAYER-1/audit.md` when the review is broader, owner-facing, or release-critical.
- If the trigger is unclear, stay on the quality route and open the smallest legacy source that answers the question.

## Verification and readiness
- `CHECKLIST.md` holds release-oriented readiness items and should be treated as a checkpoint, not as new governance.
- `LAYER-2/qa/verification-criteria.md` defines the evidence expected when a task claims it is verified.
- `LAYER-2/qa/test-scenarios.md` gives smoke scenarios that prove the route and context flow still work.
- Use concrete evidence: observed result, command output, browser behavior, or clearly described manual check.
- If automatic proof is not possible, mark it as manual verification instead of pretending it is complete.
- Do not promote one checklist item into a universal project rule unless the source clearly does that.

## Audit depth and escalation
- The quick audit is a short daily-style check: state, handoff, links, adapters, blockers, session log, next step.
- Treat the quick route as a 5–7 point check for basic health, not as a replacement for the full audit path.
- If any point is no or unclear, stop the quick route and follow the full audit route instead.
- Quick integrity checks: links ok, metadata ok, bootstrap unique, adapters pure.
- The full audit is a structured audit path with state checks, structure validation, health scoring, and summary.
- Use the quick route when the question is "is the system still basically healthy?"
- Use the full route when the question is "are we safe to release or hand off?"
- If a red flag appears, stop and follow the audit route rather than turning it into ordinary workflow.

## Canonical role
`quality/MAIN.md` is the canonical routing entry for verification and quality decisions, but deep quality content is still partially legacy-backed.
It is canonical for deciding what to verify and when, not for replacing the detailed legacy proof material yet.

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
- Audit detail, test examples, and release-readiness proof remain direct-read sources.

## Migration exit criteria
- Canonical quality map is complete.
- Deep checks are classified.
- Release, audit, and verification roles are clearly separated.
- Legacy sources are referenced as supporting material, not hidden authority.

## Current operational rule
- Start from `quality/MAIN.md`.
- Open only the deep sources needed by trigger.
- Use workflow to execute checks and this module to decide which checks matter.
- If the exact proof or checklist detail is unclear, open the legacy source directly instead of inventing it.

## Migration boundary
- This module partially surfaces approved legacy quality content from `LAYER-1/testing-guide.md`, `CHECKLIST.md`, `LAYER-2/qa/verification-criteria.md`, `LAYER-2/qa/test-scenarios.md`, `LAYER-1/audit.md`, and `LAYER-1/audit-quick.md`.
- Those legacy sources still require direct read for full procedures, scenario detail, and audit step depth.
- `quality/MAIN.md` is canonical for quality entry and routing guidance, but not yet the sole deep source.
- Do not use this module to duplicate governance authority from `core-rules/MAIN.md`, execution sequencing from `workflow/MAIN.md`, state authority from `state/MAIN.md`, or incident recovery detail from `incidents/MAIN.md`.
