# htable #

* 📖[kamailio.cfg::module::htable.html](https://kamailio.org/docs/modules/devel/modules/htable.html)

Functions exported by `htable` module.

Exported functions:

* [KSR.htable.sht_cn\(\)](#ksrhtablesht_cn)
* [KSR.htable.sht_dec\(\)](#ksrhtablesht_dec)
* [KSR.htable.sht_get\(\)](#ksrhtablesht_get)
* [KSR.htable.sht_gete\(\)](#ksrhtablesht_gete)
* [KSR.htable.sht_getw\(\)](#ksrhtablesht_getw)
* [KSR.htable.sht_inc\(\)](#ksrhtablesht_inc)
* [KSR.htable.sht_is_null\(\)](#ksrhtablesht_is_null)
* [KSR.htable.sht_iterator_end\(\)](#ksrhtablesht_iterator_end)
* [KSR.htable.sht_iterator_next\(\)](#ksrhtablesht_iterator_next)
* [KSR.htable.sht_iterator_rm\(\)](#ksrhtablesht_iterator_rm)
* [KSR.htable.sht_iterator_setex\(\)](#ksrhtablesht_iterator_setex)
* [KSR.htable.sht_iterator_seti\(\)](#ksrhtablesht_iterator_seti)
* [KSR.htable.sht_iterator_sets\(\)](#ksrhtablesht_iterator_sets)
* [KSR.htable.sht_iterator_start\(\)](#ksrhtablesht_iterator_start)
* [KSR.htable.sht_lock\(\)](#ksrhtablesht_lock)
* [KSR.htable.sht_match_name\(\)](#ksrhtablesht_match_name)
* [KSR.htable.sht_match_str_value\(\)](#ksrhtablesht_match_str_value)
* [KSR.htable.sht_reset\(\)](#ksrhtablesht_reset)
* [KSR.htable.sht_rm\(\)](#ksrhtablesht_rm)
* [KSR.htable.sht_rm_name\(\)](#ksrhtablesht_rm_name)
* [KSR.htable.sht_rm_name_re\(\)](#ksrhtablesht_rm_name_re)
* [KSR.htable.sht_rm_value\(\)](#ksrhtablesht_rm_value)
* [KSR.htable.sht_rm_value_re\(\)](#ksrhtablesht_rm_value_re)
* [KSR.htable.sht_setex\(\)](#ksrhtablesht_setex)
* [KSR.htable.sht_seti\(\)](#ksrhtablesht_seti)
* [KSR.htable.sht_sets\(\)](#ksrhtablesht_sets)
* [KSR.htable.sht_setxi\(\)](#ksrhtablesht_setxi)
* [KSR.htable.sht_setxs\(\)](#ksrhtablesht_setxs)
* [KSR.htable.sht_unlock\(\)](#ksrhtablesht_unlock)

## KSR.htable.sht_cn ##

```cpp
int KSR.htable.sht_cn(str "table", str "op", str "pattern");
```

* 📖[kamailio.cfg::function::sht_cn\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_cn)

Functions exported by `htable` module.

## KSR.htable.sht_dec ##

```cpp
int KSR.htable.sht_dec(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_dec\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_dec)

Functions exported by `htable` module.

## KSR.htable.sht_get ##

```cpp
xval KSR.htable.sht_get(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_get\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_get)

Functions exported by `htable` module.

## KSR.htable.sht_gete ##

```cpp
xval KSR.htable.sht_gete(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_gete\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_gete)

Functions exported by `htable` module.

## KSR.htable.sht_getw ##

```cpp
xval KSR.htable.sht_getw(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_getw\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_getw)

Functions exported by `htable` module.

## KSR.htable.sht_inc ##

```cpp
int KSR.htable.sht_inc(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_inc\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_inc)

Functions exported by `htable` module.

## KSR.htable.sht_is_null ##

```cpp
int KSR.htable.sht_is_null(str "htname", str "itname");
```

* 📖[kamailio.cfg::function::sht_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_is_null)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_end ##

```cpp
int KSR.htable.sht_iterator_end(str "iname");
```

* 📖[kamailio.cfg::function::sht_iterator_end\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_end)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_next ##

```cpp
int KSR.htable.sht_iterator_next(str "iname");
```

* 📖[kamailio.cfg::function::sht_iterator_next\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_next)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_rm ##

```cpp
int KSR.htable.sht_iterator_rm(str "iname");
```

* 📖[kamailio.cfg::function::sht_iterator_rm\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_rm)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_setex ##

```cpp
int KSR.htable.sht_iterator_setex(str "iname", int exval);
```

* 📖[kamailio.cfg::function::sht_iterator_setex\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_setex)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_seti ##

```cpp
int KSR.htable.sht_iterator_seti(str "iname", int ival);
```

* 📖[kamailio.cfg::function::sht_iterator_seti\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_seti)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_sets ##

```cpp
int KSR.htable.sht_iterator_sets(str "iname", str "sval");
```

* 📖[kamailio.cfg::function::sht_iterator_sets\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_sets)

Functions exported by `htable` module.

## KSR.htable.sht_iterator_start ##

```cpp
int KSR.htable.sht_iterator_start(str "iname", str "hname");
```

* 📖[kamailio.cfg::function::sht_iterator_start\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_start)

Functions exported by `htable` module.

## KSR.htable.sht_lock ##

```cpp
int KSR.htable.sht_lock(str "htname", str "skey");
```

* 📖[kamailio.cfg::function::sht_lock\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_lock)

Functions exported by `htable` module.

## KSR.htable.sht_match_name ##

```cpp
int KSR.htable.sht_match_name(str "sname", str "sop", str "sval");
```

* 📖[kamailio.cfg::function::sht_match_name\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_name)

Functions exported by `htable` module.

## KSR.htable.sht_match_str_value ##

```cpp
int KSR.htable.sht_match_str_value(str "sname", str "sop", str "sval");
```

* 📖[kamailio.cfg::function::sht_match_str_value\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_str_value)

Functions exported by `htable` module.

## KSR.htable.sht_reset ##

```cpp
int KSR.htable.sht_reset(str "hname");
```

* 📖[kamailio.cfg::function::sht_reset\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_reset)

Functions exported by `htable` module.

## KSR.htable.sht_rm ##

```cpp
int KSR.htable.sht_rm(str "hname", str "iname");
```

* 📖[kamailio.cfg::function::sht_rm\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm)

Functions exported by `htable` module.

## KSR.htable.sht_rm_name ##

```cpp
int KSR.htable.sht_rm_name(str "sname", str "sop", str "sval");
```

* 📖[kamailio.cfg::function::sht_rm_name\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name)

Functions exported by `htable` module.

## KSR.htable.sht_rm_name_re ##

```cpp
int KSR.htable.sht_rm_name_re(str "htname", str "rexp");
```

* 📖[kamailio.cfg::function::sht_rm_name_re\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name_re)

Functions exported by `htable` module.

## KSR.htable.sht_rm_value ##

```cpp
int KSR.htable.sht_rm_value(str "sname", str "sop", str "sval");
```

* 📖[kamailio.cfg::function::sht_rm_value\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value)

Functions exported by `htable` module.

## KSR.htable.sht_rm_value_re ##

```cpp
int KSR.htable.sht_rm_value_re(str "htname", str "rexp");
```

* 📖[kamailio.cfg::function::sht_rm_value_re\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value_re)

Functions exported by `htable` module.

## KSR.htable.sht_setex ##

```cpp
int KSR.htable.sht_setex(str "htname", str "itname", int itval);
```

* 📖[kamailio.cfg::function::sht_setex\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setex)

Functions exported by `htable` module.

## KSR.htable.sht_seti ##

```cpp
int KSR.htable.sht_seti(str "htname", str "itname", int itval);
```

* 📖[kamailio.cfg::function::sht_seti\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_seti)

Functions exported by `htable` module.

## KSR.htable.sht_sets ##

```cpp
int KSR.htable.sht_sets(str "htname", str "itname", str "itval");
```

* 📖[kamailio.cfg::function::sht_sets\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_sets)

Functions exported by `htable` module.

## KSR.htable.sht_setxi ##

```cpp
int KSR.htable.sht_setxi(str "htname", str "itname", int itval, int exval);
```

* 📖[kamailio.cfg::function::sht_setxi\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxi)

Functions exported by `htable` module.

## KSR.htable.sht_setxs ##

```cpp
int KSR.htable.sht_setxs(str "htname", str "itname", str "itval", int exval);
```

* 📖[kamailio.cfg::function::sht_setxs\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxs)

Functions exported by `htable` module.

## KSR.htable.sht_unlock ##

```cpp
int KSR.htable.sht_unlock(str "htname", str "skey");
```

* 📖[kamailio.cfg::function::sht_unlock\(\)](https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_unlock)

Functions exported by `htable` module.
