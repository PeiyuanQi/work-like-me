---
name: prepare-repository-for-open-source
description: Audit and prepare a software repository for a safe open-source release under an OSI-approved license. Use when a user asks to open-source a repo, turn a private product or internal component into an open-source project, extract a reusable engine or library from proprietary code, create an OSS-readiness plan, or verify licensing, provenance, secrets and Git history, dependency notices, contributor terms, documentation, CI, packaging, branding, and governance before launch. Also use to catch requests that say open source but actually require a restrictive source-available license; report that mismatch as a blocker instead of mislabeling it.
---

# Prepare Repository for Open Source

Work from the repository root. Read every applicable `AGENTS.md` or equivalent
instruction file before inspecting or changing the repository. Treat open
sourcing as a disclosure, rights, security, and operations change rather than a
README-only task.

For a full audit or implementation, read
[`references/open-source-readiness-gates.md`](references/open-source-readiness-gates.md).

## Establish the release contract

1. Record the target revision, intended public scope, supported platforms, and
   distributed artifacts: source, packages, binaries, containers, data, models,
   documentation, examples, or generated assets.
2. Confirm that the intended outbound terms use an OSI-approved open-source
   license. If the requested terms include field-of-use limits, revenue
   thresholds, royalties, mandatory product display, non-commercial clauses, or
   similar restrictions, mark the open-source plan `NO-GO` and identify the
   result as source-available instead. Do not silently broaden the task into a
   different publication model.
3. Decide whether proprietary code or assets remain in a separate product and
   whether the open-source component will also support a dual-license model.
4. Identify the public/private boundary before moving files. Keep proprietary
   product logic, private datasets, paid assets, credentials, business plans,
   user data, and restricted documentation outside the public dependency graph.
5. Confirm which external actions are authorized. Do not create a public repo,
   rewrite history, force-push, tag, publish, upload, or announce by implication.

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

Run the bundled preflight early. Resolve the script path relative to this
`SKILL.md`, not relative to the repository being audited:

    python "<skill-folder>/scripts/audit_open_source_readiness.py" --repo . --format markdown

Use `--fail-on blockers` for a release gate. Treat the script as triage, not as
proof that the repository is safe or legally releasable.

## Clear the hard gates

### Secrets, privacy, and history

- Search current files and reachable history for credentials, tokens, keys,
  customer or employee data, private URLs, personal contact details, internal
  infrastructure, and confidential artifacts.
- Revoke or rotate exposed credentials before cleaning history. Deleting a file
  from the current branch does not remove it from Git history, forks, caches, or
  prior downloads.
- Require explicit approval and coordination before history rewriting or a
  force-push. Preserve a recovery path and tell collaborators how to reclone.
- Use `audit-repository-security-privacy` when the trust, telemetry, update,
  network, permissions, or data-flow surface needs deeper source tracing.

### Ownership, licensing, and provenance

- Establish rights for first-party code, copied snippets, contributions,
  dependencies, fonts, icons, images, audio, datasets, models, documentation,
  generated content, and trademarks.
- Block release when provenance is unknown or the intended license conflicts
  with an upstream license, employment agreement, contract, or asset terms.
- Keep package metadata, README claims, `LICENSE`/`COPYING`, notices, headers,
  and distribution terms consistent. Do not invent a legal entity, owner,
  address, jurisdiction, contact, or copyright assignment.
- For custom commercial licensing, verify that contribution terms actually
  preserve any needed relicensing authority. A DCO proves provenance but does
  not automatically grant broad relicensing rights.
- Treat legal drafting and enforceability as counsel-review work. Record
  placeholders and unresolved decisions as blockers rather than guessing.

### Third-party materials and supply chain

- Resolve exact locked dependency versions and inspect target-specific and
  optional dependencies used by every release artifact.
- Generate an SBOM or dependency inventory when practical. Preserve full
  license text, copyright, attribution, and upstream NOTICE obligations.
- Audit embedded assets separately from package metadata. Compiled binaries,
  containers, installers, fonts, models, and vendored code often need notices
  that a source package does not bundle.
- Review generated notice diffs; do not assume a lockfile or SPDX expression is
  a complete notice bundle. Remember that SPDX `OR` and `AND` have different
  compliance meanings.
- Use `remediate-dependency-vulnerabilities` when current advisories need fixes.

## Build the open-source repository surface

Add only files that serve an actual public workflow. Typical needs include:

- clear README, license, contribution guide, security policy, support path,
  code of conduct, changelog/versioning policy, and release instructions;
- issue and pull-request templates, ownership/reviewer routing, dependency
  maintenance, and least-privilege CI;
- accurate package metadata, repository URLs, minimum toolchain/runtime,
  platform support, feature flags, examples, and clean-clone setup;
- architecture and extension boundaries that let the public component build and
  test without a private sibling repository or absolute local path;
- third-party notices, branding/trademark rules, sponsor acknowledgements, and
  localization when the actual distribution model requires them.

Keep sponsor recognition separate from ownership, governance, endorsement, and
license rights. Do not make downstream users acknowledge sponsors unless that
is an intentional, legally reviewed license obligation.

When a repository has unusual release obligations—dual licensing, required
trademark treatment, generated notices, platform-specific packaging, special
fixtures, or strict artifact contents—create a concise project-local release
skill that records those exact checks and known pitfalls. If the owner chooses
a restrictive source-available model instead, stop calling the work an
open-source release and capture that separate release contract explicitly.

## Verify from the consumer boundary

1. Test from a clean clone at the intended public revision.
2. Run repository-defined format, lint, test, build, documentation, package, and
   example commands for every supported platform or CI matrix.
3. Inspect package and archive contents before distribution. Verify that source
   packages exclude private/generated clutter and compiled artifacts include
   every required license, notice, branding, and runtime asset.
4. Check links, install instructions, version/SemVer policy, compatibility of
   serialized formats or public APIs, and release rollback/reproducibility.
5. Rerun secret/history scans, dependency/license checks, and the bundled
   preflight after edits.
6. Do not bump a version merely because the repository was cleaned up. Bump,
   tag, publish, or push only when the user authorizes that release state.

## Report a go/no-go result

Lead with `GO`, `NO-GO`, or `CONDITIONAL`, then provide:

- the exact revision and artifacts assessed;
- blockers, warnings, and accepted residual risks;
- files changed and checks run;
- license classification and unresolved legal-owner/contributor decisions;
- secret-history and third-party-material coverage;
- clean-clone, platform, package, and notice results; and
- external actions still requiring authorization.

Do not call the repository ready while a hard gate remains unresolved.

## Guardrails

- Keep audits read-only unless the user also asks for implementation.
- Preserve unrelated user changes and avoid broad cleanup outside the release
  boundary.
- Never publish confidential material to make a build self-contained; replace
  it with a public interface, fixture, or documented optional integration.
- Never treat repository visibility as proof that every file is redistributable.
- Never describe a custom restricted license as OSI-approved open source.
