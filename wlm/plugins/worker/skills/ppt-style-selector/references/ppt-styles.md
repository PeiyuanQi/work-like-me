# PPT Style Registry

Work-like-me can reference multiple PPT styles. Pick a style intentionally
instead of assuming one presentation style fits every deck.

Registry order records when a style was added. It does not define a universal
default. When the user asks the agent to choose, match the style to the deck's
content, audience, requested format, template, brand, and visual references.

## guizang

- Local skill: `ppt-guizang-style`
- Qualified local skill: `worker:ppt-guizang-style`
- External skill: `guizang-ppt-skill`
- External source: `https://github.com/op7418/guizang-ppt-skill`
- Use mode: `wrapper`
- Status: first registered PPT style in work-like-me
- Selection aliases: Guizang, 归藏, 歸藏, `op7418/guizang-ppt-skill`, electronic
  magazine, e-ink, 杂志风 PPT, Swiss international, Swiss Style, 瑞士风 PPT
- Intended use: Guizang-style HTML/PPT presentations, including its electronic
  magazine/e-ink direction and Swiss international style direction
- Not intended for: all PPT requests, corporate decks that require a different
  brand system, or presentation styles the user has not selected
- License note: verify upstream `LICENSE` before copying or vendoring upstream
  content; this registry only references the external source
- Fallback when missing: ask whether to install/reference the upstream skill or
  continue with a local approximation
