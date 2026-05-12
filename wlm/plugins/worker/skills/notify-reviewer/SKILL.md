---
name: notify-reviewer
description: Use when user wants to notify someone about a merge request, send MR link to reviewer, or message the team about code ready for review.
---

# Notify Reviewer

Version: 1.0.0

Send a merge request link to the appropriate communication channel to notify the reviewer.

## When to Use

- User says: "notify", "send MR link", "message reviewer", "let them know"
- Merge request created and reviewer needs to be notified
- Code ready for review and team should be informed

## Step 1: Identify Reviewer

**REQUIRED SUB-SKILL:** Use worker:find-poc to identify the appropriate reviewer.

This will return:
- Reviewer name
- Role
- Best contact method

## Step 2: Find Preferred Communication Channel

Search memory for communication preferences:
- Look in `memory/corps/tools/` for Slack, Teams, Email configurations
- Search for team communication preferences
- Check for any "preferred contact method" notes

Common channels:
- Slack
- Microsoft Teams
- Email
- Discord

## Step 3: Compose Message

Create a clear, concise message:
```
🔍 Code Review Request

Branch: <branch-name>
MR: <mr-link>
Summary: <brief description of changes>

Please review when you have time.
```

## Step 4: Send Message

Send to the appropriate channel:

**Slack:**
```bash
# Use Slack CLI or webhook if configured
slack chat send --channel "#code-reviews" --text "<message>"
```

**Teams:**
```bash
# Use Teams webhook if configured
curl -X POST <teams-webhook-url> -d "<message>"
```

**Email:**
- Draft email to reviewer
- Subject: Code Review: <branch-name>
- Body: MR link + brief summary

## Step 5: Confirm

Report:
- Reviewer notified
- Channel used
- Message sent
