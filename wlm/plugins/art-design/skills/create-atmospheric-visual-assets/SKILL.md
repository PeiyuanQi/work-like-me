---
name: create-atmospheric-visual-assets
description: Create or art-direct atmospheric visual assets for websites, games, decks, covers, and product pages. Use when the user wants AI-generated raster imagery for hero art, key art, section backgrounds, social cards, game backgrounds, props, item icons, texture references, UI ornaments, or reusable visual styles with cinematic lighting, tactile materials, Chinese or East Asian strategic visual language when appropriate, and clear production constraints.
---

# Create Atmospheric Visual Assets

Use this skill to turn a strong reference image or visual direction into reusable image-generation guidance for website and game assets. Preserve the visual grammar, not exact subjects, marks, logos, names, or protected assets. When the reference has Chinese visual cues, abstract them as cultural texture and grand-strategy mood rather than as a project-specific setting.

## Workflow

1. Classify the asset before prompting: hero/key art, website section background, editorial illustration, social card, game background, prop/item icon, UI ornament, texture/material reference, sprite concept, or tileable pattern.
2. Set production constraints: aspect ratio, target pixel size, transparency, text-safe space, crop behavior, animation readiness, tiling, and whether the asset must read at small sizes.
3. Identify interchangeable slots: topic, cultural register, surface, object vocabulary, material palette, focal clue, lighting, and negative constraints.
4. Generate or edit 2-4 candidates, then judge the asset in its real use case: page crop, thumbnail, game UI slot, inventory icon, tile repeat, or background behind text.
5. Iterate with small edits: clear the functional area, simplify silhouettes, strengthen the focal cluster, remove unreadable text, tune lighting, or make the asset more modular.

## Asset Types

- Website hero or key art: use wide cinematic framing, strong text-safe negative space, a detailed focal area, and lighting that still works under a dark overlay.
- Website section background: keep contrast lower than hero art, avoid focal clutter, and leave room for cards, headings, or navigation to sit above it.
- Editorial or social card: make one readable focal idea, strong silhouette, and safe crop for square, 4:5, and 16:9 variants.
- Game background: separate foreground, midground, and background layers in the prompt when parallax or later animation may matter.
- Prop or item icon: request isolated object, clear silhouette, readable at 64-128 px, consistent light direction, transparent or plain background.
- UI ornament or frame: request modular corners, dividers, buttons, badges, borders, panels, or resource markers with consistent material and states when needed.
- Texture or material reference: request flat, evenly lit swatches or seamless/tileable textures only when the output needs to repeat.
- Map, board, or strategy surface: keep routes, tokens, terrain, and documents legible as shapes, while generated writing stays illegible or symbolic unless exact text is supplied.

## Core Style Recipe

- Composition: choose the composition for the asset type. Wide assets can use oblique top-down or high three-quarter tabletop scenes; icons need centered object silhouettes; UI ornaments need symmetry and modular edges.
- Surface: worn paper, ink-wash map, chart, blueprint, manuscript, ledger, tabletop, workbench, fabric, stone, metal, wood, or another physically plausible narrative ground.
- Detail layer: fine drawn routes, contour lines, annotations, pins, jade/stone/brass wargame pieces, brushes, inkstones, carved seals, seal-paste impressions on paper, tools, samples, folders, cords, stamps, or domain-specific small objects. Treat these as evidence, not decoration.
- Focal balance: put detail where the asset can afford it. Leave text-safe zones calm for web art; simplify edges for game icons and UI elements.
- Lighting: low-key cinematic light, warm side light, soft falloff, subtle haze or dust, gentle vignette, realistic shadows, no flat studio lighting unless producing texture references.
- Palette: parchment, ink-wash gray, charcoal, aged green-black, jade green, muted teal or river blue, oxidized brass or bronze, restrained cinnabar from seal paste or small accents.
- Materials: fibrous paper, carved wood, jade, stone, brass, bronze, ceramic, silk or rough fabric, ink, and worn edges. Avoid glossy plastic unless the subject explicitly calls for it.
- Mood: premium, quiet, strategic, tactile, mysterious, hand-crafted, grounded. Prefer implied story over explicit fantasy illustration.

## Chinese Strategy Mode

Use this mode when the requested asset should feel Chinese, East Asian, dynastic, historical-strategy, or ink-painting inspired without being tied to a specific franchise.

- Prefer: jade or stone army pieces, bronze tokens, carved wooden markers, brush and inkstone, hand-drawn route lines, river systems, mountain washes, archival reports, silk cords, carved stone seals, and vermilion seal-paste impressions on paper.
- Map language: use guohua or ink-wash mountains, river deltas, pale paper fibers, hand-drawn roads, annotated passes, and abstract place marks. Keep generated writing illegible or symbolic unless the user supplies exact text.
- Avoid by default: European sealing wax, wax seals, lacquer-seal props, fantasy runes, dragons as generic decoration, modern UI screens, and overly literal imperial iconography.

## Prompt Pattern

Build prompts from these slots instead of hard-coding a project:

```text
[Asset type] for [topic or product/game context], [surface or background] with [main object/document/terrain layer], [small physical tokens/tools/ornaments] arranged along [routes/diagram/composition structure], one subtle focal clue suggesting [core idea]. [Camera/framing appropriate to asset type], [functional constraint: text-safe space/transparent background/tileable/64 px readable/layered background]. Warm directional light, tactile worn materials, muted parchment/ink-wash gray/jade/teal/bronze palette with restrained cinnabar accents, premium editorial or game art, painterly realism, high detail where useful, no visible typography.
```

Add a negative prompt or explicit avoidance line:

```text
Avoid readable text, logos, protected symbols, UI panels unless requested, generic fantasy symbols, characters unless requested, neon colors, plastic shine, wax seals or lacquer-seal props in Chinese/East Asian contexts, clutter in functional areas, distorted perspective, oversharpened texture, and direct copies of any reference image.
```

## Output Specs

- Hero/key art: recommend exact aspect ratio, text-safe zone, and overlay assumptions.
- Website background: recommend crop behavior, contrast level, and whether it should be decorative or narrative.
- Game background: recommend layer separation, camera angle, and whether the output should be loopable or parallax-ready.
- Item/icon/prop: recommend transparent background, target size, silhouette rules, and variant count.
- UI ornament: recommend states or variants such as default, hover, active, disabled, selected, damaged, rare, or legendary.
- Texture/pattern: recommend seamless/tileable wording, flat lighting, material scale, and edge-repeat checks.

## Quality Checklist

- The image works in the real slot, not just as a standalone picture.
- Functional areas are clean: text zones, icon silhouettes, tile edges, UI edges, and animation/layer boundaries do not fight the design.
- The subject is conveyed through objects, material, and composition, not through generated readable words.
- Props are theme-appropriate but not tied to a protected or project-specific symbol set.
- Chinese or East Asian cues feel coherent: use brush, ink, stone, jade, bronze, and vermilion seal paste rather than wax or lacquer-seal props.
- Small assets remain readable at intended size; large assets keep enough quiet space for layout.
- The image feels tactile and cinematic rather than stock-like, glossy, or overly literal.

## Response Format

When responding to a user, provide the asset classification, recommended size or aspect ratio, a ready-to-use prompt, an avoidance prompt, and 2-3 concise edit directions for the next generation pass.
