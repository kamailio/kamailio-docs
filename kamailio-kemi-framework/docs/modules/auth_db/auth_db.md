# auth_db #

* 📖[kamailio.cfg::module::auth_db.html](https://kamailio.org/docs/modules/devel/modules/auth_db.html)

Exported functions:

* [KSR.auth_db.auth_check\(\)](#ksrauth_dbauth_check)
* [KSR.auth_db.is_subscriber\(\)](#ksrauth_dbis_subscriber)
* [KSR.auth_db.www_authenticate\(\)](#ksrauth_dbwww_authenticate)
* [KSR.auth_db.www_authenticate_method\(\)](#ksrauth_dbwww_authenticate_method)

## KSR.auth_db.auth_check ##

```cpp
int KSR.auth_db.auth_check(str "srealm", str "stable", int iflags);
```

* 📖[kamailio.cfg::function::auth_check\(\)](https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.auth_check)

## KSR.auth_db.is_subscriber ##

```cpp
int KSR.auth_db.is_subscriber(str "suri", str "stable", int iflags);
```

* 📖[kamailio.cfg::function::is_subscriber\(\)](https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.is_subscriber)

## KSR.auth_db.www_authenticate ##

```cpp
int KSR.auth_db.www_authenticate(str "realm", str "table");
```

* 📖[kamailio.cfg::function::www_authenticate\(\)](https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.www_authenticate)

## KSR.auth_db.www_authenticate_method ##

```cpp
int KSR.auth_db.www_authenticate_method(str "realm", str "table", str "method");
```

* 📖[kamailio.cfg::function::www_authenticate_method\(\)](https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.www_authenticate_method)
