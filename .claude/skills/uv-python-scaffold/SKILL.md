---
name: uv-python-scaffold
description: Scaffold a minimal Python backend with uv, a runnable Hello World entry point, and a synced environment. Use when the user asks to create, start, bootstrap, or scaffold a Python project or backend using uv.
---

# uv Python Scaffold

Creates a small Python project using [uv](https://docs.astral.sh/uv/), adds a Hello World entry point, runs it, and syncs the environment.

## Prerequisites

Check that uv is installed:

```bash
uv --version
```

If uv is missing, install it using the official instructions: https://docs.astral.sh/uv/getting-started/installation/.

## Scaffold

1. Choose a project directory name. Use `backend` if the user has not specified one. If it already exists, do not overwrite it; ask before proceeding or choose another name.

2. Create the project:

   ```bash
   uv init backend
   cd backend
   ```

3. Replace the generated `main.py` with `scripts/main.py` from this skill. For example, from the new project directory:

   ```powershell
   Copy-Item <skill-dir>/scripts/main.py ./main.py
   ```

4. Run and sync:

   ```bash
   uv run main.py
   uv sync
   ```

   Expected output:

   ```
   Hello, World! Your uv backend is running.
   ```

## Result

```text
backend/
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

`uv run` creates the virtual environment automatically when needed.

## Handy commands

| Task | Command |
|---|---|
| Add a package | `uv add fastapi` |
| Add a development package | `uv add --dev pytest` |
| Remove a package | `uv remove fastapi` |
| Pin a Python version | `uv python pin 3.12` |
| Run tests | `uv run pytest` |