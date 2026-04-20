<!-- ROLE: CANONICAL_POLICY -->
<!-- AUTHORITY: PRIMARY для медицинских сценариев -->
<!-- SOURCE_OF_TRUTH: yes -->
<!-- UPDATED_BY: owner -->

> Trigger: медицинский домен, границы ИИ, клинические сценарии, ПДн
> Read-time: ~5 min
> Filled-by: owner / agent (по запросу)
> Needs-approval: yes (для изменений границ)
> Next: [LEGAL-152FZ.md](./LEGAL-152FZ.md), [UX-CHECKLIST-MEDICAL.md](./UX-CHECKLIST-MEDICAL.md)

# Medical Safety — Границы использования

Этот документ задаёт **продуктовые и операционные границы**: что допустимо без ограничений, что только с участием человека и что нельзя автоматизировать «под ключ». Юридические формулировки и ПДн — в [LEGAL-152FZ.md](./LEGAL-152FZ.md); технические меры — в [security.md](./security.md). Юрисдикция и классификация изделия/ПО определяются отдельно с юристом.

## Можно без ограничений

- Обучение, тренинги, симуляции
- Внутренние административные процессы
- Документирование, шаблоны, организационные задачи

## Только с human review

- Decision support (поддержка принятия решений)
- Структурированные клинические резюме
- Triage-adjacent сценарии
- Любые outputs, влияющие на клинические решения

## Нельзя в автономном режиме

- Постановка диагноза
- Назначение лечения или препаратов
- Финальные клинические решения без врача
- Использование реальных данных пациента в LLM вне разрешённого контура

**Autonomous clinical use** (когда ИИ подменяет врача по итоговому клиническому решению) **запрещён**.

## Обязательные правила

- AI-агент не ставит диагноз
- AI-агент не заменяет врача
- educational content ≠ clinical advice
- human oversight обязателен для клинических outputs
- legal boundary зависит от юрисдикции

**Real patient data in LLM:** передача идентифицируемых или клинически чувствительных данных пациента в сторонние LLM — **только** при явно оформленном разрешённом контуре (договор/DPA, локализация, политика оператора, согласие); иначе — **нельзя**. Детали — [security.md](./security.md), [LEGAL-152FZ.md](./LEGAL-152FZ.md).

## Связанные документы

- [LEGAL-152FZ.md](./LEGAL-152FZ.md)
- [security.md](./security.md)
- [UX-CHECKLIST-MEDICAL.md](./UX-CHECKLIST-MEDICAL.md)
- [MEDICAL-ROLES-AND-PERMISSIONS.md](./MEDICAL-ROLES-AND-PERMISSIONS.md)
- [MEDICAL-DASHBOARDS.md](./MEDICAL-DASHBOARDS.md)
