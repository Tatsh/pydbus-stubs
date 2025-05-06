from xml.etree.ElementTree import Element

from gi.repository import Gio, GLib

from .bus import Bus
from .exitable import Exitable
from .generic import signal


class ObjectWrapper(Exitable):
    object: str
    outargs: dict[str, GLib.Variant]
    readable_properties: dict[str, GLib.Variant]
    writable_properties: dict[str, GLib.Variant]

    def __init__(self, object: str, interfaces: Element) -> None:
        ...

    SignalEmitted: signal

    def call_method(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant,
        invocation: Gio.DBusMethodInvocation,
    ) -> None:
        ...

    def Get(self, interface_name: str, property_name: str) -> GLib.Variant:
        ...

    def GetAll(self, interface_name: str) -> dict[str, GLib.Variant]:
        ...

    def Set(self, interface_name: str, property_name: str, value: GLib.Variant) -> None:
        ...

    def unwrap(self) -> None:
        ...  # added by ExitableWithAliases('unwrap')


class ObjectRegistration(Exitable):
    def __init__(self,
                 bus: Bus,
                 path: str,
                 interfaces: Element,
                 wrapper: ObjectWrapper,
                 own_wrapper: bool = False) -> None:
        ...

    def unregister(self) -> None:
        ...  # added by ExitableWithAliases('unregister')


class RegistrationMixin:
    def register_object(self, path: str, object: str,
                        node_info: str | list[str] | tuple[str, ...]) -> ObjectRegistration:
        ...
