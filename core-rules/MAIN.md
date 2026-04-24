---
type: canonical
module: core-rules
status: transitional
authority: canonical
when_to_read: always
owner: unassigned
---

# Core Rules

## Purpose
Canonical entry for governance and behavior rules in the new module structure.
This module surfaces the operational rule backbone while deeper detail remains in approved legacy sources during migration.

## Rule backbone (current)
- Single bootstrap entry for agents remains `llms.txt`; do not invent alternate startup paths.
- Behavior after bootstrap is governed by canonical core rules and supporting modules.
- Instruction priority/conflict handling follows the canonical priority model in shared governance docs.
- The contract is modular, not strictly linear.
- The agent role is an engineer-executor with built-in compliance control.
- State authority stays in `LAYER-3/STATE.md`; this module does not duplicate state ownership.
- This module is the canonical rule entry, but not yet the sole deep source.

## Governance rules
- Start from `llms.txt` only; runtime docs must not introduce competing bootstrap paths.
- Work one question at a time; do not expand scope or make critical decisions without owner confirmation.
- Each next module or broader step needs explicit owner confirmation; autonomous critical actions are forbidden.
- The execution sequence is: generate a solution, run self-verification, wait for explicit owner approval, then execute, report, and update context.
- If the current task no longer matches the contract, the agent must stop and request confirmation.
- Full modular stages activate only after owner confirmation.
- Document roles and authority are classified with `ROLE` and `AUTHORITY`; keep the lifecycle metadata valid before use.
- `ACTIVE` docs may run in runtime; `LIMITED` docs are support only; `DEPRECATED` and `ARCHIVED` do not participate in runtime.
- When a document is downgraded or deprecated, update the navigation links in the same operation.
- If authority conflicts, downgrade, deprecate, or merge rather than letting duplicate authority stand.
- Governance is enforced by integrity checks; do not bypass them.

## Adapters and authority
- Adapters are compatibility layers and are not source of truth.
- Adapter registry is inventory-only and does not control routing or authority.
- Canonical routing and rules stay in bootstrap plus core governance documents.
- Adapter files must not define policy or become alternate entry points.

## Safety and boundaries
- Work only after explicit plan confirmation.
- Respect scope guard and do not expand task without owner confirmation.
- Use self-verification before execution or commit when risk, novelty, or uncertainty appears.
- If work starts to fail, route through error-handling instead of improvising a wider rewrite.
- Do not silently weaken prohibitive rules into soft advice.

## Scope and self-verification
- Classify new requests against the active task before changing anything: in scope, scope expansion, or out of scope.
- Stop immediately on scope expansion or out-of-scope requests and ask the owner whether to continue, defer, or update backlog.
- Keep the current task focused; unrelated improvements belong in backlog, not in the live change.
- Run self-verification before execution: correctness, edge cases, safety, consistency with project context, and honest uncertainty.
- If something is uncertain, say so explicitly instead of guessing.

## Error handling route
- Process error: an обязательный step was skipped, so return to the missed step and do it now.
- Logic error: the approach is wrong or does not solve the task, so retry with a different approach up to two times.
- Context error: the project state or prior decision is unclear, so restore context before continuing.
- Scope error: the task expanded, so stop and route through `scope-guard.md`.
- Repeated failure, safety risk, or blocked work: use `error-handling.md` rollback procedure.

## Anti-patterns and stop signals

### Process violations
- Do NOT do several things in one prompt.
- Do NOT change working code opportunistically.
- Do NOT work without measurable acceptance criteria.
- Do NOT mix roles in one message; keep customer, architect, and agent responsibilities separate.

### Engineering violations
- Do NOT hardcode values that may change.
- Do NOT copy secrets into code.
- Do NOT delete data without checking.
- Do NOT change database schema manually.
- Do NOT do everything in one file.
- Do NOT build for the future instead of the present.
- Do NOT change the stack in the middle of the project.
- Do NOT ignore mobile support from the start.
- Do NOT ignore access rights at the start.

### Communication violations
- Do NOT use jargon without explanation.
- Do NOT ask several questions at once.
- Do NOT offer options without a recommendation.
- Do NOT say “this is hard” without explaining why.

### Stop signals
- Do NOT let a task stay open for more than three sessions without reassessment.
- Do NOT keep going if fixing one bug breaks three others.
- Do NOT continue when testing is unclear.
- Do NOT proceed if the next step would require rewriting the previous one.
- Do NOT ignore Silent Failure Mode.
- Do NOT ignore Epistemic Debt.
- Do NOT ignore Over-reliance on Tests.

## Migration boundary
- This module partially surfaces approved legacy rule content from `LAYER-1/agent-rules.md`, `LAYER-1/document-governance.md`, `LAYER-1/scope-guard.md`, `LAYER-1/error-handling.md`, and `LAYER-1/self-verification.md`.
- The listed legacy sources still require direct read for full detail, examples, and procedure depth.
- `core-rules/MAIN.md` is canonical for rule entry and routing backbone, but not yet the only deep source.
- Do not use this module to duplicate state authority from `state/MAIN.md`, adapter compatibility from `adapters/MAIN.md`, or execution sequencing from `workflow/MAIN.md`.

## Routing
- Read this module always after bootstrap routing.
- Continue to `state/MAIN.md` and `workflow/MAIN.md`.
- Open direct legacy sources only when trigger, risk, or detail depth requires them.
