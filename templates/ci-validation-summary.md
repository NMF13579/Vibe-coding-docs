---
type: template
module: m24
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# CI Validation Summary

## Human Summary
Result: PASS | WARN | FAIL | ERROR | NOT_RUN | INCOMPLETE
Reason:
Next step:

## CI Evidence
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

## Validation Result
Allowed values:
- PASS
- WARN
- FAIL
- ERROR
- NOT_RUN
- INCOMPLETE

## Checks
- command:
  exit_code:
  result:
  output_summary:

## Warnings
- NONE

## Failures
- NONE

## Not Run
- NONE

## Human Action Required
- YES | NO

## Artifact Reference
- reports/ci/agentos-validate.json
- agentos-validation-evidence

## Review Boundary
- CI evidence is not approval.
- PASS does not prove implementation correctness.
- NOT_RUN is not PASS.
- INCOMPLETE is not PASS.
- ERROR requires human review.
- FAIL requires human review.

## Next Step
- Human review of warnings, failures, errors, and not-run checks.
