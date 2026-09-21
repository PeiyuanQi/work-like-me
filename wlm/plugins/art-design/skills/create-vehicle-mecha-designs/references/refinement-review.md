# Refinement and visual review

Use for revisions of an existing image, recurring visual defects, or a requested
comparison with a quality reference. This is an art-review workflow, not proof
of engineering feasibility, originality, or legal clearance.

## Establish the edit contract

- Inspect the current artifact and use the latest approved version as the base.
  Track accepted changes and rejected traits; do not silently fall back to an
  earlier design because it has a cleaner render.
- Assign each input a role: edit target, identity reference, finish reference,
  or material reference. Matching finish does not require copying a silhouette.
- Translate a local request into a visible target and invariants. Identify both
  subject-relative and image-relative sides when needed, such as the machine's
  left tool on image-right. For marked-up references, use the clean source for
  the edit when available and exclude the annotation from the output.
- Preserve approved architecture, pose, tools, palette, operator access,
  environment, and prior fixes unless the user changes them. Treat new feedback
  as cumulative rather than restarting the brief.
- State the intended change and proceed within the authorized scope. A request
  to inspect coverage calls for an inspection; edit when the user requests a
  fix or authorizes corrections if needed.

## Diagnose before increasing detail

Separate **geometry** (silhouette, joints, panel boundaries, rock outline),
**surface material** (paint, roughness, grain, wear), and **lighting** (reflection,
shading, contact and cast shadows). A defect in one does not justify replacing
the others. Do not misclassify intentional stylization as an artifact.

Review the full frame at viewing size for massing and hierarchy, then inspect
the actual available resolution, with detail views where supported. Scan armor,
bare metal, rubber, tools, support surfaces, ground, and background separately.
Report affected regions and severity; do not invent numerical coverage without
a defined measurement. A texture copied across unrelated materials is a useful
signal of a generated artifact.

- Keep real seams, bolts, ribs, bearing edges, cutting picks, and geological
  boundaries. Remove unwanted fine polygon networks, repeated cells, crackle,
  uniform speckling, and arbitrary facets inside otherwise continuous surfaces.
- Specify the replacement material positively: broad satin paint gradients,
  restrained directional metal sheen, matte rubber, or quiet diffuse stone.
  Keep wear at plausible contact points rather than coating every panel in it.
- For rocks, preserve the approved landform and biome. Removing surface noise
  need not round desert bedrock into river cobbles or turn natural rock into
  visibly tessellated clay. Broad fractures and sparse natural grain can remain
  when they support the requested realism; a plain surface is appropriate when
  the user explicitly asks to remove texture.
- Keep mechanical complexity in purposeful assemblies. More scratches, lights,
  micro-panels, and exposure do not substitute for a readable mounting and
  motion path.

## Perspective, grounding, and lighting

Check camera and horizon consistency, coherent foreshortening of parallel forms
and shared shafts, joint clearances, overlap, support contact, and apparent
weight. Different articulated parts can legitimately have different angles;
do not force them onto one vanishing point or redesign a coherent pose.

Identify the intended key light, ambient fill, bounce, and practical lights.
Check their combined effect on metal, paint, stone, and ground: highlights need
not match across materials, but unexplained uniform rim light is suspect.
Contact shadows should anchor feet and tools; cast shadows must agree with the
dominant source and terrain. Control lamp bloom and background contrast without
crushing joint detail. Preserve clean materials during a relighting pass.

## Iterate from evidence

Use the available image editor for a scoped correction. Keep the requested
finish and material distinctions; a blanket blur or unrequested flat shader can
hide artifacts while degrading the design. Inspect the returned artifact before
claiming the change succeeded, including untouched regions for regression.

When the same defect survives a focused edit, change the method rather than
repeating a longer list of adjectives: tighten the target region, isolate a
material pass, use an appropriate clean reference, or use a supported mask or
retouch workflow within the user's tool constraints. Treat generated reference
images as generated, even when they look photographic. Do not claim they are
real photographs or that text-only preservation instructions ensure identical
pixels. Do not silently switch to an unavailable or unauthorized editing path.

If the defect remains or a tool limit prevents work, say what remains. Do not
call a partial improvement fixed, spend retries with no changed strategy, or
overwrite the last approved version. Save the selected result non-destructively
and link the artifact actually inspected.

## Blind comparison when requested

Use independent reviewers only when the user requests or otherwise authorizes
that workflow. Agree on or state a reasonable meaning of “close” before seeing
scores; for example a panel-mean difference within 0.5 on a 10-point scale, with
an individual-deficit limit. The example is not a universal target.

- Give reviewers the same rubric and comparable image presentation. For blind
  review, use neutral filenames and fresh context; withhold origin labels,
  desired winner, prior scores, suspected defects, and stopping target. Vary
  presentation order when useful. Do not claim visual familiarity is eliminated.
- Separate finish quality from likeness and brief compliance. Useful quality
  criteria include silhouette/readability, mechanical coherence, detail
  hierarchy, material rendering, and composition/lighting. Preserve explicit
  design requirements even if a different design might score higher.
- Record per-image scores and visible evidence from every reviewer; compute
  aggregates consistently, without selecting favorable reviews or moving the
  target after results. Revise concrete weaknesses, then compare the actual
  revision against the same reference using fresh blind context.
- Verify the final saved artifact is the one reviewed. Later edits invalidate
  the old result for that new version. Report remaining weaknesses, subjective
  reviewer variation, and the limits of an AI panel; scores do not certify
  commercial use or physical performance.
