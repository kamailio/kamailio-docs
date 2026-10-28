# msrp #

* 📖[kamailio.cfg::module::msrp.html](https://kamailio.org/docs/modules/devel/modules/msrp.html)

Exported functions:

* [KSR.msrp.cmap_lookup\(\)](#ksrmsrpcmap_lookup)
* [KSR.msrp.cmap_save\(\)](#ksrmsrpcmap_save)
* [KSR.msrp.forward\(\)](#ksrmsrpforward)
* [KSR.msrp.is_reply\(\)](#ksrmsrpis_reply)
* [KSR.msrp.is_request\(\)](#ksrmsrpis_request)
* [KSR.msrp.relay\(\)](#ksrmsrprelay)
* [KSR.msrp.relay_flags\(\)](#ksrmsrprelay_flags)
* [KSR.msrp.reply\(\)](#ksrmsrpreply)
* [KSR.msrp.reply_flags\(\)](#ksrmsrpreply_flags)
* [KSR.msrp.set_dst\(\)](#ksrmsrpset_dst)

## KSR.msrp.cmap_lookup ##

```cpp
int KSR.msrp.cmap_lookup();
```

* 📖[kamailio.cfg::function::cmap_lookup\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_lookup)

## KSR.msrp.cmap_save ##

```cpp
int KSR.msrp.cmap_save();
```

* 📖[kamailio.cfg::function::cmap_save\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_save)

## KSR.msrp.forward ##

```cpp
int KSR.msrp.forward(str "tpath", str "fpath");
```

* 📖[kamailio.cfg::function::forward\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.forward)

## KSR.msrp.is_reply ##

```cpp
int KSR.msrp.is_reply();
```

* 📖[kamailio.cfg::function::is_reply\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_reply)

## KSR.msrp.is_request ##

```cpp
int KSR.msrp.is_request();
```

* 📖[kamailio.cfg::function::is_request\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_request)

## KSR.msrp.relay ##

```cpp
int KSR.msrp.relay();
```

* 📖[kamailio.cfg::function::relay\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay)

## KSR.msrp.relay_flags ##

```cpp
int KSR.msrp.relay_flags(int rtflags);
```

* 📖[kamailio.cfg::function::relay_flags\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay_flags)

## KSR.msrp.reply ##

```cpp
int KSR.msrp.reply(str "rcode", str "rtext", str "rhdrs");
```

* 📖[kamailio.cfg::function::reply\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply)

## KSR.msrp.reply_flags ##

```cpp
int KSR.msrp.reply_flags(int rtflags);
```

* 📖[kamailio.cfg::function::reply_flags\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply_flags)

## KSR.msrp.set_dst ##

```cpp
int KSR.msrp.set_dst(str "rtaddr", str "rfsock");
```

* 📖[kamailio.cfg::function::set_dst\(\)](https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.set_dst)
