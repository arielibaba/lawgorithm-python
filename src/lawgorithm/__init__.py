"""Lawgorithm Python SDK - AI Act Compliance Platform.

Usage:
    from lawgorithm import LawgorithmClient

    client = LawgorithmClient(
        api_url="https://api.lawgorithm.io",
        api_token="your-api-token"
    )

    # Check compliance
    result = client.check_compliance(system_id="uuid")

    # Export dossier
    dossier = client.export_dossier(system_id="uuid", format="markdown")
"""

import logging

from lawgorithm.client import LawgorithmClient
from lawgorithm.exceptions import (
    LawgorithmError,
    AuthenticationError,
    ComplianceError,
    NotFoundError,
    ValidationError,
)
from lawgorithm.models import (
    System,
    Policy,
    ControlResult,
    ComplianceCheckResult,
    Incident,
    Attestation,
    DossierExport,
)

# Library logging best practice: attach a NullHandler to the package's root
# logger so importing the SDK never emits a "last resort" message to stderr.
# The host application is responsible for configuring handlers/levels.
# Individual modules use logging.getLogger(__name__).
logging.getLogger("lawgorithm").addHandler(logging.NullHandler())

__version__ = "0.1.0"

__all__ = [
    # Client
    "LawgorithmClient",
    # Exceptions
    "LawgorithmError",
    "AuthenticationError",
    "ComplianceError",
    "NotFoundError",
    "ValidationError",
    # Models
    "System",
    "Policy",
    "ControlResult",
    "ComplianceCheckResult",
    "Incident",
    "Attestation",
    "DossierExport",
]
