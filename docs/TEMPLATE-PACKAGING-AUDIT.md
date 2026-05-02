# Template Packaging Audit

## Purpose
This audit checks M21 template packaging coverage.
It is read-only.
It does not make an MVP readiness decision.

## What the audit checks
- minimal template
- full template
- template integrity
- install smoke
- example project
- example project smoke
- quickstart
- usage docs
- forbidden readiness/autonomy claims

## Result labels
- PASS
- WARN
- FAIL
- NOT_RUN
- NOT_IMPLEMENTED
- ERROR

## Strict mode
Default mode allows WARN as final WARN.
Strict mode treats WARN, NOT_RUN, and NOT_IMPLEMENTED as blocking.
Strict mode still does not make MVP readiness decision.

## JSON output
Use:

```bash
python3 scripts/audit-template-packaging.py --json
```

## Boundaries
Template packaging audit PASS does not mean AgentOS is MVP-ready.
Template packaging audit WARN does not mean AgentOS is MVP-ready.
M21 template packaging audit does not override M19/M20 safety gates.
Audit results do not legalize unsafe operations after the fact.
Final M21 decision belongs to the Milestone 21 completion review.

## Non-goals
This audit does not create:
- templates
- install smoke
- example project
- example project smoke
- quickstart
- usage docs
- evidence report
- completion review
- release readiness decision
- autonomous execution

## Commands
```bash
python3 scripts/audit-template-packaging.py
python3 scripts/audit-template-packaging.py --strict
python3 scripts/audit-template-packaging.py --json
python3 scripts/audit-template-packaging.py --json --strict
```
