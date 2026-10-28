# mqtt #

* 📖[kamailio.cfg::module::mqtt.html](https://kamailio.org/docs/modules/devel/modules/mqtt.html)

Exported functions:

* [KSR.mqtt.publish\(\)](#ksrmqttpublish)
* [KSR.mqtt.subscribe\(\)](#ksrmqttsubscribe)
* [KSR.mqtt.unsubscribe\(\)](#ksrmqttunsubscribe)

## KSR.mqtt.publish ##

```cpp
int KSR.mqtt.publish(str "topic", str "payload", int qos);
```

* 📖[kamailio.cfg::function::publish\(\)](https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.publish)

## KSR.mqtt.subscribe ##

```cpp
int KSR.mqtt.subscribe(str "topic", int qos);
```

* 📖[kamailio.cfg::function::subscribe\(\)](https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.subscribe)

## KSR.mqtt.unsubscribe ##

```cpp
int KSR.mqtt.unsubscribe(str "topic");
```

* 📖[kamailio.cfg::function::unsubscribe\(\)](https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.unsubscribe)
