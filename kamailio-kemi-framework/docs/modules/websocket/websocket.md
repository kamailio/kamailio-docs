# websocket #

* 📖[kamailio.cfg::module::websocket.html](https://kamailio.org/docs/modules/devel/modules/websocket.html)

Exported functions:

* [KSR.websocket.close\(\)](#ksrwebsocketclose)
* [KSR.websocket.close_conid\(\)](#ksrwebsocketclose_conid)
* [KSR.websocket.close_reason\(\)](#ksrwebsocketclose_reason)
* [KSR.websocket.connect\(\)](#ksrwebsocketconnect)
* [KSR.websocket.handle_handshake\(\)](#ksrwebsockethandle_handshake)
* [KSR.websocket.send\(\)](#ksrwebsocketsend)

## KSR.websocket.close ##

```cpp
int KSR.websocket.close();
```

* 📖[kamailio.cfg::function::close\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close)

## KSR.websocket.close_conid ##

```cpp
int KSR.websocket.close_conid(int status, str "reason", int con);
```

* 📖[kamailio.cfg::function::close_conid\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_conid)

## KSR.websocket.close_reason ##

```cpp
int KSR.websocket.close_reason(int status, str "reason");
```

* 📖[kamailio.cfg::function::close_reason\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_reason)

## KSR.websocket.connect ##

```cpp
int KSR.websocket.connect(str "host", int port, str "path", str "sub_protocol", int cmode);
```

* 📖[kamailio.cfg::function::connect\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.connect)

## KSR.websocket.handle_handshake ##

```cpp
int KSR.websocket.handle_handshake();
```

* 📖[kamailio.cfg::function::handle_handshake\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.handle_handshake)

## KSR.websocket.send ##

```cpp
int KSR.websocket.send(str "host", int port, str "path", str "sub_protocol", int cmode);
```

* 📖[kamailio.cfg::function::send\(\)](https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.send)
