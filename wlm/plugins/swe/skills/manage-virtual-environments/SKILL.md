---
name: manage-virtual-environments
description: Use when user wants to set up, create, or manage virtual environments for Python, Node.js, or other programming language projects. Triggers on "set up virtual environment", "create venv", "activate virtual env", "manage python environment", "node environment setup", "nvm", "uv", "pipenv", "virtualenv", or when starting work on a new project that needs environment configuration. Essential for maintaining clean, isolated coding environments — always use this skill when setting up project environments.
---

# Manage Virtual Environments

Set up and manage isolated virtual environments for programming projects. This skill detects project languages and creates appropriate environments using the best available tools.

## Why This Matters

- **Isolation** — Prevents dependency conflicts between projects
- **Reproducibility** — Ensures consistent environments across machines
- **Best practices** — Uses modern, fast tools (uv, nvm) with fallbacks

## Step 1: Detect Project Language

Scan the project directory to identify the primary language:

```bash
# Check for Python
ls -la | grep -E "(requirements\.txt|pyproject\.toml|Pipfile|setup\.py)"
test -f "requirements.txt" || test -f "pyproject.toml" || test -f "Pipfile" && echo "python"

# Check for Node.js
ls -la | grep -E "(package\.json|\.nvmrc|node_modules)"
test -f "package.json" && echo "nodejs"

# Check for other languages
test -f "Cargo.toml" && echo "rust"
test -f "go.mod" && echo "go"
test -f "pom.xml" && echo "java"
test -f "*.csproj" && echo "csharp"
```

If no language detected, ask the user what language they're working with.

---

## Step 2: Python Virtual Environment

### Option A: Using uv (Preferred — Fast, Modern)

```bash
# Check if uv is available
command -v uv && echo "uv available" || echo "uv not found"
```

**If uv is available:**
```bash
# Create virtual environment in .venv
uv venv .venv

# Activate and install dependencies
source .venv/bin/activate

# Install from pyproject.toml (preferred)
uv sync

# OR install from requirements.txt
uv pip install -r requirements.txt

# OR install specific packages
uv pip install <package-name>
```

**Best practices with uv:**
- Use `uv sync` for projects with `pyproject.toml`
- Use `uv pip install -r requirements.txt` for legacy projects
- Add `.venv/` to `.gitignore`

### Option B: Using pip venv (Fallback)

```bash
# Check if python3 is available
command -v python3 && echo "python3 available"

# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# OR for pyproject.toml projects
pip install -e .
```

---

## Step 3: Node.js Virtual Environment (Using nvm 24)

### Check nvm Availability

```bash
# Check if nvm is installed
command -v nvm && nvm --version || echo "nvm not found"

# Or check via loaded nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm --version
```

### Using nvm 24 for Node.js Projects

```bash
# Ensure nvm is loaded
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Check if .nvmrc exists in project
if [ -f ".nvmrc" ]; then
  nvm install  # Installs version from .nvmrc
  nvm use
else
  # Use nvm 24 (latest stable LTS)
  nvm install 24
  nvm use 24
fi

# Install dependencies
npm install

# Verify installation
node --version
npm --version
```

### Create .nvmrc for Project

```bash
# Create .nvmrc with version 24
echo "24" > .nvmrc

# Add to git (optional but recommended)
git add .nvmrc
```

---

## Step 4: Other Language Environments

### Rust (Cargo)

```bash
# Verify Cargo.toml exists
test -f "Cargo.toml" && echo "Rust project detected"

# Build project
cargo build

# Run tests
cargo test

# Verify installation
rustc --version
cargo --version
```

### Go

```bash
# Verify go.mod exists
test -f "go.mod" && echo "Go project detected"

# Download dependencies
go mod download

# Build project
go build ./...

# Run tests
go test ./...

# Verify installation
go version
```

### Java/Maven

```bash
# Use Maven wrapper or system Maven
./mvnw install  # If using wrapper
mvn install    # System Maven
```

---

## Step 5: Verify Environment

After setup, verify everything works:

```bash
# Python
source .venv/bin/activate
python --version
pip list

# Node.js
nvm use
node --version
npm --version
```

---

## Step 6: Document Environment Setup

Create or update a `SETUP.md` or `ENVIRONMENT.md` file:

```markdown
# Environment Setup

## Python
```bash
source .venv/bin/activate
```

## Node.js
```bash
nvm use
npm install
```

## Commands
- Run tests: `pytest` / `npm test`
- Install deps: `uv sync` / `npm install`
```

---

## Best Practices Checklist

- [ ] Use `uv` for Python (fast, reliable) — fallback to `pip venv`
- [ ] Use `nvm 24` for Node.js projects
- [ ] Activate environment before installing dependencies
- [ ] Keep `.venv/` and `node_modules/` in `.gitignore`
- [ ] Create `.nvmrc` files for Node.js projects
- [ ] Use `pyproject.toml` over `requirements.txt` when possible
- [ ] Run tests after environment setup to verify
- [ ] Run `go mod download` and `go test ./...` for Go projects
- [ ] Run `cargo build` and `cargo test` for Rust projects
