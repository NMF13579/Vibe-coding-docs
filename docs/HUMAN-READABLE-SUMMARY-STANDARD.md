# Human-Readable Guardrail Summary MVP

## Executive Summary
Human-readable summaries are needed so people can understand validation results quickly without reading a long technical report first. They reduce review burden by putting the important result, reason, and next action in one short place. This standard defines a compact summary format for future reports and guardrails. It does not decide approval, correctness, or release readiness.

## Summary Purpose
The summary is a compact interface for humans. The full report remains the evidence archive. The summary must not hide failures, warnings, or missing checks. The summary must not replace human approval. The summary must not claim correctness or release readiness.

## Required Summary Fields
| Field | Meaning | Allowed Values / Format |
|---|---|---|
| `Result` | Overall summary result | `PASS` / `WARN` / `FAIL` / `ERROR` / `NOT_RUN` |
| `Reason` | One-line explanation | short text |
| `Changed files` | Count or status | number / `NOT_CHECKED` |
| `Violations` | Count or status | number / `NOT_CHECKED` |
| `Human action required` | Whether human review is needed | `YES` / `NO` |
| `Next step` | Recommended next action | `accept for review` / `review` / `fix` / `rerun` / `investigate` |
| `Evidence` | Where details can be found | command list, report path, or section reference |

## Result Semantics
| Result | Meaning | Human Boundary |
|---|---|---|
| `PASS` | No blocking issue found by the checks that ran | Does not prove correctness |
| `WARN` | Non-blocking issue or incomplete confidence | Human may still review |
| `FAIL` | Blocking issue found | Do not accept without fix or review |
| `ERROR` | Check could not complete correctly | Investigate before accepting |
| `NOT_RUN` | Check was not executed | Must include reason |

## Human Action Rules
`FAIL` requires human action. `ERROR` requires human action. `WARN` usually requires review. `NOT_RUN` must not be treated as `PASS`. `PASS` still does not equal approval, completion, correctness, or release readiness.

## Canonical Summary Example
| Field | Value |
|---|---|
| Result | `FAIL` |
| Reason | `Scope violation found: changed file outside allowed paths.` |
| Changed files | `3` |
| Violations | `1` |
| Human action required | `YES` |
| Next step | `review unexpected file before accepting` |
| Evidence | `Scope Compliance section and git status output` |

This example is not approval. This example is not proof of correctness. Full evidence must remain available below or in a linked report.

## Examples
| Case | Example |
|---|---|
| Passing check | `PASS`, reason: `All required checks passed.` |
| Warning check | `WARN`, reason: `One non-blocking issue found.` |
| Failing scope check | `FAIL`, reason: `Unexpected file outside allowed paths.` |
| Error during validation | `ERROR`, reason: `Validator could not read input.` |
| Not-run check | `NOT_RUN`, reason: `Check was not executed.` |

## Boundary Rules
The summary does not approve work. The summary does not complete a task. The summary does not prove correctness. The summary does not decide release readiness. The summary does not replace evidence. The summary does not replace human review.

## Future Integration Guidance
Future validators and reports may adopt this summary format. This task does not modify existing validators. Future integration should happen separately. Each validator should eventually print or report a compact summary. Evidence reports should place the human summary at the top.

## Recommended Next Task
`22.14.1 — Milestone 22 Evidence Report`

