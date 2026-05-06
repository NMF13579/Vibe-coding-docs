# Branch Protection Setup Guide

## Purpose
This document provides a clear manual setup guide for enabling AgentOS required checks through GitHub protected branch settings.

## Enforcement boundary
This guide does not enable branch protection by itself.
Branch protection is GitHub platform state.
M25 cannot be considered fully enforced until platform evidence confirms required checks are enabled.
Repository files alone are not proof of platform enforcement.

## Repository state vs platform state
- Repository state  = files in repo
- Platform state    = GitHub branch protection / required checks settings
- Platform evidence = human-verified proof that GitHub settings are enabled

## Prerequisites
- Maintainer or Admin access to the repository on GitHub.
- The workflow containing the required check has been executed at least once so it appears in the GitHub UI.

## Branches to protect
Required protected branches:
- `dev`
- `main`

## Required status checks
Require status checks to pass before merging.
PASS is not human approval.
Required checks do not replace owner review.
Skipped / neutral / missing AgentOS validation must not be treated as PASS.

## Required check name
Require the `AgentOS Validate / agentos-validate` check.

## Pull request review requirements
Require pull request review before merge.
Auto-merge is forbidden.
Automatic approval is forbidden.

## Bypass policy
Limit bypass permissions.
Document any bypass or override.

## Force-push policy
Disallow force pushes.

## Branch deletion policy
Disallow branch deletion.

## Admin bypass guidance
Disable admin bypass or explicitly document it with reason and record path.

## Manual setup steps
1. Navigate to the repository settings on GitHub.
2. Select "Branches" under "Code and automation".
3. Click "Add branch protection rule".
4. Follow the policies defined above for the `dev` and `main` branches.

## Verification checklist
- [ ] Branch protection is enabled on dev
- [ ] Branch protection is enabled on main
- [ ] AgentOS Validate / agentos-validate is listed as required status check
- [ ] Required status checks to pass before merging: enabled
- [ ] Pull request review is required before merge
- [ ] Force push is disabled on dev
- [ ] Force push is disabled on main
- [ ] Branch deletion is disabled on dev
- [ ] Branch deletion is disabled on main
- [ ] Bypass permissions are documented
- [ ] Admin bypass is disabled or documented with reason and record path
- [ ] Platform evidence must be collected in Task 25.5.1 after manual setup

## Evidence collection boundary
Create one platform enforcement evidence record per protected branch.
dev and main must be verified separately.
Platform evidence must be collected in Task 25.5.1 after manual setup.

## Non-goals
- Do not configure branch protection directly via repository files.
- Do not add GitHub API automation for branch protection.
- Do not use gh CLI to configure branch protection.

## Relationship to M25
This guide is part of Task 25.4.1. M25 cannot be considered fully enforced until platform evidence is collected in Task 25.5.1.
