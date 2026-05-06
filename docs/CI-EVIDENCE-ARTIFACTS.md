---
type: canonical
module: m24
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# CI Evidence Artifacts

## Purpose
- CI evidence artifacts capture validation results.
- CI evidence artifacts support human review.
- CI evidence artifacts do not approve work.
- CI evidence artifacts do not enforce merge blocking.
- CI evidence is not approval.

## Core Principle
CI evidence is review input, not approval.

## Required CI Evidence Artifact
Standard artifact path:
- reports/ci/agentos-validate.json

Standard artifact name:
- agentos-validation-evidence

## Minimum CI Evidence Fields
CI Evidence
workflow:
run_id:
branch:
commit:
command:
exit_code:
result:
output_summary:
artifact_path:
human_action_required:

## Field Meanings
- workflow = name of the CI workflow that ran validation
- run_id = CI run identifier when available
- branch = branch being validated
- commit = commit SHA being validated
- command = validation command that produced the evidence
- exit_code = command exit code
- result = PASS / WARN / FAIL / ERROR / NOT_RUN / INCOMPLETE
- output_summary = short summary of command output
- artifact_path = path where evidence is stored
- human_action_required = YES / NO or true / false

## Result Semantics
- PASS means validation completed successfully.
- WARN means validation completed with warnings.
- FAIL means one or more checks failed.
- ERROR means validation could not complete correctly.
- NOT_RUN means a required check did not run.
- INCOMPLETE means evidence is missing required fields.
- NOT_RUN is not PASS.
- INCOMPLETE is not PASS.
- ERROR requires human review.
- FAIL requires human review.

## JSON Evidence Expectations
- JSON evidence should come from `python scripts/agentos-validate.py all --json`.
- JSON evidence must be valid JSON.
- JSON evidence must not mix human-readable output with JSON.
- Child command output should be captured inside output_summary.
- JSON evidence is automation evidence, not approval.

## Human-Readable Summary Expectations
- Human-readable summaries should be short.
- They should show result, command, exit code, warnings, failures, not-run checks, and next step.
- They should not claim approval.
- They should not claim implementation correctness.

## Advisory Boundary
- M24 stores and displays evidence.
- M24 does not enforce protected branches.
- M24 does not enforce required checks.
- M24 does not block merges.
- M24 does not approve changes.
- M25 may use this evidence standard for enforced CI.

## Non-Authority Boundaries
- CI evidence is not automatic approval.
- CI evidence is not a release gate.
- CI evidence is not a deployment gate.
- CI evidence is not proof of implementation correctness.
- CI evidence is not a security guarantee.
