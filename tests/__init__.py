"""Test package initialisation.

Adding this module ensures the lightweight YAML shim is available before
any test modules import :mod:`yaml`.  The production bundle uses PyYAML
through Claude's runtime, but our unit tests execute in a minimal
environment that doesn't ship with optional dependencies.
"""

from __future__ import annotations

import sys

if "yaml" not in sys.modules:
    from importlib import import_module

    import_module("yaml")
