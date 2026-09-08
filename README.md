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

This copies every `SKILL.md` folder from `wlm/plugins/*/skills/` into
`~/.agents/skills`, the user-level Codex skills directory. Existing skill files
are updated in place; files that exist only in the destination are preserved.

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

**SWE Plugin** — Software Engineer workflow skills for starting, finishing,
submitting, and onboarding code work, plus technical writing, security/privacy
audits, dependency vulnerability remediation, open-source readiness, verified
website publishing, git, review, environment setup, third-party skill
references, and software decision ranking

**CPA Plugin** — Tax intake, tax research, filing preparation, personal finance decision ranking, and future CPA workflow skills

**Worker Plugin** — Daily office worker skills for productivity, memory, team collaboration, office decision ranking, and presentation workflows, including PPT style selection and the Guizang PPT style wrapper

**Mechanical Plugin** — Hands-on mechanical, physical build, repair, regulated-device, tooling, material, and maker decision ranking

**MLE Plugin** — Machine learning engineering workflows for reliable,
observable, and scale-aware training systems, including distributed-training
stability and straggler diagnosis

**Art Design Plugin** — Art direction and visual design skills for generated
images, website assets, game assets, hero art, and theme-specific workflows for
fan art, studies, vehicles, architecture, props, creatures, sci-fi, fantasy,
environments, characters, worldbuilding, 3D, UI, illustration, and mixed media

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

## Development Flow

- Read `AGENTS.md` before using an agent on this repository.
- Use `$start-work` and a local git worktree for parallel or unrelated work.
- Keep task branches local by default; this solo-maintained repository does not
  require a remote feature branch or pull request for normal delivery.
- At an explicit delivery boundary, use `$land-work` to verify and commit the
  task, rebase it onto the latest `main` when needed, fast-forward it into the
  clean local `main`, and push `main` directly.
- Include cleanup explicitly when desired; `$land-work` then calls
  `$cleanup-work` only after the landed commit is verified on remote `main` and
  only from outside the completed task worktree.
- Serialize `main` integration across parallel worktrees. Do not create merge
  commits or force-push `main`.
- Use `$submit-work` only when a pull request or human review is requested or
  required by repository protection.
- Run `./install.sh --help` as the lightweight repository smoke check.

## Help

```bash
./install.sh --help
```

## License

This project is licensed under the GNU General Public License v3.0 or later
(`GPL-3.0-or-later`) to preserve copyleft/open-source terms for redistributed
versions and derivative works. See `LICENSE`. Third-party attributions and
license terms are recorded in `THIRD_PARTY_NOTICES.md`.
