---
name: cleanup-work
description: "Removes one completed Git worktree and its local task branch after delivery, never forced, once it has verified the exact target, a clean worktree, and that the task commit is in the remote default branch. Use when the user explicitly asks to remove a finished worktree or delete its local branch, or when swe:land-work was authorized to clean up. Not for code cleanup, unfinished work, forced deletion, or remote branch deletion."
---

# Cleanup Work

Version: 1.1.0

Remove one completed Git worktree and its local task branch without discarding
work. Cleanup is a destructive delivery action, so it needs explicit user
authorization, either directly or as part of an authorized `swe:land-work`
request.

## Caller Contract

- `swe:land-work` may call this skill only after it verifies that the landed
  commit is on the remote default branch, only when the user also requested
  cleanup, and only from outside the target worktree.
- A user may call this skill directly with an exact or unambiguous completed
  worktree target.
- `swe:start-work`, `swe:finish-work`, `swe:submit-work`, and ordinary task
  completion do not call it.
- Abandoning or deleting unmerged work is a different, destructive request.
  Handle it separately rather than reinterpreting it as completed-work cleanup.

## 1. Resolve the Exact Target

Operate from a different checkout than the worktree being removed:

```bash
git rev-parse --show-toplevel
git worktree list --porcelain
git -C <target-worktree> status --short --branch
git -C <target-worktree> branch --show-current
```

- Resolve an absolute target path and its checked-out branch from Git metadata;
  Build a destructive target only from resolved values, never from an
  unresolved variable, glob, or guessed directory.
- Confirm the target is a registered linked worktree of this repository.
- Leave these checkouts in place: the primary repository checkout, the
  default-branch integration worktree, the caller's current worktree, and any
  worktree used by another active task.
- If the target is ambiguous, stop and report the matching worktrees.

## 2. Prove Cleanup Is Safe

1. Require empty staged, unstaged, and untracked status in the target worktree.
2. Confirm no merge, rebase, cherry-pick, or revert is in progress.
3. Resolve the canonical remote and its default branch rather than assuming
   `origin` or `main`.
4. Fetch that remote immediately before the containment check.
5. For a task branch, prove its tip is an ancestor of the remote default branch:

```bash
git fetch <remote> --prune
git merge-base --is-ancestor <task-branch> <remote>/<default-branch>
```

For a detached worktree, apply the same containment check to `HEAD` and skip
branch deletion. If containment cannot be proven, stop and report. Making the
check pass with `--force`, `git branch -D`, reset, stash, or file deletion
would discard exactly the work these checks protect, so don't.

## 3. Remove the Worktree

From another checkout of the same repository, remove only the verified path,
without `--force`:

```bash
git worktree remove <absolute-target-worktree>
git worktree list --porcelain
```

- If Git refuses removal, stop and report its reason.
- Remove nothing else: no broad filesystem deletion and no pruning of unrelated
  worktree metadata.

## 4. Delete Only the Local Task Branch

After confirming the worktree was removed, delete its local branch with Git's
merged-safety check:

```bash
git branch -d <task-branch>
```

- Keep the default branch.
- If `-d` refuses, stop and report; do not escalate to `-D`.
- Leave remote branches and upstream configuration alone unless the user makes
  a separate explicit request for that operation.

## Completion Report

Report the repository, removed worktree path, deleted local branch or detached
HEAD, remote default branch used for the containment proof, landed commit, and
any target left intact because a safety check failed.
