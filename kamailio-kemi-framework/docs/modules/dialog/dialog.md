# dialog #

* 📖[kamailio.cfg::module::dialog.html](https://kamailio.org/docs/modules/devel/modules/dialog.html)

Exported functions:

* [KSR.dialog.dlg_bridge\(\)](#ksrdialogdlg_bridge)
* [KSR.dialog.dlg_bye\(\)](#ksrdialogdlg_bye)
* [KSR.dialog.dlg_db_load_callid\(\)](#ksrdialogdlg_db_load_callid)
* [KSR.dialog.dlg_db_load_extra\(\)](#ksrdialogdlg_db_load_extra)
* [KSR.dialog.dlg_get\(\)](#ksrdialogdlg_get)
* [KSR.dialog.dlg_get_var\(\)](#ksrdialogdlg_get_var)
* [KSR.dialog.dlg_isflagset\(\)](#ksrdialogdlg_isflagset)
* [KSR.dialog.dlg_manage\(\)](#ksrdialogdlg_manage)
* [KSR.dialog.dlg_refer_cid\(\)](#ksrdialogdlg_refer_cid)
* [KSR.dialog.dlg_refer_did\(\)](#ksrdialogdlg_refer_did)
* [KSR.dialog.dlg_remove_dialogs_from_node\(\)](#ksrdialogdlg_remove_dialogs_from_node)
* [KSR.dialog.dlg_req_within2\(\)](#ksrdialogdlg_req_within2)
* [KSR.dialog.dlg_req_within3\(\)](#ksrdialogdlg_req_within3)
* [KSR.dialog.dlg_req_within4\(\)](#ksrdialogdlg_req_within4)
* [KSR.dialog.dlg_req_within5\(\)](#ksrdialogdlg_req_within5)
* [KSR.dialog.dlg_reset_property\(\)](#ksrdialogdlg_reset_property)
* [KSR.dialog.dlg_resetflag\(\)](#ksrdialogdlg_resetflag)
* [KSR.dialog.dlg_set_property\(\)](#ksrdialogdlg_set_property)
* [KSR.dialog.dlg_set_state\(\)](#ksrdialogdlg_set_state)
* [KSR.dialog.dlg_set_timeout\(\)](#ksrdialogdlg_set_timeout)
* [KSR.dialog.dlg_set_timeout_id\(\)](#ksrdialogdlg_set_timeout_id)
* [KSR.dialog.dlg_set_var\(\)](#ksrdialogdlg_set_var)
* [KSR.dialog.dlg_setflag\(\)](#ksrdialogdlg_setflag)
* [KSR.dialog.dlg_update_contact\(\)](#ksrdialogdlg_update_contact)
* [KSR.dialog.dlg_update_socket\(\)](#ksrdialogdlg_update_socket)
* [KSR.dialog.dlg_update_state\(\)](#ksrdialogdlg_update_state)
* [KSR.dialog.get_profile_size\(\)](#ksrdialogget_profile_size)
* [KSR.dialog.get_profile_size_static\(\)](#ksrdialogget_profile_size_static)
* [KSR.dialog.is_in_profile\(\)](#ksrdialogis_in_profile)
* [KSR.dialog.is_in_profile_static\(\)](#ksrdialogis_in_profile_static)
* [KSR.dialog.is_known_dlg\(\)](#ksrdialogis_known_dlg)
* [KSR.dialog.set_dlg_profile\(\)](#ksrdialogset_dlg_profile)
* [KSR.dialog.set_dlg_profile_static\(\)](#ksrdialogset_dlg_profile_static)
* [KSR.dialog.unset_dlg_profile\(\)](#ksrdialogunset_dlg_profile)
* [KSR.dialog.unset_dlg_profile_static\(\)](#ksrdialogunset_dlg_profile_static)
* [KSR.dialog.var_get\(\)](#ksrdialogvar_get)
* [KSR.dialog.var_gete\(\)](#ksrdialogvar_gete)
* [KSR.dialog.var_getw\(\)](#ksrdialogvar_getw)
* [KSR.dialog.var_is_null\(\)](#ksrdialogvar_is_null)
* [KSR.dialog.var_rm\(\)](#ksrdialogvar_rm)
* [KSR.dialog.var_sets\(\)](#ksrdialogvar_sets)

## KSR.dialog.dlg_bridge ##

```cpp
int KSR.dialog.dlg_bridge(str "sfrom", str "sto", str "soproxy");
```

* 📖[kamailio.cfg::function::dlg_bridge\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bridge)

## KSR.dialog.dlg_bye ##

```cpp
int KSR.dialog.dlg_bye(str "side");
```

* 📖[kamailio.cfg::function::dlg_bye\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bye)

## KSR.dialog.dlg_db_load_callid ##

```cpp
int KSR.dialog.dlg_db_load_callid(str "callid");
```

* 📖[kamailio.cfg::function::dlg_db_load_callid\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_callid)

## KSR.dialog.dlg_db_load_extra ##

```cpp
int KSR.dialog.dlg_db_load_extra();
```

* 📖[kamailio.cfg::function::dlg_db_load_extra\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_extra)

## KSR.dialog.dlg_get ##

```cpp
int KSR.dialog.dlg_get(str "sc", str "sf", str "st");
```

* 📖[kamailio.cfg::function::dlg_get\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_get)

## KSR.dialog.dlg_get_var ##

```cpp
xval KSR.dialog.dlg_get_var(str "sc", str "sf", str "st", str "key");
```

* 📖[kamailio.cfg::function::dlg_get_var\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_get_var)

## KSR.dialog.dlg_isflagset ##

```cpp
int KSR.dialog.dlg_isflagset(int val);
```

* 📖[kamailio.cfg::function::dlg_isflagset\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_isflagset)

## KSR.dialog.dlg_manage ##

```cpp
int KSR.dialog.dlg_manage();
```

* 📖[kamailio.cfg::function::dlg_manage\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_manage)

## KSR.dialog.dlg_refer_cid ##

```cpp
int KSR.dialog.dlg_refer_cid(str "callid", str "side", str "to");
```

* 📖[kamailio.cfg::function::dlg_refer_cid\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_refer_cid)

## KSR.dialog.dlg_refer_did ##

```cpp
int KSR.dialog.dlg_refer_did(int h_entry, int h_id, str "side", str "to");
```

* 📖[kamailio.cfg::function::dlg_refer_did\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_refer_did)

## KSR.dialog.dlg_remove_dialogs_from_node ##

```cpp
int KSR.dialog.dlg_remove_dialogs_from_node(str "node_uri");
```

* 📖[kamailio.cfg::function::dlg_remove_dialogs_from_node\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_remove_dialogs_from_node)

## KSR.dialog.dlg_req_within2 ##

```cpp
int KSR.dialog.dlg_req_within2(str "side", str "method");
```

* 📖[kamailio.cfg::function::dlg_req_within2\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_req_within2)

## KSR.dialog.dlg_req_within3 ##

```cpp
int KSR.dialog.dlg_req_within3(str "side", str "method", str "headers");
```

* 📖[kamailio.cfg::function::dlg_req_within3\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_req_within3)

## KSR.dialog.dlg_req_within4 ##

```cpp
int KSR.dialog.dlg_req_within4(str "side", str "method", str "content_type", str "content");
```

* 📖[kamailio.cfg::function::dlg_req_within4\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_req_within4)

## KSR.dialog.dlg_req_within5 ##

```cpp
int KSR.dialog.dlg_req_within5(str "side", str "method", str "headers", str "content_type", str "content");
```

* 📖[kamailio.cfg::function::dlg_req_within5\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_req_within5)

## KSR.dialog.dlg_reset_property ##

```cpp
int KSR.dialog.dlg_reset_property(str "pval");
```

* 📖[kamailio.cfg::function::dlg_reset_property\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_reset_property)

## KSR.dialog.dlg_resetflag ##

```cpp
int KSR.dialog.dlg_resetflag(int val);
```

* 📖[kamailio.cfg::function::dlg_resetflag\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_resetflag)

## KSR.dialog.dlg_set_property ##

```cpp
int KSR.dialog.dlg_set_property(str "pval");
```

* 📖[kamailio.cfg::function::dlg_set_property\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_property)

## KSR.dialog.dlg_set_state ##

```cpp
int KSR.dialog.dlg_set_state(str "state");
```

* 📖[kamailio.cfg::function::dlg_set_state\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_state)

## KSR.dialog.dlg_set_timeout ##

```cpp
int KSR.dialog.dlg_set_timeout(int to);
```

* 📖[kamailio.cfg::function::dlg_set_timeout\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout)

## KSR.dialog.dlg_set_timeout_id ##

```cpp
int KSR.dialog.dlg_set_timeout_id(int to, int he, int hi);
```

* 📖[kamailio.cfg::function::dlg_set_timeout_id\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout_id)

## KSR.dialog.dlg_set_var ##

```cpp
int KSR.dialog.dlg_set_var(str "sc", str "sf", str "st", str "key", str "val");
```

* 📖[kamailio.cfg::function::dlg_set_var\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_var)

## KSR.dialog.dlg_setflag ##

```cpp
int KSR.dialog.dlg_setflag(int val);
```

* 📖[kamailio.cfg::function::dlg_setflag\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_setflag)

## KSR.dialog.dlg_update_contact ##

```cpp
int KSR.dialog.dlg_update_contact();
```

* 📖[kamailio.cfg::function::dlg_update_contact\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_update_contact)

## KSR.dialog.dlg_update_socket ##

```cpp
int KSR.dialog.dlg_update_socket();
```

* 📖[kamailio.cfg::function::dlg_update_socket\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_update_socket)

## KSR.dialog.dlg_update_state ##

```cpp
int KSR.dialog.dlg_update_state();
```

* 📖[kamailio.cfg::function::dlg_update_state\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_update_state)

## KSR.dialog.get_profile_size ##

```cpp
int KSR.dialog.get_profile_size(str "sprofile", str "svalue", str "spv");
```

* 📖[kamailio.cfg::function::get_profile_size\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size)

## KSR.dialog.get_profile_size_static ##

```cpp
int KSR.dialog.get_profile_size_static(str "sprofile", str "spv");
```

* 📖[kamailio.cfg::function::get_profile_size_static\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size_static)

## KSR.dialog.is_in_profile ##

```cpp
int KSR.dialog.is_in_profile(str "sprofile", str "svalue");
```

* 📖[kamailio.cfg::function::is_in_profile\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile)

## KSR.dialog.is_in_profile_static ##

```cpp
int KSR.dialog.is_in_profile_static(str "sprofile");
```

* 📖[kamailio.cfg::function::is_in_profile_static\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile_static)

## KSR.dialog.is_known_dlg ##

```cpp
int KSR.dialog.is_known_dlg();
```

* 📖[kamailio.cfg::function::is_known_dlg\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_known_dlg)

## KSR.dialog.set_dlg_profile ##

```cpp
int KSR.dialog.set_dlg_profile(str "sprofile", str "svalue");
```

* 📖[kamailio.cfg::function::set_dlg_profile\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile)

## KSR.dialog.set_dlg_profile_static ##

```cpp
int KSR.dialog.set_dlg_profile_static(str "sprofile");
```

* 📖[kamailio.cfg::function::set_dlg_profile_static\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile_static)

## KSR.dialog.unset_dlg_profile ##

```cpp
int KSR.dialog.unset_dlg_profile(str "sprofile", str "svalue");
```

* 📖[kamailio.cfg::function::unset_dlg_profile\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile)

## KSR.dialog.unset_dlg_profile_static ##

```cpp
int KSR.dialog.unset_dlg_profile_static(str "sprofile");
```

* 📖[kamailio.cfg::function::unset_dlg_profile_static\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile_static)

## KSR.dialog.var_get ##

```cpp
xval KSR.dialog.var_get(str "name");
```

* 📖[kamailio.cfg::function::var_get\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_get)

## KSR.dialog.var_gete ##

```cpp
xval KSR.dialog.var_gete(str "name");
```

* 📖[kamailio.cfg::function::var_gete\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_gete)

## KSR.dialog.var_getw ##

```cpp
xval KSR.dialog.var_getw(str "name");
```

* 📖[kamailio.cfg::function::var_getw\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_getw)

## KSR.dialog.var_is_null ##

```cpp
int KSR.dialog.var_is_null(str "name");
```

* 📖[kamailio.cfg::function::var_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_is_null)

## KSR.dialog.var_rm ##

```cpp
int KSR.dialog.var_rm(str "name");
```

* 📖[kamailio.cfg::function::var_rm\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_rm)

## KSR.dialog.var_sets ##

```cpp
int KSR.dialog.var_sets(str "name", str "val");
```

* 📖[kamailio.cfg::function::var_sets\(\)](https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_sets)
