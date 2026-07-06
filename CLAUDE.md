# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Overview

**Lawgorithm Python SDK** — the official Python client library for the
[Lawgorithm](https://lawgorithm.io) AI Act compliance platform. It wraps the
Lawgorithm HTTP API (AI system management, compliance checks, incidents,
dossiers, attestations, MLOps evidence import) behind a typed `LawgorithmClient`.
This is a **reusable library published to PyPI** — it is imported by other
applications and has no executable entry point of its own.

## Stack

- Python 3.10+ (src-layout: `src/lawgorithm/`)
- `httpx` (HTTP transport) + `pydantic` v2 (typed models)
- Build backend: `hatchling` · Lint: `ruff` · Types: `mypy --strict`
- Tests: `pytest` (+ `pytest-asyncio`, `pytest-httpx`) — `asyncio_mode = "auto"`

## Logging

Binding of the global *Logging & observability* guideline for a **library**
(there is no application here to own the root logger):

- The package **does not configure the root logger** and writes **no log file** —
  that is the responsibility of the host application that imports the SDK.
- `src/lawgorithm/__init__.py` attaches a single `logging.NullHandler()` to the
  package root logger (`logging.getLogger("lawgorithm")`), so importing the SDK
  never emits a "last resort" message to stderr.
- Modules that need to log should use `logging.getLogger(__name__)`; never call
  `logging.basicConfig()` or add non-null handlers from library code.
- Never log secrets (API tokens, private keys, Authorization headers, request
  bodies).
