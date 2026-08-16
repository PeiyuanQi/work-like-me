---
name: audit-repository-security-privacy
description: Audit a repository and its dependency boundaries for source-backed security and privacy risks. Use when the user asks whether an app, service, library, or repository is safe; requests a security or privacy review; asks about MITM, telemetry, permissions, secrets, updates, backups, remote config, or data collection; or wants a direct risk assessment grounded in code rather than project claims.
---

# Audit Repository Security Privacy

Version: 1.0.0

Trace real behavior through source, manifests, dependencies, and trust
boundaries. Separate proven findings from plausible risks and missing evidence.

## Workflow

1. Establish the audit target.
   - Record the repository, revision, platform, build flavor, and user question.
   - Identify public, private, generated, vendored, Git, path, native, and remote
     components that may sit outside the visible checkout.
   - Treat README, privacy-policy, and security-policy claims as assertions to
     compare with implementation, not as proof.

2. Map the attack and privacy surface.
   - Inspect dependency manifests and lockfiles before reading isolated files.
   - Inspect permissions, entitlements, exported components, IPC, webviews,
     plugin bridges, and native services.
   - Trace network clients, TLS validation, proxy handling, remote config,
     update/download flows, authentication, and endpoint construction.
   - Trace identifiers, telemetry, logs, local storage, credentials, backups,
     archives, synchronization, clipboard, camera, microphone, and file access.
   - When public release or secret exposure is in scope, inspect reachable Git
     history, tags, submodules, and LFS objects; a clean current tree does not
     prove the repository history is safe.
   - Inspect code execution, deserialization, archive extraction, shelling out,
     and downloaded-content verification where present.

3. Prove behavior end to end.
   - Find shared helpers first, then enumerate their consumers.
   - Pin Git or registry dependencies to the exact locked revision before
     attributing behavior to the built product.
   - Narrow noisy searches to production source, manifests, and the paths tied
     to the user's question.
   - Follow data from collection to storage, transmission, recipient, and
     deletion instead of stopping at a matching keyword.

4. Classify every important claim.
   - **Confirmed finding:** directly demonstrated by the inspected revision.
   - **Conditional risk:** requires a stated precondition or deployment choice.
   - **Blind spot:** relevant code, service, build input, or runtime evidence is
     unavailable.
   - **Informational:** increases exposure but is not a vulnerability by itself.
   - Assign severity from impact, exploitability, reachability, and existing
     mitigations; do not assign it from a suspicious pattern alone.

5. Answer the user's actual risk question.
   - For direct questions such as "Is there MITM risk?", lead with `yes`, `no`,
     or `not proven`.
   - Name the concrete trust-breaker, affected flows, attacker prerequisites,
     likely impact, and the boundary of what was not verified.
   - Distinguish control-plane exposure from data-plane exposure when the
     evidence supports only one of them.

6. Report actionable findings.
   - Order findings by severity and include tight file/line or dependency
     references.
   - State observed behavior, realistic impact, evidence, and remediation.
   - Compare privacy disclosures with actual identifiers, metadata, storage,
     and transmissions.
   - End with coverage limits and the highest-value next evidence to obtain.

## Guardrails

- Keep the audit read-only unless the user also asks for fixes.
- Do not claim a whole product is safe because the visible repository looks
  clean.
- Do not claim a whole traffic path is compromised when only one application
  helper or control-plane path is proven vulnerable.
- Use current primary advisories and upstream documentation for facts that may
  have changed; do not rely on remembered vulnerability status.
- Avoid dumping low-signal search matches. Prefer a small set of defensible,
  reachable findings.
