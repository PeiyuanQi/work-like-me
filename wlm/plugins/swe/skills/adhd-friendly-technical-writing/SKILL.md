---
name: adhd-friendly-technical-writing
description: "Restructures engineering and technical text to lead with the result or next action and keep steps short and executable. Use only when the user explicitly asks for ADHD-friendly, action-first, or i-have-adhd wording for technical content such as implementation steps, debugging guidance, code reviews, incident updates, architecture notes, technical docs, or developer handoffs. Not for non-technical, office, creative, personal, or marketing text, or a plain request for brevity."
---

# ADHD-Friendly Technical Writing

Version: 2.1.0

Shape engineering and technical text so the reader can act without digging the
next step out of a wall of context. This skill is locally owned and complete; it
does not load or depend on another installed skill.

Adapted from `ayghri/i-have-adhd` under the MIT License. Work-like-me narrows
the behavior to explicitly requested engineering and technical communication.
See `THIRD_PARTY_NOTICES.md` for attribution and license terms.

## Activation Boundary

Apply this skill only when both conditions hold:

1. The user explicitly asks for ADHD-friendly wording, action-first wording,
   low-tangent structure, or `i-have-adhd` behavior.
2. The requested text is engineering or technical work:
   - implementation plans and executable development steps
   - debugging, testing, deployment, migration, and operational instructions
   - code-review feedback and pull-request or issue summaries
   - incident, reliability, security, and technical status updates
   - architecture notes, API descriptions, technical documentation, and
     developer handoffs

Keep normal wording for general office writing, non-technical email, personal
messages, creative writing, marketing copy, medical advice, and other
non-technical prose. A request for brevity alone is not an activation signal,
and the request never implies a diagnosis.

## Session Scope

Apply the style to the current response. When the user asked for it as a mode,
keep applying it for the rest of the same technical task, until the user asks
for normal wording or the task becomes non-technical.

Edit user configuration or save health-related preferences only when the user
explicitly asks for persistence, because the preference is personal health
information.

## Core Rules

1. **Lead with the result or action.** The first line states the engineering
   result or the next executable technical action, not background, a plan
   announcement, praise, or a preview of the answer. When the answer is a
   command, path, error, decision, or code change, put that item first and add
   only the context needed to execute or evaluate it.
2. **Make multi-step work executable.** Use a numbered list for multiple steps.
   Each step holds one bounded operation and its immediate verification, with
   the command, file path, expected output, and failure signal next to it. Split
   any step that chains several hidden actions with "and then".
3. **Keep the critical path short.** Include the fewest steps that safely reach
   the requested outcome. Put optional improvements, unrelated findings, and
   future cleanup in a separate section after the critical path, and include
   that section only when it helps the current decision.
4. **Restate operational state across turns.** For ongoing work, show what
   passed or is complete, what failed or remains uncertain, what remains, and
   the single next technical action. If the harness provides a task or plan
   tool, keep multi-step state there instead of repeating the full checklist in
   prose.
5. **End with one next action.** When work remains, end with one concrete
   action the reader can perform or approve, rather than competing options or a
   generic offer to help. When the task is complete, end with the verified
   result instead of a long recap.
6. **Use concrete technical evidence.** Prefer exact commands, paths, line
   references, error messages, test names, status values, and verification
   criteria over vague descriptions. Give time estimates only when useful and
   supportable, and state the assumptions that materially affect them rather
   than inventing precision.
7. **Make progress visible.** State completed technical outcomes directly:
   which behavior now works, which check passed, which artifact changed, or
   which remote state is aligned, instead of burying the result in process
   narration.
8. **Report failures matter-of-factly:** where it failed, the observed result,
   the supported cause or current hypothesis (labeled as a hypothesis), and the
   next diagnostic or fix. Leave out emotional filler.
9. **Keep lists scannable.** Aim for five items or fewer per list. When more
   are necessary, group them by execution priority, such as "do now" and
   "later", or by technical layer.
10. **Cut non-functional prose:** preambles, repeated recaps, generic closing
    pleasantries, unnecessary hedging, idioms, and sidebars that don't change
    the reader's action or decision. Keep uncertainty language when it
    accurately communicates risk.

## Engineering Rigor Overrides Wording Style

The style changes information architecture, not the verification bar. Keep
everything required for correctness, safety, or informed review:

- destructive-action confirmations and rollback steps
- security, privacy, legal, and operational warnings
- evidence, assumptions, limitations, and unresolved risks
- requested design rationale, diagnosis, review detail, or walkthroughs
- repository-required progress updates and tool-call narration

## When To Pause The Format

- If the request is materially ambiguous, ask one concise question instead of
  guessing.
- After three consecutive failed attempts, stop repeating fixes, say which core
  assumption may be wrong, and request or run one discriminating diagnostic.
- If the user asks for options, give a small ranked set with the recommended
  choice first instead of forcing a single path.
- If the task needs a full explanation, keep it complete but organize it with
  descriptive headings and an action-first opening.

## Pre-Send Check

Before sending, confirm:

1. The request explicitly called for this wording style.
2. The content is engineering or technical.
3. The first line gives the result or next action.
4. Commands, paths, errors, and checks appear where they are needed.
5. If work remains, the final line identifies one next action.
