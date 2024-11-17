from typing import Any
from xml.etree.ElementTree import Element


class ProxyProperty:
    def __init__(self, iface_name: str, property: Element) -> None:
        ...

    def __get__(self, instance: Any, owner: Any) -> Any:
        ...

    def __set__(self, instance: Any, value: Any) -> None:
        ...
