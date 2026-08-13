---
name: adhd-friendly-technical-writing
description: Use only when the user asks for ADHD-friendly wording or explicitly invokes i-have-adhd for software engineering or technical text, such as implementation steps, debugging guidance, code reviews, incident updates, architecture notes, technical documentation, or developer handoffs. Do not use for general office writing, creative prose, personal communication, marketing, or non-technical text.
---

# ADHD-Friendly Technical Writing

Version: 1.1.0

This is a work-like-me adapter for the third-party skill
`ayghri/i-have-adhd`, scoped to engineering and technical communication.

## Source

- Upstream: `https://github.com/ayghri/i-have-adhd`
- Upstream skill: `skills/i-have-adhd/SKILL.md`
- Pinned commit: `2ed064090711586e0c97a2fbbf15465fe8f1808b`
- Upstream plugin version at the pinned commit: `0.1.0`
- Use mode: `wrapper`
- License: MIT, copyright 2026 Ayoub Ghriss
- Local content policy: this wrapper references the upstream skill but does not
  vendor its skill text, scripts, hooks, assets, or examples

## Required Activation Conditions

Use this skill only when both conditions are true:

1. The user explicitly requests ADHD-friendly wording, invokes
   `i-have-adhd`, or asks for the equivalent action-first and low-tangent
   structure.
2. The text is engineering or technical work.

Qualifying technical text includes:

- implementation plans and executable development steps
- debugging, testing, deployment, migration, and operational instructions
- code-review feedback and pull-request or issue summaries
- incident, reliability, security, and technical status updates
- architecture notes, API descriptions, technical documentation, and developer
  handoffs

Do not activate this skill for general office writing, emails unrelated to
technical work, personal messages, creative writing, marketing copy, medical
advice, or other non-technical prose. Do not infer a medical diagnosis or
activate it merely because the user asks for brevity.

## Workflow

1. Confirm from the request that the output is both explicitly ADHD-shaped and
   technical. If either condition is absent, use the normal relevant skill.
2. Load and follow the installed upstream `i-have-adhd` skill first when it is
   available, then apply the local technical-writing rules below.
3. Treat activation as scoped to the current response or technical work
   session. Do not edit user configuration or persist health-related
   information unless the user explicitly asks.
4. Preserve safety checks, required tool-call updates, technical completeness,
   evidence, commands, paths, and verification results. Change the information
   architecture, not the engineering rigor.
5. If the upstream skill is unavailable, use the fallback below and say that
   the exact upstream rules were not loaded.

## Technical-Writing Rules

- Lead with the engineering result or next executable technical action.
- Use numbered steps for multi-step work, with one bounded operation per step.
- Keep commands, file paths, errors, expected results, and verification criteria
  adjacent to the step where they are needed.
- Keep active state visible across turns: what passed, what failed, what remains,
  and the single next technical action.
- Separate optional improvements and unrelated findings from the critical path.
- Use concrete estimates only when useful and supportable; do not invent false
  precision.
- Do not remove necessary explanation when the user asks for a design rationale,
  review, diagnosis, or technical walkthrough.

## Fallback When Upstream Is Missing

Use the technical-writing rules above as a safe approximation. Do not claim
that the upstream skill, its hooks, or its full session-persistence behavior is
active. If the user wants the exact upstream behavior, point them to the source
and ask whether to install it.
