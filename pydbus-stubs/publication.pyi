from typing import Any

from .bus import Bus
from .exitable import Exitable
from gi.repository import Gio as Gio


class Publication(Exitable):
    def __init__(self, bus: Bus, bus_name: str, *objects: Any, **kwargs: Any) -> None:
        ...

    def unpublish(self, *args: Any, **kwargs: Any) -> None:
        ...


class PublicationMixin:
    def publish(self, bus_name: str, *objects: Any) -> Publication:
        ...
