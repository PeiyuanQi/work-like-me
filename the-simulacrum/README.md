# The Simulacrum

A long-running agent that replicates the user, powered by Claude Agent SDK.

## Overview

The Simulacrum is an autonomous agent that acts as a digital twin of the user. It:

- Loads skills from every skill group under `wlm/plugins/`
- Uses `~/.wlm/memory/` for persistent memory
- Runs continuously, processing tasks interactively or in batch mode

## Setup

```bash
cd the-simulacrum
uv sync
```

## Usage

### Interactive Mode

```bash
uv run python src/agent.py
```

### Batch Mode

```bash
uv run python src/agent.py "task 1" "task 2" "task 3"
```

## Loaded Skills

### Worker Skills (wlm:worker)

- **find-poc** - Find person of contact
- **consolidate-memory** - Consolidate memory location
- **update-memory** - Save to memory
- **notify-reviewer** - Notify MR reviewer
- **contact-new-teammate** - Contact new teammate
- **onboard-as-new-hire** - Onboard as new hire
- **search-memory** - Search memory
- **rank-office-decisions** - Rank office and daily work choices
- **ppt-style-selector** - Choose a PPT style before generating a deck
- **ppt-guizang-style** - Use the Guizang PPT style wrapper

### SWE Skills (wlm:swe)

- **create-merge-request** - Create MR/PR
- **prepare-code-for-commit** - Format/lint code
- **git-start-work** - Start new work
- **find-code-reviewer** - Find code reviewer
- **git-commit-push** - Commit and push
- **rank-software-decisions** - Rank software engineering choices

### CPA Skills (wlm:cpa)

- **tax-intake-and-research** - Gather tax facts and organize source-backed tax research
- **rank-finance-decisions** - Rank tax and personal finance choices

### Mechanical Skills (wlm:mechanical)

- **rank-mechanical-decisions** - Rank physical build, repair, tool, material, and regulated-device choices

## Configuration

- Model: Claude (uses Agent SDK default)
- Max turns: 50
- Memory: `~/.wlm/memory/`
- Skills: `../wlm/plugins/`
- Permission mode: acceptEdits
