---
name: contact-new-teammate
description: Draft a brief first-contact message to a coworker, new teammate, cross-team colleague, or internal stakeholder who may not know the sender. Use for introductory outreach, cold internal messages, asking a new colleague for help, or contacting someone for the first time. If the user first needs to identify whom to contact, use worker:find-poc instead.
---

# Contact New Teammate

## Gather Context

Use details the user already provided. When identity, organizational context, the recipient's role, or a relevant connection is missing and memory may answer it, use `worker:search-memory`.

Collect only the facts needed for the message:

- Sender name, role, and team
- Recipient name and why they are relevant
- Specific request and any real deadline
- Channel and tone, when specified

Do not invent roles, relationships, referrals, project involvement, or urgency. If a required detail remains unknown, leave a descriptive placeholder or ask one concise question when a useful draft cannot be produced without it.

## Draft the Message

- Match the requested channel and formality; default to a short chat message.
- Keep the introduction to at most one sentence.
- State why this person is relevant without implying unsupported familiarity.
- Make one clear, bounded request. Add what has already been tried only when useful.
- Prefer an asynchronous response unless a meeting is genuinely needed.
- Draft only by default. Do not send unless the user explicitly asks and a messaging capability is available.

Use this adaptable structure:

```markdown
# Draft Message

Hi [Name]—I'm [sender/role] on [team], reaching out because [specific relevance].

Could you [specific, bounded request]? [Optional useful context or deadline.]

Thanks,
[Sender name]
```

For email, add a concise subject line. If there is no genuine prior connection, say directly that the recipient owns or works on the relevant topic.
