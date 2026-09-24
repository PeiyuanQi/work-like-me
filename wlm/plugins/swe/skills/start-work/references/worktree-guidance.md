# Worktree Guidance

Prefer worktrees when work is parallel, unrelated to current local changes, or
likely to involve another agent.

Selection order:

1. Use an existing repo-local `.worktrees/` or `worktrees/` directory.
2. Use a repo-documented worktree location from `AGENTS.md`, `CLAUDE.md`, or
   the development guide.
3. Ask before choosing a new project-local or global worktree location.

Before creating a project-local worktree, verify the directory is ignored with
`git check-ignore`. If it is not ignored, add the narrow ignore entry before
creating the worktree, because an unignored worktree inside the repository
shows up as untracked files and can be committed by accident. Mention the
`.gitignore` edit in the report. If you are unsure the entry is right, have a
fresh subagent with clean context review it first; if you are still unsure,
ask the user to review it. `swe:git-start-work` lists the cases that call for
that review.

Create from the remote default branch after fetching. Report the exact path and
branch so the user can tell concurrent agent workspaces apart.
