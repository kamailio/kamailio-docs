# kafka #

* 📖[kamailio.cfg::module::kafka.html](https://kamailio.org/docs/modules/devel/modules/kafka.html)

Exported functions:

* [KSR.kafka.send\(\)](#ksrkafkasend)
* [KSR.kafka.send_key\(\)](#ksrkafkasend_key)

## KSR.kafka.send ##

```cpp
int KSR.kafka.send(str "s_topic", str "s_message");
```

* 📖[kamailio.cfg::function::send\(\)](https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send)

## KSR.kafka.send_key ##

```cpp
int KSR.kafka.send_key(str "s_topic", str "s_message", str "s_key");
```

* 📖[kamailio.cfg::function::send_key\(\)](https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send_key)
