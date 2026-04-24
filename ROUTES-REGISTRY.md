# ROUTES-REGISTRY

Primary registry for canonical runtime routing.
All agent runtime routes must resolve to one of the canonical modules below.

| Module | Path | Role | When to read |
|---|---|---|---|
| core-rules | `core-rules/MAIN.md` | Priority, authority, governance, agent boundaries | always |
| state | `state/MAIN.md` | State lifecycle, events, recovery, transitions | always |
| workflow | `workflow/MAIN.md` | Plan gate, scope control, execution boundaries, one-task rule | always |
| quality | `quality/MAIN.md` | Verification, smoke checks, release blockers, audit output | always |
| security | `security/MAIN.md` | Sensitive data, least privilege, compliance, security stop conditions | always |

## Routing Rule

- Start from `llms.txt`.
- Use this registry only to confirm canonical module ownership.
- Do not route runtime work to archive, adapter, or support documents.
- If no module owns the situation, stop and ask the owner for direction.
