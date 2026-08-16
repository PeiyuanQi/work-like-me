# Open-Source Readiness Gates

Use this reference for a complete audit, remediation plan, or open-source
implementation. Adapt the evidence to the repository and artifact types; do not
create every listed file mechanically.

## Finding levels

| Level | Meaning | Release effect |
|---|---|---|
| Blocker | Credible disclosure, rights, security, build, or distribution failure | NO-GO until resolved or the affected artifact is removed from scope |
| Warning | Material ambiguity, maintenance risk, or incomplete evidence | CONDITIONAL; name the owner and acceptance decision |
| Improvement | Useful public-project polish without immediate release risk | May follow after launch |
| Pass | Verified with a concrete command, artifact, or source reference | Record the evidence and revision |

## Gate matrix

| Gate | Required evidence | Typical blockers |
|---|---|---|
| Release contract | Target revision, artifact list, platforms, visibility, license class, authorized external actions | Scope or license class is undecided |
| Public/private boundary | Dependency graph, public API, fixtures, build inputs, submodule/path-dependency map | Public code imports a private repo, paid asset, internal service, or absolute path |
| Current-tree disclosure | Tracked/untracked/ignored/generated/large-file inventory | Secrets, personal data, confidential docs, customer content, private saves/logs |
| Reachable history | Branch/tag/LFS/submodule scan and secret-history result | Revoked-but-still-reachable secret, restricted file, or unknown large object |
| First-party ownership | Copyright/contract/employment provenance for code and docs | Ownership is disputed or contributor authority is insufficient for intended licensing |
| License classification | License text, README wording, manifest metadata, counsel placeholders | Restricted/custom terms are called open source; license is missing or contradictory |
| Third-party code | Locked dependency inventory, licenses, advisories, upstream notices | Incompatible license, missing notice, unlicensed copied code, unknown vendored source |
| Assets/data/models | Per-item source, creator, license, modification and redistribution rights | Paid/restricted font, image, audio, dataset, model, map, or generated asset lacks rights |
| Package metadata | Correct name, version, license/license-file, repository, README, runtime/toolchain | Package claims a different license or points at private/nonexistent resources |
| Community surface | README, contribution path, security reporting, support and conduct expectations | Users cannot install, report vulnerabilities, or understand contribution terms |
| Supply chain | Lockfiles, CI permissions, pinned/reviewed actions, dependency update policy, SBOM when useful | Release depends on mutable/untrusted remote code or an unreviewed build download |
| Build and tests | Clean-clone setup plus format/lint/test/build/docs/examples | Build requires developer-local state, private cache, undeclared tool, or unsupported platform |
| Distribution contents | Source-package and binary/archive inventories | Private files included; required license, notice, runtime asset, or attribution omitted |
| Version/release operations | SemVer/compatibility decision, changelog, signing/checksums, rollback | Unapproved version bump, incompatible release mislabeled, unreproducible artifact |
| Governance/operations | Maintainer/reviewer ownership, support boundary, disclosure process | No responsible owner for security, release, legal, or community decisions |

## License classification

Classify the outbound terms before editing marketing copy:

- **Open source:** use an OSI-approved license without extra field-of-use,
  revenue, royalty, product-display, or non-commercial restrictions.
- **Source-available/public-source:** source is visible and usable under custom or
  restrictive terms, but the project must not claim OSI open-source status. For
  this skill, that discovery is a `NO-GO` for the open-source plan until the
  owner either selects an OSI-approved license or explicitly starts a separate
  source-available release workflow.
- **Dual/multi-license:** state which artifact or use receives which license and
  confirm that the rights holder can offer every path.
- **Proprietary public repository:** code may be viewable while copying,
  modification, or redistribution remains restricted. Say so plainly.

Check all of these together:

- root license/copying files and notices;
- README badges, headings, package pages, websites, and release notes;
- manifest `license` or `license-file` fields and source headers;
- contribution terms, trademark/branding rules, and commercial agreements;
- placeholders for owner, year, contact, governing law, or jurisdiction.

Do not invent missing legal facts. A custom license with unresolved owner or
jurisdiction fields is not ready for formal publication.

## Public/private extraction

When extracting a reusable engine, library, SDK, or tool from a private product:

1. Draw the dependency direction. The proprietary product may depend on the
   public component; the public component must not require proprietary code.
2. Move product-specific entities, rules, data, art, configuration, telemetry,
   and business logic behind public interfaces or plugins.
3. Replace private fixtures with small redistributable examples that still
   exercise the real public API.
4. Remove sibling-repo assumptions, absolute paths, unpublished packages,
   private registries, and hidden build steps.
5. Test the public component from a clean clone with no private repositories
   present.
6. Document compatibility, extension points, serialization/version boundaries,
   and what intentionally remains proprietary.

Treat architecture documentation and examples as disclosure surfaces. A clean
code boundary can still leak private product plans, internal names, endpoints,
or licensed content through docs and fixtures.

## Secrets and Git history

Follow this order when a secret or restricted artifact is found:

1. Stop further publication and revoke/rotate the credential or access path.
2. Identify every reachable branch, tag, pull-request ref, LFS object, mirror,
   archive, cache, and fork containing it.
3. Obtain explicit approval for any history rewrite and force-push.
4. Preserve a recoverable private backup, rewrite the minimum required history,
   and coordinate collaborator reclones.
5. Invalidate cached artifacts and notify affected parties when required.
6. Rescan the rewritten repository and verify the replacement credential.

Never promise complete erasure after material has been cloned or downloaded.
History cleaning reduces future exposure; revocation addresses the active risk.

## Contributor authority

Match the inbound contribution model to the outbound business model:

- **Inbound equals outbound:** simple for normal open-source projects, but may
  not permit a single owner to offer incompatible proprietary licenses.
- **DCO:** records contributor provenance and authority to submit; it is not a
  general copyright assignment or automatic broad relicensing grant.
- **CLA/CLG:** may grant additional copyright and patent rights while the
  contributor retains ownership. Keep it no broader or heavier than necessary.
- **Copyright assignment:** transfers ownership and usually requires a written
  signed instrument to an identifiable legal person/entity; consider a
  contributor license-back and counsel review.

Inspect existing commits before changing policy. New terms normally solve
future contributions, not missing authority for past contributions.

## Third-party code, assets, and notices

Build an inventory with at least:

- component or asset name and exact version/revision;
- source URL or creator;
- license and copyright holder;
- where it appears in source and distributed artifacts;
- modifications and required attribution/NOTICE text;
- whether it is linked, bundled, embedded, generated, or downloaded at runtime.

Distinguish source packages from compiled distributions:

- A source package may reference dependencies without including their code.
- A binary, container, installer, application bundle, or generated site may
  embed dependency code, fonts, icons, media, models, or data and therefore need
  a fuller notice bundle.
- Lockfiles and SBOMs identify components but do not replace required license
  text, copyright notices, or upstream NOTICE files.
- Package-level SPDX metadata may omit embedded asset licenses and named
  copyright notices.
- Optional features and target-specific dependencies can change the obligations
  per Windows, macOS, Linux, mobile, web, or container artifact.

Review generated notices as a diff. Upstream metadata and harvested text can
change even when the dependency version does not.

## Open-source project surface

Create only what maintainers will actually support:

- `README` with purpose, status, install, minimal example, platforms, support,
  contribution path, license class, and limitations;
- `LICENSE`/`COPYING`, `NOTICE` or third-party notices, and branding/trademark
  guidance when applicable;
- `CONTRIBUTING`, security policy, code of conduct, support policy, changelog or
  versioning policy, and release instructions;
- issue forms/templates, pull-request template, ownership/reviewer routing, and
  dependency update configuration;
- CI for repository-defined format, lint, test, build, docs, packages, and the
  promised platform matrix;
- clear deprecation, compatibility, vulnerability disclosure, and maintenance
  expectations.

Keep sponsor acknowledgement factual. Sponsorship alone must not imply
copyright, ownership, governance, endorsement, exclusivity, or special license
rights unless a separate written agreement says otherwise.

## Supply-chain and CI checks

- Minimize workflow-token permissions and secrets exposure.
- Pin or deliberately review third-party CI actions and build tools.
- Avoid executing untrusted pull-request code with write tokens or production
  secrets.
- Preserve lockfiles when the ecosystem and artifact type expect them.
- Verify checksums/signatures for downloaded tools and release inputs.
- Generate an SBOM for complex binary/container releases when useful.
- Run dependency advisory and license checks against the exact locked graph.
- Document how maintainers rotate release keys and recover from a bad release.

## Final consumer-boundary verification

Before GO:

1. Create a clean clone from the exact proposed public revision.
2. Follow only the public README and contribution instructions.
3. Build/test/package on every promised platform or prove the CI result.
4. Run examples and validate that no private service or repository is required.
5. List every source package and compiled archive entry.
6. Confirm license classification, owner fields, notices, branding, and
   attribution inside each artifact.
7. Re-run secret/current-tree/history, dependency, link, and package scans.
8. Record hashes, version, toolchain, inputs, and rollback path for release
   artifacts when reproducibility matters.

## Recommended report shape

1. Verdict: GO, CONDITIONAL, or NO-GO.
2. Scope: revision, repository refs, platforms, and artifacts.
3. Blockers with evidence and required owner/decision.
4. Warnings and accepted residual risks.
5. License class, first-party ownership, and contributor authority.
6. Secret/history and privacy coverage.
7. Third-party code/assets/data plus notice/SBOM coverage.
8. Clean-clone, CI, package, and cross-platform results.
9. Files changed and exact commands run.
10. External actions still awaiting authorization.
