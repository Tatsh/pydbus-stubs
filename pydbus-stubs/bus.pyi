import types
from typing import Any, Literal, TypedDict, overload
from typing_extensions import Self

from gi.repository import Gio

from .bus_names import OwnMixin, WatchMixin
from .generic import bound_signal
from .proxy import CompositeObject, ProxyMixin
from .publication import PublicationMixin
from .registration import RegistrationMixin
from .request_name import RequestNameMixin
from .subscription import SubscriptionMixin


def bus_get(type: Gio.BusType) -> Bus:
    ...


def connect(address: str) -> Bus:
    ...


class DBusOrgFreedesktopDBus:
    # Incomplete interface to org.freedesktop.DBus
    Features: list[str]

    def GetId(self) -> str:
        ...


class DBusOrgFreedesktopPolicyKit1Authority:
    # Incomplete interface to org.freedesktop.PolicyKit1.Authority
    BackendFeatures: int  # flags
    BackendName: str
    BackendVersion: str


class OrgBluezAdapter1Dict(TypedDict, total=False):
    Address: str
    AddressType: Literal['public', 'random']
    Alias: str
    Class: int
    Connectable: bool
    Discoverable: bool
    DiscoverableTimeout: int
    Discovering: bool
    Manufacturer: int
    Modalias: str
    Name: str
    Pairable: bool
    PairableTimeout: int
    Powered: bool
    Roles: list[str]
    UUIDs: list[str]
    Version: int


class OrgBluezDevice1Dict(TypedDict, total=False):
    Adapter: str
    Address: str
    AddressType: Literal['public', 'random']
    Alias: str
    Appearance: int
    Blocked: bool
    Bonded: bool
    Class: int
    Connected: bool
    Icon: str
    LegacyPairing: bool
    Modalias: str
    Name: str
    Paired: bool
    ServicesResolved: bool
    Trusted: bool
    UUIDs: list[str]
    WakeAllowed: bool


class OrgBluezInput1Dict(TypedDict, total=False):
    ReconnectMode: str


class OrgBluezMedia1Dict(TypedDict, total=False):
    SupportedUUIDs: list[str]


class OrgBluezMediaControl1Dict(TypedDict, total=False):
    Connected: bool


class OrgBluezBattery1Dict(TypedDict, total=False):
    Percentage: int
    Source: str


class OrgBluezGattService1Dict(TypedDict, total=False):
    Device: str
    Handle: int
    Includes: list[str]
    Primary: bool
    UUID: str


class OrgBluezGattCharacteristic1Dict(TypedDict, total=False):
    Flags: list[str]
    Handle: int
    MTU: int
    Service: str
    UUID: str
    Value: list[int]


class OrgBluezGattDescriptor1Dict(TypedDict, total=False):
    Characteristic: str
    Handle: int
    UUID: str
    Value: list[int]


class OrgBluezLEAdvertisingManager1Dict(TypedDict, total=False):
    ActiveInstances: int
    SupportedCapabilities: dict[str, int]  # e.g. MaxTxPower: 7
    SupportedFeatures: list[str]
    SupportedIncludes: list[str]
    SupportedInstances: int
    SupportedSecondaryChannels: list[str]


# This is for keys under /org/bluez/hci0/*
OrgBluezDict = TypedDict(
    'OrgBluezDict',
    {
        'org.bluez.Adapter1': OrgBluezAdapter1Dict,
        'org.bluez.Battery1': OrgBluezBattery1Dict,
        'org.bluez.Device1': OrgBluezDevice1Dict,
        'org.bluez.GattCharacteristic1': OrgBluezGattCharacteristic1Dict,
        'org.bluez.GattDescriptor1': OrgBluezGattDescriptor1Dict,
        'org.bluez.GattService1': OrgBluezGattService1Dict,
        'org.bluez.Input1': OrgBluezInput1Dict,
        'org.bluez.LEAdvertisingManager1': OrgBluezLEAdvertisingManager1Dict,
        'org.bluez.Media1': OrgBluezMedia1Dict,
        'org.bluez.MediaControl1': OrgBluezMediaControl1Dict,
        # The following always appear as empty dictionaries on my system.
        'org.bluez.AgentManager1': dict[str, Any],
        'org.bluez.BatteryProviderManager1': dict[str, Any],
        'org.bluez.NetworkServer1': dict[str, Any],
        'org.bluez.ProfileManager1': dict[str, Any],
        'org.freedesktop.DBus.Introspectable': dict[str, Any],
        'org.freedesktop.DBus.Properties': dict[str, Any],
    },
    total=False,
)


class OrgFreedesktopDBusObjectManager:
    @staticmethod
    def GetManagedObjects() -> dict[str, OrgBluezDict]:
        ...


class OrgBluez(CompositeObject):
    def __getitem__(
            self,
            key: Literal['org.freedesktop.DBus.ObjectManager']) -> OrgFreedesktopDBusObjectManager:
        ...  # type: ignore[override]


class OrgFreedesktopNotifications(CompositeObject):
    Inhibited: bool
    ActivationToken: bound_signal
    ActionInvoked: bound_signal
    NotificationClosed: bound_signal

    def CloseNotification(self, id: int) -> None:
        ...

    def GetCapabilities(self) -> list[str]:
        ...  # We could use Literal[] here but KDE also returns its own not in the spec.

    def GetServerInformation(self) -> tuple[str, str, str, str]:
        ...

    def Inhibit(self, name: str, reason: str, hints: dict[str,
                                                          bool | bytes | int | str]) -> int | None:
        ...

    def Notify(
        self,
        app_name: str,
        replaces_id: int,
        app_icon: str,
        summary: str,
        body: str,
        actions: list[str],
        hints: dict[
            str, bool | bytes | int
            | str],  # See https://specifications.freedesktop.org/notification-spec/1.3/hints.html
        expire_timeout: int,
    ) -> int:
        ...

    def UnInhibit(self, key: int) -> int | None:
        ...


class Bus(ProxyMixin, RequestNameMixin, OwnMixin, WatchMixin, SubscriptionMixin, RegistrationMixin,
          PublicationMixin):
    Type: type[Gio.BusType] = ...
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
    def get(self, domain: Literal['.Notifications']) -> OrgFreedesktopNotifications:
        ...

    @overload  # type: ignore[override]
    def get(self, domain: Literal['org.freedesktop.Notifications']) -> OrgFreedesktopNotifications:
        ...

    @overload
    def get(self, domain: Literal['org.bluez'], path: Literal['/']) -> OrgBluez:
        ...

    @overload
    def get(self, domain: str, path: str) -> Any:
        ...  # unpredictable return value.


def SystemBus() -> Bus:
    ...


def SessionBus() -> Bus:
    ...
