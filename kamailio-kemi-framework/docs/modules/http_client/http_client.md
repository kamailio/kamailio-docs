# http_client #

* 📖[kamailio.cfg::module::http_client.html](https://kamailio.org/docs/modules/devel/modules/http_client.html)

Exported functions:

* [KSR.http_client.curl_connect\(\)](#ksrhttp_clientcurl_connect)
* [KSR.http_client.curl_connect_post\(\)](#ksrhttp_clientcurl_connect_post)
* [KSR.http_client.get_hdrs\(\)](#ksrhttp_clientget_hdrs)
* [KSR.http_client.query\(\)](#ksrhttp_clientquery)
* [KSR.http_client.query_post\(\)](#ksrhttp_clientquery_post)
* [KSR.http_client.query_post_hdrs\(\)](#ksrhttp_clientquery_post_hdrs)
* [KSR.http_client.query_request\(\)](#ksrhttp_clientquery_request)
* [KSR.http_client.query_request_v2pk\(\)](#ksrhttp_clientquery_request_v2pk)

## KSR.http_client.curl_connect ##

```cpp
int KSR.http_client.curl_connect(str "con", str "url", str "dpv");
```

* 📖[kamailio.cfg::function::curl_connect\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect)

## KSR.http_client.curl_connect_post ##

```cpp
int KSR.http_client.curl_connect_post(str "con", str "url", str "ctype", str "data", str "dpv");
```

* 📖[kamailio.cfg::function::curl_connect_post\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect_post)

## KSR.http_client.get_hdrs ##

```cpp
int KSR.http_client.get_hdrs(str "url", str "body", str "hdrs", str "dpv");
```

* 📖[kamailio.cfg::function::get_hdrs\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.get_hdrs)

## KSR.http_client.query ##

```cpp
int KSR.http_client.query(str "url", str "dpv");
```

* 📖[kamailio.cfg::function::query\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query)

## KSR.http_client.query_post ##

```cpp
int KSR.http_client.query_post(str "url", str "post", str "dpv");
```

* 📖[kamailio.cfg::function::query_post\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post)

## KSR.http_client.query_post_hdrs ##

```cpp
int KSR.http_client.query_post_hdrs(str "url", str "post", str "hdrs", str "dpv");
```

* 📖[kamailio.cfg::function::query_post_hdrs\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post_hdrs)

## KSR.http_client.query_request ##

```cpp
int KSR.http_client.query_request(str "met", str "url", str "body", str "hdrs", str "dpv");
```

* 📖[kamailio.cfg::function::query_request\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_request)

## KSR.http_client.query_request_v2pk ##

```cpp
int KSR.http_client.query_request_v2pk(str "met", str "url", str "body", str "hdrs", str "dpv");
```

* 📖[kamailio.cfg::function::query_request_v2pk\(\)](https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_request_v2pk)
