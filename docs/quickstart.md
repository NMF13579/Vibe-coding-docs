# AgentOS Quickstart

## Requirements

- Git repository
- Bash
- Python 3
- pip

## Install minimal template

```bash
cd /path/to/your/git-project
bash /path/to/AgentOS/install.sh --minimal --dry-run
bash /path/to/AgentOS/install.sh --minimal
```

## Install full template

```bash
cd /path/to/your/git-project
bash /path/to/AgentOS/install.sh --full --dry-run
bash /path/to/AgentOS/install.sh --full
```

## Validate installation

```bash
python3 scripts/agentos-validate.py all
python3 scripts/agentos-validate.py all --json
```

Focused validation commands stay available for debugging:

```bash
python3 scripts/agentos-validate.py template
python3 scripts/agentos-validate.py negative
python3 scripts/agentos-validate.py guard
python3 scripts/agentos-validate.py audit
python3 scripts/agentos-validate.py queue
python3 scripts/agentos-validate.py runner
```

## Verify installer

Run the install smoke test:

```bash
bash scripts/test-install.sh
```

## Validate example project

Run the example project validation:

```bash
bash scripts/test-example-project.sh
```

## What gets installed

- `--minimal`: базовые схемы, task/report шаблоны и две проверки
- `--full`: весь текущий набор guardrails и вспомогательных файлов

## What is not included

- backend, RAG, vector DB, agent orchestration
- Docker image, pip package, npm package
## Safety Boundaries

- Validation result PASS does not mean AgentOS is MVP-ready.
- NOT_RUN is not PASS. A check that was not run provides no evidence.
- AgentOS is not a backend, not a RAG system, not a vector database.
- AgentOS is not autonomous. Human review is required for all execution decisions.
- M21 quickstart completion does not override M19/M20 safety gates.
