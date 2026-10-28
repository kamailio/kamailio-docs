# dispatcher #

* 📖[kamailio.cfg::module::dispatcher.html](https://kamailio.org/docs/modules/devel/modules/dispatcher.html)

Exported functions:

* [KSR.dispatcher.ds_is_active\(\)](#ksrdispatcherds_is_active)
* [KSR.dispatcher.ds_is_active_uri\(\)](#ksrdispatcherds_is_active_uri)
* [KSR.dispatcher.ds_is_from_list\(\)](#ksrdispatcherds_is_from_list)
* [KSR.dispatcher.ds_is_from_list_mode\(\)](#ksrdispatcherds_is_from_list_mode)
* [KSR.dispatcher.ds_is_from_list_uri\(\)](#ksrdispatcherds_is_from_list_uri)
* [KSR.dispatcher.ds_is_from_lists\(\)](#ksrdispatcherds_is_from_lists)
* [KSR.dispatcher.ds_list_exists\(\)](#ksrdispatcherds_list_exists)
* [KSR.dispatcher.ds_load_unset\(\)](#ksrdispatcherds_load_unset)
* [KSR.dispatcher.ds_load_unset_callid\(\)](#ksrdispatcherds_load_unset_callid)
* [KSR.dispatcher.ds_load_update\(\)](#ksrdispatcherds_load_update)
* [KSR.dispatcher.ds_mark_addr\(\)](#ksrdispatcherds_mark_addr)
* [KSR.dispatcher.ds_mark_dst\(\)](#ksrdispatcherds_mark_dst)
* [KSR.dispatcher.ds_mark_dst_state\(\)](#ksrdispatcherds_mark_dst_state)
* [KSR.dispatcher.ds_next_domain\(\)](#ksrdispatcherds_next_domain)
* [KSR.dispatcher.ds_next_dst\(\)](#ksrdispatcherds_next_dst)
* [KSR.dispatcher.ds_reload\(\)](#ksrdispatcherds_reload)
* [KSR.dispatcher.ds_select\(\)](#ksrdispatcherds_select)
* [KSR.dispatcher.ds_select_dns\(\)](#ksrdispatcherds_select_dns)
* [KSR.dispatcher.ds_select_dns_limit\(\)](#ksrdispatcherds_select_dns_limit)
* [KSR.dispatcher.ds_select_domain\(\)](#ksrdispatcherds_select_domain)
* [KSR.dispatcher.ds_select_domain_limit\(\)](#ksrdispatcherds_select_domain_limit)
* [KSR.dispatcher.ds_select_dst\(\)](#ksrdispatcherds_select_dst)
* [KSR.dispatcher.ds_select_dst_limit\(\)](#ksrdispatcherds_select_dst_limit)
* [KSR.dispatcher.ds_select_limit\(\)](#ksrdispatcherds_select_limit)
* [KSR.dispatcher.ds_select_routes\(\)](#ksrdispatcherds_select_routes)
* [KSR.dispatcher.ds_select_routes_limit\(\)](#ksrdispatcherds_select_routes_limit)
* [KSR.dispatcher.ds_set_domain\(\)](#ksrdispatcherds_set_domain)
* [KSR.dispatcher.ds_set_dst\(\)](#ksrdispatcherds_set_dst)

## KSR.dispatcher.ds_is_active ##

```cpp
int KSR.dispatcher.ds_is_active(int set);
```

* 📖[kamailio.cfg::function::ds_is_active\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_active)

## KSR.dispatcher.ds_is_active_uri ##

```cpp
int KSR.dispatcher.ds_is_active_uri(int set, str "uri");
```

* 📖[kamailio.cfg::function::ds_is_active_uri\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_active_uri)

## KSR.dispatcher.ds_is_from_list ##

```cpp
int KSR.dispatcher.ds_is_from_list(int group);
```

* 📖[kamailio.cfg::function::ds_is_from_list\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list)

## KSR.dispatcher.ds_is_from_list_mode ##

```cpp
int KSR.dispatcher.ds_is_from_list_mode(int vset, int vmode);
```

* 📖[kamailio.cfg::function::ds_is_from_list_mode\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_mode)

## KSR.dispatcher.ds_is_from_list_uri ##

```cpp
int KSR.dispatcher.ds_is_from_list_uri(int vset, int vmode, str "vuri");
```

* 📖[kamailio.cfg::function::ds_is_from_list_uri\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_uri)

## KSR.dispatcher.ds_is_from_lists ##

```cpp
int KSR.dispatcher.ds_is_from_lists();
```

* 📖[kamailio.cfg::function::ds_is_from_lists\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_lists)

## KSR.dispatcher.ds_list_exists ##

```cpp
int KSR.dispatcher.ds_list_exists(int set);
```

* 📖[kamailio.cfg::function::ds_list_exists\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_list_exists)

## KSR.dispatcher.ds_load_unset ##

```cpp
int KSR.dispatcher.ds_load_unset();
```

* 📖[kamailio.cfg::function::ds_load_unset\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_unset)

## KSR.dispatcher.ds_load_unset_callid ##

```cpp
int KSR.dispatcher.ds_load_unset_callid(str "callid");
```

* 📖[kamailio.cfg::function::ds_load_unset_callid\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_unset_callid)

## KSR.dispatcher.ds_load_update ##

```cpp
int KSR.dispatcher.ds_load_update();
```

* 📖[kamailio.cfg::function::ds_load_update\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_update)

## KSR.dispatcher.ds_mark_addr ##

```cpp
int KSR.dispatcher.ds_mark_addr(str "vstate", int vgroup, str "vuri");
```

* 📖[kamailio.cfg::function::ds_mark_addr\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_addr)

## KSR.dispatcher.ds_mark_dst ##

```cpp
int KSR.dispatcher.ds_mark_dst();
```

* 📖[kamailio.cfg::function::ds_mark_dst\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst)

## KSR.dispatcher.ds_mark_dst_state ##

```cpp
int KSR.dispatcher.ds_mark_dst_state(str "sval");
```

* 📖[kamailio.cfg::function::ds_mark_dst_state\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst_state)

## KSR.dispatcher.ds_next_domain ##

```cpp
int KSR.dispatcher.ds_next_domain();
```

* 📖[kamailio.cfg::function::ds_next_domain\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_domain)

## KSR.dispatcher.ds_next_dst ##

```cpp
int KSR.dispatcher.ds_next_dst();
```

* 📖[kamailio.cfg::function::ds_next_dst\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_dst)

## KSR.dispatcher.ds_reload ##

```cpp
int KSR.dispatcher.ds_reload();
```

* 📖[kamailio.cfg::function::ds_reload\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_reload)

## KSR.dispatcher.ds_select ##

```cpp
int KSR.dispatcher.ds_select(int set, int alg);
```

* 📖[kamailio.cfg::function::ds_select\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select)

## KSR.dispatcher.ds_select_dns ##

```cpp
int KSR.dispatcher.ds_select_dns();
```

* 📖[kamailio.cfg::function::ds_select_dns\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dns)

## KSR.dispatcher.ds_select_dns_limit ##

```cpp
int KSR.dispatcher.ds_select_dns_limit(int limit);
```

* 📖[kamailio.cfg::function::ds_select_dns_limit\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dns_limit)

## KSR.dispatcher.ds_select_domain ##

```cpp
int KSR.dispatcher.ds_select_domain(int set, int alg);
```

* 📖[kamailio.cfg::function::ds_select_domain\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain)

## KSR.dispatcher.ds_select_domain_limit ##

```cpp
int KSR.dispatcher.ds_select_domain_limit(int set, int alg, int limit);
```

* 📖[kamailio.cfg::function::ds_select_domain_limit\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain_limit)

## KSR.dispatcher.ds_select_dst ##

```cpp
int KSR.dispatcher.ds_select_dst(int set, int alg);
```

* 📖[kamailio.cfg::function::ds_select_dst\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst)

## KSR.dispatcher.ds_select_dst_limit ##

```cpp
int KSR.dispatcher.ds_select_dst_limit(int set, int alg, int limit);
```

* 📖[kamailio.cfg::function::ds_select_dst_limit\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst_limit)

## KSR.dispatcher.ds_select_limit ##

```cpp
int KSR.dispatcher.ds_select_limit(int set, int alg, int limit);
```

* 📖[kamailio.cfg::function::ds_select_limit\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_limit)

## KSR.dispatcher.ds_select_routes ##

```cpp
int KSR.dispatcher.ds_select_routes(str "srules", str "smode");
```

* 📖[kamailio.cfg::function::ds_select_routes\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes)

## KSR.dispatcher.ds_select_routes_limit ##

```cpp
int KSR.dispatcher.ds_select_routes_limit(str "srules", str "smode", int rlimit);
```

* 📖[kamailio.cfg::function::ds_select_routes_limit\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes_limit)

## KSR.dispatcher.ds_set_domain ##

```cpp
int KSR.dispatcher.ds_set_domain();
```

* 📖[kamailio.cfg::function::ds_set_domain\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_domain)

## KSR.dispatcher.ds_set_dst ##

```cpp
int KSR.dispatcher.ds_set_dst();
```

* 📖[kamailio.cfg::function::ds_set_dst\(\)](https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_dst)
