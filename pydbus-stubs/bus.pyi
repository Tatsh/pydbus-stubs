import types
from typing import Any, Literal, TypedDict

from gi.repository import Gio
from typing_extensions import Self, overload

from .bus_names import OwnMixin, WatchMixin
from .proxy import ProxyMixin
from .publication import PublicationMixin
from .registration import RegistrationMixin
from .request_name import RequestNameMixin
from .subscription import SubscriptionMixin


def bus_get(type: Gio.BusType) -> Bus:
    ...


def connect(address: str) -> Bus:
    ...


class DBusOrgFreedesktopDBus:
    # Incomplete DBUS.org.freedesktop.DBus
    Features: list[str]

    def GetId(self) -> str:
        ...


class DBusOrgFreedesktopPolicyKit1Authority:
    # Incomplete DBUS.org.freedesktop.PolicyKit1.Authority
    BackendName: str
    BackendVersion: str


OrgBluezDict = TypedDict(
    'OrgBluezDict', {
        'org.bluez.AgentManager1': dict[Any, Any],
        'org.bluez.ProfileManager1': dict[Any, Any],
        'org.freedesktop.DBus.Introspectable': dict[Any, Any]
    })
OrgBluesHci0Dict = TypedDict('OrgBluesHci0Dict', {'org.bluez.Adapter1': dict[str, Any]})

DBusOrgFreedesktopDBusObjectManagerManagedObjectsDict = TypedDict(
    'DBusOrgFreedesktopDBusObjectManagerManagedObjectsDict',  # noqa: PYI053
    {
        '/org/bluez': OrgBluezDict,
        '/org/bluez/hci0': OrgBluesHci0Dict
    })


class DBusOrgFreedesktopDBusObjectManager:
    x: int
    y: int

    @staticmethod
    def GetManagedObjects() -> dict[str, Any]:
        ...


class Bluez:
    def __getitem__(
            self, key: Literal['org.freedesktop.DBus.ObjectManager']
    ) -> DBusOrgFreedesktopDBusObjectManager:
        ...


class Notifications:
    Inhibited: bool

    def UnInhibit(self, key: int) -> int | None:
        ...

    def Inhibit(self, name: str, reason: str, unk1: Any) -> int | None:
        ...


class Bus(ProxyMixin, RequestNameMixin, OwnMixin, WatchMixin, SubscriptionMixin, RegistrationMixin,
          PublicationMixin):
    Type = Gio.BusType
    autoclose: bool
    con: Gio.DBusConnection

    def __init__(self, gio_con: Gio.DBusConnection) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None,
                 traceback: types.TracebackType | None) -> None:
        ...

    @property
    def dbus(self) -> DBusOrgFreedesktopDBus:
        ...

    @property
    def polkit_authority(self) -> DBusOrgFreedesktopPolicyKit1Authority:
        ...

    @overload  # type: ignore[override]
    def get(self, domain: Literal['org.freedesktop.Notifications'],
            path: Literal['/org/freedesktop/Notifications']) -> Notifications:
        ...

    @overload
    def get(self, domain: Literal['org.bluez'], path: Literal['/']) -> Bluez:
        ...

    @overload
    def get(self, domain: str, path: str) -> Any:
        ...


def SystemBus() -> Bus:
    ...


def SessionBus() -> Bus:
    ...
