# TEST-READINESS-FIXTURES

## Purpose

Run readiness fixture coverage for `scripts/check-execution-readiness.py`.
This suite validates readiness rejection behavior and status semantics (`FAIL`, `PARTIAL`, special `PASS_WITH_LIMITATIONS`, `SKIPPED`).

References:
- `docs/EXECUTION-READINESS.md`
- `tools/state/CHECK-EXECUTION-READINESS.md`
- `docs/ACTIVE-TASK-VALIDATION.md`
- `tools/state/VALIDATE-ACTIVE-TASK.md`

## Command Usage

```bash
python3 scripts/test-readiness-fixtures.py
```

## Fixture Directory

```text
tests/fixtures/negative/readiness/<case>/
  active-task.md
  source-task.md
  source-contract.md
  approvals/
  README.md
```

## README Strict Line-Based Format

Runner parses exact line-based fields from `README.md`:
- `- status: <FAIL|PARTIAL|PASS|SKIPPED>`
- `- exit code: <int>`
- `- note contains: <text>` (required for PASS coverage case)
- `- reason: <text>` (required for SKIPPED)

Rules:
- trim whitespace before comparison
- no markdown parser
- no inference from free text paragraphs

## Required README Fields

Non-SKIPPED case:
- `status`
- `exit code`

PASS coverage case:
- also requires `note contains`

SKIPPED case:
- `status: SKIPPED`
- `reason`

Malformed expected block makes fixture FAIL.

## Expected Status Detection

Runner compares checker output header exactly:
- `Execution Readiness: FAIL`
- `Execution Readiness: PARTIAL`
- `Execution Readiness: PASS`

It also compares exact exit code and checks `Traceback` absence.

## PASS / FAIL / PARTIAL / SKIPPED Semantics

- expected `FAIL`: checker must return exit `1` and status `FAIL`
- expected `PARTIAL`: checker must return exit `1` and status `PARTIAL`
- expected `PASS`: checker must return exit `0`, status `PASS`, and required note content
- expected `SKIPPED`: checker is not run; fixture counted separately

SKIPPED is not counted as PASS.

## PASS_WITH_LIMITATIONS Special Coverage Case

Case:
- `approval-direct-checks-pass-with-limitations`

Purpose:
- coverage for PASS_WITH_LIMITATIONS note behavior, not standard rejection case.

Runner tracks this in summary:
- `PASS_WITH_LIMITATIONS_CASES: <n>`

## approval-dir Fixture Handling

Runner always calls checker with fixture-local approval directory:

```bash
python3 scripts/check-execution-readiness.py \
  --active-task <case>/active-task.md \
  --approval-dir <case>/approvals
```

This avoids production `approvals/` usage.

## Safety Boundaries

Runner is read-only for production state.
It must not modify:
- `tasks/active-task.md`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `reports/`
- `approvals/`
- git state

No fixture copying into production `tasks/active-task.md`.

## Path / CWD Requirement

Runner executes checker with `cwd=<repo_root>` so repository-relative paths resolve deterministically.

## Known Limitations

- Some readiness cases are marked `SKIPPED` when they require unsafe validator-path overrides or unavailable controls in current MVP.
- Change-detection-related readiness cases are conditional and can remain SKIPPED when mechanism is unavailable.
