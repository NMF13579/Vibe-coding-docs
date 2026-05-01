---
lessons:
  - id: "lesson-001"
    source_incident: "incident-template"
    tags:
      - "scope-creep"
    trigger: "Agent attempts to modify out_of_scope files."
    rule: "Before editing, compare target files against task.in_scope and task.out_of_scope."
    target_file: "workflow/MAIN.md"
    status: "proposed"
  - id: "lesson-002"
    source_incident: "approval-gate-not-implemented"
    tags:
      - "approval-gate"
      - "argparse"
      - "audit-marker"
    trigger: >
      В скрипте есть комментарии-маркеры аудита (# --approval <file>,
      # validate-human-approval) но сам аргумент не добавлен в argparse
      и логика не реализована. Тесты падают с missing_required_approval.
    rule: >
      Комментарии-маркеры аудита — это спецификация, а не заглушка.
      Перед завершением задачи проверять: каждый маркер из раздела
      «audit markers» должен иметь соответствующую реализацию в коде.
      Запускать тесты fixtures до закрытия задачи.
    target_file: "scripts/apply-transition.py"
    status: "active"
---
