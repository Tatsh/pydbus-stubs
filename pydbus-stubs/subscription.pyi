from typing import Any
from collections.abc import Callable
from .generic import signal
from .exitable import Exitable
from gi.repository import Gio


class Subscription(Exitable):
    Flags: Gio.DBusSignalFlags

    def __init__(self, con: Gio.DBusConnection, sender: str, iface: str, member: str | None,
                 object: str | None, arg0: str | None, flags: Gio.DBusSignalFlags,
                 callback: Callable[..., Any] | None) -> None:
        ...


class SubscriptionMixin:
    SubscriptionFlags: Gio.DBusSignalFlags

    def subscribe(
        self,
        sender: str | None = ...,
        iface: str | None = ...,
        signal: str | None = ...,
        object: str | None = ...,
        arg0: str | None = ...,
        flags: int = ...,
        signal_fired: Callable[[Any, Any, str, signal, Gio.DBusSignalFlags, Any], Any]
        | None = ...
    ) -> Subscription:
        ...
