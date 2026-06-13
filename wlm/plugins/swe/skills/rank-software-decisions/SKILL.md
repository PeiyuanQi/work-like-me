---
name: rank-software-decisions
description: Use when ranking software engineering options, architecture choices, implementation approaches, build-vs-buy decisions, tooling choices, dependency changes, migration plans, reliability tradeoffs, or AI/agent workflow decisions according to an anonymized blog-derived decision-making and value pattern.
---

# Rank Software Decisions

Version: 1.0.0

Use this skill to make software decisions in the source profile's style: concrete
constraints first, hidden cost next, then a practical ranking that preserves
future options and survives ordinary failure.

This is a decision aid, not a rule that overrides explicit user direction,
repo contracts, security requirements, or production incident needs.

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
6. Recommend the top option and the smallest next step that proves or disproves
   it.

## Software-Specific Preferences

- Prefer scoped changes with docs and tests aligned over broad rewrites.
- Prefer explicit contracts at boundaries: API, data model, persistence,
  runtime lifecycle, CLI behavior, and user-facing states.
- Prefer observability and debuggability over cleverness.
- Prefer dependency additions only when they remove real complexity or supply a
  proven domain engine.
- Prefer migration paths that can pause, rollback, or coexist with old behavior.
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

## Blog Evidence Anchors

These rules are distilled from an anonymized blog corpus, not invented
freehand. Keep citations relative to the source blog repository so the public
skill stays rooted in evidence without exposing a local username or home path.

- Preserve optionality before committing: `thoughts-14.md` compares career
  choices to a game where early moves close off future hands, and values delaying
  commitment until more paths remain possible
  (`source/_posts/thoughts-14.md:17`, `source/_posts/thoughts-14.md:21`,
  `source/_posts/thoughts-14.md:25`).
- Do not confuse process or moral theater with execution: `2019-Resolutions.md`
  explicitly names decision failure from ignoring cost, over-focusing on form,
  and raising the risk of core-work failure
  (`source/_posts/2019-Resolutions.md:20`,
  `source/_posts/2019-Resolutions.md:22`,
  `source/_posts/2019-Resolutions.md:23`).
- Separate luck, timing, and system durability from intrinsic quality:
  `thoughts-66.md` contrasts lucky success with durable survival, systems that
  reduce individual variance, and information gaps in choice-making
  (`source/_posts/thoughts-66.md:19`, `source/_posts/thoughts-66.md:21`,
  `source/_posts/thoughts-66.md:33`, `source/_posts/thoughts-66.md:39`,
  `source/_posts/thoughts-66.md:59`).
- Read the real contract and evidence before trusting convenient proposals:
  `cs-grpc-eks.md` traces a failed gRPC/EKS path to shallow understanding of
  NIC/TLS behavior, ignoring example code, and trusting advice from people who
  were not actually experienced in that part
  (`source/_posts/cs-grpc-eks.md:45`,
  `source/_posts/cs-grpc-eks.md:49`,
  `source/_posts/cs-grpc-eks.md:59`,
  `source/_posts/cs-grpc-eks.md:71`,
  `source/_posts/cs-grpc-eks.md:79`).
- Prefer dynamic evidence over static allocation when conditions change:
  `cs-robinhood-tail-latency.md` emphasizes that tail latency changes with many
  factors and uses observed request latency / blocking counts to reallocate
  cache
  (`source/_posts/cs-robinhood-tail-latency.md:42`,
  `source/_posts/cs-robinhood-tail-latency.md:44`,
  `source/_posts/cs-robinhood-tail-latency.md:46`,
  `source/_posts/cs-robinhood-tail-latency.md:50`).
