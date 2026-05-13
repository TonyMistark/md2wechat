from __future__ import annotations

from . import default, github

_registry: dict[str, object] = {
    default.NAME: default,
    github.NAME: github,
}

DEFAULT_STYLE = "default"


def get_style(name: str):
    if name not in _registry:
        available = ", ".join(sorted(_registry))
        raise ValueError(f"Unknown style: {name!r}. Available: {available}")
    return _registry[name]


def list_styles() -> list[tuple[str, str]]:
    return [(m.NAME, m.DESCRIPTION) for m in _registry.values()]
