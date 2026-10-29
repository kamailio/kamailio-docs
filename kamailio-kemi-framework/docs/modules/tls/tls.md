# tls #

* 📖[kamailio.cfg::module::tls.html](https://kamailio.org/docs/modules/devel/modules/tls.html)

Exported functions:

* [KSR.tls.cget\(\)](#ksrtlscget)
* [KSR.tls.is_peer_verified\(\)](#ksrtlsis_peer_verified)
* [KSR.tls.set_connect_server_id\(\)](#ksrtlsset_connect_server_id)

## KSR.tls.cget ##

```cpp
xval KSR.tls.cget(str "aname");
```

* 📖[kamailio.cfg::function::cget\(\)](https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.cget)

Return values corresponding the pseudo-variables exported by TLS module, related
to TLS connection and certificates. The parameter has to be the name of the
pseudo-variable (without `$`).

Example:

```lua
local vPeerSubjectCn = KSR.tls.cget("tls_peer_subject_cn");
```

## KSR.tls.is_peer_verified ##

```cpp
int KSR.tls.is_peer_verified();
```

* 📖[kamailio.cfg::function::is_peer_verified\(\)](https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.is_peer_verified)

## KSR.tls.set_connect_server_id ##

```cpp
int KSR.tls.set_connect_server_id(str "srvid");
```

* 📖[kamailio.cfg::function::set_connect_server_id\(\)](https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.set_connect_server_id)
