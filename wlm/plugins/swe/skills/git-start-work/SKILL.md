---
name: git-start-work
description: Use for the specific low-level Git operation of creating a feature branch or worktree, starting from the latest remote default branch, refreshing an existing branch from upstream, or isolating parallel/multi-agent work. Trigger on requests such as "new branch", "create a worktree", "start from latest main", or "git wt". For repository onboarding, dependency setup, and baseline tests, use swe:start-work.
---

# Git Start Work

Version: 1.2.0

Create or refresh a Git workspace without overwriting user-owned changes. Keep
this skill limited to Git workspace operations; let `swe:start-work` coordinate
repository setup, environments, and baseline verification.

The command blocks below use POSIX shell syntax. Detect the active shell first.
On PowerShell, keep the Git operations but translate shell and filesystem logic
to platform-native equivalents such as `Test-Path`, `Split-Path`, and
`Join-Path`; do not assume Bash, WSL, or Git Bash is installed.

## 1. Inspect Before Mutating

Resolve the repository root and inspect all linked worktrees:

```bash
REPO_ROOT=$(git rev-parse --show-toplevel) || exit 1
git -C "$REPO_ROOT" status --short --branch
git -C "$REPO_ROOT" worktree list --porcelain
```

Treat every existing change as user-owned.

- Never reset, clean, discard, or auto-stash changes.
- Do not switch branches or rebase a dirty checkout without explicit approval.
- Prefer a new worktree when changes are unrelated to the new task.
- If the dirty changes are the intended foundation, explain that a worktree
  based on the remote default branch will omit them. Stay in the checkout or
  ask how the user wants to carry the foundation forward.
- Run relative-path checks from `REPO_ROOT`, not from an arbitrary subdirectory.

## 2. Choose the Workspace Mode

Honor an explicit request for a worktree or regular branch. Otherwise ask once:

```text
How would you like to work?

1. Worktree (recommended) - isolated workspace for parallel work
2. Regular branch - switch this clean checkout to a new branch
```

Default to a worktree after asking when the user has no preference. Strongly
prefer worktrees for parallel/multi-agent work or when the current checkout has
unrelated changes.

Use the repository's branch convention when documented. Otherwise use a short
descriptive name with an appropriate prefix such as `feat/`, `fix/`, `docs/`,
`refactor/`, `test/`, or `chore/`. In Codex repositories, honor any configured
`codex/` prefix.

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
verified remote baseline. Do not switch to or rewrite local `main` merely to
start new work.

```bash
git -C "$REPO_ROOT" switch -c "$BRANCH_NAME" "origin/$MAIN_BRANCH"
```

When the user explicitly asks to refresh an existing feature branch, fetch and
rebase that branch onto the verified remote baseline only from a clean checkout:

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

If it is not ignored, do not create the worktree there yet. Ask before editing
`.gitignore`, then re-run `git check-ignore`. A location outside the repository
does not need this check.

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

Do not assume uncommitted files from the original checkout appear in the new
worktree. Do not copy, stash, or move them without explicit user direction.

## 6. Report the Result

Report:

- workspace mode, absolute path, and branch name
- verified remote baseline (`origin/<default-branch>` and commit)
- whether existing changes were preserved in another checkout
- any branch/path collision, missing remote, or unresolved default branch

For dependency setup and baseline tests, hand off to `swe:start-work` or follow
the repository's documented workflow when the user explicitly requests it.
