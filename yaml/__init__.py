"""Lightweight YAML compatibility layer used for tests.

This module provides a tiny subset of the :mod:`yaml` API that is
required by the BMAD Skills test-suite.  The real project depends on
PyYAML when running inside Claude's execution environment, however the
unit tests executed in this kata only rely on a couple of functions
(:func:`safe_load` and :func:`dump`).  Importing PyYAML in the execution
environment of these exercises is intentionally avoided to keep the
runtime minimal, so we emulate the behaviour we need with the standard
library.

The implementation underneath simply serialises to and from JSON.  The
metrics and sprint-status files that the tests interact with only
contain data structures that are also valid JSON, so this strategy keeps
parsing robust while remaining dependency free.  The functions mimic the
PyYAML signatures closely enough for our needs and raise :class:`YAMLError`
when the content cannot be parsed.
"""

from __future__ import annotations

import json
from typing import Any, IO, Optional

__all__ = ["YAMLError", "safe_load", "dump"]


class YAMLError(ValueError):
    """Exception raised when YAML content cannot be processed."""


def _read_input(stream: Any) -> str:
    """Return the textual content from ``stream`` or a string value."""

    if hasattr(stream, "read"):
        data = stream.read()
    else:
        data = stream

    if isinstance(data, bytes):
        return data.decode("utf-8")
    if data is None:
        return ""
    return str(data)


def safe_load(stream: Any) -> Any:
    """Parse YAML content using a permissive JSON-based loader."""

    text = _read_input(stream).strip()
    if not text:
        return None

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:  # pragma: no cover - exercised via tests
        raise YAMLError("Invalid YAML content") from exc


def dump(
    data: Any,
    stream: Optional[IO[str]] = None,
    default_flow_style: bool = False,
    sort_keys: bool = True,
) -> str:
    """Serialise *data* to YAML using JSON formatting."""

    indent = None if default_flow_style else 2
    text = json.dumps(
        data,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=False,
    )

    if stream is not None:
        stream.write(text)
        return None

    return text
