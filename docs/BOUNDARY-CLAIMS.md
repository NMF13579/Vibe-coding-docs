# Boundary Claims MVP

## Boundary Zones
- validation
- evidence
- audit
- approval
- completion
- release readiness
- source-of-truth
- index/navigation
- script authority
- human decision

## Forbidden Claims
- validation guarantees correctness
- validation proves correctness
- PASS means completed
- PASS means correct
- evidence means approval
- evidence approves
- audit approves release
- audit makes final decision
- READY means approved
- COMPLETED means correct
- index is source of truth
- data/index.json is source of truth
- script can approve
- script can make human decision
- validator decides release readiness
- self-heal can change policy
- SQLite replaces Markdown
- RAG replaces Markdown

## Safe Alternatives
- validation provides evidence
- validation does not guarantee correctness
- evidence supports review
- evidence does not equal approval
- audit reports gaps
- audit does not approve release
- human makes final decision
- Markdown remains source of truth
- index is derived navigation only
- scripts check deterministic structure
- scripts do not make human decisions

## Validator Requirements
The validator must be read-only and use only the Python standard library. It must accept one Markdown file or a directory. It must normalize case, punctuation, and repeated whitespace enough to catch obvious variants. It must fail when forbidden claims are found and pass when only safe phrasing is present.

## Final Rule
Boundary claims protect the line between evidence and decision.

