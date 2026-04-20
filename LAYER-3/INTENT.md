<!-- ROLE: NARRATIVE_CONTEXT -->
<!-- AUTHORITY: TERTIARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: policy rules, runtime state, routing logic -->

# INTENT

Этот файл описывает намерение системы.
Используется для понимания приоритетов, но не задаёт правила.

---

## Current intent
- построить стабильный AI-governed workspace
- исключить architecture drift
- приоритет: determinism над flexibility
- приоритет: clarity над brevity

## Non-goals
- не оптимизировать скорость за счёт корректности
- не добавлять новые слои без явной необходимости
- не упрощать governance ради краткости
- не мержить слои

## What success looks like
- система масштабируется без участия владельца
- агент не переизобретает закрытые решения
- новые участники понимают систему без онбординга
