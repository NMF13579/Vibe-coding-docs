# M25 Evidence Report

## Human Summary

M25 repository evidence is assembled here as facts, not approval.
The repository has the required contract, name, workflow, fixture, and override-policy artifacts.
The platform evidence is still `NEEDS_REVIEW`, so platform enforcement is not proved.
The enforcement audit script and fixture tests work as expected, but the unified validator still fails on existing repo checks.

## Evidence Boundary

- This evidence report is not approval.
- This evidence report is not a completion decision.
- This evidence report does not mark M25 complete.
- CI PASS is not human approval.
- Evidence report is not approval.
- Required checks do not replace owner review.
- Auto-merge is forbidden.
- Automatic approval is forbidden.
- Repository state = files in repo.
- Platform state = GitHub branch protection / required checks settings.
- This report does not prove platform enforcement unless platform evidence says so.

## Artifact Inventory

- path: `docs/ENFORCED-REQUIRED-CHECKS.md`
  status: PRESENT
  evidence: Contract document exists and defines the merge-gate behavior for M25.
- path: `templates/enforcement-review.md`
  status: PRESENT
  evidence: Advisory review template exists and is referenced by the audit script.
- path: `docs/REQUIRED-CHECK-NAMES.md`
  status: PRESENT
  evidence: Stable required check names are documented.
- path: `.github/workflows/agentos-validate.yml`
  status: PRESENT
  evidence: Workflow exists with the AgentOS Validate job and enforcement step.
- path: `docs/BRANCH-PROTECTION-SETUP.md`
  status: PRESENT
  evidence: Manual branch protection setup guide exists for dev and main.
- path: `templates/platform-enforcement-evidence.md`
  status: PRESENT
  evidence: Platform evidence template exists for per-branch GitHub settings proof.
- path: `reports/platform-required-checks-evidence.md`
  status: PRESENT
  evidence: Platform evidence report exists, but its final status is `NEEDS_REVIEW`.
- path: `scripts/audit-enforcement.py`
  status: PRESENT
  evidence: Read-only enforcement audit script exists and supports `--root`.
- path: `tests/fixtures/enforcement/`
  status: PRESENT
  evidence: Enforcement smoke fixtures exist for valid and invalid repository states.
- path: `scripts/test-enforcement-fixtures.py`
  status: PRESENT
  evidence: Fixture runner exists and checks expected audit outcomes.
- path: `docs/ENFORCEMENT-OVERRIDE-POLICY.md`
  status: PRESENT
  evidence: Override and bypass policy document exists.
- path: `templates/enforcement-override-record.md`
  status: PRESENT
  evidence: Override record template exists with required fields and rules.

## Required Checks Contract Evidence

- contract file present: YES
- PASS policy documented: YES
- WARN policy documented: YES
- FAIL / ERROR / NOT_RUN / INCOMPLETE blocking documented: YES
- PASS is not approval documented: YES
- auto-approval forbidden: YES
- auto-merge forbidden: YES

## Stable Check Names Evidence

- workflow name: AgentOS Validate
- job ID: agentos-validate
- job display name: agentos-validate
- required check name documented: YES
- expected required check: AgentOS Validate / agentos-validate

## Workflow Enforcement Evidence

- workflow exists: YES
- enforcement step present: YES
- evidence upload present: YES
- if: always() present: YES
- WARN blocks: YES
- FAIL blocks: YES
- ERROR blocks: YES
- NOT_RUN blocks: YES
- INCOMPLETE blocks: YES
- continue-on-error: true masking present: YES
- || true masking present: NO
- contents: write present: NO

## Branch Protection Setup Evidence

- setup guide present: YES
- branches documented: dev / main
- required check documented: YES
- force-push policy documented: YES
- branch deletion policy documented: YES
- bypass policy documented: YES
- platform evidence requirement documented: YES

## Platform Required Checks Evidence

- platform evidence report present: YES
- dev branch status: NEEDS_REVIEW
- main branch status: NEEDS_REVIEW
- final platform enforcement status: NEEDS_REVIEW
- required check confirmed on dev: UNKNOWN
- required check confirmed on main: UNKNOWN
- evidence source: Unavailable; read-only GitHub settings evidence was not available in this environment
- human verifier: UNKNOWN
- missing evidence: GitHub settings link, screenshot, export, or explicit human verifier statement
- gaps: No proof of branch protection, required checks, pull request review, force-push policy, branch deletion policy, bypass permissions, or admin bypass policy

## Enforcement Audit Evidence

- audit script present: YES
- audit command: `python3 scripts/audit-enforcement.py`
- audit result: NEEDS_REVIEW
- audit exit code: 1
- classification valid: YES
- warnings: Platform evidence is NEEDS_REVIEW.
- failures: none

## Enforcement Fixture Evidence

- fixture test script present: YES
- fixture directory present: YES
- fixture command: `python3 scripts/test-enforcement-fixtures.py`
- fixture result: PASS
- fixture failures: none
- valid fixture result: ENFORCEMENT_READY
- invalid fixture coverage summary: 8 invalid fixtures covered plus 1 valid fixture

## Override Policy Evidence

- override policy present: YES
- override record template present: YES
- silent bypass forbidden documented: YES
- owner approval requirement documented: YES
- expiry / one-time scope documented: YES
- override does not convert CI failure into PASS documented: YES
- override does not prove platform enforcement documented: YES
- actual override records created: NO

## Command Evidence

- command: `test -f reports/milestone-25-evidence-report.md`
  result: PASS
- command: `test -f docs/ENFORCED-REQUIRED-CHECKS.md`
  result: PASS
- command: `test -f docs/REQUIRED-CHECK-NAMES.md`
  result: PASS
- command: `test -f .github/workflows/agentos-validate.yml`
  result: PASS
- command: `test -f docs/BRANCH-PROTECTION-SETUP.md`
  result: PASS
- command: `test -f reports/platform-required-checks-evidence.md`
  result: PASS
- command: `test -f scripts/audit-enforcement.py`
  result: PASS
- command: `test -f scripts/test-enforcement-fixtures.py`
  result: PASS
- command: `test -f docs/ENFORCEMENT-OVERRIDE-POLICY.md`
  result: PASS
- command: `test -f templates/enforcement-override-record.md`
  result: PASS
- command: `python3 scripts/audit-enforcement.py`
  result: NEEDS_REVIEW
  exit code: 1
- command: `python3 scripts/test-enforcement-fixtures.py`
  result: PASS
  exit code: 0
- command: `python3 scripts/agentos-validate.py all`
  result: FAIL
  exit code: 1

## Warnings

- Platform evidence is `NEEDS_REVIEW`.
- Human verifier is `UNKNOWN`.
- Read-only GitHub settings evidence was unavailable.
- The unified validator still fails on existing repository checks.

## Failures

- `python3 scripts/agentos-validate.py all` failed with `Checks run: 3` and `Failed checks: 2`.
- Platform enforcement is not proven because the platform evidence remains `NEEDS_REVIEW`.

## Not Run

- None. The required commands were run.

## Remaining Gaps

- No read-only GitHub settings evidence for `dev` and `main`.
- No explicit human verifier identity for platform enforcement.
- Platform enforcement remains unproven at the GitHub settings level.
- The unified validator still fails on existing repository checks.

## Non-Authority Boundaries

- This report does not approve merge.
- This report does not approve release.
- This report does not configure branch protection.
- This report does not prove platform enforcement unless platform evidence says so.
- This report does not authorize auto-merge.
- This report does not authorize automatic approval.
- This report does not complete M25.

## Next Step

Task 25.10.1 — M25 Completion Review
