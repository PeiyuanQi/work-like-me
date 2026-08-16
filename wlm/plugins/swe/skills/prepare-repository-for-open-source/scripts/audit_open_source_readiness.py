#!/usr/bin/env python3
"""Fast, dependency-free preflight for repository open-source readiness.

This script is intentionally conservative. It identifies evidence that needs a
human decision; it does not certify security, ownership, or license compliance.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 fallback
    tomllib = None


MAX_TEXT_BYTES = 2 * 1024 * 1024
LARGE_WARNING_BYTES = 10 * 1024 * 1024
LARGE_BLOCKER_BYTES = 100 * 1024 * 1024
SEVERITY_ORDER = {"blocker": 0, "warning": 1, "improvement": 2, "info": 3}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    evidence: str | None = None


def run(
    command: Sequence[str],
    cwd: Path,
    *,
    text: bool = True,
) -> subprocess.CompletedProcess[str] | subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=text,
    )


def git_text(root: Path, *args: str) -> str:
    result = run(["git", *args], root, text=True)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def git_bytes(root: Path, *args: str) -> bytes:
    result = run(["git", *args], root, text=False)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).decode("utf-8", "replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def nul_paths(data: bytes) -> list[str]:
    return [
        item.decode("utf-8", "surrogateescape").replace("\\", "/")
        for item in data.split(b"\0")
        if item
    ]


def read_text(path: Path) -> str | None:
    try:
        if not path.is_file() or path.stat().st_size > MAX_TEXT_BYTES:
            return None
        data = path.read_bytes()
    except OSError:
        return None
    if b"\0" in data[:8192]:
        return None
    return data.decode("utf-8", "replace")


def find_root_file(files: Iterable[str], prefixes: Sequence[str]) -> list[str]:
    found: list[str] = []
    for rel in files:
        if "/" in rel:
            continue
        lowered = rel.lower()
        if any(
            lowered == prefix
            or lowered.startswith(prefix + ".")
            or lowered.startswith(prefix + "-")
            or lowered.startswith(prefix + "_")
            for prefix in prefixes
        ):
            found.append(rel)
    return sorted(found)


def find_community_file(files: Iterable[str], prefixes: Sequence[str]) -> list[str]:
    found: list[str] = []
    allowed_parents = {"", ".github", "docs"}
    for rel in files:
        path = Path(rel)
        parent = path.parent.as_posix()
        if parent == ".":
            parent = ""
        if parent not in allowed_parents:
            continue
        lowered = path.name.lower()
        if any(
            lowered == prefix
            or lowered.startswith(prefix + ".")
            or lowered.startswith(prefix + "-")
            or lowered.startswith(prefix + "_")
            for prefix in prefixes
        ):
            found.append(rel)
    return sorted(found)


def looks_like_placeholder(line: str) -> bool:
    lowered = line.lower()
    markers = (
        "example",
        "sample",
        "fixture",
        "dummy",
        "placeholder",
        "redacted",
        "changeme",
        "your_",
        "your-",
        "<token",
        "<secret",
        "{{",
    )
    return any(marker in lowered for marker in markers)


def compact_paths(paths: Sequence[str], limit: int = 8) -> str:
    shown = list(paths[:limit])
    suffix = "" if len(paths) <= limit else f" (+{len(paths) - limit} more)"
    return ", ".join(shown) + suffix


def add(
    findings: list[Finding],
    severity: str,
    code: str,
    message: str,
    evidence: str | None = None,
) -> None:
    findings.append(Finding(severity, code, message, evidence))


def inspect_root_documents(root: Path, files: set[str], findings: list[Finding]) -> None:
    readmes = find_root_file(files, ("readme",))
    licenses = find_root_file(files, ("license", "copying"))
    contributing = find_community_file(files, ("contributing",))
    security = find_community_file(files, ("security",))
    conduct = find_community_file(files, ("code_of_conduct", "code-of-conduct"))
    support = find_community_file(files, ("support",))
    changelog = find_community_file(files, ("changelog", "changes", "history"))

    if not readmes:
        add(findings, "blocker", "DOC001", "No root README was found.")
    else:
        add(findings, "info", "DOC101", "Root README found.", compact_paths(readmes))

    if not licenses:
        add(findings, "blocker", "LIC001", "No root LICENSE or COPYING file was found.")
    else:
        add(findings, "info", "LIC101", "Root license file found.", compact_paths(licenses))

    if not contributing:
        add(
            findings,
            "warning",
            "COM001",
            "No CONTRIBUTING guide was found in the root, .github, or docs directory.",
        )
    if not security:
        add(
            findings,
            "warning",
            "SEC001",
            "No SECURITY policy was found in the root, .github, or docs directory.",
        )
    if not conduct:
        add(
            findings,
            "improvement",
            "COM002",
            "No code of conduct was found in the root, .github, or docs directory.",
        )
    if not support:
        add(
            findings,
            "improvement",
            "COM003",
            "No SUPPORT policy was found in the root, .github, or docs directory.",
        )
    if not changelog:
        add(
            findings,
            "improvement",
            "REL001",
            "No changelog/history file was found in the root or docs directory.",
        )

    public_docs = sorted(set(readmes + licenses + contributing + security + conduct + support))
    placeholder_re = re.compile(
        r"(?i)(\[(?:year|copyright holder|licensor legal name|governing law|"
        r"exclusive court|contact email|insert name)\]|"
        r"<(?:copyright holder|licensor legal name|governing law|exclusive court)>|"
        r"\bTBD\b|\bCHANGEME\b)"
    )
    for rel in public_docs:
        text = read_text(root / rel)
        if text and placeholder_re.search(text):
            severity = "blocker" if rel in licenses else "warning"
            add(
                findings,
                severity,
                "DOC002",
                "Unresolved public-facing placeholder detected.",
                rel,
            )


def inspect_license_classification(
    root: Path, files: set[str], findings: list[Finding]
) -> None:
    license_files = find_root_file(files, ("license", "copying"))
    readme_files = find_root_file(files, ("readme",))
    license_text = "\n".join(
        text for rel in license_files if (text := read_text(root / rel)) is not None
    )
    readme_text = "\n".join(
        text for rel in readme_files if (text := read_text(root / rel)) is not None
    )
    if not license_text:
        return

    normalized = license_text.lower().replace("royalty-free", "")
    restriction_patterns = {
        "non-commercial restriction": r"\bnon[- ]commercial\b",
        "field-of-use restriction": r"\bfield[- ]of[- ]use\b",
        "revenue threshold": r"\b(?:product )?revenue threshold\b",
        "royalty obligation": (
            r"\b(?:owes?|payable|due|accrued|remit(?:ted)?)\b[^\n]{0,80}"
            r"\broyalt(?:y|ies)\b|"
            r"\broyalt(?:y|ies)\b[^\n]{0,80}"
            r"\b(?:owes?|payable|due|accrued|rates?|obligation)\b"
        ),
        "mandatory product display": (
            r"\b(?:commercial\s+)?product\b[^\n]{0,160}"
            r"\b(?:must|required to)\s+display\b"
        ),
        "commercial-use condition": r"\bcommercial use\s+(?:requires|must|only)\b",
        "restricted-use clause": r"\bno\s+(?:military|commercial|production)\s+use\b",
    }
    detected = [
        label
        for label, pattern in restriction_patterns.items()
        if re.search(pattern, normalized, re.IGNORECASE)
    ]
    claims_open_source = bool(
        re.search(
            r"(?i)\b(open[- ]source|OSI[- ]approved|open source initiative)\b",
            readme_text,
        )
    )
    known_open_source_markers = (
        "permission is hereby granted, free of charge",
        "apache license\nversion 2.0",
        "mozilla public license version 2.0",
        "gnu general public license",
        "gnu lesser general public license",
        "gnu affero general public license",
        "redistribution and use in source and binary forms",
        "isc license",
        "the unlicense",
        "eclipse public license",
        "european union public licence",
        "common development and distribution license",
        "boost software license",
        "artistic license",
        "zlib license",
    )
    resembles_known_license = any(
        marker in license_text.lower() for marker in known_open_source_markers
    )
    if detected and claims_open_source:
        add(
            findings,
            "blocker",
            "LIC002",
            "README appears to call a restricted/custom license open source.",
            ", ".join(detected),
        )
    elif detected:
        add(
            findings,
            "blocker",
            "LIC003",
            "License restriction signals are incompatible with an open-source "
            "release; choose an OSI-approved license or classify the project "
            "as source-available instead.",
            ", ".join(detected),
        )
    elif resembles_known_license:
        add(
            findings,
            "info",
            "LIC102",
            "License text resembles a common OSI-approved license; manually "
            "confirm the exact license and version.",
            compact_paths(license_files),
        )
    else:
        add(
            findings,
            "warning",
            "LIC004",
            "License text was not recognized by the limited heuristic; manually "
            "confirm the exact license and version are OSI-approved.",
            compact_paths(license_files),
        )


SENSITIVE_PATH_PATTERNS = (
    re.compile(r"(?i)(^|/)\.env(?:$|\.)"),
    re.compile(r"(?i)(^|/)(?:id_rsa|id_ed25519)(?:$|\.)"),
    re.compile(r"(?i)\.(?:pem|p12|pfx|key|keystore)$"),
    re.compile(r"(?i)(^|/)(?:credentials?|secrets?|auth|tokens?)(?:[._/-]|$)"),
    re.compile(r"(?i)service[-_]?account.*\.json$"),
)

SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    (
        "GitHub token",
        re.compile(
            r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"
        ),
    ),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    ("Stripe live key", re.compile(r"\bsk_live_[0-9A-Za-z]{16,}\b")),
    (
        "credential assignment",
        re.compile(
            r"""(?ix)
            \b(api[_-]?key|client[_-]?secret|access[_-]?token|refresh[_-]?token|password)
            \b\s*[:=]\s*["']?([A-Za-z0-9_./+=:@-]{12,})
            """
        ),
    ),
)

LOCAL_PATH_RE = re.compile(
    r"(?:[A-Za-z]:\\Users\\[^\\\s\"']+|/Users/[^/\s\"']+|/home/[^/\s\"']+)"
)
CONFIDENTIAL_RE = re.compile(
    r"(?im)^\s*(?:\[?confidential\]?|internal only|do not distribute|under nda)\b"
)


def sensitive_path(path: str) -> bool:
    lowered = path.lower()
    if any(
        marker in lowered
        for marker in (".example", ".sample", "/examples/", "/samples/", "/fixtures/")
    ):
        return False
    return any(pattern.search(path) for pattern in SENSITIVE_PATH_PATTERNS)


def inspect_paths_and_content(
    root: Path,
    current_files: set[str],
    tracked_files: set[str],
    findings: list[Finding],
) -> None:
    suspicious_current = sorted(path for path in current_files if sensitive_path(path))
    if suspicious_current:
        add(
            findings,
            "warning",
            "SEC002",
            "Sensitive-looking filenames require manual review.",
            compact_paths(suspicious_current),
        )

    secret_hits: list[str] = []
    local_path_hits: list[str] = []
    confidential_hits: list[str] = []
    large_warning: list[str] = []
    large_blocker: list[str] = []
    this_script = Path(__file__).resolve()

    for rel in sorted(current_files):
        path = root / rel
        try:
            if path.is_symlink() or not path.is_file() or path.resolve() == this_script:
                continue
            size = path.stat().st_size
        except OSError:
            continue

        if size >= LARGE_BLOCKER_BYTES:
            large_blocker.append(f"{rel} ({size / (1024 * 1024):.1f} MiB)")
        elif size >= LARGE_WARNING_BYTES:
            large_warning.append(f"{rel} ({size / (1024 * 1024):.1f} MiB)")

        text = read_text(path)
        if text is None:
            continue

        if LOCAL_PATH_RE.search(text):
            local_path_hits.append(rel)
        if CONFIDENTIAL_RE.search(text):
            confidential_hits.append(rel)

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line) and not looks_like_placeholder(line):
                    classification = "tracked" if rel in tracked_files else "untracked"
                    secret_hits.append(
                        f"{rel}:{line_number} ({label}, {classification})"
                    )
                    break

    if secret_hits:
        add(
            findings,
            "blocker",
            "SEC003",
            "Potential live secret material detected. Values are intentionally omitted.",
            compact_paths(secret_hits, 12),
        )
    if local_path_hits:
        add(
            findings,
            "warning",
            "BND001",
            "Developer-machine absolute paths were found and may break clean "
            "clones or disclose usernames.",
            compact_paths(sorted(set(local_path_hits))),
        )
    if confidential_hits:
        add(
            findings,
            "warning",
            "PRV001",
            "Confidentiality markers were found; confirm every occurrence is "
            "intended for public disclosure.",
            compact_paths(sorted(set(confidential_hits))),
        )
    if large_blocker:
        add(
            findings,
            "blocker",
            "PKG001",
            "Files at or above 100 MiB need removal, LFS treatment, or explicit "
            "distribution review.",
            compact_paths(large_blocker),
        )
    if large_warning:
        add(
            findings,
            "warning",
            "PKG002",
            "Large files need provenance, history, hosting, and package-content review.",
            compact_paths(large_warning),
        )


def inspect_history_paths(
    root: Path, current_files: set[str], findings: list[Finding]
) -> None:
    result = run(["git", "rev-list", "--objects", "--all"], root, text=True)
    if result.returncode != 0:
        add(
            findings,
            "warning",
            "HIS001",
            "Could not enumerate reachable Git objects.",
            (result.stderr or result.stdout).strip()[:300],
        )
        return

    historical_paths: set[str] = set()
    for line in result.stdout.splitlines():
        if " " not in line:
            continue
        _, path = line.split(" ", 1)
        historical_paths.add(path.replace("\\", "/"))

    historical_sensitive = sorted(
        path
        for path in historical_paths
        if path not in current_files and sensitive_path(path)
    )
    if historical_sensitive:
        add(
            findings,
            "warning",
            "HIS002",
            "Sensitive-looking paths remain in reachable Git history.",
            compact_paths(historical_sensitive),
        )
    add(
        findings,
        "info",
        "HIS101",
        "History pathnames were inspected; commit contents still require a "
        "dedicated secret scanner.",
        f"{len(historical_paths)} reachable named objects",
    )


ASSET_SUFFIXES = {
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".svg",
    ".gif",
    ".mp3",
    ".wav",
    ".ogg",
    ".mp4",
    ".glb",
    ".gltf",
    ".fbx",
    ".obj",
    ".onnx",
    ".parquet",
    ".sqlite",
    ".db",
    ".dll",
    ".so",
    ".dylib",
    ".exe",
}


def inspect_third_party_surface(files: set[str], findings: list[Finding]) -> None:
    root_notices = find_root_file(
        files,
        (
            "notice",
            "third_party",
            "third-party",
            "third_party_licenses",
            "third-party-licenses",
            "sbom",
        ),
    )
    assets = sorted(
        rel for rel in files if Path(rel).suffix.lower() in ASSET_SUFFIXES
    )
    vendored = sorted(
        rel
        for rel in files
        if any(
            part.lower() in {"vendor", "vendored", "third_party", "third-party", "extern"}
            for part in Path(rel).parts
        )
    )
    if assets and not root_notices:
        add(
            findings,
            "warning",
            "TPR001",
            "Binary/media/data assets exist without an obvious root notice or "
            "third-party inventory.",
            f"{len(assets)} files; examples: {compact_paths(assets)}",
        )
    elif assets:
        add(
            findings,
            "info",
            "TPR101",
            "Binary/media/data assets require per-item provenance review.",
            f"{len(assets)} files; notice candidates: {compact_paths(root_notices)}",
        )
    if vendored and not root_notices:
        add(
            findings,
            "warning",
            "TPR002",
            "Vendored/third-party paths exist without an obvious root notice inventory.",
            compact_paths(vendored),
        )
    if not root_notices:
        add(
            findings,
            "improvement",
            "TPR003",
            "No obvious SBOM or third-party notice inventory was found; decide "
            "whether the release artifacts require one.",
        )


def inspect_cargo(root: Path, files: set[str], findings: list[Finding]) -> None:
    manifests = sorted(rel for rel in files if Path(rel).name == "Cargo.toml")
    if not manifests or tomllib is None:
        return

    root_manifest = root / "Cargo.toml"
    workspace_package: dict[str, object] = {}
    if root_manifest.is_file():
        try:
            root_data = tomllib.loads(root_manifest.read_text(encoding="utf-8"))
            workspace_package = root_data.get("workspace", {}).get("package", {})
        except (OSError, tomllib.TOMLDecodeError):
            pass

    problems: list[str] = []
    for rel in manifests:
        try:
            data = tomllib.loads((root / rel).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        package = data.get("package")
        if not isinstance(package, dict):
            continue
        if package.get("publish") is False:
            continue

        license_value = package.get("license")
        license_file_value = package.get("license-file")
        if isinstance(license_value, dict) and license_value.get("workspace") is True:
            license_value = workspace_package.get("license")
        if isinstance(license_file_value, dict) and license_file_value.get("workspace") is True:
            license_file_value = workspace_package.get("license-file")

        if not license_value and not license_file_value:
            problems.append(f"{rel}: missing license/license-file")
        if isinstance(license_file_value, str):
            base = root if (
                isinstance(package.get("license-file"), dict)
                and package["license-file"].get("workspace") is True
            ) else (root / rel).parent
            if not (base / license_file_value).resolve().is_file():
                problems.append(f"{rel}: license-file not found ({license_file_value})")
        if not package.get("description") and not workspace_package.get("description"):
            problems.append(f"{rel}: missing description")
        if not package.get("repository") and not workspace_package.get("repository"):
            problems.append(f"{rel}: missing repository URL")
        if not package.get("readme") and not workspace_package.get("readme"):
            problems.append(f"{rel}: missing readme metadata")

    if problems:
        add(
            findings,
            "warning",
            "META001",
            "Publishable Cargo package metadata is incomplete or inconsistent.",
            compact_paths(problems, 12),
        )
    else:
        add(
            findings,
            "info",
            "META101",
            "Publishable Cargo package metadata includes license, description, "
            "repository, and README fields.",
        )
    if "Cargo.lock" not in files:
        add(
            findings,
            "improvement",
            "DEP001",
            "Cargo manifests exist without a tracked Cargo.lock; confirm this is "
            "intentional for the artifact type.",
        )


def inspect_package_json(root: Path, files: set[str], findings: list[Finding]) -> None:
    manifests = sorted(
        rel
        for rel in files
        if Path(rel).name == "package.json"
        and "node_modules" not in Path(rel).parts
    )
    problems: list[str] = []
    for rel in manifests:
        try:
            data = json.loads((root / rel).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("private") is True:
            continue
        for field in ("license", "repository", "description"):
            if not data.get(field):
                problems.append(f"{rel}: missing {field}")
    if problems:
        add(
            findings,
            "warning",
            "META002",
            "Publishable package.json metadata is incomplete.",
            compact_paths(problems, 12),
        )
    if manifests and not any(
        lock in files
        for lock in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb")
    ):
        add(
            findings,
            "warning",
            "DEP002",
            "JavaScript package manifests exist without an obvious tracked lockfile.",
        )


def inspect_pyproject(root: Path, files: set[str], findings: list[Finding]) -> None:
    manifests = sorted(rel for rel in files if Path(rel).name == "pyproject.toml")
    if not manifests or tomllib is None:
        return
    problems: list[str] = []
    for rel in manifests:
        try:
            data = tomllib.loads((root / rel).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        project = data.get("project")
        if not isinstance(project, dict):
            continue
        for field in ("description", "readme", "license"):
            if not project.get(field):
                problems.append(f"{rel}: missing project.{field}")
        urls = project.get("urls")
        if not isinstance(urls, dict) or not any(
            key.lower() in {"repository", "source", "homepage"} for key in urls
        ):
            problems.append(f"{rel}: missing project.urls repository/homepage")
    if problems:
        add(
            findings,
            "warning",
            "META003",
            "Publishable Python project metadata is incomplete.",
            compact_paths(problems, 12),
        )


def inspect_private_dependencies(
    root: Path, files: set[str], findings: list[Finding]
) -> None:
    manifest_names = {
        "cargo.toml",
        "package.json",
        "pyproject.toml",
        "go.mod",
        "pom.xml",
        "build.gradle",
        "build.gradle.kts",
        "requirements.txt",
    }
    private_hits: list[str] = []
    private_remote_re = re.compile(
        r"""(?ix)
        (git@[^:\s]+:|ssh://|file://|
        (?:registry|index)\s*[:=]\s*["']?https?://
        (?!github\.com|gitlab\.com|crates\.io|pypi\.org|npmjs\.org))
        """
    )
    path_ref_patterns = (
        re.compile(r"""(?ix)\b(?:path|file)\s*[:=]\s*["']([^"']+)["']"""),
        re.compile(r"""(?ix)["']file:([^"']+)["']"""),
    )
    for rel in sorted(files):
        if Path(rel).name.lower() not in manifest_names:
            continue
        text = read_text(root / rel)
        if not text:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if private_remote_re.search(line):
                private_hits.append(f"{rel}:{line_number}")
                continue
            for pattern in path_ref_patterns:
                match = pattern.search(line)
                if not match:
                    continue
                value = match.group(1).strip()
                if "$" in value or "{" in value:
                    private_hits.append(f"{rel}:{line_number} (unresolved path)")
                    break
                absolute_like = bool(
                    re.match(r"^(?:[A-Za-z]:[\\/]|/)", value)
                )
                if absolute_like:
                    private_hits.append(f"{rel}:{line_number} (absolute path)")
                    break
                resolved = ((root / rel).parent / value).resolve()
                try:
                    resolved.relative_to(root)
                except ValueError:
                    private_hits.append(f"{rel}:{line_number} (outside repository)")
                break
    if private_hits:
        add(
            findings,
            "warning",
            "BND002",
            "Manifest references may require private/local repositories, registries, or paths.",
            compact_paths(private_hits, 12),
        )


def inspect_github(root: Path, files: set[str], findings: list[Finding]) -> None:
    workflows = sorted(
        rel
        for rel in files
        if rel.startswith(".github/workflows/")
        and Path(rel).suffix.lower() in {".yml", ".yaml"}
    )
    if not workflows:
        add(
            findings,
            "warning",
            "CI001",
            "No GitHub Actions workflows were found; verify equivalent public CI exists.",
        )
        return

    mutable_actions: list[str] = []
    permissions_seen = False
    uses_re = re.compile(r"(?m)^\s*-\s*uses:\s*([^#\s]+)")
    for rel in workflows:
        text = read_text(root / rel) or ""
        if re.search(r"(?m)^\s*permissions\s*:", text):
            permissions_seen = True
        for match in uses_re.finditer(text):
            action = match.group(1)
            if action.startswith("./") or action.startswith("docker://"):
                continue
            if "@" not in action:
                mutable_actions.append(f"{rel}: {action} (no ref)")
                continue
            _, ref = action.rsplit("@", 1)
            if not re.fullmatch(r"[0-9a-fA-F]{40}", ref):
                mutable_actions.append(f"{rel}: {action}")

    if mutable_actions:
        add(
            findings,
            "warning",
            "CI002",
            "Third-party workflow actions are not pinned to full commit SHAs; "
            "review the supply-chain decision.",
            compact_paths(mutable_actions, 12),
        )
    if not permissions_seen:
        add(
            findings,
            "warning",
            "CI003",
            "No explicit workflow permissions block was detected; verify "
            "least-privilege token access.",
        )


def inspect_submodules(root: Path, files: set[str], findings: list[Finding]) -> None:
    if ".gitmodules" not in files:
        return
    text = read_text(root / ".gitmodules") or ""
    urls = re.findall(r"(?m)^\s*url\s*=\s*(.+?)\s*$", text)
    private_urls = [
        url
        for url in urls
        if url.startswith("git@")
        or url.startswith("ssh://")
        or re.search(r"(?i)(localhost|127\.0\.0\.1|10\.\d+\.\d+\.\d+|192\.168\.)", url)
    ]
    if private_urls:
        add(
            findings,
            "warning",
            "BND003",
            "Submodule URLs may not be anonymously accessible to public consumers.",
            compact_paths(private_urls),
        )
    add(
        findings,
        "info",
        "BND101",
        "Submodules exist and need independent license, history, and availability review.",
        f"{len(urls)} configured URLs",
    )


def inspect_git_state(
    root: Path, untracked_files: set[str], findings: list[Finding]
) -> None:
    status = git_text(root, "status", "--porcelain=v1")
    if status.strip():
        add(
            findings,
            "warning",
            "GIT001",
            "Working tree is not clean; bind release evidence to an exact committed revision.",
            f"{len(status.splitlines())} status entries",
        )
    if untracked_files:
        add(
            findings,
            "info",
            "GIT101",
            "Untracked, non-ignored files were included in current-tree scanning.",
            f"{len(untracked_files)} files",
        )
    add(
        findings,
        "info",
        "GIT102",
        "Ignored files are not content-scanned by this preflight; inspect "
        "relevant ignored artifacts separately.",
    )


def render_markdown(root: Path, revision: str, findings: list[Finding]) -> str:
    counts = {
        severity: sum(1 for finding in findings if finding.severity == severity)
        for severity in SEVERITY_ORDER
    }
    verdict = (
        "NO-GO"
        if counts["blocker"]
        else "CONDITIONAL"
        if counts["warning"]
        else "GO"
    )
    lines = [
        "# Open-Source Readiness Preflight",
        "",
        f"- Repository: {root}",
        f"- Revision: {revision}",
        f"- Verdict: {verdict}",
        (
            "- Findings: "
            f"{counts['blocker']} blockers, {counts['warning']} warnings, "
            f"{counts['improvement']} improvements, {counts['info']} informational"
        ),
        "",
    ]
    for severity, title in (
        ("blocker", "Blockers"),
        ("warning", "Warnings"),
        ("improvement", "Improvements"),
        ("info", "Informational"),
    ):
        group = sorted(
            (finding for finding in findings if finding.severity == severity),
            key=lambda finding: (finding.code, finding.message),
        )
        if not group:
            continue
        lines.extend([f"## {title}", ""])
        for finding in group:
            item = f"- [{finding.code}] {finding.message}"
            if finding.evidence:
                item += f" Evidence: {finding.evidence}"
            lines.append(item)
        lines.append("")
    lines.extend(
        [
            "## Limits",
            "",
            "- This preflight is heuristic and does not certify legal rights, "
            "security, privacy, or license compliance.",
            "- It does not scan ignored-file contents, every historical blob, "
            "remote forks/caches, issue trackers, release downloads, container "
            "layers, or external services.",
            "- Resolve findings against the exact artifacts and public refs intended for release.",
            "",
        ]
    )
    return "\n".join(lines)


def render_json(root: Path, revision: str, findings: list[Finding]) -> str:
    counts = {
        severity: sum(1 for finding in findings if finding.severity == severity)
        for severity in SEVERITY_ORDER
    }
    verdict = (
        "NO-GO"
        if counts["blocker"]
        else "CONDITIONAL"
        if counts["warning"]
        else "GO"
    )
    payload = {
        "repository": str(root),
        "revision": revision,
        "verdict": verdict,
        "counts": counts,
        "findings": [asdict(finding) for finding in findings],
        "limits": [
            "Heuristic preflight; not legal, security, privacy, or license certification.",
            "Ignored contents, all historical blobs, remote forks/caches, issue "
            "trackers, downloads, container layers, and external services are "
            "not fully scanned.",
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path inside the Git repository.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Report format.",
    )
    parser.add_argument("--output", help="Write the report to this path.")
    parser.add_argument(
        "--fail-on",
        choices=("never", "blockers", "warnings"),
        default="never",
        help="Choose which finding level makes the command exit non-zero.",
    )
    parser.add_argument(
        "--skip-history",
        action="store_true",
        help="Skip reachable-history pathname enumeration.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    candidate = Path(args.repo).expanduser().resolve()
    try:
        root = Path(git_text(candidate, "rev-parse", "--show-toplevel").strip()).resolve()
    except (RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    tracked_files = set(nul_paths(git_bytes(root, "ls-files", "-z")))
    untracked_files = set(
        nul_paths(git_bytes(root, "ls-files", "--others", "--exclude-standard", "-z"))
    )
    current_files = tracked_files | untracked_files
    findings: list[Finding] = []

    inspect_git_state(root, untracked_files, findings)
    inspect_root_documents(root, current_files, findings)
    inspect_license_classification(root, current_files, findings)
    inspect_paths_and_content(root, current_files, tracked_files, findings)
    if not args.skip_history:
        inspect_history_paths(root, current_files, findings)
    inspect_third_party_surface(current_files, findings)
    inspect_cargo(root, current_files, findings)
    inspect_package_json(root, current_files, findings)
    inspect_pyproject(root, current_files, findings)
    inspect_private_dependencies(root, current_files, findings)
    inspect_github(root, current_files, findings)
    inspect_submodules(root, current_files, findings)

    findings.sort(
        key=lambda finding: (
            SEVERITY_ORDER[finding.severity],
            finding.code,
            finding.message,
        )
    )
    revision = git_text(root, "rev-parse", "HEAD").strip()
    report = (
        render_json(root, revision, findings)
        if args.format == "json"
        else render_markdown(root, revision, findings)
    )
    if args.output:
        output = Path(args.output).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report + "\n", encoding="utf-8")
    else:
        print(report)

    blockers = any(finding.severity == "blocker" for finding in findings)
    warnings = any(finding.severity == "warning" for finding in findings)
    if args.fail_on == "warnings" and (blockers or warnings):
        return 1
    if args.fail_on == "blockers" and blockers:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
