---
name: create-creatures-animals
description: Create or art-direct believable creatures, stylized animals, monsters, wildlife, mounts, and creature-character hybrids. Use when the user wants creature concept art, anatomy exploration, a creature portrait, ecological worldbuilding, animal illustration, or an image-generation prompt grounded in locomotion, habitat, behavior, and material anatomy.
---

# Create Creatures and Animals

Read [references/style-profile.md](references/style-profile.md) before composing a prompt or generating an image. Use the profile as a visual grammar, not as permission to copy any artist, project, composition, character, logo, or protected mark from the source archive.

## Workflow

1. Infer the deliverable from the request: finished image, prompt, art-direction brief, variation sheet, production concept, or edit of an attached image. When a finished visual is requested and the required source image is available, proceed directly without asking for confirmation.
2. Apply stated output constraints: aspect ratio, pixel size, crop, transparency, text-safe space, target viewing distance, and whether multiple views or states are required. Choose sensible defaults for optional details instead of pausing generation.
3. Select one production mode from the style profile and state the image's subject, action, function, environment, and emotional beat.
4. Build the prompt in this order: intent, composition, form/structure, materials, lighting, palette, technique, production constraints, then avoidance instructions.
5. When an image-generation or image-editing tool is available and the user requests a finished visual, use it directly; do not stop after writing a prompt.
6. Review the first result against the profile's quality checks. Iterate with focused edits instead of replacing the whole direction at once.

## Originality and Rights

- Abstract reusable traits such as composition, shape language, material handling, edge control, lighting, and workflow.
- Do not name a living artist as the requested style. Translate references into observable visual properties.
- Do not reproduce archived images, signatures, watermarks, project names, or exact compositions.
- Use recognizable characters, franchises, logos, or protected symbols only when the user explicitly requests them and the applicable image policy allows it; otherwise create original equivalents.
- Do not commit or redistribute the source archive media as skill assets.

## Response Format

For prompts, briefs, and production concepts, return:

1. **Direction** — one sentence naming the production mode and visual objective.
2. **Specifications** — aspect ratio/size, composition, camera, lighting, palette, materials, and required variants.
3. **Generation prompt** — ready to use, concrete, and free of artist-name imitation.
4. **Avoidance prompt** — concise failure modes and protected elements to omit.
5. **Iteration notes** — 2-4 specific changes to try after the first result.

For a finished image generation or edit, return the generated result directly. Add only an essential limitation or usage note when needed; do not summarize the image unless the user asks.
