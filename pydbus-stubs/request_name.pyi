from .bus import Bus
from .exitable import Exitable


class NameOwner(Exitable):
    def __init__(self, bus: Bus, name: str, allow_replacement: bool, replace: bool) -> None:
        ...

    def unown(self) -> None:
        ...  # added by ExitableWithAliases('unown')


class RequestNameMixin:
    def request_name(self,
                     name: str,
                     allow_replacement: bool = True,
                     replace: bool = False) -> NameOwner:
        ...
