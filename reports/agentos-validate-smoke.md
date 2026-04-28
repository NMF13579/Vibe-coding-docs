# AgentOS Validate Smoke Report

## Command

Main smoke command:

```bash
python3 scripts/agentos-validate.py all
```

Individual commands:

```bash
python3 scripts/agentos-validate.py template
python3 scripts/agentos-validate.py negative
python3 scripts/agentos-validate.py guard
python3 scripts/agentos-validate.py audit
python3 scripts/agentos-validate.py queue
python3 scripts/agentos-validate.py runner
python3 scripts/agentos-validate.py all
```

## Date

2026-04-28

## Branch

dev

## Overall Result

FAIL

## Exit Codes

- template: 0
- negative: 0
- guard: 0
- audit: 0
- queue: 1
- runner: 1
- all: 1

## Suite-Level Summary

- template: PASS
- negative: PASS
- guard: PASS_WITH_WARNINGS
- audit: PASS_WITH_WARNINGS
- queue: FAIL
- runner: FAIL
- all: FAIL

## Warnings

- guard: PASS_WITH_WARNINGS
- audit: PASS_WITH_WARNINGS

## Failures

- queue: `tasks/queue/QUEUE.md: FAIL`
- runner: `scripts/agent-next.py` and `scripts/agent-complete.py` / `scripts/agent-fail.py` failed runner-protocol checks

## Missing Commands

None observed.

## Known Limitations

- This smoke report does not approve release.
- This smoke report does not approve execution.
- This smoke report does not validate state transitions.
- This smoke report does not create approval markers.
- This smoke report does not move queue entries.
- This smoke report does not replace tasks/active-task.md.
- JSON output is out of scope for Milestone 9.1.2.

## Safety Confirmation

agentos-validate.py was used only as a read-only validation wrapper.

No task files were intentionally modified.
No queue entries were moved.
No approval markers were created.
No state transitions were executed.
No release approval was granted.
No active-task.md replacement was performed.
