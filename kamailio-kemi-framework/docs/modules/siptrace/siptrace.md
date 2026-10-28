# siptrace #

* 📖[kamailio.cfg::module::siptrace.html](https://kamailio.org/docs/modules/devel/modules/siptrace.html)

Exported functions:

* [KSR.siptrace.hlog\(\)](#ksrsiptracehlog)
* [KSR.siptrace.hlog_cid\(\)](#ksrsiptracehlog_cid)
* [KSR.siptrace.sip_trace\(\)](#ksrsiptracesip_trace)
* [KSR.siptrace.sip_trace_dst\(\)](#ksrsiptracesip_trace_dst)
* [KSR.siptrace.sip_trace_dst_cid\(\)](#ksrsiptracesip_trace_dst_cid)
* [KSR.siptrace.sip_trace_dst_cid_type\(\)](#ksrsiptracesip_trace_dst_cid_type)
* [KSR.siptrace.sip_trace_mode\(\)](#ksrsiptracesip_trace_mode)
* [KSR.siptrace.sip_trace_msg\(\)](#ksrsiptracesip_trace_msg)

## KSR.siptrace.hlog ##

```cpp
int KSR.siptrace.hlog(str "message");
```

* 📖[kamailio.cfg::function::hlog\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog)

## KSR.siptrace.hlog_cid ##

```cpp
int KSR.siptrace.hlog_cid(str "correlationid", str "message");
```

* 📖[kamailio.cfg::function::hlog_cid\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog_cid)

## KSR.siptrace.sip_trace ##

```cpp
int KSR.siptrace.sip_trace();
```

* 📖[kamailio.cfg::function::sip_trace\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace)

## KSR.siptrace.sip_trace_dst ##

```cpp
int KSR.siptrace.sip_trace_dst(str "duri");
```

* 📖[kamailio.cfg::function::sip_trace_dst\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst)

## KSR.siptrace.sip_trace_dst_cid ##

```cpp
int KSR.siptrace.sip_trace_dst_cid(str "duri", str "cid");
```

* 📖[kamailio.cfg::function::sip_trace_dst_cid\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid)

## KSR.siptrace.sip_trace_dst_cid_type ##

```cpp
int KSR.siptrace.sip_trace_dst_cid_type(str "duri", str "cid", str "sflag");
```

* 📖[kamailio.cfg::function::sip_trace_dst_cid_type\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid_type)

## KSR.siptrace.sip_trace_mode ##

```cpp
int KSR.siptrace.sip_trace_mode(str "smode");
```

* 📖[kamailio.cfg::function::sip_trace_mode\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_mode)

## KSR.siptrace.sip_trace_msg ##

```cpp
int KSR.siptrace.sip_trace_msg(str "vmsg", str "saddr", str "taddr", str "duri", str "corrid");
```

* 📖[kamailio.cfg::function::sip_trace_msg\(\)](https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_msg)
