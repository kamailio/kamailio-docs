# jwt3 #

* 📖[kamailio.cfg::module::jwt3.html](https://kamailio.org/docs/modules/devel/modules/jwt3.html)

Exported functions:

* [KSR.jwt3.jwt3_generate\(\)](#ksrjwt3jwt3_generate)
* [KSR.jwt3.jwt3_generate_hdrs\(\)](#ksrjwt3jwt3_generate_hdrs)
* [KSR.jwt3.jwt3_verify\(\)](#ksrjwt3jwt3_verify)
* [KSR.jwt3.jwt3_verify_key\(\)](#ksrjwt3jwt3_verify_key)

## KSR.jwt3.jwt3_generate ##

```cpp
int KSR.jwt3.jwt3_generate(str "key", str "alg", str "claims");
```

* 📖[kamailio.cfg::function::jwt3_generate\(\)](https://kamailio.org/docs/modules/devel/modules/jwt3.html#jwt3.f.jwt3_generate)

## KSR.jwt3.jwt3_generate_hdrs ##

```cpp
int KSR.jwt3.jwt3_generate_hdrs(str "key", str "alg", str "claims", str "headers");
```

* 📖[kamailio.cfg::function::jwt3_generate_hdrs\(\)](https://kamailio.org/docs/modules/devel/modules/jwt3.html#jwt3.f.jwt3_generate_hdrs)

## KSR.jwt3.jwt3_verify ##

```cpp
int KSR.jwt3.jwt3_verify(str "keypath", str "alg", str "claims", str "jwtval");
```

* 📖[kamailio.cfg::function::jwt3_verify\(\)](https://kamailio.org/docs/modules/devel/modules/jwt3.html#jwt3.f.jwt3_verify)

## KSR.jwt3.jwt3_verify_key ##

```cpp
int KSR.jwt3.jwt3_verify_key(str "key", str "alg", str "claims", str "jwtval");
```

* 📖[kamailio.cfg::function::jwt3_verify_key\(\)](https://kamailio.org/docs/modules/devel/modules/jwt3.html#jwt3.f.jwt3_verify_key)
