---
name: publish-and-verify-website
description: "Publishes a website through its real hosting path and proves the production result. Use when the user asks to deploy, publish, release, commit-push-deploy, or update a live site, diagnose deployment warnings, confirm where a site is actually hosted, or verify that pages, generated assets, data, and recent content are live rather than merely built locally."
---

# Publish And Verify Website

Version: 1.1.0

Complete the release path from validated source to observable production. A
successful command or an HTTP `200` alone is not sufficient proof.

## Workflow

1. Discover the real publish chain.
   - Read repo guidance, package scripts, CI workflows, hosting metadata,
     custom-domain configuration, and generated-output rules.
   - Identify the source repository, host repository or deployment service,
     target branch, base path, site URL, and required runtime.
   - Distinguish alternate paths such as preview, project Pages, custom-domain
     Pages, and external hosting.

2. Establish release scope.
   - Review the intended diff and generated files.
   - If the user asks to "commit push and deploy", treat validation, source
     commit, push, deployment, and production verification as one workflow.
   - Use `swe:finish-work` for the source commit and push when requested.
   - When the request is only to build or preview, stop short of publishing
     publicly.

3. Build with the production contract.
   - Use the repository's canonical command and supported runtime.
   - Preserve production URL, base-path, environment, asset, and routing
     settings.
   - Verify generated output before deployment, including required files such
     as `.nojekyll`, redirects, manifests, or server bundles where applicable.

4. Run the canonical deployment.
   - Prefer the repo's deploy script or hosting workflow over an invented
     sequence.
   - Map each log stage to the repository or service that emitted it before
     diagnosing warnings.
   - Treat source-repo, host-repo, CI, and CDN failures as separate boundaries.

5. Wait for the hosting system.
   - Check the provider's build or deployment status when available.
   - If deployment succeeded but production is stale, allow for propagation
     and use cache-busted requests before declaring failure.
   - Probe transitional HTTP failures with a client or error handler that
     preserves the non-2xx status and response body, so an expected rollout
     `404` or `503` doesn't abort polling or trigger null follow-on checks.
   - Keep working until the deployment succeeds, fails with evidence, or needs
     authority outside the requested scope.

6. Prove production.
   - Fetch the intended page and confirm the expected route and changed
     content, not only the status code.
   - Fetch at least one generated CSS, JavaScript, image, font, or other hashed
     asset with a normal GET and confirm its status and content type.
   - For data or media releases, verify the changed JSON/data route and binary
     asset directly.
   - For interaction or layout changes, check the live site in a browser at
     relevant desktop and mobile sizes, including console and network errors.
   - When CDN lag is possible, compare the served asset fingerprint or content
     marker with the new build.

7. Confirm repository alignment.
   - Verify the source branch and any host branch or host repository are
     pushed.
   - Confirm the worktree is clean, or explain intentional generated changes.
   - Report the source commit, deployment result, live URL, asset/data checks,
     and any warnings that remain.

## Failure Interpretation

- HTML `200` plus CSS/JS `404`: suspect base path, packaging, `.nojekyll`, or
  stale generated output before blaming component styling.
- Successful deploy command plus an old fingerprint: check provider status and
  CDN propagation before redeploying.
- Warning during a nested host build: fix the repository that owns the warning,
  which may not be the source repository that launched the deployment.
- Live page loads but the changed content is absent: the release stays
  unverified until the served revision is identified.

## Guardrails

- Keep deployment credentials, write tokens, and secret environment values out
  of logs and completion reports.
- Claim production success only from live evidence, never from a local build,
  push, or deployment banner.
- While the provider reports a valid build still in progress, wait rather than
  redeploying.
