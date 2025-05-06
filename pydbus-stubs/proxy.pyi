from typing import Generic, TypeVar
from typing_extensions import Self
from xml.etree.ElementTree import Element

from .bus import Bus


class ProxyMixin:
    def get(self,
            bus_name: str,
            object_path: str | None = None,
            *,
            timeout: int | None = None) -> CompositeObject:
        ...


_T = TypeVar('_T')


class ProxyObject(Generic[_T]):
    def __init__(self, bus: Bus, bus_name: str, path: str, object: Self | None = None) -> None:
        ...

    def __getattr__(self, name: str) -> _T:
        ...

    def __setattr__(self, name: str, value: _T) -> None:
        ...


class CompositeObject(ProxyObject[_T]):  # Inside CompositeInterface
    def __getitem__(self, iface: str) -> ProxyObject[_T]:
        ...


class interface(ProxyObject[_T]):  # inside Interface
    @staticmethod
    def _Introspect() -> None:
        ...


def Interface(iface: Element) -> interface[object]:
    ...


def CompositeInterface(introspection: Element) -> CompositeObject[object]:
    ...
