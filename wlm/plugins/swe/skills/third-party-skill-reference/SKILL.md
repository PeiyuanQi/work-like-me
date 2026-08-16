---
name: third-party-skill-reference
description: Use when deciding whether to reuse, reference, wrap, adopt, vendor, fork, or document a third-party skill instead of implementing a new work-like-me skill. Also use when copying or adapting borrowed skills, adding skill adapters or external skill dependencies, or updating plugin docs to point at someone else's skill.
---

# Third-Party Skill Reference

Version: 1.1.0

Borrow existing skills when they already solve the job well. Prefer a thin
adapter or reference when runtime reuse is acceptable. Use a locally owned copy
only when local control is intentional and the license allows redistribution.

## Workflow

1. Search for an existing skill before writing a new one. Check installed skills,
   enabled plugins, repo-local skills, and the user's named third-party source.
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
   `references/third-party-skills.md`. For references and wrappers, also record
   the runtime load path.
4. Do not copy third-party skill text, scripts, assets, or examples unless the
   license permits it and attribution/notice requirements are captured.
5. Treat a recorded version or commit as provenance, not an automatic runtime
   pin. Pin only when the user requests it or compatibility and reproducibility
   require it; explain that tradeoff.
6. Preserve the requested ownership model. Do not turn an adoption request into
   a wrapper, or a reference request into a copied derivative, without explaining
   why the change is necessary.
7. If a referenced skill is missing at runtime, say so and continue with the best
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
- Provenance version, commit, tag, or retrieval date when known
- Runtime dependency and pinning policy, or `none` for an adopted copy
- License and attribution requirements when copied or vendored
- Why work-like-me references it instead of implementing its own version
- Local overrides, if any
- Upstream tracking policy for forks or adopted copies
- Fallback behavior when the external skill is not installed

Use `references/third-party-skills.md` for shared registry entries or for
details that would make `SKILL.md` too long.
