# textopsx #

* 📖[kamailio.cfg::module::textopsx.html](https://kamailio.org/docs/modules/devel/modules/textopsx.html)

Exported functions:

* [KSR.textopsx.append_hf_value\(\)](#ksrtextopsxappend_hf_value)
* [KSR.textopsx.assign_hf_value\(\)](#ksrtextopsxassign_hf_value)
* [KSR.textopsx.assign_hf_value2\(\)](#ksrtextopsxassign_hf_value2)
* [KSR.textopsx.bl_iterator_append\(\)](#ksrtextopsxbl_iterator_append)
* [KSR.textopsx.bl_iterator_end\(\)](#ksrtextopsxbl_iterator_end)
* [KSR.textopsx.bl_iterator_insert\(\)](#ksrtextopsxbl_iterator_insert)
* [KSR.textopsx.bl_iterator_next\(\)](#ksrtextopsxbl_iterator_next)
* [KSR.textopsx.bl_iterator_rm\(\)](#ksrtextopsxbl_iterator_rm)
* [KSR.textopsx.bl_iterator_start\(\)](#ksrtextopsxbl_iterator_start)
* [KSR.textopsx.bl_iterator_value\(\)](#ksrtextopsxbl_iterator_value)
* [KSR.textopsx.change_reply_status\(\)](#ksrtextopsxchange_reply_status)
* [KSR.textopsx.change_reply_status_code\(\)](#ksrtextopsxchange_reply_status_code)
* [KSR.textopsx.exclude_hf_value\(\)](#ksrtextopsxexclude_hf_value)
* [KSR.textopsx.fnmatch\(\)](#ksrtextopsxfnmatch)
* [KSR.textopsx.fnmatch_ex\(\)](#ksrtextopsxfnmatch_ex)
* [KSR.textopsx.hf_iterator_append\(\)](#ksrtextopsxhf_iterator_append)
* [KSR.textopsx.hf_iterator_end\(\)](#ksrtextopsxhf_iterator_end)
* [KSR.textopsx.hf_iterator_hbody\(\)](#ksrtextopsxhf_iterator_hbody)
* [KSR.textopsx.hf_iterator_hname\(\)](#ksrtextopsxhf_iterator_hname)
* [KSR.textopsx.hf_iterator_insert\(\)](#ksrtextopsxhf_iterator_insert)
* [KSR.textopsx.hf_iterator_next\(\)](#ksrtextopsxhf_iterator_next)
* [KSR.textopsx.hf_iterator_prev\(\)](#ksrtextopsxhf_iterator_prev)
* [KSR.textopsx.hf_iterator_rm\(\)](#ksrtextopsxhf_iterator_rm)
* [KSR.textopsx.hf_iterator_start\(\)](#ksrtextopsxhf_iterator_start)
* [KSR.textopsx.hf_value_exists\(\)](#ksrtextopsxhf_value_exists)
* [KSR.textopsx.include_hf_value\(\)](#ksrtextopsxinclude_hf_value)
* [KSR.textopsx.insert_hf_value\(\)](#ksrtextopsxinsert_hf_value)
* [KSR.textopsx.keep_hf\(\)](#ksrtextopsxkeep_hf)
* [KSR.textopsx.keep_hf_re\(\)](#ksrtextopsxkeep_hf_re)
* [KSR.textopsx.msg_apply_changes\(\)](#ksrtextopsxmsg_apply_changes)
* [KSR.textopsx.msg_set_buffer\(\)](#ksrtextopsxmsg_set_buffer)
* [KSR.textopsx.remove_body\(\)](#ksrtextopsxremove_body)
* [KSR.textopsx.remove_hf_value\(\)](#ksrtextopsxremove_hf_value)
* [KSR.textopsx.remove_hf_value2\(\)](#ksrtextopsxremove_hf_value2)

## KSR.textopsx.append_hf_value ##

```cpp
int KSR.textopsx.append_hf_value(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::append_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.append_hf_value)

## KSR.textopsx.assign_hf_value ##

```cpp
int KSR.textopsx.assign_hf_value(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::assign_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value)

## KSR.textopsx.assign_hf_value2 ##

```cpp
int KSR.textopsx.assign_hf_value2(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::assign_hf_value2\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value2)

## KSR.textopsx.bl_iterator_append ##

```cpp
int KSR.textopsx.bl_iterator_append(str "iname", str "text");
```

* 📖[kamailio.cfg::function::bl_iterator_append\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_append)

## KSR.textopsx.bl_iterator_end ##

```cpp
int KSR.textopsx.bl_iterator_end(str "iname");
```

* 📖[kamailio.cfg::function::bl_iterator_end\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_end)

## KSR.textopsx.bl_iterator_insert ##

```cpp
int KSR.textopsx.bl_iterator_insert(str "iname", str "text");
```

* 📖[kamailio.cfg::function::bl_iterator_insert\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_insert)

## KSR.textopsx.bl_iterator_next ##

```cpp
int KSR.textopsx.bl_iterator_next(str "iname");
```

* 📖[kamailio.cfg::function::bl_iterator_next\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_next)

## KSR.textopsx.bl_iterator_rm ##

```cpp
int KSR.textopsx.bl_iterator_rm(str "iname");
```

* 📖[kamailio.cfg::function::bl_iterator_rm\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_rm)

## KSR.textopsx.bl_iterator_start ##

```cpp
int KSR.textopsx.bl_iterator_start(str "iname");
```

* 📖[kamailio.cfg::function::bl_iterator_start\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_start)

## KSR.textopsx.bl_iterator_value ##

```cpp
xval KSR.textopsx.bl_iterator_value(str "iname");
```

* 📖[kamailio.cfg::function::bl_iterator_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_value)

Return the content of the body line for the current position of the cursor, including the EoL.

It is an alternative to getting the line content via `$blitval(iname)`.

## KSR.textopsx.change_reply_status ##

```cpp
int KSR.textopsx.change_reply_status(int code, str "reason");
```

* 📖[kamailio.cfg::function::change_reply_status\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status)

## KSR.textopsx.change_reply_status_code ##

```cpp
int KSR.textopsx.change_reply_status_code(int code);
```

* 📖[kamailio.cfg::function::change_reply_status_code\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status_code)

## KSR.textopsx.exclude_hf_value ##

```cpp
int KSR.textopsx.exclude_hf_value(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::exclude_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.exclude_hf_value)

## KSR.textopsx.fnmatch ##

```cpp
int KSR.textopsx.fnmatch(str "val", str "match");
```

* 📖[kamailio.cfg::function::fnmatch\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch)

## KSR.textopsx.fnmatch_ex ##

```cpp
int KSR.textopsx.fnmatch_ex(str "val", str "match", str "flags");
```

* 📖[kamailio.cfg::function::fnmatch_ex\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch_ex)

## KSR.textopsx.hf_iterator_append ##

```cpp
int KSR.textopsx.hf_iterator_append(str "iname", str "htext");
```

* 📖[kamailio.cfg::function::hf_iterator_append\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_append)

## KSR.textopsx.hf_iterator_end ##

```cpp
int KSR.textopsx.hf_iterator_end(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_end\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_end)

## KSR.textopsx.hf_iterator_hbody ##

```cpp
xval KSR.textopsx.hf_iterator_hbody(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_hbody\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_hbody)

## KSR.textopsx.hf_iterator_hname ##

```cpp
xval KSR.textopsx.hf_iterator_hname(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_hname\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_hname)

## KSR.textopsx.hf_iterator_insert ##

```cpp
int KSR.textopsx.hf_iterator_insert(str "iname", str "htext");
```

* 📖[kamailio.cfg::function::hf_iterator_insert\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_insert)

## KSR.textopsx.hf_iterator_next ##

```cpp
int KSR.textopsx.hf_iterator_next(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_next\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_next)

## KSR.textopsx.hf_iterator_prev ##

```cpp
int KSR.textopsx.hf_iterator_prev(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_prev\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_prev)

## KSR.textopsx.hf_iterator_rm ##

```cpp
int KSR.textopsx.hf_iterator_rm(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_rm\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_rm)

## KSR.textopsx.hf_iterator_start ##

```cpp
int KSR.textopsx.hf_iterator_start(str "iname");
```

* 📖[kamailio.cfg::function::hf_iterator_start\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_start)

## KSR.textopsx.hf_value_exists ##

```cpp
int KSR.textopsx.hf_value_exists(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::hf_value_exists\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_value_exists)

## KSR.textopsx.include_hf_value ##

```cpp
int KSR.textopsx.include_hf_value(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::include_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.include_hf_value)

## KSR.textopsx.insert_hf_value ##

```cpp
int KSR.textopsx.insert_hf_value(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::insert_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.insert_hf_value)

## KSR.textopsx.keep_hf ##

```cpp
int KSR.textopsx.keep_hf();
```

* 📖[kamailio.cfg::function::keep_hf\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf)

## KSR.textopsx.keep_hf_re ##

```cpp
int KSR.textopsx.keep_hf_re(str "sre");
```

* 📖[kamailio.cfg::function::keep_hf_re\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf_re)

## KSR.textopsx.msg_apply_changes ##

```cpp
int KSR.textopsx.msg_apply_changes();
```

* 📖[kamailio.cfg::function::msg_apply_changes\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_apply_changes)

## KSR.textopsx.msg_set_buffer ##

```cpp
int KSR.textopsx.msg_set_buffer(str "obuf");
```

* 📖[kamailio.cfg::function::msg_set_buffer\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_set_buffer)

## KSR.textopsx.remove_body ##

```cpp
int KSR.textopsx.remove_body();
```

* 📖[kamailio.cfg::function::remove_body\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_body)

## KSR.textopsx.remove_hf_value ##

```cpp
int KSR.textopsx.remove_hf_value(str "hexp");
```

* 📖[kamailio.cfg::function::remove_hf_value\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value)

## KSR.textopsx.remove_hf_value2 ##

```cpp
int KSR.textopsx.remove_hf_value2(str "hexp", str "val");
```

* 📖[kamailio.cfg::function::remove_hf_value2\(\)](https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value2)
