---
name: onboard-repo
description: "Use when preparing an existing repository for agentic software development: creating or aligning AGENTS.md and CLAUDE.md, documenting human development flow, capturing coding conventions, adding worktree-first guidance, checking setup commands, or onboarding a project for Claude Code, Codex, Cursor, or other coding agents. Orchestrates project-dev-setup and onboard-agentic-dev-flow."
---

# Onboard Repo

Version: 1.0.0

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
   - Add a minimal human development flow only where the repo naturally keeps
     human-facing setup and workflow docs.

4. Validate the result.
   - Confirm all bridge references point to existing files.
   - Confirm any project-local worktree directory is ignored before recommending
     it.
   - Run lightweight markdown or diff checks when available.
   - Read `references/onboarding-checklist.md` before reporting completion.

## Safety Checks

- Do not replace meaningful repo-specific rules with generic defaults.
- Do not create duplicate docs when an existing development guide should be
  updated in place.
- Do not add third-party skill text, code, assets, or templates without checking
  license and attribution requirements.
- Do not invent setup, run, or verification commands when the repo does not
  define them.

## Completion Report

Report the instruction source of truth, files changed, captured conventions,
documented setup and verification commands, worktree readiness, and any missing
repo guidance that remains.
