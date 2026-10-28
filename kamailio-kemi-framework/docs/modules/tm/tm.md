# tm #

* 📖[kamailio.cfg::module::tm.html](https://kamailio.org/docs/modules/devel/modules/tm.html)

Exported functions:

* [KSR.tm.ki_t_load_contacts_mode\(\)](#ksrtmki_t_load_contacts_mode)
* [KSR.tm.t_any_replied\(\)](#ksrtmt_any_replied)
* [KSR.tm.t_any_timeout\(\)](#ksrtmt_any_timeout)
* [KSR.tm.t_branch_replied\(\)](#ksrtmt_branch_replied)
* [KSR.tm.t_branch_timeout\(\)](#ksrtmt_branch_timeout)
* [KSR.tm.t_check_status\(\)](#ksrtmt_check_status)
* [KSR.tm.t_check_trans\(\)](#ksrtmt_check_trans)
* [KSR.tm.t_clean\(\)](#ksrtmt_clean)
* [KSR.tm.t_drop_replies\(\)](#ksrtmt_drop_replies)
* [KSR.tm.t_drop_replies_all\(\)](#ksrtmt_drop_replies_all)
* [KSR.tm.t_exists\(\)](#ksrtmt_exists)
* [KSR.tm.t_get_branch_index\(\)](#ksrtmt_get_branch_index)
* [KSR.tm.t_get_status_code\(\)](#ksrtmt_get_status_code)
* [KSR.tm.t_grep_status\(\)](#ksrtmt_grep_status)
* [KSR.tm.t_is_canceled\(\)](#ksrtmt_is_canceled)
* [KSR.tm.t_is_expired\(\)](#ksrtmt_is_expired)
* [KSR.tm.t_is_retr_async_reply\(\)](#ksrtmt_is_retr_async_reply)
* [KSR.tm.t_is_set\(\)](#ksrtmt_is_set)
* [KSR.tm.t_load_contacts\(\)](#ksrtmt_load_contacts)
* [KSR.tm.t_lookup_cancel\(\)](#ksrtmt_lookup_cancel)
* [KSR.tm.t_lookup_cancel_flags\(\)](#ksrtmt_lookup_cancel_flags)
* [KSR.tm.t_lookup_request\(\)](#ksrtmt_lookup_request)
* [KSR.tm.t_newtran\(\)](#ksrtmt_newtran)
* [KSR.tm.t_next_contact_flow\(\)](#ksrtmt_next_contact_flow)
* [KSR.tm.t_next_contacts\(\)](#ksrtmt_next_contacts)
* [KSR.tm.t_on_branch\(\)](#ksrtmt_on_branch)
* [KSR.tm.t_on_branch_failure\(\)](#ksrtmt_on_branch_failure)
* [KSR.tm.t_on_failure\(\)](#ksrtmt_on_failure)
* [KSR.tm.t_on_reply\(\)](#ksrtmt_on_reply)
* [KSR.tm.t_relay\(\)](#ksrtmt_relay)
* [KSR.tm.t_relay_to_flags\(\)](#ksrtmt_relay_to_flags)
* [KSR.tm.t_relay_to_proto\(\)](#ksrtmt_relay_to_proto)
* [KSR.tm.t_relay_to_proto_addr\(\)](#ksrtmt_relay_to_proto_addr)
* [KSR.tm.t_relay_to_proxy\(\)](#ksrtmt_relay_to_proxy)
* [KSR.tm.t_relay_to_proxy_flags\(\)](#ksrtmt_relay_to_proxy_flags)
* [KSR.tm.t_release\(\)](#ksrtmt_release)
* [KSR.tm.t_replicate\(\)](#ksrtmt_replicate)
* [KSR.tm.t_reply\(\)](#ksrtmt_reply)
* [KSR.tm.t_reply_error\(\)](#ksrtmt_reply_error)
* [KSR.tm.t_reset_fr\(\)](#ksrtmt_reset_fr)
* [KSR.tm.t_reset_max_lifetime\(\)](#ksrtmt_reset_max_lifetime)
* [KSR.tm.t_reset_retr\(\)](#ksrtmt_reset_retr)
* [KSR.tm.t_retransmit_reply\(\)](#ksrtmt_retransmit_reply)
* [KSR.tm.t_save_lumps\(\)](#ksrtmt_save_lumps)
* [KSR.tm.t_send_reply\(\)](#ksrtmt_send_reply)
* [KSR.tm.t_set_auto_inv_100\(\)](#ksrtmt_set_auto_inv_100)
* [KSR.tm.t_set_disable_6xx\(\)](#ksrtmt_set_disable_6xx)
* [KSR.tm.t_set_disable_failover\(\)](#ksrtmt_set_disable_failover)
* [KSR.tm.t_set_disable_internal_reply\(\)](#ksrtmt_set_disable_internal_reply)
* [KSR.tm.t_set_fr\(\)](#ksrtmt_set_fr)
* [KSR.tm.t_set_fr_inv\(\)](#ksrtmt_set_fr_inv)
* [KSR.tm.t_set_max_lifetime\(\)](#ksrtmt_set_max_lifetime)
* [KSR.tm.t_set_no_auto_ack\(\)](#ksrtmt_set_no_auto_ack)
* [KSR.tm.t_set_no_e2e_cancel_reason\(\)](#ksrtmt_set_no_e2e_cancel_reason)
* [KSR.tm.t_set_retr\(\)](#ksrtmt_set_retr)
* [KSR.tm.t_uac_send\(\)](#ksrtmt_uac_send)
* [KSR.tm.t_use_uac_headers\(\)](#ksrtmt_use_uac_headers)

## KSR.tm.ki_t_load_contacts_mode ##

```cpp
int KSR.tm.ki_t_load_contacts_mode(int mode);
```

* 📖[kamailio.cfg::function::ki_t_load_contacts_mode\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.ki_t_load_contacts_mode)

## KSR.tm.t_any_replied ##

```cpp
int KSR.tm.t_any_replied();
```

* 📖[kamailio.cfg::function::t_any_replied\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_replied)

## KSR.tm.t_any_timeout ##

```cpp
int KSR.tm.t_any_timeout();
```

* 📖[kamailio.cfg::function::t_any_timeout\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_timeout)

## KSR.tm.t_branch_replied ##

```cpp
int KSR.tm.t_branch_replied();
```

* 📖[kamailio.cfg::function::t_branch_replied\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_replied)

## KSR.tm.t_branch_timeout ##

```cpp
int KSR.tm.t_branch_timeout();
```

* 📖[kamailio.cfg::function::t_branch_timeout\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_timeout)

## KSR.tm.t_check_status ##

```cpp
int KSR.tm.t_check_status(str "sexp");
```

* 📖[kamailio.cfg::function::t_check_status\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_status)

## KSR.tm.t_check_trans ##

```cpp
int KSR.tm.t_check_trans();
```

* 📖[kamailio.cfg::function::t_check_trans\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_trans)

## KSR.tm.t_clean ##

```cpp
int KSR.tm.t_clean();
```

* 📖[kamailio.cfg::function::t_clean\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_clean)

## KSR.tm.t_drop_replies ##

```cpp
int KSR.tm.t_drop_replies(str "mode");
```

* 📖[kamailio.cfg::function::t_drop_replies\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies)

## KSR.tm.t_drop_replies_all ##

```cpp
int KSR.tm.t_drop_replies_all();
```

* 📖[kamailio.cfg::function::t_drop_replies_all\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies_all)

## KSR.tm.t_exists ##

```cpp
int KSR.tm.t_exists();
```

* 📖[kamailio.cfg::function::t_exists\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_exists)

## KSR.tm.t_get_branch_index ##

```cpp
int KSR.tm.t_get_branch_index();
```

* 📖[kamailio.cfg::function::t_get_branch_index\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_branch_index)

## KSR.tm.t_get_status_code ##

```cpp
int KSR.tm.t_get_status_code();
```

* 📖[kamailio.cfg::function::t_get_status_code\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_status_code)

## KSR.tm.t_grep_status ##

```cpp
int KSR.tm.t_grep_status(int code);
```

* 📖[kamailio.cfg::function::t_grep_status\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_grep_status)

## KSR.tm.t_is_canceled ##

```cpp
int KSR.tm.t_is_canceled();
```

* 📖[kamailio.cfg::function::t_is_canceled\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_canceled)

## KSR.tm.t_is_expired ##

```cpp
int KSR.tm.t_is_expired();
```

* 📖[kamailio.cfg::function::t_is_expired\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_expired)

## KSR.tm.t_is_retr_async_reply ##

```cpp
int KSR.tm.t_is_retr_async_reply();
```

* 📖[kamailio.cfg::function::t_is_retr_async_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_retr_async_reply)

## KSR.tm.t_is_set ##

```cpp
int KSR.tm.t_is_set(str "target");
```

* 📖[kamailio.cfg::function::t_is_set\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_set)

## KSR.tm.t_load_contacts ##

```cpp
int KSR.tm.t_load_contacts();
```

* 📖[kamailio.cfg::function::t_load_contacts\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_load_contacts)

## KSR.tm.t_lookup_cancel ##

```cpp
int KSR.tm.t_lookup_cancel();
```

* 📖[kamailio.cfg::function::t_lookup_cancel\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel)

## KSR.tm.t_lookup_cancel_flags ##

```cpp
int KSR.tm.t_lookup_cancel_flags(int flags);
```

* 📖[kamailio.cfg::function::t_lookup_cancel_flags\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel_flags)

## KSR.tm.t_lookup_request ##

```cpp
int KSR.tm.t_lookup_request();
```

* 📖[kamailio.cfg::function::t_lookup_request\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_request)

## KSR.tm.t_newtran ##

```cpp
int KSR.tm.t_newtran();
```

* 📖[kamailio.cfg::function::t_newtran\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_newtran)

## KSR.tm.t_next_contact_flow ##

```cpp
int KSR.tm.t_next_contact_flow();
```

* 📖[kamailio.cfg::function::t_next_contact_flow\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contact_flow)

## KSR.tm.t_next_contacts ##

```cpp
int KSR.tm.t_next_contacts();
```

* 📖[kamailio.cfg::function::t_next_contacts\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contacts)

## KSR.tm.t_on_branch ##

```cpp
int KSR.tm.t_on_branch(str "rname");
```

* 📖[kamailio.cfg::function::t_on_branch\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch)

## KSR.tm.t_on_branch_failure ##

```cpp
int KSR.tm.t_on_branch_failure(str "rname");
```

* 📖[kamailio.cfg::function::t_on_branch_failure\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch_failure)

## KSR.tm.t_on_failure ##

```cpp
int KSR.tm.t_on_failure(str "rname");
```

* 📖[kamailio.cfg::function::t_on_failure\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_failure)

## KSR.tm.t_on_reply ##

```cpp
int KSR.tm.t_on_reply(str "rname");
```

* 📖[kamailio.cfg::function::t_on_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_reply)

## KSR.tm.t_relay ##

```cpp
int KSR.tm.t_relay();
```

* 📖[kamailio.cfg::function::t_relay\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay)

## KSR.tm.t_relay_to_flags ##

```cpp
int KSR.tm.t_relay_to_flags(int rflags);
```

* 📖[kamailio.cfg::function::t_relay_to_flags\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_flags)

## KSR.tm.t_relay_to_proto ##

```cpp
int KSR.tm.t_relay_to_proto(str "sproto");
```

* 📖[kamailio.cfg::function::t_relay_to_proto\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto)

## KSR.tm.t_relay_to_proto_addr ##

```cpp
int KSR.tm.t_relay_to_proto_addr(str "sproto", str "host", int port);
```

* 📖[kamailio.cfg::function::t_relay_to_proto_addr\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto_addr)

## KSR.tm.t_relay_to_proxy ##

```cpp
int KSR.tm.t_relay_to_proxy(str "sproxy");
```

* 📖[kamailio.cfg::function::t_relay_to_proxy\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy)

## KSR.tm.t_relay_to_proxy_flags ##

```cpp
int KSR.tm.t_relay_to_proxy_flags(str "sproxy", int rflags);
```

* 📖[kamailio.cfg::function::t_relay_to_proxy_flags\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy_flags)

## KSR.tm.t_release ##

```cpp
int KSR.tm.t_release();
```

* 📖[kamailio.cfg::function::t_release\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_release)

## KSR.tm.t_replicate ##

```cpp
int KSR.tm.t_replicate(str "suri");
```

* 📖[kamailio.cfg::function::t_replicate\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_replicate)

## KSR.tm.t_reply ##

```cpp
int KSR.tm.t_reply(int code, str "reason");
```

* 📖[kamailio.cfg::function::t_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reply)

## KSR.tm.t_reply_error ##

```cpp
int KSR.tm.t_reply_error();
```

* 📖[kamailio.cfg::function::t_reply_error\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reply_error)

## KSR.tm.t_reset_fr ##

```cpp
int KSR.tm.t_reset_fr();
```

* 📖[kamailio.cfg::function::t_reset_fr\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_fr)

## KSR.tm.t_reset_max_lifetime ##

```cpp
int KSR.tm.t_reset_max_lifetime();
```

* 📖[kamailio.cfg::function::t_reset_max_lifetime\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_max_lifetime)

## KSR.tm.t_reset_retr ##

```cpp
int KSR.tm.t_reset_retr();
```

* 📖[kamailio.cfg::function::t_reset_retr\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_retr)

## KSR.tm.t_retransmit_reply ##

```cpp
int KSR.tm.t_retransmit_reply();
```

* 📖[kamailio.cfg::function::t_retransmit_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_retransmit_reply)

## KSR.tm.t_save_lumps ##

```cpp
int KSR.tm.t_save_lumps();
```

* 📖[kamailio.cfg::function::t_save_lumps\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_save_lumps)

## KSR.tm.t_send_reply ##

```cpp
int KSR.tm.t_send_reply(int code, str "reason");
```

* 📖[kamailio.cfg::function::t_send_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_send_reply)

## KSR.tm.t_set_auto_inv_100 ##

```cpp
int KSR.tm.t_set_auto_inv_100(int state);
```

* 📖[kamailio.cfg::function::t_set_auto_inv_100\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_auto_inv_100)

## KSR.tm.t_set_disable_6xx ##

```cpp
int KSR.tm.t_set_disable_6xx(int state);
```

* 📖[kamailio.cfg::function::t_set_disable_6xx\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_6xx)

## KSR.tm.t_set_disable_failover ##

```cpp
int KSR.tm.t_set_disable_failover(int state);
```

* 📖[kamailio.cfg::function::t_set_disable_failover\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_failover)

## KSR.tm.t_set_disable_internal_reply ##

```cpp
int KSR.tm.t_set_disable_internal_reply(int state);
```

* 📖[kamailio.cfg::function::t_set_disable_internal_reply\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_internal_reply)

## KSR.tm.t_set_fr ##

```cpp
int KSR.tm.t_set_fr(int fr_inv, int fr);
```

* 📖[kamailio.cfg::function::t_set_fr\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr)

## KSR.tm.t_set_fr_inv ##

```cpp
int KSR.tm.t_set_fr_inv(int fr_inv);
```

* 📖[kamailio.cfg::function::t_set_fr_inv\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr_inv)

## KSR.tm.t_set_max_lifetime ##

```cpp
int KSR.tm.t_set_max_lifetime(int t1, int t2);
```

* 📖[kamailio.cfg::function::t_set_max_lifetime\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_max_lifetime)

## KSR.tm.t_set_no_auto_ack ##

```cpp
int KSR.tm.t_set_no_auto_ack(int state);
```

* 📖[kamailio.cfg::function::t_set_no_auto_ack\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_no_auto_ack)

## KSR.tm.t_set_no_e2e_cancel_reason ##

```cpp
int KSR.tm.t_set_no_e2e_cancel_reason(int state);
```

* 📖[kamailio.cfg::function::t_set_no_e2e_cancel_reason\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_no_e2e_cancel_reason)

## KSR.tm.t_set_retr ##

```cpp
int KSR.tm.t_set_retr(int t1, int t2);
```

* 📖[kamailio.cfg::function::t_set_retr\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_retr)

## KSR.tm.t_uac_send ##

```cpp
int KSR.tm.t_uac_send(str "method", str "ruri", str "nexthop", str "ssock", str "hdrs", str "body");
```

* 📖[kamailio.cfg::function::t_uac_send\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_uac_send)

## KSR.tm.t_use_uac_headers ##

```cpp
int KSR.tm.t_use_uac_headers();
```

* 📖[kamailio.cfg::function::t_use_uac_headers\(\)](https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_use_uac_headers)
