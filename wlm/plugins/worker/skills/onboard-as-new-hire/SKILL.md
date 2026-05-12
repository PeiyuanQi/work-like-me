---
name: onboard-as-new-hire
description: Onboard the agent itself by discovering communication tools, office suites, and organizational structure. Use when user asks to onboard the agent, set up agent context, agent needs to learn about the team, or discover available tools. Triggers for phrases like "onboard yourself", "introduce yourself to the team", "what tools do we use", "discover communication tools", "set up your context", etc.
---

# Onboard as New Hire

Version: 1.0.0

This skill helps an agent onboard itself by discovering and documenting the team's communication tools, office suites, and organizational structure — the same context a new human hire would need.

## Memory Structure

The memory is organized into three main sections:

```
memory/
├── corps/           # Company-level information
│   └── tools/       # Communication and office tools
├── projects/        # Project-specific information
│   └── [project]/  # Per-project folders
└── teams/           # Team and organizational information
    └── [team]/     # Per-team folders
```

Each folder should have a time-based subfolder label in format `YYYY-MM/` to track when information was added.

## Discovery Process

### Step 1: Ask Discovery Questions

Start by asking the user questions to discover the team's tools so the agent can operate effectively. Frame questions conversationally — as if you were a new team member asking about the tools available to you:

**Communication Tools:**
- "What chat tool does your team use most? Slack, Microsoft Teams, Google Chat, Discord, or something else?"
- "Do you use any other communication tools besides [primary tool]?"
- "Which tool should I use to communicate with the team on your behalf?"

**Office Suites:**
- "Does your company use Microsoft Office, Google Workspace (formerly G Suite), or Feishu/Lark?"
- "What's your primary email platform?"
- "What tools do I have access to for creating or editing documents?"

**Organization:**
- "What's the team name and who are the key team members?"
- "Are there any peer teams or departments we should know about?"
- "Who should I coordinate with for [specific tasks]?"

### Step 2: Document Findings in Memory

After discovering the tools, create or update memory files:

#### For Corps/Tools (company-wide tools)

Create: `memory/corps/tools/YYYY-MM/communication.md`
```markdown
# Communication Tools

**Primary Chat Tool:** [tool name]
**Secondary Tools:** [other tools, if any]
**Discovery Date:** YYYY-MM-DD

## Details
- [Tool name]: [usage context, channels, etc.]
```

Create: `memory/corps/tools/YYYY-MM/office_suite.md`
```markdown
# Office Suite

**Primary Suite:** [Microsoft Office / Google Workspace / Feishu / Lark / Other]
**Email:** [email platform]
**Discovery Date:** YYYY-MM-DD

## Details
- [Suite name]: [products used, context]
```

#### For Teams

Create: `memory/teams/[team-name]/YYYY-MM/info.md`
```markdown
# Team: [Team Name]

**Discovered:** YYYY-MM-DD
**Communication Tool:** [tool]
**Office Suite:** [suite]
**Key Members:** [names and roles]

## Notes
[Any additional context]
```

#### For Projects (if applicable)

Create: `memory/projects/[project-name]/YYYY-MM/tools.md`
```markdown
# Project: [Project Name]

**Discovered:** YYYY-MM-DD
**Communication:** [tool used for this project]
**Tools:** [specific tools used]

## Team
[Associated team members]
```

## Conflict Resolution

When new information conflicts with existing memory entries:

1. **Compare timestamps**: Check the `YYYY-MM` folder labels
2. **If new entry is more recent**:
   - Add the new information with a note about the update
   - Mark the old entry as "superseded" with a reference to the new file
3. **If old entry might be outdated**:
   - Add a comment questioning the old entry
   - Ask the user to confirm which is correct
4. **Resolution format**:
   ```
   ## Conflict Resolution [YYYY-MM-DD]
   - Old (from YYYY-MM): [old info]
   - New (from YYYY-MM): [new info]
   - Resolution: [explanation]
   ```

## Memory Queries

The memory should be queriable. When asked about:
- "What chat tool does the team use?" → Read `memory/corps/tools/*/communication.md`
- "What office suite?" → Read `memory/corps/tools/*/office_suite.md`
- "Tell me about [team]" → Read `memory/teams/[team-name]/*/info.md`
- "What tools for [project]" → Read `memory/projects/[project-name]/*/tools.md`

## Summary Output

After completing onboarding, provide a summary to the user:

```markdown
# Agent Onboarding Summary

## Communication Tools
- Primary: [tool]
- Others: [list]
- How to reach team: [channels, mentions, etc.]

## Office Suite
- Suite: [name]
- Email: [platform]
- Available tools: [list]

## Team
- Name: [team name]
- Members: [list]
- Key contacts: [who to ask for what]

## Memory Locations
- Tools: memory/corps/tools/YYYY-MM/
- Team: memory/teams/[name]/YYYY-MM/

## Next Steps
- [Suggested first actions with the discovered context]
```

## Important Notes

- Always use time-based subfolders (YYYY-MM format) for new entries
- Keep memory files markdown-based for easy reading
- Ask clarifying questions if tool usage is unclear
- Update existing files rather than creating duplicates when possible
