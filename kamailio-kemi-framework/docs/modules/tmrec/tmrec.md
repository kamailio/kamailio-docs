# tmrec #

* 📖[kamailio.cfg::module::tmrec.html](https://kamailio.org/docs/modules/devel/modules/tmrec.html)

Exported functions:

* [KSR.tmrec.is_leap_year\(\)](#ksrtmrecis_leap_year)
* [KSR.tmrec.is_leap_year_now\(\)](#ksrtmrecis_leap_year_now)
* [KSR.tmrec.match\(\)](#ksrtmrecmatch)
* [KSR.tmrec.match_timestamp\(\)](#ksrtmrecmatch_timestamp)
* [KSR.tmrec.time_period_match\(\)](#ksrtmrectime_period_match)
* [KSR.tmrec.time_period_match_timestamp\(\)](#ksrtmrectime_period_match_timestamp)

## KSR.tmrec.is_leap_year ##

```cpp
int KSR.tmrec.is_leap_year(int y);
```

* 📖[kamailio.cfg::function::is_leap_year\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year)

## KSR.tmrec.is_leap_year_now ##

```cpp
int KSR.tmrec.is_leap_year_now();
```

* 📖[kamailio.cfg::function::is_leap_year_now\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year_now)

## KSR.tmrec.match ##

```cpp
int KSR.tmrec.match(str "rv");
```

* 📖[kamailio.cfg::function::match\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match)

## KSR.tmrec.match_timestamp ##

```cpp
int KSR.tmrec.match_timestamp(str "rv", int ti);
```

* 📖[kamailio.cfg::function::match_timestamp\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match_timestamp)

## KSR.tmrec.time_period_match ##

```cpp
int KSR.tmrec.time_period_match(str "period");
```

* 📖[kamailio.cfg::function::time_period_match\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match)

## KSR.tmrec.time_period_match_timestamp ##

```cpp
int KSR.tmrec.time_period_match_timestamp(str "period", int ti);
```

* 📖[kamailio.cfg::function::time_period_match_timestamp\(\)](https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match_timestamp)
