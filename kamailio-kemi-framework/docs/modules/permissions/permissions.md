# permissions #

* 📖[kamailio.cfg::module::permissions.html](https://kamailio.org/docs/modules/devel/modules/permissions.html)

Exported functions:

* [KSR.permissions.allow_address\(\)](#ksrpermissionsallow_address)
* [KSR.permissions.allow_address_group\(\)](#ksrpermissionsallow_address_group)
* [KSR.permissions.allow_source_address\(\)](#ksrpermissionsallow_source_address)
* [KSR.permissions.allow_source_address_group\(\)](#ksrpermissionsallow_source_address_group)
* [KSR.permissions.allow_trusted\(\)](#ksrpermissionsallow_trusted)

## KSR.permissions.allow_address ##

```cpp
int KSR.permissions.allow_address(int addr_group, str "ips", int port);
```

* 📖[kamailio.cfg::function::allow_address\(\)](https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address)

## KSR.permissions.allow_address_group ##

```cpp
int KSR.permissions.allow_address_group(str "_addr", int _port);
```

* 📖[kamailio.cfg::function::allow_address_group\(\)](https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address_group)

## KSR.permissions.allow_source_address ##

```cpp
int KSR.permissions.allow_source_address(int addr_group);
```

* 📖[kamailio.cfg::function::allow_source_address\(\)](https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address)

## KSR.permissions.allow_source_address_group ##

```cpp
int KSR.permissions.allow_source_address_group();
```

* 📖[kamailio.cfg::function::allow_source_address_group\(\)](https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address_group)

## KSR.permissions.allow_trusted ##

```cpp
int KSR.permissions.allow_trusted();
```

* 📖[kamailio.cfg::function::allow_trusted\(\)](https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_trusted)
