# Enforcement Override Policy

## Purpose

This policy defines how enforcement overrides and bypass paths must be handled for M25.
It exists to prevent silent bypass and to keep merge-gate enforcement explicit, documented, and reviewable.

## Enforcement boundary

M25 defines the merge-gate enforcement boundary.
This policy does not change platform state, branch protection, workflow behavior, or CI behavior.
It only defines how human override and bypass decisions are recorded and reviewed.

## Definitions

Override = explicit documented human decision to proceed despite a warning or controlled exception.

Bypass = platform or permission path that allows enforcement to be avoided.

Silent bypass = bypass without documented reason, evidence, reviewer identity, and record path.

## Override vs bypass

An override is a documented human decision.
A bypass is a platform or permission path.
An override may respond to a visible warning or a controlled exception.
A bypass can skip enforcement unless it is controlled, documented, and reviewed.

Override must be explicit, documented, and traceable.
Bypass must never be treated as invisible or automatic.

## Allowed override cases

- WARN with documented human enforcement review
- Documented platform limitation with owner approval
- Temporary emergency exception with explicit expiry
- Administrative bypass only when recorded with reason and reviewer identity

## Forbidden override cases

- FAIL cannot be silently overridden
- ERROR cannot be silently overridden
- NOT_RUN cannot be silently overridden
- INCOMPLETE cannot be silently overridden
- Missing AgentOS validation cannot be treated as PASS
- Unknown platform state cannot be treated as enforcement

## Silent bypass forbidden

Silent bypass is forbidden.
Silent bypass cannot be accepted, hidden, or implied.
Any bypass must have a documented reason, evidence, reviewer identity, and record path.
If those items are missing, the bypass is not acceptable.

## Required override evidence

Every override record must include:

- reason
- evidence
- reviewer identity
- owner approval when blocking results are present
- record path
- expiry or one-time scope

Evidence must be sufficient for later review.
Evidence must show what was decided, who decided it, and why the exception was allowed.

## Reviewer identity requirement

The reviewer must be identified by name, account, or other durable human identity.
Anonymous approval is not acceptable.
Owner approval must identify the owner who approved the exception.

## Expiration and one-time use

Each override applies once.
Each override must have an expiry or explicit one-time scope.
Open-ended override is forbidden.
If the exception is needed again, it must be recorded again and reviewed again.

## Blocking result policy

FAIL, ERROR, NOT_RUN, and INCOMPLETE require resolution or explicit owner-level override record.
A normal reviewer cannot silently convert blocking results into PASS.
WARN may proceed only with documented human enforcement review.
Owner-level override may allow a documented exception, but it does not convert the underlying check result to PASS and does not prove platform enforcement.

## WARN handling

WARN is not silent approval.
WARN may proceed only when a human enforcement review is documented.
The review must explain the warning, the risk accepted, and the reason the exception is allowed.
If the warning cannot be explained, the result must remain blocked or be escalated for owner review.

## Admin bypass policy

Admin bypass must be disabled or explicitly documented.
Silent admin bypass is forbidden.
Admin bypass does not equal approval.
Admin bypass does not authorize auto-merge.
If admin bypass exists, it must be recorded with reason, reviewer identity, and evidence.

## Emergency override policy

Emergency override requires reason, evidence, human reviewer identity, owner approval, and follow-up action.
Emergency override must not become permanent policy.
Emergency use does not remove the need for traceability.
Emergency use does not convert CI failure into PASS.

## Non-approval statement

CI PASS is not human approval.
Evidence report is not approval.
Required checks do not replace owner review.
Automatic approval is forbidden.
Auto-merge is forbidden.
Override does not authorize auto-merge.
Override does not authorize automatic approval.

## Non-goals

This policy does not configure branch protection.
This policy does not approve pull requests.
This policy does not create automation.
This policy does not weaken enforcement.
This policy does not replace platform state with repository state.

## Relationship to M25 and M26

M25 closes merge-gate enforcement.
M26 handles pre-merge agent execution corridor.
This policy belongs to M25 exception handling and must not weaken M25 enforcement.
It must not imply that overrides are automatic.
It must not imply that bypass is acceptable without documentation.
It must not imply that override converts CI failure into PASS.
It must not imply that override proves platform enforcement.
