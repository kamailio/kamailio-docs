# xhttp_prom #

* 📖[kamailio.cfg::module::xhttp_prom.html](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html)

Exported functions:

* [KSR.xhttp_prom.check_uri\(\)](#ksrxhttp_promcheck_uri)
* [KSR.xhttp_prom.counter_inc_l0\(\)](#ksrxhttp_promcounter_inc_l0)
* [KSR.xhttp_prom.counter_inc_l1\(\)](#ksrxhttp_promcounter_inc_l1)
* [KSR.xhttp_prom.counter_inc_l2\(\)](#ksrxhttp_promcounter_inc_l2)
* [KSR.xhttp_prom.counter_inc_l3\(\)](#ksrxhttp_promcounter_inc_l3)
* [KSR.xhttp_prom.counter_reset_l0\(\)](#ksrxhttp_promcounter_reset_l0)
* [KSR.xhttp_prom.counter_reset_l1\(\)](#ksrxhttp_promcounter_reset_l1)
* [KSR.xhttp_prom.counter_reset_l2\(\)](#ksrxhttp_promcounter_reset_l2)
* [KSR.xhttp_prom.counter_reset_l3\(\)](#ksrxhttp_promcounter_reset_l3)
* [KSR.xhttp_prom.dispatch\(\)](#ksrxhttp_promdispatch)
* [KSR.xhttp_prom.gauge_inc_l0\(\)](#ksrxhttp_promgauge_inc_l0)
* [KSR.xhttp_prom.gauge_inc_l1\(\)](#ksrxhttp_promgauge_inc_l1)
* [KSR.xhttp_prom.gauge_inc_l2\(\)](#ksrxhttp_promgauge_inc_l2)
* [KSR.xhttp_prom.gauge_inc_l3\(\)](#ksrxhttp_promgauge_inc_l3)
* [KSR.xhttp_prom.gauge_reset_l0\(\)](#ksrxhttp_promgauge_reset_l0)
* [KSR.xhttp_prom.gauge_reset_l1\(\)](#ksrxhttp_promgauge_reset_l1)
* [KSR.xhttp_prom.gauge_reset_l2\(\)](#ksrxhttp_promgauge_reset_l2)
* [KSR.xhttp_prom.gauge_reset_l3\(\)](#ksrxhttp_promgauge_reset_l3)
* [KSR.xhttp_prom.gauge_set_l0\(\)](#ksrxhttp_promgauge_set_l0)
* [KSR.xhttp_prom.gauge_set_l1\(\)](#ksrxhttp_promgauge_set_l1)
* [KSR.xhttp_prom.gauge_set_l2\(\)](#ksrxhttp_promgauge_set_l2)
* [KSR.xhttp_prom.gauge_set_l3\(\)](#ksrxhttp_promgauge_set_l3)
* [KSR.xhttp_prom.histogram_observe_l0\(\)](#ksrxhttp_promhistogram_observe_l0)
* [KSR.xhttp_prom.histogram_observe_l1\(\)](#ksrxhttp_promhistogram_observe_l1)
* [KSR.xhttp_prom.histogram_observe_l2\(\)](#ksrxhttp_promhistogram_observe_l2)
* [KSR.xhttp_prom.histogram_observe_l3\(\)](#ksrxhttp_promhistogram_observe_l3)

## KSR.xhttp_prom.check_uri ##

```cpp
int KSR.xhttp_prom.check_uri();
```

* 📖[kamailio.cfg::function::check_uri\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.check_uri)

## KSR.xhttp_prom.counter_inc_l0 ##

```cpp
int KSR.xhttp_prom.counter_inc_l0(str "s_name", int number);
```

* 📖[kamailio.cfg::function::counter_inc_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l0)

## KSR.xhttp_prom.counter_inc_l1 ##

```cpp
int KSR.xhttp_prom.counter_inc_l1(str "s_name", int number, str "l1");
```

* 📖[kamailio.cfg::function::counter_inc_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l1)

## KSR.xhttp_prom.counter_inc_l2 ##

```cpp
int KSR.xhttp_prom.counter_inc_l2(str "s_name", int number, str "l1", str "l2");
```

* 📖[kamailio.cfg::function::counter_inc_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l2)

## KSR.xhttp_prom.counter_inc_l3 ##

```cpp
int KSR.xhttp_prom.counter_inc_l3(str "s_name", int number, str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::counter_inc_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l3)

## KSR.xhttp_prom.counter_reset_l0 ##

```cpp
int KSR.xhttp_prom.counter_reset_l0(str "s_name");
```

* 📖[kamailio.cfg::function::counter_reset_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l0)

## KSR.xhttp_prom.counter_reset_l1 ##

```cpp
int KSR.xhttp_prom.counter_reset_l1(str "s_name", str "l1");
```

* 📖[kamailio.cfg::function::counter_reset_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l1)

## KSR.xhttp_prom.counter_reset_l2 ##

```cpp
int KSR.xhttp_prom.counter_reset_l2(str "s_name", str "l1", str "l2");
```

* 📖[kamailio.cfg::function::counter_reset_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l2)

## KSR.xhttp_prom.counter_reset_l3 ##

```cpp
int KSR.xhttp_prom.counter_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::counter_reset_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l3)

## KSR.xhttp_prom.dispatch ##

```cpp
int KSR.xhttp_prom.dispatch();
```

* 📖[kamailio.cfg::function::dispatch\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.dispatch)

## KSR.xhttp_prom.gauge_inc_l0 ##

```cpp
int KSR.xhttp_prom.gauge_inc_l0(str "s_name", str "s_number");
```

* 📖[kamailio.cfg::function::gauge_inc_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_inc_l0)

## KSR.xhttp_prom.gauge_inc_l1 ##

```cpp
int KSR.xhttp_prom.gauge_inc_l1(str "s_name", str "s_number", str "l1");
```

* 📖[kamailio.cfg::function::gauge_inc_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_inc_l1)

## KSR.xhttp_prom.gauge_inc_l2 ##

```cpp
int KSR.xhttp_prom.gauge_inc_l2(str "s_name", str "s_number", str "l1", str "l2");
```

* 📖[kamailio.cfg::function::gauge_inc_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_inc_l2)

## KSR.xhttp_prom.gauge_inc_l3 ##

```cpp
int KSR.xhttp_prom.gauge_inc_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::gauge_inc_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_inc_l3)

## KSR.xhttp_prom.gauge_reset_l0 ##

```cpp
int KSR.xhttp_prom.gauge_reset_l0(str "s_name");
```

* 📖[kamailio.cfg::function::gauge_reset_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l0)

## KSR.xhttp_prom.gauge_reset_l1 ##

```cpp
int KSR.xhttp_prom.gauge_reset_l1(str "s_name", str "l1");
```

* 📖[kamailio.cfg::function::gauge_reset_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l1)

## KSR.xhttp_prom.gauge_reset_l2 ##

```cpp
int KSR.xhttp_prom.gauge_reset_l2(str "s_name", str "l1", str "l2");
```

* 📖[kamailio.cfg::function::gauge_reset_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l2)

## KSR.xhttp_prom.gauge_reset_l3 ##

```cpp
int KSR.xhttp_prom.gauge_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::gauge_reset_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l3)

## KSR.xhttp_prom.gauge_set_l0 ##

```cpp
int KSR.xhttp_prom.gauge_set_l0(str "s_name", str "s_number");
```

* 📖[kamailio.cfg::function::gauge_set_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l0)

## KSR.xhttp_prom.gauge_set_l1 ##

```cpp
int KSR.xhttp_prom.gauge_set_l1(str "s_name", str "s_number", str "l1");
```

* 📖[kamailio.cfg::function::gauge_set_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l1)

## KSR.xhttp_prom.gauge_set_l2 ##

```cpp
int KSR.xhttp_prom.gauge_set_l2(str "s_name", str "s_number", str "l1", str "l2");
```

* 📖[kamailio.cfg::function::gauge_set_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l2)

## KSR.xhttp_prom.gauge_set_l3 ##

```cpp
int KSR.xhttp_prom.gauge_set_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::gauge_set_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l3)

## KSR.xhttp_prom.histogram_observe_l0 ##

```cpp
int KSR.xhttp_prom.histogram_observe_l0(str "s_name", str "s_number");
```

* 📖[kamailio.cfg::function::histogram_observe_l0\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l0)

## KSR.xhttp_prom.histogram_observe_l1 ##

```cpp
int KSR.xhttp_prom.histogram_observe_l1(str "s_name", str "s_number", str "l1");
```

* 📖[kamailio.cfg::function::histogram_observe_l1\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l1)

## KSR.xhttp_prom.histogram_observe_l2 ##

```cpp
int KSR.xhttp_prom.histogram_observe_l2(str "s_name", str "s_number", str "l1", str "l2");
```

* 📖[kamailio.cfg::function::histogram_observe_l2\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l2)

## KSR.xhttp_prom.histogram_observe_l3 ##

```cpp
int KSR.xhttp_prom.histogram_observe_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

* 📖[kamailio.cfg::function::histogram_observe_l3\(\)](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l3)
