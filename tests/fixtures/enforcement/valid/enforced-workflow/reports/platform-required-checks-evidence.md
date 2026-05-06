# Platform Required Checks Evidence

## Purpose
This report records platform evidence for GitHub branch protection and required checks for AgentOS.

## Evidence boundary
- Repository state = files in repo.
- Platform state = GitHub branch protection / required checks settings.
- Repository files alone are not proof of platform enforcement.
- This evidence report is not approval.
- This evidence report does not authorize auto-merge.
- This evidence report does not authorize automatic approval.
- PASS is not human approval.
- Required checks do not replace owner review.

## Branch evidence: dev
- Protected branch enabled: YES
- Required status checks enabled: YES
- Required check observed: AgentOS Validate / agentos-validate
- Expected required check: AgentOS Validate / agentos-validate
- Match: YES
- Pull request review required: YES
- Force-push allowed: NO
- Branch deletion allowed: NO
- Bypass permissions: NONE
- Bypass reason: none
- Bypass record path: none
- Admin bypass allowed: NO
- Admin bypass reason: none
- Admin bypass record path: none
- Evidence source: Read-only GitHub UI observation
- Screenshot / link / audit reference: https://example.invalid/dev
- Gaps found: none
- Branch status: PLATFORM_ENFORCED

## Branch evidence: main
- Protected branch enabled: YES
- Required status checks enabled: YES
- Required check observed: AgentOS Validate / agentos-validate
- Expected required check: AgentOS Validate / agentos-validate
- Match: YES
- Pull request review required: YES
- Force-push allowed: NO
- Branch deletion allowed: NO
- Bypass permissions: NONE
- Bypass reason: none
- Bypass record path: none
- Admin bypass allowed: NO
- Admin bypass reason: none
- Admin bypass record path: none
- Evidence source: Read-only GitHub UI observation
- Screenshot / link / audit reference: https://example.invalid/main
- Gaps found: none
- Branch status: PLATFORM_ENFORCED

## Required check verification
- Expected required check: AgentOS Validate / agentos-validate
- Dev branch verified: YES
- Main branch verified: YES
- Result: Required check is confirmed at the platform level.

## Review requirement verification
- Dev branch review requirement: YES
- Main branch review requirement: YES
- Result: Required pull request review is confirmed at the platform level.

## Force-push verification
- Dev branch force-push policy: NO
- Main branch force-push policy: NO
- Result: Force-push is disabled at the platform level.

## Branch deletion verification
- Dev branch branch deletion policy: NO
- Main branch branch deletion policy: NO
- Result: Branch deletion is disabled at the platform level.

## Bypass permission verification
- Dev branch bypass permissions: NONE
- Main branch bypass permissions: NONE
- Result: No bypass permissions are configured.

## Admin bypass verification
- Dev branch admin bypass: NO
- Main branch admin bypass: NO
- Result: Admin bypass is disabled.

## Gaps found
- none

## Final platform enforcement status
- Final platform enforcement status: PLATFORM_ENFORCED

## Human verifier
- Fixture Verifier

## Non-approval statement
- This evidence report is not approval.
- This evidence report does not authorize auto-merge.
- This evidence report does not authorize automatic approval.
- PASS is not human approval.
- Required checks do not replace owner review.

## Remaining actions
- none
