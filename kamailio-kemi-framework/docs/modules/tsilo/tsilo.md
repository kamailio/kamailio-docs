# tsilo #

* 📖[kamailio.cfg::module::tsilo.html](https://kamailio.org/docs/modules/devel/modules/tsilo.html)

Exported functions:

* [KSR.tsilo.ts_append\(\)](#ksrtsilots_append)
* [KSR.tsilo.ts_append_by_contact\(\)](#ksrtsilots_append_by_contact)
* [KSR.tsilo.ts_append_by_contact_uri\(\)](#ksrtsilots_append_by_contact_uri)
* [KSR.tsilo.ts_append_to\(\)](#ksrtsilots_append_to)
* [KSR.tsilo.ts_append_to_uri\(\)](#ksrtsilots_append_to_uri)
* [KSR.tsilo.ts_store\(\)](#ksrtsilots_store)
* [KSR.tsilo.ts_store_uri\(\)](#ksrtsilots_store_uri)

## KSR.tsilo.ts_append ##

```cpp
int KSR.tsilo.ts_append(str "_table", str "_ruri");
```

* 📖[kamailio.cfg::function::ts_append\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append)

## KSR.tsilo.ts_append_by_contact ##

```cpp
int KSR.tsilo.ts_append_by_contact(str "_table", str "_ruri");
```

* 📖[kamailio.cfg::function::ts_append_by_contact\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_by_contact)

## KSR.tsilo.ts_append_by_contact_uri ##

```cpp
int KSR.tsilo.ts_append_by_contact_uri(str "_table", str "_ruri", str "_contact");
```

* 📖[kamailio.cfg::function::ts_append_by_contact_uri\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_by_contact_uri)

## KSR.tsilo.ts_append_to ##

```cpp
int KSR.tsilo.ts_append_to(int tindex, int tlabel, str "_table");
```

* 📖[kamailio.cfg::function::ts_append_to\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to)

## KSR.tsilo.ts_append_to_uri ##

```cpp
int KSR.tsilo.ts_append_to_uri(int tindex, int tlabel, str "_table", str "_uri");
```

* 📖[kamailio.cfg::function::ts_append_to_uri\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to_uri)

## KSR.tsilo.ts_store ##

```cpp
int KSR.tsilo.ts_store();
```

* 📖[kamailio.cfg::function::ts_store\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store)

## KSR.tsilo.ts_store_uri ##

```cpp
int KSR.tsilo.ts_store_uri(str "puri");
```

* 📖[kamailio.cfg::function::ts_store_uri\(\)](https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store_uri)
