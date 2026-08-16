---
name: create-3d-sculpture-models
description: Plan or art-direct 3D sculpture, character models, hard-surface models, props, vehicles, materials, grooming, texturing, and presentation renders. Use when the user wants a production-ready 3D workflow, game-ready or printable mesh brief, topology/UV/baking/LOD/export plan, sculpt or modeling breakdown, texture/render direction, turnaround, portfolio presentation, or image-generation reference for a model that must work beyond one camera angle.
---

# Create 3D Sculpture and Models

Read [references/style-profile.md](references/style-profile.md) before composing a prompt or generating an image. Use the profile as a visual grammar, not as permission to copy any artist, project, composition, character, logo, or protected mark from the source archive.

## Workflow

1. Identify the deliverable: raster concept/reference, prompt, art-direction brief, production workflow, mesh specification, variation sheet, presentation render, or edit of an attached image. Infer obvious requirements from context and ask only for missing constraints that would materially change the result.
2. For a raster deliverable, set aspect ratio, pixel size, crop, transparency, text-safe space, target viewing distance, and required views. For a 3D asset brief, set use case, real-world scale and units, target DCC/engine or print process, geometry and texture budgets, topology/rig/groom needs, LODs, and export formats.
3. Select one production mode from the style profile and state the image's subject, action, function, environment, and emotional beat.
4. For a visual reference, build the prompt in this order: intent, composition, form/structure, materials, lighting, palette, technique, production constraints, then avoidance instructions. For a production workflow, define blockout and turntable approval, secondary forms, retopology, UVs, baking, texturing, grooming/rigging when applicable, LOD/export, and acceptance checks.
5. When an image-generation or image-editing tool is available and the user requests a finished visual or visual reference, use it directly; do not stop after writing a prompt. Treat generated raster images as concept or presentation references, not as usable mesh files, unless a real 3D-generation tool produced and verified the requested asset.
6. Review the first result against the profile's quality checks. Iterate with focused edits instead of replacing the whole direction at once.

## Originality and Rights

- Abstract reusable traits such as composition, shape language, material handling, edge control, lighting, and workflow.
- Do not name a living artist as the requested style. Translate references into observable visual properties.
- Do not reproduce archived images, signatures, watermarks, project names, or exact compositions.
- Use recognizable characters, franchises, logos, or protected symbols only when the user explicitly requests them and the applicable image policy allows it; otherwise create original equivalents.
- Do not commit or redistribute the source archive media as skill assets.

## Response Format

For a visual or prompt request, return:

1. **Direction** — one sentence naming the production mode and visual objective.
2. **Specifications** — aspect ratio/size, composition, camera, lighting, palette, materials, and required variants.
3. **Generation prompt** — ready to use, concrete, and free of artist-name imitation.
4. **Avoidance prompt** — concise failure modes and protected elements to omit.
5. **Iteration notes** — 2-4 specific changes to try after the first result.

For a production workflow or mesh brief, return:

1. **Asset target** — use case, scale, platform/process, and viewing distance.
2. **Technical specification** — geometry, topology, UVs, textures/materials, rig/groom, LODs, and exports.
3. **Production stages** — ordered milestones with review gates.
4. **Deliverables** — source files, interchange files, texture sets, turntable, and diagnostic views.
5. **Acceptance checks** — concrete tests for silhouette, deformation or printability, shading, materials, scale, and export integrity.
