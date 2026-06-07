# Code Review Guidance

Use this reference when reviewing a merge request or pull request. Calibrate the
review to the product stage and expected audience before judging risk.

## Review Stance

- Prioritize correctness, security, data integrity, concurrency, reliability,
  user-visible regressions, and missing tests.
- Lead with actionable findings ordered by severity. Include file and line
  references when possible.
- Distinguish blocking issues from follow-up improvements. Avoid over-reviewing
  a demo, prototype, or MVP as if it were a large-scale production system.
- Match the review depth to the likely audience and operating context: internal
  tool, simple demo, MVP, production service, or large-scale user system.
- Preserve original intent. When suggesting changes, keep the feature's intended
  behavior unless the implementation proves that intent unsafe or inconsistent
  with repo requirements.

## Language And Style Defaults

- Python: follow the repo's Ruff configuration first. Where the repo is silent,
  use Ruff formatting/linting conventions and the Google Python Style Guide.
- TypeScript: follow the repo's ESLint/formatter configuration first. Where the
  repo is silent, use the Google TypeScript Style Guide.
- JavaScript: follow the repo's ESLint/formatter configuration first. Where the
  repo is silent, prefer modern, typed, maintainable patterns consistent with
  adjacent code.
- For all languages, prefer established repo patterns over generic style advice.

## Backend Review Focus

- Concurrency: check races, lost updates, duplicate processing, idempotency,
  transaction boundaries, lock scope, retry behavior, and cancellation.
- Database design: check schema normalization where appropriate, constraints,
  indexes, migrations, rollback safety, data lifecycle, and query scalability.
- API and service boundaries: check resource modeling, validation, error shapes,
  authz/authn assumptions, pagination, rate limits, observability, and backward
  compatibility.
- Scalability: judge expected load honestly. For a small demo, flag obvious
  dead ends without demanding premature distributed-system machinery. For a
  large-scale user system, review hot paths, fan-out, N+1 queries, cache
  invalidation, queue semantics, and operational failure modes.

## Frontend And Product Review Focus

- Check loading, empty, error, retry, and success states.
- Check accessibility, keyboard flow, focus states, contrast, text expansion,
  responsive layouts, and light/dark theme behavior when relevant.
- Match UX polish to the product context: an internal admin screen can be quiet
  and dense; a customer-facing flow needs stronger affordances and copy.

## Test Expectations

- Look for tests around changed behavior, edge cases, regressions, migrations,
  and failure paths.
- For small changes, focused tests may be enough. For shared logic, cross-module
  contracts, concurrency, or persistence changes, expect broader coverage.
- If tests are missing, explain the concrete risk the missing test would catch.
