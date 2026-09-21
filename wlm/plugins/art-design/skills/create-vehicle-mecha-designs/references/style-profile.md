# Style Profile: Vehicle and Mecha Designs

## Corpus basis

- Source category: `03_Vehicles-Mecha-and-Robots`
- Coverage: 654 projects and 711 media files
- Common production evidence: Photoshop concept paint over 3ds Max, Maya, Blender, Cinema 4D, Octane, or V-Ray block-ins
- Provenance boundary: derived from aggregate metadata and representative visual inspection on 2026-08-02; no source artwork is bundled with this skill.

## Best-fit modes

- three-quarter hero vehicle
- orthographic/design sheet
- mecha or robot character
- machine operating in an environment

## Visual grammar

- Start with a distinctive massing ratio and direction of travel.
- Expose functional zones: propulsion, suspension, access, sensors, cargo, cooling, and maintenance.
- Use a human, hatch, wheel, railing, or cockpit as a scale anchor.
- Reserve emissive accents and decals for hierarchy, not surface noise.

## Liked-corpus calibration

- Default to an authored concept-design presentation with selective painterly edges, simplified secondary surfaces, and one or two operational context cues. An explicit photographic, cinematic-render, or reference-finish request overrides this default.
- Make one role-driven massing decision obvious before panel detail: an offset payload bay, articulated chassis, deployable module, or unusual propulsion ratio.
- When mobility is a defining feature, show it under load through steering, compression, extension, terrain contact, or a small obstacle.
- Expose at least one role-specific workflow or payload so the design is not merely a plausible generic truck, spacecraft, or robot.
- For hero or operating views, prefer a directional operating pose over a neutral showroom stance. Different contact, control, or propulsion elements should visibly carry different loads, angles, or active states.
- Avoid solving the brief as a rectangular expedition truck with accessories. Let the mobility system and payload workflow reshape the primary silhouette.

## Generation priorities

1. For hero or operating views, lead with the distinctive massing and the machine's visible motion or load state; for orthographic sheets, lead with silhouette and mechanism consistency instead.
2. Name one role-specific payload workflow and one access path; long equipment inventories dilute these identity signals.
3. Place the requested rendering style and restrained context last; use authored concept paint when no different finish is requested.

## Functional complexity and revision constraints

- Preserve the user's chosen architecture across revisions. A request for better terrain handling does not itself authorize replacing an approved biped with a crawler or quadruped; improve its stance, support, articulation, and equipment within the brief.
- Make complexity come from readable assemblies, load paths, service access, and material separation. More rivets, scratches, hoses, or lights everywhere can reduce perceived quality. Leave quiet armor faces around dense working joints.
- Give each prominent attachment a visible job, mounting interface, drive or actuation path, working clearance, and appropriate protection. When the user asks whether it has a real use, distinguish a supported real-world tool analogue from the unvalidated concept mechanism; consult primary technical sources for unfamiliar claims.
- Match tools to the machine's role. Civilian construction equipment may call for surveying, handling, excavation, or repair modules instead of launcher-like silhouettes. Add defensive equipment only within the brief and keep it subordinate when requested.
- A cockpit need not be a large exposed canopy. Pressure seals, a hatch, narrow viewing ports, access hardware, or cameras can communicate operation while preserving the requested armor and scale.
- Multi-environment capability needs compatible modules and visible functional cues, not an inventory of unrelated gadgets. Distinguish illustrative plausibility from validated performance, and label extreme-environment shielding as speculative when it is fictional.

## Technique workflow

- Thumbnail silhouettes before panel lines.
- Block major volumes in 3D or explicit primitive language.
- Resolve joints, clearances, center of gravity, and repeated modules.
- Finish with material separation, wear at contact points, and one controlled beauty light.
- Before finalizing the prompt, remove secondary equipment that does not change silhouette, motion, access, or workflow.

## Prompt pattern

```text
Production-minded [vehicle/mecha/robot] for [role and environment], first read defined by [distinctive primary massing] in [directional operating pose or consistent orthographic set], [mobility/propulsion] visibly steering, compressing, extending, vectoring thrust, or interacting with terrain under an active state, one unmistakable [payload workflow] with a usable access path, human-scale cue, restrained [material palette], [requested finish, or authored concept paint by default], selective crisp edges and quieter secondary surfaces.
```

## Avoidance pattern

```text
Avoid unrequested generic chassis substitutions, random greebles, impossible joints, floating parts, uniform panel density, unreadable mobility or operator-access cues, excessive neon, and tool or weapon attachments without structural support. For operating views, avoid identical suspension states and a neutral showroom stance. Do not use these defaults to override a requested design sheet, protected cockpit, or photographic finish.
```

## Quality checks

- The role is understandable from silhouette alone.
- Movement and access systems could plausibly operate.
- Scale is explicit.
- Material and damage placement follow function.
- Quiet armor faces remain distinct from joints and fasteners; repeated cellular or polygon crackle is not mistaken for engineered panel seams or natural wear.
- Small cockpit and tool changes preserve approved neighboring components and the overall architecture.
- When an operating view claims mobility, at least two contact, control, or propulsion elements visibly differ in steering, compression, extension, thrust, or environmental response; otherwise the mobility is not actually demonstrated.
- The payload workflow remains identifiable after removing small antennas, panels, and surface detail.
