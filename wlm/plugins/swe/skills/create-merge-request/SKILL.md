---
name: create-merge-request
description: "Creates one pull request or merge request (draft by default) for an already prepared branch, from a regular branch or git worktree, and verifies the result. Use when the user wants only the low-level operation of opening a PR or MR. For end-to-end submission with finish checks, independent review, and reviewer routing, use swe:submit-work."
---

# Create Merge Request

Version: 1.3.0

Create exactly one merge request (MR) or pull request (PR) for an already
prepared branch. For preparation, independent review, reviewer discovery, and
notification, use `swe:submit-work`.

## 1. Inspect Without Rewriting the Branch

```bash
git status --short --branch
git branch --show-current
git branch -vv
git remote -v
```

- A PR/MR contains pushed commits only, so uncommitted changes stay out of it.
- If the branch still needs checks, commits, or scope cleanup, return to
  `swe:finish-work`, unless the user explicitly wants a draft from the
  currently committed state.
- Creating the request never requires a rebase, merge, amend, or force-push.
  If a refresh or conflict repair is needed, report it, or perform it only when
  the user requested that broader work.
- Stop if the current branch is the target/default branch or no writable
  source remote can be identified.

## 2. Resolve Source, Target, and Existing Requests

- Use the user's target branch when specified; otherwise derive the remote
  default branch rather than assuming `main`.
- Account for forks: the pushed source repository can differ from the target
  repository.
- If an open PR/MR already exists for the same source and target, return its
  URL instead of creating a duplicate.

## 3. Ensure the Prepared Branch Is Published

If the prepared branch has no upstream, push it with tracking:

```bash
git push -u <source-remote> <branch-name>
```

If local and remote histories diverge, stop and explain the mismatch. A plain
force push is off the table, and `--force-with-lease` needs explicit user
authorization for the history rewrite.

## 4. Create the PR/MR

Create a draft unless the user explicitly asks for ready-for-review status.
Build a meaningful title and body from the compare range; the body summarizes
what changed, why, impact, and validation. Write the body to a temporary file
for CLI calls so Markdown keeps real newlines, then remove the file.

### GitHub

Prefer the connected GitHub app's pull-request creation operation after the
branch is pushed, deriving repository, head, and base explicitly. If the
connector cannot access the repository or cannot express a forked head, fall
back to an authenticated GitHub CLI:

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

`glab` takes `--description`, not `--description-file`, so pass the body file's
contents through the shell's safe file-content argument handling to keep real
newlines. Confirm the installed version supports these flags and adapt to its
documented equivalents when necessary.

### Other Hosts or Manual Fallback

Use the repository's configured provider integration or CLI. If no creation
tool is available, return the exact compare/create URL and a ready-to-paste
title and body, and say plainly that the request was not created.

## 5. Verify and Return

Read the created request back from the provider and verify:

- URL and open state
- source and target branches
- draft versus ready-for-review status
- title and body presence

Return those fields plus any remaining blocker. Merging is a separate action
that needs its own explicit user request.

## Submission-Flow Boundary

This low-level skill does not run code review, select reviewers, or notify
people. When called by `swe:submit-work`, return the verified request metadata
so that orchestrator can load
[references/code-review-guidance.md](references/code-review-guidance.md), run
the independent review, and handle reviewer routing.
