---
name: git-start-work
description: Use when user wants to start new code work, create a new feature branch, begin coding on a fresh branch, switch to latest main before starting work, or coordinate parallel/multi-agent development. Ask to use git worktrees so multiple agents can work at the same time without colliding, and support regular branches when explicitly requested. Also useful when the user says "git wt".
---

# Git Start Work

Version: 1.1.1

Start new code work from the latest main branch. Supports two modes:
- **Worktree** — Isolated workspace in separate directory (default and recommended for multi-agent work)
- **Regular branch** — Standard git checkout

## When to Use

- User says: "start new work", "start new feature", "begin coding", "new branch"
- User wants to work on a bug fix or new feature
- User needs to refresh their branch from latest main

## Step 0: Ask Worktree Preference

Ask the user unless they already chose a mode:
```
How would you like to work?

1. Worktree (recommended, default) — Isolated workspace for parallel or multi-agent work
2. Regular branch — Simple git checkout
```

If no preference is expressed after asking, default to worktree. Strongly prefer
worktrees when multiple agents may be active, when the current checkout has
unrelated changes, or when the user asks to start independent work.

## Integration Rule

When refreshing from upstream or resolving conflicts, prefer a rebase-based
workflow that preserves the original intent of the work:

```bash
git fetch origin
git rebase origin/<main-branch>
```

During conflicts, keep the behavior the branch was trying to introduce unless
the user explicitly changes direction. Avoid merge commits unless the repository
requires them or the user asks for one.

## Branch Naming Convention

Use these prefixes based on the type of work:
- `feat/` - New features (e.g., `feat/user-authentication`)
- `fix/` - Bug fixes (e.g., `fix/login-validation`)
- `docs/` - Documentation changes
- `refactor/` - Code restructuring
- `test/` - Adding or updating tests
- `chore/` - Maintenance tasks

---

## Mode 1: Regular Branch

### Step 1: Check Repository Exists

```bash
ls -la /path/to/repo/.git
```

If not exists, clone from remote:
```bash
git clone <remote-url>
cd repo-name
```

### Step 2: Fetch Latest Changes

```bash
git fetch origin
```

### Step 3: Determine Main Branch

```bash
MAIN_BRANCH=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')
test -n "$MAIN_BRANCH" || MAIN_BRANCH=$(git remote show origin | sed -n 's/.*HEAD branch: //p')
```

Common names: `main`, `master`, `develop`

### Step 4: Checkout Latest Main

```bash
git switch --track -c "$MAIN_BRANCH" "origin/$MAIN_BRANCH"
```

If the local main branch already exists, update it by rebasing onto the remote
default branch rather than creating a merge commit:

```bash
git switch "$MAIN_BRANCH"
git rebase "origin/$MAIN_BRANCH"
```

### Step 5: Create New Branch

If user specified a branch name:
```bash
git switch -c <prefix>/<description>
```

If user didn't specify, ask them:
- What type of work? (feature/fix/docs/refactor)
- What is the short description?

Example:
```bash
git switch -c feat/user-login
```

### Step 6: Confirm

Report:
- Branch name created
- Current branch
- Any relevant next steps

---

## Mode 2: Worktree (Isolated Workspace)

**Core principle:** Systematic directory selection + safety verification = reliable isolation.

### Directory Selection Process

Follow this priority order:

#### 1. Check Existing Directories

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**If found:** Use that directory.

#### 2. Check CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**If preference specified:** Use it without asking.

#### 3. Ask User

If no directory exists and no CLAUDE.md preference:
```
No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. worktrees/ (project-local)
3. ~/.config/worktrees/<project>/ (global)

Which would you prefer?
```

### Safety Verification

**CRITICAL: Must verify directory is ignored before creating worktree.**

#### For Project-Local Directories (.worktrees or worktrees)

```bash
# Check if directory is ignored (respects local, global, and system gitignore)
git check-ignore -q .worktrees 2>/dev/null && echo "IGNORED" || echo "NOT_IGNORED"
git check-ignore -q worktrees 2>/dev/null && echo "IGNORED" || echo "NOT_IGNORED"
```

**If NOT ignored:**

1. Add the appropriate line to `.gitignore`.
2. Include that `.gitignore` update in the current change or ask before making a
   separate setup commit.
3. Proceed with worktree creation after Git confirms the directory is ignored.

**Why critical:** Prevents accidentally committing worktree contents to repository.

#### For Global Directory (~/.config/worktrees)

No .gitignore verification needed — outside project entirely.

### Creation Steps

#### Step 1: Detect Project Name and Main Branch

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
MAIN_BRANCH=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')
test -n "$MAIN_BRANCH" || MAIN_BRANCH=$(git remote show origin | sed -n 's/.*HEAD branch: //p')
```

Common fallback values for `MAIN_BRANCH` are `main`, `master`, and `develop`.

#### Step 2: Create Worktree

```bash
# Determine full path
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/worktrees/*)
    path="$LOCATION/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with new branch from the latest remote default branch
git fetch origin
git worktree add "$path" -b "$BRANCH_NAME" "origin/$MAIN_BRANCH"
cd "$path"
```

#### Step 3: Run Project Setup

Auto-detect and run appropriate setup:

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then uv sync; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

#### Step 4: Verify Clean Baseline

Run tests to ensure worktree starts clean:
```bash
# Use project-appropriate command
npm test
cargo test
pytest
go test ./...
```

**If tests fail:** Report failures, ask whether to proceed or investigate.

**If tests pass:** Continue.

### Step 5: Report Location

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

---

## Common Mistakes to Avoid

### Skipping ignore verification

- **Problem:** Worktree contents get tracked, pollute git status
- **Fix:** Always use `git check-ignore` before creating project-local worktree

### Assuming directory location

- **Problem:** Creates inconsistency, violates project conventions
- **Fix:** Follow priority: existing > CLAUDE.md > ask

### Proceeding with failing tests

- **Problem:** Can't distinguish new bugs from pre-existing issues
- **Fix:** Report failures, get explicit permission to proceed

### Hardcoding setup commands

- **Problem:** Breaks on projects using different tools
- **Fix:** Auto-detect from project files (package.json, etc.)
