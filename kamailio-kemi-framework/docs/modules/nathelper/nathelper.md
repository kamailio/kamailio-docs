# nathelper #

* 📖[kamailio.cfg::module::nathelper.html](https://kamailio.org/docs/modules/devel/modules/nathelper.html)

Exported functions:

* [KSR.nathelper.add_contact_alias\(\)](#ksrnathelperadd_contact_alias)
* [KSR.nathelper.add_contact_alias_addr\(\)](#ksrnathelperadd_contact_alias_addr)
* [KSR.nathelper.add_rcv_param\(\)](#ksrnathelperadd_rcv_param)
* [KSR.nathelper.fix_nated_contact\(\)](#ksrnathelperfix_nated_contact)
* [KSR.nathelper.fix_nated_register\(\)](#ksrnathelperfix_nated_register)
* [KSR.nathelper.fix_nated_sdp\(\)](#ksrnathelperfix_nated_sdp)
* [KSR.nathelper.fix_nated_sdp_ip\(\)](#ksrnathelperfix_nated_sdp_ip)
* [KSR.nathelper.handle_ruri_alias\(\)](#ksrnathelperhandle_ruri_alias)
* [KSR.nathelper.handle_ruri_alias_mode\(\)](#ksrnathelperhandle_ruri_alias_mode)
* [KSR.nathelper.is_rfc1918\(\)](#ksrnathelperis_rfc1918)
* [KSR.nathelper.nat_uac_test\(\)](#ksrnathelpernat_uac_test)
* [KSR.nathelper.set_alias_to_pv\(\)](#ksrnathelperset_alias_to_pv)
* [KSR.nathelper.set_contact_alias\(\)](#ksrnathelperset_contact_alias)
* [KSR.nathelper.set_contact_alias_trim\(\)](#ksrnathelperset_contact_alias_trim)

## KSR.nathelper.add_contact_alias ##

```cpp
int KSR.nathelper.add_contact_alias();
```

* 📖[kamailio.cfg::function::add_contact_alias\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias)

## KSR.nathelper.add_contact_alias_addr ##

```cpp
int KSR.nathelper.add_contact_alias_addr(str "ip_str", str "port_str", str "proto_str");
```

* 📖[kamailio.cfg::function::add_contact_alias_addr\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias_addr)

## KSR.nathelper.add_rcv_param ##

```cpp
int KSR.nathelper.add_rcv_param(int upos);
```

* 📖[kamailio.cfg::function::add_rcv_param\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_rcv_param)

## KSR.nathelper.fix_nated_contact ##

```cpp
int KSR.nathelper.fix_nated_contact();
```

* 📖[kamailio.cfg::function::fix_nated_contact\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_contact)

## KSR.nathelper.fix_nated_register ##

```cpp
int KSR.nathelper.fix_nated_register();
```

* 📖[kamailio.cfg::function::fix_nated_register\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_register)

## KSR.nathelper.fix_nated_sdp ##

```cpp
int KSR.nathelper.fix_nated_sdp(int level);
```

* 📖[kamailio.cfg::function::fix_nated_sdp\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp)

## KSR.nathelper.fix_nated_sdp_ip ##

```cpp
int KSR.nathelper.fix_nated_sdp_ip(int level, str "ip");
```

* 📖[kamailio.cfg::function::fix_nated_sdp_ip\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp_ip)

## KSR.nathelper.handle_ruri_alias ##

```cpp
int KSR.nathelper.handle_ruri_alias();
```

* 📖[kamailio.cfg::function::handle_ruri_alias\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias)

## KSR.nathelper.handle_ruri_alias_mode ##

```cpp
int KSR.nathelper.handle_ruri_alias_mode(int mode);
```

* 📖[kamailio.cfg::function::handle_ruri_alias_mode\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias_mode)

## KSR.nathelper.is_rfc1918 ##

```cpp
int KSR.nathelper.is_rfc1918(str "address");
```

* 📖[kamailio.cfg::function::is_rfc1918\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.is_rfc1918)

## KSR.nathelper.nat_uac_test ##

```cpp
int KSR.nathelper.nat_uac_test(int tests);
```

* 📖[kamailio.cfg::function::nat_uac_test\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.nat_uac_test)

## KSR.nathelper.set_alias_to_pv ##

```cpp
int KSR.nathelper.set_alias_to_pv(str "uri_avp");
```

* 📖[kamailio.cfg::function::set_alias_to_pv\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_alias_to_pv)

## KSR.nathelper.set_contact_alias ##

```cpp
int KSR.nathelper.set_contact_alias();
```

* 📖[kamailio.cfg::function::set_contact_alias\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias)

## KSR.nathelper.set_contact_alias_trim ##

```cpp
int KSR.nathelper.set_contact_alias_trim();
```

* 📖[kamailio.cfg::function::set_contact_alias_trim\(\)](https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias_trim)
