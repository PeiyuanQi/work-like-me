---
name: ppt-style-selector
description: Use when the user asks what PPT styles are available, wants to choose a presentation style, asks to add or manage PPT styles in work-like-me, or asks for a PPT without naming a style and style selection matters. Do not generate a deck directly unless a style has been selected or is clearly implied.
---

# PPT Style Selector

Version: 1.0.0

Work-like-me supports multiple selectable PPT styles. Use this skill to choose
the style before routing to a style-specific skill.

## Workflow

1. Read `references/ppt-styles.md` for the registered style list.
2. If the user named a style, route to that style-specific skill.
3. If the user asked generically for a PPT and style matters, ask which style to
   use or present the available style names. Do not assume Guizang applies to all
   PPT requests.
4. If only one style is registered and the user wants the first/default
   work-like-me PPT style, route to `ppt-guizang-style`.
5. When adding another style, prefer a wrapper/reference to the external style
   skill over vendoring content. Record source, version, license, local
   overrides, and fallback behavior in `references/ppt-styles.md`.
