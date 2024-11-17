from typing import Any, Callable
from collections.abc import Iterable


class _empty:
    ...


class Signature:
    empty: _empty
    parameters: Any
    return_annotation: Any

    def __init__(self,
                 parameters: Iterable[Parameter] | None = None,
                 return_annotation: Any = ...) -> None:
        ...


class Parameter:
    empty: _empty
    POSITIONAL_ONLY: int
    POSITIONAL_OR_KEYWORD: int
    KEYWORD_ONLY: int
    name: str
    kind: int
    annotation: Any

    def __init__(self, name: str, kind: int, default: Any = ..., annotation: Any = ...) -> None:
        ...


def signature(f: Callable[..., Any]) -> Signature:
    ...
