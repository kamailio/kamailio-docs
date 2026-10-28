# rr #

* 📖[kamailio.cfg::module::rr.html](https://kamailio.org/docs/modules/devel/modules/rr.html)

Exported functions:

* [KSR.rr.add_rr_param\(\)](#ksrrradd_rr_param)
* [KSR.rr.check_route_param\(\)](#ksrrrcheck_route_param)
* [KSR.rr.cookie_add\(\)](#ksrrrcookie_add)
* [KSR.rr.cookie_check\(\)](#ksrrrcookie_check)
* [KSR.rr.cookie_flfetch\(\)](#ksrrrcookie_flfetch)
* [KSR.rr.cookie_flinit\(\)](#ksrrrcookie_flinit)
* [KSR.rr.cookie_flisset\(\)](#ksrrrcookie_flisset)
* [KSR.rr.cookie_flreset\(\)](#ksrrrcookie_flreset)
* [KSR.rr.cookie_flset\(\)](#ksrrrcookie_flset)
* [KSR.rr.is_direction\(\)](#ksrrris_direction)
* [KSR.rr.loose_route\(\)](#ksrrrloose_route)
* [KSR.rr.loose_route_mode\(\)](#ksrrrloose_route_mode)
* [KSR.rr.loose_route_preloaded\(\)](#ksrrrloose_route_preloaded)
* [KSR.rr.next_hop_route\(\)](#ksrrrnext_hop_route)
* [KSR.rr.record_route\(\)](#ksrrrrecord_route)
* [KSR.rr.record_route_advertised_address\(\)](#ksrrrrecord_route_advertised_address)
* [KSR.rr.record_route_params\(\)](#ksrrrrecord_route_params)
* [KSR.rr.record_route_preset\(\)](#ksrrrrecord_route_preset)
* [KSR.rr.record_route_preset_one\(\)](#ksrrrrecord_route_preset_one)
* [KSR.rr.remove_record_route\(\)](#ksrrrremove_record_route)

## KSR.rr.add_rr_param ##

```cpp
int KSR.rr.add_rr_param(str "sparam");
```

* 📖[kamailio.cfg::function::add_rr_param\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.add_rr_param)

## KSR.rr.check_route_param ##

```cpp
int KSR.rr.check_route_param(str "sre");
```

* 📖[kamailio.cfg::function::check_route_param\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.check_route_param)

## KSR.rr.cookie_add ##

```cpp
int KSR.rr.cookie_add(str "name", str "sval");
```

* 📖[kamailio.cfg::function::cookie_add\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_add)

## KSR.rr.cookie_check ##

```cpp
int KSR.rr.cookie_check(str "name", str "sval", int tdiff);
```

* 📖[kamailio.cfg::function::cookie_check\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_check)

## KSR.rr.cookie_flfetch ##

```cpp
int KSR.rr.cookie_flfetch(str "name");
```

* 📖[kamailio.cfg::function::cookie_flfetch\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_flfetch)

## KSR.rr.cookie_flinit ##

```cpp
int KSR.rr.cookie_flinit(int ival);
```

* 📖[kamailio.cfg::function::cookie_flinit\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_flinit)

## KSR.rr.cookie_flisset ##

```cpp
int KSR.rr.cookie_flisset(int idx);
```

* 📖[kamailio.cfg::function::cookie_flisset\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_flisset)

## KSR.rr.cookie_flreset ##

```cpp
int KSR.rr.cookie_flreset(int idx);
```

* 📖[kamailio.cfg::function::cookie_flreset\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_flreset)

## KSR.rr.cookie_flset ##

```cpp
int KSR.rr.cookie_flset(int idx);
```

* 📖[kamailio.cfg::function::cookie_flset\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.cookie_flset)

## KSR.rr.is_direction ##

```cpp
int KSR.rr.is_direction(str "dir");
```

* 📖[kamailio.cfg::function::is_direction\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.is_direction)

## KSR.rr.loose_route ##

```cpp
int KSR.rr.loose_route();
```

* 📖[kamailio.cfg::function::loose_route\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route)

## KSR.rr.loose_route_mode ##

```cpp
int KSR.rr.loose_route_mode(int vmode);
```

* 📖[kamailio.cfg::function::loose_route_mode\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_mode)

## KSR.rr.loose_route_preloaded ##

```cpp
int KSR.rr.loose_route_preloaded();
```

* 📖[kamailio.cfg::function::loose_route_preloaded\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_preloaded)

## KSR.rr.next_hop_route ##

```cpp
int KSR.rr.next_hop_route();
```

* 📖[kamailio.cfg::function::next_hop_route\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.next_hop_route)

## KSR.rr.record_route ##

```cpp
int KSR.rr.record_route();
```

* 📖[kamailio.cfg::function::record_route\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route)

## KSR.rr.record_route_advertised_address ##

```cpp
int KSR.rr.record_route_advertised_address(str "addr");
```

* 📖[kamailio.cfg::function::record_route_advertised_address\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_advertised_address)

## KSR.rr.record_route_params ##

```cpp
int KSR.rr.record_route_params(str "sparams");
```

* 📖[kamailio.cfg::function::record_route_params\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_params)

## KSR.rr.record_route_preset ##

```cpp
int KSR.rr.record_route_preset(str "addr1", str "addr2");
```

* 📖[kamailio.cfg::function::record_route_preset\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset)

## KSR.rr.record_route_preset_one ##

```cpp
int KSR.rr.record_route_preset_one(str "addr1");
```

* 📖[kamailio.cfg::function::record_route_preset_one\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset_one)

## KSR.rr.remove_record_route ##

```cpp
int KSR.rr.remove_record_route();
```

* 📖[kamailio.cfg::function::remove_record_route\(\)](https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.remove_record_route)
