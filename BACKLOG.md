# Backlog — Lawgorithm Python SDK

Tracking file for the official Python SDK for the Lawgorithm AI Act Compliance Platform.

## Done

- Core `LawgorithmClient` (`src/lawgorithm/client.py`) — synchronous HTTP client on `httpx`, configurable `api_url`/`api_token`, context-manager support (`__enter__`/`__exit__`, `close()`).
- Request helpers (`_get`/`_post`/`_patch`/`_delete`) with centralized response handling and error mapping.
- Typed exception hierarchy (`src/lawgorithm/exceptions.py`): `LawgorithmError`, `AuthenticationError`, `ComplianceError`, `NotFoundError`, `ValidationError`.
- Pydantic models (`src/lawgorithm/models.py`): `System`, `Policy`, `ControlResult`, `Incident`, `IncidentStats`, compliance-history / dossier-completeness / attestation types.
- AI system management: `list_systems`, `get_system`, `create_system`, `classify_system` (AI risk classification).
- Policy engine: `list_policies`, `execute_policies`, `sync_policies`.
- Compliance checks for CI/CD: `check_compliance` (standard + strict mode raising `ComplianceError`).
- Post-market surveillance (AI Act Art. 72): `list_incidents`, `create_incident`, `get_incident_stats`, `notify_authority`.
- Compliance state history + tamper detection: `get_compliance_history`, `verify_compliance_chain`.
- Attestations (Ed25519): `create_attestation`, `verify_attestation`.
- Compliance dossier ("Le Dossier Vivant"): `check_dossier_completeness`, `export_dossier`.
- MLOps evidence import: `import_mlflow_run`, `import_wandb_run`.
- Environment-variable configuration (`LAWGORITHM_API_URL`, `LAWGORITHM_API_TOKEN`).
- Packaging: `pyproject.toml` (hatchling build, `dev` extras), ruff + mypy (strict) + pytest config.
- Unit tests (`tests/test_client.py`) and public API exports (`src/lawgorithm/__init__.py`).
- README with quick start and per-feature usage examples.

## In progress

- (none tracked)

## Planned

- Async client variant (repo already configures `pytest-asyncio` / `asyncio_mode = "auto"`).
- Expand test coverage across all client methods and error paths.
- Retry / backoff handling for transient HTTP failures.
- CI workflow (lint + type-check + tests) and PyPI publish automation.
