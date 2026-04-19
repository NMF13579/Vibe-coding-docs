<!-- ROLE: CANONICAL_POLICY -->
<!-- AUTHORITY: PRIMARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: yes -->
<!-- MUST_NOT_CONTAIN: runtime state, duplicate policy, archival history -->

# Document governance — роли, статусы, lifecycle

Каноническая модель **классификации документов** в этом репозитории.  
Связка: [`ARCHITECTURE.md`](../ARCHITECTURE.md) (архитектура слоёв), [`audit.md`](./audit.md) (разделы **State Consistency Audit** и **Document Governance Audit**) — правила здесь **не** дублируются в audit, audit только проверяет соответствие.

---

## Document roles and statuses

### Роли документов

| Role | Назначение |
|---|---|
| CANONICAL_POLICY | канонические правила и протоколы |
| RUNTIME_STATE | формальное runtime-состояние |
| SESSION_CONTEXT | контекст текущей/последней сессии |
| NARRATIVE_CONTEXT | человекочитаемый контекст проекта |
| NAVIGATION | маршрутизация по системе |
| ADAPTER | вход для IDE/агентов, без policy |
| REFERENCE | справочный документ |
| DEPRECATED | устаревший, не для runtime |
| ARCHIVE | исторический артефакт |

### Статусы документов

| Status | Значение |
|---|---|
| ACTIVE | используется в текущей системе |
| LIMITED | используется ограниченно, не как source of truth |
| DEPRECATED | не использовать в runtime |
| ARCHIVED | хранится только как история |

---

## Authority levels

| Authority | Значение |
|---|---|
| PRIMARY | главный источник истины в своей зоне |
| SECONDARY | вспомогательный, подчинён PRIMARY |
| TERTIARY | контекстный, не источник истины |
| NON-AUTHORITY | не должен использоваться как source of truth |

Правило приоритета:

> При конфликте документов выигрывает документ
> с более высоким authority.
> При равном authority конфликт выносится на пользователя
> или устраняется архитектурно.

---

## Lifecycle rules

**ACTIVE**

* используется в runtime или governance
* может обновляться агентом или owner по ownership
* участвует в маршрутах и проверках

**LIMITED**

* допустим как reference или support
* не должен быть основным source of truth

**DEPRECATED**

* не используется в runtime
* обязан содержать явную шапку DEPRECATED
* обязан ссылаться на заменяющий документ (REPLACED_BY)
* не фигурирует в navigation как рабочий путь

**ARCHIVED**

* не используется в runtime
* хранится только как исторический артефакт
* не фигурирует в navigation как рабочий путь

---

## Metadata standard

### Шапка для ACTIVE-документа:

```html
<!-- ROLE: [role] -->
<!-- AUTHORITY: [authority] -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent | owner | both | manual-only -->
<!-- SOURCE_OF_TRUTH: yes | no -->
<!-- MUST_NOT_CONTAIN: [что запрещено] -->
```

### Шапка для DEPRECATED-документа:

```html
<!-- ROLE: DEPRECATED -->
<!-- AUTHORITY: NON-AUTHORITY -->
<!-- STATUS: DEPRECATED -->
<!-- REPLACED_BY: [путь к заменяющему документу] -->
<!-- DO_NOT_USE_FOR: runtime, state decisions, active bootstrap -->
<!-- Archived: YYYY-MM -->
```

---

## Canonical document registry

| Файл | Role | Authority | Status | Updated by | Notes |
|---|---|---|---|---|---|
| LAYER-3/STATE.md | RUNTIME_STATE | PRIMARY | ACTIVE | agent | — |
| HANDOFF.md | SESSION_CONTEXT | SECONDARY | ACTIVE | agent | — |
| LAYER-3/project-status.md | NARRATIVE_CONTEXT | TERTIARY | ACTIVE | agent | — |
| llms.txt | NAVIGATION | SECONDARY | ACTIVE | owner | — |
| LAYER-1/agent-rules.md | CANONICAL_POLICY | PRIMARY | ACTIVE | owner | — |
| LAYER-1/state-transitions.md | CANONICAL_POLICY | PRIMARY | ACTIVE | owner | — |
| LAYER-1/event-dictionary.md | CANONICAL_POLICY | PRIMARY | ACTIVE | owner | — |
| LAYER-1/audit.md | CANONICAL_POLICY | PRIMARY | ACTIVE | owner | — |
| LAYER-1/document-governance.md | CANONICAL_POLICY | PRIMARY | ACTIVE | owner | — |
| CLAUDE.md | ADAPTER | NON-AUTHORITY | ACTIVE | owner | Adapter only |
| .cursor/rules/* | ADAPTER | NON-AUTHORITY | ACTIVE | owner | Adapter only |
| AGENTS.md | ADAPTER | NON-AUTHORITY | ACTIVE | owner | Adapter only |
| LAYER-3/session-log.md | REFERENCE | SECONDARY | ACTIVE | agent | Append only |
| CHANGELOG.md | REFERENCE | NON-AUTHORITY | LIMITED | both | Historical record |
| LAYER-1/deprecated/* | DEPRECATED | NON-AUTHORITY | DEPRECATED | manual-only | Replaced by: см. шапку каждого файла |

---

## Governance rules

1. Один PRIMARY в каждой authority-зоне.
2. ADAPTER-файлы не содержат policy.
3. Runtime state допускается только в STATE.md.
4. DEPRECATED и ARCHIVED не участвуют в runtime.
5. Новый документ получает metadata до начала использования.
6. Дублирующий authority → downgrade, deprecated или merge.
7. При downgrade или deprecation — все ссылки на документ в navigation-файлах (`llms.txt`, `ARCHITECTURE.md` и др.) обновляются в той же операции.
