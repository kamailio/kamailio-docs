# enum #

* 📖[kamailio.cfg::module::enum.html](https://kamailio.org/docs/modules/devel/modules/enum.html)

Exported functions:

* [KSR.enum.enum_i_query_suffix\(\)](#ksrenumenum_i_query_suffix)
* [KSR.enum.enum_pv_query\(\)](#ksrenumenum_pv_query)
* [KSR.enum.enum_pv_query_suffix\(\)](#ksrenumenum_pv_query_suffix)
* [KSR.enum.enum_pv_query_suffix_service\(\)](#ksrenumenum_pv_query_suffix_service)
* [KSR.enum.enum_query\(\)](#ksrenumenum_query)
* [KSR.enum.enum_query_suffix\(\)](#ksrenumenum_query_suffix)
* [KSR.enum.enum_query_suffix_service\(\)](#ksrenumenum_query_suffix_service)
* [KSR.enum.i_enum_query\(\)](#ksrenumi_enum_query)
* [KSR.enum.i_enum_query_suffix_service\(\)](#ksrenumi_enum_query_suffix_service)
* [KSR.enum.is_from_user_enum\(\)](#ksrenumis_from_user_enum)
* [KSR.enum.is_from_user_enum_suffix\(\)](#ksrenumis_from_user_enum_suffix)
* [KSR.enum.is_from_user_enum_suffix_service\(\)](#ksrenumis_from_user_enum_suffix_service)

## KSR.enum.enum_i_query_suffix ##

```cpp
int KSR.enum.enum_i_query_suffix(str "vsuffix");
```

* 📖[kamailio.cfg::function::enum_i_query_suffix\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_i_query_suffix)

## KSR.enum.enum_pv_query ##

```cpp
int KSR.enum.enum_pv_query(str "ve164");
```

* 📖[kamailio.cfg::function::enum_pv_query\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query)

## KSR.enum.enum_pv_query_suffix ##

```cpp
int KSR.enum.enum_pv_query_suffix(str "ve164", str "vsuffix");
```

* 📖[kamailio.cfg::function::enum_pv_query_suffix\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix)

## KSR.enum.enum_pv_query_suffix_service ##

```cpp
int KSR.enum.enum_pv_query_suffix_service(str "ve164", str "vsuffix", str "vservice");
```

* 📖[kamailio.cfg::function::enum_pv_query_suffix_service\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix_service)

## KSR.enum.enum_query ##

```cpp
int KSR.enum.enum_query();
```

* 📖[kamailio.cfg::function::enum_query\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query)

## KSR.enum.enum_query_suffix ##

```cpp
int KSR.enum.enum_query_suffix(str "vsuffix");
```

* 📖[kamailio.cfg::function::enum_query_suffix\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix)

## KSR.enum.enum_query_suffix_service ##

```cpp
int KSR.enum.enum_query_suffix_service(str "vsuffix", str "vservice");
```

* 📖[kamailio.cfg::function::enum_query_suffix_service\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix_service)

## KSR.enum.i_enum_query ##

```cpp
int KSR.enum.i_enum_query();
```

* 📖[kamailio.cfg::function::i_enum_query\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query)

## KSR.enum.i_enum_query_suffix_service ##

```cpp
int KSR.enum.i_enum_query_suffix_service(str "vsuffix", str "vservice");
```

* 📖[kamailio.cfg::function::i_enum_query_suffix_service\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query_suffix_service)

## KSR.enum.is_from_user_enum ##

```cpp
int KSR.enum.is_from_user_enum();
```

* 📖[kamailio.cfg::function::is_from_user_enum\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum)

## KSR.enum.is_from_user_enum_suffix ##

```cpp
int KSR.enum.is_from_user_enum_suffix(str "vsuffix");
```

* 📖[kamailio.cfg::function::is_from_user_enum_suffix\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix)

## KSR.enum.is_from_user_enum_suffix_service ##

```cpp
int KSR.enum.is_from_user_enum_suffix_service(str "vsuffix", str "vservice");
```

* 📖[kamailio.cfg::function::is_from_user_enum_suffix_service\(\)](https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix_service)
