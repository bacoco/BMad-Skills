"""Ensure lightweight YAML shim is available during tests.

Python automatically imports :mod:`sitecustomize` on start-up when the
module is present on ``sys.path``.  The shim below makes sure our
minimal YAML implementation is registered even in environments where the
current working directory is not searched for modules (as happens on
some CI sandboxes).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

MODULE_NAME = "yaml"

if MODULE_NAME not in sys.modules:
    yaml_dir = Path(__file__).resolve().parent / MODULE_NAME
    module_file = yaml_dir / "__init__.py"

    if module_file.exists():
        spec = importlib.util.spec_from_file_location(MODULE_NAME, module_file)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules.setdefault(MODULE_NAME, module)
