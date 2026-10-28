# sl #

* 📖[kamailio.cfg::module::sl.html](https://kamailio.org/docs/modules/devel/modules/sl.html)

Exported functions:

* [KSR.sl.send_reply\(\)](#ksrslsend_reply)
* [KSR.sl.send_reply_error\(\)](#ksrslsend_reply_error)
* [KSR.sl.send_reply_mode\(\)](#ksrslsend_reply_mode)
* [KSR.sl.sl_forward_reply\(\)](#ksrslsl_forward_reply)
* [KSR.sl.sl_reply_error\(\)](#ksrslsl_reply_error)
* [KSR.sl.sl_send_reply\(\)](#ksrslsl_send_reply)

## KSR.sl.send_reply ##

```cpp
int KSR.sl.send_reply(int code, str "reason");
```

* 📖[kamailio.cfg::function::send_reply\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply)

## KSR.sl.send_reply_error ##

```cpp
int KSR.sl.send_reply_error();
```

* 📖[kamailio.cfg::function::send_reply_error\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply_error)

## KSR.sl.send_reply_mode ##

```cpp
int KSR.sl.send_reply_mode(int code, str "reason", int mode);
```

* 📖[kamailio.cfg::function::send_reply_mode\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply_mode)

## KSR.sl.sl_forward_reply ##

```cpp
int KSR.sl.sl_forward_reply(str "code", str "reason");
```

* 📖[kamailio.cfg::function::sl_forward_reply\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_forward_reply)

## KSR.sl.sl_reply_error ##

```cpp
int KSR.sl.sl_reply_error();
```

* 📖[kamailio.cfg::function::sl_reply_error\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_reply_error)

## KSR.sl.sl_send_reply ##

```cpp
int KSR.sl.sl_send_reply(int code, str "reason");
```

* 📖[kamailio.cfg::function::sl_send_reply\(\)](https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_send_reply)
