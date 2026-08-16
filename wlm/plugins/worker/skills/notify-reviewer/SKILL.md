---
name: notify-reviewer
description: Notify a human reviewer or documented review channel that a pull request or merge request is ready for review. Use when the user explicitly asks to send, share, or draft a PR/MR review notification, including "notify the reviewer," "send the PR link," or "message the team that this is ready for review." Use swe:find-code-reviewer when the recipient is not already established; use swe:submit-work for the full code-submission workflow.
---

# Notify Reviewer

Send a concise, evidence-based review notification without inventing the recipient,
contact method, change status, or delivery result.

## Establish the Request

Confirm from available context:

- the PR/MR URL and repository;
- whether it is actually ready for review or still a draft;
- the intended reviewer or official review channel;
- the requested communication channel, if specified;
- the change summary and any checks, risks, or known failures worth mentioning.

Do not treat "ready for review" by itself as authorization to contact someone. Draft
only unless the user explicitly asked to send or notify. If the link, target, or
authorization is ambiguous, resolve it from current context or ask one concise question
before making the external change.

## Resolve the Recipient and Channel

- If a reviewer is already assigned or named, verify the identity from the PR/MR or a
  documented team source when practical.
- If the reviewer is unknown, use `swe:find-code-reviewer`. Do not use
  `worker:find-poc` for code-review routing.
- Use `worker:search-memory` only when documented team preferences, reviewer rotation,
  or communication channels may be stored there. Do not rely on a hard-coded memory
  path.
- Prefer a documented review channel over guessing a person's private contact method.
- Never derive an email address or chat identity from Git commit metadata.

Use the user-specified channel when available. Otherwise prefer a currently connected,
purpose-built messaging or email capability supported by documented team context. Do
not invent a CLI command, webhook, channel name, or address. If no sending capability is
available, return a ready-to-send draft and clearly state that it was not sent.

## Compose the Notification

Match the channel and team tone. Keep chat messages brief; add a concise subject for
email. Include only verified facts:

- PR/MR title and link;
- one- or two-sentence change summary;
- review area or reason this recipient is relevant, when useful;
- verification status and material known failures;
- a real deadline or urgency only when the user supplied one.

Use this adaptable default:

```markdown
Hi [name/team] — [PR/MR title] is ready for review: [link]

[Brief summary]. [Verification or known-risk note, if useful.]

Could you review [specific area, if applicable]? [Real deadline, if any.]
```

Avoid generic urgency, unsupported claims that checks passed, and unnecessary branch
details when the link already provides them.

## Send and Verify

Before sending, verify that the final recipient, channel, and link match the user's
request. Use the available messaging or email capability and inspect its result. Never
report success from an attempted command alone.

Report:

- recipient or channel;
- communication method;
- the PR/MR notified about;
- confirmed send status, or the exact blocker if it was not sent.
