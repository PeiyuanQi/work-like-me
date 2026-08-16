---
name: create-mixed-style-art
description: Create or art-direct intentionally hybrid visual work that combines two or more art directions, media languages, or production techniques into one coherent result. Use when no single Art Design category fits, the user requests a mixed-media or cross-genre image, or a project needs a controlled blend such as painterly plus graphic, 2D plus 3D, architectural plus character, or realistic plus stylized.
---

# Create Mixed Style Art

Read [references/style-profile.md](references/style-profile.md) before composing a prompt or generating an image. Use the profile as a visual grammar, not as permission to copy any artist, project, composition, character, logo, or protected mark from the source archive.

## Workflow

1. Clarify the deliverable: finished image, prompt, art-direction brief, variation sheet, production concept, or edit of an attached image.
2. Set output constraints: aspect ratio, pixel size, crop, transparency, text-safe space, target viewing distance, and whether multiple views or states are required.
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

For prompt, brief, or concept deliverables, return:

1. **Direction** — one sentence naming the production mode and visual objective.
2. **Specifications** — aspect ratio/size, composition, camera, lighting, palette, materials, and required variants.
3. **Generation prompt** — ready to use, concrete, and free of artist-name imitation.
4. **Avoidance prompt** — concise failure modes and protected elements to omit.
5. **Iteration notes** — 2-4 specific changes to try after the first result.

For a finished-image request, generate or edit the image directly and return the generated result according to the image tool's response contract. Do not add this text template unless the user also asks for the prompt or art-direction rationale.
