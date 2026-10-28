# log_systemd #

* 📖[kamailio.cfg::module::log_systemd.html](https://kamailio.org/docs/modules/devel/modules/log_systemd.html)

Exported functions:

* [KSR.log_systemd.sd_journal_print\(\)](#ksrlog_systemdsd_journal_print)
* [KSR.log_systemd.sd_journal_send_xvap\(\)](#ksrlog_systemdsd_journal_send_xvap)

## KSR.log_systemd.sd_journal_print ##

```cpp
int KSR.log_systemd.sd_journal_print(str "slev", str "stxt");
```

* 📖[kamailio.cfg::function::sd_journal_print\(\)](https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_print)

## KSR.log_systemd.sd_journal_send_xvap ##

```cpp
int KSR.log_systemd.sd_journal_send_xvap(str "xname");
```

* 📖[kamailio.cfg::function::sd_journal_send_xvap\(\)](https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_send_xvap)
