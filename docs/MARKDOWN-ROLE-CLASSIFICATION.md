# MARKDOWN-ROLE-CLASSIFICATION

## Executive Summary

Классификация ролей Markdown нужна, чтобы агент не путал документы с разным назначением: правила, шаблоны, контракты задач, отчёты и примеры.
Такая классификация снижает ошибки, когда один и тот же статус или правило встречается в нескольких типах файлов.
Этот документ задаёт ролевую модель и распределяет семейства Markdown-файлов по ролям.
Этот документ не удаляет Markdown, не внедряет валидаторы и не назначает финальных владельцев source-of-truth.

## Role Model

| Role | Meaning | Typical Location | Automation Boundary |
|---|---|---|---|
| `semantic_source_of_truth` | Defines meaning, policy, rationale, or durable rules | `llms.txt`, `core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, `security/MAIN.md`, ключевые `docs/*.md` | Scripts may check structure, not replace meaning |
| `template` | Provides reusable document/task/report structure | `templates/*.md`, `tasks/templates/*.md`, `reports/templates/*.md` | Scripts may check required fields/sections |
| `task_contract` | Defines executable task scope and expected behavior | `tasks/active-task.md`, `tasks/*/TASK.md`, `tasks/drafts/*.md` | Scripts may validate structure; human controls approval |
| `verification_record` | Records evidence from checks and validation | `tasks/*/REVIEW.md`, `tasks/*/TRACE.md`, `reports/verification.md` | Scripts may validate evidence format |
| `evidence_report` | Summarizes validation results and gaps | `reports/milestone-*.md`, `reports/*-evidence-report.md` | Scripts may check sections; human interprets |
| `audit_report` | Reports consistency, coverage, and risks | `reports/*audit*.md`, `reports/*smoke*.md` | Scripts may generate/check, but not approve |
| `example` | Demonstrates usage or expected behavior | `examples/**/*.md` | Scripts may smoke-test examples |
| `generated_or_derived` | Produced from another source | `templates/dist/**`, build/export artifacts in `reports/` | Must be rebuildable or clearly marked |
| `unclear` | Role cannot yet be determined | массовые дубли `* 2.md` в разных папках | Must not be automated until classified |

## Markdown File Family Classification

| File / Family | Assigned Role | Reason | Scriptable Checks | Human-Controlled Parts | Confidence |
|---|---|---|---|---|---|
| `llms.txt` | semantic_source_of_truth | Канонический bootstrap и порядок чтения | Наличие обязательных ссылок/порядка | Интерпретация правил и приоритетов | HIGH |
| `core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, `security/MAIN.md` | semantic_source_of_truth | Канонические области правил | Проверка frontmatter/обязательных секций | Смысловое управление правилами | HIGH |
| `docs/*.md` (policy/process docs) | semantic_source_of_truth | Описывают границы, смысл, rationale | Проверка разделов, boundary-маркеров | Финальная трактовка правил | MEDIUM |
| `templates/*.md` | template | Каркасы документов | Required sections/fields | Что считается корректным содержанием | HIGH |
| `tasks/templates/*.md` | template | Шаблоны task contract и связанного потока | Проверка обязательных блоков | Решение о применении шаблона | HIGH |
| `reports/templates/*.md` | template | Шаблоны verification/evidence отчётов | Проверка формата таблиц | Интерпретация итогов отчёта | HIGH |
| `tasks/active-task.md` | task_contract | Активный исполняемый контракт | Валидация структуры и полей | Одобрение и активация человеком | HIGH |
| `tasks/*/TASK.md` | task_contract | Контекст и scope задачи | Проверка обязательных метаданных | Подтверждение бизнес-смысла | MEDIUM |
| `tasks/*/REVIEW.md`, `tasks/*/TRACE.md` | verification_record | Фиксируют review/trace и решение по готовности | Проверка статусов/полей | Решение человека по готовности | HIGH |
| `reports/milestone-*.md` | evidence_report | Сводка проверок, рисков и рекомендаций | Проверка структуры/статусов | Финальная оценка значимости рисков | MEDIUM |
| `reports/*audit*.md` | audit_report | Аудит покрытий и границ | Проверка vocabulary и выходных маркеров | Решение на основе аудита остаётся человеческим | MEDIUM |
| `examples/**/*.md` | example | Демонстрация сценариев | Smoke-check примеров | Оценка достаточности примера | HIGH |
| `templates/dist/**` | generated_or_derived | Производные пакеты шаблонов | Сверка с исходными шаблонами | Решение о публикации/использовании | MEDIUM |
| `* 2.md` families | unclear | Дубли без явного статуса каноничности | Детектор дублей, compare checks | Решение: хранить/удалять/объединять | UNCLEAR |
| `data/` Markdown families | NOT_FOUND | Каталог отсутствует | NOT_RUN | N/A | NOT_FOUND |

## Semantic Markdown to Preserve

| Markdown Area | Why It Must Stay Semantic | Allowed Script Support | Forbidden Automation |
|---|---|---|---|
| architecture | Объясняет смысл архитектурных решений | Проверка наличия обязательных разделов | Автоматическое переписывание архитектурного смысла |
| guardrails | Фиксирует принципы безопасной работы | Проверка boundary-фраз | Автоматическое снятие human checkpoint |
| limitations | Ограничения должны читаться человеком | Проверка структуры | Авто-интерпретация как разрешение на риск |
| usage docs | Обучающий контент для людей | Проверка ссылок/секций | Авто-изменение инструкций без review |
| risk model | Обоснование и словарь рисков | Проверка наличия классов риска | Автоматическое принятие риск-решений |
| approval policy | Границы, когда нужен approval | Проверка policy mapping | Автоматическое approval-решение |
| completion decision logic | Условия готовности к завершению | Проверка статусов/поля stop_reason | Авто-завершение задач |
| release decision logic | Финальная готовность к релизу | Проверка vocabulary отчётов | Авто-релиз по PASS-маркерам |
| lessons | Человеческая ретроспектива | Проверка минимальных полей записи | Авто-генерация выводов без review |
| human decisions | Решения по одобрению и приоритету | Проверка наличия доказательств | Подмена решения человека скриптом |
| evidence reports | Контекст и выводы по проверкам | Проверка формата таблиц/статусов | Трактовка evidence как approval |

## Scriptable Markdown Parts

| Markdown Part | Future Check Type | Why Deterministic | Candidate Future Script |
|---|---|---|---|
| Required sections | section presence check | Фиксированный список секций | `validate-required-sections.py` |
| Allowed statuses | enum/status check | Допустимые значения конечны | `validate-status-semantics.py` |
| Forbidden claims | forbidden phrase check | Список фраз можно закрепить | `validate-forbidden-claims.py` |
| Boundary statements | boundary marker check | Маркеры безопасности формализуемы | `validate-boundary-claims.py` |
| Evidence format | table/field format check | Табличная структура проверяема | `validate-evidence-format.py` |
| Command result markers | marker vocabulary check | PASS/WARN/FAIL маркеры фиксированы | `validate-command-markers.py` |
| Template required files | required-path check | Список файлов конечен | `check-template-integrity.py` (extended) |
| Task required fields | frontmatter field check | Поля и типы фиксируются | `validate-task-fields.py` |
| Report required sections | report section check | Секции отчёта предсказуемы | `validate-report-sections.py` |
| Frontmatter presence | frontmatter existence check | Проверка наличия детерминирована | `validate-frontmatter.py` |

## Generated or Derived Markdown Rules

- Generated or derived Markdown must not become hidden source of truth.
- Generated reports may summarize evidence but must not approve outcomes.
- Generated docs should identify their source when possible.
- Derived artifacts must be reproducible or explicitly marked as non-reproducible.
- Human decisions must not be stored only in generated artifacts.

| Derived Artifact Type | Source | Rebuildable? | Risk | Rule |
|---|---|---|---|---|
| `templates/dist/**` docs | `templates/agentos-*` | YES (expected) | MEDIUM | Всегда проверять синхронность с исходниками |
| audit output reports | validator/audit scripts + repo state | PARTIAL | MEDIUM | Не считать audit output источником решения |
| milestone evidence summaries | runtime checks + manual interpretation | PARTIAL | MEDIUM | Сохранять разделение evidence и decision |
| duplicated `* 2.md` files | неизвестно | NO | HIGH | Не считать каноникой, пока не классифицировано |

## Role Boundaries

| Boundary | Difference | Risk if Confused |
|---|---|---|
| `semantic_source_of_truth` vs `evidence_report` | Первый задаёт правило, второй фиксирует наблюдение | Временный отчёт ошибочно станет правилом |
| `evidence_report` vs decision | Отчёт даёт факты, решение принимает человек | Автоматическое действие по отчёту без review |
| evidence vs approval | Evidence = доказательства; approval = разрешение человека | Нелегитимное исполнение без одобрения |
| `template` vs `task_contract` | Template — заготовка, task_contract — активные обязательства | Исполнение по черновику вместо активного контракта |
| `audit_report` vs completion review | Audit оценивает, completion review принимает итог | Преждевременное закрытие задачи |
| index/navigation vs source of truth | Index помогает найти, но не определяет правило | Скрытый сдвиг authority в индекс |

## Unclear Classification Handling

- Если роль неясна, помечать как `unclear`.
- Не автоматизировать такую зону до отдельной классификации.
- Не считать `unclear`-файлы source-of-truth.
- Не удалять и не переписывать их в этой задаче.
- Выносить на отдельный review в следующем этапе.

## Frontmatter Implications

Этот документ подготавливает будущий frontmatter-стандарт, но не создаёт его.

| Role | Likely Future Frontmatter Fields | Reason |
|---|---|---|
| `semantic_source_of_truth` | `type`, `module`, `status`, `authority`, `source_of_truth` | Явная фиксация каноничности |
| `template` | `type`, `template_family`, `version`, `last_validated` | Контроль совместимости шаблонов |
| `task_contract` | `type`, `task_id`, `state`, `risk_level`, `created` | Структурная проверка lifecycle |
| `verification_record` | `type`, `task_id`, `result`, `created` | Сопоставление evidence с задачей |
| `evidence_report` | `type`, `scope`, `result`, `last_validated` | Единый формат отчётов |
| `audit_report` | `type`, `audit_scope`, `result`, `created` | Аудитная трассируемость |
| `generated_or_derived` | `type`, `derived_from`, `created`, `rebuildable` | Запрет скрытого source-of-truth |
| `unclear` | `type`, `status`, `note` | Явный маркер зоны для review |

## Index Implications

- index must be derived
- Markdown remains source of truth
- index is for navigation only
- index must not store approval, completion, or release decisions as authority

| Role | Should Be Indexed? | Index Purpose | Risk |
|---|---|---|---|
| `semantic_source_of_truth` | YES | Быстрый переход к каноническому правилу | MEDIUM (если индекс устареет) |
| `template` | YES | Навигация по шаблонам и версиям | LOW |
| `task_contract` | YES | Поиск активных/исторических контрактов | MEDIUM |
| `verification_record` | YES | Связь проверок с task_id | LOW |
| `evidence_report` | YES | Навигация по доказательствам | LOW |
| `audit_report` | YES | Сводный обзор рисков и покрытий | LOW |
| `example` | OPTIONAL | Поиск демонстрационных сценариев | LOW |
| `generated_or_derived` | YES | Явное отделение производных артефактов | MEDIUM |
| `unclear` | YES | Очередь для ручной классификации | MEDIUM |

## Do Not Automate Yet

- ambiguous policy interpretation
- approval decisions
- completion review decisions
- release readiness decisions
- ambiguous risk classification
- active-task mutation
- self-healing
- SQLite
- vector RAG
- backend/service layer
- autonomous execution

## Recommended Next Task

`22.3.1 — Source-of-Truth Map MVP`

Role classification сначала разделяет «тип документа», а затем source-of-truth map закрепляет «владельца смысла» для каждого крупного правила.
Без промежуточной ролевой модели карта владельцев будет смешивать шаблоны, отчёты и канонические правила.
Поэтому 22.3.1 логично выполнять сразу после этой классификации.

## Validation Evidence

| Command / Check | Status | Output Summary | Notes |
|---|---|---|---|
| verify `docs/MARKDOWN-ROLE-CLASSIFICATION.md` exists | PASS | документ создан | Проверено после записи |
| inspect `reports/milestone-22-markdown-to-script-inventory.md` | PASS | входной M22 отчёт найден | Использован как источник фактов |
| `git status --short` (read-only) | WARN | в репозитории есть pre-existing untracked файлы | Для этой задачи добавлен только `docs/MARKDOWN-ROLE-CLASSIFICATION.md` |
| inspect `data/` | NOT_FOUND | каталог отсутствует | Не создавался |
| inspect validation scripts read-only behavior | NOT_RUN | не подтверждалось в этой задаче отдельно | Вне минимально нужного объёма |

## Final Classification Result

`READY_WITH_WARNINGS`

Ролевая модель полная, и основные семейства Markdown-файлов классифицированы.
При этом остаются `unclear`-зоны (в первую очередь дубли `* 2.md`), которые требуют дальнейшего ручного закрепления ownership.
Это не блокирует переход к Source-of-Truth Map, но требует аккуратного шага без преждевременной автоматизации.

Recommended next task: `22.3.1 — Source-of-Truth Map MVP`.
