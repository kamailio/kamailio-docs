# cfgutils #

* 📖[kamailio.cfg::module::cfgutils.html](https://kamailio.org/docs/modules/devel/modules/cfgutils.html)

Exported functions:

* [KSR.cfgutils.abort\(\)](#ksrcfgutilsabort)
* [KSR.cfgutils.check_route_exists\(\)](#ksrcfgutilscheck_route_exists)
* [KSR.cfgutils.core_hash\(\)](#ksrcfgutilscore_hash)
* [KSR.cfgutils.lock\(\)](#ksrcfgutilslock)
* [KSR.cfgutils.lock_key2\(\)](#ksrcfgutilslock_key2)
* [KSR.cfgutils.pkg_status\(\)](#ksrcfgutilspkg_status)
* [KSR.cfgutils.pkg_summary\(\)](#ksrcfgutilspkg_summary)
* [KSR.cfgutils.rand_event\(\)](#ksrcfgutilsrand_event)
* [KSR.cfgutils.rand_get_prob\(\)](#ksrcfgutilsrand_get_prob)
* [KSR.cfgutils.rand_reset_prob\(\)](#ksrcfgutilsrand_reset_prob)
* [KSR.cfgutils.rand_set_prob\(\)](#ksrcfgutilsrand_set_prob)
* [KSR.cfgutils.route_if_exists\(\)](#ksrcfgutilsroute_if_exists)
* [KSR.cfgutils.shm_status\(\)](#ksrcfgutilsshm_status)
* [KSR.cfgutils.shm_summary\(\)](#ksrcfgutilsshm_summary)
* [KSR.cfgutils.sleep\(\)](#ksrcfgutilssleep)
* [KSR.cfgutils.trylock\(\)](#ksrcfgutilstrylock)
* [KSR.cfgutils.trylock_key2\(\)](#ksrcfgutilstrylock_key2)
* [KSR.cfgutils.unlock\(\)](#ksrcfgutilsunlock)
* [KSR.cfgutils.unlock_key2\(\)](#ksrcfgutilsunlock_key2)
* [KSR.cfgutils.usleep\(\)](#ksrcfgutilsusleep)

## KSR.cfgutils.abort ##

```cpp
int KSR.cfgutils.abort();
```

* 📖[kamailio.cfg::function::abort\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.abort)

## KSR.cfgutils.check_route_exists ##

```cpp
int KSR.cfgutils.check_route_exists(str "route");
```

* 📖[kamailio.cfg::function::check_route_exists\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.check_route_exists)

## KSR.cfgutils.core_hash ##

```cpp
int KSR.cfgutils.core_hash(str "s1", str "s2", int sz);
```

* 📖[kamailio.cfg::function::core_hash\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.core_hash)

## KSR.cfgutils.lock ##

```cpp
int KSR.cfgutils.lock(str "lkey");
```

* 📖[kamailio.cfg::function::lock\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.lock)

## KSR.cfgutils.lock_key2 ##

```cpp
int KSR.cfgutils.lock_key2(str "lkey", str "lkey2");
```

* 📖[kamailio.cfg::function::lock_key2\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.lock_key2)

## KSR.cfgutils.pkg_status ##

```cpp
int KSR.cfgutils.pkg_status();
```

* 📖[kamailio.cfg::function::pkg_status\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_status)

## KSR.cfgutils.pkg_summary ##

```cpp
int KSR.cfgutils.pkg_summary();
```

* 📖[kamailio.cfg::function::pkg_summary\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_summary)

## KSR.cfgutils.rand_event ##

```cpp
int KSR.cfgutils.rand_event();
```

* 📖[kamailio.cfg::function::rand_event\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_event)

## KSR.cfgutils.rand_get_prob ##

```cpp
int KSR.cfgutils.rand_get_prob();
```

* 📖[kamailio.cfg::function::rand_get_prob\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_get_prob)

## KSR.cfgutils.rand_reset_prob ##

```cpp
int KSR.cfgutils.rand_reset_prob();
```

* 📖[kamailio.cfg::function::rand_reset_prob\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_reset_prob)

## KSR.cfgutils.rand_set_prob ##

```cpp
int KSR.cfgutils.rand_set_prob(int percent_par);
```

* 📖[kamailio.cfg::function::rand_set_prob\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_set_prob)

## KSR.cfgutils.route_if_exists ##

```cpp
int KSR.cfgutils.route_if_exists(str "route");
```

* 📖[kamailio.cfg::function::route_if_exists\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.route_if_exists)

## KSR.cfgutils.shm_status ##

```cpp
int KSR.cfgutils.shm_status();
```

* 📖[kamailio.cfg::function::shm_status\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_status)

## KSR.cfgutils.shm_summary ##

```cpp
int KSR.cfgutils.shm_summary();
```

* 📖[kamailio.cfg::function::shm_summary\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_summary)

## KSR.cfgutils.sleep ##

```cpp
int KSR.cfgutils.sleep(int v);
```

* 📖[kamailio.cfg::function::sleep\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.sleep)

## KSR.cfgutils.trylock ##

```cpp
int KSR.cfgutils.trylock(str "lkey");
```

* 📖[kamailio.cfg::function::trylock\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.trylock)

## KSR.cfgutils.trylock_key2 ##

```cpp
int KSR.cfgutils.trylock_key2(str "lkey", str "lkey2");
```

* 📖[kamailio.cfg::function::trylock_key2\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.trylock_key2)

## KSR.cfgutils.unlock ##

```cpp
int KSR.cfgutils.unlock(str "lkey");
```

* 📖[kamailio.cfg::function::unlock\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.unlock)

## KSR.cfgutils.unlock_key2 ##

```cpp
int KSR.cfgutils.unlock_key2(str "lkey", str "lkey2");
```

* 📖[kamailio.cfg::function::unlock_key2\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.unlock_key2)

## KSR.cfgutils.usleep ##

```cpp
int KSR.cfgutils.usleep(int v);
```

* 📖[kamailio.cfg::function::usleep\(\)](https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.usleep)
