# stirshaken #

* 📖[kamailio.cfg::module::stirshaken.html](https://kamailio.org/docs/modules/devel/modules/stirshaken.html)

Exported functions:

* [KSR.stirshaken.stirshaken_add_identity\(\)](#ksrstirshakenstirshaken_add_identity)
* [KSR.stirshaken.stirshaken_add_identity_with_key\(\)](#ksrstirshakenstirshaken_add_identity_with_key)
* [KSR.stirshaken.stirshaken_check_identity\(\)](#ksrstirshakenstirshaken_check_identity)
* [KSR.stirshaken.stirshaken_check_identity_with_cert\(\)](#ksrstirshakenstirshaken_check_identity_with_cert)
* [KSR.stirshaken.stirshaken_check_identity_with_key\(\)](#ksrstirshakenstirshaken_check_identity_with_key)

## KSR.stirshaken.stirshaken_add_identity ##

```cpp
int KSR.stirshaken.stirshaken_add_identity(str "x5u", str "attest", str "origtn_val", str "desttn_val", str "origid");
```

* 📖[kamailio.cfg::function::stirshaken_add_identity\(\)](https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_add_identity)

## KSR.stirshaken.stirshaken_add_identity_with_key ##

```cpp
int KSR.stirshaken.stirshaken_add_identity_with_key(str "x5u", str "attest", str "origtn_val", str "desttn_val", str "origid", str "keypath");
```

* 📖[kamailio.cfg::function::stirshaken_add_identity_with_key\(\)](https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_add_identity_with_key)

## KSR.stirshaken.stirshaken_check_identity ##

```cpp
int KSR.stirshaken.stirshaken_check_identity();
```

* 📖[kamailio.cfg::function::stirshaken_check_identity\(\)](https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity)

## KSR.stirshaken.stirshaken_check_identity_with_cert ##

```cpp
int KSR.stirshaken.stirshaken_check_identity_with_cert(str "cert_path");
```

* 📖[kamailio.cfg::function::stirshaken_check_identity_with_cert\(\)](https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity_with_cert)

## KSR.stirshaken.stirshaken_check_identity_with_key ##

```cpp
int KSR.stirshaken.stirshaken_check_identity_with_key(str "keypath");
```

* 📖[kamailio.cfg::function::stirshaken_check_identity_with_key\(\)](https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity_with_key)
