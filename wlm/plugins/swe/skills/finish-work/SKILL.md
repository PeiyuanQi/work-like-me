---
name: finish-work
description: "Use when wrapping up software engineering work: preparing code for commit, running format/lint/test checks, reviewing diffs, creating a conventional commit, pushing a branch, or handling \"finish this\", \"commit this\", \"save and push\", or \"ready to submit\" requests. Orchestrates prepare-code-for-commit and git-commit-push."
---

# Finish Work

Version: 1.0.0

Finish a development change by checking quality, reviewing intent, committing,
and pushing when requested.

## Workflow

1. Inspect the change.
   - Run `git status --short --branch`.
   - Review unstaged and staged diffs.
   - Separate intended changes from unrelated user-owned changes.

2. Run quality checks.
   - Use `swe:prepare-code-for-commit` before committing unless the user
     explicitly asks to skip it.
   - Read `references/quality-checks.md` for how to choose verification scope.
   - Prefer repo-defined commands over language defaults.

3. Re-check the diff.
   - Confirm formatters did not introduce unrelated churn.
   - Confirm generated files, locks, and docs changes are intentional.
   - Run `git diff --check` when available.

4. Commit and push.
   - Use `swe:git-commit-push`.
   - Read `references/commit-guidance.md` before choosing the commit type.
   - If the user asked for a local commit only, commit without pushing and say
     that the branch was not pushed.

## Safety Checks

- Do not stage unrelated files just because they are present.
- Do not rewrite history, force-push, reset, or clean unless the user explicitly
  requested that operation.
- If verification fails, stop before committing unless the user explicitly
  accepts the failure.
- If the branch is behind, prefer rebase-based refresh that preserves the
  original intent of the change.

## Completion Report

Report the commit hash, branch, pushed remote if any, checks run, check result,
files changed, and any skipped or failing verification.
