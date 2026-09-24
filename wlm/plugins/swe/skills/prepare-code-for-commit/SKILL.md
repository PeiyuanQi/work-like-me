---
name: prepare-code-for-commit
description: "Formats and lints modified code with the repository's own formatter and linter commands, scoped to the intended change, checks for unexpected diff churn, and reports failures without committing or pushing. Use when the user asks to format code, run lint, clean up code, or run pre-commit checks, or when swe:finish-work, swe:git-commit-push, or swe:land-work needs a quality pass."
---

# Prepare Code For Commit

Version: 1.3.0

Format and lint the intended change while preserving user-owned work. Prefer
repository commands over language defaults. For an end-to-end wrap-up that also
reviews, commits, and pushes, use `swe:finish-work`.

## 1. Capture the Baseline

- Run `git status --short --branch` when the work is in a Git repository.
- Review unstaged and staged diffs, and record the paths that were already
  modified or untracked.
- Identify the files or package in scope from the user's request and the work
  completed in the current task.
- Leave unrelated changes untouched: no reset, clean, checkout, stash, stage,
  commit, or overwrite.
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
4. Team memory through the available memory-search capability. Search only
   memory roots that actually exist rather than assuming a fixed directory.
5. Language defaults, only when the repository is silent.

Inspect scripts or help output before using an unfamiliar option. A manifest or
configuration file proves that a tool is relevant, not which command or scope
the repository expects. A search with no matches means "not found", not a
failed quality check.

This pass does not install tools or fetch packages. Prefer the repository's
pinned environment or package-manager execution command, and if a required tool
is unavailable, report the skipped check and the missing command.

## 3. Choose Scope and Mode

- Use the smallest scope that covers the intended change: changed files first,
  then the affected package, then the workspace only when the repository's
  canonical command requires it.
- Run check-only modes first when practical, to separate existing failures
  from changes introduced by this pass.
- Apply the repository-approved formatter and safe lint fixes to the intended
  scope. Run broad or semantic auto-fixes only with a clear repository
  convention or user request.
- Add tests, builds, or release checks only when the caller requests broader
  verification or the repository's canonical quality command includes them.

When the repository is silent, use installed standard tools for the language:
Ruff for Python; the project's Prettier/ESLint or Biome for JavaScript and
TypeScript; `gofmt` and an installed Go linter for Go; and `cargo fmt` plus
Clippy for Rust. Use their check-only forms before mutating when available.

## 4. Run and Verify

1. Run formatters before linters unless the repository defines another order.
2. When a check fails, stop and report the exact command. An empty or failed
   composite command is not a success.
3. Re-run check-only modes after fixes.
4. Run `git diff --check` when available.
5. Compare post-run status and changed paths with the captured baseline.
   Inspect any unexpected path or large formatting churn without undoing
   user-owned work.

## 5. Report

Summarize the commands and scope, files changed by the pass, failures or
warnings, checks skipped and why, and whether failures were pre-existing or
introduced. State explicitly that this skill did not stage, commit, or push.
