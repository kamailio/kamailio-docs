# uac #

* 📖[kamailio.cfg::module::uac.html](https://kamailio.org/docs/modules/devel/modules/uac.html)

Exported functions:

* [KSR.uac.uac_auth\(\)](#ksruacuac_auth)
* [KSR.uac.uac_auth_mode\(\)](#ksruacuac_auth_mode)
* [KSR.uac.uac_reg_disable\(\)](#ksruacuac_reg_disable)
* [KSR.uac.uac_reg_enable\(\)](#ksruacuac_reg_enable)
* [KSR.uac.uac_reg_lookup\(\)](#ksruacuac_reg_lookup)
* [KSR.uac.uac_reg_lookup_uri\(\)](#ksruacuac_reg_lookup_uri)
* [KSR.uac.uac_reg_refresh\(\)](#ksruacuac_reg_refresh)
* [KSR.uac.uac_reg_request_to\(\)](#ksruacuac_reg_request_to)
* [KSR.uac.uac_reg_status\(\)](#ksruacuac_reg_status)
* [KSR.uac.uac_replace_from\(\)](#ksruacuac_replace_from)
* [KSR.uac.uac_replace_from_uri\(\)](#ksruacuac_replace_from_uri)
* [KSR.uac.uac_replace_to\(\)](#ksruacuac_replace_to)
* [KSR.uac.uac_replace_to_uri\(\)](#ksruacuac_replace_to_uri)
* [KSR.uac.uac_req_send\(\)](#ksruacuac_req_send)
* [KSR.uac.uac_restore_from\(\)](#ksruacuac_restore_from)
* [KSR.uac.uac_restore_to\(\)](#ksruacuac_restore_to)

## KSR.uac.uac_auth ##

```cpp
int KSR.uac.uac_auth();
```

* 📖[kamailio.cfg::function::uac_auth\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth)

## KSR.uac.uac_auth_mode ##

```cpp
int KSR.uac.uac_auth_mode(int mode);
```

* 📖[kamailio.cfg::function::uac_auth_mode\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth_mode)

## KSR.uac.uac_reg_disable ##

```cpp
int KSR.uac.uac_reg_disable(str "attr", str "val");
```

* 📖[kamailio.cfg::function::uac_reg_disable\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_disable)

## KSR.uac.uac_reg_enable ##

```cpp
int KSR.uac.uac_reg_enable(str "attr", str "val");
```

* 📖[kamailio.cfg::function::uac_reg_enable\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_enable)

## KSR.uac.uac_reg_lookup ##

```cpp
int KSR.uac.uac_reg_lookup(str "userid", str "sdst");
```

* 📖[kamailio.cfg::function::uac_reg_lookup\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup)

## KSR.uac.uac_reg_lookup_uri ##

```cpp
int KSR.uac.uac_reg_lookup_uri(str "suri", str "sdst");
```

* 📖[kamailio.cfg::function::uac_reg_lookup_uri\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup_uri)

## KSR.uac.uac_reg_refresh ##

```cpp
int KSR.uac.uac_reg_refresh(str "l_uuid");
```

* 📖[kamailio.cfg::function::uac_reg_refresh\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_refresh)

## KSR.uac.uac_reg_request_to ##

```cpp
int KSR.uac.uac_reg_request_to(str "userid", int imode);
```

* 📖[kamailio.cfg::function::uac_reg_request_to\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_request_to)

## KSR.uac.uac_reg_status ##

```cpp
int KSR.uac.uac_reg_status(str "sruuid");
```

* 📖[kamailio.cfg::function::uac_reg_status\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_status)

## KSR.uac.uac_replace_from ##

```cpp
int KSR.uac.uac_replace_from(str "pdsp", str "puri");
```

* 📖[kamailio.cfg::function::uac_replace_from\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from)

## KSR.uac.uac_replace_from_uri ##

```cpp
int KSR.uac.uac_replace_from_uri(str "puri");
```

* 📖[kamailio.cfg::function::uac_replace_from_uri\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from_uri)

## KSR.uac.uac_replace_to ##

```cpp
int KSR.uac.uac_replace_to(str "pdsp", str "puri");
```

* 📖[kamailio.cfg::function::uac_replace_to\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to)

## KSR.uac.uac_replace_to_uri ##

```cpp
int KSR.uac.uac_replace_to_uri(str "puri");
```

* 📖[kamailio.cfg::function::uac_replace_to_uri\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to_uri)

## KSR.uac.uac_req_send ##

```cpp
int KSR.uac.uac_req_send();
```

* 📖[kamailio.cfg::function::uac_req_send\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_req_send)

## KSR.uac.uac_restore_from ##

```cpp
int KSR.uac.uac_restore_from();
```

* 📖[kamailio.cfg::function::uac_restore_from\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_from)

## KSR.uac.uac_restore_to ##

```cpp
int KSR.uac.uac_restore_to();
```

* 📖[kamailio.cfg::function::uac_restore_to\(\)](https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_to)
