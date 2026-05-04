# Milestone 22 — Markdown-to-Script Optimization Inventory

## Executive Summary
Проверены разрешённые области: `docs/`, `templates/`, `scripts/`, `reports/`, `examples/`, `tasks/`, `core-rules/`, `policies/`, `quality/`, `data/`, а также релевантные корневые файлы (`llms.txt`). Найдена повторяемость правил в статусах, границах (boundary statements: фразы-ограничители), frontmatter (служебный блок метаданных в начале Markdown), а также дубли файлов с суффиксом ` 2`.

Смысловые документы (архитектура, политика, ограничения, объяснения рисков, решения человека) должны остаться в Markdown. Повторяемые детерминированные правила (одинаковые и проверяемые автоматически) подходят для постепенного переноса в скриптовые проверки.

Не следует автоматизировать решения, где нужен человек: approval (одобрение), completion/release решения, неоднозначная трактовка политики и рисков, активные мутации задач и автономное выполнение.

## Observed Repository Coverage

| Path | Status | Notes |
|---|---|---|
| `docs/` | FOUND | Много правил, статусов и границ; есть дубли `* 2.md` |
| `templates/` | FOUND | Шаблоны контрактов и переходов; есть дубли `* 2.md` |
| `scripts/` | FOUND | Уже есть валидаторы и аудиты; часть покрывает frontmatter/sections/status |
| `reports/` | FOUND | Отчёты доказательств и аудитов; много дублирующих копий `* 2.md` |
| `examples/` | FOUND | Сценарии и пример проекта; присутствуют дубли `* 2.md` |
| `tasks/` | FOUND | Контракты и очередь; присутствуют дубли `* 2.md` |
| `core-rules/` | FOUND | Канонические правила приоритета и границ |
| `policies/` | FOUND | YAML-политики, не Markdown |
| `quality/` | FOUND | Канонический модуль верификации |
| `data/` | FOUND | JSON-артефакты, не Markdown |

## Markdown Role Inventory

| File / Family | Current Role | Should Stay MD? | Scriptable Parts | Risk |
|---|---|---|---|---|
| `llms.txt` + `core-rules/MAIN.md` + `state/MAIN.md` + `workflow/MAIN.md` + `quality/MAIN.md` + `security/MAIN.md` | semantic source of truth | YES | Проверка обязательного набора и ссылочной целостности | MEDIUM |
| `templates/*.md` | template | YES | Проверка обязательных секций и полей | LOW |
| `tasks/**/TASK.md`, `tasks/active-task.md`, `tasks/queue/*.md` | task contract | YES | Проверка frontmatter, статусных полей, forbidden claims (запрещённые формулировки) | HIGH |
| `reports/verification*.md`, `reports/*completion-review*.md` | verification record | YES | Required sections check (проверка обязательных разделов), статусные маркеры | MEDIUM |
| `reports/*evidence*.md` | evidence report | YES | Проверка формата доказательств, наличия команд и статусов | MEDIUM |
| `reports/*audit*.md` | audit report | YES | Проверка структуры, boundary-фраз и запретных заявлений | MEDIUM |
| `examples/**/*.md` | example | YES | Проверка, что examples не объявляют authority (право решать) | MEDIUM |
| `docs/FRONTMATTER-STANDARD.md`, `docs/INDEX-SCHEMA.md` | generated or derived guidance | YES | Проверка согласованности с каноникой и boundary-ограничениями | MEDIUM |
| `* 2.md` / `* 2.py` / `* 2.sh` семейства | unclear | NO (как authoritative) | Авто-детектор конфликтных дублей | HIGH |

## Markdown-to-Script Candidates

| Rule / Pattern | Current Markdown Locations | Candidate Script | Why Scriptable | Priority |
|---|---|---|---|---|
| Required section checks | `templates/`, `reports/`, `docs/ACTIVE-TASK-VALIDATION.md` | `scripts/validate-required-sections.py` (already present) + расширение coverage | Секции легко формализуются списком | HIGH |
| Status marker checks | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `reports/` | `scripts/validate-status-semantics.py` (already present) | Статусы конечный словарь и правила переходов | HIGH |
| Forbidden claim checks | `docs/BOUNDARY-CLAIMS.md`, `docs/HUMAN-APPROVAL-EVIDENCE.md` | `scripts/validate-boundary-claims.py` (already present) | Запрещённые фразы проверяются детерминированно | HIGH |
| Boundary statement checks | `docs/SAFETY-BOUNDARIES.md`, `docs/BOUNDARY-CLAIMS.md`, `quality/MAIN.md` | Future: `scripts/validate-boundary-statements.py` | Набор обязательных ограничителей фиксируемый | MEDIUM |
| Evidence format checks | `reports/*evidence*.md`, `reports/*completion-review*.md` | Future: `scripts/validate-evidence-report.py` | Единый табличный формат и статусы | MEDIUM |
| Template structure checks | `templates/*.md` | `scripts/check-template-integrity.py` (already present) | Структура и обязательные файлы проверяемы | HIGH |
| Frontmatter presence checks | `tasks/`, `reports/verification.md`, `docs/EXECUTION-SESSION.md` | `scripts/validate-frontmatter.py` (already present) | Наличие и базовый синтаксис YAML проверяемы | HIGH |
| Source-of-truth reference checks | `llms.txt`, `docs/SOURCE-OF-TRUTH-MAP.md`, canonical modules | Future: `scripts/validate-source-of-truth-map.py` | Можно сверять owner/authority ссылки | HIGH |
| Index consistency checks | `docs/INDEX-SCHEMA.md`, `data/*.json` | `scripts/validate-index.py` + `scripts/build-index.py` (already present as base) | Поля и rebuild-правила формализуются | MEDIUM |

## Meaningful Markdown to Preserve

| Markdown Area | Why It Should Stay MD | Automation Boundary |
|---|---|---|
| Architecture explanations | Нужен контекст причин, не только проверка фактов | Автоматизация проверяет только структуру/ссылки |
| Guardrail philosophy | Это смысловые границы безопасности | Скрипт не должен подменять смысловую интерпретацию |
| Risk model rationale | Оценка риска часто контекстная | Скрипт проверяет только формат и обязательные поля |
| Approval policy rationale | Требует человеческого решения и трактовки | Не автоматизировать финальное approval-решение |
| Completion decision logic | Финал задачи остаётся у человека | Скрипты только готовят доказательства |
| Release decision logic | Release-решение не детерминируется полностью | Скрипт не даёт authority на релиз |
| Limitations | Это живое описание границ системы | Автопроверка только на наличие раздела |
| Usage docs | Нужны объяснения для людей | Скрипт не оценивает полноту практических советов |
| Troubleshooting | Часто основано на опыте и кейсах | Можно проверять только каркас разделов |
| Lessons | Человеческий вывод по инцидентам | Не автоматизировать вывод и приоритет уроков |
| Human decisions | Это зона ответственности владельца/ревьюера | Запрет на автоматическую замену решения |
| Evidence reports | Нужны текстовые выводы и контекст проверки | Скрипт валидирует формат, не вывод |

## Duplication Audit

| Repeated Content | Locations | Duplication Type | Risk | Recommendation |
|---|---|---|---|---|
| Файлы-копии с суффиксом ` 2` (`*.md`, `*.py`, `*.sh`) | `docs/`, `templates/`, `reports/`, `examples/`, `tasks/`, `scripts/` | dangerous duplication | HIGH | Добавить скрипт детекта и явную политику canonical-vs-copy |
| Повтор статусов в разных документах (`PASS/FAIL/WARN/NOT_RUN/ERROR/...`) | `docs/STATUS-SEMANTICS.md`, `docs/COMPLETION-READINESS.md`, `reports/*` | scriptable duplication | HIGH | Централизовать словарь статусов через валидатор |
| Повтор boundary-фраз (“PASS is not approval” и аналоги) | `docs/HUMAN-APPROVAL-EVIDENCE.md`, `docs/BOUNDARY-CLAIMS.md`, `docs/CONTROLLED-*` | safe duplication | MEDIUM | Оставить как защитную избыточность + автоматическая проверка фраз |
| Повтор frontmatter-правил в описаниях и скриптах | `docs/ACTIVE-TASK-FORMAT.md`, `docs/EXECUTION-SESSION.md`, `scripts/validate-*.py` | scriptable duplication | MEDIUM | Вынести обязательные поля в единый машинный список |
| Повтор переходных правил task/review/completion | `docs/TASK-STATE-MACHINE.md`, `docs/TASK-TRANSITION-RULES.md`, `docs/CONTROLLED-COMPLETION*.md` | needs review | HIGH | Сначала согласовать owner правил, потом автоматизировать |

Total dangerous duplications found: 3
Total scriptable duplications found: 2

## MD-to-Agent Gap Audit

| Gap Type | Example | Current Protection | Missing Check | Priority |
|---|---|---|---|---|
| rule gap | Правило “не считать NOT_RUN как PASS” повторяется текстом | Частичные проверки в docs и отдельных скриптах | Единый универсальный check для всех отчётов | HIGH |
| structure gap | Разные семейства отчётов имеют близкую, но не идентичную структуру | Локальные шаблоны | Единый required-sections профиль по типу отчёта | HIGH |
| status gap | Статусы смешаны между lifecycle и validation-result | `docs/STATUS-SEMANTICS.md` + частичные валидаторы | Автопроверка допустимого словаря по контексту | HIGH |
| source-of-truth gap | Дубли `* 2` могут быть приняты за первоисточник | Ручной контроль | Автодетектор конфликтующих пар canonical/copy | HIGH |
| context gap | Отчёты иногда содержат вывод без явной границы наблюдение/рекомендация | Ревью человеком | Линтер разделов Observation vs Recommendation | MEDIUM |
| execution gap | Некоторые “аудиты” могут запускать вложенные команды и менять временное состояние | Ручная проверка скриптов перед запуском | Явный флаг read-only contract для скриптов | MEDIUM |
| verification gap | Нет одного реестра, какие проверки обязательны для каждого типа задач | Частичные run-all и audit-скрипты | Матрица “тип задачи -> обязательные проверки” | HIGH |
| human-review gap | Риск автоматической трактовки PASS как approval/completion | Boundary-документы | Автопроверка запрета claim-формулировок в отчётах | HIGH |

## Status and Boundary Semantics

| Status / Boundary | Current Meaning | Locations | Drift Risk | Recommendation |
|---|---|---|---|---|
| `PASS` | Проверка пройдена | `reports/`, `docs/TEMPLATE-INTEGRITY.md` | MEDIUM | Фиксировать контекст PASS (какой именно check) |
| `FAIL` | Проверка не пройдена | `reports/`, `docs/*` | MEDIUM | Запретить размытые FAIL без причины |
| `WARN` | Есть риск/неполнота без критического сбоя | `docs/TEMPLATE-INTEGRITY.md`, audit reports | MEDIUM | Унифицировать WARN vs PASS_WITH_WARNINGS |
| `NOT_RUN` | Проверка не запускалась | scenarios, checklists, отчёты | HIGH | Обязательная причина `NOT_RUN` |
| `ERROR` | Ошибка выполнения проверки | docs/scenarios/reports | HIGH | Явное разделение FAIL (логика) и ERROR (инструмент) |
| `READY` | Готовность на текущем этапе | queue/examples/reviews | MEDIUM | Проверять контекст готовности (к чему READY) |
| `NEEDS_REVIEW` | Нужна ручная проверка | scenarios/checklists/reports | LOW | Оставить как human-controlled статус |
| `APPROVED` | Явное человеческое одобрение | approval/review/task flows | HIGH | Проверять наличие approval evidence |
| `BLOCKED` | Выполнение остановлено правилом/риском | policies/docs/templates | HIGH | Обязательные поля причины блокировки |
| `COMPLETED` | Задача завершена | task lifecycle docs/reports | MEDIUM | Проверять наличие evidence до completion |
| `FAILED` | Задача/сессия завершилась с ошибкой | state/docs/reports | MEDIUM | Проверка корректного recovery шага |
| Boundary: “PASS is not approval” | PASS проверки не равен решению человека | `docs/HUMAN-APPROVAL-EVIDENCE.md`, `docs/BOUNDARY-CLAIMS.md` | HIGH | Проверять присутствие boundary-фразы в критичных отчётах |
| Boundary: “Markdown remains source of truth” | Markdown — первоисточник смысла | `llms.txt`, `docs/BOUNDARY-CLAIMS.md`, `docs/INDEX-SCHEMA.md` | HIGH | Проверка запрета claim “index is source of truth” |

## Script Readiness Map

| Script / Future Script | Purpose | Source-of-Truth Needed | Read-only? | Priority |
|---|---|---|---|---|
| `scripts/validate-required-sections.py` | Проверка обязательных разделов | Report/template section profiles | NOT_CONFIRMED | HIGH |
| `scripts/validate-status-semantics.py` | Проверка корректности статусов | Единый словарь статусов и контекстов | NOT_CONFIRMED | HIGH |
| `scripts/validate-boundary-claims.py` | Проверка запретных/обязательных boundary-формулировок | `docs/BOUNDARY-CLAIMS.md` | NOT_CONFIRMED | HIGH |
| `scripts/check-template-integrity.py` | Проверка структуры template-паков | Template contract files | CONFIRMED (read-only by inspection) | HIGH |
| `scripts/validate-frontmatter.py` | Проверка frontmatter | Frontmatter standard | NOT_CONFIRMED | HIGH |
| `scripts/validate-index.py` | Проверка согласованности индекса | Index schema + derived rule | NOT_CONFIRMED | MEDIUM |
| `scripts/build-index.py` | Сборка derived index | Index schema + source map | NOT_CONFIRMED | MEDIUM |
| Future: `scripts/validate-source-of-truth-map.py` | Проверка owner/authority связей | `llms.txt` + canonical modules + source map | YES (планируемый read-only) | HIGH |
| Future: `scripts/check-duplicate-canonical-files.py` | Детект конфликтующих дублей (`* 2`) | Canonical naming policy | YES (планируемый read-only) | HIGH |
| Future: `scripts/validate-evidence-report.py` | Формат и полнота evidence-таблиц | Evidence/report contract | YES (планируемый read-only) | MEDIUM |

## Frontmatter Readiness

| File Family | Useful Metadata | Benefit | Risk |
|---|---|---|---|
| `tasks/**` | `task.id`, `state`, `risk_level`, `acceptance_criteria` | Стабильная машинная проверка контрактов | Риск неправильного owner поля |
| `reports/*completion-review*.md` | `task_id`, `result`, `verified_at`, `review_scope` | Сопоставление результата и доказательств | Формальная структура без смысловой ясности |
| `reports/*evidence*.md` | `task_id`, `commands`, `evidence_status` | Авто-сверка покрытия проверок | Ошибка трактовки PASS как финального решения |
| `docs/policy/*.md` семейства | `owner`, `authority`, `status` | Ясность первоисточника правил | Дрейф при дубликатах `* 2.md` |
| `templates/*.md` | `template_type`, `required_sections` | Единая валидация шаблонов | Жёсткость шаблона против реальных кейсов |

## Index Readiness

| Entity | Fields Needed | Consumer | Priority |
|---|---|---|---|
| Canonical modules | `path`, `module`, `authority`, `status` | Validators, audit tools | HIGH |
| Task contracts | `task_id`, `state`, `risk_level`, `updated_at` | Task health / readiness checks | HIGH |
| Reports | `report_type`, `task_id`, `result`, `created_at` | Evidence aggregation | MEDIUM |
| Templates | `template_name`, `required_sections`, `version` | Template integrity checks | MEDIUM |
| Status vocabulary | `status`, `context`, `allowed_meaning` | Status validator | HIGH |

`data/index.json` must be derived — Markdown remains source of truth.
Index must be rebuildable from Markdown at any time.
Index must not store approval, completion, or release decisions as authority.

## Do Not Automate Yet

- approval decisions
- completion review decisions
- release readiness decisions
- ambiguous policy interpretation
- ambiguous risk classification
- active-task mutation
- self-healing
- SQLite
- vector RAG
- backend/service layer
- autonomous execution

## Recommended Next M22 Tasks

| # | Task | Status | Reason |
|---|---|---|---|
| 1 | Markdown Role Classification | CONFIRMED | Уже есть чёткие семейства ролей, нужен формальный owner-map |
| 2 | Source-of-Truth Map | CONFIRMED | Высокий риск из-за дублей и пересечения authority |
| 3 | Frontmatter Standard | ADJUSTED | Делать после фиксации source-of-truth владельцев |
| 4 | Frontmatter Validator | ADJUSTED | Привязать к утверждённому стандарту, иначе закрепим дрейф |
| 5 | Status Semantics Validator | CONFIRMED | Высокий риск смешения статусов |
| 6 | Required Sections Validator | CONFIRMED | Большая повторяемость структурных правил |
| 7 | Boundary Claims Validator | CONFIRMED | Критично для защиты human-controlled решений |
| 8 | Index Schema | ADJUSTED | Только как derived слой после source map и frontmatter |
| 9 | Build Index | ADJUSTED | После schema и явного запрета authority в index |
| 10 | Validate Index | ADJUSTED | После build; включить rebuildability checks |
| 11 | Audit Uses Index | DEFERRED | Сначала стабилизировать исходные MD-контракты |
| 12 | Negative Fixtures | CONFIRMED | Нужны тесты на запрещённые claim и статусные ошибки |
| 13 | Evidence Report | CONFIRMED | Нужна единая форма доказательств NOT_RUN/ERROR/PASS |
| 14 | Completion Review | CONFIRMED | Оставить human-controlled финальное решение |

## Validation Evidence

| Command | Status | Output Summary | Notes |
|---|---|---|---|
| `bash scripts/run-all.sh` | PASS | `PASS: task validation passed`; `PASS: verification validation passed` | Read-only confirmed by source inspection |
| `python3 scripts/audit-agentos.py` | NOT_RUN | Скрипт пишет `reports/audit.md` | read-only not confirmed |
| `python3 scripts/audit-template-packaging.py` | PASS | `TEMPLATE_PACKAGING_AUDIT_RESULT: PASS` | Запущен; работа во временной папке, мутаций репозитория не выявлено |
| `python3 scripts/test-negative-fixtures.py` | NOT_RUN | Запускает набор команд, где репозиторные мутации нельзя исключить быстрым чтением всей цепочки | read-only not confirmed |

## Final Inventory Result

**READY_WITH_WARNINGS**

Обнаружены опасные дубли (включая многочисленные `* 2` копии) и высокий риск дрейфа source-of-truth между близкими документами. При этом блокирующей неоднозначности для старта следующего шага нет: роль Markdown как первоисточника уже явно зафиксирована, а детерминированные проверки можно наращивать поэтапно. Переход к классификации ролей можно продолжать, но только с явной фиксацией owner/authority перед расширением frontmatter и index.

Highest-priority recommended next task: **Markdown Role Classification**.
