---
name: prepare-repository-for-open-source
description: "Audits and prepares a software repository for a safe open-source release under an OSI-approved license. Use when a user asks to open-source a repo, turn a private product or internal component into an open-source project, extract a reusable engine or library from proprietary code, create an OSS-readiness plan, or verify licensing, provenance, secrets and Git history, dependency notices, contributor terms, documentation, CI, packaging, branding, and governance before launch. Also catches requests that say open source but require a restrictive source-available license, reporting the mismatch as a blocker instead of mislabeling it."
---

# Prepare Repository for Open Source

Work from the repository root. Read every applicable `AGENTS.md` or equivalent
instruction file before inspecting or changing the repository. Treat open
sourcing as a disclosure, rights, security, and operations change rather than a
README-only task.

For a full audit or implementation, read
[references/open-source-readiness-gates.md](references/open-source-readiness-gates.md).

## Establish the release contract

1. Record the target revision, intended public scope, supported platforms, and
   distributed artifacts: source, packages, binaries, containers, data, models,
   documentation, examples, or generated assets.
2. Confirm that the intended outbound terms use an OSI-approved open-source
   license. If the requested terms include field-of-use limits, revenue
   thresholds, royalties, mandatory product display, non-commercial clauses, or
   similar restrictions, mark the open-source plan `NO-GO` and identify the
   result as source-available. Report that instead of silently broadening the
   task into a different publication model.
3. Decide whether proprietary code or assets remain in a separate product and
   whether the open-source component will also support a dual-license model.
4. Identify the public/private boundary before moving files. Keep proprietary
   product logic, private datasets, paid assets, credentials, business plans,
   user data, and restricted documentation outside the public dependency graph.
5. Confirm which external actions are authorized. Creating a public repo,
   rewriting history, force-pushing, tagging, publishing, uploading, or
   announcing each needs explicit authorization, never implication.

## Inventory the complete disclosure surface

Inspect more than the current tracked tree:

- tracked, untracked, ignored, generated, vendored, and large files;
- all branches and tags that will become reachable;
- Git LFS objects, submodules, nested repositories, release archives, and CI
  artifacts;
- examples, fixtures, screenshots, saves, logs, crash dumps, agent artifacts,
  design documents, and local-machine paths;
- package metadata, lockfiles, build scripts, installers, containers, and
  deployment configuration.

Run the bundled preflight early. It needs Python 3.10+ and only the standard
library. Resolve the script path relative to this `SKILL.md`, not relative to
the repository being audited (use `py -3` on Windows):

```bash
python3 "<skill-folder>/scripts/audit_open_source_readiness.py" --repo . --format markdown
```

Add `--fail-on blockers` for a release gate; `--help` lists the other options,
such as `--format json` and `--skip-history`. The script is triage, not proof
that the repository is safe or legally releasable.

## Clear the hard gates

### Secrets, privacy, and history

- Search current files and reachable history for credentials, tokens, keys,
  customer or employee data, private URLs, personal contact details, internal
  infrastructure, and confidential artifacts.
- Revoke or rotate exposed credentials before cleaning history. Deleting a file
  from the current branch does not remove it from Git history, forks, caches,
  or prior downloads.
- Get explicit approval and coordination before any history rewrite or
  force-push. Preserve a recovery path and tell collaborators how to reclone.
- Use `swe:audit-repository-security-privacy` when the trust, telemetry,
  update, network, permissions, or data-flow surface needs deeper source
  tracing.

### Ownership, licensing, and provenance

- Establish rights for first-party code, copied snippets, contributions,
  dependencies, fonts, icons, images, audio, datasets, models, documentation,
  generated content, and trademarks.
- Block release when provenance is unknown or the intended license conflicts
  with an upstream license, employment agreement, contract, or asset terms.
- Keep package metadata, README claims, `LICENSE`/`COPYING`, notices, headers,
  and distribution terms consistent. Record missing legal facts (entity, owner,
  address, jurisdiction, contact, copyright assignment) as open decisions
  rather than inventing them.
- For custom commercial licensing, verify that contribution terms actually
  preserve any needed relicensing authority. A DCO proves provenance but does
  not automatically grant broad relicensing rights.
- Treat legal drafting and enforceability as counsel-review work. Record
  placeholders and unresolved decisions as blockers rather than guessing.

### Third-party materials and supply chain

- Resolve exact locked dependency versions and inspect the target-specific and
  optional dependencies used by every release artifact.
- Generate an SBOM or dependency inventory when practical. Preserve full
  license text, copyright, attribution, and upstream NOTICE obligations.
- Audit embedded assets separately from package metadata. Compiled binaries,
  containers, installers, fonts, models, and vendored code often need notices
  that a source package does not bundle.
- Review generated notice diffs. A lockfile or SPDX expression is not a
  complete notice bundle, and SPDX `OR` and `AND` have different compliance
  meanings.
- Use `swe:remediate-dependency-vulnerabilities` when current advisories need
  fixes.

## Build the open-source repository surface

Add only files that serve an actual public workflow. Typical needs include:

- clear README, license, contribution guide, security policy, support path,
  code of conduct, changelog/versioning policy, and release instructions;
- issue and pull-request templates, ownership/reviewer routing, dependency
  maintenance, and least-privilege CI;
- accurate package metadata, repository URLs, minimum toolchain/runtime,
  platform support, feature flags, examples, and clean-clone setup;
- architecture and extension boundaries that let the public component build
  and test without a private sibling repository or absolute local path
- third-party notices, branding/trademark rules, sponsor acknowledgements, and
  localization when the actual distribution model requires them.

Keep sponsor recognition separate from ownership, governance, endorsement, and
license rights. Require downstream users to acknowledge sponsors only when that
is an intentional, legally reviewed license obligation.

When a repository has unusual release obligations (dual licensing, required
trademark treatment, generated notices, platform-specific packaging, special
fixtures, or strict artifact contents), create a concise project-local release
skill that records those exact checks and known pitfalls. If the owner chooses
a restrictive source-available model instead, stop calling the work an
open-source release and capture that separate release contract explicitly.

## Verify from the consumer boundary

1. Test from a clean clone at the intended public revision.
2. Run repository-defined format, lint, test, build, documentation, package,
   and example commands for every supported platform or CI matrix.
3. Inspect package and archive contents before distribution. Verify that source
   packages exclude private and generated clutter, and that compiled artifacts
   include every required license, notice, branding, and runtime asset.
4. Check links, install instructions, version/SemVer policy, compatibility of
   serialized formats or public APIs, and release rollback/reproducibility.
5. Rerun secret/history scans, dependency/license checks, and the bundled
   preflight after edits.
6. Leave the version alone when the repository was merely cleaned up. Bump,
   tag, publish, or push only when the user authorizes that release state.

## Report a go/no-go result

Lead with `GO`, `NO-GO`, or `CONDITIONAL`, then provide:

- the exact revision and artifacts assessed;
- blockers, warnings, and accepted residual risks;
- files changed and checks run;
- license classification and unresolved legal-owner/contributor decisions;
- secret-history and third-party-material coverage;
- clean-clone, platform, package, and notice results
- external actions still requiring authorization.

While any hard gate remains unresolved, the repository is not ready; say so.

## Guardrails

- Keep audits read-only unless the user also asks for implementation.
- Preserve unrelated user changes and keep cleanup inside the release
  boundary.
- Replace confidential material with a public interface, fixture, or
  documented optional integration rather than publishing it to make a build
  self-contained.
- Repository visibility is not proof that every file is redistributable.
- Describe only OSI-approved licenses as open source; a custom restricted
  license is source-available.
