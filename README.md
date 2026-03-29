# work-like-me

Shared Cursor rules, Claude skills, and Claude plugins that encode how you work — install them into your user profile or individual projects so every AI assistant follows the same conventions.

## Quick Start

### Install to Claude Code Marketplace

1. **Push this repo to GitHub** (public or private)

2. **In Claude Code, use:**
   ```
   /marketplace add https://github.com/PeiyuanQi/work-like-me
   ```

Or manually install via installer:
```bash
chmod +x install.sh && ./install.sh
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

### Claude Plugins (`wlm/plugins/`)

**SWE Plugin** — Software Engineer skills for git workflows, code review, and merge requests

**Worker Plugin** — Daily worker skills for general productivity, memory, and team collaboration

---

## Requirements

- Bash
- `rsync` (preferred) — falls back to `cp` if unavailable
- `uv` for Python virtual environment management

### Setup

```bash
cd wlm
uv sync  # Create and activate virtual environment
```

## Virtual Environments

This project uses `uv` for Python virtual environments in the `wlm/` directory:

```bash
cd wlm
source .venv/bin/activate
uv sync
```

## Help

```bash
./install.sh --help
```

## License

Use and adapt as you like.
