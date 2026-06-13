---
name: submit-work
description: "Use when submitting software engineering work for review: opening a pull request or merge request, preparing a branch for review, running independent code review, finding a reviewer, notifying the reviewer, or handling \"create PR\", \"open MR\", \"submit this\", or \"ready for review\" requests. Orchestrates finish-work, create-merge-request, and find-code-reviewer."
---

# Submit Work

Version: 1.0.0

Submit finished code for human review with the branch current, pushed, reviewed,
and routed to the right reviewer.

## Workflow

1. Ensure the branch is ready.
   - If changes are uncommitted or checks have not run, use `swe:finish-work`.
   - If the user already committed and pushed, inspect status and continue.
   - Do not push unrelated or unreviewed local changes.

2. Create the PR or MR with `swe:create-merge-request`.
   - Prefer the repo's configured hosting tool and target branch.
   - Use the platform CLI when available; otherwise provide the compare URL.
   - Read `references/review-routing.md` for review and routing expectations.

3. Run independent review.
   - Follow `create-merge-request` review guidance.
   - Prefer a high-effort subagent review when available.
   - If no subagent is available, do the review locally and say so.

4. Route to a human reviewer.
   - Use `swe:find-code-reviewer` for code review ownership.
   - Use `worker:notify-reviewer` only when the worker plugin is available.
   - If notification tooling is unavailable, return the reviewer and message
     draft instead of pretending notification happened.

## Safety Checks

- Do not merge the PR/MR unless the user explicitly asks.
- Do not force-push after a rebase without `--force-with-lease` and explicit
  confirmation that the remote state is expected.
- Do not use `worker:find-poc` for code review routing.
- Do not skip independent review unless the user explicitly asks.

## Completion Report

Report the PR/MR URL, target branch, pushed source branch, independent review
result, reviewer, notification status, and any remaining merge blockers.
