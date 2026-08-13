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

## ADHD-Friendly Technical Writing

- External skill: `i-have-adhd`
- External plugin/package: `ayghri/i-have-adhd`
- Source: `https://github.com/ayghri/i-have-adhd`
- Version: not pinned; work-like-me owns its adapted copy
- License: MIT, copyright 2026 Ayoub Ghriss; attribution and license text are in
  `THIRD_PARTY_NOTICES.md`
- Use mode: `fork`
- Why borrowed: the upstream response-shaping principles are useful, while the
  local skill needs an independently maintained technical-domain policy
- Local overrides: require explicit activation and engineering or technical
  text; exclude office and non-technical prose; do not infer a diagnosis or
  persist health-related preferences; preserve safety and verification rigor
- Fallback when missing: not applicable; the local skill is self-contained
