# tcpops #

* 📖[kamailio.cfg::module::tcpops.html](https://kamailio.org/docs/modules/devel/modules/tcpops.html)

Exported functions:

* [KSR.tcpops.tcp_close_connection\(\)](#ksrtcpopstcp_close_connection)
* [KSR.tcpops.tcp_close_connection_id\(\)](#ksrtcpopstcp_close_connection_id)
* [KSR.tcpops.tcp_con_alive\(\)](#ksrtcpopstcp_con_alive)
* [KSR.tcpops.tcp_conid_alive\(\)](#ksrtcpopstcp_conid_alive)
* [KSR.tcpops.tcp_conid_state\(\)](#ksrtcpopstcp_conid_state)
* [KSR.tcpops.tcp_enable_closed_event\(\)](#ksrtcpopstcp_enable_closed_event)
* [KSR.tcpops.tcp_enable_closed_event_cid\(\)](#ksrtcpopstcp_enable_closed_event_cid)
* [KSR.tcpops.tcp_get_conid\(\)](#ksrtcpopstcp_get_conid)
* [KSR.tcpops.tcp_keepalive_disable\(\)](#ksrtcpopstcp_keepalive_disable)
* [KSR.tcpops.tcp_keepalive_disable_cid\(\)](#ksrtcpopstcp_keepalive_disable_cid)
* [KSR.tcpops.tcp_keepalive_enable\(\)](#ksrtcpopstcp_keepalive_enable)
* [KSR.tcpops.tcp_keepalive_enable_cid\(\)](#ksrtcpopstcp_keepalive_enable_cid)
* [KSR.tcpops.tcp_set_connection_lifetime\(\)](#ksrtcpopstcp_set_connection_lifetime)
* [KSR.tcpops.tcp_set_connection_lifetime_cid\(\)](#ksrtcpopstcp_set_connection_lifetime_cid)
* [KSR.tcpops.tcp_set_otcpid\(\)](#ksrtcpopstcp_set_otcpid)
* [KSR.tcpops.tcp_set_otcpid_flag\(\)](#ksrtcpopstcp_set_otcpid_flag)

## KSR.tcpops.tcp_close_connection ##

```cpp
int KSR.tcpops.tcp_close_connection();
```

* 📖[kamailio.cfg::function::tcp_close_connection\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_close_connection)

## KSR.tcpops.tcp_close_connection_id ##

```cpp
int KSR.tcpops.tcp_close_connection_id(int conid);
```

* 📖[kamailio.cfg::function::tcp_close_connection_id\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_close_connection_id)

## KSR.tcpops.tcp_con_alive ##

```cpp
int KSR.tcpops.tcp_con_alive(str "saddr");
```

* 📖[kamailio.cfg::function::tcp_con_alive\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_con_alive)

## KSR.tcpops.tcp_conid_alive ##

```cpp
int KSR.tcpops.tcp_conid_alive(int i_conid);
```

* 📖[kamailio.cfg::function::tcp_conid_alive\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_alive)

## KSR.tcpops.tcp_conid_state ##

```cpp
int KSR.tcpops.tcp_conid_state(int i_conid);
```

* 📖[kamailio.cfg::function::tcp_conid_state\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_state)

## KSR.tcpops.tcp_enable_closed_event ##

```cpp
int KSR.tcpops.tcp_enable_closed_event();
```

* 📖[kamailio.cfg::function::tcp_enable_closed_event\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event)

## KSR.tcpops.tcp_enable_closed_event_cid ##

```cpp
int KSR.tcpops.tcp_enable_closed_event_cid(int i_conid);
```

* 📖[kamailio.cfg::function::tcp_enable_closed_event_cid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event_cid)

## KSR.tcpops.tcp_get_conid ##

```cpp
int KSR.tcpops.tcp_get_conid(str "saddr", str "pvs");
```

* 📖[kamailio.cfg::function::tcp_get_conid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_get_conid)

## KSR.tcpops.tcp_keepalive_disable ##

```cpp
int KSR.tcpops.tcp_keepalive_disable();
```

* 📖[kamailio.cfg::function::tcp_keepalive_disable\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable)

## KSR.tcpops.tcp_keepalive_disable_cid ##

```cpp
int KSR.tcpops.tcp_keepalive_disable_cid(int i_con);
```

* 📖[kamailio.cfg::function::tcp_keepalive_disable_cid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable_cid)

## KSR.tcpops.tcp_keepalive_enable ##

```cpp
int KSR.tcpops.tcp_keepalive_enable(int i_idle, int i_cnt, int i_intvl);
```

* 📖[kamailio.cfg::function::tcp_keepalive_enable\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable)

## KSR.tcpops.tcp_keepalive_enable_cid ##

```cpp
int KSR.tcpops.tcp_keepalive_enable_cid(int i_con, int i_idle, int i_cnt, int i_intvl);
```

* 📖[kamailio.cfg::function::tcp_keepalive_enable_cid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable_cid)

## KSR.tcpops.tcp_set_connection_lifetime ##

```cpp
int KSR.tcpops.tcp_set_connection_lifetime(int i_time);
```

* 📖[kamailio.cfg::function::tcp_set_connection_lifetime\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime)

## KSR.tcpops.tcp_set_connection_lifetime_cid ##

```cpp
int KSR.tcpops.tcp_set_connection_lifetime_cid(int i_conid, int i_time);
```

* 📖[kamailio.cfg::function::tcp_set_connection_lifetime_cid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime_cid)

## KSR.tcpops.tcp_set_otcpid ##

```cpp
int KSR.tcpops.tcp_set_otcpid(int vconid);
```

* 📖[kamailio.cfg::function::tcp_set_otcpid\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid)

## KSR.tcpops.tcp_set_otcpid_flag ##

```cpp
int KSR.tcpops.tcp_set_otcpid_flag(int vmode);
```

* 📖[kamailio.cfg::function::tcp_set_otcpid_flag\(\)](https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid_flag)
