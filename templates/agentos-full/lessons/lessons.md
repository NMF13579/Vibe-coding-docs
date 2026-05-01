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
---
