# mqueue #

* 📖[kamailio.cfg::module::mqueue.html](https://kamailio.org/docs/modules/devel/modules/mqueue.html)

Exported functions:

* [KSR.mqueue.mq_add\(\)](#ksrmqueuemq_add)
* [KSR.mqueue.mq_fetch\(\)](#ksrmqueuemq_fetch)
* [KSR.mqueue.mq_pv_free\(\)](#ksrmqueuemq_pv_free)
* [KSR.mqueue.mq_size\(\)](#ksrmqueuemq_size)
* [KSR.mqueue.mqk_get\(\)](#ksrmqueuemqk_get)
* [KSR.mqueue.mqk_gete\(\)](#ksrmqueuemqk_gete)
* [KSR.mqueue.mqk_getw\(\)](#ksrmqueuemqk_getw)
* [KSR.mqueue.mqv_get\(\)](#ksrmqueuemqv_get)
* [KSR.mqueue.mqv_gete\(\)](#ksrmqueuemqv_gete)
* [KSR.mqueue.mqv_getw\(\)](#ksrmqueuemqv_getw)

## KSR.mqueue.mq_add ##

```cpp
int KSR.mqueue.mq_add(str "mq", str "key", str "val");
```

* 📖[kamailio.cfg::function::mq_add\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_add)

## KSR.mqueue.mq_fetch ##

```cpp
int KSR.mqueue.mq_fetch(str "mq");
```

* 📖[kamailio.cfg::function::mq_fetch\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_fetch)

## KSR.mqueue.mq_pv_free ##

```cpp
int KSR.mqueue.mq_pv_free(str "mq");
```

* 📖[kamailio.cfg::function::mq_pv_free\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_pv_free)

## KSR.mqueue.mq_size ##

```cpp
int KSR.mqueue.mq_size(str "mq");
```

* 📖[kamailio.cfg::function::mq_size\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_size)

## KSR.mqueue.mqk_get ##

```cpp
xval KSR.mqueue.mqk_get(str "qname");
```

* 📖[kamailio.cfg::function::mqk_get\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_get)

## KSR.mqueue.mqk_gete ##

```cpp
xval KSR.mqueue.mqk_gete(str "qname");
```

* 📖[kamailio.cfg::function::mqk_gete\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_gete)

## KSR.mqueue.mqk_getw ##

```cpp
xval KSR.mqueue.mqk_getw(str "qname");
```

* 📖[kamailio.cfg::function::mqk_getw\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_getw)

## KSR.mqueue.mqv_get ##

```cpp
xval KSR.mqueue.mqv_get(str "qname");
```

* 📖[kamailio.cfg::function::mqv_get\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_get)

## KSR.mqueue.mqv_gete ##

```cpp
xval KSR.mqueue.mqv_gete(str "qname");
```

* 📖[kamailio.cfg::function::mqv_gete\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_gete)

## KSR.mqueue.mqv_getw ##

```cpp
xval KSR.mqueue.mqv_getw(str "qname");
```

* 📖[kamailio.cfg::function::mqv_getw\(\)](https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_getw)
