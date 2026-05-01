# AgentOS Input Layer

AgentOS помогает безопасно оформлять и выполнять задачи для AI coding.

Сначала нужно пройти Discovery:

- `/init` = понять проект
- `/spec` = оформить задачу
- `workflow/MAIN.md` = выполнить задачу

Порядок работы:

1. Запусти `/init`, чтобы описать проект и зафиксировать Discovery.
2. Потом запусти `/spec`, чтобы оформить задачу как Task Brief.
3. После этого отдельно оформи executable Task Contract, если задачу нужно выполнять.

Важно:

- Spec Wizard создаёт только Task Brief.
- Spec Wizard не создаёт executable Task Contract автоматически.
- Для выполнения задачи нужно отдельно использовать `tasks/active-task.md`.
