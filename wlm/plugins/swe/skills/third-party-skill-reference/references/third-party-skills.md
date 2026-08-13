# Third-Party Skill References

Use this registry for skills that work-like-me references or wraps instead of
owning directly. Keep entries short and factual.

## Entry Template

```markdown
## <Local Wrapper Or Reference Name>

- External skill: `<skill name>`
- External plugin/package: `<plugin or package name>`
- Source: `<URL or local install path>`
- Version: `<tag, commit, release, or unknown>`
- License: `<license and notice requirements, or unknown>`
- Use mode: `reference | wrapper | fork`
- Why borrowed: `<one sentence>`
- Local overrides: `<none or short list>`
- Fallback when missing: `<ask to install, use local fallback, or stop>`
```

## Policy

- Prefer `reference` or `wrapper` for active upstream skills.
- Prefer `fork` only when local edits are required, the license permits copying,
  and the fork has a maintenance owner.
- Do not vendor third-party skill content with an unknown or incompatible
  license.
- If copied material requires attribution or notices, update the repo's relevant
  notice file before committing.

## ADHD-Friendly Wording

- External skill: `i-have-adhd`
- External plugin/package: `ayghri/i-have-adhd`
- Source: `https://github.com/ayghri/i-have-adhd`
- Version: plugin `0.1.0`, commit
  `2ed064090711586e0c97a2fbbf15465fe8f1808b` (2026-08-10)
- License: MIT, copyright 2026 Ayoub Ghriss; preserve the notice if upstream
  content is copied in the future
- Use mode: `wrapper`
- Why borrowed: the active upstream already defines the specialized response
  shape and supports Codex, so work-like-me only needs routing and local policy
- Local overrides: explicit activation, no diagnosis inference, no persistence
  of health-related preferences without a direct request, and no reduction in
  safety or verification rigor
- Fallback when missing: use the adapter's concise action-first approximation
  and disclose that the exact upstream rules were not loaded
