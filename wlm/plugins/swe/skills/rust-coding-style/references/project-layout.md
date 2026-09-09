# Rust project layout: decisions and evidence

## Choose a boundary before choosing folders

These are recommendations derived from the examples below and Cargo's documented behavior. They are not a single author's published style guide.

| Situation | Starting layout | Reason to change it |
| --- | --- | --- |
| Small library or application | One `Cargo.toml`, `src/lib.rs` or `src/main.rs`, domain modules | Split when a real consumer, dependency boundary, or platform requirement appears. |
| CLI with reusable logic | One package with `src/lib.rs` and a thin `src/main.rs` | Separate CLI package when its dependencies, distribution, or release lifecycle warrant it. |
| Several tools sharing the same library and dependencies | `src/bin/<tool>.rs` in the same package | Separate packages when tools need materially different dependency or build boundaries. |
| Several cohesive product subsystems | Virtual root workspace, packages under `crates/` | Keep dependency direction clear and choose intentional default members. |
| Main public library plus runtime/internal support | Root package and sibling packages in one workspace | Preserve the obvious public entry point; `crates/` nesting is optional. |
| Independent exercises or experiments | Topic-grouped workspace members, or independent packages | Do not make unrelated experiments share product abstractions merely because they share a workspace. |

Illustrative shapes, not mandatory scaffolds; create only files needed by the task:

```text
small-tool/
  Cargo.toml
  src/
    main.rs             # command-line setup and orchestration
    lib.rs              # only if reusable/library logic is useful
    document.rs         # domain module
    document/parse.rs   # private implementation behind document.rs
  tests/roundtrip.rs    # public API integration test, when useful
  examples/read.rs      # executable usage example, when useful
```

```text
product/
  Cargo.toml            # virtual workspace, no [package]
  crates/
    product-model/Cargo.toml
    product-model/src/lib.rs
    product-cli/Cargo.toml
    product-cli/src/main.rs
  tools/                # optional tooling; membership must be declared
```

The CLI depends on the model library in the second example. Do not create an empty model crate in advance of meaningful shared logic. A package boundary adds manifests, public interfaces, dependency management, and potentially release coordination; it does not guarantee faster builds.

Keep `macro_rules!` macros in an ordinary library when sufficient. Procedural macros use a `proc-macro` library target; separate that package from runtime code when both are needed. The ordinary-macro and procedural-macro examples below show why “all macros need a separate macros crate” is incorrect.

## Cargo mechanics to preserve

Based on the [Cargo workspace reference](https://doc.rust-lang.org/cargo/reference/workspaces.html):

- Set a virtual workspace's resolver explicitly, compatible with its supported toolchain. Preserve an existing choice unless changing it is in scope.
- `members`, `exclude`, and `default-members` have different roles: membership, removal from membership, and default command selection. `default-members` does not remove packages from `--workspace` checks.
- Workspace metadata, dependencies, and lints require member opt-in, such as `edition.workspace = true`, `dep.workspace = true`, and `[lints] workspace = true`.
- Workspace dependency features are additive; shared declarations do not force every member to depend on that library. Put optionality in the consuming package.
- Keep profiles at the workspace root. Members share a root lockfile and build-output directory. Excluded independent packages need their own coherent configuration.

Use the [Cargo package-layout conventions](https://doc.rust-lang.org/cargo/guide/project-layout.html) for library, binary, example, benchmark, and test targets. Integration tests compile separately and exercise accessible APIs; use local unit tests for private details. A directory in `src/` is not automatically a Rust module: declare it from its parent. Preserve custom target paths when already configured.

## Evidence from VitalyAnkh's account

Inspected 2026-09-08. Links record the default-branch snapshots actually inspected; they are provenance, not runtime pins. No projects were compiled, and structural examples do not establish production readiness. Small learning projects are useful evidence of layout, not blanket endorsements of their code or dependency versions.

### Personal or learning repositories

- [algorithms](https://github.com/VitalyAnkh/algorithms/tree/87b3ae48304a5436ccb3d56a700e059b1a0a28ed): its manifest names VitalyR. One library package contains `data`, `searching`, and `sorting` modules. [`sorting.rs`](https://github.com/VitalyAnkh/algorithms/blob/87b3ae48304a5436ccb3d56a700e059b1a0a28ed/src/sorting.rs) keeps algorithm implementation modules private and re-exports selected functions. This is a concrete example of organizing implementation without multiplying packages.
- [bevy_newton](https://github.com/VitalyAnkh/bevy_newton/tree/5f2a5a6a37c6da173c4068aa988c16c981bb3be8): its manifest names VitalyR. A very small library plus `examples/simple.rs`; useful as the minimal plugin/library shape, not evidence for a mature physics-engine architecture.
- [pngme](https://github.com/VitalyAnkh/pngme/tree/34f02eb6b16e62828a6c876ba306cab2628f8783): an account-owned non-fork with one binary package and `args`, `commands`, `chunk`, `chunk_type`, and `png` modules. The inspected `main` is unfinished and `commands.rs` empty. Treat the domain-oriented module skeleton as illustrative, not a finished CLI design or verified original authorship of every part.
- [awesome-macros](https://github.com/VitalyAnkh/awesome-macros/tree/7d63b9d1ab9fe0e729f4d0aa50fa614c9196c107): its manifest names VitalyR. A single ordinary library with declarative macros and local tests; its name does not imply a procedural-macro target.
- [play workspace](https://github.com/VitalyAnkh/play/blob/77f30341c3d8e91fcb419d8fc9a66f11fa0550f0/Cargo.toml): an account-owned non-fork collecting exercises and experiments. Topic directories contain packages; members use globs and explicit exclusions. `atomics_and_locks` has a main binary, an additional `src/bin/atomic.rs`, examples, and explicit edition inheritance. This supports flexible folder grouping and multiple targets per package. Its wildcard dependency versions and experimental exclusions are not recommended production defaults; a collection of exercises is not proof of authorship of every example.

### Upstream comparisons, with attribution

- [Typst fork](https://github.com/VitalyAnkh/typst/blob/26e924d311367d69e819a62bfd505ed6787b4537/Cargo.toml), fork of `typst/typst`: virtual workspace with `crates/*`, documentation and test packages, and CLI as default member. Separate syntax, evaluation, layout, export, CLI, and macro packages illustrate larger subsystem boundaries. [`typst-cli`](https://github.com/VitalyAnkh/typst/blob/26e924d311367d69e819a62bfd505ed6787b4537/crates/typst-cli/Cargo.toml) consumes the libraries; [`typst-macros`](https://github.com/VitalyAnkh/typst/blob/26e924d311367d69e819a62bfd505ed6787b4537/crates/typst-macros/Cargo.toml) declares `proc-macro = true`. Attribute this architecture to the Typst project, not solely to the fork owner.
- [Rayon fork](https://github.com/VitalyAnkh/rayon/blob/ee0a00bdb1ab039e178a215ad5712fb7fa58e58f/Cargo.toml), fork of `rayon-rs/rayon`: root library package plus `rayon-core` and non-published `rayon-demo` workspace members. The root depends on `rayon-core`. This demonstrates that a useful multi-package library need not have a virtual root or `crates/` folder. Attribute this architecture to Rayon.
- [softposit-rs](https://github.com/VitalyAnkh/softposit-rs/blob/a6f304e94fd2b19e86ea892b170f723e862d7368/Cargo.toml): GitHub reports a non-fork, but the manifest names Andrey Zgarbul and points to `gitlab.com/burrbull/softposit-rs`. Do not infer personal authorship from account ownership. Its single library uses nested numeric modules, optional integrations, examples, and a benchmark; it demonstrates substantial modularity inside one package.

## Verify an actual layout change

Inspect `cargo metadata --no-deps --format-version 1` from the intended root to confirm packages, targets, membership, and default members. This inspects structure, not compilation or behavior. Use an existing lockfile/offline options when suitable; do not add dependencies merely to run this check.

After a move or split, check path dependencies, `include_str!`/asset paths, build scripts, custom target paths, and CI working directories. Run required checks for the changed packages and their affected consumers, including examples or integration tests whose target paths moved. If publication is in scope, verify package contents and registry-compatible internal dependencies; do not publish merely to validate a layout.
