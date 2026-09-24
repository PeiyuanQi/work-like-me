---
name: git-commit-push
description: "Performs only the requested low-level Git operation (stage selected changes, commit, push existing commits, or commit and push) from a branch or git worktree while preserving user-owned changes. Use when the user asks for just that operation. For end-to-end wrap-up with quality checks, use swe:finish-work; to integrate a local task branch into the default branch, use swe:land-work."
---

# Git Commit Push

Version: 1.5.0

Perform only the requested Git mutation while preserving user-owned changes.

This skill does not move commits between branches. In a repository whose
delivery flow keeps task branches local and pushes only the default branch, use
`swe:land-work` rather than pushing the task branch.

## Establish scope

- Match the requested endpoint: stage only, commit only, push only, or commit
  and push. Stop there even though this skill supports later steps.
- Act only on an explicit Git mutation request. Finished implementation or
  verification does not by itself grant permission to stage, commit, or push.
- Run `git status --short --branch` and review both unstaged and staged changes.
- Treat pre-existing staged, unstaged, and untracked files as user-owned until
  they are clearly part of the requested scope.
- If the task and diff make the intended paths clear, proceed with those paths.
  If a mixed worktree makes the commit scope materially ambiguous, ask the user
  before staging or committing.
- Leave unrelated work untouched: no reset, clean, restore, checkout, stash,
  amend, or force-push to make the operation easier.

Useful inspection commands:

```bash
git status --short --branch
git diff --name-status
git diff --cached --name-status
git diff -- <paths>
git diff --cached -- <paths>
```

## Run proportional checks

If formatting, linting, and verification have not already run, use
`swe:prepare-code-for-commit` before committing. Scope checks to the intended
change so formatters don't churn unrelated files. If the user explicitly asks
to skip checks, report exactly what was skipped.

Stop before committing when required checks fail, unless the user explicitly
accepts the failure. Keep credentials, private keys, tokens, and obvious
temporary output out of commits.

## Choose the commit boundary

- Default to one commit for the cohesive change in the requested scope.
- Commits are not progress markers after individual files, subtasks, tool
  calls, tests, fixes, or agent turns.
- Split pending work only when the user asks, the repository convention
  requires it, or each part is independently understandable, testable, and
  revertible.
- Stage together the code, tests, docs, formatting, and generated metadata that
  jointly deliver the same outcome.
- If related work is still incomplete, continue it before committing instead
  of creating a checkpoint.
- Preserve existing commits. Amending, squashing, or rewriting them merely to
  reduce commit count needs explicit instruction.

## Stage the intended change

Prefer explicit pathspecs:

```bash
git add -- <path1> <path2>
```

Use `git add -A` only when the user explicitly wants all repository changes and
the reviewed status confirms that every change belongs in the commit.

Verify the index before committing:

```bash
git diff --cached --name-status
git diff --cached --stat
git diff --cached --check
```

If the user asked only to stage files, stop here and report the staged set and
any remaining unstaged changes.

## Create the commit

Follow the repository's commit convention when one exists. Otherwise use a
conventional commit with a short imperative subject:

```text
<type>: <description>
```

Common types are `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`,
and `perf`.

```bash
git commit -m "<type>: <short description>"
git show --stat --oneline --summary HEAD
```

If a hook changes files or the commit fails, inspect status and diffs again.
before retrying, and restage only the intended paths rather than the whole
repository. If the user asked for a local commit only, stop here and state that
nothing was pushed.

## Synchronize and push

For a push-only request, push existing commits without creating a new one.
Inspect the current branch, remote, and upstream before contacting the remote:

```bash
git branch --show-current
git remote -v
git fetch <remote>
git rev-parse --abbrev-ref --symbolic-full-name "@{upstream}"
git rev-list --left-right --count "HEAD...@{upstream}"
```

The `rev-list` output is `<local-only> <upstream-only>`. Rebase only when the
upstream-only count is greater than zero. If unrelated working-tree changes
make a rebase unsafe, stop and ask rather than stashing, resetting, or cleaning
them. When the worktree is safe to refresh, prefer:

```bash
git rebase "@{upstream}"
```

If no upstream exists, select the intended remote and push with tracking:

```bash
git push -u <remote> <branch>
```

Otherwise:

```bash
git push
```

If the push is rejected because the remote moved, fetch and re-check the
ahead/behind relation. Create a merge commit or force-push only when the
repository requires it or the user explicitly authorizes it.

## Confirm the result

Report:

- Operation performed and commit hash/subject when applicable
- Files staged or committed
- Branch and pushed remote when applicable
- Checks run, results, and any explicitly skipped checks
- Remaining staged, unstaged, or untracked changes
- Remote URL only when useful, with embedded credentials redacted
