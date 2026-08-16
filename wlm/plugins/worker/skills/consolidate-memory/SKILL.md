---
name: consolidate-memory
description: Resolve ambiguous or fragmented WLM memory storage by finding distinct memory roots, choosing a canonical location, safely consolidating files, and recording the result. Use when the user asks to consolidate or migrate memory, multiple memory roots are discovered, or memory tools cannot determine the canonical store. Do not use for ordinary lookup or merely because a new work session started; use worker:search-memory to recover prior context.
---

# Consolidate Memory

Version: 1.1.0

Find the actual memory roots, preserve their contents, and establish one canonical store without overwriting unrelated files or configuration.

## Workflow

### 1. Discover candidates read-only

- Inspect `~/.wlm/SOUL.md` first. If its `## Memory` section names an existing canonical path, treat that path as authoritative unless the user explicitly requests a migration.
- Check these candidates: `memory/` in the current directory, `memory/` at the Git repository root when one exists, and `~/.wlm/memory/`.
- Resolve candidates to normalized absolute paths and deduplicate them. The current directory and repository root may identify the same store; junctions or symlinks may also point to one store.
- Use platform-native read-only commands. Do not assume Bash; on PowerShell use `Get-ChildItem` and `Test-Path`. A directory outside a Git repository is valid and must not make the discovery step fail.
- Record which distinct locations exist and inventory their relative file paths. Do not create, copy, move, or delete anything during discovery.

### 2. Select the canonical store

- If `SOUL.md` already names a valid store, keep it unless the user requested a different destination.
- If exactly one distinct store exists, report it as canonical. There is nothing to consolidate.
- If no store exists, ask the user where memory should live. Recommend `~/.wlm/memory/` only as a default, not as an already-decided destination.
- If multiple distinct stores exist and no valid canonical path is recorded, propose `~/.wlm/memory/` as the destination. Do not merge until the user has explicitly requested consolidation or approved the destination.

### 3. Consolidate without data loss

Before copying, compare each source by relative path and content hash:

- Copy files that do not exist at the destination.
- Skip byte-identical duplicates.
- Never overwrite divergent files that share a relative path. Report each conflict and ask the user whether to keep one version, rename both, or merge their contents.
- Copy by default so the original sources remain recoverable. Remove source files or directories only when the user explicitly asks and the copied files have been verified.
- Preserve existing directory structure. Create `corps/`, `projects/`, or `teams/` subdirectories only when content requires them; do not create empty scaffolding.

### 4. Track the canonical path

Update only the `## Memory` section of `~/.wlm/SOUL.md`; preserve every other section and any user formatting outside that section. Avoid rewriting the file when the recorded path is already correct.

Use fields that describe what actually happened:

- `Canonical path`: the confirmed location.
- `Last verified`: the current date.
- `Consolidated`: the current date only when files were actually combined.
- `Sources`: the distinct source locations involved in an actual consolidation.

If `SOUL.md` does not exist, create a minimal file only after the canonical location is confirmed. Obtain the current date from the runtime environment or system context rather than assuming a repository instruction file contains it.

## Verification

- Confirm the canonical directory exists and `SOUL.md` points to its normalized path.
- Verify every copied file by size or content hash and confirm no divergent conflict was overwritten.
- Confirm only the intended `## Memory` section changed in an existing `SOUL.md`.
- Report the canonical path, inspected sources, copied files, skipped identical files, unresolved conflicts, and whether any sources were removed.
