---
name: onboard-repo
description: "Prepares an existing repository for humans and coding agents end to end: setup discovery, AGENTS.md and CLAUDE.md alignment, human development flow, coding conventions, and worktree-first, low-churn commit guidance. Orchestrates swe:project-dev-setup and swe:onboard-agentic-dev-flow. Use when onboarding a repo or project for agentic development with Claude Code, Codex, Cursor, or other coding agents."
---

# Onboard Repo

Version: 1.2.0

Prepare a repository so humans and coding agents share one explicit development
workflow without duplicating or diluting the repo's existing conventions.

## Workflow

1. Inspect the repo with `swe:project-dev-setup`.
   - Read existing `AGENTS.md`, `CLAUDE.md`, `README.md`, contribution docs,
     docs indexes, package manifests, and lint or formatter configs.
   - Search for existing coding rules before writing new ones.
   - Treat local uncommitted changes as user-owned.

2. Check whether a wrapper is better than a new skill.
   - Use `swe:third-party-skill-reference` when adding or adapting skill
     behavior from another source.

3. Align agent and human docs with `swe:onboard-agentic-dev-flow`.
   - Keep one source of truth for agent instructions.
   - Use `CLAUDE.md` and `AGENTS.md` as compatibility bridges when appropriate.
   - Document worktree isolation and a low-churn commit cadence that treats
     commits as explicit delivery boundaries rather than per-step checkpoints.
   - Add a minimal human development flow only where the repo naturally keeps
     human-facing setup and workflow docs.

4. Validate the result.
   - Confirm all bridge references point to existing files.
   - Confirm any project-local worktree directory is ignored before
     recommending it.
   - Run lightweight markdown or diff checks when available.
   - Work through [references/onboarding-checklist.md](references/onboarding-checklist.md)
     before reporting completion.

## Safety Checks

- Keep meaningful repo-specific rules; generic defaults fill gaps only.
- Update an existing development guide in place rather than creating a
  duplicate doc.
- Check license and attribution requirements before adding third-party skill
  text, code, assets, or templates.
- Use only setup, run, and verification commands the repo actually defines;
  mark missing ones as not documented instead of inventing them.

## Completion Report

Report the instruction source of truth, files changed, captured conventions,
documented setup and verification commands, worktree readiness, commit cadence,
and any missing repo guidance that remains.
