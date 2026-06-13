# Software Engineering Plugin

SWE workflow skills for repository setup, parallel git work, quality checks,
commit and push, merge-request review, reviewer discovery, virtual environment
management, and agentic project onboarding.

## Workflow Skills

Use these as the primary entry points for normal software engineering work:

- `start-work`: begin a feature, fix, refactor, docs task, or investigation from
  a current baseline. Orchestrates `project-dev-setup`, `git-start-work`, and
  `manage-virtual-environments`.
- `finish-work`: wrap up a change with formatting, linting, verification, diff
  review, commit, and optional push. Orchestrates `prepare-code-for-commit` and
  `git-commit-push`.
- `submit-work`: prepare a branch for review, create a PR/MR, run independent
  review, find a reviewer, and notify them when tooling is available.
  Orchestrates `finish-work`, `create-merge-request`, and
  `find-code-reviewer`.
- `onboard-repo`: prepare an existing repo for human and agent collaboration.
  Orchestrates `project-dev-setup`, `onboard-agentic-dev-flow`, and
  `third-party-skill-reference` when borrowed skill behavior is involved.

## Primitive Skills

Use these directly when the user asks for a specific narrow operation:

- `project-dev-setup`: read repo guidance, identify setup conventions, and keep
  docs and code aligned.
- `onboard-agentic-dev-flow`: add minimal `AGENTS.md`/`CLAUDE.md` project
  guidance, human development flow notes, worktree-first git workflow, and
  distilled coding rules.
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
- `rank-software-decisions`: rank engineering, architecture, tooling,
  dependency, migration, and AI/agent workflow options with an anonymized
  blog-derived value pattern.

## Workflow Preferences

- Prefer workflow skills for end-to-end requests and primitive skills for
  focused operations.
- Prefer git worktrees for new work so multiple agents can work safely at the
  same time.
- Prefer rebase-based branch refresh and conflict resolution that preserves the
  original intent of the change.
- Prefer repo-defined format, lint, test, build, and setup commands over generic
  language defaults.
- Prefer independent high-effort review before requesting human review on a
  merge request.
- Prefer referencing or wrapping a good third-party skill over copying it or
  rebuilding it locally.
- Prefer decisions that preserve options, expose hidden cost, and survive
  ordinary maintenance over choices that only look elegant in the short term.
