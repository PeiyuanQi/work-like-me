---
name: create-merge-request
description: Use when user wants to create a merge request, pull request, submit code for review, or merge their branch to main. Works with branch-based and worktree-based development.
---

# Create Merge Request

Version: 1.0.0

Create a merge request (MR) or pull request (PR) and notify the appropriate reviewer.

## When to Use

- User says: "create merge request", "create PR", "submit for review", "open MR"
- User wants to merge their branch to main
- Code is ready for review

## Step 1: Ensure Branch is Pushed

Check if branch exists on remote:
```bash
git status
git branch -vv
```

If not pushed, push the branch:
```bash
git push -u origin <branch-name>
```

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

## Step 5: Find Reviewer

**REQUIRED SUB-SKILL:** Use worker:find-poc to identify the appropriate reviewer.

The find-poc skill will search memory for:
- Team structure
- CODEOWNERS file
- Git blame for recent changes
- Team directory

## Step 6: Notify Reviewer

**REQUIRED SUB-SKILL:** Use worker:notify-reviewer to send the MR link to the appropriate communication channel.

## Step 7: Confirm

Report:
- MR/PR URL
- Reviewer name
- Notification method used
- Any notes for the user
