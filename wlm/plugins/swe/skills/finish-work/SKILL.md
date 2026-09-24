---
name: finish-work
description: "Wraps up completed software work at an explicit Git delivery boundary: proportional checks, diff review, one coherent delivery commit by default, and a push only when asked. Orchestrates swe:prepare-code-for-commit and swe:git-commit-push. Use when the user asks to prepare finished work for commit, commit it, push it, save it to Git, or make it ready to submit, not merely because a task or agent turn ended. To land a local task branch on the default branch without a PR, use swe:land-work."
---

# Finish Work

Version: 1.3.0

Finish a development change by checking quality, reviewing intent, committing,
and pushing when requested. This workflow is a delivery boundary, not a
recurring checkpoint during active implementation.

## Workflow

1. Inspect the change.
   - Run `git status --short --branch`.
   - Review unstaged and staged diffs.
   - Separate intended changes from unrelated user-owned changes.

2. Run quality checks.
   - Use `swe:prepare-code-for-commit` before committing unless the user
     explicitly asks to skip it.
   - Read [references/quality-checks.md](references/quality-checks.md) to
     choose the verification scope.
   - Prefer repo-defined commands over language defaults.

3. Re-check the diff.
   - Confirm formatters did not introduce unrelated churn.
   - Confirm generated files, locks, and docs changes are intentional.
   - Run `git diff --check` when available.

4. Choose the delivery path.
   - If repo-local policy selects direct integration and the user asked to land
     a task branch on the default branch, use `swe:land-work` instead of
     pushing the task branch, and end this workflow there.

5. Choose the commit boundary.
   - Confirm the user requested a commit, push, submission, or other explicit
     Git delivery. Finishing implementation or verification is not that
     authorization.
   - Default to one commit for the coherent outcome completed in the current
     request.
   - Split commits only when each part is independently reviewable and
     revertible, or when the user or repository convention requires it.
   - Fold progress, checkpoint, formatting-fix, test-fix, and per-file changes
     into the pending outcome's commit rather than committing them separately.
   - If related implementation work remains, finish and verify it before
     committing instead of recording an intermediate checkpoint.

6. Commit and push.
   - Use `swe:git-commit-push`.
   - Read [references/commit-guidance.md](references/commit-guidance.md)
     before choosing the commit type.
   - Invoke the commit operation once per planned delivery commit; normally
     that is one invocation for the current request.
   - If the user asked for a local commit only, commit without pushing and say
     that the branch was not pushed.

## Safety Checks

- Stage only the intended files, even when unrelated files are present.
- Rewrite history, force-push, reset, or clean only when the user explicitly
  requested that operation.
- Leave existing commits as they are; amending or squashing them just to reduce
  the commit count needs explicit instruction.
- If verification fails, stop before committing unless the user explicitly
  accepts the failure.
- If the branch is behind, prefer a rebase-based refresh that preserves the
  original intent of the change.

## Completion Report

Report the commit count and rationale, commit hash or hashes, branch, pushed
remote if any, checks run and their results, files changed, and any skipped or
failing verification.
