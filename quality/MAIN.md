---
type: canonical
module: quality
status: canonical
authority: canonical
when_to_read: always
owner: unassigned
---

# Quality

## Purpose

Canonical module for verification, smoke checks, release blockers, and audit output.
Quality decides what proof is required; workflow executes the checks.

## When To Use

- Before declaring a task done.
- Before merge or release readiness.
- When the owner asks for verification, audit, or risk review.
- When a change needs concrete proof instead of a claim.
- When a red flag could affect core behavior, safety, or user-critical flow.

## Verification

- Verification must be evidence-based.
- Evidence can be command output, observed behavior, test result, or clearly described manual check.
- Use the smallest check set that proves the task.
- If automatic proof is not possible, mark the result as manual verification.
- A task is verified only when acceptance criteria are supported by proof.
- Do not claim completion when checks were skipped or could not run.

## Verification Gates

Gate 1 — Structure

- Files, routes, and links are present and consistent.

Gate 2 — Scope

- Only the confirmed task scope was changed.

Gate 3 — Acceptance Criteria

- Every acceptance criterion has proof.

Gate 4 — Regression / Smoke

- Relevant validation or smoke checks were run, or skipped with an explicit reason.

Gate 5 — Security / Release Blockers

- If data, access, API, auth, database, release, or CI is affected, security proof is required.

- The agent must not claim done or complete if the gates were not passed or explicitly explained.

## Smoke Checks

- Smoke checks confirm that the main route still opens, the core action still works, and no obvious failure blocks the user.
- For documentation-only work, smoke checks confirm that required routes point to the intended canonical module.
- For script or validator work, smoke checks confirm that the relevant command exits successfully.
- If a smoke check fails or is unclear, stop and report the failure before declaring readiness.

## Release Blockers

Block release when any of these are true:

- Data safety is unclear or broken.
- Security checks fail or were not performed for sensitive work.
- A core user path is broken.
- Required state, route, or verification proof is missing.
- A blocker affects core functionality, safety, or user-critical flows.

## Audit Output

Audit reports must be plain-language and evidence-backed:

- what works;
- what is missing;
- runtime risks;
- critical blockers;
- secondary blockers;
- top next steps.

Saving an audit result as a file requires explicit owner approval.

## Boundaries

- Do not define governance authority here; use `core-rules/MAIN.md`.
- Do not define execution sequence here; use `workflow/MAIN.md`.
- Do not define state transitions here; use `state/MAIN.md`.
- Do not define security policy here; use `security/MAIN.md`.
