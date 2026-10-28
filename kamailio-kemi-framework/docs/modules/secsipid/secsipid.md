# secsipid #

* 📖[kamailio.cfg::module::secsipid.html](https://kamailio.org/docs/modules/devel/modules/secsipid.html)

Exported functions:

* [KSR.secsipid.result_str\(\)](#ksrsecsipidresult_str)
* [KSR.secsipid.secsipid_add_identity\(\)](#ksrsecsipidsecsipid_add_identity)
* [KSR.secsipid.secsipid_build_identity\(\)](#ksrsecsipidsecsipid_build_identity)
* [KSR.secsipid.secsipid_build_identity_prvkey\(\)](#ksrsecsipidsecsipid_build_identity_prvkey)
* [KSR.secsipid.secsipid_check\(\)](#ksrsecsipidsecsipid_check)
* [KSR.secsipid.secsipid_check_identity\(\)](#ksrsecsipidsecsipid_check_identity)
* [KSR.secsipid.secsipid_check_identity_pubkey\(\)](#ksrsecsipidsecsipid_check_identity_pubkey)
* [KSR.secsipid.secsipid_get_url\(\)](#ksrsecsipidsecsipid_get_url)
* [KSR.secsipid.secsipid_get_val\(\)](#ksrsecsipidsecsipid_get_val)
* [KSR.secsipid.secsipid_sign\(\)](#ksrsecsipidsecsipid_sign)
* [KSR.secsipid.secsipid_sign_prvkey\(\)](#ksrsecsipidsecsipid_sign_prvkey)
* [KSR.secsipid.secsipid_verify\(\)](#ksrsecsipidsecsipid_verify)

## KSR.secsipid.result_str ##

```cpp
int KSR.secsipid.result_str(str "attrname", str "avpname");
```

* 📖[kamailio.cfg::function::result_str\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.result_str)

## KSR.secsipid.secsipid_add_identity ##

```cpp
int KSR.secsipid.secsipid_add_identity(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keypath");
```

* 📖[kamailio.cfg::function::secsipid_add_identity\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_add_identity)

## KSR.secsipid.secsipid_build_identity ##

```cpp
int KSR.secsipid.secsipid_build_identity(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keypath");
```

* 📖[kamailio.cfg::function::secsipid_build_identity\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_build_identity)

## KSR.secsipid.secsipid_build_identity_prvkey ##

```cpp
int KSR.secsipid.secsipid_build_identity_prvkey(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keydata");
```

* 📖[kamailio.cfg::function::secsipid_build_identity_prvkey\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_build_identity_prvkey)

## KSR.secsipid.secsipid_check ##

```cpp
int KSR.secsipid.secsipid_check(str "sidentity", str "keypath");
```

* 📖[kamailio.cfg::function::secsipid_check\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check)

## KSR.secsipid.secsipid_check_identity ##

```cpp
int KSR.secsipid.secsipid_check_identity(str "keypath");
```

* 📖[kamailio.cfg::function::secsipid_check_identity\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity)

## KSR.secsipid.secsipid_check_identity_pubkey ##

```cpp
int KSR.secsipid.secsipid_check_identity_pubkey(str "keyval");
```

* 📖[kamailio.cfg::function::secsipid_check_identity_pubkey\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity_pubkey)

## KSR.secsipid.secsipid_get_url ##

```cpp
xval KSR.secsipid.secsipid_get_url(str "surl");
```

* 📖[kamailio.cfg::function::secsipid_get_url\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_get_url)

## KSR.secsipid.secsipid_get_val ##

```cpp
xval KSR.secsipid.secsipid_get_val();
```

* 📖[kamailio.cfg::function::secsipid_get_val\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_get_val)

## KSR.secsipid.secsipid_sign ##

```cpp
int KSR.secsipid.secsipid_sign(str "sheaders", str "spayload", str "keypath");
```

* 📖[kamailio.cfg::function::secsipid_sign\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_sign)

## KSR.secsipid.secsipid_sign_prvkey ##

```cpp
int KSR.secsipid.secsipid_sign_prvkey(str "sheaders", str "spayload", str "keydata");
```

* 📖[kamailio.cfg::function::secsipid_sign_prvkey\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_sign_prvkey)

## KSR.secsipid.secsipid_verify ##

```cpp
int KSR.secsipid.secsipid_verify(str "sidentity", str "keyval", str "opts");
```

* 📖[kamailio.cfg::function::secsipid_verify\(\)](https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_verify)
