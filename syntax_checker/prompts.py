"""Loads the .md prompt files and fills their {placeholders}."""

import re

from . import config


def _read(name: str) -> str:
    return (config.PROMPTS_DIR / name).read_text(encoding="utf-8")


SYSTEM = _read("system.md")
SYNTAX_SEMANTICS = _read("syntax_semantics.md")


def fill(template: str, **values: str) -> str:
    """Single-pass {name} substitution. Other braces (e.g. JSON examples) are left alone,
    and inserted values are never re-scanned for placeholders."""
    return re.sub(
        r"\{(\w+)\}",
        lambda m: str(values.get(m.group(1), m.group(0))),
        template,
    )