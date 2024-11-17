from typing import Any

from .bus import Bus
from .exitable import Exitable


class NameOwner(Exitable):
    def __init__(self, bus: Bus, name: str, allow_replacement: bool, replace: bool) -> None:
        ...

    def unown(self, *args: Any, **kwargs: Any) -> None:
        ...


class RequestNameMixin:
    def request_name(self,
                     name: str,
                     allow_replacement: bool = ...,
                     replace: bool = ...) -> NameOwner:
        ...
