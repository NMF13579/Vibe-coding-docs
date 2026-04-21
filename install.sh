#!/usr/bin/env bash
# AgentOS — установка в текущую папку проекта.
# Источник: https://github.com/NMF13579/AgentOS

set -euo pipefail

readonly REPO_URL="https://github.com/NMF13579/AgentOS.git"
readonly TMP_ROOT="/tmp/agentos-install"

# ANSI colors
readonly C_GREEN='\033[0;32m'
readonly C_YELLOW='\033[1;33m'
readonly C_RED='\033[0;31m'
readonly C_RESET='\033[0m'

err() {
  printf '%b%s%b\n' "$C_RED" "$*" "$C_RESET" >&2
}

info_green() {
  printf '%b%s%b\n' "$C_GREEN" "$*" "$C_RESET"
}

ask_yellow() {
  # В stderr, чтобы не попадало в $(...) при чтении ответов
  printf '%b%s%b' "$C_YELLOW" "$*" "$C_RESET" >&2
}

# При запуске через curl | bash stdin — это поток скрипта; вопросы читаем с терминала.
read_reply() {
  local _var="$1"
  if [[ -t 0 ]]; then
    read -r "$_var"
  elif exec 3</dev/tty 2>/dev/null; then
    read -r "$_var" <&3
    exec 3<&-
  else
    read -r "$_var"
  fi
}

require_git() {
  if ! command -v git >/dev/null 2>&1; then
    err "Ошибка: не найден git. Установите git и запустите скрипт снова."
    exit 1
  fi
}

normalize_yes_no() {
  local a
  a=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
  case "$a" in
    да|д|yes|y) echo "yes" ;;
    нет|н|no|n) echo "no" ;;
    *) echo "" ;;
  esac
}

ask_level() {
  local ans=""
  while true; do
    ask_yellow "Уровень установки: 0 — минимум (только LAYER-1), 1 — стандарт (+ LAYER-2), 2 — полный (всё). Введите 0, 1 или 2: "
    read_reply ans
    case "$ans" in
      0|1|2) echo "$ans"; return 0 ;;
      *) err "Нужно ввести 0, 1 или 2." ;;
    esac
  done
}

ask_medical() {
  local ans="" n
  while true; do
    ask_yellow "Медицинский проект? (да/нет): "
    read_reply ans
    n=$(normalize_yes_no "$ans")
    if [[ "$n" == "yes" || "$n" == "no" ]]; then
      echo "$n"
      return 0
    fi
    err "Ответьте «да» или «нет»."
  done
}

ask_project_name() {
  local name
  while true; do
    ask_yellow "Имя проекта (для HANDOFF.md, поле Project Name): "
    read_reply name
    name=$(printf '%s' "$name" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    if [[ -n "$name" ]]; then
      printf '%s' "$name"
      return 0
    fi
    err "Имя проекта не может быть пустым."
  done
}

confirm_overwrite() {
  local path="$1"
  local ans="" n
  while true; do
    ask_yellow "Файл ${path} уже существует. Перезаписать? (да/нет): "
    read_reply ans
    n=$(normalize_yes_no "$ans")
    if [[ "$n" == "yes" ]]; then
      return 0
    elif [[ "$n" == "no" ]]; then
      return 1
    fi
    err "Ответьте «да» или «нет»."
  done
}

# Copy one file from source repo to DEST; tracks COPIED_LIST, respects overwrite policy.
copy_one() {
  local src="$1"
  local rel="$2"
  local dest="${DEST}/${rel}"

  [[ -f "$src" ]] || return 0

  mkdir -p "$(dirname "$dest")"

  if [[ -e "$dest" ]]; then
    if ! confirm_overwrite "$rel"; then
      return 0
    fi
  fi

  cp -f "$src" "$dest"
  COPIED_LIST+=("$rel")
  if [[ "$rel" == "HANDOFF.md" ]]; then
    HANDOFF_WAS_COPIED=1
  fi
}

copy_dir_tree() {
  local src_root="$1"

  [[ -d "$src_root" ]] || return 0

  local f rel
  while IFS= read -r -d '' f; do
    rel="${f#"$SRC"/}"
    copy_one "$f" "$rel"
  done < <(find "$src_root" -type f -print0 2>/dev/null || true)
}

inject_handoff_project_name() {
  local file="$DEST/HANDOFF.md"
  local name="$1"
  local tmp

  [[ -f "$file" ]] || return 0

  if grep -qFx '<!--VIBE_DOCS_PROJECT_NAME-->' "$file" 2>/dev/null; then
    tmp=$(mktemp)
    awk -v pname="$name" '{ if ($0 == "<!--VIBE_DOCS_PROJECT_NAME-->") print pname; else print }' "$file" > "$tmp" && mv "$tmp" "$file"
    return 0
  fi

  if grep -q '^## Project Name$' "$file" 2>/dev/null; then
    return 0
  fi

  tmp=$(mktemp)
  {
    head -n 1 "$file"
    echo ""
    echo "## Project Name"
    echo ""
    printf '%s\n' "$name"
    echo ""
    tail -n +2 "$file"
  } > "$tmp" && mv "$tmp" "$file"
}

# --- main ---

printf '%b%s%b\n' "$C_GREEN" "Добро пожаловать в установщик AgentOS." "$C_RESET"
printf '%s\n' "Файлы будут скопированы в: $(pwd)"
echo ""

require_git

LEVEL=$(ask_level)
MEDICAL=$(ask_medical)
PROJECT_NAME=$(ask_project_name)

echo ""
require_git

if [[ -d "$TMP_ROOT" ]]; then
  rm -rf "$TMP_ROOT"
fi

info_green "Клонирование репозитория во временную папку..."
if ! git clone --depth 1 "$REPO_URL" "$TMP_ROOT" >/dev/null 2>&1; then
  err "Не удалось клонировать репозиторий. Проверьте сеть и доступ к GitHub."
  exit 1
fi

SRC="$TMP_ROOT"
DEST="$(pwd)"
COPIED_LIST=()
HANDOFF_WAS_COPIED=0

require_git

info_green "Копирование файлов..."

# Уровень 0
copy_dir_tree "$SRC/LAYER-1"
copy_one "$SRC/CLAUDE.md" "CLAUDE.md"
copy_one "$SRC/HANDOFF.md" "HANDOFF.md"
copy_one "$SRC/CHECKLIST.md" "CHECKLIST.md"

# Уровень 1
if [[ "$LEVEL" == "1" || "$LEVEL" == "2" ]]; then
  copy_dir_tree "$SRC/LAYER-2"
  copy_one "$SRC/QUICK-START.md" "QUICK-START.md"
fi

# Уровень 2
if [[ "$LEVEL" == "2" ]]; then
  copy_dir_tree "$SRC/LAYER-3"
  copy_dir_tree "$SRC/stages"
  copy_dir_tree "$SRC/tasks"
  copy_dir_tree "$SRC/shared"
fi

# Медицинский UX (явно; при уровне 0 уже внутри LAYER-1 в ux-checklist-core.md)
if [[ "$MEDICAL" == "yes" ]]; then
  printf '%b%s%b\n' "$C_YELLOW" "Медицинский проект: обновляю LAYER-1/ux-checklist-core.md (раздел MEDICAL) …" "$C_RESET"
  copy_one "$SRC/LAYER-1/ux-checklist-core.md" "LAYER-1/ux-checklist-core.md"
fi

if [[ "$HANDOFF_WAS_COPIED" -eq 1 ]]; then
  inject_handoff_project_name "$PROJECT_NAME"
fi

require_git

rm -rf "$TMP_ROOT"

N=${#COPIED_LIST[@]}
echo ""
info_green "✅ AgentOS установлен"
printf '%s\n' "📁 Скопировано файлов: ${N}"
info_green "👉 Следующий шаг: открой START.md (онбординг) или llms.txt (каноничный порядок для агента в этом репозитории)"
echo ""
printf '%b%s%b\n' "$C_GREEN" "Список скопированных файлов:" "$C_RESET"
if [[ "$N" -eq 0 ]]; then
  printf '%s\n' "(ничего нового — все пути уже существовали и перезапись отклонена)"
else
  printf '%s\n' "${COPIED_LIST[@]}"
fi
