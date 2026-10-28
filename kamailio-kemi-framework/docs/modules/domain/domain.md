# domain #

* 📖[kamailio.cfg::module::domain.html](https://kamailio.org/docs/modules/devel/modules/domain.html)

Exported functions:

* [KSR.domain.is_domain_local\(\)](#ksrdomainis_domain_local)
* [KSR.domain.is_from_local\(\)](#ksrdomainis_from_local)
* [KSR.domain.is_uri_host_local\(\)](#ksrdomainis_uri_host_local)
* [KSR.domain.lookup_domain\(\)](#ksrdomainlookup_domain)
* [KSR.domain.lookup_domain_prefix\(\)](#ksrdomainlookup_domain_prefix)

## KSR.domain.is_domain_local ##

```cpp
int KSR.domain.is_domain_local(str "sdomain");
```

* 📖[kamailio.cfg::function::is_domain_local\(\)](https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_domain_local)

## KSR.domain.is_from_local ##

```cpp
int KSR.domain.is_from_local();
```

* 📖[kamailio.cfg::function::is_from_local\(\)](https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_from_local)

## KSR.domain.is_uri_host_local ##

```cpp
int KSR.domain.is_uri_host_local();
```

* 📖[kamailio.cfg::function::is_uri_host_local\(\)](https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_uri_host_local)

## KSR.domain.lookup_domain ##

```cpp
int KSR.domain.lookup_domain(str "_sdomain");
```

* 📖[kamailio.cfg::function::lookup_domain\(\)](https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain)

## KSR.domain.lookup_domain_prefix ##

```cpp
int KSR.domain.lookup_domain_prefix(str "_sdomain", str "_sprefix");
```

* 📖[kamailio.cfg::function::lookup_domain_prefix\(\)](https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain_prefix)
