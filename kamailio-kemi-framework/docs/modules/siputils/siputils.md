# siputils #

* 📖[kamailio.cfg::module::siputils.html](https://kamailio.org/docs/modules/devel/modules/siputils.html)

Exported functions:

* [KSR.siputils.add_uri_param\(\)](#ksrsiputilsadd_uri_param)
* [KSR.siputils.cmp_aor\(\)](#ksrsiputilscmp_aor)
* [KSR.siputils.cmp_hdr_name\(\)](#ksrsiputilscmp_hdr_name)
* [KSR.siputils.cmp_uri\(\)](#ksrsiputilscmp_uri)
* [KSR.siputils.contact_param_check\(\)](#ksrsiputilscontact_param_check)
* [KSR.siputils.contact_param_decode\(\)](#ksrsiputilscontact_param_decode)
* [KSR.siputils.contact_param_decode_ruri\(\)](#ksrsiputilscontact_param_decode_ruri)
* [KSR.siputils.contact_param_encode\(\)](#ksrsiputilscontact_param_encode)
* [KSR.siputils.contact_param_encode_alias\(\)](#ksrsiputilscontact_param_encode_alias)
* [KSR.siputils.contact_param_rm\(\)](#ksrsiputilscontact_param_rm)
* [KSR.siputils.decode_contact\(\)](#ksrsiputilsdecode_contact)
* [KSR.siputils.decode_contact_header\(\)](#ksrsiputilsdecode_contact_header)
* [KSR.siputils.encode_contact\(\)](#ksrsiputilsencode_contact)
* [KSR.siputils.has_totag\(\)](#ksrsiputilshas_totag)
* [KSR.siputils.hdr_date_check\(\)](#ksrsiputilshdr_date_check)
* [KSR.siputils.is_alphanum\(\)](#ksrsiputilsis_alphanum)
* [KSR.siputils.is_alphanumex\(\)](#ksrsiputilsis_alphanumex)
* [KSR.siputils.is_first_hop\(\)](#ksrsiputilsis_first_hop)
* [KSR.siputils.is_first_hop_mode\(\)](#ksrsiputilsis_first_hop_mode)
* [KSR.siputils.is_gruu\(\)](#ksrsiputilsis_gruu)
* [KSR.siputils.is_http\(\)](#ksrsiputilsis_http)
* [KSR.siputils.is_numeric\(\)](#ksrsiputilsis_numeric)
* [KSR.siputils.is_reply\(\)](#ksrsiputilsis_reply)
* [KSR.siputils.is_request\(\)](#ksrsiputilsis_request)
* [KSR.siputils.is_sip\(\)](#ksrsiputilsis_sip)
* [KSR.siputils.is_tel_number\(\)](#ksrsiputilsis_tel_number)
* [KSR.siputils.is_uri\(\)](#ksrsiputilsis_uri)
* [KSR.siputils.is_user\(\)](#ksrsiputilsis_user)
* [KSR.siputils.options_reply\(\)](#ksrsiputilsoptions_reply)
* [KSR.siputils.sip_parse_headers\(\)](#ksrsiputilssip_parse_headers)
* [KSR.siputils.uri_param\(\)](#ksrsiputilsuri_param)
* [KSR.siputils.uri_param_any\(\)](#ksrsiputilsuri_param_any)
* [KSR.siputils.uri_param_rm\(\)](#ksrsiputilsuri_param_rm)
* [KSR.siputils.uri_param_value\(\)](#ksrsiputilsuri_param_value)

## KSR.siputils.add_uri_param ##

```cpp
int KSR.siputils.add_uri_param(str "param");
```

* 📖[kamailio.cfg::function::add_uri_param\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.add_uri_param)

## KSR.siputils.cmp_aor ##

```cpp
int KSR.siputils.cmp_aor(str "uri1", str "uri2");
```

* 📖[kamailio.cfg::function::cmp_aor\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_aor)

## KSR.siputils.cmp_hdr_name ##

```cpp
int KSR.siputils.cmp_hdr_name(str "shname1", str "shname2");
```

* 📖[kamailio.cfg::function::cmp_hdr_name\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_hdr_name)

## KSR.siputils.cmp_uri ##

```cpp
int KSR.siputils.cmp_uri(str "uri1", str "uri2");
```

* 📖[kamailio.cfg::function::cmp_uri\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_uri)

## KSR.siputils.contact_param_check ##

```cpp
int KSR.siputils.contact_param_check(str "nparam");
```

* 📖[kamailio.cfg::function::contact_param_check\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_check)

## KSR.siputils.contact_param_decode ##

```cpp
int KSR.siputils.contact_param_decode(str "nparam");
```

* 📖[kamailio.cfg::function::contact_param_decode\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode)

## KSR.siputils.contact_param_decode_ruri ##

```cpp
int KSR.siputils.contact_param_decode_ruri(str "nparam");
```

* 📖[kamailio.cfg::function::contact_param_decode_ruri\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode_ruri)

## KSR.siputils.contact_param_encode ##

```cpp
int KSR.siputils.contact_param_encode(str "nparam", str "saddr");
```

* 📖[kamailio.cfg::function::contact_param_encode\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_encode)

## KSR.siputils.contact_param_encode_alias ##

```cpp
int KSR.siputils.contact_param_encode_alias(str "nparam", str "saddr");
```

* 📖[kamailio.cfg::function::contact_param_encode_alias\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_encode_alias)

## KSR.siputils.contact_param_rm ##

```cpp
int KSR.siputils.contact_param_rm(str "nparam");
```

* 📖[kamailio.cfg::function::contact_param_rm\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_rm)

## KSR.siputils.decode_contact ##

```cpp
int KSR.siputils.decode_contact();
```

* 📖[kamailio.cfg::function::decode_contact\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact)

## KSR.siputils.decode_contact_header ##

```cpp
int KSR.siputils.decode_contact_header();
```

* 📖[kamailio.cfg::function::decode_contact_header\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact_header)

## KSR.siputils.encode_contact ##

```cpp
int KSR.siputils.encode_contact(str "eprefix", str "eaddr");
```

* 📖[kamailio.cfg::function::encode_contact\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.encode_contact)

## KSR.siputils.has_totag ##

```cpp
int KSR.siputils.has_totag();
```

* 📖[kamailio.cfg::function::has_totag\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.has_totag)

## KSR.siputils.hdr_date_check ##

```cpp
int KSR.siputils.hdr_date_check(int tdiff);
```

* 📖[kamailio.cfg::function::hdr_date_check\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.hdr_date_check)

## KSR.siputils.is_alphanum ##

```cpp
int KSR.siputils.is_alphanum(str "tval");
```

* 📖[kamailio.cfg::function::is_alphanum\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanum)

## KSR.siputils.is_alphanumex ##

```cpp
int KSR.siputils.is_alphanumex(str "tval", str "eset");
```

* 📖[kamailio.cfg::function::is_alphanumex\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanumex)

## KSR.siputils.is_first_hop ##

```cpp
int KSR.siputils.is_first_hop();
```

* 📖[kamailio.cfg::function::is_first_hop\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop)

## KSR.siputils.is_first_hop_mode ##

```cpp
int KSR.siputils.is_first_hop_mode(int mode);
```

* 📖[kamailio.cfg::function::is_first_hop_mode\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop_mode)

## KSR.siputils.is_gruu ##

```cpp
int KSR.siputils.is_gruu();
```

* 📖[kamailio.cfg::function::is_gruu\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_gruu)

## KSR.siputils.is_http ##

```cpp
int KSR.siputils.is_http();
```

* 📖[kamailio.cfg::function::is_http\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_http)

## KSR.siputils.is_numeric ##

```cpp
int KSR.siputils.is_numeric(str "tval");
```

* 📖[kamailio.cfg::function::is_numeric\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_numeric)

## KSR.siputils.is_reply ##

```cpp
int KSR.siputils.is_reply();
```

* 📖[kamailio.cfg::function::is_reply\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_reply)

## KSR.siputils.is_request ##

```cpp
int KSR.siputils.is_request();
```

* 📖[kamailio.cfg::function::is_request\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_request)

## KSR.siputils.is_sip ##

```cpp
int KSR.siputils.is_sip();
```

* 📖[kamailio.cfg::function::is_sip\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_sip)

## KSR.siputils.is_tel_number ##

```cpp
int KSR.siputils.is_tel_number(str "tval");
```

* 📖[kamailio.cfg::function::is_tel_number\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_tel_number)

## KSR.siputils.is_uri ##

```cpp
int KSR.siputils.is_uri(str "suri");
```

* 📖[kamailio.cfg::function::is_uri\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_uri)

## KSR.siputils.is_user ##

```cpp
int KSR.siputils.is_user(str "suser");
```

* 📖[kamailio.cfg::function::is_user\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_user)

## KSR.siputils.options_reply ##

```cpp
int KSR.siputils.options_reply();
```

* 📖[kamailio.cfg::function::options_reply\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.options_reply)

## KSR.siputils.sip_parse_headers ##

```cpp
int KSR.siputils.sip_parse_headers();
```

* 📖[kamailio.cfg::function::sip_parse_headers\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.sip_parse_headers)

## KSR.siputils.uri_param ##

```cpp
int KSR.siputils.uri_param(str "sparam");
```

* 📖[kamailio.cfg::function::uri_param\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param)

## KSR.siputils.uri_param_any ##

```cpp
int KSR.siputils.uri_param_any(str "sparam");
```

* 📖[kamailio.cfg::function::uri_param_any\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_any)

## KSR.siputils.uri_param_rm ##

```cpp
int KSR.siputils.uri_param_rm(str "sparam");
```

* 📖[kamailio.cfg::function::uri_param_rm\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_rm)

## KSR.siputils.uri_param_value ##

```cpp
int KSR.siputils.uri_param_value(str "sparam", str "svalue");
```

* 📖[kamailio.cfg::function::uri_param_value\(\)](https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_value)
