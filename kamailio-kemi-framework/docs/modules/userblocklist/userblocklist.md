# userblocklist #

* 📖[kamailio.cfg::module::userblocklist.html](https://kamailio.org/docs/modules/devel/modules/userblocklist.html)

Exported functions:

* [KSR.userblocklist.check_allowlist\(\)](#ksruserblocklistcheck_allowlist)
* [KSR.userblocklist.check_blocklist\(\)](#ksruserblocklistcheck_blocklist)
* [KSR.userblocklist.check_global_blocklist\(\)](#ksruserblocklistcheck_global_blocklist)
* [KSR.userblocklist.check_user_allowlist\(\)](#ksruserblocklistcheck_user_allowlist)
* [KSR.userblocklist.check_user_allowlist_number\(\)](#ksruserblocklistcheck_user_allowlist_number)
* [KSR.userblocklist.check_user_allowlist_table\(\)](#ksruserblocklistcheck_user_allowlist_table)
* [KSR.userblocklist.check_user_blocklist\(\)](#ksruserblocklistcheck_user_blocklist)
* [KSR.userblocklist.check_user_blocklist_number\(\)](#ksruserblocklistcheck_user_blocklist_number)
* [KSR.userblocklist.check_user_blocklist_table\(\)](#ksruserblocklistcheck_user_blocklist_table)

## KSR.userblocklist.check_allowlist ##

```cpp
int KSR.userblocklist.check_allowlist(str "stable");
```

* 📖[kamailio.cfg::function::check_allowlist\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_allowlist)

## KSR.userblocklist.check_blocklist ##

```cpp
int KSR.userblocklist.check_blocklist(str "stable");
```

* 📖[kamailio.cfg::function::check_blocklist\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_blocklist)

## KSR.userblocklist.check_global_blocklist ##

```cpp
int KSR.userblocklist.check_global_blocklist();
```

* 📖[kamailio.cfg::function::check_global_blocklist\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_global_blocklist)

## KSR.userblocklist.check_user_allowlist ##

```cpp
int KSR.userblocklist.check_user_allowlist(str "suser", str "sdomain");
```

* 📖[kamailio.cfg::function::check_user_allowlist\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist)

## KSR.userblocklist.check_user_allowlist_number ##

```cpp
int KSR.userblocklist.check_user_allowlist_number(str "suser", str "sdomain", str "snumber");
```

* 📖[kamailio.cfg::function::check_user_allowlist_number\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_number)

## KSR.userblocklist.check_user_allowlist_table ##

```cpp
int KSR.userblocklist.check_user_allowlist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

* 📖[kamailio.cfg::function::check_user_allowlist_table\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_table)

## KSR.userblocklist.check_user_blocklist ##

```cpp
int KSR.userblocklist.check_user_blocklist(str "suser", str "sdomain");
```

* 📖[kamailio.cfg::function::check_user_blocklist\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist)

## KSR.userblocklist.check_user_blocklist_number ##

```cpp
int KSR.userblocklist.check_user_blocklist_number(str "suser", str "sdomain", str "snumber");
```

* 📖[kamailio.cfg::function::check_user_blocklist_number\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_number)

## KSR.userblocklist.check_user_blocklist_table ##

```cpp
int KSR.userblocklist.check_user_blocklist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

* 📖[kamailio.cfg::function::check_user_blocklist_table\(\)](https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_table)
