---
name: rank-software-decisions
description: "Ranks software engineering options with an anonymized, blog-derived value pattern that favors reversibility, visible hidden costs, and survivable failure modes. Use when ranking architecture choices, implementation approaches, build-vs-buy decisions, tooling choices, dependency changes, migration plans, reliability tradeoffs, or AI/agent workflow decisions."
---

# Rank Software Decisions

Version: 1.1.0

Make software decisions in the source profile's style: concrete constraints
first, hidden cost next, then a practical ranking that preserves future options
and survives ordinary failure.

This is a decision aid. Explicit user direction, repo contracts, security
requirements, and production incident needs take precedence over it.

## Core Value Pattern

Rank higher the option that:

1. Preserves real options and avoids premature irreversible commitment.
2. Makes hidden costs visible: maintenance, coordination, proof burden,
   migration, operational support, documentation, and future debugging.
3. Survives ordinary teams and ordinary failure, not only the ideal engineer on
   the ideal day.
4. Uses repo-native conventions and boring proven tools unless novelty buys a
   real capability.
5. Converts ambiguity into evidence: tests, logs, metrics, docs, prototypes, or
   primary source reading.
6. Gives the user more agency, leverage, and freedom without pretending status
   or aesthetic neatness is the same as value.
7. Distinguishes luck, timing, and platform tailwinds from intrinsic technical
   quality.
8. Avoids moral or process theater when it raises cost and endangers the core
   work.

Rank lower the option that:

- Looks elegant but makes future work harder to inspect, operate, or reverse.
- Depends on high-context heroics, undocumented assumptions, or one person's
  taste.
- Optimizes a local metric while increasing system-level fragility.
- Creates coordination cost without buying a durable capability.
- Treats an LLM, framework, vendor, or architectural fashion as inevitable
  without checking the actual contract.

## Workflow

1. State the decision in one sentence.
2. List hard gates first: security, privacy, compliance, data loss risk,
   backwards compatibility, production safety, user-visible behavior, and repo
   ownership.
3. Identify the options, including "do nothing", "smaller patch", and "defer
   with evidence-gathering" when they are plausible.
4. Score each option qualitatively on:
   - Reversibility
   - Maintenance burden
   - Operational visibility
   - Fit with existing repo patterns
   - Blast radius
   - User/product value
   - Time-to-evidence
   - Long-term leverage
5. Name the hidden cost and worst boring failure mode for each serious option.
6. Recommend the top option and the smallest next step that proves or
   disproves it.

## Software-Specific Preferences

- Prefer scoped changes with docs and tests aligned over broad rewrites.
- Prefer explicit contracts at boundaries: API, data model, persistence,
  runtime lifecycle, CLI behavior, and user-facing states.
- Prefer observability and debuggability over cleverness.
- Add a dependency only when it removes real complexity or supplies a proven
  domain engine.
- Prefer migration paths that can pause, roll back, or coexist with old
  behavior.
- For AI/agent workflow choices, rank actual repeatability and verification
  above demo novelty.

## Output Shape

For non-trivial decisions, answer with:

- **Recommendation:** the top option.
- **Why This Wins:** the value pattern it satisfies.
- **Hidden Cost:** what is easy to underestimate.
- **Failure Mode:** the most likely boring way this goes wrong.
- **Next Step:** the smallest reversible action.

Keep uncertainty visible. If the evidence is thin, say what would change the
ranking.

## Evidence

These rules are distilled from an anonymized blog corpus, not invented
freehand. When the user asks why a value applies, or wants the source behind a
ranking, read [references/blog-evidence.md](references/blog-evidence.md) for
the cited passages.
