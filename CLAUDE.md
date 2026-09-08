# Worker Plugin - CLAUDE.md

This document defines how to work with work-like-me repo.

## Virtual Environments

This project uses `uv` for Python virtual environment management:

```bash
cd wlm
source .venv/bin/activate  # Activate environment
uv sync                    # Install dependencies
```

## Always use First Principle Thinking

## Git Workflow

- This repository uses a solo-maintainer direct-integration flow; remote task
  branches and pull requests are optional, not the default delivery path.
- Use a local task branch in a separate git worktree for parallel or unrelated
  tasks. Keep that branch local unless the user explicitly asks to publish it.
- Treat existing uncommitted changes as user-owned unless the user says otherwise.
- Do not switch branches, rewrite history, or clean up another active worktree without explicit instruction.
- Keep changes scoped to the current worktree and say which worktree you used when it matters.
## Git Commit Cadence

- Treat commits as delivery boundaries, not routine progress checkpoints.
- Do not commit after each file, test, subtask, or agent turn. Completing an
  ordinary implementation task does not by itself authorize a commit or push.
- Default to one cohesive commit for each user-requested delivery. Split only
  when the parts are independently reviewable and revertible, or when the user
  or repository convention requires separate commits.
- In parallel work, contributors should leave intermediate changes uncommitted
  unless they were explicitly assigned a Git endpoint. When a commit is
  authorized, let the coordinating agent create the final delivery commit.
- Preserve existing commits. Do not amend, squash, or otherwise rewrite history
  merely to reduce commit count without explicit instruction.

## Git Conflict Resolution

- If branches diverge or conflicts appear, prefer rebase-based resolution that preserves the original intent of the work.
- Avoid merge commits for conflict resolution unless the repo explicitly requires them.
- Keep history clean and minimal while preserving the shape of the original change.

## Direct Integration

- Treat commit, integration, push, worktree removal, and branch deletion as
  explicit delivery actions; ordinary task completion does not authorize them.
- When authorized to deliver a completed task, use `swe:land-work`: verify and
  commit in the task worktree, fetch the remote, fast-forward the clean local
  `main`, rebase the task branch onto the updated `main` when needed,
  fast-forward merge it into `main`, and push `main` directly.
- If the delivery request also includes cleanup, let `swe:land-work` call
  `swe:cleanup-work` only after the remote `main` contains the landed commit.
  Cleanup must run outside the target worktree; otherwise leave the worktree
  and local branch intact and report cleanup as deferred.
- Serialize integrations into `main`; never let parallel agents land changes
  there concurrently.
- Prefer rebase-based conflict resolution that preserves the intent of both
  changes. Avoid merge commits and never force-push `main`.
- Use a pull request only when the user explicitly requests review or repository
  protection prevents direct integration.

## Code Review Bar

- Review frontend work for UX, visual polish, accessibility, and i18n.
- UX: keep flows intuitive, states explicit, and defaults sensible.
- Aesthetics: keep spacing, typography, alignment, and hierarchy consistent.
- Accessibility: use semantic HTML, keyboard support, focus states, contrast, and clear labels.
- i18n: avoid hard-coded locale assumptions, avoid string concatenation, and allow for text expansion.
- Review backend work for layered services, clear boundaries, and proper design.
- Keep transport, business logic, and persistence concerns separated when practical.
- Review database and data model changes carefully for naming, constraints, indexes, and normalization.
- Check for concurrency issues, race conditions, idempotency gaps, and transactional safety.
- For API design, follow RESTful principles: resource-oriented paths, correct HTTP verbs, appropriate status codes, and consistent request and response shapes.
