---
name: update-memory
description: Save important information to memory after tasks, milestones, or discoveries. Use when user asks to remember something, save context, store a decision, or document a finding. Also proactively save when making decisions, meeting people, or discovering information useful for future work.
---

Version: 1.0.0

This skill saves important information to memory files for future reference. Memory is organized in `memory/` directory with subdirectories for corps, projects, and teams.

**Finding Memory:** The `memory/` directory is relative to the current working directory. Check:
1. Current directory first (`./memory/`)
2. Parent directory (`../memory/`)
3. Home directory (`~/.wlm/memory/`)

## When to Update Memory

**Explicit requests:**
- User asks: "remember this", "save this to memory", "store this decision", "don't forget"
- User says: "we should document this"

**Proactive saves (agent-initiated):**
- After completing a significant task or milestone
- When making important decisions
- When meeting new people (especially team members, contacts)
- When discovering solutions, tools, or approaches worth remembering
- When context is gathered that would be useful for future work

## Memory Structure

```
memory/
├── corps/           # Company-level information
│   └── tools/       # Communication and office tools
├── projects/        # Project-specific information
│   └── [project]/  # Per-project folders
└── teams/           # Team and organizational information
    └── [team]/     # Per-team folders
        └── roles/  # Role-based memory
```

## Update Process

### Step 1: Identify What to Save

Ask the user: "What should I remember from this?" if unclear.

Otherwise, infer from context:
- Completed actions → what was done, outcome
- People met → name, role, team, relevant context
- Decisions made → what, why, implications
- Solutions found → problem, solution, when useful

### Step 2: Determine Memory Path

| Type | Path |
|------|------|
| Team-related | `memory/teams/[team-name]/` |
| Project-related | `memory/projects/[project-name]/` |
| Company-wide | `memory/corps/` |
| Role-based | `memory/teams/roles/[role]/` |

### Step 3: Format Entry

Keep concise: 2-3 sentences max.

Include:
- What happened / what was learned
- Who is involved (name, role)
- When (date if relevant)
- Why it's useful for future

```markdown
# YYYY-MM-DD: [Topic]

[1-2 sentences describing what, who, and why useful]
```

### Step 4: Write to Memory

1. Check if relevant file already exists
2. If exists, append new entry with date header
3. If not, create new file with descriptive name
4. Use date-stamped filenames (YYYY-MM-DD-topic.md) or descriptive names

## Example

**Input:** User completed a meeting with Sarah from the backend team about API migration.

**Memory entry:**
```markdown
# 2026-03-13: API Migration Meeting

Met Sarah from backend team about API migration. She's the tech lead.
Key info: They're moving to GraphQL by Q2. Contact for questions: sarah@company.com
```
