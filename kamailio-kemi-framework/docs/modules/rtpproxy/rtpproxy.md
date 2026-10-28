# rtpproxy #

* 📖[kamailio.cfg::module::rtpproxy.html](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html)

Exported functions:

* [KSR.rtpproxy.rtpproxy_answer\(\)](#ksrrtpproxyrtpproxy_answer)
* [KSR.rtpproxy.rtpproxy_answer0\(\)](#ksrrtpproxyrtpproxy_answer0)
* [KSR.rtpproxy.rtpproxy_answer_ip\(\)](#ksrrtpproxyrtpproxy_answer_ip)
* [KSR.rtpproxy.rtpproxy_destroy\(\)](#ksrrtpproxyrtpproxy_destroy)
* [KSR.rtpproxy.rtpproxy_destroy0\(\)](#ksrrtpproxyrtpproxy_destroy0)
* [KSR.rtpproxy.rtpproxy_manage\(\)](#ksrrtpproxyrtpproxy_manage)
* [KSR.rtpproxy.rtpproxy_manage0\(\)](#ksrrtpproxyrtpproxy_manage0)
* [KSR.rtpproxy.rtpproxy_manage_ip\(\)](#ksrrtpproxyrtpproxy_manage_ip)
* [KSR.rtpproxy.rtpproxy_offer\(\)](#ksrrtpproxyrtpproxy_offer)
* [KSR.rtpproxy.rtpproxy_offer0\(\)](#ksrrtpproxyrtpproxy_offer0)
* [KSR.rtpproxy.rtpproxy_offer_ip\(\)](#ksrrtpproxyrtpproxy_offer_ip)
* [KSR.rtpproxy.rtpproxy_stop_stream2uac\(\)](#ksrrtpproxyrtpproxy_stop_stream2uac)
* [KSR.rtpproxy.rtpproxy_stop_stream2uas\(\)](#ksrrtpproxyrtpproxy_stop_stream2uas)
* [KSR.rtpproxy.rtpproxy_stream2uac\(\)](#ksrrtpproxyrtpproxy_stream2uac)
* [KSR.rtpproxy.rtpproxy_stream2uas\(\)](#ksrrtpproxyrtpproxy_stream2uas)
* [KSR.rtpproxy.set_rtpproxy_set\(\)](#ksrrtpproxyset_rtpproxy_set)
* [KSR.rtpproxy.start_recording\(\)](#ksrrtpproxystart_recording)

## KSR.rtpproxy.rtpproxy_answer ##

```cpp
int KSR.rtpproxy.rtpproxy_answer(str "flags");
```

* 📖[kamailio.cfg::function::rtpproxy_answer\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer)

## KSR.rtpproxy.rtpproxy_answer0 ##

```cpp
int KSR.rtpproxy.rtpproxy_answer0();
```

* 📖[kamailio.cfg::function::rtpproxy_answer0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer0)

## KSR.rtpproxy.rtpproxy_answer_ip ##

```cpp
int KSR.rtpproxy.rtpproxy_answer_ip(str "flags", str "mip");
```

* 📖[kamailio.cfg::function::rtpproxy_answer_ip\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer_ip)

## KSR.rtpproxy.rtpproxy_destroy ##

```cpp
int KSR.rtpproxy.rtpproxy_destroy(str "flags");
```

* 📖[kamailio.cfg::function::rtpproxy_destroy\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy)

## KSR.rtpproxy.rtpproxy_destroy0 ##

```cpp
int KSR.rtpproxy.rtpproxy_destroy0();
```

* 📖[kamailio.cfg::function::rtpproxy_destroy0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy0)

## KSR.rtpproxy.rtpproxy_manage ##

```cpp
int KSR.rtpproxy.rtpproxy_manage(str "flags");
```

* 📖[kamailio.cfg::function::rtpproxy_manage\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage)

## KSR.rtpproxy.rtpproxy_manage0 ##

```cpp
int KSR.rtpproxy.rtpproxy_manage0();
```

* 📖[kamailio.cfg::function::rtpproxy_manage0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage0)

## KSR.rtpproxy.rtpproxy_manage_ip ##

```cpp
int KSR.rtpproxy.rtpproxy_manage_ip(str "flags", str "mip");
```

* 📖[kamailio.cfg::function::rtpproxy_manage_ip\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage_ip)

## KSR.rtpproxy.rtpproxy_offer ##

```cpp
int KSR.rtpproxy.rtpproxy_offer(str "flags");
```

* 📖[kamailio.cfg::function::rtpproxy_offer\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer)

## KSR.rtpproxy.rtpproxy_offer0 ##

```cpp
int KSR.rtpproxy.rtpproxy_offer0();
```

* 📖[kamailio.cfg::function::rtpproxy_offer0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer0)

## KSR.rtpproxy.rtpproxy_offer_ip ##

```cpp
int KSR.rtpproxy.rtpproxy_offer_ip(str "flags", str "mip");
```

* 📖[kamailio.cfg::function::rtpproxy_offer_ip\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer_ip)

## KSR.rtpproxy.rtpproxy_stop_stream2uac ##

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uac();
```

* 📖[kamailio.cfg::function::rtpproxy_stop_stream2uac\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uac)

## KSR.rtpproxy.rtpproxy_stop_stream2uas ##

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uas();
```

* 📖[kamailio.cfg::function::rtpproxy_stop_stream2uas\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uas)

## KSR.rtpproxy.rtpproxy_stream2uac ##

```cpp
int KSR.rtpproxy.rtpproxy_stream2uac(str "pname", int count);
```

* 📖[kamailio.cfg::function::rtpproxy_stream2uac\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uac)

## KSR.rtpproxy.rtpproxy_stream2uas ##

```cpp
int KSR.rtpproxy.rtpproxy_stream2uas(str "pname", int count);
```

* 📖[kamailio.cfg::function::rtpproxy_stream2uas\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uas)

## KSR.rtpproxy.set_rtpproxy_set ##

```cpp
int KSR.rtpproxy.set_rtpproxy_set(int rset);
```

* 📖[kamailio.cfg::function::set_rtpproxy_set\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.set_rtpproxy_set)

## KSR.rtpproxy.start_recording ##

```cpp
int KSR.rtpproxy.start_recording();
```

* 📖[kamailio.cfg::function::start_recording\(\)](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.start_recording)
