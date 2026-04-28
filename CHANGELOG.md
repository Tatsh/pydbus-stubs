<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.1/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Ported semantic differences from the typeshed `pydbus` stubs
(<https://github.com/python/typeshed/tree/main/stubs/pydbus>).

### Added

- New `_OrgBluezNetwork1Dict` `TypedDict` covering `org.bluez.Network1` properties.
- `bound_signal.__self__: _T` attribute, matching GObject signal binding.

### Changed

- Loosened callback parameter return types from `Callable[..., None]` to `Callable[..., object]` in
  the `bus_names`, `subscription`, and `proxy_signal` modules, so handlers that return any value are
  accepted.
- `pydbus.identifier.isident(s)` parameter is now positional-only (`isident(s, /)`).
- Moved the `Bus.get()` overloads onto `ProxyMixin.get()`. `Bus` no longer overrides `get`;
  downstream typing behaviour for `Bus(...).get(...)` is unchanged because `Bus` inherits
  `ProxyMixin.get()`.

### Fixed

- Corrected the variadic `*objects` parameter type on `Publication.__init__` and
  `PublicationMixin.publish`, which was incorrectly wrapped in `Iterable[...]`. The variadic now
  accepts the tuple/string union directly, matching pydbus's actual runtime behaviour.
- Corrected the `pydbus.exitable.ExitableWithAliases(*exit_methods)` parameter type from
  `Iterable[str]` to `str`.

### Removed

- `Variant` is no longer re-exported from `pydbus` (`__init__.pyi`); consumers must import it from
  `gi.repository.GLib`.
- Renamed the following classes with a leading underscore and marked them `@type_check_only`,
  effectively making them private (they remain available structurally but should not be referenced
  by name):
  - `CompositeObject` to `_CompositeObject`.
  - `interface` to `_interface`.
  - `OrgBluez` to `_OrgBluez`.
  - `OrgFreedesktopNotifications` to `_OrgFreedesktopNotifications`.
  - `OrgFreedesktopDBusObjectManager` to `_OrgFreedesktopDBusObjectManager`.
  - `DBusOrgFreedesktopDBus` to `_DBusOrgFreedesktopDBus`.
  - `DBusOrgFreedesktopPolicyKit1Authority` to `_DBusOrgFreedesktopPolicyKit1Authority`.
  - All `OrgBluez*1Dict` `TypedDict`s (`Adapter1`, `Battery1`, `Device1`, `GattCharacteristic1`,
    `GattDescriptor1`, `GattService1`, `Input1`, `LEAdvertisingManager1`, `Media1`, and
    `MediaControl1`) to their leading-underscore variants.
  - `OrgBluezDict` to `_OrgBluezDict`.

## [0.0.1] - 2025-00-00

First version.

[unreleased]: https://github.com/Tatsh/pydbus-stubs/compare/v0.0.3...HEAD
[0.0.1]: https://github.com/Tatsh/pydbus-stubs/releases/tag/v0.0.1
