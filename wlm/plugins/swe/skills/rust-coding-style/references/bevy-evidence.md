# Bevy evidence and scope

Inspected on 2026-09-08. Repository snapshot: `bevyengine/bevy` commit `b3fd9d783124128ac169704d0f4c0b8790daae78` (then `main`). This is provenance, not a required dependency or toolchain pin. Website guidance was read on the same date and can change independently.

This is an original synthesis of configuration and design guidance, not a vendored third-party skill. It requires no Bevy installation or network access for ordinary use. Recheck upstream when updating Bevy-specific claims.

## Findings

| Evidence | What it establishes | How to apply it |
| --- | --- | --- |
| [rustfmt.toml](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/rustfmt.toml) | Enables field shorthand, Unix newlines, and formatting edition 2021. Nightly import grouping and comment normalization are commented out; automatic comment wrapping is discouraged in comments. | Use the active formatter settings. Do not interpret comments as enabled options or change a project's formatting edition incidentally. |
| [Cargo.toml](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/Cargo.toml#L48) | Selects individual clarity, documentation, pointer, unsafe, and suppression lints. Allows complexity, argument-count, and lifetime lints. Library and root/example policies differ. | Adopt relevant rules selectively and check crate inheritance. The root's language edition is 2024 despite formatting edition 2021. |
| [clippy.toml](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/clippy.toml) | Configures documentation identifiers, private-item checking, deterministic floating-point replacements, and `children!` square brackets. | These are domain constraints, not general Rust requirements. Private-item checking configures relevant Clippy checks; it does not itself require documentation on every private item. |
| [Contributor introduction](https://bevy.org/learn/contribute/introduction/) | Prioritizes caller ergonomics, selective public APIs, modularity, careful dependencies, and useful tests. | Evaluate interface usability and maintenance cost rather than maximizing abstraction or configurability. |
| [Writing documentation](https://bevy.org/learn/contribute/helping-out/writing-docs/) | Favors accurate, concise inline documentation and compiler-checked examples. | Explain behavior and link broader context; examples should remain executable. |
| [Timer implementation](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/crates/bevy_time/src/timer.rs) | Shows private state, semantic `TimerMode`, named constructors, shorthand/default initialization, feature-gated derives, units in methods, links, and behavioral examples. | This illustrates API clarity. Its `#[inline]` annotations and exact import layout are not universal mandates. |
| [ECS crate root](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/crates/bevy_ecs/src/lib.rs) | Uses `no_std`, optional `std`, `alloc`, a curated prelude, and a reasoned crate-level unsafe expectation. | Preserve existing platform and safety boundaries. A workspace denial can have deliberate local exceptions. |

## Enforcement actually observed

[Format command](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/tools/ci/src/commands/format.rs):

```sh
cargo fmt --all -- --check
```

[Clippy command](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/tools/ci/src/commands/clippy.rs), omitting its optional job-count argument:

```sh
cargo clippy --workspace --all-targets --all-features -- -Dwarnings
```

The [lints command](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/tools/ci/src/commands/lints.rs) combines these. The [`cargo ci` alias](https://github.com/bevyengine/bevy/blob/b3fd9d783124128ac169704d0f4c0b8790daae78/.cargo/config_aliases.toml) is supplied in an optional configuration template. Do not assume it is already installed. Other projects may require separate feature combinations instead of all features together.

## Broader Rust guidance

The [Rust API naming guidelines](https://rust-lang.github.io/api-guidelines/naming.html) support casing, getter names, ownership-aware conversion names, and iterator naming. The [documentation guidelines](https://rust-lang.github.io/api-guidelines/documentation.html) support useful examples, propagation in fallible examples, and explicit error, panic, and safety contracts.

Borrowing over unnecessary cloning, choosing domain types, and avoiding incidental API changes are this skill's general engineering recommendations. They are not claims that Bevy mechanically enforces those choices everywhere. The inspected lint configuration is not a blanket prohibition on panics, `unwrap`, glob imports, explicit lifetimes, or unsafe code.

## Optional formatting baseline

For a project explicitly adopting Bevy's formatting choices, the observed active settings are:

```toml
use_field_init_shorthand = true
newline_style = "Unix"
style_edition = "2021"
```

For a fresh project without that preference, use its supported rustfmt defaults and selected style edition. Do not copy this snapshot just to make all Rust projects resemble Bevy. Likewise, lint adoption should account for the project's MSRV, existing warnings, and whether it is a library, CLI, embedded crate, or engine.
