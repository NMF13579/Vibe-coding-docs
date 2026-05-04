# STATUS-SEMANTICS

## Purpose

Документ задаёт допустимые маркеры статусов и результатов проверок в AgentOS.
Он нужен, чтобы одинаковые сигналы (`PASS`, `FAIL`, `READY` и т.д.) трактовались одинаково в отчётах и проверках.

## Validation Result Markers

| Marker | Meaning | Human Decision Boundary |
|---|---|---|
| `PASS` | Check completed successfully | Does not prove total correctness |
| `FAIL` | Check completed and found a problem | Does not automatically decide final outcome |
| `WARN` | Check completed with non-blocking concern | Human may still review |
| `NOT_RUN` | Check was not executed | Must include reason where possible |
| `ERROR` | Check could not complete due to unexpected issue | Requires review |

## Workflow / Review Status Markers

| Marker | Meaning | Human Decision Boundary |
|---|---|---|
| `READY` | Item appears ready for next step | Does not imply approval |
| `NEEDS_REVIEW` | Human or follow-up review needed | Must not be treated as failure by itself |
| `APPROVED` | Explicit approval recorded | Must require human-controlled evidence |
| `BLOCKED` | Cannot proceed until blocker is resolved | Must identify blocker where possible |
| `COMPLETED` | Completion was recorded | Does not prove correctness without evidence |
| `FAILED` | Failure was recorded | Must preserve evidence and reason |

## Forbidden or Unsafe Status Claims

Небезопасные утверждения (должны считаться ошибкой):

- `validation guarantees correctness`
- `evidence means approval`
- `audit approves release`
- `PASS means completed`
- `READY means approved`
- `COMPLETED means correct`
- `index is source of truth`
- `script can make human decision`

## Unknown / Custom Markers

- custom markers не разрешены в MVP validator mode;
- missing checks нужно маркировать `NOT_RUN`, а не произвольным словом;
- если статус review неясен, использовать `NEEDS_REVIEW`.

## Allowed Marker Set

Validation markers:
- `PASS`, `FAIL`, `WARN`, `NOT_RUN`, `ERROR`

Workflow/review markers:
- `READY`, `NEEDS_REVIEW`, `APPROVED`, `BLOCKED`, `COMPLETED`, `FAILED`

## Boundaries

- Валидатор проверяет только корректность маркеров и запретных фраз.
- Валидатор не решает, что задача действительно завершена, одобрена или безопасна.
- Финальные решения остаются за человеком.
