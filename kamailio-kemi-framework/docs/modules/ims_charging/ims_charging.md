# ims_charging #

* 📖[kamailio.cfg::module::ims_charging.html](https://kamailio.org/docs/modules/devel/modules/ims_charging.html)

Exported functions:

* [KSR.ims_charging.Ro_CCR\(\)](#ksrims_chargingro_ccr)
* [KSR.ims_charging.Ro_CCR_Stop\(\)](#ksrims_chargingro_ccr_stop)
* [KSR.ims_charging.Ro_set_session_id_avp\(\)](#ksrims_chargingro_set_session_id_avp)

## KSR.ims_charging.Ro_CCR ##

```cpp
int KSR.ims_charging.Ro_CCR(str "s_route_name", str "s_direction", int reservation_units, str "s_incoming_trunk_id", str "s_outgoing_trunk_id");
```

* 📖[kamailio.cfg::function::Ro_CCR\(\)](https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_CCR)

## KSR.ims_charging.Ro_CCR_Stop ##

```cpp
int KSR.ims_charging.Ro_CCR_Stop(str "p_direction", int p_code, str "p_reason");
```

* 📖[kamailio.cfg::function::Ro_CCR_Stop\(\)](https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_CCR_Stop)

## KSR.ims_charging.Ro_set_session_id_avp ##

```cpp
int KSR.ims_charging.Ro_set_session_id_avp();
```

* 📖[kamailio.cfg::function::Ro_set_session_id_avp\(\)](https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_set_session_id_avp)
