---
type: canonical
module: m24
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# CI Advisory Mode

## Purpose
CI advisory mode дает видимость результатов проверок и создает доказательства для ревью человеком.
CI advisory mode не принимает решение о приемке изменений.
CI evidence is not approval.

## Core Principle
Advisory CI provides visibility, not enforcement.

## What Advisory CI May Do
- run AgentOS validation
- run `scripts/agentos-validate.py all`
- run `scripts/agentos-validate.py all --json`
- upload CI evidence artifacts
- report PASS / WARN / FAIL / ERROR / NOT_RUN
- support human review
- expose validation gaps

## What Advisory CI Must Not Do
- configure protected branches
- configure required checks
- block merges by policy
- approve changes
- auto-merge changes
- push commits
- deploy
- release
- override human review
- convert FAIL / ERROR / NOT_RUN into PASS

## Result Semantics
- PASS means checks completed successfully.
- WARN means checks completed with warnings.
- FAIL means one or more checks failed.
- ERROR means validation could not complete correctly.
- NOT_RUN means a required check did not run.
- NOT_RUN is not PASS.
- ERROR requires human review.
- FAIL requires human review.
- WARN should be reviewed before acceptance.

## Human Review Rules
- CI advisory output is evidence, not approval.
- A human reviewer remains responsible for acceptance.
- Human review must inspect failures, warnings, errors, and not-run checks.
- A green advisory CI result does not prove implementation correctness.

## Evidence Expectations
Минимальный набор доказательств в CI:
- workflow name
- branch
- commit
- command
- exit code
- result
- output summary
- artifact path
- human_action_required

## Boundary with M25
- M24 defines advisory validation.
- M24 does not implement required checks.
- M24 does not implement protected branch enforcement.
- M24 does not implement merge blocking.
- M25 may introduce enforced CI/protected branch required checks.
- M24 does not implement required checks enforcement.

## Non-Authority Boundaries
- CI advisory mode is not automatic approval.
- CI advisory mode is not a release gate.
- CI advisory mode is not a deployment gate.
- CI advisory mode is not a security guarantee.
- CI advisory mode is not proof that implementation is correct.
- M24 does not implement automatic approval.
