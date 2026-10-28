# pv_headers #

* 📖[kamailio.cfg::module::pv_headers.html](https://kamailio.org/docs/modules/devel/modules/pv_headers.html)

Exported functions:

* [KSR.pv_headers.pvh_append_header\(\)](#ksrpv_headerspvh_append_header)
* [KSR.pv_headers.pvh_apply_headers\(\)](#ksrpv_headerspvh_apply_headers)
* [KSR.pv_headers.pvh_check_header\(\)](#ksrpv_headerspvh_check_header)
* [KSR.pv_headers.pvh_collect_headers\(\)](#ksrpv_headerspvh_collect_headers)
* [KSR.pv_headers.pvh_header_param_exists\(\)](#ksrpv_headerspvh_header_param_exists)
* [KSR.pv_headers.pvh_modify_header\(\)](#ksrpv_headerspvh_modify_header)
* [KSR.pv_headers.pvh_remove_header\(\)](#ksrpv_headerspvh_remove_header)
* [KSR.pv_headers.pvh_remove_header_param\(\)](#ksrpv_headerspvh_remove_header_param)
* [KSR.pv_headers.pvh_reset_headers\(\)](#ksrpv_headerspvh_reset_headers)

## KSR.pv_headers.pvh_append_header ##

```cpp
int KSR.pv_headers.pvh_append_header(str "hname", str "hvalue");
```

* 📖[kamailio.cfg::function::pvh_append_header\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_append_header)

## KSR.pv_headers.pvh_apply_headers ##

```cpp
int KSR.pv_headers.pvh_apply_headers();
```

* 📖[kamailio.cfg::function::pvh_apply_headers\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_apply_headers)

## KSR.pv_headers.pvh_check_header ##

```cpp
int KSR.pv_headers.pvh_check_header(str "hname");
```

* 📖[kamailio.cfg::function::pvh_check_header\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_check_header)

## KSR.pv_headers.pvh_collect_headers ##

```cpp
int KSR.pv_headers.pvh_collect_headers();
```

* 📖[kamailio.cfg::function::pvh_collect_headers\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_collect_headers)

## KSR.pv_headers.pvh_header_param_exists ##

```cpp
int KSR.pv_headers.pvh_header_param_exists(str "hname", str "hvalue");
```

* 📖[kamailio.cfg::function::pvh_header_param_exists\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_header_param_exists)

## KSR.pv_headers.pvh_modify_header ##

```cpp
int KSR.pv_headers.pvh_modify_header(str "hname", str "hvalue", int indx);
```

* 📖[kamailio.cfg::function::pvh_modify_header\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_modify_header)

## KSR.pv_headers.pvh_remove_header ##

```cpp
int KSR.pv_headers.pvh_remove_header(str "hname", int indx);
```

* 📖[kamailio.cfg::function::pvh_remove_header\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_remove_header)

## KSR.pv_headers.pvh_remove_header_param ##

```cpp
int KSR.pv_headers.pvh_remove_header_param(str "hname", str "toRemove");
```

* 📖[kamailio.cfg::function::pvh_remove_header_param\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_remove_header_param)

## KSR.pv_headers.pvh_reset_headers ##

```cpp
int KSR.pv_headers.pvh_reset_headers();
```

* 📖[kamailio.cfg::function::pvh_reset_headers\(\)](https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_reset_headers)
