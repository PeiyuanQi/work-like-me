---
name: prepare-code-for-commit
description: Prepare modified code for commit by discovering repository-defined formatter and linter commands, applying them to the intended scope, checking for unexpected diff churn, and reporting failures. Use when the user asks to format code, run lint, clean up code, perform pre-commit checks, or when swe:finish-work or swe:git-commit-push needs a low-level quality pass. Do not commit or push.
---

# Prepare Code For Commit

Version: 1.2.0

Format and lint the intended change while preserving user-owned work. Prefer
repository commands over language defaults. For an end-to-end wrap-up that
also reviews, commits, and pushes, use `swe:finish-work`.

## 1. Capture the Baseline

- Run `git status --short --branch` when the work is in a Git repository.
- Review unstaged and staged diffs and record the paths that were already
  modified or untracked.
- Identify the files or package in scope from the user's request and the work
  completed in the current task.
- Never reset, clean, checkout, stash, stage, commit, or overwrite unrelated
  changes.
- If a mutating formatter cannot be limited safely and the worktree contains
  unrelated changes, use its check-only mode or ask before running it across
  the repository.

## 2. Discover the Repository Commands

Inspect sources in this order:

1. Repository instructions and contributor docs such as `AGENTS.md`,
   `CLAUDE.md`, `CONTRIBUTING*`, and relevant development documentation.
2. Dedicated commands in package scripts, `Makefile`, `justfile`, `Taskfile`,
   `tox.ini`, `noxfile.py`, build files, pre-commit hooks, and CI workflows.
3. Formatter and linter configuration such as `pyproject.toml`, `ruff.toml`,
   `eslint.config.*`, `.eslintrc*`, `.prettierrc*`, `biome.json`,
   `rustfmt.toml`, `clippy.toml`, `Cargo.toml`, or `go.mod`.
4. Team memory through the available memory-search capability. Do not assume a
   fixed memory directory exists; search only roots that are actually present.
5. Language defaults only when the repository is silent.

Inspect scripts or help output before using an unfamiliar option. A manifest or
configuration file proves that a tool is relevant, not which command or scope
the repository expects. Treat a search with no matches as "not found," not as a
failed quality check.

Do not install tools or fetch packages merely to run this pass. Prefer the
repository's pinned environment or package-manager execution command. If a
required tool is unavailable, report the skipped check and the missing command.

## 3. Choose Scope and Mode

- Use the smallest scope that covers the intended change: changed files first,
  then the affected package, then the workspace only when the repository's
  canonical command requires it.
- Run check-only modes first when practical to distinguish existing failures
  from changes introduced by this pass.
- Apply the repository-approved formatter and safe lint fixes to the intended
  scope. Do not run broad or semantic auto-fixes without a clear repository
  convention or user request.
- Do not add tests, builds, or release checks unless the caller requests broader
  verification or the repository's canonical quality command includes them.

When the repository is silent, use installed standard tools appropriate to the
language: Ruff for Python; the project's Prettier/ESLint or Biome for
JavaScript and TypeScript; `gofmt` and an installed Go linter for Go; and
`cargo fmt` plus Clippy for Rust. Use their normal check-only forms before
mutating when available.

## 4. Run and Verify

1. Run formatters before linters unless the repository defines another order.
2. Stop and report the exact command when a check fails. Do not silently infer
   success from an empty or failed composite command.
3. Re-run check-only modes after fixes.
4. Run `git diff --check` when available.
5. Compare post-run status and changed paths with the captured baseline. Inspect
   any unexpected path or large formatting churn; do not undo user-owned work.

## 5. Report

Summarize the commands and scope, files changed by the pass, failures or
warnings, checks skipped and why, and whether failures were pre-existing or
introduced. Explicitly state that this skill did not stage, commit, or push.
