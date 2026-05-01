# Activation Positive Smoke

## Purpose
Prove that a valid approved activation can create `tasks/active-task.md` in an isolated temp workspace.

## Scope
This smoke validates activation only.
It does not validate task execution.
It does not validate task completion.
It does not validate queue processing.

## Preconditions
- `scripts/activate-task.py` exists.
- Milestone 10 validators exist:
  - `scripts/detect-task-state.py`
  - `scripts/validate-task-state.py`
  - `scripts/check-transition.py`
- Approval marker validator exists:
  - `scripts/validate-approval-marker.py`
- Negative activation fixtures exist:
  - `tests/fixtures/negative/activation/`
  - `scripts/test-activation-fixtures.py`

## Temp Workspace Safety
Smoke was run in isolated temp workspace:
- `/tmp/agentos-positive-smoke-BXnNxt`

Safety boundaries used:
- Production `tasks/active-task.md` was not used as dependency.
- Activation command was run with `cwd` set to temp workspace root.
- Production repository root was not used as `cwd` for activation command.
- Smoke verified write happened only in temp workspace.

## Smoke Scenario
1. Created isolated temp workspace.
2. Copied only required scripts:
   - `activate-task.py`
   - `detect-task-state.py`
   - `validate-task-state.py`
   - `check-transition.py`
   - `validate-approval-marker.py`
3. Created valid task fixture:
   - `tasks/task-positive/TASK.md`
   - `tasks/task-positive/REVIEW.md`
   - `tasks/task-positive/TRACE.md`
   - `tasks/drafts/task-positive-contract-draft.md`
4. Created valid approval marker:
   - `approvals/approval-task-positive-execution.md`
5. Ran validator chain.
6. Ran approved activation command.
7. Verified generated `tasks/active-task.md` fields.
8. Verified production `tasks/active-task.md` was not modified.

## Commands Run
1. `python3 scripts/detect-task-state.py tasks/task-positive`  
Status: RUN  
Result: PASS (`state=approved_for_execution`, `analysis_status=ok`)

2. `python3 scripts/validate-task-state.py tasks/task-positive`  
Status: RUN  
Result: PASS (exit code `0`)

3. `python3 scripts/check-transition.py tasks/task-positive --to active`  
Status: RUN  
Result: PASS (exit code `0`)

4. `python3 scripts/validate-approval-marker.py approvals/approval-task-positive-execution.md --task task-positive --scope activate_task --transition approved_for_execution:active`  
Status: RUN  
Result: PASS (exit code `0`)

5. `python3 scripts/activate-task.py tasks/task-positive --approval approvals/approval-task-positive-execution.md --approved`  
Status: RUN (with `cwd=/tmp/agentos-positive-smoke-BXnNxt`)  
Result: PASS (exit code `0`)  
Output:
`ACTIVATION PASS`
`Updated: tasks/active-task.md`

6. `git diff -- tasks/active-task.md`  
Status: RUN (production repo)  
Result: no diff

7. `git diff -- reports/activation-positive-smoke.md`  
Status: RUN before report creation  
Result: no diff at that moment (report did not exist yet)

8. `python3 scripts/test-activation-fixtures.py`  
Status: RUN  
Result: `Activation negative fixtures: PASS`

## Expected Result
- Activation command exits `0`.
- Output contains `ACTIVATION PASS`.
- Output contains `Updated: tasks/active-task.md`.
- Temp workspace contains `tasks/active-task.md`.
- Production `tasks/active-task.md` is not modified.

## Observed Result
Exit code: `0`  
Output:
- `ACTIVATION PASS`
- `Updated: tasks/active-task.md`

Observed write location:
- `/tmp/agentos-positive-smoke-BXnNxt/tasks/active-task.md`

## Active Task Output Verification
Verified frontmatter values in temp workspace:
- `task_id: task-positive`
- `state: active`
- `activated_at: 2026-04-28T16:19:38.552779Z` (parseable ISO-8601 UTC)
- `activated_by: human-approved-command`
- `approval_id: approval-task-positive-execution`
- `source_task: tasks/task-positive`
- `source_contract: tasks/drafts/task-positive-contract-draft.md`
- `transition: approved_for_execution:active`

## Production Safety Check
- Production `tasks/active-task.md` was not modified (`git diff -- tasks/active-task.md` returned no diff).
- Expected production diff from this task is only this report file:
  - `reports/activation-positive-smoke.md`

## Limitations
- This is a smoke test, not full fixture coverage.
- Negative rejection coverage is handled by `scripts/test-activation-fixtures.py`.
- This smoke does not prove agent execution correctness.

## Result
Result: PASS
