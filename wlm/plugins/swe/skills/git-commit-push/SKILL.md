---
name: git-commit-push
description: Use when user wants to commit changes, push code to remote, save work, or stage files for commit. Works from either a regular branch or a git worktree.
---

# Git Commit Push

Version: 1.0.0

Commit changes and push to the remote repository using conventional commits format.

## When to Use

- User says: "commit", "push code", "save changes", "commit and push"
- User wants to save their work locally
- User is ready to share their code remotely

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

```bash
git push -u origin <branch-name>
```

## Step 7: Confirm

Report:
- Commit hash (short)
- Number of files changed
- Branch pushed to
- Remote URL
