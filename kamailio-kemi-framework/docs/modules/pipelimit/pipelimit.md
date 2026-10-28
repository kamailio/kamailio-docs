# pipelimit #

* 📖[kamailio.cfg::module::pipelimit.html](https://kamailio.org/docs/modules/devel/modules/pipelimit.html)

Exported functions:

* [KSR.pipelimit.pl_active\(\)](#ksrpipelimitpl_active)
* [KSR.pipelimit.pl_check\(\)](#ksrpipelimitpl_check)
* [KSR.pipelimit.pl_check_limit\(\)](#ksrpipelimitpl_check_limit)
* [KSR.pipelimit.pl_drop\(\)](#ksrpipelimitpl_drop)
* [KSR.pipelimit.pl_drop_range\(\)](#ksrpipelimitpl_drop_range)
* [KSR.pipelimit.pl_drop_retry\(\)](#ksrpipelimitpl_drop_retry)

## KSR.pipelimit.pl_active ##

```cpp
int KSR.pipelimit.pl_active(str "pipeid");
```

* 📖[kamailio.cfg::function::pl_active\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_active)

## KSR.pipelimit.pl_check ##

```cpp
int KSR.pipelimit.pl_check(str "pipeid");
```

* 📖[kamailio.cfg::function::pl_check\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check)

## KSR.pipelimit.pl_check_limit ##

```cpp
int KSR.pipelimit.pl_check_limit(str "pipeid", str "alg", int limit);
```

* 📖[kamailio.cfg::function::pl_check_limit\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check_limit)

## KSR.pipelimit.pl_drop ##

```cpp
int KSR.pipelimit.pl_drop();
```

* 📖[kamailio.cfg::function::pl_drop\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop)

## KSR.pipelimit.pl_drop_range ##

```cpp
int KSR.pipelimit.pl_drop_range(int rmin, int rmax);
```

* 📖[kamailio.cfg::function::pl_drop_range\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_range)

## KSR.pipelimit.pl_drop_retry ##

```cpp
int KSR.pipelimit.pl_drop_retry(int rafter);
```

* 📖[kamailio.cfg::function::pl_drop_retry\(\)](https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_retry)
