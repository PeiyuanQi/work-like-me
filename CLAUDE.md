# Worker Plugin - CLAUDE.md

This document defines how to work with work-like-me repo.

## Virtual Environments

This project uses `uv` for Python virtual environment management:

```bash
cd wlm
source .venv/bin/activate  # Activate environment
uv sync                    # Install dependencies
```

## Always use First Principle Thinking

## Git Worktrees

- Use a separate git worktree for parallel or unrelated tasks.
- Treat existing uncommitted changes as user-owned unless the user says otherwise.
- Do not switch branches, rewrite history, or clean up another active worktree without explicit instruction.
- Keep changes scoped to the current worktree and say which worktree you used when it matters.

## Code Review Bar

- Review frontend work for UX, visual polish, accessibility, and i18n.
- UX: keep flows intuitive, states explicit, and defaults sensible.
- Aesthetics: keep spacing, typography, alignment, and hierarchy consistent.
- Accessibility: use semantic HTML, keyboard support, focus states, contrast, and clear labels.
- i18n: avoid hard-coded locale assumptions, avoid string concatenation, and allow for text expansion.
- Review backend work for layered services, clear boundaries, and proper design.
- Keep transport, business logic, and persistence concerns separated when practical.
- Review database and data model changes carefully for naming, constraints, indexes, and normalization.
- Check for concurrency issues, race conditions, idempotency gaps, and transactional safety.
- For API design, follow RESTful principles: resource-oriented paths, correct HTTP verbs, appropriate status codes, and consistent request and response shapes.
