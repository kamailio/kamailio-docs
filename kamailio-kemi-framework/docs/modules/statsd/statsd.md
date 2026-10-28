# statsd #

* 📖[kamailio.cfg::module::statsd.html](https://kamailio.org/docs/modules/devel/modules/statsd.html)

Exported functions:

* [KSR.statsd.statsd_decr\(\)](#ksrstatsdstatsd_decr)
* [KSR.statsd.statsd_gauge\(\)](#ksrstatsdstatsd_gauge)
* [KSR.statsd.statsd_histogram\(\)](#ksrstatsdstatsd_histogram)
* [KSR.statsd.statsd_incr\(\)](#ksrstatsdstatsd_incr)
* [KSR.statsd.statsd_labels_decr\(\)](#ksrstatsdstatsd_labels_decr)
* [KSR.statsd.statsd_labels_gauge\(\)](#ksrstatsdstatsd_labels_gauge)
* [KSR.statsd.statsd_labels_histogram\(\)](#ksrstatsdstatsd_labels_histogram)
* [KSR.statsd.statsd_labels_incr\(\)](#ksrstatsdstatsd_labels_incr)
* [KSR.statsd.statsd_labels_set\(\)](#ksrstatsdstatsd_labels_set)
* [KSR.statsd.statsd_labels_stop\(\)](#ksrstatsdstatsd_labels_stop)
* [KSR.statsd.statsd_set\(\)](#ksrstatsdstatsd_set)
* [KSR.statsd.statsd_start\(\)](#ksrstatsdstatsd_start)
* [KSR.statsd.statsd_stop\(\)](#ksrstatsdstatsd_stop)

## KSR.statsd.statsd_decr ##

```cpp
int KSR.statsd.statsd_decr(str "key");
```

* 📖[kamailio.cfg::function::statsd_decr\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_decr)

## KSR.statsd.statsd_gauge ##

```cpp
int KSR.statsd.statsd_gauge(str "key", str "val");
```

* 📖[kamailio.cfg::function::statsd_gauge\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_gauge)

## KSR.statsd.statsd_histogram ##

```cpp
int KSR.statsd.statsd_histogram(str "key", str "val");
```

* 📖[kamailio.cfg::function::statsd_histogram\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_histogram)

## KSR.statsd.statsd_incr ##

```cpp
int KSR.statsd.statsd_incr(str "key");
```

* 📖[kamailio.cfg::function::statsd_incr\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_incr)

## KSR.statsd.statsd_labels_decr ##

```cpp
int KSR.statsd.statsd_labels_decr(str "key", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_decr\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_decr)

## KSR.statsd.statsd_labels_gauge ##

```cpp
int KSR.statsd.statsd_labels_gauge(str "key", str "val", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_gauge\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_gauge)

## KSR.statsd.statsd_labels_histogram ##

```cpp
int KSR.statsd.statsd_labels_histogram(str "key", str "val", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_histogram\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_histogram)

## KSR.statsd.statsd_labels_incr ##

```cpp
int KSR.statsd.statsd_labels_incr(str "key", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_incr\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_incr)

## KSR.statsd.statsd_labels_set ##

```cpp
int KSR.statsd.statsd_labels_set(str "key", str "val", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_set\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_set)

## KSR.statsd.statsd_labels_stop ##

```cpp
int KSR.statsd.statsd_labels_stop(str "key", str "labels");
```

* 📖[kamailio.cfg::function::statsd_labels_stop\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_labels_stop)

## KSR.statsd.statsd_set ##

```cpp
int KSR.statsd.statsd_set(str "key", str "val");
```

* 📖[kamailio.cfg::function::statsd_set\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_set)

## KSR.statsd.statsd_start ##

```cpp
int KSR.statsd.statsd_start(str "key");
```

* 📖[kamailio.cfg::function::statsd_start\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_start)

## KSR.statsd.statsd_stop ##

```cpp
int KSR.statsd.statsd_stop(str "key");
```

* 📖[kamailio.cfg::function::statsd_stop\(\)](https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_stop)
