# rtpengine #

* 📖[kamailio.cfg::module::rtpengine.html](https://kamailio.org/docs/modules/devel/modules/rtpengine.html)

This module enables media streams to be proxied via RTPEngine, exporting
the functions to interact with it.

Exported functions:

* [KSR.rtpengine.block_dtmf\(\)](#ksrrtpengineblock_dtmf)
* [KSR.rtpengine.block_dtmf0\(\)](#ksrrtpengineblock_dtmf0)
* [KSR.rtpengine.block_dtmf2\(\)](#ksrrtpengineblock_dtmf2)
* [KSR.rtpengine.block_media\(\)](#ksrrtpengineblock_media)
* [KSR.rtpengine.block_media0\(\)](#ksrrtpengineblock_media0)
* [KSR.rtpengine.block_media2\(\)](#ksrrtpengineblock_media2)
* [KSR.rtpengine.play_dtmf\(\)](#ksrrtpengineplay_dtmf)
* [KSR.rtpengine.play_media\(\)](#ksrrtpengineplay_media)
* [KSR.rtpengine.play_media2\(\)](#ksrrtpengineplay_media2)
* [KSR.rtpengine.rtpengine_answer\(\)](#ksrrtpenginertpengine_answer)
* [KSR.rtpengine.rtpengine_answer0\(\)](#ksrrtpenginertpengine_answer0)
* [KSR.rtpengine.rtpengine_answer2\(\)](#ksrrtpenginertpengine_answer2)
* [KSR.rtpengine.rtpengine_connect\(\)](#ksrrtpenginertpengine_connect)
* [KSR.rtpengine.rtpengine_connect0\(\)](#ksrrtpenginertpengine_connect0)
* [KSR.rtpengine.rtpengine_connect2\(\)](#ksrrtpenginertpengine_connect2)
* [KSR.rtpengine.rtpengine_delete\(\)](#ksrrtpenginertpengine_delete)
* [KSR.rtpengine.rtpengine_delete0\(\)](#ksrrtpenginertpengine_delete0)
* [KSR.rtpengine.rtpengine_delete2\(\)](#ksrrtpenginertpengine_delete2)
* [KSR.rtpengine.rtpengine_manage\(\)](#ksrrtpenginertpengine_manage)
* [KSR.rtpengine.rtpengine_manage0\(\)](#ksrrtpenginertpengine_manage0)
* [KSR.rtpengine.rtpengine_manage2\(\)](#ksrrtpenginertpengine_manage2)
* [KSR.rtpengine.rtpengine_offer\(\)](#ksrrtpenginertpengine_offer)
* [KSR.rtpengine.rtpengine_offer0\(\)](#ksrrtpenginertpengine_offer0)
* [KSR.rtpengine.rtpengine_offer2\(\)](#ksrrtpenginertpengine_offer2)
* [KSR.rtpengine.rtpengine_query\(\)](#ksrrtpenginertpengine_query)
* [KSR.rtpengine.rtpengine_query0\(\)](#ksrrtpenginertpengine_query0)
* [KSR.rtpengine.rtpengine_query2\(\)](#ksrrtpenginertpengine_query2)
* [KSR.rtpengine.rtpengine_query_v\(\)](#ksrrtpenginertpengine_query_v)
* [KSR.rtpengine.rtpengine_subscribe_answer\(\)](#ksrrtpenginertpengine_subscribe_answer)
* [KSR.rtpengine.rtpengine_subscribe_request\(\)](#ksrrtpenginertpengine_subscribe_request)
* [KSR.rtpengine.rtpengine_unsubscribe\(\)](#ksrrtpenginertpengine_unsubscribe)
* [KSR.rtpengine.set_rtpengine_set\(\)](#ksrrtpengineset_rtpengine_set)
* [KSR.rtpengine.set_rtpengine_set2\(\)](#ksrrtpengineset_rtpengine_set2)
* [KSR.rtpengine.silence_media\(\)](#ksrrtpenginesilence_media)
* [KSR.rtpengine.silence_media0\(\)](#ksrrtpenginesilence_media0)
* [KSR.rtpengine.silence_media2\(\)](#ksrrtpenginesilence_media2)
* [KSR.rtpengine.start_forwarding\(\)](#ksrrtpenginestart_forwarding)
* [KSR.rtpengine.start_forwarding0\(\)](#ksrrtpenginestart_forwarding0)
* [KSR.rtpengine.start_forwarding2\(\)](#ksrrtpenginestart_forwarding2)
* [KSR.rtpengine.start_recording\(\)](#ksrrtpenginestart_recording)
* [KSR.rtpengine.stop_forwarding\(\)](#ksrrtpenginestop_forwarding)
* [KSR.rtpengine.stop_forwarding0\(\)](#ksrrtpenginestop_forwarding0)
* [KSR.rtpengine.stop_forwarding2\(\)](#ksrrtpenginestop_forwarding2)
* [KSR.rtpengine.stop_media\(\)](#ksrrtpenginestop_media)
* [KSR.rtpengine.stop_media0\(\)](#ksrrtpenginestop_media0)
* [KSR.rtpengine.stop_media2\(\)](#ksrrtpenginestop_media2)
* [KSR.rtpengine.stop_recording\(\)](#ksrrtpenginestop_recording)
* [KSR.rtpengine.unblock_dtmf\(\)](#ksrrtpengineunblock_dtmf)
* [KSR.rtpengine.unblock_dtmf0\(\)](#ksrrtpengineunblock_dtmf0)
* [KSR.rtpengine.unblock_dtmf2\(\)](#ksrrtpengineunblock_dtmf2)
* [KSR.rtpengine.unblock_media\(\)](#ksrrtpengineunblock_media)
* [KSR.rtpengine.unblock_media0\(\)](#ksrrtpengineunblock_media0)
* [KSR.rtpengine.unblock_media2\(\)](#ksrrtpengineunblock_media2)
* [KSR.rtpengine.unsilence_media\(\)](#ksrrtpengineunsilence_media)
* [KSR.rtpengine.unsilence_media0\(\)](#ksrrtpengineunsilence_media0)
* [KSR.rtpengine.unsilence_media2\(\)](#ksrrtpengineunsilence_media2)

## KSR.rtpengine.block_dtmf ##

```cpp
int KSR.rtpengine.block_dtmf(str "flags");
```

* 📖[kamailio.cfg::function::block_dtmf\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf)

## KSR.rtpengine.block_dtmf0 ##

```cpp
int KSR.rtpengine.block_dtmf0();
```

* 📖[kamailio.cfg::function::block_dtmf0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf0)

## KSR.rtpengine.block_dtmf2 ##

```cpp
int KSR.rtpengine.block_dtmf2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::block_dtmf2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf2)

## KSR.rtpengine.block_media ##

```cpp
int KSR.rtpengine.block_media(str "flags");
```

* 📖[kamailio.cfg::function::block_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media)

## KSR.rtpengine.block_media0 ##

```cpp
int KSR.rtpengine.block_media0();
```

* 📖[kamailio.cfg::function::block_media0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media0)

## KSR.rtpengine.block_media2 ##

```cpp
int KSR.rtpengine.block_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::block_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media2)

## KSR.rtpengine.play_dtmf ##

```cpp
int KSR.rtpengine.play_dtmf(str "flags");
```

* 📖[kamailio.cfg::function::play_dtmf\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.play_dtmf)

## KSR.rtpengine.play_media ##

```cpp
int KSR.rtpengine.play_media(str "flags");
```

* 📖[kamailio.cfg::function::play_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.play_media)

## KSR.rtpengine.play_media2 ##

```cpp
int KSR.rtpengine.play_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::play_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.play_media2)

## KSR.rtpengine.rtpengine_answer ##

```cpp
int KSR.rtpengine.rtpengine_answer(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_answer\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer)

## KSR.rtpengine.rtpengine_answer0 ##

```cpp
int KSR.rtpengine.rtpengine_answer0();
```

* 📖[kamailio.cfg::function::rtpengine_answer0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer0)

## KSR.rtpengine.rtpengine_answer2 ##

```cpp
int KSR.rtpengine.rtpengine_answer2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_answer2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer2)

## KSR.rtpengine.rtpengine_connect ##

```cpp
int KSR.rtpengine.rtpengine_connect(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_connect\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_connect)

## KSR.rtpengine.rtpengine_connect0 ##

```cpp
int KSR.rtpengine.rtpengine_connect0();
```

* 📖[kamailio.cfg::function::rtpengine_connect0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_connect0)

## KSR.rtpengine.rtpengine_connect2 ##

```cpp
int KSR.rtpengine.rtpengine_connect2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_connect2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_connect2)

## KSR.rtpengine.rtpengine_delete ##

```cpp
int KSR.rtpengine.rtpengine_delete(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_delete\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete)

## KSR.rtpengine.rtpengine_delete0 ##

```cpp
int KSR.rtpengine.rtpengine_delete0();
```

* 📖[kamailio.cfg::function::rtpengine_delete0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete0)

## KSR.rtpengine.rtpengine_delete2 ##

```cpp
int KSR.rtpengine.rtpengine_delete2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_delete2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete2)

## KSR.rtpengine.rtpengine_manage ##

```cpp
int KSR.rtpengine.rtpengine_manage(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_manage\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage)

## KSR.rtpengine.rtpengine_manage0 ##

```cpp
int KSR.rtpengine.rtpengine_manage0();
```

* 📖[kamailio.cfg::function::rtpengine_manage0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage0)

## KSR.rtpengine.rtpengine_manage2 ##

```cpp
int KSR.rtpengine.rtpengine_manage2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_manage2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage2)

## KSR.rtpengine.rtpengine_offer ##

```cpp
int KSR.rtpengine.rtpengine_offer(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_offer\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer)

## KSR.rtpengine.rtpengine_offer0 ##

```cpp
int KSR.rtpengine.rtpengine_offer0();
```

* 📖[kamailio.cfg::function::rtpengine_offer0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer0)

## KSR.rtpengine.rtpengine_offer2 ##

```cpp
int KSR.rtpengine.rtpengine_offer2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_offer2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer2)

## KSR.rtpengine.rtpengine_query ##

```cpp
int KSR.rtpengine.rtpengine_query(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_query\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query)

## KSR.rtpengine.rtpengine_query0 ##

```cpp
int KSR.rtpengine.rtpengine_query0();
```

* 📖[kamailio.cfg::function::rtpengine_query0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query0)

## KSR.rtpengine.rtpengine_query2 ##

```cpp
int KSR.rtpengine.rtpengine_query2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::rtpengine_query2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query2)

## KSR.rtpengine.rtpengine_query_v ##

```cpp
int KSR.rtpengine.rtpengine_query_v(str "fmt", str "dpv");
```

* 📖[kamailio.cfg::function::rtpengine_query_v\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query_v)

## KSR.rtpengine.rtpengine_subscribe_answer ##

```cpp
int KSR.rtpengine.rtpengine_subscribe_answer(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_subscribe_answer\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_subscribe_answer)

## KSR.rtpengine.rtpengine_subscribe_request ##

```cpp
int KSR.rtpengine.rtpengine_subscribe_request(str "flags", str "sdp_spv", str "to_tag_spv", str "stream_xavp");
```

* 📖[kamailio.cfg::function::rtpengine_subscribe_request\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_subscribe_request)

## KSR.rtpengine.rtpengine_unsubscribe ##

```cpp
int KSR.rtpengine.rtpengine_unsubscribe(str "flags");
```

* 📖[kamailio.cfg::function::rtpengine_unsubscribe\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_unsubscribe)

## KSR.rtpengine.set_rtpengine_set ##

```cpp
int KSR.rtpengine.set_rtpengine_set(int r1);
```

* 📖[kamailio.cfg::function::set_rtpengine_set\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set)

## KSR.rtpengine.set_rtpengine_set2 ##

```cpp
int KSR.rtpengine.set_rtpengine_set2(int r1, int r2);
```

* 📖[kamailio.cfg::function::set_rtpengine_set2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set2)

This function is the sibling function to [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set). The original module function is declared as
`set_rtpengine_set(setid[, setid2])`.

In KEMI set_rtpengine_set() takes only the first parameter and set_rtpengine_set2() allows for the second optional parameter to be passed.

```
KSR.rtpengine.set_rtpengine_set2(2, 1);
KSR.rtpengine.rtpengine_offer();
```

Please review the documentation for [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set) for more information.

## KSR.rtpengine.silence_media ##

```cpp
int KSR.rtpengine.silence_media(str "flags");
```

* 📖[kamailio.cfg::function::silence_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.silence_media)

## KSR.rtpengine.silence_media0 ##

```cpp
int KSR.rtpengine.silence_media0();
```

* 📖[kamailio.cfg::function::silence_media0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.silence_media0)

## KSR.rtpengine.silence_media2 ##

```cpp
int KSR.rtpengine.silence_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::silence_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.silence_media2)

## KSR.rtpengine.start_forwarding ##

```cpp
int KSR.rtpengine.start_forwarding(str "flags");
```

* 📖[kamailio.cfg::function::start_forwarding\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_forwarding)

## KSR.rtpengine.start_forwarding0 ##

```cpp
int KSR.rtpengine.start_forwarding0();
```

* 📖[kamailio.cfg::function::start_forwarding0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_forwarding0)

## KSR.rtpengine.start_forwarding2 ##

```cpp
int KSR.rtpengine.start_forwarding2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::start_forwarding2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_forwarding2)

## KSR.rtpengine.start_recording ##

```cpp
int KSR.rtpengine.start_recording();
```

* 📖[kamailio.cfg::function::start_recording\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_recording)

## KSR.rtpengine.stop_forwarding ##

```cpp
int KSR.rtpengine.stop_forwarding(str "flags");
```

* 📖[kamailio.cfg::function::stop_forwarding\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_forwarding)

## KSR.rtpengine.stop_forwarding0 ##

```cpp
int KSR.rtpengine.stop_forwarding0();
```

* 📖[kamailio.cfg::function::stop_forwarding0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_forwarding0)

## KSR.rtpengine.stop_forwarding2 ##

```cpp
int KSR.rtpengine.stop_forwarding2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::stop_forwarding2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_forwarding2)

## KSR.rtpengine.stop_media ##

```cpp
int KSR.rtpengine.stop_media(str "flags");
```

* 📖[kamailio.cfg::function::stop_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media)

## KSR.rtpengine.stop_media0 ##

```cpp
int KSR.rtpengine.stop_media0();
```

* 📖[kamailio.cfg::function::stop_media0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media0)

## KSR.rtpengine.stop_media2 ##

```cpp
int KSR.rtpengine.stop_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::stop_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media2)

## KSR.rtpengine.stop_recording ##

```cpp
int KSR.rtpengine.stop_recording();
```

* 📖[kamailio.cfg::function::stop_recording\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_recording)

## KSR.rtpengine.unblock_dtmf ##

```cpp
int KSR.rtpengine.unblock_dtmf(str "flags");
```

* 📖[kamailio.cfg::function::unblock_dtmf\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf)

## KSR.rtpengine.unblock_dtmf0 ##

```cpp
int KSR.rtpengine.unblock_dtmf0();
```

* 📖[kamailio.cfg::function::unblock_dtmf0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf0)

## KSR.rtpengine.unblock_dtmf2 ##

```cpp
int KSR.rtpengine.unblock_dtmf2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::unblock_dtmf2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf2)

## KSR.rtpengine.unblock_media ##

```cpp
int KSR.rtpengine.unblock_media(str "flags");
```

* 📖[kamailio.cfg::function::unblock_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media)

## KSR.rtpengine.unblock_media0 ##

```cpp
int KSR.rtpengine.unblock_media0();
```

* 📖[kamailio.cfg::function::unblock_media0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media0)

## KSR.rtpengine.unblock_media2 ##

```cpp
int KSR.rtpengine.unblock_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::unblock_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media2)

## KSR.rtpengine.unsilence_media ##

```cpp
int KSR.rtpengine.unsilence_media(str "flags");
```

* 📖[kamailio.cfg::function::unsilence_media\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unsilence_media)

## KSR.rtpengine.unsilence_media0 ##

```cpp
int KSR.rtpengine.unsilence_media0();
```

* 📖[kamailio.cfg::function::unsilence_media0\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unsilence_media0)

## KSR.rtpengine.unsilence_media2 ##

```cpp
int KSR.rtpengine.unsilence_media2(str "flags", str "viabranch");
```

* 📖[kamailio.cfg::function::unsilence_media2\(\)](https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unsilence_media2)
