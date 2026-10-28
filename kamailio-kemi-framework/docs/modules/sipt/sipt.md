# sipt #

* 📖[kamailio.cfg::module::sipt.html](https://kamailio.org/docs/modules/devel/modules/sipt.html)

Exported functions:

* [KSR.sipt.destination\(\)](#ksrsiptdestination)
* [KSR.sipt.destination_terminator\(\)](#ksrsiptdestination_terminator)
* [KSR.sipt.forwarding\(\)](#ksrsiptforwarding)
* [KSR.sipt.has_isup_body\(\)](#ksrsipthas_isup_body)
* [KSR.sipt.set_bci_1\(\)](#ksrsiptset_bci_1)
* [KSR.sipt.set_calling\(\)](#ksrsiptset_calling)

## KSR.sipt.destination ##

```cpp
bool KSR.sipt.destination(str "_destination", str "_hops", str "_nai");
```

* 📖[kamailio.cfg::function::destination\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.destination)

## KSR.sipt.destination_terminator ##

```cpp
bool KSR.sipt.destination_terminator(str "_destination", str "_hops", str "_nai", str "_terminator");
```

* 📖[kamailio.cfg::function::destination_terminator\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.destination_terminator)

## KSR.sipt.forwarding ##

```cpp
bool KSR.sipt.forwarding(str "_fwdnumber", str "_nai");
```

* 📖[kamailio.cfg::function::forwarding\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.forwarding)

## KSR.sipt.has_isup_body ##

```cpp
bool KSR.sipt.has_isup_body();
```

* 📖[kamailio.cfg::function::has_isup_body\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.has_isup_body)

## KSR.sipt.set_bci_1 ##

```cpp
bool KSR.sipt.set_bci_1(str "_charge_indicator", str "_called_status", str "_called_category", str "_e2e_indicator");
```

* 📖[kamailio.cfg::function::set_bci_1\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.set_bci_1)

## KSR.sipt.set_calling ##

```cpp
bool KSR.sipt.set_calling(str "_origin", str "_nai", str "_pres", str "_screen");
```

* 📖[kamailio.cfg::function::set_calling\(\)](https://kamailio.org/docs/modules/devel/modules/sipt.html#sipt.f.set_calling)
