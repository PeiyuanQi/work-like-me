# Worktree Guidance

Prefer worktrees when work is parallel, unrelated to current local changes, or
likely to involve another agent.

Selection order:

1. Use an existing repo-local `.worktrees/` or `worktrees/` directory.
2. Use a repo-documented worktree location from `AGENTS.md`, `CLAUDE.md`, or the
   development guide.
3. Ask before choosing a new project-local or global worktree location.

Before creating a project-local worktree, verify the directory is ignored with
`git check-ignore`. If it is not ignored, add the narrow ignore entry before
creating the worktree.

Create from the remote default branch after fetching. Report the exact path and
branch so the user can distinguish concurrent agent workspaces.
