---
name: prepare-code-for-commit
description: Format and lint code before committing. Use as the last step after large modifications or when user requests code cleanup. Checks for team-specific linting norms first (in repo config files and memory), falls back to default tools if none exist.
---

This skill formats and lints code to prepare it for commit. Always prioritize the team's established norms over defaults.

Version: 1.0.0

## Step 1: Detect Team Norms

Before running any linters, check for team-specific configuration in TWO places:

### A. Check Memory for Team Norms

Search memory files for coding standards and linting preferences:
- Look in `memory/corps/tools/` for linter/formatter configurations
- Look in `memory/teams/[team-name]/*/` for team-specific guidelines
- Search for files containing: "lint", "format", "code style", "pre-commit", "formatter"

### B. Check Repository Config Files

Also check for team-specific configuration files in the repository:

**Common team norm files to check for:**
- `.pre-commit-config.yaml` - Pre-commit hook configurations
- `pyproject.toml` - Python project config (may contain ruff config)
- `ruff.toml` - Ruff linter/formatter configuration
- `setup.cfg` - Python setup configuration
- `.eslintrc`, `eslint.config.js` - JavaScript/TypeScript linting
- `.pylintrc` - Pylint configuration
- `Makefile` - May contain lint/format commands
- `.editorconfig` - EditorConfig for cross-editor consistency

**If team norms exist (from memory or repo):** Follow the configurations found. Run the exact linters and formatters specified.

**If no team norms found:** Proceed to Step 2.

## Step 2: Apply Default Tools by Language

If no team-specific configuration exists, use these defaults:

### Python
- **Formatter & Linter:** ruff (replaces black, isort, and flake8 in a single tool)
  - `ruff format` for formatting (replaces black)
  - `ruff check --fix` for linting and import sorting (replaces flake8 and isort)
- **Style guide:** Google Python Style Guide
- **Conflict resolution:** If rules conflict, follow Google Python Style Guide

### JavaScript/TypeScript
- **Formatter:** prettier
- **Linter:** eslint

### Go
- **Formatter:** gofmt
- **Linter:** golangci-lint

### Rust
- **Formatter:** rustfmt
- **Linter:** clippy

### Other Languages
- Use language-appropriate standard tools
- If unsure, ask the user what tools they prefer

## Step 3: Run the Linters

Execute the formatters and linters in this order:
1. Formatters first (to fix style issues)
2. Linters second (to catch issues)

## Step 4: Report Results

After running, summarize:
- Which tools ran
- What changes were made
- Any errors or warnings that need attention
