# Architecture

AgentOS uses canonical modules as the runtime architecture.
Runtime means the documents an agent must read and follow while working.

## Runtime Spine

```text
llms.txt
  -> core-rules/MAIN.md
  -> state/MAIN.md
  -> workflow/MAIN.md
  -> quality/MAIN.md
  -> security/MAIN.md
```

`ROUTES-REGISTRY.md` records the same module ownership in table form.
It is a registry, not a second startup path.

## Module Responsibilities

| Module | Responsibility | Must not own |
|---|---|---|
| `core-rules/MAIN.md` | Priority, authority, governance, agent boundaries | State transitions, verification procedure, security detail |
| `state/MAIN.md` | Project/session/task lifecycle, events, recovery, transitions | Execution plan, release proof, policy priority |
| `workflow/MAIN.md` | Plan gate, scope control, execution sequence, one-task rule | Governance authority, state source, security policy |
| `quality/MAIN.md` | Verification, smoke checks, release blockers, audit output | Runtime authority, state transitions, access policy |
| `security/MAIN.md` | Sensitive data, least privilege, compliance, security stop conditions | General workflow, state lifecycle, audit ownership |

## Authority Model

- `llms.txt` is the only agent startup entry.
- The five canonical modules are the runtime source of behavior.
- Support documents may provide context only when a canonical module sends the agent there.
- Archive and adapter files are not runtime authority.
- If two sources appear to define the same rule, the canonical module for that responsibility wins.

## Conversion Standard

A document is canonical-ready when:

- it routes through one of the five canonical modules;
- it does not create a second startup path;
- it does not require old topology to understand runtime behavior;
- it separates responsibility instead of duplicating rules across modules;
- it states uncertainty or missing ownership instead of inventing a rule.
