from typing import Any
from collections.abc import Callable
from xml.etree.ElementTree import Element

from typing_extensions import Self

from .generic import bound_signal


class ProxySignal:
    def __init__(self, iface_name: str, signal: Element) -> None:
        ...

    def connect(self, object: Any, callback: Callable[..., Any]) -> Any:
        ...

    def __get__(self, instance: Any, owner: Any) -> bound_signal | Self:
        ...

    def __set__(self, instance: Any, value: Any) -> None:
        ...


class OnSignal:
    signal: ProxySignal

    def __init__(self, signal: ProxySignal) -> None:
        ...

    def __get__(self, instance: Any, owner: Any) -> Any:
        ...

    def __set__(self, instance: Any, value: Any) -> None:
        ...
