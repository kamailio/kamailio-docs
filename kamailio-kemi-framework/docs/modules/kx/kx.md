# kx #

* 📖[kamailio.cfg::module::kemi.html](https://kamailio.org/docs/modules/devel/modules/kemi.html)

Functions exported by `kemix` module and available in KEMI language under
`KSR.kx`. They aim to provide a convenient way to retrieve string or integer
values for most commonly used variables or runtime environment attributes.

Exported functions:

* [KSR.kx.get_au\(\)](#ksrkxget_au)
* [KSR.kx.get_body\(\)](#ksrkxget_body)
* [KSR.kx.get_bodylen\(\)](#ksrkxget_bodylen)
* [KSR.kx.get_callid\(\)](#ksrkxget_callid)
* [KSR.kx.get_conid\(\)](#ksrkxget_conid)
* [KSR.kx.get_cturi\(\)](#ksrkxget_cturi)
* [KSR.kx.get_def\(\)](#ksrkxget_def)
* [KSR.kx.get_defn\(\)](#ksrkxget_defn)
* [KSR.kx.get_duri\(\)](#ksrkxget_duri)
* [KSR.kx.get_env\(\)](#ksrkxget_env)
* [KSR.kx.get_envn\(\)](#ksrkxget_envn)
* [KSR.kx.get_fhost\(\)](#ksrkxget_fhost)
* [KSR.kx.get_furi\(\)](#ksrkxget_furi)
* [KSR.kx.get_fuser\(\)](#ksrkxget_fuser)
* [KSR.kx.get_method\(\)](#ksrkxget_method)
* [KSR.kx.get_msgbuf\(\)](#ksrkxget_msgbuf)
* [KSR.kx.get_msglen\(\)](#ksrkxget_msglen)
* [KSR.kx.get_msgtype\(\)](#ksrkxget_msgtype)
* [KSR.kx.get_nhuri\(\)](#ksrkxget_nhuri)
* [KSR.kx.get_ouri\(\)](#ksrkxget_ouri)
* [KSR.kx.get_proto\(\)](#ksrkxget_proto)
* [KSR.kx.get_protoid\(\)](#ksrkxget_protoid)
* [KSR.kx.get_rcv_sock_name\(\)](#ksrkxget_rcv_sock_name)
* [KSR.kx.get_rcvaddr_sock\(\)](#ksrkxget_rcvaddr_sock)
* [KSR.kx.get_rcvadvip\(\)](#ksrkxget_rcvadvip)
* [KSR.kx.get_rcvadvport\(\)](#ksrkxget_rcvadvport)
* [KSR.kx.get_rcvip\(\)](#ksrkxget_rcvip)
* [KSR.kx.get_rcvport\(\)](#ksrkxget_rcvport)
* [KSR.kx.get_rhost\(\)](#ksrkxget_rhost)
* [KSR.kx.get_ruri\(\)](#ksrkxget_ruri)
* [KSR.kx.get_ruser\(\)](#ksrkxget_ruser)
* [KSR.kx.get_send_sock\(\)](#ksrkxget_send_sock)
* [KSR.kx.get_send_sock_name\(\)](#ksrkxget_send_sock_name)
* [KSR.kx.get_send_sock_port\(\)](#ksrkxget_send_sock_port)
* [KSR.kx.get_srcaddr_sock\(\)](#ksrkxget_srcaddr_sock)
* [KSR.kx.get_srcip\(\)](#ksrkxget_srcip)
* [KSR.kx.get_srcport\(\)](#ksrkxget_srcport)
* [KSR.kx.get_srcuri\(\)](#ksrkxget_srcuri)
* [KSR.kx.get_status\(\)](#ksrkxget_status)
* [KSR.kx.get_thost\(\)](#ksrkxget_thost)
* [KSR.kx.get_timestamp\(\)](#ksrkxget_timestamp)
* [KSR.kx.get_turi\(\)](#ksrkxget_turi)
* [KSR.kx.get_tuser\(\)](#ksrkxget_tuser)
* [KSR.kx.get_ua\(\)](#ksrkxget_ua)
* [KSR.kx.gete_au\(\)](#ksrkxgete_au)
* [KSR.kx.gete_body\(\)](#ksrkxgete_body)
* [KSR.kx.gete_cturi\(\)](#ksrkxgete_cturi)
* [KSR.kx.gete_duri\(\)](#ksrkxgete_duri)
* [KSR.kx.gete_fhost\(\)](#ksrkxgete_fhost)
* [KSR.kx.gete_fuser\(\)](#ksrkxgete_fuser)
* [KSR.kx.gete_rhost\(\)](#ksrkxgete_rhost)
* [KSR.kx.gete_ruser\(\)](#ksrkxgete_ruser)
* [KSR.kx.gete_thost\(\)](#ksrkxgete_thost)
* [KSR.kx.gete_tuser\(\)](#ksrkxgete_tuser)
* [KSR.kx.gete_ua\(\)](#ksrkxgete_ua)
* [KSR.kx.gets_status\(\)](#ksrkxgets_status)
* [KSR.kx.getw_au\(\)](#ksrkxgetw_au)
* [KSR.kx.getw_body\(\)](#ksrkxgetw_body)
* [KSR.kx.getw_cturi\(\)](#ksrkxgetw_cturi)
* [KSR.kx.getw_duri\(\)](#ksrkxgetw_duri)
* [KSR.kx.getw_fhost\(\)](#ksrkxgetw_fhost)
* [KSR.kx.getw_fuser\(\)](#ksrkxgetw_fuser)
* [KSR.kx.getw_rhost\(\)](#ksrkxgetw_rhost)
* [KSR.kx.getw_ruser\(\)](#ksrkxgetw_ruser)
* [KSR.kx.getw_thost\(\)](#ksrkxgetw_thost)
* [KSR.kx.getw_tuser\(\)](#ksrkxgetw_tuser)
* [KSR.kx.getw_ua\(\)](#ksrkxgetw_ua)
* [KSR.kx.ifdef\(\)](#ksrkxifdef)
* [KSR.kx.ifndef\(\)](#ksrkxifndef)

## KSR.kx.get_au ##

```cpp
xval KSR.kx.get_au();
```

* 📖[kamailio.cfg::function::get_au\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_au)

## KSR.kx.get_body ##

```cpp
xval KSR.kx.get_body();
```

* 📖[kamailio.cfg::function::get_body\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_body)

Return the body of the SIP message (the value of $rb).

## KSR.kx.get_bodylen ##

```cpp
int KSR.kx.get_bodylen();
```

* 📖[kamailio.cfg::function::get_bodylen\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_bodylen)

## KSR.kx.get_callid ##

```cpp
xval KSR.kx.get_callid();
```

* 📖[kamailio.cfg::function::get_callid\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_callid)

## KSR.kx.get_conid ##

```cpp
int KSR.kx.get_conid();
```

* 📖[kamailio.cfg::function::get_conid\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_conid)

Return the connection id for TCP, TLS and WebSocket, or -1 if no stream connection corresponds to current SIP message.

## KSR.kx.get_cturi ##

```cpp
xval KSR.kx.get_cturi();
```

* 📖[kamailio.cfg::function::get_cturi\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_cturi)

## KSR.kx.get_def ##

```cpp
xval KSR.kx.get_def(str "dname");
```

* 📖[kamailio.cfg::function::get_def\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_def)

## KSR.kx.get_defn ##

```cpp
int KSR.kx.get_defn(str "dname");
```

* 📖[kamailio.cfg::function::get_defn\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_defn)

## KSR.kx.get_duri ##

```cpp
xval KSR.kx.get_duri();
```

* 📖[kamailio.cfg::function::get_duri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_duri)

Return the value of destination URI ($du).

## KSR.kx.get_env ##

```cpp
xval KSR.kx.get_env(str "envname");
```

* 📖[kamailio.cfg::function::get_env\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_env)

## KSR.kx.get_envn ##

```cpp
int KSR.kx.get_envn(str "envname");
```

* 📖[kamailio.cfg::function::get_envn\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_envn)

## KSR.kx.get_fhost ##

```cpp
xval KSR.kx.get_fhost();
```

* 📖[kamailio.cfg::function::get_fhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_fhost)

Return From-URI domain ($fd).

## KSR.kx.get_furi ##

```cpp
xval KSR.kx.get_furi();
```

* 📖[kamailio.cfg::function::get_furi\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_furi)

Return the From URI($fu).

## KSR.kx.get_fuser ##

```cpp
xval KSR.kx.get_fuser();
```

* 📖[kamailio.cfg::function::get_fuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_fuser)

Return the From-URI username ($fU).

## KSR.kx.get_method ##

```cpp
xval KSR.kx.get_method();
```

* 📖[kamailio.cfg::function::get_method\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_method)

Return the SIP method ($rm).

## KSR.kx.get_msgbuf ##

```cpp
xval KSR.kx.get_msgbuf();
```

* 📖[kamailio.cfg::function::get_msgbuf\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msgbuf)

## KSR.kx.get_msglen ##

```cpp
int KSR.kx.get_msglen();
```

* 📖[kamailio.cfg::function::get_msglen\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msglen)

## KSR.kx.get_msgtype ##

```cpp
int KSR.kx.get_msgtype();
```

* 📖[kamailio.cfg::function::get_msgtype\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msgtype)

## KSR.kx.get_nhuri ##

```cpp
xval KSR.kx.get_nhuri();
```

* 📖[kamailio.cfg::function::get_nhuri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_nhuri)

## KSR.kx.get_ouri ##

```cpp
xval KSR.kx.get_ouri();
```

* 📖[kamailio.cfg::function::get_ouri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ouri)

## KSR.kx.get_proto ##

```cpp
xval KSR.kx.get_proto();
```

* 📖[kamailio.cfg::function::get_proto\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_proto)

## KSR.kx.get_protoid ##

```cpp
int KSR.kx.get_protoid();
```

* 📖[kamailio.cfg::function::get_protoid\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_protoid)

## KSR.kx.get_rcv_sock_name ##

```cpp
xval KSR.kx.get_rcv_sock_name();
```

* 📖[kamailio.cfg::function::get_rcv_sock_name\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcv_sock_name)

## KSR.kx.get_rcvaddr_sock ##

```cpp
xval KSR.kx.get_rcvaddr_sock();
```

* 📖[kamailio.cfg::function::get_rcvaddr_sock\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvaddr_sock)

## KSR.kx.get_rcvadvip ##

```cpp
xval KSR.kx.get_rcvadvip();
```

* 📖[kamailio.cfg::function::get_rcvadvip\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvadvip)

## KSR.kx.get_rcvadvport ##

```cpp
xval KSR.kx.get_rcvadvport();
```

* 📖[kamailio.cfg::function::get_rcvadvport\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvadvport)

## KSR.kx.get_rcvip ##

```cpp
xval KSR.kx.get_rcvip();
```

* 📖[kamailio.cfg::function::get_rcvip\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvip)

## KSR.kx.get_rcvport ##

```cpp
xval KSR.kx.get_rcvport();
```

* 📖[kamailio.cfg::function::get_rcvport\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvport)

## KSR.kx.get_rhost ##

```cpp
xval KSR.kx.get_rhost();
```

* 📖[kamailio.cfg::function::get_rhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rhost)

Return the Request URI host (domain) part ($rd).

## KSR.kx.get_ruri ##

```cpp
xval KSR.kx.get_ruri();
```

* 📖[kamailio.cfg::function::get_ruri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ruri)

Return the Request URI ($ru).

## KSR.kx.get_ruser ##

```cpp
xval KSR.kx.get_ruser();
```

* 📖[kamailio.cfg::function::get_ruser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ruser)

Return the Request URI user part ($rU).

## KSR.kx.get_send_sock ##

```cpp
xval KSR.kx.get_send_sock();
```

* 📖[kamailio.cfg::function::get_send_sock\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock)

## KSR.kx.get_send_sock_name ##

```cpp
xval KSR.kx.get_send_sock_name();
```

* 📖[kamailio.cfg::function::get_send_sock_name\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock_name)

## KSR.kx.get_send_sock_port ##

```cpp
int KSR.kx.get_send_sock_port();
```

* 📖[kamailio.cfg::function::get_send_sock_port\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock_port)

## KSR.kx.get_srcaddr_sock ##

```cpp
xval KSR.kx.get_srcaddr_sock();
```

* 📖[kamailio.cfg::function::get_srcaddr_sock\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcaddr_sock)

## KSR.kx.get_srcip ##

```cpp
xval KSR.kx.get_srcip();
```

* 📖[kamailio.cfg::function::get_srcip\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcip)

## KSR.kx.get_srcport ##

```cpp
xval KSR.kx.get_srcport();
```

* 📖[kamailio.cfg::function::get_srcport\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcport)

## KSR.kx.get_srcuri ##

```cpp
xval KSR.kx.get_srcuri();
```

* 📖[kamailio.cfg::function::get_srcuri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcuri)

## KSR.kx.get_status ##

```cpp
int KSR.kx.get_status();
```

* 📖[kamailio.cfg::function::get_status\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_status)

## KSR.kx.get_thost ##

```cpp
xval KSR.kx.get_thost();
```

* 📖[kamailio.cfg::function::get_thost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_thost)

Return the To-URI host (domain) part ($td).

## KSR.kx.get_timestamp ##

```cpp
int KSR.kx.get_timestamp();
```

* 📖[kamailio.cfg::function::get_timestamp\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_timestamp)

## KSR.kx.get_turi ##

```cpp
xval KSR.kx.get_turi();
```

* 📖[kamailio.cfg::function::get_turi\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_turi)

Return the To URI ($tu).

## KSR.kx.get_tuser ##

```cpp
xval KSR.kx.get_tuser();
```

* 📖[kamailio.cfg::function::get_tuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_tuser)

Return the To-URI user part ($tU).

## KSR.kx.get_ua ##

```cpp
xval KSR.kx.get_ua();
```

* 📖[kamailio.cfg::function::get_ua\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ua)

## KSR.kx.gete_au ##

```cpp
xval KSR.kx.gete_au();
```

* 📖[kamailio.cfg::function::gete_au\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_au)

## KSR.kx.gete_body ##

```cpp
xval KSR.kx.gete_body();
```

* 📖[kamailio.cfg::function::gete_body\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_body)

## KSR.kx.gete_cturi ##

```cpp
xval KSR.kx.gete_cturi();
```

* 📖[kamailio.cfg::function::gete_cturi\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_cturi)

## KSR.kx.gete_duri ##

```cpp
xval KSR.kx.gete_duri();
```

* 📖[kamailio.cfg::function::gete_duri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_duri)

## KSR.kx.gete_fhost ##

```cpp
xval KSR.kx.gete_fhost();
```

* 📖[kamailio.cfg::function::gete_fhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_fhost)

## KSR.kx.gete_fuser ##

```cpp
xval KSR.kx.gete_fuser();
```

* 📖[kamailio.cfg::function::gete_fuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_fuser)

## KSR.kx.gete_rhost ##

```cpp
xval KSR.kx.gete_rhost();
```

* 📖[kamailio.cfg::function::gete_rhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_rhost)

## KSR.kx.gete_ruser ##

```cpp
xval KSR.kx.gete_ruser();
```

* 📖[kamailio.cfg::function::gete_ruser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_ruser)

## KSR.kx.gete_thost ##

```cpp
xval KSR.kx.gete_thost();
```

* 📖[kamailio.cfg::function::gete_thost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_thost)

## KSR.kx.gete_tuser ##

```cpp
xval KSR.kx.gete_tuser();
```

* 📖[kamailio.cfg::function::gete_tuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_tuser)

## KSR.kx.gete_ua ##

```cpp
xval KSR.kx.gete_ua();
```

* 📖[kamailio.cfg::function::gete_ua\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_ua)

## KSR.kx.gets_status ##

```cpp
xval KSR.kx.gets_status();
```

* 📖[kamailio.cfg::function::gets_status\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gets_status)

## KSR.kx.getw_au ##

```cpp
xval KSR.kx.getw_au();
```

* 📖[kamailio.cfg::function::getw_au\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_au)

## KSR.kx.getw_body ##

```cpp
xval KSR.kx.getw_body();
```

* 📖[kamailio.cfg::function::getw_body\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_body)

## KSR.kx.getw_cturi ##

```cpp
xval KSR.kx.getw_cturi();
```

* 📖[kamailio.cfg::function::getw_cturi\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_cturi)

## KSR.kx.getw_duri ##

```cpp
xval KSR.kx.getw_duri();
```

* 📖[kamailio.cfg::function::getw_duri\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_duri)

## KSR.kx.getw_fhost ##

```cpp
xval KSR.kx.getw_fhost();
```

* 📖[kamailio.cfg::function::getw_fhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_fhost)

## KSR.kx.getw_fuser ##

```cpp
xval KSR.kx.getw_fuser();
```

* 📖[kamailio.cfg::function::getw_fuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_fuser)

## KSR.kx.getw_rhost ##

```cpp
xval KSR.kx.getw_rhost();
```

* 📖[kamailio.cfg::function::getw_rhost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_rhost)

## KSR.kx.getw_ruser ##

```cpp
xval KSR.kx.getw_ruser();
```

* 📖[kamailio.cfg::function::getw_ruser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_ruser)

## KSR.kx.getw_thost ##

```cpp
xval KSR.kx.getw_thost();
```

* 📖[kamailio.cfg::function::getw_thost\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_thost)

## KSR.kx.getw_tuser ##

```cpp
xval KSR.kx.getw_tuser();
```

* 📖[kamailio.cfg::function::getw_tuser\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_tuser)

## KSR.kx.getw_ua ##

```cpp
xval KSR.kx.getw_ua();
```

* 📖[kamailio.cfg::function::getw_ua\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_ua)

## KSR.kx.ifdef ##

```cpp
bool KSR.kx.ifdef(str "dname");
```

* 📖[kamailio.cfg::function::ifdef\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.ifdef)

## KSR.kx.ifndef ##

```cpp
bool KSR.kx.ifndef(str "dname");
```

* 📖[kamailio.cfg::function::ifndef\(\)](https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.ifndef)
