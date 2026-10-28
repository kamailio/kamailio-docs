# registrar #

* 📖[kamailio.cfg::module::registrar.html](https://kamailio.org/docs/modules/devel/modules/registrar.html)

Exported functions:

* [KSR.registrar.add_sock_hdr\(\)](#ksrregistraradd_sock_hdr)
* [KSR.registrar.lookup\(\)](#ksrregistrarlookup)
* [KSR.registrar.lookup_branches\(\)](#ksrregistrarlookup_branches)
* [KSR.registrar.lookup_to_dset\(\)](#ksrregistrarlookup_to_dset)
* [KSR.registrar.lookup_uri\(\)](#ksrregistrarlookup_uri)
* [KSR.registrar.lookup_xavp\(\)](#ksrregistrarlookup_xavp)
* [KSR.registrar.reg_fetch_contacts\(\)](#ksrregistrarreg_fetch_contacts)
* [KSR.registrar.reg_free_contacts\(\)](#ksrregistrarreg_free_contacts)
* [KSR.registrar.reg_from_user\(\)](#ksrregistrarreg_from_user)
* [KSR.registrar.reg_send_reply\(\)](#ksrregistrarreg_send_reply)
* [KSR.registrar.registered\(\)](#ksrregistrarregistered)
* [KSR.registrar.registered_action\(\)](#ksrregistrarregistered_action)
* [KSR.registrar.registered_flags\(\)](#ksrregistrarregistered_flags)
* [KSR.registrar.registered_uri\(\)](#ksrregistrarregistered_uri)
* [KSR.registrar.save\(\)](#ksrregistrarsave)
* [KSR.registrar.save_uri\(\)](#ksrregistrarsave_uri)
* [KSR.registrar.set_q_override\(\)](#ksrregistrarset_q_override)
* [KSR.registrar.ulc_cget\(\)](#ksrregistrarulc_cget)
* [KSR.registrar.ulc_rget\(\)](#ksrregistrarulc_rget)
* [KSR.registrar.unregister\(\)](#ksrregistrarunregister)
* [KSR.registrar.unregister_ruid\(\)](#ksrregistrarunregister_ruid)

## KSR.registrar.add_sock_hdr ##

```cpp
int KSR.registrar.add_sock_hdr(str "hdr_name");
```

* 📖[kamailio.cfg::function::add_sock_hdr\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.add_sock_hdr)

## KSR.registrar.lookup ##

```cpp
int KSR.registrar.lookup(str "table");
```

* 📖[kamailio.cfg::function::lookup\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup)

## KSR.registrar.lookup_branches ##

```cpp
int KSR.registrar.lookup_branches(str "_dtable");
```

* 📖[kamailio.cfg::function::lookup_branches\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_branches)

## KSR.registrar.lookup_to_dset ##

```cpp
int KSR.registrar.lookup_to_dset(str "table", str "uri");
```

* 📖[kamailio.cfg::function::lookup_to_dset\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_to_dset)

## KSR.registrar.lookup_uri ##

```cpp
int KSR.registrar.lookup_uri(str "table", str "uri");
```

* 📖[kamailio.cfg::function::lookup_uri\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_uri)

## KSR.registrar.lookup_xavp ##

```cpp
int KSR.registrar.lookup_xavp(str "utname", str "uri", str "rxname", str "cxname");
```

* 📖[kamailio.cfg::function::lookup_xavp\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_xavp)

## KSR.registrar.reg_fetch_contacts ##

```cpp
int KSR.registrar.reg_fetch_contacts(str "dtable", str "uri", str "profile");
```

* 📖[kamailio.cfg::function::reg_fetch_contacts\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_fetch_contacts)

## KSR.registrar.reg_free_contacts ##

```cpp
int KSR.registrar.reg_free_contacts(str "profile");
```

* 📖[kamailio.cfg::function::reg_free_contacts\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_free_contacts)

## KSR.registrar.reg_from_user ##

```cpp
int KSR.registrar.reg_from_user(str "utname", str "uri", int vmode);
```

* 📖[kamailio.cfg::function::reg_from_user\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_from_user)

## KSR.registrar.reg_send_reply ##

```cpp
int KSR.registrar.reg_send_reply();
```

* 📖[kamailio.cfg::function::reg_send_reply\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_send_reply)

## KSR.registrar.registered ##

```cpp
int KSR.registrar.registered(str "table");
```

* 📖[kamailio.cfg::function::registered\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered)

## KSR.registrar.registered_action ##

```cpp
int KSR.registrar.registered_action(str "_dtable", str "_uri", int _f, int _aflags);
```

* 📖[kamailio.cfg::function::registered_action\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_action)

## KSR.registrar.registered_flags ##

```cpp
int KSR.registrar.registered_flags(str "_dtable", str "_uri", int _f);
```

* 📖[kamailio.cfg::function::registered_flags\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_flags)

## KSR.registrar.registered_uri ##

```cpp
int KSR.registrar.registered_uri(str "_dtable", str "_uri");
```

* 📖[kamailio.cfg::function::registered_uri\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_uri)

## KSR.registrar.save ##

```cpp
int KSR.registrar.save(str "table", int flags);
```

* 📖[kamailio.cfg::function::save\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save)

## KSR.registrar.save_uri ##

```cpp
int KSR.registrar.save_uri(str "table", int flags, str "uri");
```

* 📖[kamailio.cfg::function::save_uri\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save_uri)

## KSR.registrar.set_q_override ##

```cpp
int KSR.registrar.set_q_override(str "new_q");
```

* 📖[kamailio.cfg::function::set_q_override\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.set_q_override)

## KSR.registrar.ulc_cget ##

```cpp
xval KSR.registrar.ulc_cget(str "rid", str "attr", int idx);
```

* 📖[kamailio.cfg::function::ulc_cget\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.ulc_cget)

## KSR.registrar.ulc_rget ##

```cpp
xval KSR.registrar.ulc_rget(str "rid", str "attr");
```

* 📖[kamailio.cfg::function::ulc_rget\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.ulc_rget)

## KSR.registrar.unregister ##

```cpp
int KSR.registrar.unregister(str "_dtable", str "_uri");
```

* 📖[kamailio.cfg::function::unregister\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister)

## KSR.registrar.unregister_ruid ##

```cpp
int KSR.registrar.unregister_ruid(str "_dtable", str "_uri", str "_ruid");
```

* 📖[kamailio.cfg::function::unregister_ruid\(\)](https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister_ruid)
