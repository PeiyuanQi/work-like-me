---
name: onboard-agentic-dev-flow
description: Use when onboarding an existing project or repo to agentic development flow, including creating or aligning AGENTS.md and CLAUDE.md, adding or aligning minimal human development-flow documentation, preferring git worktrees for concurrent agents, and distilling existing coding rules, 规则, 习惯, style, and workflow conventions into agent instructions.
---

# Onboard Agentic Dev Flow

Version: 1.0.0

Prepare a project so humans and agents share a small, explicit development
workflow. Preserve the repo's existing habits first; only add generic defaults
where the project is silent.

## Workflow

1. Inspect before writing.
   - Read existing `AGENTS.md`, `CLAUDE.md`, `README.md`, docs indexes, feature
     docs, `.cursor/rules/`, `.github/`, `Makefile`, package manifests, and
     lint or formatter configs.
   - Search for `coding rules`, `conventions`, `style`, `workflow`, `lint`,
     `format`, `规则`, `规范`, and `习惯`.
   - Check git status and treat existing uncommitted changes as user-owned.

2. Decide the instruction source of truth.
   - For a fresh onboarding, put shared agent instructions in `AGENTS.md`.
   - Keep `CLAUDE.md` as a minimal compatibility bridge to `AGENTS.md`, unless
     the repo already has a richer `CLAUDE.md` that should remain canonical.
   - If `CLAUDE.md` remains canonical, make `AGENTS.md` point to it and avoid
     duplicating long rules in both files.

3. Create or update `AGENTS.md`.
   - Include only durable repo guidance: project context, source-of-truth docs,
     git workflow, coding rules, test commands, documentation expectations, and
     review bar.
   - Distill existing coding rules and habits into explicit bullets. Prefer
     observed repo facts over broad defaults.
   - Add a worktree-first git rule:
     `Prefer git worktrees for parallel or unrelated agent work so multiple
     agents can develop concurrently without colliding.`
   - Keep the file short enough that future agents will actually read it.

4. Link `CLAUDE.md`.
   - If `AGENTS.md` is canonical, make `CLAUDE.md` a tiny bridge such as:
     ```md
     AGENTS.md
     ```
   - If `CLAUDE.md` is canonical, make `AGENTS.md` a tiny bridge such as:
     ```md
     CLAUDE.md
     ```
   - When both files already exist, preserve meaningful project-specific rules
     and only normalize the bridge if it reduces duplication.

5. Add or align a minimal human development flow.
   - First find where the repo already guides human dev flow. Check likely
     places such as `README.md`, `docs/README.md`, `docs/development.md`,
     `docs/contributing.md`, `CONTRIBUTING.md`, `DEVELOPMENT.md`,
     `.github/CONTRIBUTING.md`, and feature/spec docs indexes.
   - If a human dev-flow guide already exists, update that file in place with
     the minimal missing agentic flow notes instead of creating a duplicate
     section elsewhere.
   - If only `README.md` exists, add a concise `Development Flow` section
     instead of rewriting the whole file.
   - If no suitable human-facing guide exists, create a minimal `README.md`
     with setup, local run, test, worktree workflow, and where to read agent
     instructions.
   - Use actual commands discovered from the repo. If a command is unknown, say
     that the repo does not define it yet instead of inventing one.

6. Validate the onboarding.
   - Confirm `AGENTS.md`, `CLAUDE.md`, and the chosen human dev-flow guide
     exist.
   - Confirm links or bridge references point to existing files.
   - If recommending a project-local worktree directory such as `.worktrees/`,
     ensure it is ignored before agents use it.
   - Run lightweight markdown or diff checks when available, such as
     `git diff --check`.

## Minimal `AGENTS.md` Shape

Use this shape when creating a fresh file, trimming sections that do not apply:

```md
# Agent Instructions

## Compatibility
- `CLAUDE.md` is the Claude Code bridge for this agent instruction file.

## Project Context
- Read `README.md` or the repo's existing development guide for the human
  development flow.
- Keep docs and code aligned when behavior, APIs, data shape, or workflow changes.

## Git Workflow
- Prefer git worktrees for parallel or unrelated agent work.
- Treat existing uncommitted changes as user-owned unless told otherwise.
- Prefer rebase-based conflict resolution unless the repo requires merges.

## Coding Rules
- Follow the repo's existing lint, format, naming, and review conventions.
- [Add distilled project-specific rules here.]

## Verification
- [Add actual local test, lint, build, or smoke commands here.]
```

## Minimal Human Dev-Flow Section

Add this to the repo's existing human development guide. Use `README.md` only
when it is the best or only guide.

```md
## Development Flow

- Read `AGENTS.md` before using an agent on this repo.
- Use a git worktree for parallel or unrelated agent work.
- Setup: `[actual setup command or "not documented yet"]`
- Run locally: `[actual run command or "not documented yet"]`
- Verify: `[actual test/lint/build command or "not documented yet"]`
```

## Completion Report

Report the files changed, the existing rules that were captured, any missing
commands the repo still needs to document, and whether worktree guidance is
ready to use.
