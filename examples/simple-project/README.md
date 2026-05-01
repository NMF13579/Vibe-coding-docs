# AgentOS Simple Project Example

## What this is

This is a minimal example project for installing and validating AgentOS guardrails.

## Run the app

```bash
bash run-example.sh
```

## Install AgentOS minimal template

```bash
cd examples/simple-project
git init
bash ../../install.sh --minimal
```

## Validate AgentOS

```bash
python3 -m pip install -r requirements.txt
bash scripts/run-all.sh
```

## Full example validation

```bash
bash scripts/test-example-project.sh
```
