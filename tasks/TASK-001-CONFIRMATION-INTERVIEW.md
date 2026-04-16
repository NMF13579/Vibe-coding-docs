# TASK-001 — Доработка механики подтверждения интервью и связка статусов

---

## FSM-статус

| Поле | Значение |
|------|----------|
| **MODE** | `PLAN` |
| **STATE** | `pending` |

---

## Контекст

Репозиторий `Vibe-coding-docs` содержит `LAYER-1/interview-system.md` и `LAYER-2/discovery/project-interview.md`, определяющие поведение агента на этапе Discovery. Отсутствует явный stop-point перед фиксацией итогов и автоматического перехода статуса после подтверждения пользователем.

## Цель

Добавить в `LAYER-2/discovery/project-interview.md` явный stop-point и секцию `## Confirmation`, обновить `LAYER-3/project-status.md` и при необходимости `LAYER-1/audit-checklist.md` (HEALTH-SCORE), а также карту в `LAYER-1/tools/template-sync-index.md` / `README.md`, чтобы статус `accepted` выставлялся только после явного согласия пользователя.

## Шаги

1. Открыть `LAYER-2/discovery/project-interview.md`, найти конец блока интервью
2. Добавить stop-point перед фиксацией:
   ```
   > STOP: Покажи саммари пользователю и дождись явного подтверждения,
   > прежде чем фиксировать файл в LAYER-2/discovery/interview-summary.md.
   ```
3. Добавить в конец `LAYER-2/discovery/project-interview.md` секцию:
   ```markdown
   ## Confirmation
   Агент задаёт вопрос: «Согласен ли пользователь с этой суммаризацией?»
   Только при ответе "Да" → обновить `LAYER-3/project-status.md`:
   `LAYER-2/discovery/interview-summary.md` = accepted (и при необходимости поле Approved by)
   ```
4. В `LAYER-3/project-status.md` добавить колонку `Approved by` в таблицу статусов (или эквивалент в тексте)
5. В `LAYER-1/audit.md` обновить правило: `interview-summary.md` = accepted → Discovery 🟢
6. В `LAYER-1/tools/template-sync-index.md` (или `README.md`) дополнить блок Discovery пунктом о подтверждении интервью
7. Провести тестовый сценарий (см. «Критерии готовности»)

## Критерии готовности

- [ ] Стоп-поинт добавлен в `LAYER-2/discovery/project-interview.md`
- [ ] Секция `## Confirmation` добавлена с логикой вопроса/ответа
- [ ] `LAYER-3/project-status.md` содержит колонку `Approved by` (или эквивалент)
- [ ] `LAYER-1/audit-checklist.md` / HEALTH-SCORE отражает 🟢 при принятом `LAYER-2/discovery/interview-summary.md`
- [ ] Карта документов (`template-sync-index.md` / `README.md`) содержит упоминание о подтверждении интервью в Discovery
- [ ] Тестовый сценарий пройден полностью:
  1. Агент создает саммари → 2. Пользователь подтверждает → 3. `accepted` в `LAYER-3/project-status.md` → 4. 🟢 в HEALTH-SCORE (`audit-checklist`)

## Зависимости

- Требует: существование `LAYER-2/discovery/project-interview.md`, `LAYER-3/project-status.md`, `LAYER-1/audit.md`, `LAYER-1/tools/template-sync-index.md` или `README.md`
- Блокирует: корректная визуализация прогресса Discovery в HEALTH-SCORE
- Тип: `improvement` | Приоритет: `high`

## Self-check (заполняет агент перед закрытием)

- [ ] Цель достигнута: stop-point и Confirmation добавлены?
- [ ] Все артефакты из шагов обновлены?
- [ ] Побочных изменений вне scope задачи нет?
- [ ] HANDOFF.md обновлён, если были важные решения?

## Заметки агента

_Заполняется агентом в процессе работы._
