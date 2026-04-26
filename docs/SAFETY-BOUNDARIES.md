# AgentOS Safety Boundaries

AgentOS enforces strict safety boundaries to ensure human oversight and control over critical operations.

## Execution Boundary

**AgentOS does not execute tasks automatically.**

- Task execution requires explicit human approval
- No autonomous task execution happens without human checkpoints
- All automated checks are read-only by default
- Validation tools report readiness; they do not execute

## Task Contract Boundary

**Only `tasks/active-task.md` is the executable task contract.**

- `TASK.md` task briefs are **not** executable (they are descriptive specifications)
- Draft contracts in `tasks/drafts/` are **not** active contracts (they are proposals awaiting approval)
- Contract promotion to `tasks/active-task.md` requires explicit human approval
- Replacing `tasks/active-task.md` requires human decision and verification

**Enforcement:**
- Automation tools will not replace `tasks/active-task.md` without explicit human instruction
- Tools report what would happen; humans decide if it should happen
- Draft generation is read-only; promotion is a separate human action

## Queue Boundary

**Queue entries are not moved autonomously.**

- Queue items remain in `tasks/queue/` until human explicitly moves them
- Validation and audit tools do not change queue state
- Queue lifecycle remains under human control
- Automated tools report queue status but do not modify queue

## Runner Boundary

**Runner protocol remains dry-run in this milestone.**

- Runner protocol is not executable yet (future milestone)
- Validation/audit runners are read-only report generators
- No runner executes external commands without human approval
- Dry-run output is provided for human review before actual execution

**Future:**
- Runner execution protocol will be explicitly extended in a future milestone
- When extended, it will still require human checkpoints

## Audit Boundary

**Audit runner reports readiness signals; it does not approve release.**

- Audit reports on validation status
- Audit runner cannot approve or block release
- Audit runner cannot replace active task
- Release approval remains a human decision
- Audit output informs human decision-makers

## Human Checkpoints

These operations require explicit human approval:

| Operation | Checkpoint |
|---|---|
| Replace `tasks/active-task.md` | Human review and explicit approval |
| Promote draft contract to active | Human review and explicit approval |
| Mark task as complete | Human verification and explicit marking |
| Move queue items | Human explicit queue management |
| Run autonomous executor (future) | Human explicit trigger and approval |

## Safety-Enforced Behaviors

**What AgentOS will NOT do:**

- ❌ Execute tasks without `tasks/active-task.md` (even with draft contract ready)
- ❌ Replace `tasks/active-task.md` without human decision
- ❌ Move queue items based on validation results
- ❌ Run runner protocol scripts without explicit user invocation
- ❌ Approve or mark completion without human action
- ❌ Bypass review/trace requirements
- ❌ Execute concurrent tasks (one-task rule)
- ❌ Modify task payloads without validation

## Non-Goals

**These features are intentionally not implemented in this milestone:**

- Autonomous agent execution
- Automatic task promotion
- Autonomous queue management
- Release checklist automation
- Automatic status updates
- Bypass of human approval checkpoints

These will be introduced only in future milestones with explicit architecture updates.

## Validation is Not Approval

**Important distinction:**

- **Validation** = checking if structure/content meets requirements (automated)
- **Approval** = human decision to proceed with execution (manual)

Validation tools (template-integrity, negative-fixtures, guard-failures, audit) provide information for human decision-makers. They do **not** constitute approval.

## Data and Access Boundaries

AgentOS assumes deployment in a restricted environment:

- No public API endpoints (all access local or VPN)
- No autonomous external calls
- No credential storage (credentials remain in environment/secure storage)
- No automatic data sharing
- All data operations subject to review/TRACE.md

See `security/MAIN.md` for detailed security policies.

## Enforcement Mechanisms

These boundaries are enforced through:

1. **Code structure** – certain operations are read-only by design
2. **Documentation** – clear rules about what should/should not happen
3. **Task contract** – explicit `tasks/active-task.md` defines scope
4. **Mandatory checkpoints** – human signatures required at key points
5. **Audit trail** – TRACE.md records all significant operations
6. **Architecture** – runner protocol requires explicit invocation

## Verification

To verify safety boundaries are maintained:

```bash
# Check project structure compliance
python3 scripts/check-template-integrity.py --strict

# Verify all validation tools work correctly
python3 scripts/audit-agentos.py

# Review current active task
cat tasks/active-task.md

# Check project initialization status
ls -la project/PROJECT.md
```

## Incident Response

If boundaries are violated:

1. **Stop execution** immediately
2. **Review TRACE.md** for what happened
3. **Check tasks/active-task.md** for authorization
4. **Report incident** to project owner
5. **Do not proceed** until boundaries are restored

## Questions About Boundaries?

If you're unsure whether an operation respects these boundaries:

1. Check `TRACE.md` – has this operation been explicitly approved?
2. Check `tasks/active-task.md` – is this within the active task scope?
3. Read `workflow/MAIN.md` – what does the execution plan allow?
4. Read `security/MAIN.md` – does this touch sensitive boundaries?
5. Ask the owner – when in doubt, don't proceed

## Related Documentation

- **Execution flow:** `workflow/MAIN.md`
- **Security policy:** `security/MAIN.md`
- **Getting started:** [GETTING-STARTED.md](GETTING-STARTED.md)
- **Validation reference:** [VALIDATION.md](VALIDATION.md)
- **Project initialization:** `state/MAIN.md`
