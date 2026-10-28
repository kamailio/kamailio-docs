# rabbitmq #

* 📖[kamailio.cfg::module::rabbitmq.html](https://kamailio.org/docs/modules/devel/modules/rabbitmq.html)

Exported functions:

* [KSR.rabbitmq.publish\(\)](#ksrrabbitmqpublish)
* [KSR.rabbitmq.publish_consume\(\)](#ksrrabbitmqpublish_consume)

## KSR.rabbitmq.publish ##

```cpp
int KSR.rabbitmq.publish(str "exchange", str "routingkey", str "contenttype", str "messagebody");
```

* 📖[kamailio.cfg::function::publish\(\)](https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish)

## KSR.rabbitmq.publish_consume ##

```cpp
int KSR.rabbitmq.publish_consume(str "exchange", str "routingkey", str "contenttype", str "messagebody", str "dpv");
```

* 📖[kamailio.cfg::function::publish_consume\(\)](https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish_consume)
