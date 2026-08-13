---
name: adhd-friendly-wording
description: Use when the user asks for ADHD-friendly wording, action-first output, shorter executable answers, numbered steps, fewer tangents, visible progress, or explicitly names i-have-adhd. Activate only for the current session or response unless the user asks for a persistent preference.
---

# ADHD-Friendly Wording

Version: 1.0.0

This is a work-like-me adapter for the third-party skill
`ayghri/i-have-adhd`.

## Source

- Upstream: `https://github.com/ayghri/i-have-adhd`
- Upstream skill: `skills/i-have-adhd/SKILL.md`
- Pinned commit: `2ed064090711586e0c97a2fbbf15465fe8f1808b`
- Upstream plugin version at the pinned commit: `0.1.0`
- Use mode: `wrapper`
- License: MIT, copyright 2026 Ayoub Ghriss
- Local content policy: this wrapper references the upstream skill but does not
  vendor its skill text, scripts, hooks, assets, or examples

## When To Use

- The user explicitly asks for ADHD-friendly wording or invokes
  `i-have-adhd`.
- The user asks for answers that are action-first, easy to scan, broken into
  bounded steps, low in tangents, and explicit about progress.
- The user asks to rewrite an existing answer into a more executable shape.

Do not infer a medical diagnosis or activate this merely because a user asks
for brevity. Ordinary concise-writing requests should follow the normal style
unless the user asks for this specific mode.

## Workflow

1. Load and follow the installed upstream `i-have-adhd` skill first when it is
   available. Apply the local rules below after the upstream rules.
2. Treat activation as scoped to the current response or session. Do not write
   an always-on preference, edit user configuration, or persist health-related
   information unless the user explicitly asks.
3. Preserve safety checks, required tool-call updates, requested explanations,
   and task-complete technical detail. ADHD-friendly wording changes the shape
   of the answer, not the correctness bar.
4. If the upstream skill is unavailable, use the fallback below and say that
   the exact upstream rules were not loaded.

## Local Overrides

- Lead with the result or next concrete action.
- Use a numbered list for multi-step work, with one bounded action per step.
- Keep the active state visible across turns: what is done, what remains, and
  the single next action.
- Separate optional tangents from the main path.
- Use concrete estimates only when useful and supportable; do not invent false
  precision.
- End without generic pleasantries or multiple competing next steps.

## Fallback When Upstream Is Missing

Use the local overrides above as a safe approximation. Do not claim that the
upstream skill, its hooks, or its full session-persistence behavior is active.
If the user wants the exact upstream behavior, point them to the source and ask
whether to install it.
