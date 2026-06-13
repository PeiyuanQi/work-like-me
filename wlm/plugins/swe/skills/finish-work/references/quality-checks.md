# Quality Checks

Choose checks from the repo's own tooling first:

1. Dedicated quality command from docs, `Makefile`, package scripts, task files,
   or CI config.
2. Formatter and linter configs such as `.pre-commit-config.yaml`,
   `pyproject.toml`, `eslint.config.js`, `.eslintrc`, `.editorconfig`, `ruff.toml`,
   `Cargo.toml`, or `go.mod`.
3. Language defaults only when the repo is silent.

Use the smallest check that provides confidence for the change. Broaden the
scope when touching shared behavior, APIs, persistence, auth, concurrency,
build tooling, or user-facing workflows.

If checks fail before commit, report the failing command and key failure. Do not
commit failing work unless the user explicitly accepts the risk.
