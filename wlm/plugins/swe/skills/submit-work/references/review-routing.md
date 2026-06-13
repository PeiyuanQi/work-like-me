# Review Routing

Submission is not complete until the code is reviewable and routed.

Reviewable means:

- Branch is pushed.
- Target branch is correct.
- PR/MR title and body explain intent, verification, and risk.
- Independent review has been run or explicitly skipped by the user.
- Known failing checks or follow-up work are called out.

Routing order:

1. `CODEOWNERS` or repo ownership docs.
2. Team memory or documented reviewer rotation.
3. Recent maintainers from blame, related PRs, or module history.
4. Team lead or maintainer fallback when no owner is clear.

Use `swe:find-code-reviewer` for code review. Use non-code POC skills only for
ownership questions outside code review.
