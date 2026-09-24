# Review Routing

Submission is complete only when the code is reviewable and routed.

Reviewable means:

- The branch is pushed.
- The target branch is correct.
- The PR/MR title and body explain intent, verification, and risk.
- Independent review has run, or the user explicitly skipped it.
- Known failing checks or follow-up work are called out.

Routing order:

1. `CODEOWNERS` or repo ownership docs.
2. Team memory or documented reviewer rotation.
3. Recent maintainers from blame, related PRs, or module history.
4. Team lead or maintainer fallback when no owner is clear.

Use `swe:find-code-reviewer` for code review. Use non-code POC skills only for
ownership questions outside code review.
