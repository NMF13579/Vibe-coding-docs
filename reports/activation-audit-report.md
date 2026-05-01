# Activation Audit Report

## Purpose
Audit the Milestone 11 activation mechanism and confirm that safe semi-automation remains bounded to one controlled transition.

## Scope
This audit covers activation only.
It does not audit task execution.
It does not audit task completion.
It does not audit queue processing.
It does not audit release approval.

## Audit Inputs
- `docs/SAFE-TRANSITION-EXECUTION.md`
- `docs/APPROVED-MODE-CONTRACT.md`
- `scripts/activate-task.py`
- `tools/state/ACTIVATE-TASK.md`
- `docs/ACTIVE-TASK-FORMAT.md`
- `tests/fixtures/negative/activation/`
- `scripts/test-activation-fixtures.py`
- `tools/state/TEST-ACTIVATION-FIXTURES.md`
- `reports/activation-positive-smoke.md`
- `scripts/agentos-validate.py`
- `tools/validation/AGENTOS-VALIDATE.md`

## Commands Run
| Command | Status | Notes |
|---|---|---|
| `python3 scripts/activate-task.py --help` | PASS | Exit code `0`, help output shown |
| `python3 scripts/test-activation-fixtures.py` | PASS | `Activation negative fixtures: PASS` |
| `python3 scripts/agentos-validate.py activation-fixtures` | PASS | Wrapper reports `[PASS] activation-fixtures` and fixture suite `PASS` |
| `git diff -- tasks/active-task.md` | PASS | No diff |

## activate-task.py Checks
| Check | Expected | Evidence | Status |
|---|---|---|---|
| CLI mode required | exactly one of `--dry-run` / `--approved` | code + `missing-approved-flag`, `both-approved-and-dry-run` | PASS |
| task path exists | missing task path fails | code path check | PASS |
| approval path exists | missing approval fails | `missing-approval-marker` | PASS |
| detect script call | `detect-task-state.py` must run | code (`subprocess`) | PASS |
| detect JSON parse | invalid JSON fails | code (`json.loads`) | PASS |
| analysis conflict blocked | `analysis_status=conflict` blocks | `analysis-status-conflict` | PASS |
| analysis invalid blocked | `analysis_status=invalid` blocks | `analysis-status-invalid` | PASS |
| validate state call | `validate-task-state.py` required | code (`subprocess`) | PASS |
| transition check call | `check-transition.py --to active` required | code + `check-transition-fail` | PASS |
| approval validator call | `validate-approval-marker.py --scope activate_task --transition approved_for_execution:active` | code (`subprocess`) | PASS |
| approval frontmatter parse | parse marker fields | code parse function | PASS |
| marker task match | marker `task_id` must match | `wrong-task-id` | PASS |
| marker scope check | scope must be `activate_task` | `wrong-scope` | PASS |
| marker transition check | transition must match when present | `wrong-transition` | PASS |
| marker status check | status must be `approved` | `revoked-approval-marker` and code | PASS |
| revoked marker rejected | revoked fields/status fail | `revoked-approval-marker` | PASS |
| expired marker rejected | expired timestamp fails | `expired-approval-marker` | PASS |
| related contract check | existing file required when declared | `contract-missing` | PASS |
| overwrite protection | different active task is blocked | `active-task-different-task` | PASS |
| dry-run no write | `--dry-run` never writes | `dry-run-does-not-write` | PASS |
| approved write gating | write only after all checks | code + positive smoke report | PASS |

## Allowed Write Scope
`activate-task.py` may write only `tasks/active-task.md`, and only when:
- transition is `approved_for_execution -> active`
- explicit `--approved` is present
- all checks pass

## Forbidden Writes
Activation must not write:
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `approvals/`
- `reports/verification.md`
- `TASK.md`
- `REVIEW.md`
- `TRACE.md`
- contract drafts
- git state

## Dry-Run Behavior
- `--dry-run` runs checks but does not write `tasks/active-task.md`.
- dry-run PASS is verification, not permission.
- Evidence: `dry-run-does-not-write` case in negative fixtures -> PASS.

## Approved Mode Behavior
- `--approved` is required for write.
- `--approved` does not bypass validation.
- approval marker alone is insufficient.
- Evidence:
  - `missing-approved-flag` -> PASS (rejected)
  - `approval-marker-valid-but-no-approved` -> PASS (rejected)
  - positive smoke report (`reports/activation-positive-smoke.md`) -> PASS

## Overwrite Behavior
- existing `active-task.md` for another task blocks activation.
- same `task_id` can be idempotent re-activation (implemented in code path).
- existing `active-task.md` without `task_id` is rejected by parser check.
- Evidence:
  - `active-task-different-task` -> PASS
  - source code review in `scripts/activate-task.py`

## Negative Fixture Coverage
| Case | Expected | Status |
|---|---|---|
| missing-approved-flag | rejected, no write | PASS |
| both-approved-and-dry-run | rejected, no write | PASS |
| missing-approval-marker | rejected, no write | PASS |
| invalid-approval-marker | rejected, no write | PASS |
| expired-approval-marker | rejected, no write | PASS |
| revoked-approval-marker | rejected, no write | PASS |
| wrong-task-id | rejected, no write | PASS |
| wrong-scope | rejected, no write | PASS |
| wrong-transition | rejected, no write | PASS |
| analysis-status-invalid | rejected, no write | PASS |
| analysis-status-conflict | rejected, no write | PASS |
| check-transition-fail | rejected, no write | PASS |
| contract-missing | rejected, no write | PASS |
| active-task-different-task | rejected, no overwrite | PASS |
| dry-run-does-not-write | no write in dry-run mode | PASS |
| approval-marker-valid-but-no-approved | rejected, no write | PASS |

## Positive Smoke Evidence
- Source: `reports/activation-positive-smoke.md`
- Recorded result in report: `Result: PASS`
- Evidence summary: valid approved activation created `tasks/active-task.md` in isolated temp workspace only.
- Status: PASS

## Unified CLI Integration
- `python3 scripts/agentos-validate.py activation-fixtures` exists and runs.
- It calls `scripts/test-activation-fixtures.py`.
- It does not expose `agentos-validate.py activate`.
- It does not perform production activation.
- Evidence: command output `[PASS] activation-fixtures` and suite pass output.
- Status: PASS

## Production Safety Check
- Command: `git diff -- tasks/active-task.md`
- Result: no diff
- Status: PASS

## Safety Boundaries Preserved
- no automatic queue processing
- no agent runner execution
- no task execution
- no task completion
- no task failure marking
- no task dropping
- no approval marker generation
- no release approval
- no backend
- no web UI
- no RAG/vector DB
- no package installation
- no multi-agent orchestration

Status: PASS

## Known Limitations
- positive smoke is not full end-to-end task execution
- negative fixtures test rejection behavior, not business correctness
- activation does not prove implementation correctness
- manual recovery is documented later in 11.9.1
- activation audit does not replace completion review

## Result
Result: PASS
