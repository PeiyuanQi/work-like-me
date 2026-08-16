---
name: find-poc
description: Identify and rank the best-supported person, team, role, or official channel for a non-code request. Use when the user asks for a point of contact (POC), owner, approver, responsible team, "who handles this," "who should I ask," or help routing reimbursement, PTO, budget, customer, vendor, security, IT, project, or team questions. Use swe:find-code-reviewer instead for human code-review routing.
---

# Find a Point of Contact

Find the most defensible current contact without inventing identity, ownership,
availability, or contact details.

## Establish Scope

Determine the organization, team or project, request type, location or business unit
when relevant, and whether the user needs a named person, a role, or an official
channel. Infer these from available context and ask only when a missing detail would
materially change the result.

If the request is specifically about choosing or assigning a human code reviewer,
route it to `swe:find-code-reviewer`.

## Gather Evidence

Use the strongest available read-only sources:

1. User-provided policies, org charts, directories, project documents, or messages.
2. Connected organizational sources such as a directory, policy repository, project
   tracker, CRM, service catalog, or recent ownership discussion, when available.
3. `worker:search-memory` for documented team, role, policy, project, and tool context.

Search by both the request topic and likely owning functions. Typical mappings include:

| Request | Likely evidence or owner |
| --- | --- |
| Reimbursement or budget | Expense policy, approval chain, manager, finance owner |
| PTO or people policy | Current policy, manager, people/HR operations |
| Customer or vendor | Account record, customer success, sales, procurement, vendor owner |
| Security or IT | Service catalog, security/IT team, support or escalation channel |
| Team or project | Org chart, project documentation, team lead, subject-matter owner |

Prefer current authoritative sources over old mentions. Record the source and date when
available, and flag stale or conflicting evidence. Treat a historical participant or
document author only as a candidate, not automatically as the current owner.

## Select and Rank Contacts

Prefer, in order:

1. an explicitly documented current owner or approver;
2. an official team, role, queue, or channel responsible for the request;
3. a manager or broader organizational channel that can route the request.

Return a short ranked list when evidence supports multiple candidates. Report a named
person only when a source supports both their identity and current responsibility.
Never infer a contact method from private data, commit metadata, or an unrelated account.
Do not claim that someone is available or still in a role without evidence.

## Return Results

For each recommended contact, include:

- verified name, role, team, or official channel;
- why it matches the request;
- source and its date or freshness caveat;
- supported contact method, if one is documented;
- confidence (`high`, `medium`, or `low`).

If no current contact is verifiable, say what was searched and recommend the narrowest
supported role, team, directory, or manager escalation path. Do not invent a person.

Do not message, assign, or otherwise contact anyone unless the user explicitly asks for
that external action and the target is unambiguous. If the user wants help drafting a
first-contact message after choosing the POC, use `worker:contact-new-teammate` when
appropriate.
