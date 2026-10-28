# evapi #

* 📖[kamailio.cfg::module::evapi.html](https://kamailio.org/docs/modules/devel/modules/evapi.html)

Exported functions:

* [KSR.evapi.async_multicast\(\)](#ksrevapiasync_multicast)
* [KSR.evapi.async_relay\(\)](#ksrevapiasync_relay)
* [KSR.evapi.async_unicast\(\)](#ksrevapiasync_unicast)
* [KSR.evapi.close\(\)](#ksrevapiclose)
* [KSR.evapi.relay\(\)](#ksrevapirelay)
* [KSR.evapi.relay_multicast\(\)](#ksrevapirelay_multicast)
* [KSR.evapi.relay_unicast\(\)](#ksrevapirelay_unicast)
* [KSR.evapi.set_tag\(\)](#ksrevapiset_tag)

## KSR.evapi.async_multicast ##

```cpp
int KSR.evapi.async_multicast(str "sdata", str "stag");
```

* 📖[kamailio.cfg::function::async_multicast\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_multicast)

## KSR.evapi.async_relay ##

```cpp
int KSR.evapi.async_relay(str "sdata");
```

* 📖[kamailio.cfg::function::async_relay\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_relay)

## KSR.evapi.async_unicast ##

```cpp
int KSR.evapi.async_unicast(str "sdata", str "stag");
```

* 📖[kamailio.cfg::function::async_unicast\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_unicast)

## KSR.evapi.close ##

```cpp
int KSR.evapi.close();
```

* 📖[kamailio.cfg::function::close\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.close)

## KSR.evapi.relay ##

```cpp
int KSR.evapi.relay(str "sdata");
```

* 📖[kamailio.cfg::function::relay\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay)

## KSR.evapi.relay_multicast ##

```cpp
int KSR.evapi.relay_multicast(str "sdata", str "stag");
```

* 📖[kamailio.cfg::function::relay_multicast\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_multicast)

## KSR.evapi.relay_unicast ##

```cpp
int KSR.evapi.relay_unicast(str "sdata", str "stag");
```

* 📖[kamailio.cfg::function::relay_unicast\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_unicast)

## KSR.evapi.set_tag ##

```cpp
int KSR.evapi.set_tag(str "stag");
```

* 📖[kamailio.cfg::function::set_tag\(\)](https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.set_tag)
