<!-- ROLE: NARRATIVE_CONTEXT -->
<!-- AUTHORITY: TERTIARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: formal runtime state как канон, датированная история сессий -->

# Project Status

## Описание проекта

**Vibe-coding-docs** — шаблон многослойной документации для AI-агентов и команд: правила и протоколы (LAYER-1), продуктовые материалы (LAYER-2), память и статус (LAYER-3). Репозиторий служит каркасом: после копирования владелец заполняет слои под свой продукт.

## Текущий этап (нарратив)

Каркас шаблона доведён до **стабильного релиза документации v1.1.0**: пройдены этапы валидации ссылок и терминологии, релизные чеклисты и changelog согласованы, есть итоговый `AUDIT-REPORT.md`. Это описание этапа **шаблона**, а не готовности конкретного продукта после копирования репозитория.

## Ключевые цели

- Закрепить единый **control plane** состояния в `LAYER-3/STATE.md` и не смешивать его с нарративом и сессионными заметками.
- Вести формальные задачи в `LAYER-3/roadmap.md` и подтверждать Discovery по процедуре в `LAYER-2/discovery/project-interview.md`.
- Сохранять переносимость: агенты и люди ориентируются по `llms.txt`, правилам LAYER-1 и контракту HANDOFF без дублирования канона состояния.

## Текущие риски и неопределённости

- Слои Discovery → Deploy в таблице ниже помечены как **не заполнены** (`❓`) до старта реального проекта на базе шаблона.
- Подтверждение ключевых артефактов Discovery (в т.ч. `interview-summary.md`) — **not-started** до явного «Да» владельца по процедуре интервью.
- Детальная хронология изменений и сессий вынесена в `LAYER-3/session-log.md` и `CHANGELOG.md`, а не в этот файл.

## Подтверждение ключевых артефактов (Discovery)

Статусы: `not-started` | `pending-approval` | `accepted`. Колонка **Approved by** заполняется только после явного «Да» по процедуре в [`LAYER-2/discovery/project-interview.md`](../LAYER-2/discovery/project-interview.md) (секция **Confirmation**).

| Артефакт | Статус | Approved by |
|----------|--------|-------------|
| `LAYER-2/discovery/interview-summary.md` | not-started | — |

## Слои (готовность шаблона)

- Discovery: ❓
- Specs: ❓
- UX: ❓
- QA: ❓
- Deploy: ❓
- Lessons: ❓

Пояснение: знаки `❓` в исходном шаблоне ожидаемы до начала реального проекта.

## Краткий summary последних изменений

Разведены роли **STATE.md** (формальный канон), **HANDOFF.md** (контракт сессии) и **project-status.md** (этот нарратив). Полный лог сессий и прежняя летопись «Последнее действие» — в [`session-log.md`](./session-log.md); единый bootstrap и governance — в [`LAYER-1/agent-rules.md`](../LAYER-1/agent-rules.md), [`LAYER-1/audit.md`](../LAYER-1/audit.md), [`LAYER-1/document-governance.md`](../LAYER-1/document-governance.md).
