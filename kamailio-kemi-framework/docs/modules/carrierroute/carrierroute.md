# carrierroute #

* 📖[kamailio.cfg::module::carrierroute.html](https://kamailio.org/docs/modules/devel/modules/carrierroute.html)

Exported functions:

* [KSR.carrierroute.cr_next_domain\(\)](#ksrcarrierroutecr_next_domain)
* [KSR.carrierroute.cr_nofallback_route\(\)](#ksrcarrierroutecr_nofallback_route)
* [KSR.carrierroute.cr_nofallback_route_info\(\)](#ksrcarrierroutecr_nofallback_route_info)
* [KSR.carrierroute.cr_route\(\)](#ksrcarrierroutecr_route)
* [KSR.carrierroute.cr_route_info\(\)](#ksrcarrierroutecr_route_info)
* [KSR.carrierroute.cr_user_carrier\(\)](#ksrcarrierroutecr_user_carrier)

## KSR.carrierroute.cr_next_domain ##

```cpp
int KSR.carrierroute.cr_next_domain(str "_carrier", str "_domain", str "_prefix_matching", str "_host", str "_reply_code", str "_dstavp");
```

* 📖[kamailio.cfg::function::cr_next_domain\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_next_domain)

## KSR.carrierroute.cr_nofallback_route ##

```cpp
int KSR.carrierroute.cr_nofallback_route(str "_carrier", str "_domain", str "_prefix_matching", str "_rewrite_user", str "_hsrc");
```

* 📖[kamailio.cfg::function::cr_nofallback_route\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_nofallback_route)

## KSR.carrierroute.cr_nofallback_route_info ##

```cpp
int KSR.carrierroute.cr_nofallback_route_info(str "_carrier", str "_domain", str "_prefix_matching", str "_rewrite_user", str "_hsrc", str "_dstvar");
```

* 📖[kamailio.cfg::function::cr_nofallback_route_info\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_nofallback_route_info)

## KSR.carrierroute.cr_route ##

```cpp
int KSR.carrierroute.cr_route(str "_carrier", str "_domain", str "_prefix_matching", str "_rewrite_user", str "_hsrc");
```

* 📖[kamailio.cfg::function::cr_route\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_route)

## KSR.carrierroute.cr_route_info ##

```cpp
int KSR.carrierroute.cr_route_info(str "_carrier", str "_domain", str "_prefix_matching", str "_rewrite_user", str "_hsrc", str "_dstvar");
```

* 📖[kamailio.cfg::function::cr_route_info\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_route_info)

## KSR.carrierroute.cr_user_carrier ##

```cpp
int KSR.carrierroute.cr_user_carrier(str "user", str "domain", str "dstvar");
```

* 📖[kamailio.cfg::function::cr_user_carrier\(\)](https://kamailio.org/docs/modules/devel/modules/carrierroute.html#carrierroute.f.cr_user_carrier)
