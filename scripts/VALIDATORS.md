# Validators

Canonical checks used by `scripts/run-all.sh`.

| Script | Role |
|---|---|
| `health-check.sh` | Overall canonical health check |
| `validate-architecture.sh` | Runs document, route, and link validation |
| `validate-route.py` | Confirms startup and registry routes use only canonical modules |
| `validate-docs.py` | Confirms required canonical module metadata |
| `check-links.py` | Confirms selected runtime links resolve |
| `check-llms-graph-files.sh` | Confirms module paths named in `llms.txt` exist |
