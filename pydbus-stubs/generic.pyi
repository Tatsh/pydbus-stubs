import types
from _typeshed import Unused
from collections.abc import Callable
from typing import Generic, TypeVar, overload
from typing_extensions import Self


class subscription:
    callback_list: list[Callable[..., object]]
    callback: Callable[..., object]

    def __init__(self, callback_list: list[Callable[..., object]],
                 callback: Callable[..., object]) -> None:
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


_T = TypeVar('_T')


class bound_signal(Generic[_T]):
    __signal__: signal[_T]

    def __init__(self, signal: signal[_T], instance: _T) -> None:
        ...

    @property
    def callbacks(self) -> list[Callable[..., object]]:
        ...

    def connect(self, callback: Callable[..., object]) -> subscription:
        ...

    def emit(self, *args: object) -> None:
        ...

    def __call__(self, *args: object) -> None:
        ...


class signal(Generic[_T]):
    map: dict[object, Callable[..., object]]

    def __init__(self) -> None:
        ...

    def connect(self, object: str, callback: Callable[..., object]) -> subscription:
        ...

    def emit(self, object: str, *args: object) -> None:
        ...

    @overload
    def __get__(self, instance: None, owner: Unused) -> Self:
        ...

    @overload
    def __get__(self, instance: _T, owner: Unused) -> bound_signal[_T]:
        ...

    def __set__(self, instance: Unused, value: Unused) -> None:
        ...  # Always raises


bound_method: Callable[..., None]  # type(signal().emit)
