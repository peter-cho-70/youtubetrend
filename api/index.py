"""
Vercel Python Runtime entrypoint.

Vercel expects an ASGI app named `app` inside `api/` (e.g. `api/index.py`).
"""

from backend.main import app  # noqa: F401

