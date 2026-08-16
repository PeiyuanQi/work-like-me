---
name: create-merge-request
description: Use when user wants the specific low-level operation to create a merge request or pull request for an already prepared branch. Works with branch-based and worktree-based development. For end-to-end submission with finish checks and reviewer routing, prefer swe:submit-work.
---

# Create Merge Request

Version: 1.2.0

Create exactly one merge request (MR) or pull request (PR) for an already
prepared branch. For preparation, independent review, reviewer discovery, and
notification, use `swe:submit-work`.

## 1. Inspect Without Rewriting the Branch

Run:

```bash
git status --short --branch
git branch --show-current
git branch -vv
git remote -v
```

- Do not include uncommitted changes in the request; a PR/MR contains pushed
  commits only.
- If the branch still needs checks, commits, or scope cleanup, return to
  `swe:finish-work` unless the user explicitly wants a draft from the currently
  committed state.
- Do not rebase, merge, amend, or force-push merely to create the request. If
  refresh or conflict repair is needed, report it or perform it only when the
  user requested that broader work.
- Stop if the current branch is the target/default branch or if no writable
  source remote can be identified.

## 2. Resolve Source, Target, and Existing Requests

- Use the user's target branch when specified. Otherwise derive the remote
  default branch; do not assume `main`.
- Account for forks: the pushed source repository can differ from the target
  repository.
- Check whether an open PR/MR already exists for the same source and target. If
  it does, return that URL instead of creating a duplicate.

## 3. Ensure the Prepared Branch Is Published

If the prepared branch has no upstream, push it with tracking:

```bash
git push -u <source-remote> <branch-name>
```

If local and remote histories diverge, stop and explain the mismatch. Never use
a plain force push, and do not use `--force-with-lease` without explicit user
authorization for the history rewrite.

## 4. Create the PR/MR

Default to a draft request unless the user explicitly asks for ready-for-review
status. Build a meaningful title and body from the compare range. The body
should summarize what changed, why, impact, and validation. Use a temporary
body file for CLI calls so Markdown contains real newlines, then remove it.

### GitHub

Prefer the connected GitHub app's pull-request creation operation after the
branch is pushed. Derive repository, head, and base explicitly. If the connector
cannot access the repository or cannot express a forked head, fall back to an
authenticated GitHub CLI:

```bash
gh pr create --draft --repo <owner/repo> --base <target> --head <source> \
  --title "<title>" --body-file <body-file>
```

For a fork, pass `<owner>:<branch>` as the head. Omit `--draft` only when the
user explicitly requests ready-for-review status.

### GitLab

Use the configured GitLab integration when available; otherwise use an
authenticated GitLab CLI:

```bash
glab mr create --draft --source-branch <source> --target-branch <target> \
  --title "<title>" --description "<description>" --yes
```

Current `glab` uses `--description`, not `--description-file`; preserve real
newlines with the shell's safe file-content argument handling. Confirm the
installed version supports the selected flags and adapt to its documented
equivalents when necessary.

### Other Hosts or Manual Fallback

Use the repository's configured provider integration or CLI. If no creation
tool is available, return the exact compare/create URL and a ready-to-paste
title/body. Do not claim the request was created.

## 5. Verify and Return

Read the created request back from the provider and verify:

- URL and open state
- source and target branches
- draft versus ready-for-review status
- title and body presence

Return those fields plus any remaining blocker. Never merge the request unless
the user separately and explicitly asks.

## Submission-Flow Boundary

This low-level skill does not independently run code review, select reviewers,
or notify people. When called by `swe:submit-work`, return the verified request
metadata so that orchestrator can load `references/code-review-guidance.md`,
run the independent review, and handle reviewer routing.
