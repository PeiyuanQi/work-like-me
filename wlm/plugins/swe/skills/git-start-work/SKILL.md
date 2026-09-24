---
name: git-start-work
description: "Creates a feature branch or git worktree from the latest remote default branch, or refreshes an existing branch from upstream, without overwriting user-owned changes. Use for that Git workspace operation alone, such as \"new branch\", \"create a worktree\", \"start from latest main\", \"git wt\", or isolating parallel or multi-agent work. For repository setup, dependencies, and baseline tests, use swe:start-work."
---

# Git Start Work

Version: 1.4.0

Create or refresh a Git workspace without overwriting user-owned changes. Keep
this skill limited to Git workspace operations; `swe:start-work` coordinates
repository setup, environments, and baseline verification.

The command blocks below use POSIX shell syntax. Detect the active shell first.
On PowerShell, keep the Git operations but translate shell and filesystem logic
to platform-native equivalents such as `Test-Path`, `Split-Path`, and
`Join-Path`; Bash, WSL, or Git Bash may not be installed.

## 1. Inspect Before Mutating

Resolve the repository root and inspect all linked worktrees:

```bash
REPO_ROOT=$(git rev-parse --show-toplevel) || exit 1
git -C "$REPO_ROOT" status --short --branch
git -C "$REPO_ROOT" worktree list --porcelain
```

Treat every existing change as user-owned:

- Never reset, clean, discard, or auto-stash changes.
- Switch branches or rebase a dirty checkout only with explicit approval.
- Prefer a new worktree when the changes are unrelated to the new task.
- If the dirty changes are the intended foundation, explain that a worktree
  based on the remote default branch will omit them. Stay in the checkout or
  ask how the user wants to carry the foundation forward.
- Run relative-path checks from `REPO_ROOT`, not from an arbitrary
  subdirectory.

## 2. Choose the Workspace Mode

Honor an explicit request for a worktree or a regular branch. Otherwise ask
once:

```text
How would you like to work?

1. Worktree (recommended) - isolated workspace for parallel work
2. Regular branch - switch this clean checkout to a new branch
```

Default to a worktree after asking when the user has no preference. For
parallel or multi-agent work, or when the current checkout has unrelated
changes, recommend the worktree firmly, because a shared checkout lets
concurrent work collide.

Use the repository's branch convention when documented. Otherwise use a short
descriptive name with a prefix such as `feat/`, `fix/`, `docs/`, `refactor/`,
`test/`, or `chore/`. In Codex repositories, honor any configured `codex/`
prefix.

## 3. Resolve the Remote Baseline

Fetch first, then determine and verify the remote default branch:

```bash
git -C "$REPO_ROOT" fetch origin --prune
MAIN_BRANCH=$(git -C "$REPO_ROOT" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')

if [ -z "$MAIN_BRANCH" ]; then
  MAIN_BRANCH=$(git -C "$REPO_ROOT" remote show origin | sed -n 's/.*HEAD branch: //p')
fi

test -n "$MAIN_BRANCH" || {
  echo "Unable to determine origin's default branch"
  exit 1
}
git -C "$REPO_ROOT" show-ref --verify "refs/remotes/origin/$MAIN_BRANCH"
```

If `origin` is absent, authentication fails, or the default branch remains
ambiguous, stop and report the exact condition instead of guessing.

Before creating a branch, check for collisions:

```bash
git -C "$REPO_ROOT" show-ref --verify --quiet "refs/heads/$BRANCH_NAME"
git -C "$REPO_ROOT" worktree list --porcelain
```

If the branch already exists or is checked out elsewhere, reuse it only when
the user intended that; otherwise choose or ask for a different name.

## 4. Create a Regular Branch

Require a clean checkout, then create the feature branch directly from the
verified remote baseline. Starting new work does not require switching to or
rewriting local `main`.

```bash
git -C "$REPO_ROOT" switch -c "$BRANCH_NAME" "origin/$MAIN_BRANCH"
```

When the user explicitly asks to refresh an existing feature branch, fetch and
rebase that branch onto the verified remote baseline, from a clean checkout
only:

```bash
git -C "$REPO_ROOT" switch "$BRANCH_NAME"
git -C "$REPO_ROOT" rebase "origin/$MAIN_BRANCH"
```

Preserve the branch's intended behavior during conflicts. Avoid merge commits
unless repository policy or the user requires them. If the user asks to update
the local default branch and it has diverged from upstream, report the
divergence before rewriting it.

## 5. Create a Worktree

### Select a Location

Check project-local locations from the repository root, then inspect loaded
repo guidance such as root `AGENTS.md` or `CLAUDE.md` for a convention:

```bash
LOCATION=
test -d "$REPO_ROOT/.worktrees" && LOCATION="$REPO_ROOT/.worktrees"
test -z "$LOCATION" && test -d "$REPO_ROOT/worktrees" && LOCATION="$REPO_ROOT/worktrees"
```

If no convention exists, ask the user to choose:

1. `<repo>/.worktrees/` - project-local, hidden
2. `<repo>/worktrees/` - project-local
3. `~/.config/worktrees/` - outside the repository

For a project-local location, verify the prospective worktree path is ignored:

```bash
git -C "$REPO_ROOT" check-ignore -q "$LOCATION/$BRANCH_NAME"
```

If it is not ignored, add a narrow entry for the worktree directory, such as
`/.worktrees/`, to the root `.gitignore` before creating the worktree, then
re-run `git check-ignore`. An unignored worktree inside the repository shows up
as untracked files in the main checkout and can be committed by accident.
Mention the `.gitignore` edit in the report so the user can keep or revert it.
A location outside the repository does not need this check.

If you are unsure the entry is right, for example because of an unusual
layout, an existing pattern that conflicts with it, a shared or generated
`.gitignore`, or uncommitted edits already in `.gitignore`, have a fresh
subagent with clean context review the proposed entry before you apply it. If
you are still unsure after that review, show the user the proposed entry and
ask them to review it before creating the worktree.

### Create from the Remote Baseline

Build an explicit absolute path and create the new branch from the verified
remote default branch:

```bash
project=$(basename "$REPO_ROOT")

case "$LOCATION" in
  "$REPO_ROOT/.worktrees"|"$REPO_ROOT/worktrees")
    WORKTREE_PATH="$LOCATION/$BRANCH_NAME"
    ;;
  *)
    WORKTREE_PATH="$LOCATION/$project/$BRANCH_NAME"
    ;;
esac

git -C "$REPO_ROOT" worktree add "$WORKTREE_PATH" -b "$BRANCH_NAME" "origin/$MAIN_BRANCH"
git -C "$WORKTREE_PATH" status --short --branch
```

Uncommitted files from the original checkout do not appear in the new
worktree. Copy, stash, or move them only with explicit user direction.

## 6. Report the Result

Report:

- workspace mode, absolute path, and branch name
- verified remote baseline (`origin/<default-branch>` and commit)
- whether existing changes were preserved in another checkout
- any branch/path collision, missing remote, or unresolved default branch

For dependency setup and baseline tests, hand off to `swe:start-work`, or
follow the repository's documented workflow when the user explicitly requests
it.
