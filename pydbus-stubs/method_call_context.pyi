from typing import Any, NamedTuple

from gi.repository import Gio

from .bus import Bus


class AuthorizationResult(NamedTuple):
    is_authorized: bool
    is_challenge: bool
    details: Any


class MethodCallContext:
    def __init__(self, gdbus_method_invocation: Gio.DBusMethodInvocation) -> None:
        ...

    @property
    def bus(self) -> Bus:
        ...

    @property
    def sender(self) -> Any:
        ...

    @property
    def object_path(self) -> str:
        ...

    @property
    def interface_name(self) -> str:
        ...

    @property
    def method_name(self) -> str:
        ...

    def check_authorization(self,
                            action_id: str,
                            details: Any,
                            interactive: bool = ...) -> AuthorizationResult:
        ...

    def is_authorized(self, action_id: str, details: Any, interactive: bool = ...) -> bool:
        ...
