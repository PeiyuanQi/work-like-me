# Style Profile: Environments and Landscapes

## Corpus basis

- Source category: `09_Environments-and-Landscapes`
- Coverage: 751 projects and 779 media files
- Common production evidence: Photoshop and matte-painting workflows with Unreal Engine, Houdini, Blender, Maya, and terrain tools
- Provenance boundary: derived from aggregate metadata and representative visual inspection on 2026-08-02; no source artwork is bundled with this skill.

## Best-fit modes

- natural landscape
- settlement or location establishing shot
- ruin or journey keyframe
- weather and atmosphere study

## Visual grammar

- Separate foreground, midground, and background with value, edge, and atmospheric perspective.
- Use one scale anchor and one path, river, ridge, road, or light flow to lead the eye.
- Treat weather as a structural element that reveals depth.
- Let geology, vegetation, water, and settlement patterns agree.

## Liked-corpus calibration

- Keep the environment itself dominant: land, water, weather, and settlement pattern should occupy at least two-thirds of the visual read before any tower, shrine, creature, or character.
- Prefer a wide establishing composition with broad atmospheric masses and a navigable route over a fantasy landmark staged as the singular hero object.
- Use built structures as scale and ecology evidence; avoid ornate silhouettes, supernatural light, or ritual cues unless the user explicitly asks for fantasy.
- Preserve selective painterly distance and natural value variation instead of rendering every building and foreground texture with equal realism.
- Prefer environmental-design evidence over travel-postcard beauty. Hydrology, terrain, vegetation, access, weather, and settlement adaptation should explain the place before sunrise color or scenic spectacle does.
- Keep people, boats, animals, and individual buildings as low-contrast scale marks. Portrait-level rendering or a dominant foreground figure pulls the image toward narrative illustration.
- Unless the user explicitly requests naturalistic photography, break photoreal continuity with authored value grouping, atmospheric occlusion, lost edges, and visibly simplified distance; avoid a uniformly resolved tourism-photography finish.

## Generation priorities

1. Lead with the dominant land, water, or weather mass and the environmental system it creates.
2. Define one navigable route and one adaptation pattern; compress inventories of buildings, crops, boats, or props into supporting evidence.
3. Place time of day and color last so attractive lighting supports spatial logic instead of becoming the subject.

## Technique workflow

- Thumbnail value masses and horizon placement first.
- Choose a dominant landform and a secondary path through it.
- Use procedural or 3D support only for perspective and terrain, then restore focal hierarchy in paint-over.
- Finish with selective texture and small signs of life.
- Reduce or soften any figure, boat, or building that becomes more legible than the route, terrain, water system, or weather structure.

## Terrain refinement in an existing image

- Separate landform shape from surface texture and lighting. If the complaint is repeated polygon or cellular texture, keep the approved rock outline, terrain height, supporting contact, and biome while replacing the false pattern. Do not solve desert rock noise by introducing uniformly rounded river stones.
- Establish scale with large coherent landforms, a few meaningful fractures, varied fragments, and fine sediment. Avoid identical facet sizes, gravel glued across boulder faces, and equal sharpness at every depth. Angular rock edges can be legitimate; repeated small networks across every surface are a different issue.
- Use quiet matte faces and restrained grain for natural dry stone. Do not compensate for removed artifacts by adding uniform cracks or turning all rocks into featureless geometric blocks unless the requested style calls for that simplification.
- Anchor feet, wheels, and structures with believable contact and cast shadows. Preserve the support height under an approved subject; terrain replacement must not leave it floating or buried.
- Inspect the entire returned image, including the main subject: a local ground edit can propagate unwanted patterns into armor, buildings, or other materials. Check broad forms at viewing size and suspect textures at the available native resolution.
- When a pattern survives, change the editing strategy or use an appropriate material reference instead of repeatedly asking for more detail or realism. Label generated references honestly; they are not photographic evidence. Recheck the output before saying the artifact is removed.
- Match the established key light, ambient fill, reflected light, and depth cues. Smooth material cleanup should not flatten lighting, erase useful geometry, or override the requested realistic finish.

## Prompt pattern

```text
Production environment [study/keyframe] centered on [dominant landform, water system, or weather structure] and the [ecological/settlement] adaptation it creates, environment occupying at least two-thirds of the visual read, clear foreground-midground-background value masses, one navigable [path/river/ridge] guiding through the terrain, built elements and tiny figures used only as low-contrast scale evidence, [weather and time of day] shaping depth, authored painterly grouping with atmospheric occlusion, lost edges, one detailed environmental passage, and simplified distance.
```

## Avoidance pattern

```text
Avoid golden-hour travel-postcard treatment, tourism-photography realism, portrait-level foreground figures, equally finished houses, texture everywhere, random mountains, inconsistent ecosystems, equal contrast at every depth, empty scale, over-sharp clouds, and foreground clutter that blocks navigation.
```

## Quality checks

- Depth reads immediately.
- The terrain and ecology feel connected.
- The eye has a route through the frame.
- Scale anchors are present but do not dominate.
- Squinting reveals land, water, weather, and route masses before individual buildings or people.
- Removing the scale figures would not weaken the environmental story or composition.
