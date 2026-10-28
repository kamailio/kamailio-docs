# sipcapture #

* 📖[kamailio.cfg::module::sipcapture.html](https://kamailio.org/docs/modules/devel/modules/sipcapture.html)

Exported functions:

* [KSR.sipcapture.float2int\(\)](#ksrsipcapturefloat2int)
* [KSR.sipcapture.report_capture\(\)](#ksrsipcapturereport_capture)
* [KSR.sipcapture.report_capture_cid\(\)](#ksrsipcapturereport_capture_cid)
* [KSR.sipcapture.report_capture_data\(\)](#ksrsipcapturereport_capture_data)
* [KSR.sipcapture.sip_capture\(\)](#ksrsipcapturesip_capture)
* [KSR.sipcapture.sip_capture_forward\(\)](#ksrsipcapturesip_capture_forward)
* [KSR.sipcapture.sip_capture_mode\(\)](#ksrsipcapturesip_capture_mode)
* [KSR.sipcapture.sip_capture_table\(\)](#ksrsipcapturesip_capture_table)

## KSR.sipcapture.float2int ##

```cpp
int KSR.sipcapture.float2int(str "_val", str "_coof");
```

* 📖[kamailio.cfg::function::float2int\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.float2int)

## KSR.sipcapture.report_capture ##

```cpp
int KSR.sipcapture.report_capture(str "_table");
```

* 📖[kamailio.cfg::function::report_capture\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture)

## KSR.sipcapture.report_capture_cid ##

```cpp
int KSR.sipcapture.report_capture_cid(str "_table", str "_cid");
```

* 📖[kamailio.cfg::function::report_capture_cid\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_cid)

## KSR.sipcapture.report_capture_data ##

```cpp
int KSR.sipcapture.report_capture_data(str "_table", str "_cid", str "_data");
```

* 📖[kamailio.cfg::function::report_capture_data\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_data)

## KSR.sipcapture.sip_capture ##

```cpp
int KSR.sipcapture.sip_capture();
```

* 📖[kamailio.cfg::function::sip_capture\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture)

## KSR.sipcapture.sip_capture_forward ##

```cpp
int KSR.sipcapture.sip_capture_forward(str "puri");
```

* 📖[kamailio.cfg::function::sip_capture_forward\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_forward)

## KSR.sipcapture.sip_capture_mode ##

```cpp
int KSR.sipcapture.sip_capture_mode(str "_table", str "_cmdata");
```

* 📖[kamailio.cfg::function::sip_capture_mode\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_mode)

## KSR.sipcapture.sip_capture_table ##

```cpp
int KSR.sipcapture.sip_capture_table(str "_table");
```

* 📖[kamailio.cfg::function::sip_capture_table\(\)](https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_table)
