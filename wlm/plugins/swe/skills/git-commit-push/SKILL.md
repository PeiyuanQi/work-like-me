---
name: git-commit-push
description: Use when user wants the specific low-level git operation to commit changes, push code to remote, save work, or stage files for commit. Works from either a regular branch or a git worktree. For end-to-end wrap-up with quality checks, prefer swe:finish-work.
---

# Git Commit Push

Version: 1.1.1

Commit changes and push to the remote repository using conventional commits
format. For a full wrap-up flow, prefer `swe:finish-work`.

## When to Use

- User says: "commit", "push code", "save changes", "commit and push"
- User wants to save their work locally
- User is ready to share their code remotely
- User explicitly wants the git operation without the broader finish workflow

## Preflight

If formatting, linting, and verification have not already run, use
`swe:prepare-code-for-commit` before staging. If the user explicitly asks to
skip checks, say which checks were skipped in the completion report.

## Conventional Commits Format

```
<type>: <description>

[optional body]
[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `refactor` - Code restructuring
- `test` - Adding/updating tests
- `chore` - Maintenance, dependencies
- `style` - Code style changes
- `perf` - Performance improvements

## Step 1: Check Git Status

```bash
git status
```

Shows:
- Modified files
- New untracked files
- Staged files

## Step 2: Review Changes

Before staging, review what changed:
```bash
git diff
git diff --staged  # if anything is already staged
```

## Step 3: Stage Changes

Stage all changes:
```bash
git add -A
```

Or stage specific files:
```bash
git add <file1> <file2>
```

## Step 4: Determine Commit Type

Ask user or infer from context:
- New feature? → `feat`
- Bug fix? → `fix`
- Documentation? → `docs`
- Refactoring? → `refactor`
- Tests? → `test`
- Maintenance? → `chore`

## Step 5: Create Commit

```bash
git commit -m "<type>: <short description>"
```

Examples:
```bash
git commit -m "feat: add user login form"
git commit -m "fix: resolve validation error on empty input"
git commit -m "docs: update API documentation"
```

## Step 6: Push to Remote

If the user asked for a local commit only, stop after commit and report that the
branch was not pushed.

Before pushing, check whether the branch has an upstream and whether it is
behind. If the branch needs to be refreshed, prefer rebasing while preserving
the original intent of the local work:

```bash
git fetch origin
git branch -vv
UPSTREAM=$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null || true)
test -n "$UPSTREAM" && git rebase "$UPSTREAM"
```

If a push is rejected because the remote moved, fetch and rebase instead of
creating a merge commit. During conflicts, keep the behavior the branch was
trying to introduce unless the user explicitly changes direction.

```bash
git push
```

If the branch does not have an upstream yet:

```bash
git push -u origin <branch-name>
```

## Step 7: Confirm

Report:
- Commit hash (short)
- Number of files changed
- Branch pushed to
- Remote URL
- Checks run or explicitly skipped
