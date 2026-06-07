# Software Engineering Plugin

SWE workflow skills for repository setup, parallel git work, commit prep,
merge-request review, reviewer discovery, and virtual environment management.

## Skills

- `project-dev-setup`: read repo guidance, identify setup conventions, and keep
  docs and code aligned.
- `git-start-work`: start feature or fix work, preferring git worktrees for
  parallel and multi-agent development.
- `prepare-code-for-commit`: format and lint according to repo tooling first,
  with language defaults when the repo is silent.
- `git-commit-push`: review, commit, rebase when needed, and push changes.
- `create-merge-request`: create a PR/MR, run independent review, and route to a
  code reviewer.
- `find-code-reviewer`: identify the right code reviewer from repo ownership,
  memory, and recent changes.
- `manage-virtual-environments`: set up isolated project environments using
  repo-defined tools and versions.
- `third-party-skill-reference`: reference or wrap borrowed skills instead of
  reimplementing them in work-like-me.

## Workflow Preferences

- Prefer git worktrees for new work so multiple agents can work safely at the
  same time.
- Prefer rebase-based branch refresh and conflict resolution that preserves the
  original intent of the change.
- Prefer independent high-effort review before requesting human review on a
  merge request.
- Prefer referencing or wrapping a good third-party skill over copying it or
  rebuilding it locally.
