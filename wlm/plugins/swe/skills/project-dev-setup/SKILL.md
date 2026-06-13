---
name: project-dev-setup
description: Set up any repository for local development and docs-first feature work. Use when onboarding to a project, starting a local dev session, checking repo-specific workflow conventions, or preparing to work through a feature queue. For end-to-end new work, prefer swe:start-work; for agentic repo onboarding, prefer swe:onboard-repo.
---

# Project Dev Setup

Version: 1.2.0

Keep the repository ready for local development and feature delivery.

## Workflow

1. Read the repo's own guidance first. Look for `CLAUDE.md`, `AGENTS.md`, `README.md`, and any docs index or workflow files.
2. Find the repo's source of truth for pending work if it has one. Follow the local convention already defined by the repo.
3. Keep docs aligned with code whenever behavior changes.
4. Identify env files, dev scripts, and dependency setup from the repo's own docs and scripts.
5. Install Git LFS locally before handling large binaries if the repo uses it.
6. Ask to use a git worktree for new work so multiple agents can develop in parallel without colliding.
7. Before creating a new skill or workflow, check whether a third-party skill can be referenced or wrapped. Use `third-party-skill-reference` for that decision.
8. Start local dev in the foreground and prefer a single-command launcher if the repo provides one.
9. For frontend work, verify light and dark themes, responsive breakpoints, accessibility, i18n fit, and icon conventions used by the repo.
10. Before adding third-party code, assets, fonts, icons, tooling, or vendored skill content, check license compatibility with the repo's chosen license and record notices if needed.
11. When merging or refreshing a branch, use the repo's required merge strategy. If conflicts appear, prefer rebase-based resolution that preserves the original intent, then fetch latest main and clean up.

## What To Look For

- Repo-local docs that define process and conventions
- Dev environment files such as `.env.example`
- Local dev scripts or package scripts
- Docs-driven feature queues or implementation notes
- License files and third-party notices
- Existing third-party skills that could be referenced instead of reimplemented
- Any frontend-specific design rules already established by the repo

## Notes

- Keep the skill generic and adapt to the repository's own conventions.
- Do not assume every repo uses the same file names or workflow shape.
- Treat repo-local docs as the source of truth when they exist.
