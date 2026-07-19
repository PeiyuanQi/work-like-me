---
name: remediate-dependency-vulnerabilities
description: Diagnose and fix dependency vulnerabilities across package ecosystems while preserving application behavior. Use when the user asks to address GitHub or package-manager security alerts, remove vulnerable dependencies, make npm audit or pip-audit clean, update a lockfile safely, replace an unmaintained package, or verify whether reported alerts still apply to the current repository.
---

# Remediate Dependency Vulnerabilities

Version: 1.0.0

Turn vulnerability reports into the smallest verified dependency change that
removes real exposure without trading it for an uncontrolled upgrade.

## Workflow

1. Read repository guidance and establish the supported runtime.
   - Use the repo's package manager, lockfile, runtime version, and validation
     commands.
   - Inspect the working tree and preserve unrelated user-owned changes.

2. Build a current baseline.
   - Query the package manager and, when relevant, the repository host's alert
     surface.
   - Record advisory IDs, affected installed versions, severity, dependency
     paths, fix availability, and whether the vulnerable code is reachable.
   - Distinguish current remote alerts from disabled alerting, stale tracking
     refs, old pull requests, or findings that no longer match the lockfile.

3. Trace ownership of each vulnerable package.
   - Separate direct dependencies, development-only dependencies, optional
     packages, and transitive dependencies.
   - Identify which direct package introduces each transitive vulnerable
     version.
   - Check current upstream releases and changelogs from primary sources before
     choosing a target version.

4. Choose the least risky fix.
   - Prefer upgrading or removing the direct dependency that owns the chain.
   - Prefer a maintained replacement when the dependency is abandoned or the
     vulnerable behavior is unnecessary.
   - Use a narrow override, resolution, or constraint only when a compatible
     patched transitive version exists and a direct upgrade cannot resolve it.
   - Avoid broad force-upgrades, unreviewed automated fixes, and patches inside
     installed dependency directories.

5. Implement in reviewable batches.
   - Update manifests and regenerate lockfiles with the repository's package
     manager.
   - Inspect lockfile changes for unexpected package families, registries, Git
     revisions, missing integrity data, lifecycle scripts, or major-version
     jumps.
   - Keep source compatibility changes scoped to what the dependency upgrade
     actually requires.

6. Verify the committed dependency graph.
   - Run a clean or frozen install such as `npm ci`, `uv sync --locked`, or the
     ecosystem equivalent.
   - Use the package manager's graph check to detect invalid, missing,
     extraneous, or constraint-violating dependencies when available.
   - Re-run the vulnerability scanner at the repository's accepted threshold.
   - Run focused tests, then the relevant build or broader suite in proportion
     to the dependency's reach.
   - Inspect runtime behavior when the change affects rendering, networking,
     authentication, serialization, build tooling, or deployment.

7. Close the loop.
   - Report resolved advisories, remaining advisories, why any remain, and the
     exact verification performed.
   - If the user asks to commit or push, use `swe:finish-work` after the final
     audit and clean-install checks.
   - Refresh remote metadata before claiming a hosting alert or branch still
     exists.

## Guardrails

- Do not equate `audit fix` success with application correctness.
- Do not suppress or ignore an advisory merely to make the scanner green.
- Do not use a transitive override without verifying API and runtime
  compatibility for the parent package.
- Do not widen version ranges more than necessary without reviewing the lock
  result.
- Keep build warnings that are unrelated to the vulnerability separate from
  remediation failures.
