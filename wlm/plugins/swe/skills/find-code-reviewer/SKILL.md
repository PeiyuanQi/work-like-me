---
name: find-code-reviewer
description: Use when user asks who reviews code, finds a reviewer, needs a code review contact, or asks who should review their merge request. This is specifically for CODE REVIEW only - use worker:find-poc for all other POC requests. Works with branch-based and worktree-based development.
---

# Find Code Reviewer

Version: 1.0.0

Find the appropriate person to contact for code review based on team structure, code ownership, and project context.

## When to Use

- User says: "who reviews", "find reviewer", "code review", "reviewer for this PR"
- Need to identify who reviews a specific file or area
- Creating a merge request and need to assign reviewer

**NOT for non-code POC** - use `worker:find-poc` instead.

## Step 1: Search Memory for Code Review Information

**REQUIRED SUB-SKILL:** Use worker:search-memory to find team and code review information.

Search for:
- Team structure and code ownership
- Reviewer assignments
- Preferred reviewers for different areas
- Review policies

## Step 2: Check CODEOWNERS File

Look for CODEOWNERS file in the repository:
```bash
find . -name "CODEOWNERS" -type f
```

Common locations:
- `.github/CODEOWNERS`
- `docs/CODEOWNERS`
- `CODEOWNERS` (root)

Read the file to identify who owns which paths.

## Step 3: Check Git Blame

For files the user modified, find recent contributors:
```bash
git blame <file> | head -20
```

Identify who made recent changes - they may be good reviewers.

## Step 4: Check Recent PRs/MRs

Check recent merge requests to see who typically reviews:
```bash
git log --oneline -20
```

Or check the Git hosting platform for recent reviewers.

## Step 5: Determine Best Reviewer

Based on findings, determine:
- **Name:** Person to contact
- **Role:** Their role (tech lead, maintainer, etc.)
- **Contact method:** Best way to reach them (Slack, Teams, Email)
- **Why:** Why they're a good fit for this review

## Step 6: Return Results

Format the results:
```markdown
# Code Reviewer

**Name:** [Name]
**Role:** [Role]
**Best Contact:** [Slack/Teams/Email]
**Why:** [Why they're the right reviewer]
```

## Fallback

If no clear reviewer found:
- Suggest team lead or tech lead as default
- Ask user if they have a specific person in mind
- Suggest asking in the team chat/channel
