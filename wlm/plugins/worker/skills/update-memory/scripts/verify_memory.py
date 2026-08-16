#!/usr/bin/env python3
"""Discover and validate a WLM memory root without mutating it by default."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable, Optional

KNOWN_TOP_LEVEL_DIRECTORIES = ("corps", "projects", "teams")
CANONICAL_PATH_PATTERN = re.compile(
    r"^\s*-?\s*Canonical path\s*:\s*(.+?)\s*$", re.IGNORECASE
)


def normalized(path: Path) -> Path:
    """Return a normalized absolute path without requiring it to exist."""
    return Path(os.path.abspath(os.path.expandvars(str(path.expanduser()))))


def git_root() -> Optional[Path]:
    """Return the current Git root, or None outside a repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            check=False,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return normalized(Path(result.stdout.strip()))


def canonical_path_from_soul() -> Optional[Path]:
    """Read a valid canonical memory path from ~/.wlm/SOUL.md."""
    soul_path = Path.home() / ".wlm" / "SOUL.md"
    if not soul_path.is_file():
        return None

    in_memory_section = False
    try:
        lines = soul_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return None

    for line in lines:
        if line.startswith("## "):
            in_memory_section = line.strip().lower() == "## memory"
            continue
        if not in_memory_section:
            continue
        match = CANONICAL_PATH_PATTERN.match(line)
        if not match:
            continue
        raw_path = match.group(1).strip().strip("`\"'")
        candidate = normalized(Path(raw_path))
        if candidate.is_dir():
            return candidate
    return None


def existing_candidates() -> list[Path]:
    """Return distinct existing memory candidates in discovery order."""
    candidates = [Path.cwd() / "memory"]
    repository_root = git_root()
    if repository_root is not None:
        candidates.append(repository_root / "memory")
    candidates.append(Path.home() / ".wlm" / "memory")

    distinct: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        candidate = normalized(candidate)
        if not candidate.is_dir():
            continue
        key = os.path.normcase(str(candidate.resolve()))
        if key not in seen:
            seen.add(key)
            distinct.append(candidate)
    return distinct


def discover_memory_root() -> tuple[Optional[Path], list[Path]]:
    """Return a unique canonical root, plus candidates when ambiguous."""
    canonical = canonical_path_from_soul()
    if canonical is not None:
        return canonical, []
    candidates = existing_candidates()
    if len(candidates) == 1:
        return candidates[0], []
    return None, candidates


def validate_root(memory_root: Path) -> list[str]:
    """Validate known hierarchy nodes without requiring empty scaffolding."""
    errors: list[str] = []
    if not memory_root.exists():
        return [f"Memory root does not exist: {memory_root}"]
    if not memory_root.is_dir():
        return [f"Memory root is not a directory: {memory_root}"]

    for name in KNOWN_TOP_LEVEL_DIRECTORIES:
        candidate = memory_root / name
        if candidate.exists() and not candidate.is_dir():
            errors.append(f"Expected directory but found another type: {candidate}")
    return errors


def count_files(paths: Iterable[Path]) -> int:
    """Count files below the supplied roots."""
    return sum(1 for path in paths for candidate in path.rglob("*") if candidate.is_file())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--memory-root",
        type=Path,
        help="Validate this explicit memory root instead of auto-discovering one.",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create --memory-root if missing; never creates directory scaffolding.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.create and args.memory_root is None:
        print("Error: --create requires an explicit --memory-root.")
        return 2

    if args.memory_root is not None:
        memory_root = normalized(args.memory_root)
        if args.create:
            memory_root.mkdir(parents=True, exist_ok=True)
    else:
        memory_root, candidates = discover_memory_root()
        if memory_root is None:
            if candidates:
                print("Error: multiple memory roots exist and no valid canonical path is recorded:")
                for candidate in candidates:
                    print(f"  - {candidate}")
                print("Use --memory-root or consolidate the stores before writing.")
            else:
                print("Error: no memory root exists and no valid canonical path is recorded.")
                print("Choose a destination explicitly before creating one.")
            return 2

    errors = validate_root(memory_root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Memory root: {memory_root}")
    print(f"Files: {count_files([memory_root])}")
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
