# AI Failure Modes

Canonical stop rules are in `../core-rules/MAIN.md`.
Canonical recovery rules are in `../state/MAIN.md` and `../workflow/MAIN.md`.

## Common Signals

- The agent is guessing.
- The task changed without approval.
- The agent skipped verification.
- The agent treats support text as authority.
- The next step would require rewriting the agreed plan.

## Response

Stop, name the issue plainly, return to the relevant canonical module, and ask the owner for direction if the safe next step is unclear.
