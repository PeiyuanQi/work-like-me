---
name: third-party-skill-reference
description: Use when deciding whether to reuse, reference, wrap, or document a third-party skill instead of implementing a new work-like-me skill. Also use when adding borrowed skills, skill adapters, external skill dependencies, or updating plugin docs to point at someone else's skill.
---

# Third-Party Skill Reference

Version: 1.0.0

Borrow existing skills when they already solve the job well. Prefer a thin
adapter or reference over copying another author's skill into this plugin.

## Workflow

1. Search for an existing skill before writing a new one. Check installed skills,
   enabled plugins, repo-local skills, and the user's named third-party source.
2. Decide whether to reference, wrap, fork, or implement:
   - **Reference** when the skill can be used directly as installed.
   - **Wrap** when work-like-me needs local trigger wording, policy, or routing.
   - **Fork** only when local edits are required and the license allows copying.
   - **Implement** when no suitable external skill exists.
3. For references and wrappers, record the external skill source and load path in
   the wrapper `SKILL.md` or a `references/third-party-skills.md` file.
4. Do not copy third-party skill text, scripts, assets, or examples unless the
   license permits it and attribution/notice requirements are captured.
5. If a referenced skill is missing at runtime, say so and continue with the best
   local fallback instead of pretending it is available.

## Wrapper Pattern

A wrapper skill should stay short:

```markdown
---
name: local-skill-name
description: Use when...
---

# Local Skill Name

This is a work-like-me adapter for `<external skill name>`.

Load and follow `<external plugin>/<external skill>/SKILL.md` first. Apply these
local overrides:

- ...

If the external skill is unavailable, use `references/third-party-skills.md` to
find install/source details, then ask whether to install it or proceed with a
local fallback.
```

## Metadata To Record

When adding a third-party skill reference, record:

- External skill name and plugin/package name
- Source URL or local install path
- Version, commit, tag, or install date when known
- License and attribution requirements when copied or vendored
- Why work-like-me references it instead of implementing its own version
- Local overrides, if any
- Fallback behavior when the external skill is not installed

Use `references/third-party-skills.md` for shared registry entries or for
details that would make `SKILL.md` too long.
