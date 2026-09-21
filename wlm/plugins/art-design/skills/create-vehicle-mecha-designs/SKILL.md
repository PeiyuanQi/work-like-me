---
name: create-vehicle-mecha-designs
description: Create or art-direct vehicles, spacecraft, industrial machines, mecha, robots, and hard-surface mobility concepts. Use when the user needs a readable design sheet, hero render, functional machine concept, scale exploration, mechanical silhouette, or image-generation prompt grounded in plausible construction and use.
---

# Create Vehicle and Mecha Designs

Read [references/style-profile.md](references/style-profile.md) before composing a prompt or generating an image. Use the profile as a visual grammar, not as permission to copy any artist, project, composition, character, logo, or protected mark from the source archive.

For iterative edits, recurring visual defects, or a requested reference-quality review, also read [references/refinement-review.md](references/refinement-review.md). It covers preserving approved designs, material cleanup, perspective and lighting checks, and blind comparison when requested.

## Workflow

1. Infer the deliverable: finished image, prompt, art-direction brief, variation sheet, production concept, or edit of an attached image. Proceed with sensible defaults when the request is clear; ask only for missing information that prevents the requested result.
2. Set output constraints: aspect ratio, pixel size, crop, transparency, text-safe space, target viewing distance, and whether multiple views or states are required.
3. Select one production mode from the style profile and state the image's subject, action, function, environment, and emotional beat.
4. Build the prompt in this order: intent, composition, form/structure, materials, lighting, palette, technique, production constraints, then avoidance instructions.
5. When an image-generation or image-editing tool is available and the user requests a finished visual, use it directly; do not stop after writing a prompt.
6. Inspect the actual result against the profile's quality checks and the user's accumulated requirements. Review both the changed region and the whole image after each edit; a prompt requesting preservation does not prove that the output preserved it.

## Originality and Rights

- Abstract reusable traits such as composition, shape language, material handling, edge control, lighting, and workflow.
- Do not name a living artist as the requested style. Translate references into observable visual properties.
- Do not reproduce archived images, signatures, watermarks, project names, or exact compositions.
- Use recognizable characters, franchises, logos, or protected symbols only when the user explicitly requests them and the applicable image policy allows it; otherwise create original equivalents.
- Separate a reference's design identity from its rendering-quality role. For an original homage, develop distinct primary forms and mechanisms; a recolor or new background is not evidence of independence. Do not promise commercial or open-source clearance from visual differences or reviewer scores.
- Do not commit or redistribute the source archive media as skill assets.

## Response Format

For a finished image or edit, return the visual and a concise account of verified changes or remaining defects. Keep prompt records available when useful; do not substitute a prompt package for the requested image.

For a prompt, brief, or production specification, return:

1. **Direction** — one sentence naming the production mode and visual objective.
2. **Specifications** — aspect ratio/size, composition, camera, lighting, palette, materials, and required variants.
3. **Generation prompt** — ready to use, concrete, and free of artist-name imitation.
4. **Avoidance prompt** — concise failure modes and protected elements to omit.
5. **Iteration notes** — 2-4 specific changes to try after the first result.
