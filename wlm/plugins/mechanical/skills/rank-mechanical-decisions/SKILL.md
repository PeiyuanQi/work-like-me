---
name: rank-mechanical-decisions
description: Use when ranking mechanical, hardware, physical build, repair, tool, material, regulated-device, radio, vehicle, firearm-adjacent, maker, 3D printing, workshop, or hands-on engineering choices according to an anonymized blog-derived decision-making and value pattern.
---

# Rank Mechanical Decisions

Version: 1.0.0

Use this skill for tangible systems where choices touch materials, tools,
assembly, safety, regulations, repairability, or physical failure. This skill is
a decision workflow, not professional engineering, legal, firearms, radio,
medical, or safety advice.

## Core Value Pattern

Rank higher the option that:

1. Keeps people safe and stays inside applicable law, licensing, and operating
   rules.
2. Works under real material, tool, tolerance, operator-skill, and environment
   constraints.
3. Preserves the ability to inspect, repair, replace, and retry.
4. Uses proven off-the-shelf parts before custom fabrication unless the custom
   part solves a real constraint.
5. Tests the risky assumption cheaply before committing the whole build.
6. Makes failure modes visible: leaks, heat, load paths, power draw, recoil,
   interference, corrosion, wear, and user error.
7. Values "good enough and understood" over expensive or elegant parts that do
   not address the actual bottleneck.
8. Records the mistake path so future attempts avoid the same trap.

Rank lower the option that:

- Looks professional but hides the real short board.
- Requires skill, tooling, or compliance knowledge the user does not yet have.
- Creates a dangerous, illegal, or hard-to-debug failure mode.
- Optimizes aesthetics or theoretical strength while ignoring the actual load,
  seal, heat, power, or control path.
- Makes repair impossible after the first failure.

## Workflow

1. State the physical decision and the operating context.
2. List hard gates: safety, legality, licensing, environment, budget, tool
   access, materials, and irreversible damage risk.
3. Identify the critical function: hold load, seal water, move smoothly, stop
   safely, communicate, power reliably, survive heat, or be maintained.
4. Rank each option qualitatively on:
   - Safety margin
   - Legal/licensing confidence
   - Fit with available tools and skill
   - Failure visibility
   - Repairability
   - Cost-to-test
   - Parts availability
   - Maintenance burden
   - Reversibility
5. Recommend the most robust path and the cheapest test that exercises the risky
   assumption.

## Mechanical-Specific Heuristics

- When a system fails, find the actual short board before reinforcing the part
  that is easiest to redesign.
- For regulated devices, verify current rules from official or expert sources
  before buying parts or operating.
- For radio, firearms, vehicles, power tools, pressure, heat, batteries, or
  structural loads, treat safety and licensing as gates, not ranking factors.
- Prefer simple inspection and field repair over sealed cleverness.
- When documentation is scarce, write down the parts, constraints, mistakes,
  and workaround path as part of the result.

## Output Shape

- **Recommendation:** the top-ranked option.
- **Hard Gates:** safety/legal/tool constraints to verify first.
- **Why This Wins:** the practical value pattern it satisfies.
- **Hidden Cost:** material, tool, compliance, or maintenance cost.
- **Failure Mode:** the most likely physical way it breaks.
- **Cheap Test:** the smallest experiment before full commitment.

## Blog Evidence Anchors

These rules are distilled from an anonymized blog corpus, not invented
freehand. Keep citations relative to the source blog repository so the public
skill stays rooted in evidence without exposing a local username or home path.

- Physical projects need real material and tool constraints, not idealized
  tutorials: `rc-1.md` records that a simple-looking RC sailboat build hid many
  material, cutting, adhesive, heat, and tooling traps
  (`source/_posts/rc-1.md:24`, `source/_posts/rc-1.md:34`,
  `source/_posts/rc-1.md:36`, `source/_posts/rc-1.md:38`,
  `source/_posts/rc-1.md:40`, `source/_posts/rc-1.md:42`).
- Rank the actual bottleneck over the part that is fun to redesign:
  `rc-1.md` shows fiberglass that looked good but leaked, an oversized floating
  rudder that broke the boat's function, and an overbuilt stabilizing block that
  was not the real short board
  (`source/_posts/rc-1.md:48`, `source/_posts/rc-1.md:50`,
  `source/_posts/rc-1.md:57`, `source/_posts/rc-1.md:73`,
  `source/_posts/rc-1.md:79`).
- Test the real system and record the failure path: `rc-1.md` notes a leak test
  that missed the rudder and later failures from servo damage and wire melt
  (`source/_posts/rc-1.md:91`, `source/_posts/rc-1.md:135`,
  `source/_posts/rc-1.md:147`).
- Regulated devices require current rules, licensing, and official sources:
  `ham-1.md` starts with license classes and FCC identity, while
  `gun-ar-assemble-ca.md` repeatedly emphasizes changing laws and direct penal
  code reading
  (`source/_posts/ham-1.md:16`, `source/_posts/ham-1.md:20`,
  `source/_posts/ham-1.md:22`, `source/_posts/gun-ar-assemble-ca.md:18`,
  `source/_posts/gun-ar-assemble-ca.md:102`,
  `source/_posts/gun-ar-assemble-ca.md:103`).
- Rank safety and operator skill as gates: `gun-ar-assemble-ca.md` compares home
  defense options by training difficulty, over-penetration, legal constraints,
  and scenario fit, then rejects a simple universal ranking
  (`source/_posts/gun-ar-assemble-ca.md:29`,
  `source/_posts/gun-ar-assemble-ca.md:30`,
  `source/_posts/gun-ar-assemble-ca.md:78`,
  `source/_posts/gun-ar-assemble-ca.md:81`,
  `source/_posts/gun-ar-assemble-ca.md:85`,
  `source/_posts/gun-ar-assemble-ca.md:89`).
