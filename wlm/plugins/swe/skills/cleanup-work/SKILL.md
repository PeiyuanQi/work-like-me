---
name: cleanup-work
description: "Use when the user explicitly asks to remove a completed Git worktree and delete its local task branch after delivery. Verifies the exact target, requires a clean worktree, and proves the task commit is contained in the remote default branch before using non-forced removal. Do not use for code cleanup, unfinished work, forced deletion, or remote branch deletion."
---

# Cleanup Work

Version: 1.0.0

Remove one completed Git worktree and its local task branch without discarding
work. Cleanup is a destructive delivery action and requires explicit user
authorization, either directly or as part of an authorized `swe:land-work`
request.

## Caller Contract

- `swe:land-work` may call this skill only after it verifies that the landed
  commit is present on the remote default branch and only when the user also
  requested cleanup. The caller must be running outside the target worktree.
- A user may call this skill directly with an exact or unambiguous completed
  worktree target.
- Do not call it automatically from `start-work`, `finish-work`, `submit-work`,
  or ordinary task completion.
- Treat abandonment or deletion of unmerged work as a different, destructive
  request. This skill must not reinterpret it as normal completed-work cleanup.

## 1. Resolve the Exact Target

Operate from a different checkout than the worktree being removed:

```bash
git rev-parse --show-toplevel
git worktree list --porcelain
git -C <target-worktree> status --short --branch
git -C <target-worktree> branch --show-current
```

- Resolve an absolute target path and its checked-out branch from Git metadata;
  do not construct a destructive target from an unresolved variable, glob, or
  guessed directory.
- Confirm the target is a registered linked worktree belonging to this
  repository.
- Never remove the primary repository checkout, the default-branch integration
  worktree, the caller's current worktree, or a worktree used by another active
  task.
- Refuse an ambiguous target and report the matching worktrees instead.

## 2. Prove Cleanup Is Safe

1. Require empty staged, unstaged, and untracked status in the target worktree.
2. Confirm no merge, rebase, cherry-pick, or revert is in progress.
3. Resolve the canonical remote and its default branch; do not assume `origin`
   or `main`.
4. Fetch that remote immediately before the containment check.
5. For a task branch, prove its tip is an ancestor of the remote default branch:

```bash
git fetch <remote> --prune
git merge-base --is-ancestor <task-branch> <remote>/<default-branch>
```

For a detached worktree, apply the same containment check to `HEAD` and skip
branch deletion. If containment cannot be proven, stop. Do not use `--force`,
`git branch -D`, reset, stash, or file deletion to make the check pass.

## 3. Remove the Worktree

From another checkout of the same repository, remove only the verified path:

```bash
git worktree remove <absolute-target-worktree>
git worktree list --porcelain
```

- Do not pass `--force`.
- If Git refuses removal, stop and report its reason.
- Do not run broad filesystem deletion or prune unrelated worktree metadata.

## 4. Delete Only the Local Task Branch

After confirming the worktree was removed, delete its local branch with Git's
merged-safety check:

```bash
git branch -d <task-branch>
```

- Never delete the default branch.
- Never use `-D` when `-d` refuses.
- Do not delete a remote branch or modify an upstream unless the user makes a
  separate explicit request for that operation.

## Completion Report

Report the repository, removed worktree path, deleted local branch or detached
HEAD, remote default branch used for containment proof, landed commit, and any
target left intact because a safety check failed.
