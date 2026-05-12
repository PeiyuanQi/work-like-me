# work-like-me

Shared Cursor rules, Claude Code plugins, and Codex-compatible skills that encode how you work — install them into your user profile or individual projects so every AI assistant follows the same conventions.

## Quick Start

### Install to Claude Code Marketplace

1. **Push this repo to GitHub** (public or private)

2. **In Claude Code, use:**
   ```
   /plugin marketplace add https://github.com/PeiyuanQi/work-like-me.git
   ```

Or manually install via installer:
```bash
chmod +x install.sh && ./install.sh
```

### Install Skills to Codex

```bash
./install.sh --codex
```

This copies every `SKILL.md` folder from `wlm/plugins/*/skills/` into `${CODEX_HOME:-~/.codex}/skills`.

To install to a custom Codex skills directory:

```bash
./install.sh --codex-to /absolute/path/to/skills
```

### Install into a Project

```bash
./install.sh --rules-to /path/to/project      # Cursor rules
./install.sh --plugin-to /path/to/project     # Claude skills
./install.sh --rules-to /path/to/project --plugin-to /path/to/project  # Both
```

---

## What's Included

### Cursor Rules (`.cursor/rules/`)

| Rule | Description |
|------|-------------|
| `node-nvm-24.mdc` | Use Node 24 via nvm before npm/yarn/pnpm |
| `python-use-uv.mdc` | Use uv instead of raw pip/python |
| `flutter-use-fvm.mdc` | Use fvm flutter / fvm dart |

### Claude Code Plugins And Codex Skills (`wlm/plugins/`)

**SWE Plugin** — Software Engineer skills for git workflows, code review, and merge requests

**Worker Plugin** — Daily worker skills for general productivity, memory, and team collaboration

---

## Requirements

- Bash
- `rsync` (preferred) — falls back to `cp` if unavailable
- `uv` for Python virtual environment management

## Virtual Environments

```bash
cd wlm
uv sync        # Install dependencies
source .venv/bin/activate  # Activate environment
```

## Help

```bash
./install.sh --help
```

## License

Use and adapt as you like.
