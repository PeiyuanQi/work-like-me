---
name: rust-coding-style
description: Write, refactor, or review Rust code for consistent formatting, idiomatic APIs, ownership clarity, package/workspace layout, documentation, and focused linting. Use for Rust implementation and coding-style requests, including crate organization and Bevy-inspired conventions, while preserving the target repository's rules.
---

# Rust Coding Style

Use automated formatting, deliberate public interfaces, and justified lint exceptions. Bevy is a reference implementation, not a universal Rust standard. This skill combines observed Bevy conventions, layout examples from VitalyAnkh’s repositories, and explicitly identified general recommendations. Forks and upstream-derived repositories are attributed separately.

## Establish the local contract

Before editing, inspect repository instructions, nearby Rust code, workspace and crate `Cargo.toml` files, `rust-toolchain*`, `rustfmt.toml` or `.rustfmt.toml`, Clippy configuration, and relevant CI commands. Determine the MSRV, language edition, formatting edition, feature matrix, and whether workspace lints are inherited.

Follow the user's request and target repository policy first. Use these recommendations where local policy leaves room. A style request does not imply changing public API compatibility, upgrading the toolchain, adding dependencies, or reformatting unrelated code.

Read [Bevy evidence and scope](references/bevy-evidence.md) when choosing configuration, working inside Bevy, or explaining the provenance of a recommendation. Read the target checkout's current files before treating the recorded snapshot as current policy.

## Package, crate, and module layout

For project creation, package splitting, or layout review, read [layout decisions and evidence](references/project-layout.md). A Cargo package has a manifest and can contain a library crate and binary crates; source modules do not require separate packages.

- Start with one package and cohesive domain modules. Add a package boundary for independent reuse, dependency or platform isolation, a distinct release boundary, or a required crate type such as a procedural macro. Directory size alone is insufficient.
- Keep a small CLI in `src/main.rs` plus modules. Add `src/lib.rs` when reusable logic or external integration tests benefit; extra executable targets belong in `src/bin/`. A library plus CLI can remain one package.
- Use a virtual workspace with `crates/<package>/` for several peer packages, or retain a root package with sibling members when one library is the natural entry point. Follow an established layout; neither form is universally better.
- Keep dependency direction explicit: applications/adapters depend on reusable domain libraries. Prefer domain names over catchall `common` or `utils` packages. Resolve cycles by revisiting responsibilities rather than dumping unrelated types into a shared crate.
- Use private submodules and deliberate re-exports to keep implementation filenames out of the public API. Follow the existing `module.rs` plus `module/` or `module/mod.rs` convention without cosmetic migration.
- Put executable demonstrations in `examples/`, integration tests in `tests/`, and benchmarks in `benches/` only as needed. Heavy tooling or cross-package harnesses may justify their own non-published package.
- Inspect workspace membership, explicit inheritance, feature relationships, and supported resolver/MSRV before modifying manifests. After moving packages or targets, verify Cargo metadata, relative paths, CI commands, and affected dependents as described in the reference.

## Formatting and expression style

- Delegate layout and import sorting to the configured rustfmt. Follow nearby import organization; a prelude glob can be intentional, particularly in Bevy applications. Avoid unrelated import rewrites.
- Prefer field shorthand and `Self` in implementations when clear. Use `..Default::default()` when omitted values are genuinely appropriate; keep meaningful configuration explicit.
- Prefer an early return or `let ... else` for a failed precondition that exits the current path. Keep `match` when alternatives carry meaningful behavior. Remove redundant nesting without changing side effects, evaluation order, or drop timing.
- Choose loops or iterator chains for readability. Do not add abstractions merely to shorten code or satisfy an arbitrary argument-count limit.
- Keep the project's existing formatting edition. Bevy's recorded formatting edition differs from its language edition. Its commented nightly settings are not active requirements.

## API shape and ownership

The naming conventions below follow the Rust API Guidelines; ownership advice is this skill's general recommendation.

- Use Rust casing conventions. Prefer `duration()` to a mechanical `get_duration()`, and use names that expose units or meaning where ambiguity matters.
- Match conversion names to ownership and cost: `as_` for cheap borrowed views, `to_` for conversion work without consuming a non-`Copy` receiver, and `into_` for ownership-consuming conversions. Follow the standard `iter`, `iter_mut`, and `into_iter` distinction.
- Keep implementation details private; choose `pub(crate)` or narrower visibility when sufficient. Avoid breaking existing public APIs for cosmetic consistency. Add traits, generics, builders, and public fields when they solve a concrete caller need.
- Borrow when ownership transfer is unnecessary. Prefer `&str` or `&[T]` over references to owned containers when their extra capabilities are unused. Make cloning, allocation, shared ownership, and interior mutability deliberate rather than default borrow-checker workarounds.
- Preserve useful concrete domain types and invariants. Use semantic enums or newtypes when they prevent meaningful misuse; avoid wrapping every primitive. Derive traits only when their semantics fit the type.
- Prefer a clear safe implementation. Treat performance annotations, unchecked operations, and extra generic specialization as decisions needing a concrete reason, not visual style.

## Errors, documentation, and safety

General error-handling recommendations complement Bevy's documented API and safety practices:

- Represent expected failures with the project's `Result` and error conventions; use `Option` for ordinary absence. Propagate with `?` when appropriate. Do not swallow errors into defaults unless that fallback is part of the contract.
- Reserve panics and `expect` for intentional invariant failures with a useful explanation. Tests may use `unwrap` to assert setup assumptions. Do not claim Bevy bans all `unwrap` calls or impose a new error crate.
- Document public behavior and invariants, including units, mutation, and surprising edge cases. Use rustdoc links and small executable examples that demonstrate useful behavior. Include `# Errors`, `# Panics`, and `# Safety` where applicable, without empty boilerplate sections.
- Explain why non-obvious code exists. For unsafe operations, state the actual validity, aliasing, lifetime, initialization, or synchronization argument in a nearby `// SAFETY:` comment. An unsafe function also needs a caller-facing safety contract; a comment alone does not establish soundness.
- Honor local unsafe policy and keep unsafe operations explicit and scoped. A justified exception in an engine crate is not permission to relax another crate's policy.
- Prefer fixing a lint. Where suppression is justified, scope it narrowly and explain the reason. Use `#[expect(..., reason = "...")]` when supported by the MSRV and appropriate to the lint's actual occurrence; honor existing policy when an expectation would be unreliable across configurations.

## Bevy-specific decisions

Apply these only when the target actually needs them:

- Preserve Bevy's selected lint exceptions instead of blindly enabling all pedantic restrictions. ECS signatures can legitimately be complex.
- Honor crate-level `no_std`, `alloc`, feature gates, and portability constraints. Ordinary applications do not automatically need engine-internal import restrictions.
- Inside Bevy, follow its configured deterministic math replacements and macro delimiter conventions. Do not introduce `bevy_math` or ECS architecture into unrelated Rust projects for style consistency.
- Follow local library logging policy. Standard output remains appropriate for a CLI's intended output; diagnostic logging and user-facing output serve different purposes.

## Verify the change

Use the repository's documented check commands and supported feature combinations. Without a wrapper, typical focused checks are:

```sh
cargo fmt --all -- --check
cargo clippy -p <affected-package> --all-targets -- -D warnings
cargo test -p <affected-package>
cargo test -p <affected-package> --doc
```

These are command templates; substitute the package and adapt targets/features to CI. A workspace-wide formatting check is read-only; when applying fixes, keep edits within scope. Do not assume `--all-features` is valid for every project or that the optional `cargo ci` alias exists.

Run behavior tests for behavioral changes and doctests for changed examples. Formatting-only changes normally need formatting verification, not new tests. Complete required repository checks and report unavailable checks or pre-existing failures accurately. In a review-only request, report actionable findings with locations and reasons rather than editing files.
