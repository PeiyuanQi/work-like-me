# Onboarding Checklist

Before reporting repository onboarding complete, verify:

- `AGENTS.md` and `CLAUDE.md` exist or the repo has a deliberate reason to use
  only one.
- Bridge files point to real files and avoid duplicated long guidance.
- Human-facing setup and development flow live in the repo's existing guide when
  one exists.
- Setup, run, test, lint, and build commands are actual repo commands or are
  explicitly marked as not documented.
- Worktree guidance is present and any project-local worktree directory is
  ignored.
- Third-party code, assets, fonts, icons, tools, and borrowed skills have
  compatible licenses and required notices.
- `git diff --check` or an equivalent lightweight validation has passed.
