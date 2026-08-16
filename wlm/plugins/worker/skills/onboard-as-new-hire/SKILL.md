---
name: onboard-as-new-hire
description: Onboard the agent into a company as a new hire by learning the organization's business, structure, people, approved tools, policies, terminology, communication practices, and operating norms, then recording verified workplace context in canonical memory. Use when the user asks the agent to "onboard yourself," learn the company, understand how the organization works, discover workplace tools or key contacts, or prepare to operate as a company teammate. Do not use for project, repository, development-environment, or coding-agent onboarding; use swe:onboard-repo or swe:start-work for those tasks.
---

# Onboard as New Hire

Version: 1.2.0

Build a source-backed company map similar to the context a human new hire needs. Learn
the organization before narrowing into individual assignments. Minimize questions,
avoid unsupported claims, and preserve the user's control over external actions.

## Keep Company and Project Onboarding Separate

This is company onboarding, not project onboarding.

- Focus on the company, business, organization, teams, people, workplace systems,
  policies, terminology, culture, and ways of working.
- Do not inspect the current repository merely because it is the working directory.
- Do not set up source code, dependencies, branches, worktrees, development tools, or
  project documentation.
- Do not treat a repository README, package manifest, issue tracker, or code ownership
  file as evidence about the company unless the user or an authoritative workplace
  source identifies it as company documentation.
- If the request is really about joining a software project or preparing a repository,
  stop this workflow and route to `swe:onboard-repo` or `swe:start-work`.

## Establish Scope

Determine the company, business unit, office or region, team, role, and depth of
onboarding requested. Infer these from available context and ask only when a missing
detail would materially change the sources searched or information saved.

Treat onboarding as permission to inspect relevant context read-only and document the
result. It does not authorize messaging people, joining channels, changing permissions,
installing plugins, or connecting accounts.

## Reuse Existing Context First

1. Use `worker:search-memory` for existing company, organization, team, tool, policy,
   terminology, and contact context before asking the user questions.
2. If memory roots are ambiguous or fragmented, use `worker:consolidate-memory` to find
   the canonical store. Do not choose or create an arbitrary relative `memory/` tree.
3. Inventory the tools, apps, connectors, and local capabilities already available to
   the agent. Distinguish an available integration from a verified signed-in or
   authorized account.
4. Inspect relevant user-provided or connected sources read-only when available, such
   as the company handbook, official intranet or wiki, org chart, employee directory,
   shared drive, policy library, communication search, service catalog, or workplace
   calendar. Prefer authoritative company sources over broad filesystem, repository,
   or message-history searches.

Do not request installation or connection of a missing integration unless the user asks
to extend access. Otherwise, record the gap and suggest the narrowest useful next step.

## Build the Workplace Map

Gather only durable facts useful for operating inside the company:

- **Company:** mission, business model, products or services, customers, major business
  units, locations, and company-specific terminology when supported by current sources.
- **Communication:** approved chat and email systems, official team channels, and which
  medium is used for announcements, routine coordination, or urgent escalation.
- **Office and knowledge tools:** document, spreadsheet, presentation, file-sharing,
  wiki, meeting, and calendar systems that are relevant to the user's work.
- **Organization:** verified team name, roles, reporting or ownership relationships,
  peer teams, and official routing channels. Use `worker:find-poc` when ownership or a
  point of contact must be established.
- **Policies and operating norms:** security and privacy expectations, approval paths,
  working hours or location norms, recurring company and team meetings, decision
  records, naming conventions, and other documented working agreements.
- **Access state:** what the agent can inspect now, what is merely known to exist, and
  what remains unavailable or unverified.

For each material fact, retain the source, source date or observed date, and confidence.
Do not treat a historical document author, old participant, or visible account as a
current owner. Flag stale or conflicting evidence rather than silently selecting one.

## Ask Focused Questions

Ask only for gaps that remain after discovery. Group related questions and prefer
specific confirmation over a generic interview. Typical gaps include:

- Which company, business unit, location, or team should be primary when several appear
  relevant?
- Which documented tool is the official channel when sources conflict?
- Which work norms are informal and therefore absent from connected sources?
- Should verified findings be saved to memory when the request was exploratory rather
  than an instruction to complete onboarding?

Never ask the user to repeat information already available in current context or memory.

## Record Verified Context

Use `worker:update-memory` to write confirmed, durable findings to the canonical memory
store. Organize them under the existing company, organization, or team structure;
preserve the store's established naming and dating conventions instead of imposing a
new layout.

- Update an existing topic when practical instead of creating duplicate summaries.
- Preserve provenance and note unresolved conflicts or freshness caveats.
- Save concise operational facts, not complete messages, documents, or directory dumps.
- Do not store passwords, tokens, private keys, authentication details, confidential
  message bodies, or unnecessary personal data.
- Report the exact memory files created or changed.

## External Introduction

If the user asks the agent to introduce itself, first prepare a short onboarding summary
or draft. Contact a person or team only when the user explicitly requests the external
action and the target and channel are unambiguous. Use `worker:contact-new-teammate` for
a first-contact message when appropriate.

## Verify and Report

Before declaring onboarding complete, confirm that:

- important claims are sourced and current enough for their use;
- verified access is not confused with an integration merely being available;
- unresolved gaps and conflicts are explicit;
- memory writes point to the canonical store and contain no sensitive material;
- no external message, permission change, installation, or account connection occurred
  without explicit authorization.

Return a concise new-hire briefing with company context, communication and office tools,
organization and team structure, policies and operating norms, key official contacts or
channels, verified access, memory files changed, unresolved gaps, and recommended next
steps. Separate verified facts from user-confirmation needs. Do not include project setup
or repository orientation in the completion criteria.
