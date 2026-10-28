# cnxcc #

* 📖[kamailio.cfg::module::cnxcc.html](https://kamailio.org/docs/modules/devel/modules/cnxcc.html)

Exported functions:

* [KSR.cnxcc.get_channel_count\(\)](#ksrcnxccget_channel_count)
* [KSR.cnxcc.set_max_channels\(\)](#ksrcnxccset_max_channels)
* [KSR.cnxcc.set_max_credit\(\)](#ksrcnxccset_max_credit)
* [KSR.cnxcc.set_max_time\(\)](#ksrcnxccset_max_time)
* [KSR.cnxcc.terminate_all\(\)](#ksrcnxccterminate_all)
* [KSR.cnxcc.update_max_time\(\)](#ksrcnxccupdate_max_time)

## KSR.cnxcc.get_channel_count ##

```cpp
int KSR.cnxcc.get_channel_count(str "sclient", str "pvname");
```

* 📖[kamailio.cfg::function::get_channel_count\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.get_channel_count)

## KSR.cnxcc.set_max_channels ##

```cpp
int KSR.cnxcc.set_max_channels(str "sclient", int max_chan);
```

* 📖[kamailio.cfg::function::set_max_channels\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_channels)

## KSR.cnxcc.set_max_credit ##

```cpp
int KSR.cnxcc.set_max_credit(str "sclient", str "scredit", str "sconnect", str "scps", int initp, int finishp);
```

* 📖[kamailio.cfg::function::set_max_credit\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_credit)

## KSR.cnxcc.set_max_time ##

```cpp
int KSR.cnxcc.set_max_time(str "sclient", int max_secs);
```

* 📖[kamailio.cfg::function::set_max_time\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_time)

## KSR.cnxcc.terminate_all ##

```cpp
int KSR.cnxcc.terminate_all(str "sclient");
```

* 📖[kamailio.cfg::function::terminate_all\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.terminate_all)

## KSR.cnxcc.update_max_time ##

```cpp
int KSR.cnxcc.update_max_time(str "sclient", int secs);
```

* 📖[kamailio.cfg::function::update_max_time\(\)](https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.update_max_time)
