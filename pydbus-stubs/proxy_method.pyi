from typing import Any
from ._inspect3 import Signature

put_signature_in_doc: bool


class DBUSSignature(Signature):
    ...


class ProxyMethod:
    __signature__: DBUSSignature

    def __init__(self, iface_name: str, method: str) -> None:
        ...

    def __call__(self, instance: Any, *args: Any, **kwargs: Any) -> Any:
        ...

    def __get__(self, instance: Any, owner: Any) -> Any:
        ...
