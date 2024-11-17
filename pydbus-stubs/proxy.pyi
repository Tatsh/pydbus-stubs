from typing import Any
from xml.etree.ElementTree import Element

from .bus import Bus
from .proxy_property import ProxyProperty as ProxyProperty
from .proxy_signal import OnSignal as OnSignal, ProxySignal as ProxySignal
from .timeout import timeout_to_glib as timeout_to_glib


class CompositeObject:  # inside CompositeInterface
    def __getitem__(self, iface: str) -> Any:
        ...


class ProxyMixin:
    def get(self, bus_name: str, object_path: str | None = None, **kwargs: Any) -> CompositeObject:
        ...


class ProxyObject:
    def __init__(self, bus: Bus, bus_name: str, path: str, object: Any = None) -> None:
        ...


def Interface(iface: Element) -> Any:
    ...


def CompositeInterface(introspection: Element) -> CompositeObject:
    ...
