---
name: project-dev-setup
description: Inspect and prepare an existing repository for local development by discovering repo-local instructions, dependency and environment setup, development commands, and lightweight baseline checks. Use when orienting to a project, checking workflow conventions, preparing dependencies, or establishing the local setup contract without creating or switching branches. For end-to-end new work, prefer swe:start-work; for agentic repo onboarding, prefer swe:onboard-repo.
---

# Project Dev Setup

Version: 1.3.0

Establish the repository's own local-development contract before changing code.

## Workflow

1. Locate the relevant repository boundary, including nested repositories, before running setup commands.
2. Inspect `git status --short --branch` when the target is a Git repository. Treat every existing change as user-owned.
3. Read the applicable repo guidance completely. Check the nearest `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, docs index, and nested instruction files, following the repository's precedence rules.
4. Derive the setup contract from checked-in evidence: runtime versions, package managers and lockfiles, environment examples, bootstrap commands, required services, development launchers, and lint/test/format commands.
5. Find the source of truth for pending work only when the task depends on a queue, roadmap, or implementation brief. Follow the repo's existing convention.
6. Distinguish discovery from mutation. For orientation or convention checks, remain read-only. For an explicit setup request, run the documented setup command and avoid inventing generic install commands when the repo is silent.
7. If Git LFS is configured, inspect `.gitattributes`, verify whether `git-lfs` is installed or merely missing from `PATH`, and avoid commands that invoke broken clean/smudge filters during read-only inspection. Install or reconfigure LFS only when the task requires it and the user has authorized the needed machine-level change.
8. Leave branch and worktree creation to `swe:start-work` or `swe:git-start-work`. Do not ask for or create a worktree solely because this setup skill ran; follow repo-local workspace rules when those workflows are invoked.
9. Before creating a skill or workflow, use `swe:third-party-skill-reference` to decide whether an existing skill should be referenced or wrapped.
10. Before adding third-party code, assets, fonts, icons, tooling, or vendored skill content, check license compatibility and record required notices.
11. Run the lightest documented baseline check after setup. Record failures that existed before implementation instead of silently treating them as regressions.
12. Start a documented development server only when the task needs it. Keep it foregrounded or attached to an interactive session, and report whether it remains running.

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

- Do not reset, clean, switch branches, or overwrite existing local changes.
- Do not create real secret files from examples or print secret values.
- Do not install machine-wide tools, alter global Git configuration, or start background services without task authority.
- Do not perform merge, rebase, commit, or push operations as part of repository setup.

## Completion Report

Report the repository boundary, guidance files read, setup commands discovered or run, environment requirements, baseline result, and any missing or ambiguous documentation.
