---
name: create-merge-request
description: Use when user wants to create a merge request, pull request, submit code for review, or merge their branch to main. Works with branch-based and worktree-based development.
---

# Create Merge Request

Version: 1.1.1

Create a merge request (MR) or pull request (PR), run an independent review,
and notify the appropriate reviewer.

## When to Use

- User says: "create merge request", "create PR", "submit for review", "open MR"
- User wants to merge their branch to main
- Code is ready for review

## Step 1: Ensure Branch is Current and Pushed

Check if branch exists on remote:
```bash
git status
git branch -vv
```

Fetch the target branch and prefer rebasing before submission when the branch is
behind or conflicts with the target:

```bash
git fetch origin
git rebase origin/<target-branch>
```

During conflicts, preserve the original intent of the branch unless the user
explicitly changes direction. Avoid merge commits unless the repo requires them
or the user asks for one.

If not pushed, push the branch:
```bash
git push -u origin <branch-name>
```

If the branch was already pushed and the local rebase rewrote commits, use
`git push --force-with-lease` only after confirming the remote branch still
contains the commits you rebased from. Do not use a plain force push.

## Step 2: Determine Platform

Identify the Git platform:
- GitHub → Pull Request
- GitLab → Merge Request
- Bitbucket → Pull Request

Check the remote URL:
```bash
git remote -v
```

## Step 3: Create MR/PR

**GitHub (using gh CLI):**
```bash
gh pr create --title "<title>" --body "<description>"
```

**GitLab (using glab CLI):**
```bash
glab mr create --title "<title>" --description "<description>"
```

**GitHub (manual):**
Open browser to:
```
https://github.com/<owner>/<repo>/compare/<main-branch>...<branch-name>
```

## Step 4: Get MR Link

Store the MR/PR URL returned from the command or extract from browser.

## Step 5: Run Independent Code Review

Before requesting human review, load:

`references/code-review-guidance.md`

Then prefer sending a subagent with the highest available effort/reasoning
setting to review the MR/PR. Give the subagent the MR/PR URL, target branch,
changed-file list, relevant diff or compare range, and the instruction to load
and follow `references/code-review-guidance.md` from this skill.

The subagent should return review findings ordered by severity, including file
and line references when possible. If subagents are unavailable, perform this
review locally using the same reference guidance and say that a subagent review
was not available.

## Step 6: Find Reviewer

**REQUIRED SUB-SKILL:** Use `swe:find-code-reviewer` to identify the appropriate
human reviewer for code review. Use `worker:find-poc` only for non-code POC
requests.

The reviewer skill will search memory and the repo for:
- Team structure
- CODEOWNERS file
- Git blame for recent changes
- Team directory

## Step 7: Notify Reviewer

**REQUIRED SUB-SKILL:** Use worker:notify-reviewer to send the MR link to the appropriate communication channel.

## Step 8: Confirm

Report:
- MR/PR URL
- Independent review result or fallback
- Reviewer name
- Notification method used
- Any notes for the user
