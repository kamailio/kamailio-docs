# tmx #

* 📖[kamailio.cfg::module::tmx.html](https://kamailio.org/docs/modules/devel/modules/tmx.html)

Exported functions:

* [KSR.tmx.t_cancel_branches\(\)](#ksrtmxt_cancel_branches)
* [KSR.tmx.t_cancel_callid\(\)](#ksrtmxt_cancel_callid)
* [KSR.tmx.t_cancel_callid_reason\(\)](#ksrtmxt_cancel_callid_reason)
* [KSR.tmx.t_continue\(\)](#ksrtmxt_continue)
* [KSR.tmx.t_drop\(\)](#ksrtmxt_drop)
* [KSR.tmx.t_drop_rcode\(\)](#ksrtmxt_drop_rcode)
* [KSR.tmx.t_flush_flags\(\)](#ksrtmxt_flush_flags)
* [KSR.tmx.t_flush_xflags\(\)](#ksrtmxt_flush_xflags)
* [KSR.tmx.t_is_branch_route\(\)](#ksrtmxt_is_branch_route)
* [KSR.tmx.t_is_failure_route\(\)](#ksrtmxt_is_failure_route)
* [KSR.tmx.t_is_reply_route\(\)](#ksrtmxt_is_reply_route)
* [KSR.tmx.t_is_request_route\(\)](#ksrtmxt_is_request_route)
* [KSR.tmx.t_precheck_trans\(\)](#ksrtmxt_precheck_trans)
* [KSR.tmx.t_reply_callid\(\)](#ksrtmxt_reply_callid)
* [KSR.tmx.t_reuse_branch\(\)](#ksrtmxt_reuse_branch)
* [KSR.tmx.t_suspend\(\)](#ksrtmxt_suspend)
* [KSR.tmx.t_uac_ack_local\(\)](#ksrtmxt_uac_ack_local)

## KSR.tmx.t_cancel_branches ##

```cpp
int KSR.tmx.t_cancel_branches(str "mode");
```

* 📖[kamailio.cfg::function::t_cancel_branches\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_branches)

## KSR.tmx.t_cancel_callid ##

```cpp
int KSR.tmx.t_cancel_callid(str "callid_s", str "cseq_s", int fl);
```

* 📖[kamailio.cfg::function::t_cancel_callid\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid)

## KSR.tmx.t_cancel_callid_reason ##

```cpp
int KSR.tmx.t_cancel_callid_reason(str "callid_s", str "cseq_s", int fl, int rcode);
```

* 📖[kamailio.cfg::function::t_cancel_callid_reason\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid_reason)

## KSR.tmx.t_continue ##

```cpp
int KSR.tmx.t_continue(int tindex, int tlabel, str "cbname");
```

* 📖[kamailio.cfg::function::t_continue\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_continue)

## KSR.tmx.t_drop ##

```cpp
int KSR.tmx.t_drop();
```

* 📖[kamailio.cfg::function::t_drop\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop)

## KSR.tmx.t_drop_rcode ##

```cpp
int KSR.tmx.t_drop_rcode(int rcode);
```

* 📖[kamailio.cfg::function::t_drop_rcode\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop_rcode)

## KSR.tmx.t_flush_flags ##

```cpp
int KSR.tmx.t_flush_flags();
```

* 📖[kamailio.cfg::function::t_flush_flags\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_flags)

## KSR.tmx.t_flush_xflags ##

```cpp
int KSR.tmx.t_flush_xflags();
```

* 📖[kamailio.cfg::function::t_flush_xflags\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_xflags)

## KSR.tmx.t_is_branch_route ##

```cpp
int KSR.tmx.t_is_branch_route();
```

* 📖[kamailio.cfg::function::t_is_branch_route\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_branch_route)

## KSR.tmx.t_is_failure_route ##

```cpp
int KSR.tmx.t_is_failure_route();
```

* 📖[kamailio.cfg::function::t_is_failure_route\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_failure_route)

## KSR.tmx.t_is_reply_route ##

```cpp
int KSR.tmx.t_is_reply_route();
```

* 📖[kamailio.cfg::function::t_is_reply_route\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_reply_route)

## KSR.tmx.t_is_request_route ##

```cpp
int KSR.tmx.t_is_request_route();
```

* 📖[kamailio.cfg::function::t_is_request_route\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_request_route)

## KSR.tmx.t_precheck_trans ##

```cpp
int KSR.tmx.t_precheck_trans();
```

* 📖[kamailio.cfg::function::t_precheck_trans\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_precheck_trans)

## KSR.tmx.t_reply_callid ##

```cpp
int KSR.tmx.t_reply_callid(str "callid_s", str "cseq_s", int code, str "status_s");
```

* 📖[kamailio.cfg::function::t_reply_callid\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reply_callid)

## KSR.tmx.t_reuse_branch ##

```cpp
int KSR.tmx.t_reuse_branch();
```

* 📖[kamailio.cfg::function::t_reuse_branch\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reuse_branch)

## KSR.tmx.t_suspend ##

```cpp
int KSR.tmx.t_suspend();
```

* 📖[kamailio.cfg::function::t_suspend\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_suspend)

## KSR.tmx.t_uac_ack_local ##

```cpp
int KSR.tmx.t_uac_ack_local(str "callid_s", str "cseq_s", str "hdrs", str "body");
```

* 📖[kamailio.cfg::function::t_uac_ack_local\(\)](https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_uac_ack_local)
