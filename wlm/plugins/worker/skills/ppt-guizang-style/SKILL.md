---
name: ppt-guizang-style
description: Use when the user explicitly requests the Guizang, 归藏, or 歸藏 presentation style; names op7418/guizang-ppt-skill; asks for a Guizang electronic-magazine/e-ink, 杂志风 PPT, Swiss international, 瑞士风 PPT, or Swiss Style deck; or requests the upstream single-file horizontal-swipe HTML deck workflow. This wrapper routes to the upstream skill and applies local presentation QA. Do not use for a generic presentation request until the user selects Guizang.
---

# PPT Guizang Style

This is a work-like-me adapter for the third-party skill
`op7418/guizang-ppt-skill`.

Use this only as one selectable PPT style. Do not treat it as the default style
for every presentation request.

## Source

- Upstream: `https://github.com/op7418/guizang-ppt-skill`
- Use mode: `wrapper`
- Native upstream output: a single-file horizontal-swipe HTML deck
- License: verify upstream `LICENSE` before copying or vendoring any content
- Local content policy: this wrapper references the upstream skill but does not
  vendor upstream skill text, scripts, assets, or examples

## Routing

- For a generic PPT or presentation request with no selected style, use
  `ppt-style-selector` first. Do not bias the choice toward Guizang merely
  because it is the first registered style.
- Once the user selects Guizang or uses one of the trigger phrases in the
  description, route here without asking them to reconfirm the same choice.
- Treat single-file HTML as the upstream workflow's canonical output. If the
  user requires `.pptx`, use the available presentation-authoring skill or
  tooling and explain that WebGL, horizontal swiping, and browser presenter
  features may not survive conversion.

## Workflow

1. Use the installed upstream skill if it is available in the current
   environment. Read its `SKILL.md` completely, then load the references it
   requires for the selected style and task. Follow its update check, but do
   not update the upstream checkout without user approval.
2. If the upstream skill is not installed, use the source URL above and
   `../ppt-style-selector/references/ppt-styles.md` to tell the user what is
   missing. Ask whether to install/reference it or continue with a clearly
   labeled local approximation. Do not install it automatically.
3. Do not copy upstream content into this repo unless the user explicitly asks
   to vendor it and the license check passes.
4. Keep generated work in the user's requested format. Prefer the upstream HTML
   model when the user asks for its full interaction and presenter experience;
   use presentation-authoring tooling when editable `.pptx` is the hard
   requirement.
5. Validate the artifact using the upstream checks plus the local review rules
   below before delivery.

## Local Overrides

- Preserve work-like-me review standards for generated artifacts: check layout,
  text fit, contrast, image/source licensing, and whether the style matches the
  user's audience.
- Do not place wrapper metadata, upstream provenance, sponsor information, or
  installation instructions into the generated presentation.
- Treat Guizang as a style preset, not a presentation engine monopoly. If the
  user's goal calls for a different style, suggest choosing another PPT style
  instead of forcing this one.
