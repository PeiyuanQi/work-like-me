---
name: manage-virtual-environments
description: "Sets up, reuses, repairs, pins, or verifies isolated project environments and toolchains for Python, Node.js, Rust, Go, Java, .NET, and other stacks, preferring repository-declared versions, existing environments, lockfiles, and user-scope tooling. Use for requests such as \"set up a virtual environment\", \"create venv\", \"activate the environment\", \"install dependencies\", \"use uv\", \"use nvm\", \"create .nvmrc\", or \"install Rust\", or when work is blocked by a missing or wrong runtime."
---

# Manage Virtual Environments

Version: 1.3.0

Create or select a reproducible project environment without damaging an
existing toolchain or silently changing dependency intent.

## 1. Inspect Before Changing Anything

1. Read repository instructions and setup documentation.
2. Inspect manifests, lockfiles, and version pins such as `pyproject.toml`,
   `uv.lock`, `requirements*.txt`, `package.json`, `package-lock.json`,
   `pnpm-lock.yaml`, `.nvmrc`, `.node-version`, `rust-toolchain.toml`,
   `Cargo.toml`, and `Cargo.lock`.
3. Check `git status` and preserve user-owned changes.
4. Reuse a documented or existing environment before creating another one.
5. Detect the host OS and shell before choosing commands.

Useful inventory commands:

```powershell
# Windows PowerShell
Get-Command uv, py, python, python3, node, npm, nvm, fnm, rustup, rustc, cargo `
  -ErrorAction SilentlyContinue | Select-Object Name, Source
Get-ChildItem -Force -Directory | Where-Object Name -Match '^\.?(venv|env)'
```

```bash
# POSIX shell
for command_name in uv python3 python node npm nvm fnm rustup rustc cargo; do
  command -v "$command_name" 2>/dev/null || true
done
find . -maxdepth 1 -type d \( -name '.venv*' -o -name 'venv*' -o -name 'env*' \)
```

Command discovery alone can mislead: on Windows, `python.exe` or `python3.exe`
may be a disabled Microsoft Store alias. Run the candidate executable with
`--version` before relying on it.

## 2. Python

### Prefer an existing environment

In automated tool calls, invoke the environment's interpreter directly, because
activation does not persist across separate shell calls:

```powershell
& '.\.venv\Scripts\python.exe' --version
& '.\.venv\Scripts\python.exe' -m pip check
```

```bash
.venv/bin/python --version
.venv/bin/python -m pip check
```

Adapt the path when the repository uses a named environment such as
`.venv-map-tools`. A missing bare `python` is not a reason to delete or
recreate an existing environment.

### Create with uv when the repository supports it

```powershell
uv venv .venv
if (Test-Path 'uv.lock') { uv sync --locked } else { uv sync }
```

```bash
uv venv .venv
if [ -f uv.lock ]; then uv sync --locked; else uv sync; fi
```

For a requirements-based project:

```powershell
uv venv .venv
uv pip install --python '.\.venv\Scripts\python.exe' -r requirements.txt
```

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

### Fall back to the standard library venv

```powershell
py -3 -m venv .venv
& '.\.venv\Scripts\python.exe' -m pip install --upgrade pip
& '.\.venv\Scripts\python.exe' -m pip install -r requirements.txt
```

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

Use `python -m pip` rather than bare `pip` so installation targets the intended
interpreter. For an interactive shell, activation is optional convenience:

```powershell
.\.venv\Scripts\Activate.ps1
```

```bash
source .venv/bin/activate
```

## 3. Node.js

1. Prefer the version in repository docs, `.nvmrc`, `.node-version`, the
   `package.json` `engines` field, or Volta configuration.
2. Use the already-adopted version manager; add a second manager only with a
   clear need.
3. POSIX `nvm` and Windows `nvm-windows` are different tools. Unix `NVM_DIR`
   initialization does not apply on Windows.

POSIX `nvm`:

```bash
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm install  # reads .nvmrc when present
nvm use
```

Windows `nvm-windows`:

```powershell
$nodeVersion = '<version-from-repo-or-user>'
nvm version
nvm install $nodeVersion
nvm use $nodeVersion
node --version
```

When the user explicitly requests a version and a project pin:

```powershell
$nodeVersion = '<version-from-user>'
Set-Content -LiteralPath '.nvmrc' -Value $nodeVersion
```

```bash
node_version='<version-from-user>'
printf '%s\n' "$node_version" > .nvmrc
```

Install dependencies without needlessly rewriting lockfiles:

- `npm ci` when `package-lock.json` exists; otherwise `npm install`.
- `pnpm install --frozen-lockfile` when `pnpm-lock.yaml` exists.
- `yarn install --immutable` for modern Yarn lockfile-based projects.

Verify `node --version`, the package-manager version, and the repository's
build or test command.

## 4. Rust

Rust uses a pinned toolchain rather than a per-project virtual environment.

1. Reuse `rust-toolchain.toml` or `rust-toolchain` when present.
2. If Rust is missing and setup is in scope, prefer a trusted OS package-manager
   installation of Rustup. On Windows, prefer the signed Winget route over
   downloading and directly launching a bootstrap executable:

```powershell
winget install --id Rustlang.Rustup -e --source winget `
  --accept-package-agreements --accept-source-agreements --silent
$cargoBin = Join-Path $env:USERPROFILE '.cargo\bin'
$env:PATH = "$cargoBin;$env:PATH"
```

Before installing, verify `winget` is available, and check for the MSVC C++
build tools when targeting `*-pc-windows-msvc`, because Rustup alone does not
provide the native linker. If Winget is unavailable, follow repository
guidance, or use the official Rustup installer only when local command policy
permits it.

3. Install the repository-pinned toolchain. If no pin exists, use the version
   the user explicitly requested; otherwise use the repository's documented
   default and record the choice.
4. Create a new `rust-toolchain.toml` only when the user requests a project pin
   or repository convention requires one.

```powershell
rustup show active-toolchain
rustc --version
cargo --version
if (Test-Path 'Cargo.lock') { cargo check --locked } else { cargo check }
```

Use the equivalent commands in POSIX shells. Run focused tests once the
toolchain is usable.

## 5. Other Language Toolchains

Go, Java, and .NET use versioned toolchains and project dependency managers
rather than Python-style virtual environments.

- Go: honor `go.mod`/`go.work`; run `go mod download`, `go build ./...`, and
  `go test ./...` as appropriate.
- Java: prefer the repository's Maven or Gradle wrapper; verify the configured
  JDK before using a system installation.
- .NET: honor `global.json`; run `dotnet --info`, restore, build, and focused
  tests with the pinned SDK.

Install a missing toolchain only when setup is part of the request. Prefer
user-scope, version-managed, or OS package-manager installation over global
ad-hoc changes.

## 6. Safety and Verification

- Install Python or Node packages into the project environment, not globally,
  when a project environment is available.
- Before deleting, replacing, or recursively moving an existing environment,
  resolve its exact path and confirm the replacement is intended.
- Prefer lockfile-preserving commands, and report any manifest or lockfile
  changes.
- Dependency installation can execute project or package scripts, so use
  repository-defined commands and trusted sources.
- Add environment directories to `.gitignore` only when needed and consistent
  with repository convention.
- Stage files or create setup documentation only when the user requested it or
  the enclosing workflow explicitly requires it.
- Verify the exact executable path, runtime version, dependency health, and a
  focused repository build or test command.
- Report what was reused or created, commands run, files changed, and any setup
  the user must repeat in a new shell.
