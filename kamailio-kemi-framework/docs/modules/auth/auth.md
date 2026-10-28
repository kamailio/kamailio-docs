# auth #

* 📖[kamailio.cfg::module::auth.html](https://kamailio.org/docs/modules/devel/modules/auth.html)

Exported functions:

* [KSR.auth.auth_algorithm\(\)](#ksrauthauth_algorithm)
* [KSR.auth.auth_challenge\(\)](#ksrauthauth_challenge)
* [KSR.auth.auth_get_www_authenticate\(\)](#ksrauthauth_get_www_authenticate)
* [KSR.auth.consume_credentials\(\)](#ksrauthconsume_credentials)
* [KSR.auth.has_credentials\(\)](#ksrauthhas_credentials)
* [KSR.auth.proxy_challenge\(\)](#ksrauthproxy_challenge)
* [KSR.auth.pv_auth_check\(\)](#ksrauthpv_auth_check)
* [KSR.auth.pv_proxy_authenticate\(\)](#ksrauthpv_proxy_authenticate)
* [KSR.auth.pv_www_authenticate\(\)](#ksrauthpv_www_authenticate)
* [KSR.auth.pv_www_authenticate_method\(\)](#ksrauthpv_www_authenticate_method)
* [KSR.auth.www_challenge\(\)](#ksrauthwww_challenge)

## KSR.auth.auth_algorithm ##

```cpp
int KSR.auth.auth_algorithm(str "alg");
```

* 📖[kamailio.cfg::function::auth_algorithm\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.auth_algorithm)

## KSR.auth.auth_challenge ##

```cpp
int KSR.auth.auth_challenge(str "realm", int flags);
```

* 📖[kamailio.cfg::function::auth_challenge\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.auth_challenge)

## KSR.auth.auth_get_www_authenticate ##

```cpp
int KSR.auth.auth_get_www_authenticate(str "realm", int flags, str "pvdst");
```

* 📖[kamailio.cfg::function::auth_get_www_authenticate\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.auth_get_www_authenticate)

## KSR.auth.consume_credentials ##

```cpp
int KSR.auth.consume_credentials();
```

* 📖[kamailio.cfg::function::consume_credentials\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.consume_credentials)

## KSR.auth.has_credentials ##

```cpp
int KSR.auth.has_credentials(str "srealm");
```

* 📖[kamailio.cfg::function::has_credentials\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.has_credentials)

## KSR.auth.proxy_challenge ##

```cpp
int KSR.auth.proxy_challenge(str "realm", int flags);
```

* 📖[kamailio.cfg::function::proxy_challenge\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.proxy_challenge)

## KSR.auth.pv_auth_check ##

```cpp
int KSR.auth.pv_auth_check(str "srealm", str "spasswd", int vflags, int vchecks);
```

* 📖[kamailio.cfg::function::pv_auth_check\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_auth_check)

## KSR.auth.pv_proxy_authenticate ##

```cpp
int KSR.auth.pv_proxy_authenticate(str "realm", str "passwd", int flags);
```

* 📖[kamailio.cfg::function::pv_proxy_authenticate\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_proxy_authenticate)

## KSR.auth.pv_www_authenticate ##

```cpp
int KSR.auth.pv_www_authenticate(str "realm", str "passwd", int flags);
```

* 📖[kamailio.cfg::function::pv_www_authenticate\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_www_authenticate)

## KSR.auth.pv_www_authenticate_method ##

```cpp
int KSR.auth.pv_www_authenticate_method(str "realm", str "passwd", int flags, str "method");
```

* 📖[kamailio.cfg::function::pv_www_authenticate_method\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_www_authenticate_method)

## KSR.auth.www_challenge ##

```cpp
int KSR.auth.www_challenge(str "realm", int flags);
```

* 📖[kamailio.cfg::function::www_challenge\(\)](https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.www_challenge)
