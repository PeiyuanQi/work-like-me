---
name: ppt-style-selector
description: Select and route visual styles for PowerPoint, PPT/PPTX, slide-deck, presentation, and Google Slides work. Use when the user asks what presentation styles are available, wants to choose, add, or manage a work-like-me style preset, or requests a deck without a clear visual direction and the choice would materially affect the result. If the user already provides a registered style, a custom or brand direction, a template, or a clear reference, preserve that choice and continue without asking them to select again. Do not invent a style-specific skill for an unregistered direction or assume the first registered style is the default.
---

# PPT Style Selector

Choose among registered style wrappers without turning the registry into a gate
for every presentation.

## Workflow

1. Read `references/ppt-styles.md` for the registered style list.
2. Resolve the direction before asking a question:
   - If the user names a registered style or alias, route to its qualified local
     skill, such as `worker:ppt-guizang-style`, without reconfirming the choice.
   - If the user gives a clear unregistered direction such as a corporate,
     academic, minimal, custom, or brand-matched style, preserve it as the style
     brief and continue with the available presentation-authoring workflow. Do
     not invent a matching skill or force the closest registered preset.
   - If a supplied template, brand system, audience, or visual reference makes
     the direction clear, derive the style from that evidence and proceed.
3. Ask one focused style question only when the request is genuinely generic
   and different visual directions would materially change the result. Present
   the registered choices plus a custom or brand-matched option.
4. Treat registry order as registration history, not preference:
   - If the user explicitly asks for the first registered style, route to
     `worker:ppt-guizang-style`.
   - If the user asks for the default or says "choose for me," select from the
     content, audience, format, template, and references. Do not silently equate
     that request with Guizang.
5. After resolving the style, hand off artifact creation to the appropriate
   style wrapper or presentation-authoring skill and preserve the requested
   output format.
6. When adding another style, prefer a wrapper/reference to the external style
   skill over vendoring content. Record source, version, license, local
   overrides, selection aliases, intended formats, and fallback behavior in
   `references/ppt-styles.md`.
