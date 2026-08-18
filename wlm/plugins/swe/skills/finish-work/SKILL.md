---
name: finish-work
description: "Use only at an explicit Git delivery boundary: when the user asks to prepare completed software work for commit, commit it, push it, save it to Git, or make it ready to submit. Runs proportional checks, reviews the diff, and creates one coherent delivery commit by default. Do not use merely because an ordinary coding task or agent turn ended. Orchestrates prepare-code-for-commit and git-commit-push."
---

# Finish Work

Version: 1.1.0

Finish a development change by checking quality, reviewing intent, committing,
and pushing when requested. Treat this workflow as a delivery boundary, not a
recurring checkpoint during active implementation.

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

4. Choose the commit boundary.
   - Confirm the user requested a commit, push, submission, or other explicit
     Git delivery. Do not infer authorization from ordinary task completion.
   - Default to one commit for the coherent outcome completed in the current
     request.
   - Split commits only when each part is independently reviewable and
     revertible, or when the user or repository convention requires it.
   - Do not create progress, checkpoint, formatting-fix, test-fix, or
     per-file commits when those changes belong to the same pending outcome.
   - If related implementation work remains, finish and verify it before
     committing instead of recording an intermediate checkpoint.

5. Commit and push.
   - Use `swe:git-commit-push`.
   - Read `references/commit-guidance.md` before choosing the commit type.
   - Invoke the commit operation once per planned delivery commit; normally
     this means one invocation for the current request.
   - If the user asked for a local commit only, commit without pushing and say
     that the branch was not pushed.

## Safety Checks

- Do not stage unrelated files just because they are present.
- Do not commit or push solely because implementation or verification finished.
- Do not rewrite history, force-push, reset, or clean unless the user explicitly
  requested that operation.
- Do not amend or squash existing commits merely to reduce commit count.
- If verification fails, stop before committing unless the user explicitly
  accepts the failure.
- If the branch is behind, prefer rebase-based refresh that preserves the
  original intent of the change.

## Completion Report

Report the commit count and rationale, commit hash or hashes, branch, pushed
remote if any, checks run, check result, files changed, and any skipped or
failing verification.
