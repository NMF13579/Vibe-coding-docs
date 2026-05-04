# FRONTMATTER-STANDARD

## Executive Summary

AgentOS нужен стандарт frontmatter (метаданные в начале Markdown), чтобы скрипты читали документы одинаково и не путали роль файла.
Это снижает ошибки агента при проверках, когда похожие файлы имеют разное назначение.
Этот стандарт определяет минимальные поля, допустимые значения и правила безопасного использования `unknown`.
Этот документ не внедряет валидацию, не меняет существующие файлы и не запускает миграцию.

## Inputs Inspected

| Input / Path | Status | Notes |
|---|---|---|
| `reports/milestone-22-markdown-to-script-inventory.md` | FOUND | Использован как вход M22 для рисков и кандидатов проверок |
| `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | FOUND | Использован для role-to-frontmatter mapping |
| `docs/SOURCE-OF-TRUTH-MAP.md` | FOUND | Использован для authority boundaries |
| `docs/` | FOUND | Проверены ключевые policy/guardrail документы |
| `templates/` | FOUND | Подтверждены template-семейства |
| `reports/` | FOUND | Подтверждены evidence/audit семейства |
| `tasks/` | FOUND | Подтверждены task contract семейства |
| `examples/` | FOUND | Подтверждены example семейства |
| `scripts/` | FOUND | Подтверждены будущие validator кандидаты |
| `core-rules/` | FOUND | Канонический модуль доступен |
| `policies/` | FOUND | Policy layer доступен |
| `quality/` | FOUND | Канонический quality module доступен |
| `data/` | NOT_FOUND | Каталог отсутствует |
| Root-level (`llms.txt`, `README.md`) | FOUND | Использованы для общего контекста |

## Frontmatter Purpose

Frontmatter используется для:
- identification роли файла;
- identification модуля;
- lifecycle статуса;
- authority уровня;
- метаданных валидации;
- будущей сборки index;
- будущих consistency-check аудитов.

Обязательные границы:
- Markdown остаётся source of truth.
- Frontmatter описывает документ, а не заменяет его смысл.
- Frontmatter не должен хранить финальные человеческие решения как машинную authority.

## Minimum Frontmatter Block

```yaml
---
type: canonical|template|task|report|audit|verification|example|memory|handoff|derived|unknown
module: string
status: draft|active|canonical|archived|deprecated|unknown
authority: canonical|supporting|derived|context|unknown
created: YYYY-MM-DD|unknown
last_validated: YYYY-MM-DD|unknown
---
```

| Field | Required? | Meaning | Allowed Values | Notes |
|---|---|---|---|---|
| `type` | YES | Роль документа | `canonical`,`template`,`task`,`report`,`audit`,`verification`,`example`,`memory`,`handoff`,`derived`,`unknown` | Определяет класс файла |
| `module` | YES | Логическая область | non-empty string | Например `core-rules`, `workflow`, `reports` |
| `status` | YES | Жизненный статус документа | `draft`,`active`,`canonical`,`archived`,`deprecated`,`unknown` | Не равно результату проверки PASS/FAIL |
| `authority` | YES | Уровень нормативной силы | `canonical`,`supporting`,`derived`,`context`,`unknown` | Не выдаёт approval |
| `created` | YES | Дата создания записи | `YYYY-MM-DD` or `unknown` | Дату нельзя придумывать |
| `last_validated` | YES | Последняя проверка метаданных | `YYYY-MM-DD` or `unknown` | В MVP допускается `unknown` |

## Field Semantics

| Field | Semantic Meaning | Common Mistake | Future Validator Check |
|---|---|---|---|
| `type` | Роль документа в системе | Путать `task` и `template` | Проверка enum и role-family consistency |
| `module` | К какой зоне относится документ | Ставить слишком общее значение (`misc`) | Проверка non-empty и allowed module pattern |
| `status` | Текущее состояние документа | Использовать как PASS/FAIL результата команды | Проверка enum и запрет смешения с result statuses |
| `authority` | Нормативная сила текста | Ставить `canonical` без подтверждённого ownership | Проверка safe authority assignment |
| `created` | Дата создания метаданных | Придумывать дату | Проверка формата даты или `unknown` |
| `last_validated` | Когда поле/структура последний раз проверялись | Путать с датой изменения файла | Проверка формата даты или `unknown` |

## Type Values

| Type | Meaning | Typical Files | Risk if Misused |
|---|---|---|---|
| `canonical` | Основной нормативный документ | `*/MAIN.md`, ключевые rules docs | Агент примет неканоничный файл за правило |
| `template` | Шаблон структуры | `templates/*.md`, `tasks/templates/*.md` | Исполнение по шаблону вместо контракта |
| `task` | Контракт задачи | `tasks/active-task.md`, `tasks/*/TASK.md` | Ошибки scope и lifecycle |
| `report` | Сводный отчёт | `reports/milestone-*.md` | Отчёт будет трактован как правило |
| `audit` | Аудитный отчёт | `reports/*audit*.md` | Audit станет ложным approval |
| `verification` | Запись верификации | `reports/verification.md`, `REVIEW/TRACE` families | Потеря связи evidence и task |
| `example` | Пример/сценарий | `examples/**/*.md` | Пример будет трактован как обязательное правило |
| `memory` | Контекст/память сессии | `memory-bank/**/*.md` (если применяется) | Старый контекст станет authority |
| `handoff` | Передача контекста между сессиями | `handoff/*.md` | Handoff начнёт переопределять канон |
| `derived` | Производный артефакт | `templates/dist/**`, generated docs | Скрытый source-of-truth в derived файле |
| `unknown` | Роль пока не подтверждена | неясные/дублированные файлы | Избыточный `unknown` ломает автоматизацию |

## Status Values

| Status | Meaning | Allowed For | Risk if Misused |
|---|---|---|---|
| `draft` | Черновик | templates, draft docs, draft tasks | Черновик ошибочно принят как финальный |
| `active` | Используется в текущем процессе | task contracts, active operational docs | Неверный активный контекст |
| `canonical` | Канонический нормативный статус | canonical docs only | Необоснованная authority |
| `archived` | Исторический, не для текущего потока | old reports/docs | Использование устаревших правил |
| `deprecated` | Устаревающий, заменяемый | legacy docs/scripts docs | Смешение старого и нового поведения |
| `unknown` | Надёжно определить статус нельзя | unclear families | Сокрытие исправимой неопределённости |

## Authority Values

| Authority | Meaning | Allowed For | Automation Boundary |
|---|---|---|---|
| `canonical` | Основной источник правила | canonical modules/docs | Не назначать автоматически без подтверждения ownership |
| `supporting` | Поддерживающий документ | explanations, reports, guidance | Можно ссылаться, но не как final rule |
| `derived` | Производный артефакт | generated/dist outputs | Никогда не использовать как primary rule |
| `context` | Контекстный материал | handoff/memory/example notes | Использовать только как вспомогательный контекст |
| `unknown` | Уровень authority не определён | unclear files | Не автоматизировать до review |

## Unknown Handling

- `unknown` разрешён, когда надёжно определить метаданные нельзя.
- `unknown` нельзя использовать для скрытия устранимой неопределённости.
- Даты нельзя придумывать.
- Ownership нельзя придумывать.
- Будущие MVP-валидаторы могут разрешать `unknown`.
- Будущие strict-валидаторы могут предупреждать или падать при избытке `unknown`.

| Unknown Case | Allowed? | Rule | Future Validator Behavior |
|---|---|---|---|
| Роль файла неясна из-за дублей | YES | Ставить `type: unknown` до review | MVP: WARN, strict: WARN/FAIL threshold |
| Неизвестна дата создания | YES | `created: unknown` | MVP: PASS/WARN, strict: WARN |
| Неизвестен owner authority | YES | `authority: unknown` или `supporting` | MVP: WARN, strict: FAIL if safety-critical |
| Можно определить значение, но не заполнено | NO | Нельзя оставлять `unknown` без причины | MVP: WARN, strict: FAIL |

## Role-to-Frontmatter Mapping

| Markdown Role | Suggested Type | Suggested Authority | Notes |
|---|---|---|---|
| `semantic_source_of_truth` | `canonical` | `canonical` | Только при подтверждённой ownership ясности |
| `template` | `template` | `supporting` | Шаблон не должен быть rule-owner |
| `task_contract` | `task` | `supporting` | Approval остаётся человеческим решением |
| `verification_record` | `verification` | `supporting` | Evidence не равно decision |
| `evidence_report` | `report` | `supporting` | Отчёт суммирует, не утверждает authority |
| `audit_report` | `audit` | `supporting` | Audit сообщает статус, не принимает решение |
| `example` | `example` | `context` | Примеры не являются нормативными |
| `generated_or_derived` | `derived` | `derived` | Должен ссылаться на источник |
| `unclear` | `unknown` | `unknown` | Нужен последующий review |

## Source-of-Truth Implications

- `authority: canonical` нельзя назначать автоматически и без оснований.
- Финальный source-of-truth ownership должен следовать `docs/SOURCE-OF-TRUTH-MAP.md`.
- При неоднозначном ownership использовать `unknown` или `supporting`.
- Frontmatter сам по себе не должен разрешать ownership-конфликты.

| Ownership Case | Recommended Authority | Rule |
|---|---|---|
| Ясный канонический owner | `canonical` | Только если в map ownership зона ясна |
| Есть основной и вспомогательный документ | `supporting` для вторичного | Secondary doc не должен объявляться canonical |
| Ownership спорный | `unknown` | До review не автоматизировать эту зону |

## Derived Artifact Rules

- Derived artifacts должны явно обозначать свою роль.
- Derived artifacts не должны становиться скрытым source of truth.
- Generated reports могут суммировать evidence, но не approve outcome.
- Human decisions не должны существовать только в derived артефактах.

| Derived Artifact | Suggested Type | Suggested Authority | Rule |
|---|---|---|---|
| `templates/dist/**` Markdown | `derived` | `derived` | Всегда проверять соответствие исходным templates |
| generated audit summaries | `derived` or `audit` | `supporting` | Не трактовать как release/completion decision |
| generated evidence exports | `derived` | `derived` | Должны ссылаться на source Markdown |

## Future Index Implications

- index должен собираться из frontmatter + путей Markdown.
- index должен быть rebuildable.
- index только для навигации.
- index не должен хранить approval/completion/release decisions как authority.

| Frontmatter Field | Index Use | Risk |
|---|---|---|
| `type` | Группировка по ролям | Неверная роль даст ложную навигацию |
| `module` | Фильтрация по области | Смешение модулей |
| `status` | Фильтр по состоянию документа | Путаница со статусами проверок |
| `authority` | Поиск канонических зон | Ошибочный canonical override |
| `created` | Историческая сортировка | Неверные/выдуманные даты |
| `last_validated` | Контроль устаревших метаданных | Ложное ощущение актуальности |

## Future Validator Candidates

| Future Validator | What It Checks | Source Needed Before Implementation |
|---|---|---|
| `validate-frontmatter.py` | Required fields + allowed values | Этот стандарт + role classification |
| `build-index.py` | Build derived index from frontmatter/paths | Стандарт полей + index rules |
| `validate-index.py` | Index consistency/rebuildability | Build rules + source-of-truth boundaries |
| `audit-metadata-consistency.py` | Cross-file metadata consistency | Stable role mapping + ownership clarity |

## Future Validator Modes

| Mode | Behavior | Use Case |
|---|---|---|
| `MVP` | Validate required fields and allowed values; allow unknown where needed | Initial adoption and migration |
| `strict` | Warn or fail on excessive unknown, stale metadata, or unsafe authority usage | Later hardening after migration |

## Do Not Encode in Frontmatter

- ambiguous policy interpretation
- ambiguous risk classification
- approval decisions
- completion review decisions
- release readiness decisions
- active-task mutation authority
- self-healing authority
- SQLite authority
- vector RAG authority
- backend/service authority
- autonomous execution authority

## Recommended Next Task

`22.5.1 — Frontmatter Validator MVP`

Валидатор должен идти после стандарта, чтобы проверять уже согласованные поля и значения.
Если сначала написать валидатор, он зафиксирует спорные предположения и усилит ошибки.
Семантика полей в текущем MVP достаточно стабильна для старта валидатора, но strict-правила лучше включать после накопления практики.

## Validation Evidence

| Command / Check | Status | Output Summary | Notes |
|---|---|---|---|
| verify `docs/FRONTMATTER-STANDARD.md` exists | PASS | файл создан | Проверено после записи |
| inspect `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | PASS | найден и использован | Вход M22.2.1 доступен |
| inspect `docs/SOURCE-OF-TRUTH-MAP.md` | PASS | найден и использован | Вход M22.3.1 доступен |
| inspect `reports/milestone-22-markdown-to-script-inventory.md` | PASS | найден и использован | Вход M22.1.1 доступен |
| inspect `data/` | NOT_FOUND | каталог отсутствует | Не создавался |
| `git status --short` (read-only) | WARN | в репозитории есть pre-existing untracked файлы | В этой задаче добавлен только `docs/FRONTMATTER-STANDARD.md` |
| inspect validator commands with write-risk | NOT_RUN | не запускались | В задаче требовался только стандарт, без внедрения проверок |

## Final Frontmatter Standard Result

`READY_WITH_WARNINGS`

Минимальные поля, допустимые значения, role mapping и правила `unknown` определены в полном MVP-формате.
Границы authority и запреты на кодирование человеческих решений в frontmatter также зафиксированы.
Предупреждение связано с тем, что часть реальных файлов ещё не мигрирована и может содержать будущие `unknown`-случаи.

Recommended next task: `22.5.1 — Frontmatter Validator MVP`.
