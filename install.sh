#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$(pwd)"
MINIMAL_DIR="$SCRIPT_DIR/templates/agentos-minimal"
FULL_DIR="$SCRIPT_DIR/templates/agentos-full"

show_help() {
  echo "Usage: bash install.sh [--minimal|--full] [--dry-run] [--force]"
}

MODE="minimal"
DRY_RUN=0
FORCE=0
MODE_SET=0

for arg in "$@"; do
  case "$arg" in
    --minimal)
      if [ "$MODE_SET" -eq 1 ] && [ "$MODE" != "minimal" ]; then
        echo "FAIL: choose only one of --minimal or --full"
        exit 1
      fi
      MODE="minimal"
      MODE_SET=1
      ;;
    --full)
      if [ "$MODE_SET" -eq 1 ] && [ "$MODE" != "full" ]; then
        echo "FAIL: choose only one of --minimal or --full"
        exit 1
      fi
      MODE="full"
      MODE_SET=1
      ;;
    --dry-run)
      DRY_RUN=1
      ;;
    --force)
      FORCE=1
      ;;
    --help)
      show_help
      exit 0
      ;;
    *)
      echo "FAIL: unknown argument: $arg"
      exit 1
      ;;
  esac
done

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "FAIL: install.sh must be run from a git repository root"
  exit 1
fi

if [ "$MODE" = "minimal" ]; then
  TEMPLATE_ROOT="$MINIMAL_DIR"
else
  TEMPLATE_ROOT="$FULL_DIR"
fi

if [ ! -d "$TEMPLATE_ROOT" ]; then
  echo "FAIL: template not found: $TEMPLATE_ROOT"
  exit 1
fi

while IFS= read -r source_file; do
  relative_path="${source_file#$TEMPLATE_ROOT/}"
  target_path="$TARGET_DIR/$relative_path"
  target_dir="$(dirname "$target_path")"

  if [ -e "$target_path" ] && [ "$FORCE" -ne 1 ]; then
    echo "SKIP: $relative_path already exists"
    continue
  fi

  if [ "$FORCE" -eq 1 ] && [ -e "$target_path" ]; then
    echo "OVERWRITE: $relative_path"
  else
    echo "INSTALL: $relative_path"
  fi

  if [ "$DRY_RUN" -ne 1 ]; then
    mkdir -p "$target_dir"
    cp "$source_file" "$target_path"
  fi
done < <(find "$TEMPLATE_ROOT" -type f | sort)

if [ "$DRY_RUN" -eq 1 ]; then
  echo "PASS: dry run completed"
else
  echo "PASS: AgentOS template installed"
fi
