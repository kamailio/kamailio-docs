# sdpops #

* 📖[kamailio.cfg::module::sdpops.html](https://kamailio.org/docs/modules/devel/modules/sdpops.html)

Exported functions:

* [KSR.sdpops.keep_codecs_by_id\(\)](#ksrsdpopskeep_codecs_by_id)
* [KSR.sdpops.keep_codecs_by_name\(\)](#ksrsdpopskeep_codecs_by_name)
* [KSR.sdpops.remove_codecs_by_id\(\)](#ksrsdpopsremove_codecs_by_id)
* [KSR.sdpops.remove_codecs_by_name\(\)](#ksrsdpopsremove_codecs_by_name)
* [KSR.sdpops.remove_line_by_prefix\(\)](#ksrsdpopsremove_line_by_prefix)
* [KSR.sdpops.remove_media\(\)](#ksrsdpopsremove_media)
* [KSR.sdpops.sdp_content\(\)](#ksrsdpopssdp_content)
* [KSR.sdpops.sdp_content_flags\(\)](#ksrsdpopssdp_content_flags)
* [KSR.sdpops.sdp_get\(\)](#ksrsdpopssdp_get)
* [KSR.sdpops.sdp_get_address_family\(\)](#ksrsdpopssdp_get_address_family)
* [KSR.sdpops.sdp_get_line_startswith\(\)](#ksrsdpopssdp_get_line_startswith)
* [KSR.sdpops.sdp_iterator_append\(\)](#ksrsdpopssdp_iterator_append)
* [KSR.sdpops.sdp_iterator_end\(\)](#ksrsdpopssdp_iterator_end)
* [KSR.sdpops.sdp_iterator_insert\(\)](#ksrsdpopssdp_iterator_insert)
* [KSR.sdpops.sdp_iterator_next\(\)](#ksrsdpopssdp_iterator_next)
* [KSR.sdpops.sdp_iterator_rm\(\)](#ksrsdpopssdp_iterator_rm)
* [KSR.sdpops.sdp_iterator_start\(\)](#ksrsdpopssdp_iterator_start)
* [KSR.sdpops.sdp_iterator_value\(\)](#ksrsdpopssdp_iterator_value)
* [KSR.sdpops.sdp_print\(\)](#ksrsdpopssdp_print)
* [KSR.sdpops.sdp_transport\(\)](#ksrsdpopssdp_transport)
* [KSR.sdpops.sdp_with_active_media\(\)](#ksrsdpopssdp_with_active_media)
* [KSR.sdpops.sdp_with_codecs_by_id\(\)](#ksrsdpopssdp_with_codecs_by_id)
* [KSR.sdpops.sdp_with_codecs_by_name\(\)](#ksrsdpopssdp_with_codecs_by_name)
* [KSR.sdpops.sdp_with_ice\(\)](#ksrsdpopssdp_with_ice)
* [KSR.sdpops.sdp_with_media\(\)](#ksrsdpopssdp_with_media)
* [KSR.sdpops.sdp_with_transport\(\)](#ksrsdpopssdp_with_transport)
* [KSR.sdpops.sdp_with_transport_like\(\)](#ksrsdpopssdp_with_transport_like)

## KSR.sdpops.keep_codecs_by_id ##

```cpp
int KSR.sdpops.keep_codecs_by_id(str "codecs", str "media");
```

* 📖[kamailio.cfg::function::keep_codecs_by_id\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_id)

## KSR.sdpops.keep_codecs_by_name ##

```cpp
int KSR.sdpops.keep_codecs_by_name(str "codecs", str "media");
```

* 📖[kamailio.cfg::function::keep_codecs_by_name\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_name)

## KSR.sdpops.remove_codecs_by_id ##

```cpp
int KSR.sdpops.remove_codecs_by_id(str "codecs", str "media");
```

* 📖[kamailio.cfg::function::remove_codecs_by_id\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_id)

## KSR.sdpops.remove_codecs_by_name ##

```cpp
int KSR.sdpops.remove_codecs_by_name(str "codecs", str "media");
```

* 📖[kamailio.cfg::function::remove_codecs_by_name\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_name)

## KSR.sdpops.remove_line_by_prefix ##

```cpp
int KSR.sdpops.remove_line_by_prefix(str "prefix", str "media");
```

* 📖[kamailio.cfg::function::remove_line_by_prefix\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_line_by_prefix)

## KSR.sdpops.remove_media ##

```cpp
int KSR.sdpops.remove_media(str "media");
```

* 📖[kamailio.cfg::function::remove_media\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_media)

## KSR.sdpops.sdp_content ##

```cpp
int KSR.sdpops.sdp_content();
```

* 📖[kamailio.cfg::function::sdp_content\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content)

## KSR.sdpops.sdp_content_flags ##

```cpp
int KSR.sdpops.sdp_content_flags(int flags);
```

* 📖[kamailio.cfg::function::sdp_content_flags\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content_flags)

## KSR.sdpops.sdp_get ##

```cpp
int KSR.sdpops.sdp_get(str "avp");
```

* 📖[kamailio.cfg::function::sdp_get\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get)

## KSR.sdpops.sdp_get_address_family ##

```cpp
int KSR.sdpops.sdp_get_address_family();
```

* 📖[kamailio.cfg::function::sdp_get_address_family\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get_address_family)

## KSR.sdpops.sdp_get_line_startswith ##

```cpp
int KSR.sdpops.sdp_get_line_startswith(str "aname", str "sline");
```

* 📖[kamailio.cfg::function::sdp_get_line_startswith\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get_line_startswith)

## KSR.sdpops.sdp_iterator_append ##

```cpp
int KSR.sdpops.sdp_iterator_append(str "iname", str "text");
```

* 📖[kamailio.cfg::function::sdp_iterator_append\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_append)

## KSR.sdpops.sdp_iterator_end ##

```cpp
int KSR.sdpops.sdp_iterator_end(str "iname");
```

* 📖[kamailio.cfg::function::sdp_iterator_end\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_end)

## KSR.sdpops.sdp_iterator_insert ##

```cpp
int KSR.sdpops.sdp_iterator_insert(str "iname", str "text");
```

* 📖[kamailio.cfg::function::sdp_iterator_insert\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_insert)

## KSR.sdpops.sdp_iterator_next ##

```cpp
int KSR.sdpops.sdp_iterator_next(str "iname");
```

* 📖[kamailio.cfg::function::sdp_iterator_next\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_next)

## KSR.sdpops.sdp_iterator_rm ##

```cpp
int KSR.sdpops.sdp_iterator_rm(str "iname");
```

* 📖[kamailio.cfg::function::sdp_iterator_rm\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_rm)

## KSR.sdpops.sdp_iterator_start ##

```cpp
int KSR.sdpops.sdp_iterator_start(str "iname");
```

* 📖[kamailio.cfg::function::sdp_iterator_start\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_start)

## KSR.sdpops.sdp_iterator_value ##

```cpp
xval KSR.sdpops.sdp_iterator_value(str "iname");
```

* 📖[kamailio.cfg::function::sdp_iterator_value\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_iterator_value)

## KSR.sdpops.sdp_print ##

```cpp
int KSR.sdpops.sdp_print(int llevel);
```

* 📖[kamailio.cfg::function::sdp_print\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_print)

## KSR.sdpops.sdp_transport ##

```cpp
int KSR.sdpops.sdp_transport(str "avp");
```

* 📖[kamailio.cfg::function::sdp_transport\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_transport)

## KSR.sdpops.sdp_with_active_media ##

```cpp
int KSR.sdpops.sdp_with_active_media(str "media");
```

* 📖[kamailio.cfg::function::sdp_with_active_media\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_active_media)

## KSR.sdpops.sdp_with_codecs_by_id ##

```cpp
int KSR.sdpops.sdp_with_codecs_by_id(str "codecs");
```

* 📖[kamailio.cfg::function::sdp_with_codecs_by_id\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_id)

## KSR.sdpops.sdp_with_codecs_by_name ##

```cpp
int KSR.sdpops.sdp_with_codecs_by_name(str "codecs");
```

* 📖[kamailio.cfg::function::sdp_with_codecs_by_name\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_name)

## KSR.sdpops.sdp_with_ice ##

```cpp
int KSR.sdpops.sdp_with_ice();
```

* 📖[kamailio.cfg::function::sdp_with_ice\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_ice)

## KSR.sdpops.sdp_with_media ##

```cpp
int KSR.sdpops.sdp_with_media(str "media");
```

* 📖[kamailio.cfg::function::sdp_with_media\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_media)

## KSR.sdpops.sdp_with_transport ##

```cpp
int KSR.sdpops.sdp_with_transport(str "transport");
```

* 📖[kamailio.cfg::function::sdp_with_transport\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport)

## KSR.sdpops.sdp_with_transport_like ##

```cpp
int KSR.sdpops.sdp_with_transport_like(str "transport");
```

* 📖[kamailio.cfg::function::sdp_with_transport_like\(\)](https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport_like)
