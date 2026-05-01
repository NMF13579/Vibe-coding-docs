# AgentOS Validate JSON Smoke Report

## Command

Main JSON smoke command:

```bash
python3 scripts/agentos-validate.py all --json
```

Individual JSON commands:

```bash
python3 scripts/agentos-validate.py template --json
python3 scripts/agentos-validate.py negative --json
python3 scripts/agentos-validate.py guard --json
python3 scripts/agentos-validate.py audit --json
python3 scripts/agentos-validate.py queue --json
python3 scripts/agentos-validate.py runner --json
python3 scripts/agentos-validate.py all --json
```

Text mode regression command:

```bash
python3 scripts/agentos-validate.py all
```

## Date

2026-04-28

## Branch

dev

## Overall Result

FAIL

## JSON Validity

PASS

`python3 -m json.tool /tmp/agentos-validate.json` exited `0`.

## Required Fields Check

PASS

Top-level fields present: `result`, `exit_code`, `suites`.
Suite fields present: `name`, `result`, `exit_code`, `command`.

Allowed result values observed: `PASS`, `PASS_WITH_WARNINGS`, `FAIL`.

## Exit Codes

- template --json: 0
- negative --json: 0
- guard --json: 0
- audit --json: 0
- queue --json: 1
- runner --json: 1
- all --json: 1
- all text mode: 1
- json.tool: 0
- required fields check: 0

## Suite-Level Summary

- template: PASS
- negative: PASS
- guard: PASS_WITH_WARNINGS
- audit: PASS_WITH_WARNINGS
- queue: FAIL
- runner: FAIL
- all: FAIL

## Text Mode Regression Check

Result: FAIL
Exit code: 1
Observed issues: queue and runner validations fail in the current repository state.

## Warnings

- guard: PASS_WITH_WARNINGS
- audit: PASS_WITH_WARNINGS

## Failures

- queue: FAIL
- runner: FAIL

## Missing Commands

None observed.

## Known Limitations

- This JSON smoke report does not approve release.
- This JSON smoke report does not approve execution.
- This JSON smoke report does not validate state transitions.
- This JSON smoke report does not create approval markers.
- This JSON smoke report does not move queue entries.
- This JSON smoke report does not replace tasks/active-task.md.
- This JSON smoke report does not add CI integration.
- This JSON smoke report does not define a JSON Schema file.
- JSON output captures structured suite status only; full stdout/stderr capture is out of scope.

## Safety Confirmation

agentos-validate.py --json was used only as a read-only validation wrapper.

No task files were intentionally modified.
No queue entries were moved.
No approval markers were created.
No state transitions were executed.
No release approval was granted.
No active-task.md replacement was performed.
No audit policy was changed.
WARN_THRESHOLD was not re-implemented.
Warning counts were not recalculated by the wrapper.
