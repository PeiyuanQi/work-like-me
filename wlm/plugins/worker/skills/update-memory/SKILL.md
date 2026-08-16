---
name: update-memory
description: Save durable, user-useful decisions, milestones, preferences, contacts, or discoveries to user-maintained WLM memory. Use when the user explicitly asks to remember, save, store, or document context, or after a significant completed milestone when preserving verified facts will materially help future work. Do not use for transient progress, generic task summaries, speculative claims, or secrets and private data the user did not explicitly ask to retain.
---

Version: 1.1.0

Save concise, durable context without fragmenting memory stores or overwriting
user-owned records. Treat memory as persistent user data, not as a scratchpad.

## 1. Decide whether to save

- Honor explicit requests to remember or document information.
- Save proactively only after a significant completed milestone or durable
  decision whose verified result will materially help a future task. Announce
  the save before writing.
- Do not save routine progress, large transcript excerpts, tentative ideas, or
  facts that are already easy to recover from the repository.
- Do not save passwords, tokens, credentials, private contact details, health or
  financial data, or other sensitive information unless the user explicitly
  asks to retain that specific information and the destination is clear.
- Ask what to retain when the content or privacy boundary is ambiguous.
- Verify factual claims against the current task artifacts before persisting
  them. Label unresolved uncertainty instead of turning it into a durable fact.

## 2. Find the canonical memory root read-only

1. Inspect `~/.wlm/SOUL.md`. If its `## Memory` section names an existing
   canonical path, use that path.
2. Otherwise check these candidates and deduplicate their resolved paths:
   - `<current-working-directory>/memory`
   - `<git-repository-root>/memory`, only when a Git root exists
   - `~/.wlm/memory`
3. If exactly one candidate exists, use it.
4. If multiple distinct candidates exist without a valid canonical path, do not
   choose arbitrarily. Use `worker:consolidate-memory` or ask the user to select
   the destination.
5. If no store exists, ask where to create one for an explicit save and
   recommend `~/.wlm/memory` as the default. For a proactive save, do not create
   a new store without user approval.

Resolve this loaded skill's absolute directory, then use its bundled
`scripts/verify_memory.py` for deterministic, read-only discovery or validation
when useful. Do not resolve the script relative to the user's current project:

```text
python <skill-directory>/scripts/verify_memory.py
python <skill-directory>/scripts/verify_memory.py --memory-root <path>
```

The script never creates a store unless both `--memory-root` and `--create` are
provided.

## 3. Choose the narrowest location

Typical paths are:

| Scope | Path |
|---|---|
| Company-wide tools or conventions | `memory/corps/tools/` |
| Other company-wide context | `memory/corps/` |
| Project context | `memory/projects/<project-name>/` |
| Team context, including roles | `memory/teams/<team-name>/` |

Create only directories required for the entry; do not generate empty
scaffolding. Use stable, filesystem-safe lowercase names for new project or team
directories.

## 4. Merge instead of duplicating

1. Search filenames and contents for an existing record about the same topic.
2. Read the target file before editing it.
3. Append a dated section or make a minimal update when the existing file is
   canonical. Create a new dated file only when no suitable record exists.
4. Preserve unrelated content and formatting. Never replace a divergent file
   wholesale or silently resolve conflicting records.

## 5. Write a concise, attributable entry

Use the runtime's current date. Keep the entry to the smallest useful summary,
usually two to four sentences. Include:

- the durable outcome or decision;
- why it matters later;
- a repository path, commit, document, or other locator when one helps verify
  the claim;
- remaining constraints or uncertainty when material.

```markdown
# YYYY-MM-DD: [Topic]

[Verified outcome or decision, why it matters, and a useful source locator.]
```

Avoid copying secrets, unnecessary personal details, or ephemeral diagnostics.

## 6. Verify and report

- Reopen the changed file and confirm the intended text is present exactly once.
- If the memory root is in Git, inspect the scoped diff. Do not commit or push
  unless the user separately requested it.
- Report the changed path and a one-line summary. For proactive saves, make the
  persistent write explicit in the final response.

## Example

```markdown
# 2026-08-16: API migration decision

The backend team selected GraphQL for the Q2 migration; future API work should
follow the approved schema plan in `docs/api-migration.md`. Ownership remains
with the backend team until the rollout checklist is complete.
```
