# SOURCE-OF-TRUTH-MAP

## Executive Summary

AgentOS нужен источник‑истины (source of truth: главный документ по правилу), чтобы агент и человек ссылались на один и тот же первичный файл, а не на случайную копию.
Ясная карта снижает ошибки, когда правила дублируются в разных местах и трактуются по-разному.
Этот документ сопоставляет ключевые области правил AgentOS с текущими кандидатами‑владельцами.
Этот документ не решает конфликты владения, не удаляет дубли и не внедряет автоматизацию.

## Inputs Inspected

| Input / Path | Status | Notes |
|---|---|---|
| `reports/milestone-22-markdown-to-script-inventory.md` | USED | Использован как вход M22 и база рисков |
| `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | USED | Использован для ролевой модели и границ |
| `docs/` | FOUND | Проверены ключевые нормативные документы |
| `templates/` | FOUND | Проверены шаблонные правила и boundaries |
| `reports/` | FOUND | Проверены словари статусов и evidence-практика |
| `tasks/` | FOUND | Проверены контрактные и lifecycle-файлы |
| `examples/` | FOUND | Проверены ожидания по example-зоне |
| `scripts/` | FOUND | Проверены скрипты-валидаторы и аудитные точки |
| `core-rules/` | FOUND | Канонический модуль управления |
| `policies/` | FOUND | Политика рисков доступна |
| `quality/` | FOUND | Канонический модуль проверки |
| `data/` | FOUND | Каталог присутствует, но является derived layer |
| Root-level (`llms.txt`, `README.md`, `ROUTES-REGISTRY.md`) | FOUND | Использованы как навигация и контекст |

## Major Concept Map

| Concept / Rule Area | Owner Candidate | Ownership Status | Supporting Locations | Risk if Wrong | Recommendation |
|---|---|---|---|---|---|
| task contract structure | `tasks/templates/task-contract.md` | LIKELY | `workflow/MAIN.md`, `tasks/active-task.md` | HIGH | Закрепить один канонический контрактный шаблон |
| verification report structure | `reports/templates/verification-report.md` | LIKELY | `quality/MAIN.md`, `templates/verification.md` | MEDIUM | Уточнить приоритет template vs report-template |
| validation result semantics | `docs/VALIDATION.md` + профильные audit docs | DUPLICATED | `docs/RELEASE-READINESS-AUDIT.md`, `docs/TEMPLATE-PACKAGING-AUDIT.md` | MEDIUM | Вынести единый словарь статусов и ссылаться на него |
| status semantics | `state/MAIN.md` (lifecycle), профильные docs (checks) | DUPLICATED | `quality/MAIN.md`, `docs/COMPLETION-READINESS.md` | HIGH | Развести lifecycle-статусы и check-статусы официально |
| risk model | `docs/OPERATION-RISK-MODEL.md` | CLEAR | `docs/APPROVAL-REQUIREMENT-POLICY.md`, `security/MAIN.md` | HIGH | Считать документ единственным owner для risk classes |
| approval requirements | `docs/APPROVAL-REQUIREMENT-POLICY.md` | CLEAR | `docs/CONTROLLED-COMPLETION-WORKFLOW.md`, `security/MAIN.md` | HIGH | Ссылаться на policy как единственный источник решения approval_required |
| completion decision logic | `docs/COMPLETION-READINESS.md` + `docs/CONTROLLED-COMPLETION-WORKFLOW.md` | DUPLICATED | `quality/MAIN.md`, `workflow/MAIN.md` | HIGH | Утвердить главный owner, второй держать как процессный контекст |
| release readiness logic | `docs/RELEASE-READINESS-AUDIT.md` | LIKELY | `docs/STABLE-MVP-RELEASE-READINESS.md`, `reports/release-checklist.md` | HIGH | Зафиксировать owner релиз-аудита до frontmatter |
| template packaging rules | `docs/TEMPLATE-PACKAGING-AUDIT.md` | CLEAR | `scripts/audit-template-packaging.py` | MEDIUM | Держать semantics в doc, скрипт как проверка |
| install smoke expectations | `docs/TEMPLATE-PACKAGING-AUDIT.md` | LIKELY | `scripts/test-install.sh` | MEDIUM | Явно задокументировать PASS/WARN критерии |
| example project expectations | `docs/TEMPLATE-PACKAGING-AUDIT.md` | LIKELY | `scripts/test-example-project.sh`, `examples/simple-project/README.md` | MEDIUM | Уточнить owner примеров и их статус в release-гейте |
| audit report semantics | `quality/MAIN.md` | CLEAR | `docs/RELEASE-READINESS-AUDIT.md`, `docs/TEMPLATE-PACKAGING-AUDIT.md` | HIGH | Оставить единый owner в quality, профильные docs как специализация |
| boundary statements | `docs/SAFETY-BOUNDARIES.md` | CLEAR | `llms.txt`, `security/MAIN.md`, `workflow/MAIN.md` | HIGH | Считать safety-boundaries каноникой для boundary claims |
| forbidden claims | `docs/TEMPLATE-PACKAGING-AUDIT.md` + `docs/SAFETY-BOUNDARIES.md` | DUPLICATED | `docs/RELEASE-READINESS-AUDIT.md` | MEDIUM | Нужен единый список запретных формулировок |
| human decision boundaries | `docs/SAFETY-BOUNDARIES.md` | CLEAR | `workflow/MAIN.md`, `core-rules/MAIN.md` | HIGH | Сохранять human checkpoint правила как канон |
| generated or derived artifact rules | `llms.txt` + профильные audit docs | AMBIGUOUS | `docs/TEMPLATE-PACKAGING-AUDIT.md`, `reports/*` | MEDIUM | Отдельно выделить owner для derived artifacts |
| future frontmatter metadata | `UNASSIGNED` | UNASSIGNED | `reports/milestone-22-markdown-to-script-inventory.md` | MEDIUM | Сначала утвердить ownership map, потом стандарт frontmatter |
| future index navigation rules | `UNASSIGNED` | UNASSIGNED | `reports/milestone-22-markdown-to-script-inventory.md`, `data/ (NOT_FOUND)` | MEDIUM | Не внедрять index до закрепления source-of-truth owners |

## Duplicated Ownership Areas

| Concept / Rule Area | Locations | Duplication Type | Risk | Future Action |
|---|---|---|---|---|
| status semantics (lifecycle vs check statuses) | `state/MAIN.md`, `quality/MAIN.md`, `docs/COMPLETION-READINESS.md`, audit docs | DANGEROUS_DUPLICATION | HIGH | Разделить словари и назначить primary owner |
| completion logic | `docs/COMPLETION-READINESS.md`, `docs/CONTROLLED-COMPLETION-WORKFLOW.md` | SCRIPTABLE_DUPLICATION | MEDIUM | Зафиксировать primary/secondary owner |
| forbidden claims / non-autonomy wording | `docs/SAFETY-BOUNDARIES.md`, `docs/TEMPLATE-PACKAGING-AUDIT.md`, `docs/RELEASE-READINESS-AUDIT.md` | SAFE_DUPLICATION | LOW | Оставить дубли, но унифицировать формулировки |
| risk/approval link semantics | `docs/OPERATION-RISK-MODEL.md`, `docs/APPROVAL-REQUIREMENT-POLICY.md` | NEEDS_REVIEW | MEDIUM | Явно описать границу: модель риска vs policy decision |

## Ambiguous or Unassigned Areas

| Concept / Rule Area | Status | Why Unclear | Risk | Recommended Follow-Up |
|---|---|---|---|---|
| generated/derived artifact ownership | AMBIGUOUS | Нет одного явного owner документа по derived artifacts | MEDIUM | Ввести отдельный canonical раздел/документ |
| frontmatter metadata ownership | UNASSIGNED | Спецификация frontmatter ещё не создана | MEDIUM | Делать в `22.4.1` после фиксации owner map |
| index navigation ownership | UNASSIGNED | `data/` отсутствует, index-правила пока только как идея | MEDIUM | Отложить до frontmatter и source-of-truth стабилизации |

## Semantic Markdown Owners to Preserve

| Source-of-Truth Area | Owner Candidate | Why It Must Stay Semantic | Allowed Script Support |
|---|---|---|---|
| architecture | `docs/architecture.md` | Объясняет причины решений, не только формат | Проверка наличия обязательных разделов |
| guardrail philosophy | `docs/SAFETY-BOUNDARIES.md` | Границы и смысл human-control | Проверка boundary-фраз |
| risk rationale | `docs/OPERATION-RISK-MODEL.md` | Нужна понятная логика классификации | Валидация списка risk classes |
| approval rationale | `docs/APPROVAL-REQUIREMENT-POLICY.md` | Обосновывает, когда approval обязателен | Проверка mapping и forbidden bypass claims |
| completion rationale | `docs/COMPLETION-READINESS.md` | Описывает правила readiness и stop_reason | Проверка vocab и required fields |
| release rationale | `docs/RELEASE-READINESS-AUDIT.md` | Фиксирует границы релиз-аудита | Проверка markers/allowed statuses |
| limitations | `docs/limitations.md` | Ограничения продукта должны читаться человеком | Проверка структуры документа |
| human decision rules | `docs/SAFETY-BOUNDARIES.md` | Финальные решения не должны быть автоматическими | Проверка запретных заявлений об автономии |
| lessons | `lessons/lessons.md` | Человеческая ретроспектива причин ошибок | Проверка наличия обязательных полей записи |

## Script Dependency Map

| Future Script / Validator | Needs Source-of-Truth For | Required Owner Status Before Implementation | Risk if Implemented Too Early |
|---|---|---|---|
| `validate-frontmatter.py` | frontmatter metadata owner | CLEAR or LIKELY | Зафиксирует неверную схему полей |
| `validate-status-semantics.py` | единый owner словаря статусов | CLEAR | Ложные FAIL/PASS из-за смешанных словарей |
| `validate-required-sections.py` | owner обязательных разделов по семействам | CLEAR or LIKELY | Сломает легитимные документы |
| `validate-boundary-claims.py` | owner boundary/forbidden claims | CLEAR | Противоречивые проверки non-autonomy |
| `build-index.py` | owner правил derived index | CLEAR | Индекс станет скрытым источником истины |
| `validate-index.py` | owner полей index и rebuild rules | CLEAR | Ложная валидность неполного индекса |
| `audit-metadata-consistency.py` | owner метаданных между docs/tasks/reports | LIKELY minimum | Отчёты начнут конфликтовать между собой |

## Source-of-Truth Boundaries

| Boundary | Rule | Risk if Violated |
|---|---|---|
| source-of-truth doc vs report | Отчёт фиксирует наблюдение, не переопределяет каноническое правило | Агент начнёт брать временный отчёт как правило |
| source-of-truth doc vs template | Шаблон помогает оформлению, но не меняет смысл каноники | Дрейф правил при обновлении шаблонов |
| source-of-truth doc vs generated artifact | Generated/derived артефакт всегда вторичен | Потеря управляемости и скрытая authority в артефакте |
| source-of-truth doc vs index | Index только навигация, rebuild из Markdown обязателен | Индекс станет единственным источником и устареет |
| evidence vs approval | Evidence = доказательства; approval = решение человека | Ложная автоматическая авторизация действий |
| audit vs decision | Audit сообщает статус, но не принимает финальное решение | Ошибочные релиз/completion решения без человека |

## Rules for Future Consolidation

- Консолидация не выполняется в этой задаче.
- Дублированный текст нельзя удалять, пока ownership не закреплён.
- Safety-critical boundary statements могут оставаться дублированными намеренно.
- Скрипты должны ссылаться на канонический смысл, а не становиться скрытым источником истины.
- Решения по approval, completion и release должны оставаться под контролем человека.

## Do Not Automate Yet

- ambiguous policy interpretation
- ambiguous risk classification
- approval decisions
- completion review decisions
- release readiness decisions
- active-task mutation
- self-healing
- SQLite
- vector RAG
- backend/service layer
- autonomous execution

## Recommended Next Task

`22.4.1 — Frontmatter Standard MVP`

Frontmatter-стандарт должен идти после source-of-truth map, потому что без закреплённых владельцев полей мы зафиксируем нестабильную модель метаданных.
Сначала нужно стабилизировать зоны `DUPLICATED`/`AMBIGUOUS`/`UNASSIGNED` хотя бы до уровня рабочей договорённости.
Если это не сделать, валидатор frontmatter начнёт кодировать спорные решения и усилит дрейф.

## Validation Evidence

| Command / Check | Status | Output Summary | Notes |
|---|---|---|---|
| verify `docs/SOURCE-OF-TRUTH-MAP.md` exists | PASS | файл создан | Проверено после записи |
| inspect `reports/milestone-22-markdown-to-script-inventory.md` | PASS | найден и использован | Вход M22 доступен |
| inspect `docs/MARKDOWN-ROLE-CLASSIFICATION.md` | NOT_FOUND | файл отсутствует | Зафиксировано как missing input |
| inspect `data/` | NOT_FOUND | каталог отсутствует | Не создавался |
| `git status --short` | WARN | В репозитории много pre-existing untracked файлов | Для этой задачи добавлен только `docs/SOURCE-OF-TRUTH-MAP.md` |

## Final Source-of-Truth Map Result

`READY_WITH_WARNINGS`

Основные области правил получили кандидатов-владельцев, и для большинства зон ownership можно считать `CLEAR` или `LIKELY`.
Одновременно остаются дублированные и не до конца закреплённые зоны (особенно статусная семантика и derived/index область).
Это не блокирует старт frontmatter-этапа, но требует осторожного шага с явной фиксацией owner-границ до кодирования валидаторов.

Recommended next task: `22.4.1 — Frontmatter Standard MVP`.
