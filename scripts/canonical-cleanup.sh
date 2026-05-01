#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="dry-run"
CREATE_BACKUP_BRANCH=0
BACKUP_BRANCH_NAME=""

CANONICAL_REQUIRED=(
  "llms.txt"
  "ROUTES-REGISTRY.md"
  "START.md"
  "AGENTS.md"
  "CLAUDE.md"
  "SYSTEM_PROMPT.md"
  "CHECKLIST.md"
  "core-rules/MAIN.md"
  "state/MAIN.md"
  "workflow/MAIN.md"
  "quality/MAIN.md"
  "security/MAIN.md"
  "scripts/run-all.sh"
  "tools/doc-tests/run-doc-tests.js"
)

DELETE_TARGETS=(
  "LAYER-1"
  "LAYER-2"
  "LAYER-3"
  "LAYER-archive"
  "medical"
  "doctor"
  "adapters"
  "incidents"
  ".claude"
  ".cursor"
  ".aider.conf.yml"
  ".rules"
  ".windsurfrules"
  "ADVANCED-SETUP.md"
  "CHANGELOG.md"
  "CLAUDE-CODE-FLOW.md"
  "DOMAIN-ADAPTER.md"
  "GLOSSARY.md"
  "LEARNING-LOOP.md"
  "ONBOARDING-WIZARD.md"
  "QUICK-START.md"
  "QUICK-START-NOVICE.md"
  "README-INSTALL.md"
  "install.sh"
  "project/archive"
  "stages"
  "tasks"
  "scripts/ADAPTER-SPEC.md"
  "scripts/fix-adapters.sh"
  "scripts/legacy-health-check.sh"
  "scripts/validate-adapters.sh"
)

SEARCH_TARGETS=(
  "llms.txt"
  "ROUTES-REGISTRY.md"
  "START.md"
  "AGENTS.md"
  "CLAUDE.md"
  "SYSTEM_PROMPT.md"
  "CHECKLIST.md"
  "core-rules"
  "state"
  "workflow"
  "quality"
  "security"
  "scripts"
  "tools/doc-tests"
  ".github/workflows"
)

usage() {
  cat <<'EOF'
Usage:
  bash scripts/canonical-cleanup.sh [--apply] [--backup-branch NAME]

Modes:
  default           Safe preview only. Nothing is deleted.
  --apply           Execute cleanup and run verification.
  --backup-branch   Create a local backup git branch before deletion.

Examples:
  bash scripts/canonical-cleanup.sh
  bash scripts/canonical-cleanup.sh --apply
  bash scripts/canonical-cleanup.sh --apply --backup-branch backup/legacy-before-cleanup
EOF
}

log() {
  printf '%s\n' "$1"
}

warn() {
  printf 'WARNING: %s\n' "$1"
}

die() {
  printf 'ERROR: %s\n' "$1" >&2
  exit 1
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --apply)
        MODE="apply"
        shift
        ;;
      --backup-branch)
        [[ $# -ge 2 ]] || die "--backup-branch requires a branch name"
        CREATE_BACKUP_BRANCH=1
        BACKUP_BRANCH_NAME="$2"
        shift 2
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        die "unknown argument: $1"
        ;;
    esac
  done
}

ensure_repo_root() {
  [[ -d "$REPO_ROOT/.git" ]] || die "script must run inside the repository root"
  cd "$REPO_ROOT"
}

check_canonical_files() {
  local missing=0
  log "== Canonical file check =="
  for path in "${CANONICAL_REQUIRED[@]}"; do
    if [[ -e "$path" ]]; then
      log "OK  $path"
    else
      warn "missing canonical file: $path"
      missing=1
    fi
  done
  echo
  return "$missing"
}

create_backup_branch() {
  [[ $CREATE_BACKUP_BRANCH -eq 1 ]] || return 0
  [[ -n "$BACKUP_BRANCH_NAME" ]] || die "backup branch name is empty"
  git rev-parse --verify HEAD >/dev/null 2>&1 || die "cannot create backup branch before first commit"
  if git rev-parse --verify "$BACKUP_BRANCH_NAME" >/dev/null 2>&1; then
    warn "backup branch already exists: $BACKUP_BRANCH_NAME"
    return 0
  fi
  log "Creating backup branch: $BACKUP_BRANCH_NAME"
  git branch "$BACKUP_BRANCH_NAME"
  echo
}

cleanup_targets() {
  local removed=0
  local absent=0
  log "== Cleanup targets =="
  for path in "${DELETE_TARGETS[@]}"; do
    if [[ -e "$path" ]]; then
      if [[ "$MODE" == "apply" ]]; then
        rm -rf "$path"
        log "REMOVED  $path"
      else
        log "WOULD REMOVE  $path"
      fi
      removed=$((removed + 1))
    else
      log "SKIP  $path (not present)"
      absent=$((absent + 1))
    fi
  done
  echo
  log "Targets present: $removed"
  log "Targets already absent: $absent"
  echo
}

run_verification() {
  log "== Verification =="

  log "Running doc-tests"
  node tools/doc-tests/run-doc-tests.js
  echo

  log "Running canonical validators"
  bash scripts/run-all.sh
  echo

  log "Checking canonical files for forbidden words"
  if rg -n "LAYER|legacy" "${SEARCH_TARGETS[@]}"; then
    die "found forbidden references in canonical files"
  else
    log "OK  no LAYER/legacy references found in canonical files"
  fi
  echo
}

print_report() {
  log "== Report =="
  log "Mode: $MODE"
  if [[ $CREATE_BACKUP_BRANCH -eq 1 ]]; then
    log "Backup branch: $BACKUP_BRANCH_NAME"
  else
    log "Backup branch: not requested"
  fi
  log "Repository: $REPO_ROOT"
  echo
  log "Git status summary:"
  git status --short
  echo
}

main() {
  parse_args "$@"
  ensure_repo_root

  if ! check_canonical_files; then
    warn "one or more canonical files are missing; cleanup was not started"
    exit 1
  fi

  if [[ "$MODE" == "dry-run" ]]; then
    log "Dry run only. No files will be deleted."
    echo
    cleanup_targets
    print_report
    exit 0
  fi

  create_backup_branch
  cleanup_targets
  run_verification
  print_report
}

main "$@"
