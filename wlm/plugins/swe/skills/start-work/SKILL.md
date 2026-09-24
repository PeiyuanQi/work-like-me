---
name: start-work
description: "Starts software engineering work end to end: loads repo conventions, keeps or creates a branch or git worktree from the latest default branch, sets up dependencies when needed, and verifies the baseline. Orchestrates swe:project-dev-setup, swe:git-start-work, and swe:manage-virtual-environments. Use when beginning a feature, fix, refactor, docs task, or investigation, or when onboarding to a repo or setting up dependencies before coding."
---

# Start Work

Version: 1.3.0

Start a scoped development session from a clean, current baseline. This is the
high-level entry point for new software engineering work.

## Workflow

1. Inspect the current repository state.
   - Run `git status --short --branch`.
   - Treat existing uncommitted changes as user-owned.
   - If the task depends on current uncommitted work, keep the current checkout
     and scope edits narrowly, because a fresh worktree would omit that work.
   - If unrelated local changes exist, prefer a new git worktree.

2. Load repo conventions with `swe:project-dev-setup`.
   - Read repo-local guidance before choosing setup, test, or docs commands.
   - Identify the default branch, package managers, env files, and
     verification commands from the repo itself.
   - Identify, from repo-local guidance or the user's explicit direction,
     whether delivery uses review branches and PRs or a direct-integration
     flow. When direct integration is selected, keep task branches local by
     default and use `swe:land-work` only at an explicit delivery boundary.
     Base this on that guidance, never on the remote owner or repository
     visibility.

3. Choose the development workspace.
   - Keep the current checkout for a read-only investigation, an already
     assigned worktree, or work that depends on current uncommitted changes.
   - Otherwise, create the workspace with `swe:git-start-work`.
   - Prefer a git worktree for parallel or multi-agent work.
   - Use a regular branch only when the user explicitly asks or the repo
     convention requires it.
   - When using worktrees, read
     [references/worktree-guidance.md](references/worktree-guidance.md).

4. Set up dependencies only when needed.
   - If the worktree or checkout needs environment setup, use
     `swe:manage-virtual-environments`.
   - Prefer the repo's documented setup command over generic defaults.

5. Verify the baseline.
   - Run the repo's lightest relevant verification command when available.
   - If verification fails before coding starts, report it as baseline state
     and ask whether to investigate or proceed.

## Safety Checks

- Reset, clean, or overwrite local changes only when the user explicitly
  requests it.
- When a worktree can avoid the collision, use one rather than switching away
  from a dirty checkout.
- When the repo is silent on setup commands, say what is missing instead of
  inventing them.
- Keep dev servers and agent processes attached rather than daemonizing them.

## Completion Report

Report the chosen workspace mode and why it was kept or created, branch name,
path, baseline verification result, setup commands run, delivery mode, and any
repo docs or commands that were missing.
