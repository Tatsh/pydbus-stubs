from collections.abc import Iterable

from .bus import Bus
from .exitable import Exitable


class Publication(Exitable):
    def __init__(
        self,
        bus: Bus,
        bus_name: str,
        *objects: Iterable[tuple[str, str, str | list[str] | tuple[str, ...]] | tuple[str, str]
                           | tuple[str] | str],
        allow_replacement: bool = True,
        replace: bool = False,
    ) -> None:
        ...

    def unpublish(self) -> None:
        ...  # added by ExitableWithAliases('unpublish')


class PublicationMixin:
    def publish(
        self,
        bus_name: str,
        *objects: Iterable[tuple[str, str, str | list[str] | tuple[str, ...]] | tuple[str, str]
                           | tuple[str] | str],
    ) -> Publication:
        ...
