---
name: start-work
description: "Use when starting software engineering work end to end: beginning a feature, fix, refactor, docs task, or investigation; creating a branch or git worktree from latest main; onboarding to a repo before coding; or setting up dependencies before implementation. Orchestrates project-dev-setup, git-start-work, and manage-virtual-environments."
---

# Start Work

Version: 1.0.0

Start a scoped development session from a clean, current baseline. This is the
high-level entry point for new software engineering work.

## Workflow

1. Inspect the current repository state.
   - Run `git status --short --branch`.
   - Treat existing uncommitted changes as user-owned.
   - If unrelated local changes exist, prefer a new git worktree.

2. Load repo conventions with `swe:project-dev-setup`.
   - Read repo-local guidance before choosing setup, test, or docs commands.
   - Identify the default branch, package managers, env files, and verification
     commands from the repo itself.

3. Create the development workspace with `swe:git-start-work`.
   - Prefer a git worktree for parallel or multi-agent work.
   - Use a regular branch only when the user explicitly asks or the repo
     convention requires it.
   - When using worktrees, read `references/worktree-guidance.md`.

4. Set up dependencies only when needed.
   - If the worktree or checkout needs environment setup, use
     `swe:manage-virtual-environments`.
   - Prefer the repo's documented setup command over generic defaults.

5. Verify the baseline.
   - Run the repo's lightest relevant verification command when available.
   - If verification fails before coding starts, report it as baseline state and
     ask whether to investigate or proceed.

## Safety Checks

- Do not reset, clean, or overwrite local changes unless the user explicitly
  requests it.
- Do not switch away from a dirty checkout when a worktree can avoid the
  collision.
- Do not invent setup commands when the repo is silent; say what is missing.
- Do not daemonize dev servers or agent processes.

## Completion Report

Report the chosen workspace mode, branch name, path, baseline verification
result, setup commands run, and any repo docs or commands that were missing.
