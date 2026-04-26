# AgentOS

AgentOS is a governed documentation framework for AI-assisted development.
The current architecture is canonical-module driven: agents and owners navigate through a small set of runtime modules instead of scattered rule files.

## Start Here

| Need | Read |
|---|---|
| Agent startup | `llms.txt` |
| Route overview | `ROUTES-REGISTRY.md` |
| Rule priority and authority | `core-rules/MAIN.md` |
| Current state, recovery, transitions | `state/MAIN.md` |
| Planning and execution flow | `workflow/MAIN.md` |
| Verification and release readiness | `quality/MAIN.md` |
| Sensitive data and access boundaries | `security/MAIN.md` |

## Canonical Runtime Modules

| Module | Owns |
|---|---|
| `core-rules/MAIN.md` | Priority, authority, governance, agent boundaries |
| `state/MAIN.md` | State lifecycle, events, recovery, transitions |
| `workflow/MAIN.md` | Plan gate, scope control, execution boundaries, one-task rule |
| `quality/MAIN.md` | Verification, smoke checks, release blockers, audit output |
| `security/MAIN.md` | Sensitive data, least privilege, compliance, security stop conditions |

## Common Situations

| Situation | Route |
|---|---|
| I need to continue work | `state/MAIN.md` |
| I need a plan before changes | `workflow/MAIN.md` |
| The task is expanding | `workflow/MAIN.md` |
| I need to know which instruction wins | `core-rules/MAIN.md` |
| I need proof that the task is done | `quality/MAIN.md` |
| I am preparing for merge or release | `quality/MAIN.md` and `security/MAIN.md` |
| The task touches personal data, auth, access, API, or database | `security/MAIN.md` |
| The agent is unsure what to read | `ROUTES-REGISTRY.md`, then ask the owner if no route fits |

## Working Rule

- Use `llms.txt` as the only agent startup path.
- Use `ROUTES-REGISTRY.md` only to confirm module ownership.
- Keep runtime behavior inside the five canonical modules.
- Do not treat archive, adapter, support, or notes files as runtime authority.
- If the current module does not answer the situation, stop and ask the owner instead of guessing.

## Example scenarios

Practical documentation scenarios are available in:

- `examples/README.md`
- `examples/scenario-01-new-feature.md`
- `examples/scenario-02-bugfix.md`
- `examples/scenario-03-refactor.md`
- `examples/scenario-04-validation-only.md`

These examples are not executable fixtures. They illustrate expected AgentOS workflows and safety boundaries.
