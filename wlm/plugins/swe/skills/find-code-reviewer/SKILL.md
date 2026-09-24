---
name: find-code-reviewer
description: "Identifies and ranks human code reviewers for a PR, MR, branch, file, directory, or code area from CODEOWNERS, ownership docs, review history, team memory, and file or module history. Use when the user wants to find, rank, choose, request, or assign a code reviewer. Only for code-review routing: use worker:find-poc for non-code contacts, and not for performing the review itself."
---

# Find Code Reviewer

Find the best-supported human reviewer without inventing ownership,
availability, roles, or contact details.

## Establish Scope

Identify the repository, PR/MR or branch, target branch, author, and changed
paths. Stay read-only unless the user explicitly asks to request or assign a
reviewer, and preserve the current branch and worktree state.

## Gather Evidence

Use the strongest available evidence, in this order:

1. **Ownership rules and repository documentation**
   - Locate ownership files with `rg --files -g 'CODEOWNERS' -g '**/CODEOWNERS'`.
   - Check common locations such as `.github/CODEOWNERS`, `.gitlab/CODEOWNERS`,
     `docs/CODEOWNERS`, and the repository root.
   - Match the changed paths using the hosting platform's CODEOWNERS semantics,
     including rule order. Cite the matching file, rule, and path.
2. **PR/MR review history**
   - When platform access is available, inspect currently requested reviewers
     and recent merged changes that touched the same area, using the connected
     hosting app, `gh`, or the appropriate platform API or CLI.
   - Local `git log` usually records authors and committers, not reviewers, so
     it is not evidence of who reviewed a change.
3. **Documented team context**
   - Use `worker:search-memory` when team memory is available and relevant.
     Search for ownership, reviewer rotation, maintainers, and review policy.
   - Note the source date and flag stale or conflicting information.
4. **File and module history**
   - Use path-scoped `git log -- <path>` or targeted `git blame -- <file>` only
     as supporting evidence of familiarity with the area.
   - Treat contributors as candidates, not automatically as reviewers.

## Rank Candidates

Prefer an explicitly assigned individual or team member with direct ownership
and recent review activity, then documented maintainers, then recent relevant
contributors. Exclude or clearly flag:

- the change author;
- bots and automation accounts;
- people whose current team membership or account identity cannot be verified;
- stale ownership or review evidence;
- candidates whose availability is unknown.

Report a role, handle, or contact channel only when a source supports it. Never
derive a contact method from a commit email or expose private contact data;
both leak personal information that was not shared for this purpose.

## Return Results

Return a short ranked list rather than a single unsupported name. For each
candidate, include:

- verified name or platform handle;
- evidence and source;
- affected paths or review area;
- confidence (`high`, `medium`, or `low`);
- any unresolved identity, membership, or availability caveat.

If no candidate is verifiable, say what was searched and recommend a documented
maintainer role or team review channel instead of naming a person.

Request or assign a reviewer only when the user explicitly asked for that
external state change and the target account is unambiguous. Report what
changed and any platform failure.
