---
name: submit-work
description: "Use for end-to-end submission of software work for human review: prepare, check, commit, and push as needed; create a PR/MR; run independent review; and identify a reviewer. Trigger on requests such as \"submit this for review\", \"prepare and route this PR\", or \"ready for review\" when the user wants the full workflow. Do not use for isolated commit/push (swe:finish-work), isolated PR/MR creation (swe:create-merge-request), reviewer lookup (swe:find-code-reviewer), or notification only (worker:notify-reviewer). Reviewer assignment or notification requires explicit user authorization."
---

# Submit Work

Version: 1.1.0

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
   - Read `swe:create-merge-request`'s
     `references/code-review-guidance.md` before reviewing the compare.
   - Prefer a high-effort subagent review when available.
   - If no subagent is available, do the review locally and say so.
   - Treat unresolved blocking findings as submission blockers; do not present
     the branch as ready without calling them out.

4. Route to a human reviewer.
   - Use `swe:find-code-reviewer` to identify and rank candidates.
   - Do not request, assign, or notify a reviewer unless the user explicitly
     asked for that external state change.
   - When notification is authorized, use `worker:notify-reviewer` only when
     the worker plugin is available.
   - Without authorization or notification tooling, return the reviewer
     recommendation and a ready-to-send message draft instead of pretending a
     request or notification happened.

## Safety Checks

- Do not merge the PR/MR unless the user explicitly asks.
- Do not force-push after a rebase without `--force-with-lease` and explicit
  confirmation that the remote state is expected.
- Do not use `worker:find-poc` for code review routing.
- Do not skip independent review unless the user explicitly asks.
- Do not treat "submit", "ready", or PR creation alone as authorization to
  contact or assign a human reviewer.

## Completion Report

Report the PR/MR URL, target branch, pushed source branch, independent review
result, reviewer, notification status, and any remaining merge blockers.
