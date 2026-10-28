# corex #

* 📖[kamailio.cfg::module::corex.html](https://kamailio.org/docs/modules/devel/modules/corex.html)

Exported functions:

* [KSR.corex.append_branch\(\)](#ksrcorexappend_branch)
* [KSR.corex.append_branch_uri\(\)](#ksrcorexappend_branch_uri)
* [KSR.corex.append_branch_uri_q\(\)](#ksrcorexappend_branch_uri_q)
* [KSR.corex.file_read\(\)](#ksrcorexfile_read)
* [KSR.corex.file_write\(\)](#ksrcorexfile_write)
* [KSR.corex.forward_uac\(\)](#ksrcorexforward_uac)
* [KSR.corex.forward_uac_branch\(\)](#ksrcorexforward_uac_branch)
* [KSR.corex.forward_uac_uri\(\)](#ksrcorexforward_uac_uri)
* [KSR.corex.forward_uac_uri_branch\(\)](#ksrcorexforward_uac_uri_branch)
* [KSR.corex.has_ruri_user\(\)](#ksrcorexhas_ruri_user)
* [KSR.corex.has_user_agent\(\)](#ksrcorexhas_user_agent)
* [KSR.corex.is_faked_msg\(\)](#ksrcorexis_faked_msg)
* [KSR.corex.is_socket_name\(\)](#ksrcorexis_socket_name)
* [KSR.corex.isxflagset\(\)](#ksrcorexisxflagset)
* [KSR.corex.resetxflag\(\)](#ksrcorexresetxflag)
* [KSR.corex.send_data\(\)](#ksrcorexsend_data)
* [KSR.corex.sendx\(\)](#ksrcorexsendx)
* [KSR.corex.set_recv_socket\(\)](#ksrcorexset_recv_socket)
* [KSR.corex.set_recv_socket_name\(\)](#ksrcorexset_recv_socket_name)
* [KSR.corex.set_send_socket\(\)](#ksrcorexset_send_socket)
* [KSR.corex.set_send_socket_map\(\)](#ksrcorexset_send_socket_map)
* [KSR.corex.set_send_socket_name\(\)](#ksrcorexset_send_socket_name)
* [KSR.corex.set_source_address\(\)](#ksrcorexset_source_address)
* [KSR.corex.setxflag\(\)](#ksrcorexsetxflag)
* [KSR.corex.via_add_srvid\(\)](#ksrcorexvia_add_srvid)
* [KSR.corex.via_add_xavp_params\(\)](#ksrcorexvia_add_xavp_params)
* [KSR.corex.via_reply_add_xavp_params\(\)](#ksrcorexvia_reply_add_xavp_params)
* [KSR.corex.via_use_xavp_fields\(\)](#ksrcorexvia_use_xavp_fields)

## KSR.corex.append_branch ##

```cpp
int KSR.corex.append_branch();
```

* 📖[kamailio.cfg::function::append_branch\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch)

## KSR.corex.append_branch_uri ##

```cpp
int KSR.corex.append_branch_uri(str "uri");
```

* 📖[kamailio.cfg::function::append_branch_uri\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri)

## KSR.corex.append_branch_uri_q ##

```cpp
int KSR.corex.append_branch_uri_q(str "uri", str "q");
```

* 📖[kamailio.cfg::function::append_branch_uri_q\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri_q)

## KSR.corex.file_read ##

```cpp
xval KSR.corex.file_read(str "fname");
```

* 📖[kamailio.cfg::function::file_read\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_read)

## KSR.corex.file_write ##

```cpp
int KSR.corex.file_write(str "fname", str "fdata");
```

* 📖[kamailio.cfg::function::file_write\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_write)

## KSR.corex.forward_uac ##

```cpp
int KSR.corex.forward_uac();
```

* 📖[kamailio.cfg::function::forward_uac\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.forward_uac)

## KSR.corex.forward_uac_branch ##

```cpp
int KSR.corex.forward_uac_branch(int bindex);
```

* 📖[kamailio.cfg::function::forward_uac_branch\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.forward_uac_branch)

## KSR.corex.forward_uac_uri ##

```cpp
int KSR.corex.forward_uac_uri(str "vuri");
```

* 📖[kamailio.cfg::function::forward_uac_uri\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.forward_uac_uri)

## KSR.corex.forward_uac_uri_branch ##

```cpp
int KSR.corex.forward_uac_uri_branch(str "vuri", int bindex);
```

* 📖[kamailio.cfg::function::forward_uac_uri_branch\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.forward_uac_uri_branch)

## KSR.corex.has_ruri_user ##

```cpp
int KSR.corex.has_ruri_user();
```

* 📖[kamailio.cfg::function::has_ruri_user\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_ruri_user)

## KSR.corex.has_user_agent ##

```cpp
int KSR.corex.has_user_agent();
```

* 📖[kamailio.cfg::function::has_user_agent\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_user_agent)

## KSR.corex.is_faked_msg ##

```cpp
int KSR.corex.is_faked_msg();
```

* 📖[kamailio.cfg::function::is_faked_msg\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_faked_msg)

## KSR.corex.is_socket_name ##

```cpp
int KSR.corex.is_socket_name(str "sockname");
```

* 📖[kamailio.cfg::function::is_socket_name\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_socket_name)

## KSR.corex.isxflagset ##

```cpp
int KSR.corex.isxflagset(int fval);
```

* 📖[kamailio.cfg::function::isxflagset\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.isxflagset)

## KSR.corex.resetxflag ##

```cpp
int KSR.corex.resetxflag(int fval);
```

* 📖[kamailio.cfg::function::resetxflag\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.resetxflag)

## KSR.corex.send_data ##

```cpp
int KSR.corex.send_data(str "uri", str "data");
```

* 📖[kamailio.cfg::function::send_data\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.send_data)

## KSR.corex.sendx ##

```cpp
int KSR.corex.sendx(str "uri", str "sock", str "data");
```

* 📖[kamailio.cfg::function::sendx\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.sendx)

## KSR.corex.set_recv_socket ##

```cpp
int KSR.corex.set_recv_socket(str "ssock");
```

* 📖[kamailio.cfg::function::set_recv_socket\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket)

## KSR.corex.set_recv_socket_name ##

```cpp
int KSR.corex.set_recv_socket_name(str "ssock");
```

* 📖[kamailio.cfg::function::set_recv_socket_name\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket_name)

## KSR.corex.set_send_socket ##

```cpp
int KSR.corex.set_send_socket(str "ssock");
```

* 📖[kamailio.cfg::function::set_send_socket\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket)

## KSR.corex.set_send_socket_map ##

```cpp
int KSR.corex.set_send_socket_map(str "smap");
```

* 📖[kamailio.cfg::function::set_send_socket_map\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket_map)

## KSR.corex.set_send_socket_name ##

```cpp
int KSR.corex.set_send_socket_name(str "ssock");
```

* 📖[kamailio.cfg::function::set_send_socket_name\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket_name)

## KSR.corex.set_source_address ##

```cpp
int KSR.corex.set_source_address(str "saddr");
```

* 📖[kamailio.cfg::function::set_source_address\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_source_address)

## KSR.corex.setxflag ##

```cpp
int KSR.corex.setxflag(int fval);
```

* 📖[kamailio.cfg::function::setxflag\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.setxflag)

## KSR.corex.via_add_srvid ##

```cpp
int KSR.corex.via_add_srvid(int fval);
```

* 📖[kamailio.cfg::function::via_add_srvid\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_srvid)

## KSR.corex.via_add_xavp_params ##

```cpp
int KSR.corex.via_add_xavp_params(int fval);
```

* 📖[kamailio.cfg::function::via_add_xavp_params\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_xavp_params)

## KSR.corex.via_reply_add_xavp_params ##

```cpp
int KSR.corex.via_reply_add_xavp_params(int fval);
```

* 📖[kamailio.cfg::function::via_reply_add_xavp_params\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_reply_add_xavp_params)

## KSR.corex.via_use_xavp_fields ##

```cpp
int KSR.corex.via_use_xavp_fields(int fval);
```

* 📖[kamailio.cfg::function::via_use_xavp_fields\(\)](https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_use_xavp_fields)
