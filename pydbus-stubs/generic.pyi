from typing import Any, Callable
from typing_extensions import Self
import types


class subscription:
    callback_list: list[Callable[..., Any]]
    callback: Callable[..., Any]

    def __init__(self, callback_list: list[Callable[..., Any]], callback: Callable[...,
                                                                                   Any]) -> None:
        ...

    def unsubscribe(self) -> None:
        ...

    def disconnect(self) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None,
                 traceback: types.TracebackType | None) -> None:
        ...


class bound_signal:
    __signal__: signal

    def __init__(self, signal: signal, instance: Any) -> None:
        ...

    @property
    def callbacks(self) -> list[Callable[..., Any]]:
        ...

    def connect(self, callback: Callable[..., Any]) -> subscription:
        ...

    def emit(self, *args: Any) -> None:
        ...

    def __call__(self, *args: Any) -> None:
        ...


class signal:
    map: dict[Any, Any]

    def __init__(self) -> None:
        ...

    def connect(self, object: Any, callback: Callable[..., Any]) -> subscription:
        ...

    def emit(self, object: Any, *args: Any) -> None:
        ...

    def __get__(self, instance: Any, owner: Any) -> Self | bound_signal:
        ...

    def __set__(self, instance: Any, value: Any) -> None:
        ...


bound_method: Any  # type[Callable[..., None]]
