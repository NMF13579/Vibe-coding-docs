---
type: canonical
module: m24
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Required Checks Policy (Draft)

## Purpose
Этот документ описывает будущие обязательные проверки (required checks) для AgentOS.
Он подготавливает этап M25, где возможен принудительный режим.
В M24 принудительное включение не выполняется.

## Core Principle
M24 defines required checks policy; M24 does not enforce required checks.
Required checks are documented in M24, not enforced.

## Future Required Checks
Будущие обязательные проверки:
- agentos-validate all
- scope compliance
- scope fixtures
- execution audit
- CI evidence artifact presence
- milestone evidence report presence
- milestone completion review presence

## Required Check Semantics
- PASS means the check can be accepted.
- WARN means review is required before acceptance.
- FAIL blocks acceptance in enforced mode.
- ERROR blocks acceptance in enforced mode.
- NOT_RUN blocks acceptance in enforced mode.
- INCOMPLETE blocks acceptance in enforced mode.

## Advisory vs Enforced Mode
- In M24, required checks are documented only.
- In M24, checks may run in CI but are not branch-protection requirements.
- In M24, failed checks provide evidence for review.
- In M25, these checks may become enforced via protected branches and required checks.
- M25 may introduce enforced required checks.

## Human Review Boundary
- Required checks do not replace human review.
- PASS does not prove implementation correctness.
- WARN / FAIL / ERROR / NOT_RUN require human inspection.
- Overrides, if allowed in future, must be explicit and documented.

## Future M25 Enforcement Candidates
- protected branch required check for agentos-validate all
- required scope compliance check
- required fixture check
- required execution audit check
- required CI evidence artifact
- required evidence report
- required completion review

## Non-Goals for M24
- no protected branch enforcement
- no required checks enforcement
- no CODEOWNERS enforcement
- no no-merge policy
- no automatic approval
- no release gate
- no deployment gate

## M24 Boundaries
- M24 does not implement protected branch enforcement.
- M24 does not implement required checks enforcement.
- M24 does not implement CODEOWNERS enforcement.
- M24 does not implement automatic approval.
