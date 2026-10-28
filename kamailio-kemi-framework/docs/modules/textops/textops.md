# textops #

* 📖[kamailio.cfg::module::textops.html](https://kamailio.org/docs/modules/devel/modules/textops.html)

Exported functions:

* [KSR.textops.append_body_part\(\)](#ksrtextopsappend_body_part)
* [KSR.textops.append_body_part_cd\(\)](#ksrtextopsappend_body_part_cd)
* [KSR.textops.append_body_part_hex\(\)](#ksrtextopsappend_body_part_hex)
* [KSR.textops.append_body_part_hex_cd\(\)](#ksrtextopsappend_body_part_hex_cd)
* [KSR.textops.cmp_istr\(\)](#ksrtextopscmp_istr)
* [KSR.textops.cmp_str\(\)](#ksrtextopscmp_str)
* [KSR.textops.ends_with\(\)](#ksrtextopsends_with)
* [KSR.textops.filter_body\(\)](#ksrtextopsfilter_body)
* [KSR.textops.get_body_part\(\)](#ksrtextopsget_body_part)
* [KSR.textops.get_body_part_raw\(\)](#ksrtextopsget_body_part_raw)
* [KSR.textops.has_body\(\)](#ksrtextopshas_body)
* [KSR.textops.has_body_type\(\)](#ksrtextopshas_body_type)
* [KSR.textops.in_list\(\)](#ksrtextopsin_list)
* [KSR.textops.in_list_prefix\(\)](#ksrtextopsin_list_prefix)
* [KSR.textops.is_audio_on_hold\(\)](#ksrtextopsis_audio_on_hold)
* [KSR.textops.is_present_hf\(\)](#ksrtextopsis_present_hf)
* [KSR.textops.is_present_hf_re\(\)](#ksrtextopsis_present_hf_re)
* [KSR.textops.is_privacy\(\)](#ksrtextopsis_privacy)
* [KSR.textops.regex_substring\(\)](#ksrtextopsregex_substring)
* [KSR.textops.remove_body_part\(\)](#ksrtextopsremove_body_part)
* [KSR.textops.remove_hf\(\)](#ksrtextopsremove_hf)
* [KSR.textops.remove_hf_exp\(\)](#ksrtextopsremove_hf_exp)
* [KSR.textops.remove_hf_idx\(\)](#ksrtextopsremove_hf_idx)
* [KSR.textops.remove_hf_match\(\)](#ksrtextopsremove_hf_match)
* [KSR.textops.remove_hf_re\(\)](#ksrtextopsremove_hf_re)
* [KSR.textops.replace\(\)](#ksrtextopsreplace)
* [KSR.textops.replace_all\(\)](#ksrtextopsreplace_all)
* [KSR.textops.replace_body\(\)](#ksrtextopsreplace_body)
* [KSR.textops.replace_body_all\(\)](#ksrtextopsreplace_body_all)
* [KSR.textops.replace_body_atonce\(\)](#ksrtextopsreplace_body_atonce)
* [KSR.textops.replace_body_str\(\)](#ksrtextopsreplace_body_str)
* [KSR.textops.replace_hdrs\(\)](#ksrtextopsreplace_hdrs)
* [KSR.textops.replace_hdrs_str\(\)](#ksrtextopsreplace_hdrs_str)
* [KSR.textops.replace_str\(\)](#ksrtextopsreplace_str)
* [KSR.textops.search\(\)](#ksrtextopssearch)
* [KSR.textops.search_append\(\)](#ksrtextopssearch_append)
* [KSR.textops.search_append_body\(\)](#ksrtextopssearch_append_body)
* [KSR.textops.search_body\(\)](#ksrtextopssearch_body)
* [KSR.textops.search_hf\(\)](#ksrtextopssearch_hf)
* [KSR.textops.search_str\(\)](#ksrtextopssearch_str)
* [KSR.textops.set_body\(\)](#ksrtextopsset_body)
* [KSR.textops.set_body_hex\(\)](#ksrtextopsset_body_hex)
* [KSR.textops.set_body_multipart\(\)](#ksrtextopsset_body_multipart)
* [KSR.textops.set_body_multipart_boundary\(\)](#ksrtextopsset_body_multipart_boundary)
* [KSR.textops.set_body_multipart_content\(\)](#ksrtextopsset_body_multipart_content)
* [KSR.textops.set_body_multipart_mode\(\)](#ksrtextopsset_body_multipart_mode)
* [KSR.textops.set_reply_body\(\)](#ksrtextopsset_reply_body)
* [KSR.textops.set_reply_body_hex\(\)](#ksrtextopsset_reply_body_hex)
* [KSR.textops.starts_with\(\)](#ksrtextopsstarts_with)
* [KSR.textops.str_all_in\(\)](#ksrtextopsstr_all_in)
* [KSR.textops.str_any_in\(\)](#ksrtextopsstr_any_in)
* [KSR.textops.str_find\(\)](#ksrtextopsstr_find)
* [KSR.textops.str_ifind\(\)](#ksrtextopsstr_ifind)
* [KSR.textops.subst\(\)](#ksrtextopssubst)
* [KSR.textops.subst_body\(\)](#ksrtextopssubst_body)
* [KSR.textops.subst_hf\(\)](#ksrtextopssubst_hf)
* [KSR.textops.subst_uri\(\)](#ksrtextopssubst_uri)
* [KSR.textops.subst_user\(\)](#ksrtextopssubst_user)
* [KSR.textops.subst_v\(\)](#ksrtextopssubst_v)

## KSR.textops.append_body_part ##

```cpp
int KSR.textops.append_body_part(str "txt", str "ct");
```

* 📖[kamailio.cfg::function::append_body_part\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part)

## KSR.textops.append_body_part_cd ##

```cpp
int KSR.textops.append_body_part_cd(str "txt", str "ct", str "cd");
```

* 📖[kamailio.cfg::function::append_body_part_cd\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_cd)

## KSR.textops.append_body_part_hex ##

```cpp
int KSR.textops.append_body_part_hex(str "txt", str "ct");
```

* 📖[kamailio.cfg::function::append_body_part_hex\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex)

## KSR.textops.append_body_part_hex_cd ##

```cpp
int KSR.textops.append_body_part_hex_cd(str "htxt", str "ct", str "cd");
```

* 📖[kamailio.cfg::function::append_body_part_hex_cd\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex_cd)

## KSR.textops.cmp_istr ##

```cpp
int KSR.textops.cmp_istr(str "s1", str "s2");
```

* 📖[kamailio.cfg::function::cmp_istr\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_istr)

## KSR.textops.cmp_str ##

```cpp
int KSR.textops.cmp_str(str "s1", str "s2");
```

* 📖[kamailio.cfg::function::cmp_str\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_str)

## KSR.textops.ends_with ##

```cpp
int KSR.textops.ends_with(str "vstr", str "vsuffix");
```

* 📖[kamailio.cfg::function::ends_with\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.ends_with)

## KSR.textops.filter_body ##

```cpp
int KSR.textops.filter_body(str "content_type");
```

* 📖[kamailio.cfg::function::filter_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.filter_body)

## KSR.textops.get_body_part ##

```cpp
int KSR.textops.get_body_part(str "ctype", str "pvname");
```

* 📖[kamailio.cfg::function::get_body_part\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part)

## KSR.textops.get_body_part_raw ##

```cpp
int KSR.textops.get_body_part_raw(str "ctype", str "pvname");
```

* 📖[kamailio.cfg::function::get_body_part_raw\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part_raw)

## KSR.textops.has_body ##

```cpp
int KSR.textops.has_body();
```

* 📖[kamailio.cfg::function::has_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body)

## KSR.textops.has_body_type ##

```cpp
int KSR.textops.has_body_type(str "ctype");
```

* 📖[kamailio.cfg::function::has_body_type\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body_type)

## KSR.textops.in_list ##

```cpp
int KSR.textops.in_list(str "subject", str "list", str "vsep");
```

* 📖[kamailio.cfg::function::in_list\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list)

## KSR.textops.in_list_prefix ##

```cpp
int KSR.textops.in_list_prefix(str "subject", str "list", str "vsep");
```

* 📖[kamailio.cfg::function::in_list_prefix\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list_prefix)

## KSR.textops.is_audio_on_hold ##

```cpp
int KSR.textops.is_audio_on_hold();
```

* 📖[kamailio.cfg::function::is_audio_on_hold\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_audio_on_hold)

## KSR.textops.is_present_hf ##

```cpp
int KSR.textops.is_present_hf(str "hname");
```

* 📖[kamailio.cfg::function::is_present_hf\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf)

## KSR.textops.is_present_hf_re ##

```cpp
int KSR.textops.is_present_hf_re(str "ematch");
```

* 📖[kamailio.cfg::function::is_present_hf_re\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf_re)

## KSR.textops.is_privacy ##

```cpp
int KSR.textops.is_privacy(str "privacy");
```

* 📖[kamailio.cfg::function::is_privacy\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_privacy)

## KSR.textops.regex_substring ##

```cpp
int KSR.textops.regex_substring(str "input", str "regex", int mindex, int nmatch, str "dst");
```

* 📖[kamailio.cfg::function::regex_substring\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.regex_substring)

## KSR.textops.remove_body_part ##

```cpp
int KSR.textops.remove_body_part(str "content_type");
```

* 📖[kamailio.cfg::function::remove_body_part\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_body_part)

## KSR.textops.remove_hf ##

```cpp
int KSR.textops.remove_hf(str "hname");
```

* 📖[kamailio.cfg::function::remove_hf\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf)

## KSR.textops.remove_hf_exp ##

```cpp
int KSR.textops.remove_hf_exp(str "ematch", str "eskip");
```

* 📖[kamailio.cfg::function::remove_hf_exp\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_exp)

## KSR.textops.remove_hf_idx ##

```cpp
int KSR.textops.remove_hf_idx(str "hname", int idx);
```

* 📖[kamailio.cfg::function::remove_hf_idx\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_idx)

## KSR.textops.remove_hf_match ##

```cpp
int KSR.textops.remove_hf_match(str "hname", str "op", str "expr");
```

* 📖[kamailio.cfg::function::remove_hf_match\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_match)

## KSR.textops.remove_hf_re ##

```cpp
int KSR.textops.remove_hf_re(str "ematch");
```

* 📖[kamailio.cfg::function::remove_hf_re\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_re)

## KSR.textops.replace ##

```cpp
int KSR.textops.replace(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace)

## KSR.textops.replace_all ##

```cpp
int KSR.textops.replace_all(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace_all\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_all)

## KSR.textops.replace_body ##

```cpp
int KSR.textops.replace_body(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body)

## KSR.textops.replace_body_all ##

```cpp
int KSR.textops.replace_body_all(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace_body_all\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_all)

## KSR.textops.replace_body_atonce ##

```cpp
int KSR.textops.replace_body_atonce(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace_body_atonce\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_atonce)

## KSR.textops.replace_body_str ##

```cpp
int KSR.textops.replace_body_str(str "mkey", str "rval", str "rmode");
```

* 📖[kamailio.cfg::function::replace_body_str\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_str)

## KSR.textops.replace_hdrs ##

```cpp
int KSR.textops.replace_hdrs(str "sre", str "sval");
```

* 📖[kamailio.cfg::function::replace_hdrs\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs)

## KSR.textops.replace_hdrs_str ##

```cpp
int KSR.textops.replace_hdrs_str(str "mkey", str "rval", str "rmode");
```

* 📖[kamailio.cfg::function::replace_hdrs_str\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs_str)

## KSR.textops.replace_str ##

```cpp
int KSR.textops.replace_str(str "mkey", str "rval", str "rmode");
```

* 📖[kamailio.cfg::function::replace_str\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_str)

## KSR.textops.search ##

```cpp
int KSR.textops.search(str "sre");
```

* 📖[kamailio.cfg::function::search\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search)

## KSR.textops.search_append ##

```cpp
int KSR.textops.search_append(str "ematch", str "val");
```

* 📖[kamailio.cfg::function::search_append\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append)

## KSR.textops.search_append_body ##

```cpp
int KSR.textops.search_append_body(str "ematch", str "val");
```

* 📖[kamailio.cfg::function::search_append_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append_body)

## KSR.textops.search_body ##

```cpp
int KSR.textops.search_body(str "sre");
```

* 📖[kamailio.cfg::function::search_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_body)

## KSR.textops.search_hf ##

```cpp
int KSR.textops.search_hf(str "hname", str "sre", str "flags");
```

* 📖[kamailio.cfg::function::search_hf\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_hf)

## KSR.textops.search_str ##

```cpp
int KSR.textops.search_str(str "stext", str "sre");
```

* 📖[kamailio.cfg::function::search_str\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_str)

## KSR.textops.set_body ##

```cpp
int KSR.textops.set_body(str "nb", str "nc");
```

* 📖[kamailio.cfg::function::set_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body)

## KSR.textops.set_body_hex ##

```cpp
int KSR.textops.set_body_hex(str "htxt", str "ct");
```

* 📖[kamailio.cfg::function::set_body_hex\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_hex)

## KSR.textops.set_body_multipart ##

```cpp
int KSR.textops.set_body_multipart(str "nbody", str "ctype", str "boundary");
```

* 📖[kamailio.cfg::function::set_body_multipart\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart)

## KSR.textops.set_body_multipart_boundary ##

```cpp
int KSR.textops.set_body_multipart_boundary(str "boundary");
```

* 📖[kamailio.cfg::function::set_body_multipart_boundary\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_boundary)

## KSR.textops.set_body_multipart_content ##

```cpp
int KSR.textops.set_body_multipart_content(str "nbody", str "ctype");
```

* 📖[kamailio.cfg::function::set_body_multipart_content\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_content)

## KSR.textops.set_body_multipart_mode ##

```cpp
int KSR.textops.set_body_multipart_mode();
```

* 📖[kamailio.cfg::function::set_body_multipart_mode\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_mode)

## KSR.textops.set_reply_body ##

```cpp
int KSR.textops.set_reply_body(str "nb", str "nc");
```

* 📖[kamailio.cfg::function::set_reply_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_reply_body)

## KSR.textops.set_reply_body_hex ##

```cpp
int KSR.textops.set_reply_body_hex(str "htxt", str "ct");
```

* 📖[kamailio.cfg::function::set_reply_body_hex\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_reply_body_hex)

## KSR.textops.starts_with ##

```cpp
int KSR.textops.starts_with(str "s1", str "s2");
```

* 📖[kamailio.cfg::function::starts_with\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.starts_with)

## KSR.textops.str_all_in ##

```cpp
int KSR.textops.str_all_in(str "txt", str "clist");
```

* 📖[kamailio.cfg::function::str_all_in\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_all_in)

## KSR.textops.str_any_in ##

```cpp
int KSR.textops.str_any_in(str "txt", str "clist");
```

* 📖[kamailio.cfg::function::str_any_in\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_any_in)

## KSR.textops.str_find ##

```cpp
int KSR.textops.str_find(str "txt", str "needle");
```

* 📖[kamailio.cfg::function::str_find\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_find)

## KSR.textops.str_ifind ##

```cpp
int KSR.textops.str_ifind(str "txt", str "needle");
```

* 📖[kamailio.cfg::function::str_ifind\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_ifind)

## KSR.textops.subst ##

```cpp
int KSR.textops.subst(str "subst");
```

* 📖[kamailio.cfg::function::subst\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst)

## KSR.textops.subst_body ##

```cpp
int KSR.textops.subst_body(str "subst");
```

* 📖[kamailio.cfg::function::subst_body\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_body)

## KSR.textops.subst_hf ##

```cpp
int KSR.textops.subst_hf(str "hname", str "subst", str "flags");
```

* 📖[kamailio.cfg::function::subst_hf\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_hf)

## KSR.textops.subst_uri ##

```cpp
int KSR.textops.subst_uri(str "subst");
```

* 📖[kamailio.cfg::function::subst_uri\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_uri)

## KSR.textops.subst_user ##

```cpp
int KSR.textops.subst_user(str "subst");
```

* 📖[kamailio.cfg::function::subst_user\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_user)

## KSR.textops.subst_v ##

```cpp
int KSR.textops.subst_v(str "itext", str "subex", str "opv");
```

* 📖[kamailio.cfg::function::subst_v\(\)](https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_v)
