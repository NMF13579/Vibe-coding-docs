# Task Contract From Brief — Manual Guide Template

This file is a guide-template for manual conversion.
It is not an executable Task Contract by itself.

Use it together with:

- `tasks/{task-id}/TASK.md`
- `tasks/templates/task-contract.md`

## Mapping

| TASK.md поле | → | Contract поле |
|---|---|---|
| Context | → | task context / background |
| User Story | → | goal / user_value |
| Expected Result | → | expected_result |
| Acceptance Criteria | → | acceptance_criteria |
| Out of Scope | → | out_of_scope |
| Dependencies | → | dependencies / in_scope candidates |
| Risks | → | risk_level / risk_reason candidates |
| Rollback / Reversal Notes | → | rollback_plan |

## Manual Notes

- `risk_level` нельзя автоматически выводить без проверки
- `in_scope` нельзя заполнять произвольными файлами
- `verification_plan` должен быть добавлен вручную
- если данных недостаточно — использовать `TODO:` и не считать contract готовым

## Suggested Manual Bridge

1. Open the approved brief.
2. Open `tasks/templates/task-contract.md`.
3. Copy only confirmed information.
4. Mark unclear parts with `TODO:`.
5. Ask for approval before replacing `tasks/active-task.md`.

## Example Risk Fallback

```yaml
risk_level: MEDIUM
risk_reason: "Risk requires human review because the brief does not provide enough detail."
```

## Example Verification Fallback

```yaml
verification_plan:
  - "TODO: define verification command or manual verification step"
```
