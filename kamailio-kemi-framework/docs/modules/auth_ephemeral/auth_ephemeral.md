# auth_ephemeral #

* 📖[kamailio.cfg::module::auth_ephemeral.html](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html)

Exported functions:

* [KSR.auth_ephemeral.autheph_authenticate\(\)](#ksrauth_ephemeralautheph_authenticate)
* [KSR.auth_ephemeral.autheph_check\(\)](#ksrauth_ephemeralautheph_check)
* [KSR.auth_ephemeral.autheph_proxy\(\)](#ksrauth_ephemeralautheph_proxy)
* [KSR.auth_ephemeral.autheph_www\(\)](#ksrauth_ephemeralautheph_www)
* [KSR.auth_ephemeral.autheph_www_method\(\)](#ksrauth_ephemeralautheph_www_method)

## KSR.auth_ephemeral.autheph_authenticate ##

```cpp
int KSR.auth_ephemeral.autheph_authenticate(str "susername", str "spassword");
```

* 📖[kamailio.cfg::function::autheph_authenticate\(\)](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_authenticate)

## KSR.auth_ephemeral.autheph_check ##

```cpp
int KSR.auth_ephemeral.autheph_check(str "srealm");
```

* 📖[kamailio.cfg::function::autheph_check\(\)](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_check)

## KSR.auth_ephemeral.autheph_proxy ##

```cpp
int KSR.auth_ephemeral.autheph_proxy(str "srealm");
```

* 📖[kamailio.cfg::function::autheph_proxy\(\)](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_proxy)

## KSR.auth_ephemeral.autheph_www ##

```cpp
int KSR.auth_ephemeral.autheph_www(str "srealm");
```

* 📖[kamailio.cfg::function::autheph_www\(\)](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www)

## KSR.auth_ephemeral.autheph_www_method ##

```cpp
int KSR.auth_ephemeral.autheph_www_method(str "srealm", str "smethod");
```

* 📖[kamailio.cfg::function::autheph_www_method\(\)](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www_method)
