---
name: project-dev-setup
description: "Inspects and prepares an existing repository for local development by discovering repo-local instructions, dependency and environment setup, development commands, and lightweight baseline checks, without creating or switching branches. Use when orienting to a project, checking workflow conventions, preparing dependencies, or establishing the local setup contract. For end-to-end new work, use swe:start-work; for agentic repo onboarding, use swe:onboard-repo."
---

# Project Dev Setup

Version: 1.4.0

Establish the repository's own local-development contract before changing code.

## Workflow

1. Locate the relevant repository boundary, including nested repositories,
   before running setup commands.
2. Inspect `git status --short --branch` when the target is a Git repository.
   Treat every existing change as user-owned.
3. Read the applicable repo guidance completely: the nearest `AGENTS.md`,
   `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, docs index, and nested
   instruction files, following the repository's precedence rules.
4. Derive the setup contract from checked-in evidence: runtime versions,
   package managers and lockfiles, environment examples, bootstrap commands,
   required services, development launchers, and lint/test/format commands.
5. Find the source of truth for pending work only when the task depends on a
   queue, roadmap, or implementation brief, and follow the repo's existing
   convention for it.
6. Separate discovery from mutation. For orientation or convention checks,
   stay read-only. For an explicit setup request, run the documented setup
   command; when the repo is silent, report the gap rather than inventing
   generic install commands.
7. If Git LFS is configured, inspect `.gitattributes` and check whether
   `git-lfs` is installed or merely missing from `PATH`. During read-only
   inspection, avoid commands that invoke broken clean/smudge filters. Install
   or reconfigure LFS only when the task requires it and the user has
   authorized the machine-level change.
8. Leave branch and worktree creation to `swe:start-work` or
   `swe:git-start-work`; this setup skill running is not a reason to ask for or
   create a worktree. Follow repo-local workspace rules when those workflows
   are invoked.
9. Before creating a skill or workflow, use `swe:third-party-skill-reference`
   to decide whether an existing skill should be referenced or wrapped.
10. Before adding third-party code, assets, fonts, icons, tooling, or vendored
    skill content, check license compatibility and record required notices.
11. Run the lightest documented baseline check after setup. Record failures
    that existed before implementation so they are not later mistaken for
    regressions.
12. Start a documented development server only when the task needs it. Keep it
    in the foreground or attached to an interactive session, and report
    whether it remains running.

## What To Look For

- Repo-local docs that define process and conventions
- Repository boundaries and nested instruction scopes
- Runtime and package-manager version files
- Dev environment files such as `.env.example`
- Bootstrap, local dev, lint, test, and format scripts
- Required local services, ports, and non-secret environment variables
- Docs-driven feature queues or implementation notes
- Git LFS attributes, executable availability, and filter health
- License files and third-party notices
- Existing third-party skills that could be referenced instead of reimplemented

## Safety

- Preserve existing local changes: no reset, clean, branch switch, or
  overwrite.
- Leave secrets alone: don't create real secret files from examples or print
  secret values.
- Install machine-wide tools, alter global Git configuration, or start
  background services only with task authority.
- Merge, rebase, commit, and push are outside repository setup.

## Completion Report

Report the repository boundary, guidance files read, setup commands discovered
or run, environment requirements, baseline result, and any missing or ambiguous
documentation.
