---
name: consolidate-memory
description: Find, consolidate, and track the canonical memory location. Use when starting a new work session, memory feels fragmented, or the agent needs to determine where memory should be read from and written to.
---

# consolidate-memory

Version: 1.0.0

Find, consolidate, and track the canonical memory location.

## When to use

Use this skill when:
- Starting a new work session
- Memory feels fragmented across locations
- You need to know where to look for memory

## Steps

### Step 1: Check for existing memory

Search in this order:
1. `memory/` in current directory (`.`)
2. `memory/` in git repo root (via `git rev-parse --show-toplevel`)
3. `~/.wlm/memory/`

Use Bash with `ls` to check each location. Note what you find.

### Step 2: If multiple found

- Merge all content into `~/.wlm/memory/`
- Keep all unique files from each location
- Create directory structure if needed: `corps/tools/`, `projects/`, `teams/roles/`

### Step 3: If none found

- Ask user: "I couldn't find any existing memory. Is there a memory location you'd like me to note?"

### Step 4: Update SOUL.md

After consolidation, update `~/.wlm/SOUL.md` with:

```markdown
# SOUL

## Memory

- Canonical path: ~/.wlm/memory/
- Consolidated: YYYY-MM-DD
- Sources: [list of merged locations if any]
```

Use the current date for the consolidation date (check CLAUDE.md for currentDate).

## Verification

- Confirm `~/.wlm/SOUL.md` updated with the canonical memory path
- List contents of `~/.wlm/memory/` to confirm structure
