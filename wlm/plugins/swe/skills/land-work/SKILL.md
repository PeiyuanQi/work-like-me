---
name: land-work
description: "Use at an explicit delivery boundary to land completed local task-branch or worktree changes directly onto the remote default branch without a PR when repo-local guidance or the user selects a direct-integration workflow. Verifies and commits the task, rebases for linear history, fast-forward merges into the local default branch, and pushes that branch. Do not use for ordinary task completion or review-based PR/MR submission."
---

# Land Work

Version: 1.1.0

Land verified work from a local task worktree onto the repository's default
branch without publishing the task branch or creating a pull request. This is
an explicit delivery operation; never infer permission to run it merely because
implementation is complete.

## 1. Confirm Direct-Integration Mode

- Resolve the canonical remote URL and its default branch; do not assume the
  remote is `origin` or the branch is `main`.
- Use direct integration only when repo-local guidance defines it or the user
  explicitly chooses it for the current repository. Repository policy selects
  the workflow but does not itself authorize a commit, merge, or push.
- Never infer direct integration from a hosting provider, account name, remote
  owner, repository visibility, or apparent maintainer count.
- Use `swe:submit-work` when repo policy or the user selects review-based
  delivery.
- Keep the task branch local by default. Do not push it merely as an
  intermediate step.

## 2. Inspect Both Worktrees

From the repository root, inspect the task worktree, default-branch worktree,
and all linked worktrees:

```bash
git status --short --branch
git remote -v
git worktree list --porcelain
git symbolic-ref --short refs/remotes/<remote>/HEAD
```

- Identify the exact task branch, task worktree, default branch, and integration
  worktree before mutating either checkout.
- Treat every pre-existing staged, unstaged, and untracked change as user-owned.
- Require the default-branch integration worktree to be clean. Do not stash,
  reset, clean, switch, or overwrite it to make integration possible.
- Serialize delivery through the default branch. If another agent or process is
  landing work, wait or stop rather than changing the branch concurrently.
- If the completed work is already on the default branch, skip the branch
  integration steps and use `swe:finish-work` for the explicitly requested
  checks, commit, and push.

## 3. Prepare and Commit the Task Locally

1. Review the task worktree's staged and unstaged diffs and isolate the intended
   change from unrelated files.
2. Use `swe:prepare-code-for-commit` and run the proportional repo-defined tests
   or build checks.
3. Re-check the diff and run `git diff --check`.
4. Use `swe:git-commit-push` in **commit-only** mode to create one cohesive
   delivery commit by default. Do not push the task branch.
5. Require the task worktree to be clean before integration.

Stop before integration when required checks fail unless the user explicitly
accepts the failure.

## 4. Synchronize and Rebase

Fetch the canonical remote immediately before integration:

```bash
git fetch <remote> --prune
```

Then:

1. Verify again that the remote default branch exists and the integration
   worktree is clean.
2. Compare the local default branch with `<remote>/<default-branch>`.
3. If the local default branch is only behind, update it with a fast-forward.
4. If it contains unexpected local-only commits or has diverged, stop and report
   the commits instead of rewriting user-owned history.
5. Rebase the task branch onto the updated local default branch when needed.
   Resolve conflicts in the task worktree, preserving the intended behavior of
   both the new upstream work and the task.
6. Re-run relevant verification after any rebase or conflict resolution.

Prefer a linear history. Do not create a merge commit and do not force-push.

## 5. Fast-Forward the Default Branch and Push

In the clean integration worktree:

```bash
git merge --ff-only <task-branch>
git push <remote> <default-branch>
```

- Inspect the commits and diff being added before pushing.
- If the remote moves before the push, fetch again. Rebase only the known
  current landing commits onto the new remote tip, rerun relevant verification,
  and retry a normal push. If that range is ambiguous, stop instead of
  rewriting history.
- Never bypass branch protection. If direct push is rejected by repository
  policy, report the blocker and use a PR only when the user requests that
  fallback.
- Verify that the remote default branch resolves to the landed commit before
  reporting success.

## 6. Delegate Cleanup When Authorized

- If the user included cleanup in the landing request, call
  `swe:cleanup-work` only after verifying the landed commit on the remote
  default branch. Pass the exact task worktree, local task branch, canonical
  remote, default branch, and verified landed commit to the cleanup workflow.
- Call cleanup only from outside the target worktree. If this workflow is
  running inside the task worktree, leave it intact and report cleanup as
  deferred for a caller running from the integration checkout after this task
  has ended.
- Otherwise, leave the task worktree and branch intact and report them.
- Do not inline removal, infer cleanup permission from successful delivery, or
  broaden cleanup to other completed worktrees.

## Completion Report

Report the task branch and worktree, default branch and integration worktree,
commit or commits landed, checks run, whether a rebase or conflict resolution
was needed, fast-forward result, pushed remote, remote verification, cleanup
result or deferral reason, and any remaining local worktree or branch.
