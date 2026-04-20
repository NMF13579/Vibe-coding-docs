<!-- ROLE: CANONICAL_POLICY -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: runtime state, adapter logic, duplicate of agent-rules -->

# SYSTEM CONSTRAINTS

Этот файл описывает жёсткие ограничения системы.
Дополняет существующие governance-документы и не заменяет их.

---

## Hard constraints
- max bootstrap documents: 7
- max adapter file size: 150 lines
- max core governance file size: 300 lines
- no competing entrypoints
- adapters must remain dumb (no logic, no rules)
- registry is read-only (no routing)
- one canonical entry point: llms.txt

## Violation policy
Любое нарушение должно быть:
- исправлено, или
- явно принято через запись в LAYER-3/DECISIONS.md с обоснованием

## Enforcement
Эти ограничения могут проверяться автоматическими integrity checks
(например, scripts/health-check.sh), если такие проверки настроены.
