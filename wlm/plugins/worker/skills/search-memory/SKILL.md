---
name: search-memory
description: Search and retrieve information from memory files. Use when user asks to find stored information, recall previous context, search memory, look up documented knowledge, or find team/project details. Also proactively search memory when context about teams, tools, or projects would help complete tasks. Triggers for phrases like "search memory", "what did we store", "find in memory", "look up", "do we have", "recall", etc.
---

Version: 1.0.0

This skill searches through memory files to find stored information. Memory is organized in `memory/` directory with subdirectories for corps, projects, and teams. The agent should also proactively search memory when working on tasks that involve team context, tools, or project history.

**Finding Memory:** The `memory/` directory is relative to the current working directory. Check:
1. Current directory first (`./memory/`)
2. Git repository root (`git rev-parse --show-toplevel` + `/memory/`)
3. Home directory (`~/.wlm/memory/`)

## When to Search Memory

**Explicit requests:**
- User asks: "search memory for...", "what did we store about...", "find information about..."

**Proactive searches (agent-initiated):**
- Starting work on a new project — search for existing project context
- Communicating with a team — search for team preferences and tools
- Using tools — search for tool configurations and team norms
- Onboarding to new context — search for relevant team/project information
- Before asking the user questions that might be answered in memory

## Memory Structure

```
memory/
├── corps/           # Company-level information
│   └── tools/       # Communication and office tools
├── projects/        # Project-specific information
│   └── [project]/  # Per-project folders
└── teams/           # Team and organizational information
    └── [team]/     # Per-team folders
```

Each folder may have time-based subfolders (YYYY-MM format).

## Search Process

### Step 1: Find Relevant Memory Files

Search the memory directory for files matching the user's query. Use grep to search for:
- Keywords from the user's question
- Topic-related terms
- Team/project names

**Memory search locations:**
- `memory/corps/tools/` - Company-wide tools, communication, office suites
- `memory/teams/[team-name]/` - Team-specific information
- `memory/projects/[project-name]/` - Project details

### Step 2: Read Matching Files

For each file that matches the search query:
1. Read the file contents
2. Extract relevant sections
3. Note the file path and date for context

### Step 3: Present Results

When user explicitly asked: Format the findings clearly with sources

```markdown
# Search Results: [query]

## Sources
- memory/path/to/file.md (YYYY-MM-DD)

## Findings
[Relevant information extracted from memory]
```

When agent proactively searched: Integrate the findings into the task naturally

### Step 4: Handle Missing Information

If no matching information is found:
- For explicit requests: Tell the user what was searched and suggest adding it
- For proactive searches: Note that no memory exists yet and proceed without it, or ask user if they want to add context

## Search Tips

- Search both file names and file contents
- Look in multiple subdirectories if the topic could span areas
- Check for time-based subfolders (YYYY-MM/) which may contain newer information
- If information seems outdated, note this for the user
