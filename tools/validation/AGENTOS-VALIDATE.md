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
| `all` | `template`, `negative`, `guard`, `audit`, `queue`, `runner` |

The wrapper uses `sys.executable` to launch each script.
Primary usage is `python3 scripts/agentos-validate.py all`.
Focused commands remain available for debugging specific validators.

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

The wrapper only launches existing read-only validation commands.
