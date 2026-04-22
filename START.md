# START — с чего начать

> Primary human route: `ROUTES-REGISTRY.md` → core modules (`core-rules/`, `state/`, `architecture/`, `workflow/`).
> Legacy `LAYER-*` материалы остаются как reference/history layer.

## 👤 Ты человек — выбери кто ты:

| Кто ты | Куда идти | Что пропустить на первом шаге |
|--------|-----------|--------------------------------|
| Новичок без опыта | [ROUTES-REGISTRY.md](./ROUTES-REGISTRY.md) → [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) | legacy `LAYER-*` как primary route |
| Врач / менеджер / эксперт | [ROUTES-REGISTRY.md](./ROUTES-REGISTRY.md) → [medical/MAIN.md](./medical/MAIN.md) | legacy medical docs как primary route |
| Потерял контекст | [state/MAIN.md](./state/MAIN.md) → `LAYER-3/STATE.md` / `HANDOFF.md` (по маршруту) | — |
| IDE user / разработчик | [QUICK-START.md](./QUICK-START.md) | [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) |
| AI-agent | `llms.txt` | всё остальное |

*Дальше по продукту: UX — [`LAYER-1/UX-CHECKLIST-MEDICAL.md`](./LAYER-1/UX-CHECKLIST-MEDICAL.md), роли — [`LAYER-1/MEDICAL-ROLES-AND-PERMISSIONS.md`](./LAYER-1/MEDICAL-ROLES-AND-PERMISSIONS.md), дашборды — [`LAYER-1/MEDICAL-DASHBOARDS.md`](./LAYER-1/MEDICAL-DASHBOARDS.md) (ссылки также в MEDICAL-SAFETY).*

## 🤖 Ты AI-агент (Claude Code, Cursor и др.):

AI-agent: прочитай `llms.txt` и следуй только ему.
Routing spine (stub): `ROUTES-REGISTRY.md`.
Правила поведения — в `LAYER-1/agent-rules.md`.

## Обязательное правило

Plan -> Confirm -> Execute.  
Без подтверждения владельца изменения не вносятся.
