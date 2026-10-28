# pvx #

* 📖[kamailio.cfg::module::pv.html](https://kamailio.org/docs/modules/devel/modules/pv.html)

Exported functions:

* [KSR.pvx.avp_get\(\)](#ksrpvxavp_get)
* [KSR.pvx.avp_gete\(\)](#ksrpvxavp_gete)
* [KSR.pvx.avp_getw\(\)](#ksrpvxavp_getw)
* [KSR.pvx.avp_is_null\(\)](#ksrpvxavp_is_null)
* [KSR.pvx.avp_rm\(\)](#ksrpvxavp_rm)
* [KSR.pvx.avp_seti\(\)](#ksrpvxavp_seti)
* [KSR.pvx.avp_sets\(\)](#ksrpvxavp_sets)
* [KSR.pvx.evalx\(\)](#ksrpvxevalx)
* [KSR.pvx.pv_var_to_xavp\(\)](#ksrpvxpv_var_to_xavp)
* [KSR.pvx.pv_xavi_print\(\)](#ksrpvxpv_xavi_print)
* [KSR.pvx.pv_xavp_print\(\)](#ksrpvxpv_xavp_print)
* [KSR.pvx.pv_xavp_to_var\(\)](#ksrpvxpv_xavp_to_var)
* [KSR.pvx.pv_xavu_print\(\)](#ksrpvxpv_xavu_print)
* [KSR.pvx.sbranch_append\(\)](#ksrpvxsbranch_append)
* [KSR.pvx.sbranch_reset\(\)](#ksrpvxsbranch_reset)
* [KSR.pvx.sbranch_set_ruri\(\)](#ksrpvxsbranch_set_ruri)
* [KSR.pvx.shv_get\(\)](#ksrpvxshv_get)
* [KSR.pvx.shv_seti\(\)](#ksrpvxshv_seti)
* [KSR.pvx.shv_sets\(\)](#ksrpvxshv_sets)
* [KSR.pvx.shvinc_get\(\)](#ksrpvxshvinc_get)
* [KSR.pvx.var_get\(\)](#ksrpvxvar_get)
* [KSR.pvx.var_seti\(\)](#ksrpvxvar_seti)
* [KSR.pvx.var_sets\(\)](#ksrpvxvar_sets)
* [KSR.pvx.xavi_child_get\(\)](#ksrpvxxavi_child_get)
* [KSR.pvx.xavi_child_gete\(\)](#ksrpvxxavi_child_gete)
* [KSR.pvx.xavi_child_getw\(\)](#ksrpvxxavi_child_getw)
* [KSR.pvx.xavi_child_is_null\(\)](#ksrpvxxavi_child_is_null)
* [KSR.pvx.xavi_child_rm\(\)](#ksrpvxxavi_child_rm)
* [KSR.pvx.xavi_child_seti\(\)](#ksrpvxxavi_child_seti)
* [KSR.pvx.xavi_child_sets\(\)](#ksrpvxxavi_child_sets)
* [KSR.pvx.xavi_get\(\)](#ksrpvxxavi_get)
* [KSR.pvx.xavi_get_keys\(\)](#ksrpvxxavi_get_keys)
* [KSR.pvx.xavi_getd\(\)](#ksrpvxxavi_getd)
* [KSR.pvx.xavi_getd_p1\(\)](#ksrpvxxavi_getd_p1)
* [KSR.pvx.xavi_gete\(\)](#ksrpvxxavi_gete)
* [KSR.pvx.xavi_getw\(\)](#ksrpvxxavi_getw)
* [KSR.pvx.xavi_is_null\(\)](#ksrpvxxavi_is_null)
* [KSR.pvx.xavi_rm\(\)](#ksrpvxxavi_rm)
* [KSR.pvx.xavi_rm_all\(\)](#ksrpvxxavi_rm_all)
* [KSR.pvx.xavi_seti\(\)](#ksrpvxxavi_seti)
* [KSR.pvx.xavi_sets\(\)](#ksrpvxxavi_sets)
* [KSR.pvx.xavp_child_get\(\)](#ksrpvxxavp_child_get)
* [KSR.pvx.xavp_child_gete\(\)](#ksrpvxxavp_child_gete)
* [KSR.pvx.xavp_child_getw\(\)](#ksrpvxxavp_child_getw)
* [KSR.pvx.xavp_child_is_null\(\)](#ksrpvxxavp_child_is_null)
* [KSR.pvx.xavp_child_rm\(\)](#ksrpvxxavp_child_rm)
* [KSR.pvx.xavp_child_seti\(\)](#ksrpvxxavp_child_seti)
* [KSR.pvx.xavp_child_sets\(\)](#ksrpvxxavp_child_sets)
* [KSR.pvx.xavp_copy\(\)](#ksrpvxxavp_copy)
* [KSR.pvx.xavp_copy_dst\(\)](#ksrpvxxavp_copy_dst)
* [KSR.pvx.xavp_get\(\)](#ksrpvxxavp_get)
* [KSR.pvx.xavp_get_keys\(\)](#ksrpvxxavp_get_keys)
* [KSR.pvx.xavp_getd\(\)](#ksrpvxxavp_getd)
* [KSR.pvx.xavp_getd_p1\(\)](#ksrpvxxavp_getd_p1)
* [KSR.pvx.xavp_gete\(\)](#ksrpvxxavp_gete)
* [KSR.pvx.xavp_getw\(\)](#ksrpvxxavp_getw)
* [KSR.pvx.xavp_is_null\(\)](#ksrpvxxavp_is_null)
* [KSR.pvx.xavp_lshift\(\)](#ksrpvxxavp_lshift)
* [KSR.pvx.xavp_params_explode\(\)](#ksrpvxxavp_params_explode)
* [KSR.pvx.xavp_params_implode\(\)](#ksrpvxxavp_params_implode)
* [KSR.pvx.xavp_params_implode_qval\(\)](#ksrpvxxavp_params_implode_qval)
* [KSR.pvx.xavp_push_dst\(\)](#ksrpvxxavp_push_dst)
* [KSR.pvx.xavp_rm\(\)](#ksrpvxxavp_rm)
* [KSR.pvx.xavp_rm_all\(\)](#ksrpvxxavp_rm_all)
* [KSR.pvx.xavp_seti\(\)](#ksrpvxxavp_seti)
* [KSR.pvx.xavp_sets\(\)](#ksrpvxxavp_sets)
* [KSR.pvx.xavp_slist_explode\(\)](#ksrpvxxavp_slist_explode)
* [KSR.pvx.xavp_xparams_explode\(\)](#ksrpvxxavp_xparams_explode)
* [KSR.pvx.xavu_child_get\(\)](#ksrpvxxavu_child_get)
* [KSR.pvx.xavu_child_gete\(\)](#ksrpvxxavu_child_gete)
* [KSR.pvx.xavu_child_getw\(\)](#ksrpvxxavu_child_getw)
* [KSR.pvx.xavu_child_is_null\(\)](#ksrpvxxavu_child_is_null)
* [KSR.pvx.xavu_child_rm\(\)](#ksrpvxxavu_child_rm)
* [KSR.pvx.xavu_child_seti\(\)](#ksrpvxxavu_child_seti)
* [KSR.pvx.xavu_child_sets\(\)](#ksrpvxxavu_child_sets)
* [KSR.pvx.xavu_get\(\)](#ksrpvxxavu_get)
* [KSR.pvx.xavu_gete\(\)](#ksrpvxxavu_gete)
* [KSR.pvx.xavu_getw\(\)](#ksrpvxxavu_getw)
* [KSR.pvx.xavu_is_null\(\)](#ksrpvxxavu_is_null)
* [KSR.pvx.xavu_params_explode\(\)](#ksrpvxxavu_params_explode)
* [KSR.pvx.xavu_params_implode\(\)](#ksrpvxxavu_params_implode)
* [KSR.pvx.xavu_rm\(\)](#ksrpvxxavu_rm)
* [KSR.pvx.xavu_seti\(\)](#ksrpvxxavu_seti)
* [KSR.pvx.xavu_sets\(\)](#ksrpvxxavu_sets)

## KSR.pvx.avp_get ##

```cpp
xval KSR.pvx.avp_get(str "xname");
```

* 📖[kamailio.cfg::function::avp_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_get)

## KSR.pvx.avp_gete ##

```cpp
xval KSR.pvx.avp_gete(str "xname");
```

* 📖[kamailio.cfg::function::avp_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_gete)

## KSR.pvx.avp_getw ##

```cpp
xval KSR.pvx.avp_getw(str "xname");
```

* 📖[kamailio.cfg::function::avp_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_getw)

## KSR.pvx.avp_is_null ##

```cpp
int KSR.pvx.avp_is_null(str "xname");
```

* 📖[kamailio.cfg::function::avp_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_is_null)

## KSR.pvx.avp_rm ##

```cpp
int KSR.pvx.avp_rm(str "xname");
```

* 📖[kamailio.cfg::function::avp_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_rm)

## KSR.pvx.avp_seti ##

```cpp
int KSR.pvx.avp_seti(str "xname", int vn);
```

* 📖[kamailio.cfg::function::avp_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_seti)

## KSR.pvx.avp_sets ##

```cpp
int KSR.pvx.avp_sets(str "xname", str "vs");
```

* 📖[kamailio.cfg::function::avp_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_sets)

## KSR.pvx.evalx ##

```cpp
int KSR.pvx.evalx(str "dst", str "fmt");
```

* 📖[kamailio.cfg::function::evalx\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.evalx)

## KSR.pvx.pv_var_to_xavp ##

```cpp
int KSR.pvx.pv_var_to_xavp(str "varname", str "xname");
```

* 📖[kamailio.cfg::function::pv_var_to_xavp\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_var_to_xavp)

## KSR.pvx.pv_xavi_print ##

```cpp
int KSR.pvx.pv_xavi_print();
```

* 📖[kamailio.cfg::function::pv_xavi_print\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavi_print)

## KSR.pvx.pv_xavp_print ##

```cpp
int KSR.pvx.pv_xavp_print();
```

* 📖[kamailio.cfg::function::pv_xavp_print\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavp_print)

## KSR.pvx.pv_xavp_to_var ##

```cpp
int KSR.pvx.pv_xavp_to_var(str "xname");
```

* 📖[kamailio.cfg::function::pv_xavp_to_var\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavp_to_var)

## KSR.pvx.pv_xavu_print ##

```cpp
int KSR.pvx.pv_xavu_print();
```

* 📖[kamailio.cfg::function::pv_xavu_print\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavu_print)

## KSR.pvx.sbranch_append ##

```cpp
int KSR.pvx.sbranch_append();
```

* 📖[kamailio.cfg::function::sbranch_append\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_append)

## KSR.pvx.sbranch_reset ##

```cpp
int KSR.pvx.sbranch_reset();
```

* 📖[kamailio.cfg::function::sbranch_reset\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_reset)

## KSR.pvx.sbranch_set_ruri ##

```cpp
int KSR.pvx.sbranch_set_ruri();
```

* 📖[kamailio.cfg::function::sbranch_set_ruri\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_set_ruri)

## KSR.pvx.shv_get ##

```cpp
xval KSR.pvx.shv_get(str "vname");
```

* 📖[kamailio.cfg::function::shv_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_get)

## KSR.pvx.shv_seti ##

```cpp
int KSR.pvx.shv_seti(str "vname", int ival);
```

* 📖[kamailio.cfg::function::shv_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_seti)

## KSR.pvx.shv_sets ##

```cpp
int KSR.pvx.shv_sets(str "vname", str "sval");
```

* 📖[kamailio.cfg::function::shv_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_sets)

## KSR.pvx.shvinc_get ##

```cpp
xval KSR.pvx.shvinc_get(str "vname");
```

* 📖[kamailio.cfg::function::shvinc_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shvinc_get)

## KSR.pvx.var_get ##

```cpp
xval KSR.pvx.var_get(str "vname");
```

* 📖[kamailio.cfg::function::var_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_get)

## KSR.pvx.var_seti ##

```cpp
int KSR.pvx.var_seti(str "vname", int ival);
```

* 📖[kamailio.cfg::function::var_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_seti)

## KSR.pvx.var_sets ##

```cpp
int KSR.pvx.var_sets(str "vname", str "sval");
```

* 📖[kamailio.cfg::function::var_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_sets)

## KSR.pvx.xavi_child_get ##

```cpp
xval KSR.pvx.xavi_child_get(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavi_child_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_get)

## KSR.pvx.xavi_child_gete ##

```cpp
xval KSR.pvx.xavi_child_gete(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavi_child_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_gete)

## KSR.pvx.xavi_child_getw ##

```cpp
xval KSR.pvx.xavi_child_getw(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavi_child_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_getw)

## KSR.pvx.xavi_child_is_null ##

```cpp
int KSR.pvx.xavi_child_is_null(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavi_child_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_is_null)

## KSR.pvx.xavi_child_rm ##

```cpp
int KSR.pvx.xavi_child_rm(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavi_child_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_rm)

## KSR.pvx.xavi_child_seti ##

```cpp
int KSR.pvx.xavi_child_seti(str "rname", str "cname", int ival);
```

* 📖[kamailio.cfg::function::xavi_child_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_seti)

## KSR.pvx.xavi_child_sets ##

```cpp
int KSR.pvx.xavi_child_sets(str "rname", str "cname", str "sval");
```

* 📖[kamailio.cfg::function::xavi_child_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_sets)

## KSR.pvx.xavi_get ##

```cpp
xval KSR.pvx.xavi_get(str "rname");
```

* 📖[kamailio.cfg::function::xavi_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_get)

## KSR.pvx.xavi_get_keys ##

```cpp
xval KSR.pvx.xavi_get_keys(str "rname", int indx);
```

* 📖[kamailio.cfg::function::xavi_get_keys\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_get_keys)

## KSR.pvx.xavi_getd ##

```cpp
xval KSR.pvx.xavi_getd(str "rname");
```

* 📖[kamailio.cfg::function::xavi_getd\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getd)

## KSR.pvx.xavi_getd_p1 ##

```cpp
xval KSR.pvx.xavi_getd_p1(str "rname", int indx);
```

* 📖[kamailio.cfg::function::xavi_getd_p1\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getd_p1)

## KSR.pvx.xavi_gete ##

```cpp
xval KSR.pvx.xavi_gete(str "rname");
```

* 📖[kamailio.cfg::function::xavi_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_gete)

## KSR.pvx.xavi_getw ##

```cpp
xval KSR.pvx.xavi_getw(str "rname");
```

* 📖[kamailio.cfg::function::xavi_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getw)

## KSR.pvx.xavi_is_null ##

```cpp
int KSR.pvx.xavi_is_null(str "rname");
```

* 📖[kamailio.cfg::function::xavi_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_is_null)

## KSR.pvx.xavi_rm ##

```cpp
int KSR.pvx.xavi_rm(str "rname");
```

* 📖[kamailio.cfg::function::xavi_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_rm)

## KSR.pvx.xavi_rm_all ##

```cpp
int KSR.pvx.xavi_rm_all(str "rname");
```

* 📖[kamailio.cfg::function::xavi_rm_all\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_rm_all)

## KSR.pvx.xavi_seti ##

```cpp
int KSR.pvx.xavi_seti(str "rname", int ival);
```

* 📖[kamailio.cfg::function::xavi_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_seti)

## KSR.pvx.xavi_sets ##

```cpp
int KSR.pvx.xavi_sets(str "rname", str "sval");
```

* 📖[kamailio.cfg::function::xavi_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_sets)

## KSR.pvx.xavp_child_get ##

```cpp
xval KSR.pvx.xavp_child_get(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavp_child_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_get)

## KSR.pvx.xavp_child_gete ##

```cpp
xval KSR.pvx.xavp_child_gete(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavp_child_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_gete)

## KSR.pvx.xavp_child_getw ##

```cpp
xval KSR.pvx.xavp_child_getw(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavp_child_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_getw)

## KSR.pvx.xavp_child_is_null ##

```cpp
int KSR.pvx.xavp_child_is_null(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavp_child_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_is_null)

## KSR.pvx.xavp_child_rm ##

```cpp
int KSR.pvx.xavp_child_rm(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavp_child_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_rm)

## KSR.pvx.xavp_child_seti ##

```cpp
int KSR.pvx.xavp_child_seti(str "rname", str "cname", int ival);
```

* 📖[kamailio.cfg::function::xavp_child_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_seti)

## KSR.pvx.xavp_child_sets ##

```cpp
int KSR.pvx.xavp_child_sets(str "rname", str "cname", str "sval");
```

* 📖[kamailio.cfg::function::xavp_child_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_sets)

## KSR.pvx.xavp_copy ##

```cpp
int KSR.pvx.xavp_copy(str "src_name", int src_idx, str "dst_name");
```

* 📖[kamailio.cfg::function::xavp_copy\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_copy)

## KSR.pvx.xavp_copy_dst ##

```cpp
int KSR.pvx.xavp_copy_dst(str "src_name", int src_idx, str "dst_name", int dst_idx);
```

* 📖[kamailio.cfg::function::xavp_copy_dst\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_copy_dst)

## KSR.pvx.xavp_get ##

```cpp
xval KSR.pvx.xavp_get(str "rname");
```

* 📖[kamailio.cfg::function::xavp_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_get)

## KSR.pvx.xavp_get_keys ##

```cpp
xval KSR.pvx.xavp_get_keys(str "rname", int indx);
```

* 📖[kamailio.cfg::function::xavp_get_keys\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_get_keys)

## KSR.pvx.xavp_getd ##

```cpp
xval KSR.pvx.xavp_getd(str "rname");
```

* 📖[kamailio.cfg::function::xavp_getd\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getd)

## KSR.pvx.xavp_getd_p1 ##

```cpp
xval KSR.pvx.xavp_getd_p1(str "rname", int indx);
```

* 📖[kamailio.cfg::function::xavp_getd_p1\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getd_p1)

## KSR.pvx.xavp_gete ##

```cpp
xval KSR.pvx.xavp_gete(str "rname");
```

* 📖[kamailio.cfg::function::xavp_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_gete)

## KSR.pvx.xavp_getw ##

```cpp
xval KSR.pvx.xavp_getw(str "rname");
```

* 📖[kamailio.cfg::function::xavp_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getw)

## KSR.pvx.xavp_is_null ##

```cpp
int KSR.pvx.xavp_is_null(str "rname");
```

* 📖[kamailio.cfg::function::xavp_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_is_null)

## KSR.pvx.xavp_lshift ##

```cpp
int KSR.pvx.xavp_lshift(str "xname", int idx);
```

* 📖[kamailio.cfg::function::xavp_lshift\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_lshift)

## KSR.pvx.xavp_params_explode ##

```cpp
int KSR.pvx.xavp_params_explode(str "sparams", str "sxname");
```

* 📖[kamailio.cfg::function::xavp_params_explode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_params_explode)

## KSR.pvx.xavp_params_implode ##

```cpp
int KSR.pvx.xavp_params_implode(str "sxname", str "svname");
```

* 📖[kamailio.cfg::function::xavp_params_implode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_params_implode)

## KSR.pvx.xavp_params_implode_qval ##

```cpp
int KSR.pvx.xavp_params_implode_qval(str "sxname", str "svname");
```

* 📖[kamailio.cfg::function::xavp_params_implode_qval\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_params_implode_qval)

## KSR.pvx.xavp_push_dst ##

```cpp
int KSR.pvx.xavp_push_dst(str "xname");
```

* 📖[kamailio.cfg::function::xavp_push_dst\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_push_dst)

## KSR.pvx.xavp_rm ##

```cpp
int KSR.pvx.xavp_rm(str "rname");
```

* 📖[kamailio.cfg::function::xavp_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_rm)

## KSR.pvx.xavp_rm_all ##

```cpp
int KSR.pvx.xavp_rm_all(str "rname");
```

* 📖[kamailio.cfg::function::xavp_rm_all\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_rm_all)

## KSR.pvx.xavp_seti ##

```cpp
int KSR.pvx.xavp_seti(str "rname", int ival);
```

* 📖[kamailio.cfg::function::xavp_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_seti)

## KSR.pvx.xavp_sets ##

```cpp
int KSR.pvx.xavp_sets(str "rname", str "sval");
```

* 📖[kamailio.cfg::function::xavp_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_sets)

## KSR.pvx.xavp_slist_explode ##

```cpp
int KSR.pvx.xavp_slist_explode(str "slist", str "sep", str "mode", str "sxname");
```

* 📖[kamailio.cfg::function::xavp_slist_explode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_slist_explode)

## KSR.pvx.xavp_xparams_explode ##

```cpp
int KSR.pvx.xavp_xparams_explode(str "sparams", str "sep", str "sxname");
```

* 📖[kamailio.cfg::function::xavp_xparams_explode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_xparams_explode)

## KSR.pvx.xavu_child_get ##

```cpp
xval KSR.pvx.xavu_child_get(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavu_child_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_get)

## KSR.pvx.xavu_child_gete ##

```cpp
xval KSR.pvx.xavu_child_gete(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavu_child_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_gete)

## KSR.pvx.xavu_child_getw ##

```cpp
xval KSR.pvx.xavu_child_getw(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavu_child_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_getw)

## KSR.pvx.xavu_child_is_null ##

```cpp
int KSR.pvx.xavu_child_is_null(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavu_child_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_is_null)

## KSR.pvx.xavu_child_rm ##

```cpp
int KSR.pvx.xavu_child_rm(str "rname", str "cname");
```

* 📖[kamailio.cfg::function::xavu_child_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_rm)

## KSR.pvx.xavu_child_seti ##

```cpp
int KSR.pvx.xavu_child_seti(str "rname", str "cname", int ival);
```

* 📖[kamailio.cfg::function::xavu_child_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_seti)

## KSR.pvx.xavu_child_sets ##

```cpp
int KSR.pvx.xavu_child_sets(str "rname", str "cname", str "sval");
```

* 📖[kamailio.cfg::function::xavu_child_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_sets)

## KSR.pvx.xavu_get ##

```cpp
xval KSR.pvx.xavu_get(str "rname");
```

* 📖[kamailio.cfg::function::xavu_get\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_get)

## KSR.pvx.xavu_gete ##

```cpp
xval KSR.pvx.xavu_gete(str "rname");
```

* 📖[kamailio.cfg::function::xavu_gete\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_gete)

## KSR.pvx.xavu_getw ##

```cpp
xval KSR.pvx.xavu_getw(str "rname");
```

* 📖[kamailio.cfg::function::xavu_getw\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_getw)

## KSR.pvx.xavu_is_null ##

```cpp
int KSR.pvx.xavu_is_null(str "rname");
```

* 📖[kamailio.cfg::function::xavu_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_is_null)

## KSR.pvx.xavu_params_explode ##

```cpp
int KSR.pvx.xavu_params_explode(str "sparams", str "sxname");
```

* 📖[kamailio.cfg::function::xavu_params_explode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_params_explode)

## KSR.pvx.xavu_params_implode ##

```cpp
int KSR.pvx.xavu_params_implode(str "sxname", str "svname");
```

* 📖[kamailio.cfg::function::xavu_params_implode\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_params_implode)

## KSR.pvx.xavu_rm ##

```cpp
int KSR.pvx.xavu_rm(str "rname");
```

* 📖[kamailio.cfg::function::xavu_rm\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_rm)

## KSR.pvx.xavu_seti ##

```cpp
int KSR.pvx.xavu_seti(str "rname", int ival);
```

* 📖[kamailio.cfg::function::xavu_seti\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_seti)

## KSR.pvx.xavu_sets ##

```cpp
int KSR.pvx.xavu_sets(str "rname", str "sval");
```

* 📖[kamailio.cfg::function::xavu_sets\(\)](https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_sets)
