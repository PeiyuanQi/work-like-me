# Commit Guidance

## Cadence and boundaries

- Treat Git commits as durable delivery and review boundaries, not as a log of
  every agent step.
- Default to one commit for one coherent user-requested outcome, created after
  the implementation and proportional checks are complete.
- Do not commit after each file, subtask, tool call, test run, lint fix, or agent
  turn. Keep evolving work in the working tree and use status, diffs, and test
  output for visibility.
- Split the pending work only when each part can be understood, validated, and
  reverted independently, or when the user or repository convention requires
  separate commits. Different file types or implementation phases alone are
  not reasons to split.
- Fold formatting, tests, documentation, generated metadata, and small repairs
  that support the same outcome into that outcome's commit.
- Use checkpoint commits only when the user asks, the repository requires them,
  or an unusually long or risky task has a concrete recovery need that outweighs
  the extra history. Ask before introducing checkpoints when authority is not
  already clear.
- Preserve existing local and published commits. Do not amend, squash, or
  rewrite them solely to reduce commit count without explicit instruction.

## Message convention

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
