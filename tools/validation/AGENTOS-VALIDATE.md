# AgentOS Unified Validation Wrapper

## Purpose

`scripts/agentos-validate.py` is a unified wrapper around existing validation commands.
It is orchestration only.
It does not introduce a new validator, a state machine, an approval system, or packaging logic.
It is the official validation entrypoint for AgentOS.

## Commands

```bash
python3 scripts/agentos-validate.py template
python3 scripts/agentos-validate.py negative
python3 scripts/agentos-validate.py guard
python3 scripts/agentos-validate.py audit
python3 scripts/agentos-validate.py queue
python3 scripts/agentos-validate.py runner
python3 scripts/agentos-validate.py state-fixtures
python3 scripts/agentos-validate.py approval-fixtures
python3 scripts/agentos-validate.py activation-fixtures
python3 scripts/agentos-validate.py active-task
python3 scripts/agentos-validate.py active-task-fixtures
python3 scripts/agentos-validate.py execution-readiness
python3 scripts/agentos-validate.py readiness-fixtures
python3 scripts/agentos-validate.py all
```

## Mapping

| Wrapper command | Existing script |
|---|---|
| `template` | `scripts/check-template-integrity.py --strict` |
| `negative` | `scripts/test-negative-fixtures.py` |
| `guard` | `scripts/test-guard-failures.py` |
| `audit` | `scripts/audit-agentos.py` |
| `queue` | `scripts/validate-queue.py` |
| `runner` | `scripts/validate-runner-protocol.py` |
| `state-fixtures` | `scripts/test-state-fixtures.py` |
| `approval-fixtures` | `scripts/test-approval-marker-fixtures.py` |
| `activation-fixtures` | `scripts/test-activation-fixtures.py` |
| `active-task` | `scripts/validate-active-task.py` |
| `active-task-fixtures` | `scripts/test-active-task-fixtures.py` |
| `execution-readiness` | `scripts/check-execution-readiness.py` |
| `readiness-fixtures` | `scripts/test-readiness-fixtures.py` |
| `all` | `template`, `negative`, `guard`, `audit`, `queue`, `runner`, `active-task-fixtures`, `readiness-fixtures` |

The wrapper uses `sys.executable` to launch each script.
Primary usage is `python3 scripts/agentos-validate.py all`.
Focused commands remain available for debugging specific validators.
Command success is based primarily on child process exit code.
Child stdout/stderr is printed for human inspection.

## state-fixtures

`state-fixtures` runs the v1.1-compatible negative state-machine fixture suite.

```bash
python3 scripts/agentos-validate.py state-fixtures
```

What it runs:

- `scripts/test-state-fixtures.py`

Exit code passthrough:

- child exit `0` -> wrapper exit `0`
- child exit `1` -> wrapper exit `1`
- child exit `2` -> wrapper exit `2`

Exit codes:

- `0` - all expected fixture rejections happened
- `1` - at least one invalid marker was accepted, or fixture failed unexpectedly, or runner not found
- `2` - usage error passed through from child runner: fixture dir missing, `fixture.json` unreadable, or `scripts/validate-approval-marker.py` not found

JSON mode status:

- not added in this MVP

Included in `all`:

- no

Safety boundaries:

- `state-fixtures` does not execute transitions
- `state-fixtures` does not modify task files
- `state-fixtures` does not create approval markers
- `state-fixtures` does not replace `tasks/active-task.md`
- `state-fixtures` does not move queue entries
- `state-fixtures` does not create `tasks/failed/`
- `state-fixtures` does not create task-level state operation commands
- `state-fixtures` keeps the suite-wrapper boundary intact
- `state-fixtures` consumes `scripts/test-state-fixtures.py` only

Suite-wrapper boundary:

- `state-fixtures` is only another suite in the wrapper
- it is not a task manager CLI
- task-level state/transition commands are intentionally not added in Milestone 10.8.1
- no task-level state commands were added for the v1.1 compatibility update

## approval-fixtures

`approval-fixtures` runs the approval marker negative fixture suite.

```bash
python3 scripts/agentos-validate.py approval-fixtures
```

What it runs:

- `scripts/test-approval-marker-fixtures.py`

Exit code passthrough:

- child exit `0` -> wrapper exit `0`
- child exit `1` -> wrapper exit `1`
- child exit `2` -> wrapper exit `2`

JSON mode status:

- not added in this MVP

Included in `all`:

- no

Safety boundaries:

- `approval-fixtures` does not execute transitions
- `approval-fixtures` does not create approval markers
- `approval-fixtures` does not grant approval
- `approval-fixtures` does not replace `tasks/active-task.md`
- `approval-fixtures` does not move queue entries
- `approval-fixtures` does not create or modify production `approvals/`
- `approval-fixtures` does not modify production task files
- `approval-fixtures` does not enable approved mode
- `approval-fixtures` does not add task-level approval commands
- `approval-fixtures` keeps the suite-wrapper boundary intact
- `approval-fixtures` consumes `scripts/test-approval-marker-fixtures.py` only

Suite-wrapper boundary:

- `approval-fixtures` is only another suite in the wrapper
- it is not a task manager CLI
- task-level approval validation remains in `scripts/validate-approval-marker.py`
- no task-level approval commands were added in Milestone 10.17.1

## activation-fixtures

`activation-fixtures` runs the activation negative fixture suite.

```bash
python3 scripts/agentos-validate.py activation-fixtures
```

Equivalent:

```bash
python3 scripts/test-activation-fixtures.py
```

Exit code passthrough:

- child exit `0` -> wrapper exit `0`
- child exit non-zero -> wrapper exit non-zero
- missing `scripts/test-activation-fixtures.py` -> wrapper exits non-zero and reports `MISSING`

Included in `all`:

- no

Safety boundaries:

- `activation-fixtures` validates rejection behavior only
- `activation-fixtures` does not activate a production task
- `activation-fixtures` does not write production `tasks/active-task.md`
- `activation-fixtures` does not execute tasks
- `activation-fixtures` does not process the queue

## active-task

`active-task` runs live Active Task Integrity validation.

```bash
python3 scripts/agentos-validate.py active-task
```

What it runs:

- `scripts/validate-active-task.py`

Exit behavior:

- child exit `0` -> wrapper exit `0`
- child exit non-zero (`FAIL` or `PARTIAL`) -> wrapper exit non-zero

State model note:

- live repository may not have a valid active task at every moment
- non-zero result can be expected validation failure, not implementation failure

Safety boundaries:

- validation only
- no task activation
- no task execution

## active-task-fixtures

`active-task-fixtures` runs Active Task negative fixture suite.

```bash
python3 scripts/agentos-validate.py active-task-fixtures
```

What it runs:

- `scripts/test-active-task-fixtures.py`

Exit behavior:

- child exit `0` -> wrapper exit `0`
- child exit non-zero -> wrapper exit non-zero

Safety boundaries:

- fixture-only validation
- no production task activation
- no production task execution

## execution-readiness

`execution-readiness` runs live readiness check.

```bash
python3 scripts/agentos-validate.py execution-readiness
```

What it runs:

- `scripts/check-execution-readiness.py`

Exit behavior:

- child exit `0` (`PASS`) -> wrapper exit `0`
- child exit non-zero (`FAIL` or `PARTIAL`) -> wrapper exit non-zero

State model note:

- live repository may be not execution-ready by design
- non-zero can be expected validation failure

Safety boundaries:

- validation only
- no task activation
- no task execution

## readiness-fixtures

`readiness-fixtures` runs readiness fixture suite.

```bash
python3 scripts/agentos-validate.py readiness-fixtures
```

What it runs:

- `scripts/test-readiness-fixtures.py`

Exit behavior:

- child exit `0` -> wrapper exit `0`
- child exit non-zero -> wrapper exit non-zero
- SKIPPED cases do not fail command when child runner exits `0`

Safety boundaries:

- fixture-only validation
- no production task activation
- no production task execution

## Result Semantics

For each suite, the wrapper prints one status line:

```text
[PASS] template
[FAIL] negative
[PASS_WITH_WARNINGS] guard
[MISSING] queue
```

Status rules:

- `exit code 0` -> `PASS`
- `exit code non-zero` -> `FAIL`
- `PASS_WITH_WARNINGS` is used only when the subprocess output explicitly contains `PASS_WITH_WARNINGS`
- `MISSING` is used when the mapped script does not exist

The wrapper does not infer warnings from counts, thresholds, or custom policy.

## `all` Aggregate Behavior

`all` runs suites in this order:

1. `template`
2. `negative`
3. `guard`
4. `audit`
5. `queue`
6. `runner`
7. `active-task-fixtures`
8. `readiness-fixtures`

Included in `all`:

- `active-task-fixtures`: yes
- `readiness-fixtures`: yes
- `active-task`: no
- `execution-readiness`: no

Rationale:

- fixture suites are deterministic and safe as default aggregate checks
- live checks depend on current repository task state and may fail as expected validation outcomes
- keep live checks explicit commands unless repository policy requires active task at all times

Aggregate rules:

- `FAIL` if at least one suite exits non-zero
- `PASS_WITH_WARNINGS` if no suite fails and at least one suite explicitly outputs `PASS_WITH_WARNINGS`
- `PASS` if all suites exit `0` and none outputs `PASS_WITH_WARNINGS`
- `MISSING` counts as a failure case for aggregation

Exit codes:

- overall `FAIL` -> `1`
- overall `PASS` -> `0`
- overall `PASS_WITH_WARNINGS` -> `0`

## Missing Command Behavior

If a mapped script is missing:

- the wrapper does not invent a result
- the wrapper does not emit a fake `PASS`
- the wrapper prints the suite as `MISSING`
- the wrapper returns non-zero

Example:

```text
[MISSING] queue
```

## Safety Boundaries

`agentos-validate.py` does not:

- approve execution
- move tasks
- replace `tasks/active-task.md`
- create approval markers
- implement state transitions
- recalculate warning counts
- re-implement `WARN_THRESHOLD`
- define audit policy
- execute task flows
- activate tasks
- run agents

The wrapper only launches existing read-only validation commands.
