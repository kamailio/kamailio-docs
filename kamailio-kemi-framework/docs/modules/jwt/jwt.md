# jwt #

* 📖[kamailio.cfg::module::jwt.html](https://kamailio.org/docs/modules/devel/modules/jwt.html)

Exported functions:

* [KSR.jwt.jwt_generate\(\)](#ksrjwtjwt_generate)
* [KSR.jwt.jwt_generate_hdrs\(\)](#ksrjwtjwt_generate_hdrs)
* [KSR.jwt.jwt_verify\(\)](#ksrjwtjwt_verify)
* [KSR.jwt.jwt_verify_key\(\)](#ksrjwtjwt_verify_key)

## KSR.jwt.jwt_generate ##

```cpp
int KSR.jwt.jwt_generate(str "key", str "alg", str "claims");
```

* 📖[kamailio.cfg::function::jwt_generate\(\)](https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_generate)

## KSR.jwt.jwt_generate_hdrs ##

```cpp
int KSR.jwt.jwt_generate_hdrs(str "key", str "alg", str "claims", str "headers");
```

* 📖[kamailio.cfg::function::jwt_generate_hdrs\(\)](https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_generate_hdrs)

## KSR.jwt.jwt_verify ##

```cpp
int KSR.jwt.jwt_verify(str "keypath", str "alg", str "claims", str "jwtval");
```

* 📖[kamailio.cfg::function::jwt_verify\(\)](https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_verify)

## KSR.jwt.jwt_verify_key ##

```cpp
int KSR.jwt.jwt_verify_key(str "key", str "alg", str "claims", str "jwtval");
```

* 📖[kamailio.cfg::function::jwt_verify_key\(\)](https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_verify_key)
