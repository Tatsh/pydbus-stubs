from typing import Any
from collections.abc import Sequence
from xml.etree.ElementTree import Element

from gi.repository import GLib, Gio

from .bus import Bus
from .generic import signal
from .exitable import Exitable
from functools import partial as partial


class ObjectWrapper(Exitable):
    object: Any
    outargs: dict[str, Any]
    readable_properties: dict[str, Any]
    writable_properties: dict[str, Any]

    def __init__(self, object: Any, interfaces: Element) -> None:
        ...

    SignalEmitted: signal

    def call_method(self, connection: Gio.DBusConnection, sender: Any, object_path: Any,
                    interface_name: str, method_name: str, parameters: Any,
                    invocation: Gio.DBusMethodInvocation) -> None:
        ...

    def Get(self, interface_name: str, property_name: str) -> GLib.Variant:
        ...

    def GetAll(self, interface_name: str) -> dict[str, GLib.Variant]:
        ...

    def Set(self, interface_name: str, property_name: str, value: Any) -> None:
        ...

    def unwrap(self, *args: Any, **kwargs: Any) -> None:
        ...


class ObjectRegistration(Exitable):
    def __init__(self,
                 bus: Bus,
                 path: str,
                 interfaces: Element,
                 wrapper: Any,
                 own_wrapper: bool = ...) -> None:
        ...

    def unregister(self, *args: Any, **kwargs: Any) -> None:
        ...


class RegistrationMixin:
    def register_object(self, path: str, object: Any,
                        node_info: Sequence[str]) -> ObjectRegistration:
        ...
