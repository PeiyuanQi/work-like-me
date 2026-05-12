---
name: contact-new-teammate
description: Use when contacting a new co-worker or teammate for the first time, especially in a large corporation where they may not know who you are. Creates a brief, relevant introduction and polite request.
---

# Contact New Teammate

Version: 1.0.0

First-time contact with a colleague in a large organization where they may not know who you are.

## When to Use

- First time messaging a new teammate
- Reaching out to someone in a different team/group
- Cold contact in a corporate setting

## Step 1: Gather Context

**REQUIRED:** Use worker:search-memory to find:
1. **About "you" (the agent):** Who are you? What's your role? What projects do you work on?
2. **About the contact:** What's their role? What team? What projects?

Search for:
- `memory/corpx/soul.md` or similar files defining the agent
- `memory/teams/[their-team]/*`
- Any shared context (same project, shared stakeholder, etc.)

## Step 2: Craft Introduction

**Rule: Keep it under 1 sentence.** Be brief.

Find the most relevant connection:
- Same project → "Hi [Name], I work on [Project] with [Shared Person/Team]"
- Similar role → "Hi [Name], I'm also a [Role] on the [Team]"
- They've helped before → "Hi [Name], [Person] mentioned you could help with [Topic]"
- External stakeholder → "Hi [Name], I'm reaching out regarding [Project/Topic]"

## Step 3: Make the Request

Be specific and polite:
- "Would you be able to help me understand [X]?"
- "Could you point me to [X] or suggest who to ask?"
- "Do you have 5 minutes to chat about [X]?"

## Step 4: Return Draft Message

Format:
```markdown
# Draft Message

Hi [Name],

[1-sentence intro: who you are + relevant connection]

[Polite request]

Thanks!
[Your name/role]
```

## Tips

- Keep intro under 1 sentence (strict limit)
- Always state WHY you're contacting them specifically
- Be specific about what you need (not "help me" but "explain X")
- Offer context: what you've already tried, what you need
- If no memory exists, use generic intro: "Hi [Name], I'm [Role] on [Team] and I'm reaching out about [Topic]"
