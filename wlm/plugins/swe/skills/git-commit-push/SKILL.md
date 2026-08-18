---
name: git-commit-push
description: Use when the user wants the specific low-level Git operation to stage selected changes, create a commit, push existing commits, or commit and push. Works from either a regular branch or a git worktree. Respect the exact requested endpoint; for end-to-end wrap-up with quality checks, prefer swe:finish-work.
---

# Git Commit Push

Version: 1.3.0

Perform only the requested Git mutation while preserving user-owned changes.

## Establish scope

- Match the requested endpoint: stage only, commit only, push only, or commit
  and push. Do not perform a later step merely because this skill supports it.
- Require an explicit Git mutation request. Do not infer permission to stage,
  commit, or push merely because implementation or verification finished.
- Run `git status --short --branch` and review both unstaged and staged changes.
- Treat pre-existing staged, unstaged, and untracked files as user-owned until
  they are clearly part of the requested scope.
- If the intended paths are clear from the task and diff, proceed with those
  paths. If a mixed worktree makes the commit scope materially ambiguous, ask
  the user before staging or committing.
- Never reset, clean, restore, checkout, stash, amend, or force-push unrelated
  work to make the operation easier.

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
change so formatters do not churn unrelated files. If the user explicitly asks
to skip checks, report exactly what was skipped.

Stop before committing when required checks fail unless the user explicitly
accepts the failure. Never commit credentials, private keys, tokens, or obvious
temporary output.

## Choose the commit boundary

- Default to one commit for the cohesive change in the requested scope.
- Do not create commits as progress markers after individual files, subtasks,
  tool calls, tests, fixes, or agent turns.
- Split pending work only when the user asks, the repository convention
  requires it, or each part is independently understandable, testable, and
  revertible.
- Stage together the code, tests, docs, formatting, and generated metadata that
  jointly deliver the same outcome.
- If related work is still incomplete, continue it before committing instead
  of creating a checkpoint.
- Preserve existing commits. Do not amend, squash, or rewrite them merely to
  reduce commit count without explicit instruction.

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
Do not blindly restage the whole repository and retry. If the user asked for a
local commit only, stop here and state that nothing was pushed.

## Synchronize and push

For a push-only request, do not create a new commit. Inspect the current branch,
remote, and upstream before contacting the remote:

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
ahead/behind relation. Do not create a merge commit or force-push unless the
repository requires it or the user explicitly authorizes it.

## Confirm the result

Report:

- Operation performed and commit hash/subject when applicable
- Files staged or committed
- Branch and pushed remote when applicable
- Checks run, results, and any explicitly skipped checks
- Remaining staged, unstaged, or untracked changes
- Remote URL only when useful, with embedded credentials redacted
