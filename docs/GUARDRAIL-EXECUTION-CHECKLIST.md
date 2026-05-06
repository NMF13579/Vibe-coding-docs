---
type: canonical
module: m23
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Guardrail Execution Checklist

## Purpose
This checklist is a review aid used before accepting agent execution results. It ensures scope and evidence checks are visible and complete.

## Usage
Use this checklist after execution and before acceptance review. Fill every item using real command evidence.

## Required Pre-Acceptance Checks
Pre-Acceptance Checklist

- [ ] git status checked
- [ ] scope compliance checked
- [ ] changed files reviewed
- [ ] staged changes reviewed
- [ ] untracked files reviewed
- [ ] validators run
- [ ] fixture runner run when relevant
- [ ] invalid fixtures not hidden
- [ ] NOT_RUN explained
- [ ] ERROR reviewed
- [ ] FAIL reviewed
- [ ] WARN reviewed or accepted
- [ ] human summary present
- [ ] scope summary present
- [ ] evidence block present
- [ ] no forbidden files changed
- [ ] sensitive paths reviewed
- [ ] human review required when scope violation exists

## Scope Compliance Checks
Required scope commands:
- git status --short
- git diff --name-status
- git diff --name-status --cached
- git ls-files --others --exclude-standard
- python scripts/check-scope-compliance.py --task tasks/active-task.md
- python scripts/check-scope-compliance.py --task tasks/active-task.md --json

## Changed Files Evidence Checks
Review must include tracked, staged, and untracked changes. Missing changed files evidence blocks acceptance.

## Validation Evidence Checks
Validators run status, command, and exit code must be recorded. Missing scope compliance evidence blocks acceptance.

## Fixture Evidence Checks
When scope validator changes are relevant, run fixture coverage:
- python scripts/test-scope-compliance-fixtures.py

Invalid fixture failures must remain visible and must not be hidden.

## Summary Evidence Checks
Human summary and scope summary must both be present and consistent with validator outputs.

## Human Review Checks
Human review is required for scope violations.
Human review is required for sensitive path changes.
Human review is required for missing evidence.
Human review is required for ERROR results.
Human review is required for FAIL results.
Human review or documented acceptance is required for WARN results.
Human override must be explicit and documented.

## Blocking Conditions
Scope violation blocks acceptance unless a human explicitly overrides.
Forbidden file changes block acceptance unless a human explicitly overrides.
Missing changed files evidence blocks acceptance.
Missing scope compliance evidence blocks acceptance.
NOT_RUN is not PASS.
ERROR requires human review.
FAIL requires human review.
INCOMPLETE is not PASS.

## Non-Authority Boundaries
Unsafe claims that are rejected:
- checklist approves task completion
- checklist proves correctness
- checked items mean implementation is correct
- PASS means human review is unnecessary
- NOT_RUN can be treated as PASS
- missing evidence can be ignored
- scope violations can be auto-approved
- validator output replaces human review

This checklist does not approve completion and does not prove implementation correctness.
