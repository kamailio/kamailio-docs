# misc_radius #

* 📖[kamailio.cfg::module::misc_radius.html](https://kamailio.org/docs/modules/devel/modules/misc_radius.html)

Exported functions:

* [KSR.misc_radius.does_uri_exist\(\)](#ksrmisc_radiusdoes_uri_exist)
* [KSR.misc_radius.does_uri_exist_uval\(\)](#ksrmisc_radiusdoes_uri_exist_uval)
* [KSR.misc_radius.does_uri_user_exist\(\)](#ksrmisc_radiusdoes_uri_user_exist)
* [KSR.misc_radius.does_uri_user_exist_uval\(\)](#ksrmisc_radiusdoes_uri_user_exist_uval)
* [KSR.misc_radius.is_user_in\(\)](#ksrmisc_radiusis_user_in)
* [KSR.misc_radius.load_callee_avps\(\)](#ksrmisc_radiusload_callee_avps)
* [KSR.misc_radius.load_caller_avps\(\)](#ksrmisc_radiusload_caller_avps)

## KSR.misc_radius.does_uri_exist ##

```cpp
int KSR.misc_radius.does_uri_exist();
```

* 📖[kamailio.cfg::function::does_uri_exist\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist)

## KSR.misc_radius.does_uri_exist_uval ##

```cpp
int KSR.misc_radius.does_uri_exist_uval(str "suri");
```

* 📖[kamailio.cfg::function::does_uri_exist_uval\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist_uval)

## KSR.misc_radius.does_uri_user_exist ##

```cpp
int KSR.misc_radius.does_uri_user_exist();
```

* 📖[kamailio.cfg::function::does_uri_user_exist\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist)

## KSR.misc_radius.does_uri_user_exist_uval ##

```cpp
int KSR.misc_radius.does_uri_user_exist_uval(str "user");
```

* 📖[kamailio.cfg::function::does_uri_user_exist_uval\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist_uval)

## KSR.misc_radius.is_user_in ##

```cpp
int KSR.misc_radius.is_user_in(str "user", str "group");
```

* 📖[kamailio.cfg::function::is_user_in\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.is_user_in)

## KSR.misc_radius.load_callee_avps ##

```cpp
int KSR.misc_radius.load_callee_avps(str "user");
```

* 📖[kamailio.cfg::function::load_callee_avps\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_callee_avps)

## KSR.misc_radius.load_caller_avps ##

```cpp
int KSR.misc_radius.load_caller_avps(str "user");
```

* 📖[kamailio.cfg::function::load_caller_avps\(\)](https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_caller_avps)
