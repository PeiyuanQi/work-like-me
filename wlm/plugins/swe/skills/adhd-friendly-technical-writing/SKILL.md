---
name: adhd-friendly-technical-writing
description: Use only when the user explicitly asks for ADHD-friendly wording, action-first wording, or i-have-adhd behavior for software engineering or technical text, including implementation steps, debugging guidance, code reviews, incident updates, architecture notes, technical documentation, and developer handoffs. Do not use for general office writing, creative prose, personal communication, marketing, or non-technical text.
---

# ADHD-Friendly Technical Writing

Version: 2.0.0

Shape engineering and technical text so the reader can act without extracting
the next step from a wall of context. This skill is locally owned and complete;
it does not load or depend on another installed skill.

Adapted from `ayghri/i-have-adhd` under the MIT License. Work-like-me narrows
the behavior to explicitly requested engineering and technical communication.
See `THIRD_PARTY_NOTICES.md` for attribution and license terms.

## Activation Boundary

Use this skill only when both conditions are true:

1. The user explicitly asks for ADHD-friendly wording, action-first wording,
   low-tangent structure, or `i-have-adhd` behavior.
2. The requested text is engineering or technical work.

Qualifying text includes:

- implementation plans and executable development steps
- debugging, testing, deployment, migration, and operational instructions
- code-review feedback and pull-request or issue summaries
- incident, reliability, security, and technical status updates
- architecture notes, API descriptions, technical documentation, and developer
  handoffs

Do not activate this skill for general office writing, non-technical email,
personal messages, creative writing, marketing copy, medical advice, or other
non-technical prose. Do not infer a diagnosis or activate it merely because the
user asks for brevity.

## Session Scope

Apply this skill to the current response. Continue applying it during the same
technical task when the user clearly asked for a mode, until the user requests
normal wording or changes to a non-technical task.

Do not edit user configuration or save health-related preferences unless the
user explicitly asks for persistence.

## Core Rules

### 1. Lead With The Result Or Action

The first line should state the engineering result or the next executable
technical action. Do not begin with background, a plan announcement, praise,
or a summary of what the answer will contain.

When the answer is a command, path, error, decision, or code change, put that
item first. Add only the context needed to execute or evaluate it.

### 2. Make Multi-Step Work Executable

Use a numbered list when work has multiple steps. Each step should contain one
bounded operation and its immediate verification.

Keep commands, file paths, expected output, and failure signals adjacent to the
step where the reader needs them. Avoid steps that contain several hidden
actions joined by repeated "and then" clauses.

### 3. Keep The Critical Path Short

Include the fewest steps that safely complete the requested technical outcome.
Move optional improvements, unrelated findings, and future cleanup into a
separate section after the critical path, and include that section only when it
helps the current decision.

### 4. Restate Operational State Across Turns

For ongoing technical work, make the current state visible:

- what passed or is complete
- what failed or remains uncertain
- what remains
- the single next technical action

If the harness provides a task or plan tool, use it for multi-step state and do
not duplicate the full checklist in prose.

### 5. End With One Next Action

When work remains, end with one concrete action the reader can perform or
approve. Do not end with multiple competing options or generic offers to help.

When the task is complete, end with the verified result rather than repeating a
long recap.

### 6. Use Concrete Technical Evidence

Prefer exact commands, paths, line references, error messages, test names,
status values, and verification criteria over vague descriptions.

Use time estimates only when useful and supportable. State the assumptions that
materially affect the estimate; do not invent precision.

### 7. Make Progress Visible

State completed technical outcomes directly: which behavior now works, which
check passed, which artifact changed, or which remote state is aligned. Do not
bury the result inside process narration.

### 8. Describe Failures Matter-Of-Factly

For a failure, state:

1. where it failed
2. the observed result
3. the supported cause or current hypothesis
4. the next diagnostic or fix

Avoid emotional filler. Distinguish confirmed causes from hypotheses.

### 9. Keep Lists Scannable

Prefer no more than five items in one list. When more are necessary, group them
by execution priority, such as "do now" and "later," or by technical layer.

### 10. Remove Non-Functional Prose

Delete preambles, repeated recaps, generic closing pleasantries, unnecessary
hedging, idioms, and sidebars that do not change the reader's action or
decision. Keep uncertainty language when it accurately communicates risk.

## Engineering Rigor Overrides Wording Style

Do not shorten away information required for correctness, safety, or informed
review. Preserve:

- destructive-action confirmations and rollback steps
- security, privacy, legal, and operational warnings
- evidence, assumptions, limitations, and unresolved risks
- requested design rationale, diagnosis, review detail, or walkthroughs
- repository-required progress updates and tool-call narration

The style changes information architecture, not the verification bar.

## When To Pause The Format

- If the request is materially ambiguous, ask one concise question instead of
  guessing.
- If three consecutive attempts fail, stop repeating fixes, state which core
  assumption may be wrong, and request or run one discriminating diagnostic.
- If the user requests options, provide a small ranked set with the recommended
  choice first instead of forcing a single path.
- If the task requires a full explanation, keep the explanation complete but
  organize it with descriptive headings and an action-first opening.

## Pre-Send Check

Before sending, verify:

1. The request explicitly called for this wording style.
2. The content is engineering or technical.
3. The first line gives the result or next action.
4. Commands, paths, errors, and checks appear where they are needed.
5. If work remains, the final line identifies one next action.
