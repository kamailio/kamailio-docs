# lcr #

* 📖[kamailio.cfg::module::lcr.html](https://kamailio.org/docs/modules/devel/modules/lcr.html)

Exported functions:

* [KSR.lcr.defunct_gw\(\)](#ksrlcrdefunct_gw)
* [KSR.lcr.from_any_gw\(\)](#ksrlcrfrom_any_gw)
* [KSR.lcr.from_any_gw_addr\(\)](#ksrlcrfrom_any_gw_addr)
* [KSR.lcr.from_any_gw_addr_port\(\)](#ksrlcrfrom_any_gw_addr_port)
* [KSR.lcr.from_gw\(\)](#ksrlcrfrom_gw)
* [KSR.lcr.from_gw_addr\(\)](#ksrlcrfrom_gw_addr)
* [KSR.lcr.from_gw_addr_port\(\)](#ksrlcrfrom_gw_addr_port)
* [KSR.lcr.inactivate_gw\(\)](#ksrlcrinactivate_gw)
* [KSR.lcr.load_gws\(\)](#ksrlcrload_gws)
* [KSR.lcr.load_gws_furi\(\)](#ksrlcrload_gws_furi)
* [KSR.lcr.load_gws_ruser\(\)](#ksrlcrload_gws_ruser)
* [KSR.lcr.next_gw\(\)](#ksrlcrnext_gw)
* [KSR.lcr.to_any_gw\(\)](#ksrlcrto_any_gw)
* [KSR.lcr.to_any_gw_addr\(\)](#ksrlcrto_any_gw_addr)
* [KSR.lcr.to_gw\(\)](#ksrlcrto_gw)
* [KSR.lcr.to_gw_addr\(\)](#ksrlcrto_gw_addr)

## KSR.lcr.defunct_gw ##

```cpp
int KSR.lcr.defunct_gw(int defunct_period);
```

* 📖[kamailio.cfg::function::defunct_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.defunct_gw)

## KSR.lcr.from_any_gw ##

```cpp
int KSR.lcr.from_any_gw();
```

* 📖[kamailio.cfg::function::from_any_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw)

## KSR.lcr.from_any_gw_addr ##

```cpp
int KSR.lcr.from_any_gw_addr(str "addr_str", int transport);
```

* 📖[kamailio.cfg::function::from_any_gw_addr\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr)

## KSR.lcr.from_any_gw_addr_port ##

```cpp
int KSR.lcr.from_any_gw_addr_port(str "addr_str", int transport, int src_port);
```

* 📖[kamailio.cfg::function::from_any_gw_addr_port\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr_port)

## KSR.lcr.from_gw ##

```cpp
int KSR.lcr.from_gw(int lcr_id);
```

* 📖[kamailio.cfg::function::from_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw)

## KSR.lcr.from_gw_addr ##

```cpp
int KSR.lcr.from_gw_addr(int lcr_id, str "addr_str", int transport);
```

* 📖[kamailio.cfg::function::from_gw_addr\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr)

## KSR.lcr.from_gw_addr_port ##

```cpp
int KSR.lcr.from_gw_addr_port(int lcr_id, str "addr_str", int transport, int src_port);
```

* 📖[kamailio.cfg::function::from_gw_addr_port\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr_port)

## KSR.lcr.inactivate_gw ##

```cpp
int KSR.lcr.inactivate_gw();
```

* 📖[kamailio.cfg::function::inactivate_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.inactivate_gw)

## KSR.lcr.load_gws ##

```cpp
int KSR.lcr.load_gws(int lcr_id);
```

* 📖[kamailio.cfg::function::load_gws\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws)

## KSR.lcr.load_gws_furi ##

```cpp
int KSR.lcr.load_gws_furi(int lcr_id, str "ruri_user", str "from_uri");
```

* 📖[kamailio.cfg::function::load_gws_furi\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_furi)

## KSR.lcr.load_gws_ruser ##

```cpp
int KSR.lcr.load_gws_ruser(int lcr_id, str "ruri_user");
```

* 📖[kamailio.cfg::function::load_gws_ruser\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_ruser)

## KSR.lcr.next_gw ##

```cpp
int KSR.lcr.next_gw();
```

* 📖[kamailio.cfg::function::next_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.next_gw)

## KSR.lcr.to_any_gw ##

```cpp
int KSR.lcr.to_any_gw();
```

* 📖[kamailio.cfg::function::to_any_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw)

## KSR.lcr.to_any_gw_addr ##

```cpp
int KSR.lcr.to_any_gw_addr(str "addr_str", int transport);
```

* 📖[kamailio.cfg::function::to_any_gw_addr\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw_addr)

## KSR.lcr.to_gw ##

```cpp
int KSR.lcr.to_gw(int lcr_id);
```

* 📖[kamailio.cfg::function::to_gw\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw)

## KSR.lcr.to_gw_addr ##

```cpp
int KSR.lcr.to_gw_addr(int lcr_id, str "addr_str", int transport);
```

* 📖[kamailio.cfg::function::to_gw_addr\(\)](https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw_addr)
