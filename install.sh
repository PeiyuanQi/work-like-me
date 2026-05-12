#!/usr/bin/env bash
#
# install.sh — Install work-like-me config into your user profile or a project.
#
# Usage:
#   ./install.sh                              # install Cursor rules to ~/.cursor
#   ./install.sh --rules-to /path/to/project  # copy rules into a project
#   ./install.sh --plugin-to /path/to/project # copy wlm plugin into a project
#   ./install.sh --codex                      # copy skills to ${CODEX_HOME:-~/.codex}/skills
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURSOR_SRC="${SCRIPT_DIR}/.cursor"
WLM_SRC="${SCRIPT_DIR}/wlm"
CURSOR_HOME="${HOME}/.cursor"
RULES_TO=""
PLUGIN_TO=""
CODEX_TO=""
INSTALL_CODEX=0

confirm_create_dir() {
  local dir="$1"
  if [[ -d "$dir" ]]; then
    return 0
  fi
  echo "Directory does not exist: $dir"
  read -r -p "Create it? [y/N] " reply
  if [[ "$reply" =~ ^[yY]$ ]]; then
    mkdir -p "$dir"
    return 0
  fi
  return 1
}

sync_dir() {
  local src="$1" dst="$2"
  rsync -a --ignore-existing "${src}/" "${dst}/" 2>/dev/null || {
    cp -Rn "${src}"/* "${dst}/" 2>/dev/null || true
  }
}

install_codex_skills() {
  local dst="$1"
  local skill_count=0

  if [[ ! -d "${WLM_SRC}/plugins" ]]; then
    echo "Warning: No wlm/plugins directory in repo, skipping Codex skills." >&2
    return 0
  fi

  echo "Copying skills to Codex skills directory ${dst} ..."
  if ! confirm_create_dir "$dst"; then
    echo "  Skipped (directory not created)."
    return 0
  fi

  while IFS= read -r skill_md; do
    local skill_dir
    local skill_name
    skill_dir="$(dirname "$skill_md")"
    skill_name="$(basename "$skill_dir")"
    mkdir -p "${dst}/${skill_name}"
    sync_dir "$skill_dir" "${dst}/${skill_name}"
    echo "  installed ${skill_name}"
    skill_count=$((skill_count + 1))
  done < <(find "${WLM_SRC}/plugins" -path '*/skills/*/SKILL.md' -print | sort)

  if [[ "$skill_count" -eq 0 ]]; then
    echo "Warning: No skill files found under wlm/plugins/*/skills." >&2
  else
    echo "  done (${skill_count} skills)."
  fi
}

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --rules-to)
      if [[ -z "${2:-}" ]]; then
        echo "Error: --rules-to requires a path argument." >&2
        exit 1
      fi
      RULES_TO="$2"
      shift 2
      ;;
    --plugin-to)
      if [[ -z "${2:-}" ]]; then
        echo "Error: --plugin-to requires a path argument." >&2
        exit 1
      fi
      PLUGIN_TO="$2"
      shift 2
      ;;
    --codex)
      INSTALL_CODEX=1
      CODEX_TO="${CODEX_HOME:-${HOME}/.codex}/skills"
      shift
      ;;
    --codex-to)
      if [[ -z "${2:-}" ]]; then
        echo "Error: --codex-to requires a path argument." >&2
        exit 1
      fi
      INSTALL_CODEX=1
      CODEX_TO="$2"
      shift 2
      ;;
    -h|--help)
      cat <<'HELP'
Usage: install.sh [OPTIONS]

Options:
  (no args)              Copy .cursor rules to user profile (~/.cursor).
  --rules-to PATH        Copy .cursor/rules into the project at PATH.
  --plugin-to PATH       Copy wlm/ plugin package into the project at PATH.
  --codex                Copy all wlm plugin skills to ${CODEX_HOME:-~/.codex}/skills.
  --codex-to PATH        Copy all wlm plugin skills to a specific Codex skills directory.
  -h, --help             Show this help.

PATH must be an absolute system path.

Examples:
  ./install.sh
  ./install.sh --rules-to /Users/me/projects/my-app
  ./install.sh --plugin-to /Users/me/projects/my-app
  ./install.sh --codex
  ./install.sh --codex-to /Users/me/.codex/skills
  ./install.sh --rules-to /Users/me/projects/my-app --plugin-to /Users/me/projects/my-app
HELP
      exit 0
      ;;
    *)
      echo "Error: Unknown option: $1" >&2
      echo "Use --help for usage." >&2
      exit 1
      ;;
  esac
done

# ---------------------------------------------------------------------------
# Validate paths are absolute
# ---------------------------------------------------------------------------
for path_var in RULES_TO PLUGIN_TO CODEX_TO; do
  val="${!path_var}"
  if [[ -n "$val" && "$val" != /* ]]; then
    echo "Error: --${path_var,,} path must be absolute. Got: $val" >&2
    exit 1
  fi
done

# ---------------------------------------------------------------------------
# Default: install Cursor rules to user profile
# ---------------------------------------------------------------------------
if [[ -z "$RULES_TO" && -z "$PLUGIN_TO" && "$INSTALL_CODEX" -eq 0 ]]; then
  if [[ ! -d "$CURSOR_SRC" ]]; then
    echo "Warning: No .cursor directory in repo, nothing to install." >&2
    exit 0
  fi
  echo "Installing .cursor rules to ${CURSOR_HOME} ..."
  if confirm_create_dir "$CURSOR_HOME"; then
    sync_dir "$CURSOR_SRC" "$CURSOR_HOME"
    echo "  done."
  else
    echo "  Skipped (directory not created)."
  fi
fi

# ---------------------------------------------------------------------------
# --rules-to: copy .cursor/rules into a project
# ---------------------------------------------------------------------------
if [[ -n "$RULES_TO" ]]; then
  if [[ ! -d "${CURSOR_SRC}/rules" ]]; then
    echo "Warning: No .cursor/rules in repo, skipping rules." >&2
  else
    echo "Copying Cursor rules to ${RULES_TO} ..."
    if confirm_create_dir "${RULES_TO}/.cursor/rules"; then
      sync_dir "${CURSOR_SRC}/rules" "${RULES_TO}/.cursor/rules"
      echo "  done."
    else
      echo "  Skipped (directory not created)."
    fi
  fi
fi

# ---------------------------------------------------------------------------
# --plugin-to: copy wlm/ plugin package into a project
# ---------------------------------------------------------------------------
if [[ -n "$PLUGIN_TO" ]]; then
  if [[ ! -d "$WLM_SRC" ]]; then
    echo "Warning: No wlm/ directory in repo, skipping plugin." >&2
  else
    echo "Copying wlm plugin to ${PLUGIN_TO} ..."
    if confirm_create_dir "${PLUGIN_TO}/wlm"; then
      sync_dir "$WLM_SRC" "${PLUGIN_TO}/wlm"
      echo "  done."
    else
      echo "  Skipped (directory not created)."
    fi
  fi
fi

# ---------------------------------------------------------------------------
# --codex / --codex-to: copy plugin skills into Codex skill directory
# ---------------------------------------------------------------------------
if [[ "$INSTALL_CODEX" -eq 1 ]]; then
  install_codex_skills "$CODEX_TO"
fi

echo "Install complete."
