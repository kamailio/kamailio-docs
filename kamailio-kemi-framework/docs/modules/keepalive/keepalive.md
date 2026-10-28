# keepalive #

* 📖[kamailio.cfg::module::keepalive.html](https://kamailio.org/docs/modules/devel/modules/keepalive.html)

Exported functions:

* [KSR.keepalive.add_destination\(\)](#ksrkeepaliveadd_destination)
* [KSR.keepalive.del_destination\(\)](#ksrkeepalivedel_destination)
* [KSR.keepalive.is_alive\(\)](#ksrkeepaliveis_alive)

## KSR.keepalive.add_destination ##

```cpp
int KSR.keepalive.add_destination(str "uri", str "owner");
```

* 📖[kamailio.cfg::function::add_destination\(\)](https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.add_destination)

## KSR.keepalive.del_destination ##

```cpp
int KSR.keepalive.del_destination(str "uri", str "owner");
```

* 📖[kamailio.cfg::function::del_destination\(\)](https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.del_destination)

## KSR.keepalive.is_alive ##

```cpp
int KSR.keepalive.is_alive(str "dest");
```

* 📖[kamailio.cfg::function::is_alive\(\)](https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.is_alive)
