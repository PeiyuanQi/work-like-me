---
name: create-characters-portraits
description: Create or art-direct character designs, portraits, costume concepts, character sheets, stylized people, and expressive figure imagery. Use when the user wants a protagonist, NPC, portrait, outfit exploration, turnaround, beauty image, or image-generation prompt with strong identity, pose, face, costume logic, and readable shape language.
---

# Create Characters and Portraits

Read [references/style-profile.md](references/style-profile.md) before composing a prompt or generating an image. Use the profile as a visual grammar, not as permission to copy any artist, project, composition, character, logo, or protected mark from the source archive.

## Workflow

1. Determine the deliverable from the request: finished image, prompt, art-direction brief, variation sheet, production concept, or edit of an attached image. For finished-image and edit requests, infer unspecified creative defaults and proceed without reconfirmation; ask only when a required reference image is unavailable.
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

Match the response to the requested deliverable:

- For a finished image or edit, use the image tool and return the visual directly. Add only a brief note when it helps the user choose or request another iteration; do not dump an unused prompt package unless requested.
- For a prompt, art-direction brief, variation sheet, or production concept, return:

1. **Direction** — one sentence naming the production mode and visual objective.
2. **Specifications** — aspect ratio/size, composition, camera, lighting, palette, materials, and required variants.
3. **Generation prompt** — ready to use, concrete, and free of artist-name imitation.
4. **Avoidance prompt** — concise failure modes and protected elements to omit.
5. **Iteration notes** — 2-4 specific changes to try after the first result.
