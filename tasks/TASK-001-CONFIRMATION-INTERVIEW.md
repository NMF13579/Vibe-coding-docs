# TASK-001 — Доработка механики подтверждения интервью и связка статусов

---

## FSM-статус

| Поле | Значение |
|------|----------|
| **MODE** | `PLAN` |
| **STATE** | `pending` |

---

## Контекст

Репозиторий `Vibe-coding-docs` содержит файлы `INTERVIEWER.md` и `INTERVIEW-GUARDIAN.md`, определяющие поведение агента на этапе Discovery. Отсутствует явный stop-point перед фиксацией итогов и автоматического перехода статуса после подтверждения пользователем.

## Цель

Добавить в `docs/PROJECT-INTERVIEW.md` явный stop-point и секцию `## Confirmation`, обновить `PROJECT-STATUS.md`, `HEALTH-SCORE.md` и `DOCS-MAP.md`, чтобы статус `accepted` выставлялся только после явного согласия пользователя.

## Шаги

1. Открыть `docs/PROJECT-INTERVIEW.md`, найти конец блока интервью
2. Добавить stop-point перед фиксацией:
   ```
   > STOP: Покажи саммари пользователю и дождись явного подтверждения,
   > прежде чем фиксировать файл в docs/discovery/INTERVIEW-SUMMARY.md.
   ```
3. Добавить в конец `PROJECT-INTERVIEW.md` секцию:
   ```markdown
   ## Confirmation
   Агент задаёт вопрос: «Согласен ли пользователь с этой суммаризацией?»
   Только при ответе "Да" → обновить PROJECT-STATUS.md:
   `discovery/INTERVIEW-SUMMARY.md = accepted`
   ```
4. В `docs/PROJECT-STATUS.md` добавить колонку `Approved by` в таблицу статусов
5. В `docs/HEALTH-SCORE.md` обновить правило: `INTERVIEW-SUMMARY = accepted` → Discovery 🟢
6. В `docs/DOCS-MAP.md` дополнить блок Discovery пунктом о подтверждении интервью
7. Провести тестовый сценарий (см. «Критерии готовности»)

## Критерии готовности

- [ ] Стоп-поинт добавлен в `PROJECT-INTERVIEW.md`
- [ ] Секция `## Confirmation` добавлена с логикой вопроса/ответа
- [ ] `PROJECT-STATUS.md` содержит колонку `Approved by`
- [ ] `HEALTH-SCORE.md` показывает 🟢 при `INTERVIEW-SUMMARY = accepted`
- [ ] `DOCS-MAP.md` содержит упоминание о подтверждении интервью в Discovery
- [ ] Тестовый сценарий пройден полностью:
  1. Агент создает саммари → 2. Пользователь подтверждает → 3. `accepted` в PROJECT-STATUS → 4. 🟢 в HEALTH-SCORE

## Зависимости

- Требует: существование `docs/PROJECT-INTERVIEW.md`, `docs/PROJECT-STATUS.md`, `docs/HEALTH-SCORE.md`, `docs/DOCS-MAP.md`
- Блокирует: корректная визуализация прогресса Discovery в HEALTH-SCORE
- Тип: `improvement` | Приоритет: `high`

## Self-check (заполняет агент перед закрытием)

- [ ] Цель достигнута: stop-point и Confirmation добавлены?
- [ ] Все 4 файла из раздела «Артефакты» обновлены?
- [ ] Побочных изменений вне scope задачи нет?
- [ ] HANDOFF.md обновлён, если были важные решения?

## Заметки агента

_Заполняется агентом в процессе работы._
