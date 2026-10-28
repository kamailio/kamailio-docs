# presence #

* 📖[kamailio.cfg::module::presence.html](https://kamailio.org/docs/modules/devel/modules/presence.html)

Exported functions:

* [KSR.presence.handle_publish\(\)](#ksrpresencehandle_publish)
* [KSR.presence.handle_publish_uri\(\)](#ksrpresencehandle_publish_uri)
* [KSR.presence.handle_subscribe\(\)](#ksrpresencehandle_subscribe)
* [KSR.presence.handle_subscribe_uri\(\)](#ksrpresencehandle_subscribe_uri)
* [KSR.presence.pres_auth_status\(\)](#ksrpresencepres_auth_status)
* [KSR.presence.pres_has_subscribers\(\)](#ksrpresencepres_has_subscribers)
* [KSR.presence.pres_refresh_watchers\(\)](#ksrpresencepres_refresh_watchers)
* [KSR.presence.pres_refresh_watchers_file\(\)](#ksrpresencepres_refresh_watchers_file)
* [KSR.presence.pres_update_watchers\(\)](#ksrpresencepres_update_watchers)

## KSR.presence.handle_publish ##

```cpp
int KSR.presence.handle_publish();
```

* 📖[kamailio.cfg::function::handle_publish\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish)

## KSR.presence.handle_publish_uri ##

```cpp
int KSR.presence.handle_publish_uri(str "sender_uri");
```

* 📖[kamailio.cfg::function::handle_publish_uri\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish_uri)

## KSR.presence.handle_subscribe ##

```cpp
int KSR.presence.handle_subscribe();
```

* 📖[kamailio.cfg::function::handle_subscribe\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe)

## KSR.presence.handle_subscribe_uri ##

```cpp
int KSR.presence.handle_subscribe_uri(str "wuri");
```

* 📖[kamailio.cfg::function::handle_subscribe_uri\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe_uri)

## KSR.presence.pres_auth_status ##

```cpp
int KSR.presence.pres_auth_status(str "watcher_uri", str "presentity_uri");
```

* 📖[kamailio.cfg::function::pres_auth_status\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_auth_status)

## KSR.presence.pres_has_subscribers ##

```cpp
int KSR.presence.pres_has_subscribers(str "pres_uri", str "wevent");
```

* 📖[kamailio.cfg::function::pres_has_subscribers\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_has_subscribers)

## KSR.presence.pres_refresh_watchers ##

```cpp
int KSR.presence.pres_refresh_watchers(str "pres", str "event", int type);
```

* 📖[kamailio.cfg::function::pres_refresh_watchers\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers)

## KSR.presence.pres_refresh_watchers_file ##

```cpp
int KSR.presence.pres_refresh_watchers_file(str "pres", str "event", int type, str "file_uri", str "filename");
```

* 📖[kamailio.cfg::function::pres_refresh_watchers_file\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers_file)

## KSR.presence.pres_update_watchers ##

```cpp
int KSR.presence.pres_update_watchers(str "pres_uri", str "event");
```

* 📖[kamailio.cfg::function::pres_update_watchers\(\)](https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_update_watchers)
