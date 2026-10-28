# siprepo #

* 📖[kamailio.cfg::module::siprepo.html](https://kamailio.org/docs/modules/devel/modules/siprepo.html)

Exported functions:

* [KSR.siprepo.sr_msg_async_pull\(\)](#ksrsipreposr_msg_async_pull)
* [KSR.siprepo.sr_msg_check\(\)](#ksrsipreposr_msg_check)
* [KSR.siprepo.sr_msg_match\(\)](#ksrsipreposr_msg_match)
* [KSR.siprepo.sr_msg_pull\(\)](#ksrsipreposr_msg_pull)
* [KSR.siprepo.sr_msg_push\(\)](#ksrsipreposr_msg_push)
* [KSR.siprepo.sr_msg_rm\(\)](#ksrsipreposr_msg_rm)

## KSR.siprepo.sr_msg_async_pull ##

```cpp
int KSR.siprepo.sr_msg_async_pull(str "callid", str "msgid", str "gname", str "rname", int rmode);
```

* 📖[kamailio.cfg::function::sr_msg_async_pull\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_async_pull)

## KSR.siprepo.sr_msg_check ##

```cpp
int KSR.siprepo.sr_msg_check();
```

* 📖[kamailio.cfg::function::sr_msg_check\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_check)

## KSR.siprepo.sr_msg_match ##

```cpp
int KSR.siprepo.sr_msg_match(int mode);
```

* 📖[kamailio.cfg::function::sr_msg_match\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_match)

## KSR.siprepo.sr_msg_pull ##

```cpp
int KSR.siprepo.sr_msg_pull(str "callid", str "msgid", str "rname", int rmode);
```

* 📖[kamailio.cfg::function::sr_msg_pull\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_pull)

## KSR.siprepo.sr_msg_push ##

```cpp
int KSR.siprepo.sr_msg_push(str "msgid", int rmode);
```

* 📖[kamailio.cfg::function::sr_msg_push\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_push)

## KSR.siprepo.sr_msg_rm ##

```cpp
int KSR.siprepo.sr_msg_rm(str "callid", str "msgid");
```

* 📖[kamailio.cfg::function::sr_msg_rm\(\)](https://kamailio.org/docs/modules/devel/modules/siprepo.html#siprepo.f.sr_msg_rm)
