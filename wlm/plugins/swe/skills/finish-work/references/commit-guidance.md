# Commit Guidance

Use conventional commits unless the repo defines a different convention.

Common types:

- `feat`: user-visible feature or capability
- `fix`: bug fix
- `docs`: documentation-only change
- `refactor`: behavior-preserving restructuring
- `test`: test-only or test-support change
- `chore`: maintenance, tooling, dependency, or metadata work
- `perf`: performance improvement
- `style`: formatting-only change

Use a short imperative subject. Include a body when the reason, migration note,
or risk would not be clear from the diff.

Before staging, review both unstaged and staged diffs. Stage only intended
changes, especially in repos where the worktree may include user-owned edits.
