from typing import Any, Callable

from gi.repository import Gio

from .exitable import Exitable


class NameOwner(Exitable):
    Flags: Gio.BusNameOwnerFlags

    def __init__(self, con: Gio.DBusConnection, name: str, flags: Gio.BusNameOwnerFlags,
                 name_aquired_handler: Callable[[str], Any],
                 name_lost_handler: Callable[[str], Any]) -> None:
        ...

    def unown(self, *args: Any, **kwargs: Any) -> None:
        ...


class NameWatcher(Exitable):
    Flags: Gio.BusNameWatcherFlags

    def __init__(self, con: Gio.DBusConnection, name: str, flags: Gio.BusNameWatcherFlags,
                 name_appeared_handler: Callable[[str], Any],
                 name_vanished_handler: Callable[[str], Any]) -> None:
        ...

    def unwatch(self, *args: Any, **kwargs: Any) -> None:
        ...


class OwnMixin:
    NameOwnerFlags: Gio.BusNameOwnerFlags

    def own_name(self,
                 name: str,
                 flags: Gio.BusNameOwnerFlags = ...,
                 name_aquired: Callable[[str], Any] | None = ...,
                 name_lost: Callable[[str], Any] | None = ...) -> NameOwner:
        ...

    def unwatch(self, *args: Any, **kwargs: Any) -> None:
        ...


class WatchMixin:
    NameWatcherFlags: Gio.BusNameWatcherFlags

    def watch_name(self,
                   name: str,
                   flags: Gio.BusNameWatcherFlags = ...,
                   name_appeared: Callable[[str], Any] | None = ...,
                   name_vanished: Callable[[str], Any] | None = ...) -> NameWatcher:
        ...
