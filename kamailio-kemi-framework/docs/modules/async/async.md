# async #

* 📖[kamailio.cfg::module::async.html](https://kamailio.org/docs/modules/devel/modules/async.html)

Exported functions:

* [KSR.async.get_data\(\)](#ksrasyncget_data)
* [KSR.async.get_gname\(\)](#ksrasyncget_gname)
* [KSR.async.ms_route\(\)](#ksrasyncms_route)
* [KSR.async.route\(\)](#ksrasyncroute)
* [KSR.async.task_data\(\)](#ksrasynctask_data)
* [KSR.async.task_group_data\(\)](#ksrasynctask_group_data)
* [KSR.async.task_group_route\(\)](#ksrasynctask_group_route)
* [KSR.async.task_route\(\)](#ksrasynctask_route)

## KSR.async.get_data ##

```cpp
xval KSR.async.get_data();
```

* 📖[kamailio.cfg::function::get_data\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.get_data)

## KSR.async.get_gname ##

```cpp
xval KSR.async.get_gname();
```

* 📖[kamailio.cfg::function::get_gname\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.get_gname)

## KSR.async.ms_route ##

```cpp
int KSR.async.ms_route(str "rn", int s);
```

* 📖[kamailio.cfg::function::ms_route\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.ms_route)

## KSR.async.route ##

```cpp
int KSR.async.route(str "rn", int s);
```

* 📖[kamailio.cfg::function::route\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.route)

## KSR.async.task_data ##

```cpp
int KSR.async.task_data(str "rn", str "sdata");
```

* 📖[kamailio.cfg::function::task_data\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_data)

## KSR.async.task_group_data ##

```cpp
int KSR.async.task_group_data(str "rn", str "gn", str "sdata");
```

* 📖[kamailio.cfg::function::task_group_data\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_group_data)

## KSR.async.task_group_route ##

```cpp
int KSR.async.task_group_route(str "rn", str "gn");
```

* 📖[kamailio.cfg::function::task_group_route\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_group_route)

## KSR.async.task_route ##

```cpp
int KSR.async.task_route(str "rn");
```

* 📖[kamailio.cfg::function::task_route\(\)](https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_route)
