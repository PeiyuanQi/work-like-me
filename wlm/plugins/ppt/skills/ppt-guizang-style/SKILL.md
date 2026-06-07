---
name: ppt-guizang-style
description: Use when the user asks to make a PPT, slide deck, presentation, or HTML presentation in the Guizang PPT style from op7418/guizang-ppt-skill; asks for the Guizang electronic magazine/e-ink style; asks for the Guizang Swiss international style; or explicitly chooses Guizang as one presentation style. Do not use for all PPT requests by default.
---

# PPT Guizang Style

Version: 1.0.0

This is a work-like-me adapter for the third-party skill
`op7418/guizang-ppt-skill`.

Use this only as one selectable PPT style. Do not treat it as the default style
for every presentation request.

## Source

- Upstream: `https://github.com/op7418/guizang-ppt-skill`
- Use mode: `wrapper`
- License: verify upstream `LICENSE` before copying or vendoring any content
- Local content policy: this wrapper references the upstream skill but does not
  vendor upstream skill text, scripts, assets, or examples

## When To Use

- The user explicitly names Guizang, `guizang-ppt-skill`, or the upstream repo.
- The user asks for one of Guizang's known visual directions:
  - electronic magazine / e-ink / editorial monochrome presentation
  - Swiss international style presentation
- The user asks to use the first registered work-like-me PPT style and no other
  style has been selected.

## Workflow

1. Confirm that Guizang is the intended PPT style when the user asks generically
   for a PPT without naming a style.
2. Use the installed upstream skill if it is available in the current
   environment. Load and follow the upstream `SKILL.md` first, then apply the
   local rules in this wrapper.
3. If the upstream skill is not installed, use the source URL above and
   `../ppt-style-selector/references/ppt-styles.md` to tell the user what is
   missing. Ask whether to install/reference it or continue with a local
   approximation.
4. Do not copy upstream content into this repo unless the user explicitly asks
   to vendor it and the license check passes.
5. Keep generated deck work product in the user's requested format. If the user
   asks for an editable/publishable artifact, prefer the upstream skill's native
   output model.

## Local Overrides

- Preserve work-like-me review standards for generated artifacts: check layout,
  text fit, contrast, image/source licensing, and whether the style matches the
  user's audience.
- Treat Guizang as a style preset, not a presentation engine monopoly. If the
  user's goal calls for a different style, suggest choosing another PPT style
  instead of forcing this one.
