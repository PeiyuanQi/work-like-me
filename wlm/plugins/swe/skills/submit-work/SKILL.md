---
name: submit-work
description: "Submits software work for human review end to end: prepares, checks, commits, and pushes as needed, creates a PR/MR, runs an independent review, and identifies a reviewer. Use for the full workflow, such as \"submit this for review\", \"prepare and route this PR\", or \"ready for review\". For single steps, use swe:finish-work, swe:land-work (no PR), swe:create-merge-request, swe:find-code-reviewer, or worker:notify-reviewer. Assigning or notifying a reviewer requires explicit user authorization."
---

# Submit Work

Version: 1.4.0

Submit finished code for human review with the branch current, pushed,
reviewed, and routed to the right reviewer.

Work being ready to deliver is not by itself a reason to run this workflow.
When repo-local guidance selects direct integration without a PR, use
`swe:land-work` instead.

## Workflow

1. Ensure the branch is ready.
   - If changes are uncommitted or checks have not run, use `swe:finish-work`.
   - Batch one cohesive submission into one delivery commit by default. Run the
     finish workflow after implementation and checks are complete, not after
     each intermediate repair or agent step.
   - If the user already committed and pushed, inspect status and continue.
   - Preserve existing commits; rewrite them to reduce their count only when
     the user explicitly requests history cleanup.
   - Push only related, reviewed changes.

2. Create the PR or MR with `swe:create-merge-request`.
   - Prefer the repo's configured hosting tool and target branch.
   - Use the platform CLI when available; otherwise provide the compare URL.
   - Read [references/review-routing.md](references/review-routing.md) for
     review and routing expectations.

3. Run independent review.
   - Read the shared
     [code-review guidance](../create-merge-request/references/code-review-guidance.md)
     from `swe:create-merge-request` before reviewing the compare.
   - Prefer a high-effort subagent review when available.
   - If no subagent is available, do the review locally and say so.
   - Treat unresolved blocking findings as submission blockers, and call them
     out rather than presenting the branch as ready.

4. Route to a human reviewer.
   - Use `swe:find-code-reviewer` to identify and rank candidates.
   - Request, assign, or notify a reviewer only when the user explicitly asked
     for that external state change.
   - When notification is authorized, use `worker:notify-reviewer` only when
     the worker plugin is available.
   - Without authorization or notification tooling, return the reviewer
     recommendation and a ready-to-send message draft, and say that no request
     or notification was sent.

## Safety Checks

- Merge the PR/MR only when the user explicitly asks.
- After a rebase, force-push only with `--force-with-lease` and explicit
  confirmation that the remote state is expected.
- Route code review with `swe:find-code-reviewer`, not `worker:find-poc`.
- Run the independent review unless the user explicitly asks to skip it.
- "Submit", "ready", or PR creation alone does not authorize contacting or
  assigning a human reviewer.

## Completion Report

Report the PR/MR URL, target branch, pushed source branch, independent review
result, reviewer, notification status, and any remaining merge blockers.
