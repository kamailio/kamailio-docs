# dmq #

* 📖[kamailio.cfg::module::dmq.html](https://kamailio.org/docs/modules/devel/modules/dmq.html)

Exported functions:

* [KSR.dmq.bcast_message\(\)](#ksrdmqbcast_message)
* [KSR.dmq.handle_custom_message\(\)](#ksrdmqhandle_custom_message)
* [KSR.dmq.handle_message\(\)](#ksrdmqhandle_message)
* [KSR.dmq.handle_message_rc\(\)](#ksrdmqhandle_message_rc)
* [KSR.dmq.is_from_node\(\)](#ksrdmqis_from_node)
* [KSR.dmq.process_custom_message\(\)](#ksrdmqprocess_custom_message)
* [KSR.dmq.process_message\(\)](#ksrdmqprocess_message)
* [KSR.dmq.process_message_rc\(\)](#ksrdmqprocess_message_rc)
* [KSR.dmq.send_message\(\)](#ksrdmqsend_message)
* [KSR.dmq.t_replicate\(\)](#ksrdmqt_replicate)
* [KSR.dmq.t_replicate_mode\(\)](#ksrdmqt_replicate_mode)

## KSR.dmq.bcast_message ##

```cpp
int KSR.dmq.bcast_message(str "peer_str", str "body_str", str "ct_str");
```

* 📖[kamailio.cfg::function::bcast_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.bcast_message)

## KSR.dmq.handle_custom_message ##

```cpp
int KSR.dmq.handle_custom_message(str "peer", str "from", str "body", str "content_type");
```

* 📖[kamailio.cfg::function::handle_custom_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_custom_message)

## KSR.dmq.handle_message ##

```cpp
int KSR.dmq.handle_message();
```

* 📖[kamailio.cfg::function::handle_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message)

## KSR.dmq.handle_message_rc ##

```cpp
int KSR.dmq.handle_message_rc(int returnval);
```

* 📖[kamailio.cfg::function::handle_message_rc\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message_rc)

## KSR.dmq.is_from_node ##

```cpp
int KSR.dmq.is_from_node();
```

* 📖[kamailio.cfg::function::is_from_node\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.is_from_node)

## KSR.dmq.process_custom_message ##

```cpp
int KSR.dmq.process_custom_message(str "peer", str "from", str "body", str "content_type");
```

* 📖[kamailio.cfg::function::process_custom_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.process_custom_message)

## KSR.dmq.process_message ##

```cpp
int KSR.dmq.process_message();
```

* 📖[kamailio.cfg::function::process_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.process_message)

## KSR.dmq.process_message_rc ##

```cpp
int KSR.dmq.process_message_rc(int returnval);
```

* 📖[kamailio.cfg::function::process_message_rc\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.process_message_rc)

## KSR.dmq.send_message ##

```cpp
int KSR.dmq.send_message(str "peer_str", str "to_str", str "body_str", str "ct_str");
```

* 📖[kamailio.cfg::function::send_message\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.send_message)

## KSR.dmq.t_replicate ##

```cpp
int KSR.dmq.t_replicate();
```

* 📖[kamailio.cfg::function::t_replicate\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate)

## KSR.dmq.t_replicate_mode ##

```cpp
int KSR.dmq.t_replicate_mode(int mode);
```

* 📖[kamailio.cfg::function::t_replicate_mode\(\)](https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate_mode)
