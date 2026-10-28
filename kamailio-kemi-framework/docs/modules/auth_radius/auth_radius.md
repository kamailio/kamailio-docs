# auth_radius #

* 📖[kamailio.cfg::module::auth_radius.html](https://kamailio.org/docs/modules/devel/modules/auth_radius.html)

Exported functions:

* [KSR.auth_radius.proxy_authorize\(\)](#ksrauth_radiusproxy_authorize)
* [KSR.auth_radius.proxy_authorize_user\(\)](#ksrauth_radiusproxy_authorize_user)
* [KSR.auth_radius.www_authorize\(\)](#ksrauth_radiuswww_authorize)
* [KSR.auth_radius.www_authorize_user\(\)](#ksrauth_radiuswww_authorize_user)

## KSR.auth_radius.proxy_authorize ##

```cpp
int KSR.auth_radius.proxy_authorize(str "srealm");
```

* 📖[kamailio.cfg::function::proxy_authorize\(\)](https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize)

## KSR.auth_radius.proxy_authorize_user ##

```cpp
int KSR.auth_radius.proxy_authorize_user(str "srealm", str "suser");
```

* 📖[kamailio.cfg::function::proxy_authorize_user\(\)](https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize_user)

## KSR.auth_radius.www_authorize ##

```cpp
int KSR.auth_radius.www_authorize(str "srealm");
```

* 📖[kamailio.cfg::function::www_authorize\(\)](https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize)

## KSR.auth_radius.www_authorize_user ##

```cpp
int KSR.auth_radius.www_authorize_user(str "srealm", str "suser");
```

* 📖[kamailio.cfg::function::www_authorize_user\(\)](https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize_user)
