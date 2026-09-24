---
name: third-party-skill-reference
description: "Decides whether to reuse, reference, wrap, adopt, vendor, fork, document, or reimplement a third-party skill that may already do the job, and records provenance, license, and fallback details for borrowed skills. Use before creating a new work-like-me skill, and when copying or adapting borrowed skills, adding skill adapters or external skill dependencies, or pointing plugin docs at someone else's skill."
---

# Third-Party Skill Reference

Version: 1.2.0

Borrow existing skills when they already solve the job well. Prefer a thin
adapter or reference when runtime reuse is acceptable. Use a locally owned copy
only when local control is intentional and the license allows redistribution.

## Workflow

1. Search for an existing skill before writing a new one. Check installed
   skills, enabled plugins, repo-local skills, and the user's named third-party
   source.
2. Decide whether to reference, wrap, adopt, fork, or implement:
   - **Reference** when the skill can be used directly as installed.
   - **Wrap** when work-like-me needs local trigger wording, policy, or routing.
   - **Adopt/vendor** when work-like-me should own a self-contained derivative
     with no runtime dependency on the external skill.
   - **Fork** when local edits are required and ongoing upstream tracking is
     intentional.
   - **Implement** when no suitable external skill exists.
3. For every borrowed mode, record the external source and provenance in the
   local `SKILL.md`, the repository notice file, or
   [references/third-party-skills.md](references/third-party-skills.md). For
   references and wrappers, also record the runtime load path.
4. Copy third-party skill text, scripts, assets, or examples only when the
   license permits it and the attribution and notice requirements are captured.
5. Treat a recorded version or commit as provenance, not an automatic runtime
   pin. Pin only when the user requests it or compatibility and
   reproducibility require it, and explain that tradeoff.
6. Preserve the requested ownership model. If turning an adoption request into
   a wrapper, or a reference request into a copied derivative, is necessary,
   explain why before doing it.
7. If a referenced skill is missing at runtime, say so and continue with the
   best local fallback rather than pretending it is available.

## Wrapper Pattern

A wrapper skill stays short. Write its description in the third person, saying
what it does and when to use it:

```markdown
---
name: local-skill-name
description: Adapts <external skill> for work-like-me with local policy. Use when...
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

Replace every `<placeholder>` before saving; angle brackets are not allowed in a
real `description`.

## Metadata To Record

When adding a third-party skill reference, record:

- External skill name and plugin/package name
- Source URL or local install path
- Provenance version, commit, tag, or retrieval date when known
- Runtime dependency and pinning policy, or `none` for an adopted copy
- License and attribution requirements when copied or vendored
- Why work-like-me references it instead of implementing its own version
- Local overrides, if any
- Upstream tracking policy for forks or adopted copies
- Fallback behavior when the external skill is not installed

Use [references/third-party-skills.md](references/third-party-skills.md) for
shared registry entries or for details that would make `SKILL.md` too long.
