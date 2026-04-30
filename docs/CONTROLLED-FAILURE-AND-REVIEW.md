# Controlled Failure and Review

## 1. Purpose

Controlled failure and review is a safety model for tasks that cannot safely
complete.

completion readiness not PASS does not automatically mean task failed.

## 2. Relationship to Controlled Completion

This model is aligned with:

- docs/CONTROLLED-COMPLETION.md
- docs/COMPLETION-READINESS.md
- docs/COMPLETION-TRANSITION.md

Rules:

- PASS may allow completion preparation
- FAIL / PARTIAL / NOT RUN must not become successful completion
- M14 may classify alternatives
- M14 must not apply alternatives

## 3. Controlled Alternative Outcomes

Outcomes are candidates only. In M14 they are not applied lifecycle mutations.

Completion readiness not PASS does not automatically mean task failed.

### needs_review

Use when:

- human review is pending
- evidence is incomplete but not invalid
- human judgment is required
- some changed files are known but list may be partial

### failed

Use when:

- verification failed
- scope check failed
- evidence report failed
- execution session failed with explicit evidence
- output violates acceptance criteria

### blocked

Use when:

- required evidence is missing
- source_contract is missing
- acceptance criteria are missing
- execution session is missing
- changed files are unknown
- human review status is missing when review is required

### manual_abort

Use only when explicitly recorded:

- manual_abort
- abort_reason: manual_abort

Must not be inferred from missing evidence.

## 4. stop_reason Mapping

```yaml
stop_reason_mapping:
  human_review_pending: needs_review
  human_review_missing: blocked
  changed_files_incomplete: needs_review
  source_contract_missing: blocked
  acceptance_criteria_missing: blocked
  changed_files_unknown: blocked
  active_task_missing: blocked
  session_missing: blocked
  evidence_missing: blocked
  readiness_fail: blocked
  scope_violation: failed
  verification_fail: failed
  evidence_report_fail: failed
  watchdog_abort: failed
  manual_abort: manual_abort
```

Rules:

- mapping is advisory in M14
- mapping does not apply lifecycle transition
- readiness_fail is fallback only
- prefer specific stop_reason over readiness_fail

## 5. Terminology

Definitions:

- changed_files_incomplete = some changed files known, list may be partial
- changed_files_unknown = no changed files information available
- human_review_pending = review required and status pending
- human_review_missing = review required and status absent
- blocked as outcome vs blocked as candidate status must be interpreted by context

## 6. Candidate Statuses

Possible candidate statuses:

- candidate
- blocked
- reviewed

Forbidden in M14:

- applied

status: applied is forbidden in M14.

## 7. Evidence Requirements

Future alternative candidate evidence should include:

- task_id
- source_task
- session_id if available
- completion_readiness_result
- stop_reason
- candidate_outcome
- failing_gate if known
- missing_evidence if known
- notes

Task 14.7.1 does not create candidate records.

## 8. Safety Boundaries

M14 MUST NOT:

- move task to failed/
- move task to done/
- move task to blocked/
- mutate tasks/active-task.md
- advance queue
- apply failure transition
- apply needs-review transition
- apply blocked transition
- apply manual_abort transition
- generate approval
- deploy
- merge
- rollback

## 9. Expected Result

AgentOS can classify why successful completion is not allowed,
but cannot apply failure, review, blocked, or abort lifecycle transitions in M14.
