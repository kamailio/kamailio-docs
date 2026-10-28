# ipops #

* 📖[kamailio.cfg::module::ipops.html](https://kamailio.org/docs/modules/devel/modules/ipops.html)

Exported functions:

* [KSR.ipops.compare_ips\(\)](#ksripopscompare_ips)
* [KSR.ipops.compare_pure_ips\(\)](#ksripopscompare_pure_ips)
* [KSR.ipops.detailed_ip_type\(\)](#ksripopsdetailed_ip_type)
* [KSR.ipops.detailed_ipv4_type\(\)](#ksripopsdetailed_ipv4_type)
* [KSR.ipops.detailed_ipv6_type\(\)](#ksripopsdetailed_ipv6_type)
* [KSR.ipops.dns_int_match_ip\(\)](#ksripopsdns_int_match_ip)
* [KSR.ipops.dns_query\(\)](#ksripopsdns_query)
* [KSR.ipops.dns_set_local_ttl\(\)](#ksripopsdns_set_local_ttl)
* [KSR.ipops.dns_sys_match_ip\(\)](#ksripopsdns_sys_match_ip)
* [KSR.ipops.ip_is_in_subnet\(\)](#ksripopsip_is_in_subnet)
* [KSR.ipops.ip_type\(\)](#ksripopsip_type)
* [KSR.ipops.is_in_subnet\(\)](#ksripopsis_in_subnet)
* [KSR.ipops.is_ip\(\)](#ksripopsis_ip)
* [KSR.ipops.is_ip4\(\)](#ksripopsis_ip4)
* [KSR.ipops.is_ip6\(\)](#ksripopsis_ip6)
* [KSR.ipops.is_ip6_reference\(\)](#ksripopsis_ip6_reference)
* [KSR.ipops.is_ip_rfc1918\(\)](#ksripopsis_ip_rfc1918)
* [KSR.ipops.is_pure_ip\(\)](#ksripopsis_pure_ip)
* [KSR.ipops.naptr_query\(\)](#ksripopsnaptr_query)
* [KSR.ipops.ptr_query\(\)](#ksripopsptr_query)
* [KSR.ipops.srv_query\(\)](#ksripopssrv_query)

## KSR.ipops.compare_ips ##

```cpp
int KSR.ipops.compare_ips(str "_sval1", str "_sval2");
```

* 📖[kamailio.cfg::function::compare_ips\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_ips)

## KSR.ipops.compare_pure_ips ##

```cpp
int KSR.ipops.compare_pure_ips(str "_sval1", str "_sval2");
```

* 📖[kamailio.cfg::function::compare_pure_ips\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_pure_ips)

## KSR.ipops.detailed_ip_type ##

```cpp
int KSR.ipops.detailed_ip_type(str "_sval", str "_dpv");
```

* 📖[kamailio.cfg::function::detailed_ip_type\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ip_type)

## KSR.ipops.detailed_ipv4_type ##

```cpp
int KSR.ipops.detailed_ipv4_type(str "_sval", str "_dpv");
```

* 📖[kamailio.cfg::function::detailed_ipv4_type\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv4_type)

## KSR.ipops.detailed_ipv6_type ##

```cpp
int KSR.ipops.detailed_ipv6_type(str "_sval", str "_dpv");
```

* 📖[kamailio.cfg::function::detailed_ipv6_type\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv6_type)

## KSR.ipops.dns_int_match_ip ##

```cpp
int KSR.ipops.dns_int_match_ip(str "vhn", str "vip");
```

* 📖[kamailio.cfg::function::dns_int_match_ip\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_int_match_ip)

## KSR.ipops.dns_query ##

```cpp
int KSR.ipops.dns_query(str "naptrname", str "pvid");
```

* 📖[kamailio.cfg::function::dns_query\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_query)

## KSR.ipops.dns_set_local_ttl ##

```cpp
int KSR.ipops.dns_set_local_ttl(int vttl);
```

* 📖[kamailio.cfg::function::dns_set_local_ttl\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_set_local_ttl)

## KSR.ipops.dns_sys_match_ip ##

```cpp
int KSR.ipops.dns_sys_match_ip(str "vhn", str "vip");
```

* 📖[kamailio.cfg::function::dns_sys_match_ip\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_sys_match_ip)

## KSR.ipops.ip_is_in_subnet ##

```cpp
int KSR.ipops.ip_is_in_subnet(str "_sval1", str "_sval2");
```

* 📖[kamailio.cfg::function::ip_is_in_subnet\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_is_in_subnet)

## KSR.ipops.ip_type ##

```cpp
int KSR.ipops.ip_type(str "sval");
```

* 📖[kamailio.cfg::function::ip_type\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_type)

## KSR.ipops.is_in_subnet ##

```cpp
int KSR.ipops.is_in_subnet(str "_sval1", str "_sval2");
```

* 📖[kamailio.cfg::function::is_in_subnet\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_in_subnet)

## KSR.ipops.is_ip ##

```cpp
int KSR.ipops.is_ip(str "sval");
```

* 📖[kamailio.cfg::function::is_ip\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip)

## KSR.ipops.is_ip4 ##

```cpp
int KSR.ipops.is_ip4(str "sval");
```

* 📖[kamailio.cfg::function::is_ip4\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip4)

## KSR.ipops.is_ip6 ##

```cpp
int KSR.ipops.is_ip6(str "sval");
```

* 📖[kamailio.cfg::function::is_ip6\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6)

## KSR.ipops.is_ip6_reference ##

```cpp
int KSR.ipops.is_ip6_reference(str "sval");
```

* 📖[kamailio.cfg::function::is_ip6_reference\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6_reference)

## KSR.ipops.is_ip_rfc1918 ##

```cpp
int KSR.ipops.is_ip_rfc1918(str "sval");
```

* 📖[kamailio.cfg::function::is_ip_rfc1918\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip_rfc1918)

## KSR.ipops.is_pure_ip ##

```cpp
int KSR.ipops.is_pure_ip(str "sval");
```

* 📖[kamailio.cfg::function::is_pure_ip\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_pure_ip)

## KSR.ipops.naptr_query ##

```cpp
int KSR.ipops.naptr_query(str "naptrname", str "pvid");
```

* 📖[kamailio.cfg::function::naptr_query\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.naptr_query)

## KSR.ipops.ptr_query ##

```cpp
int KSR.ipops.ptr_query(str "ip", str "pvid");
```

* 📖[kamailio.cfg::function::ptr_query\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ptr_query)

## KSR.ipops.srv_query ##

```cpp
int KSR.ipops.srv_query(str "naptrname", str "pvid");
```

* 📖[kamailio.cfg::function::srv_query\(\)](https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.srv_query)
