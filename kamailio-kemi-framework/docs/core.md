## Core KEMI Functions ##

The exports to KEMI framework from the core of Kamailio:

  * several functions directly to `KSR` module (like `KSR.function(params)`), which are mostly
  the main functions from the core and for writing log messages (some being part of xlog module for
  native kamailio.cfg language)
  * the `KSR.pv` submodule, which are the generic functions to manage pseudo-variables, like set and get
  operations (some types of variables can have dedicated functions exported by various module, like
  `htable` to work with items in the shared memory hash table, or r-uri and xavp operations from `pv`
  and `kemix` modules).
  * the `KSR.hdr` submodule, which are the most used functions for managing SIP message headers
  (some of the functions in this submodules correspond to the ones in `textops` or `textopsx`
  modules for `kamailio.cfg`).

Example of using KEMI functions exported to Lua interpreter:

```Lua
KSR.dbg("a debug message from Lua script\n");
KSR.hdr.remove("Route");
```
Exported functions from core directly to KSR module or KSR.hdr submodule are listed in the next sections.

### KSR.add_local_rport() ###

`bool add_local_rport()`

Set the internal flag to add rport parameter to local generated Via header.

Example:

```
KSR.add_local_rport();
```

### KSR.add_tcp_alias() ###

`add_tcp_alias(int port)`

Adds a tcp port alias for the current connection (if tcp). Useful if you want to send all the trafic to port_alias through the same connection this request came from (it could help for firewall or nat traversal). When the `aliased` connection is closed (e.g. it is idle for too much time), all the port aliases are removed.

```
KSR.add_tcp_alias(5080);
```

### KSR.add_tcp_alias_via() ###

`int add_tcp_alias_via()`

Adds the port from the message via as an alias to TCP connection. See `add_tcp_alias(int port)` for more details.

Example:

```
KSR.add_tcp_alias_via();
```

### void KSR.log(...) ###

`void KSR.log(str "level", str "msg")`

Write a log message specifying the level value. The level parameter can be:

  * "dbg"
  * "info"
  * "notice"
  * "warn"
  * "crit"
  * "err"

If level value is not matched, then "err" log level is used.

Example:

```
KSR.log("dbg", "debug log message from: " + KSR.pv.getw("$si") + "\r\n");
```

### void KSR.dbg(...) ###

`void KSR.dbg(str "msg")`

Write a log message to DEBUG level.

Example:

```
KSR.dbg("debug log message from embedded interpreter\n");
```

### void KSR.err(...) ###

`void KSR.err(str "msg")`

Write a log message to ERROR level.

Example:

```
KSR.err("error log message from embedded interpreter\n");
```

### void KSR.info(...) ###

`void KSR.info(str "msg")`

Write a log message to INFO level.

Example:

```
KSR.info("info log message from embedded interpreter\n");
```

### void KSR.notice(...) ###

`void KSR.notice(str "msg")`

Write a log message to NOTICE level.

Example:

```
KSR.notice("notice log message from embedded interpreter\n");
```

### void KSR.warn(...) ###

`void KSR.warn(str "msg")`

Write a log message to WARN level.

Example:

```
KSR.warn("warn log message from embedded interpreter\n");
```

### void KSR.crit(...) ###

`void KSR.crit(str "msg")`

Write a log message to CRIT level.

Example:

```
KSR.crit("critical log message from embedded interpreter\n");
```

### int KSR.get_debug(...) ###

`int KSR.get_debug()`

Return the debug level for config logging.

Example:

```
if KSR.get_debug() < 2 then
  -- debug and info log messages are not printed
end
```

### KSR.force_rport() ###

`bool force_rport()`

Add rport parameter to the top Via of the incoming request and sent the
SIP response to source port.

### KSR.is_method() ###

`bool is_method(str "vmethod")`

Return true if the value of the parameter matches the method type of the SIP
message.

```JavaScript
if(KSR.is_method("INVITE")) {
  ...
}
```

### KSR.is_method_in() ###

`bool is_method_in(str "vmethod")`

Return true if SIP method of the currently processed message is matching one
of the corresponding characters given as parameter.

Matching the method is done based on corresponding characters:

  * `I` - INVITE
  * `A` - ACK
  * `B` - BYE
  * `C` - CANCEL
  * `R` - REGISTER
  * `M` - MESSAGE
  * `O` - OPTIONS
  * `F` - REFER
  * `S` - SUBSCRIBE
  * `P` - PUBLISH
  * `N` - NOTIFY
  * `U` - UPDATE
  * `K` - KDMQ
  * `G` - GET
  * `T` - POST
  * `V` - PUT
  * `D` - DELETE

Example:

```Lua
if KSR.is_method_in("IABC") then
  -- the method is INVITE, ACK, BYE or CANCEL
  ...
end
```

### KSR.is_INVITE() ###

`bool is_INVITE()`

Return true if the method type of the SIP message is `INVITE`.

```Lua
if KSR.is_INVITE() then
  ...
end
```

### KSR.is_ACK() ###

`bool is_ACK()`

Return true if the method type of the SIP message is `ACK`.

### KSR.is_BYE() ###

`bool is_BYE()`

Return true if the method type of the SIP message is `BYE`.

### KSR.is_CANCEL() ###

`bool is_CANCEL()`

Return true if the method type of the SIP message is `CANCEL`.

### KSR.is_REGISTER() ###

`bool is_REGISTER()`

Return true if the method type of the SIP message is `REGISTER`.

### KSR.is_MESSAGE() ###

`bool is_MESSAGE()`

Return true if the method type of the SIP message is `MESSAGE`.

### KSR.is_SUBSCRIBE() ###

`bool is_SUBSCRIBE()`

Return true if the method type of the SIP message is `SUBSCRIBE`.

### KSR.is_PUBLISH() ###

`bool is_PUBLISH()`

Return true if the method type of the SIP message is `PUBLISH`.

### KSR.is_NOTIFY() ###

`bool is_NOTIFY()`

Return true if the method type of the SIP message is `NOTIFY`.

### KSR.is_OPTIONS() ###

`bool is_OPTIONS()`

Return true if the method type of the SIP message is `OPTIONS`.

### KSR.is_REFER() ###

`bool is_REFER()`

Return true if the method type of the SIP message is `REFER`.


### KSR.is_INFO() ###

`bool is_INFO()`

Return true if the method type of the SIP message is `INFO`.

### KSR.is_UPDATE() ###

`bool is_UPDATE()`

Return true if the method type of the SIP message is `UPDATE`.

### KSR.is_PRACK() ###

`bool is_PRACK()`

Return true if the method type of the SIP message is `PRACK`.

### KSR.is_KDMQ() ###

`bool is_KDMQ()`

Return true if the method type of the SIP message is `KDMQ`.

### KSR.is_GET() ###

`bool is_GET()`

Return true if the method type of the HTTP message is `GET`.

### KSR.is_POST() ###

`bool is_POST()`

Return true if the method type of the HTTP message is `POST`.

### KSR.is_PUT() ###

`bool is_PUT()`

Return true if the method type of the HTTP message is `PUT`.

### KSR.is_DELETE() ###

`bool is_DELETE()`

Return true if the method type of the HTTP message is `DELETE`.

### KSR.is_myself(...) ###

`bool KSR.is_myself(str "uri")`

Return true of the URI address provided as parameter matches a local socket (IP)
or local domain.

```Lua
if KSR.is_myself("sip:127.0.0.1:5060") then
  ...
end
```

### KSR.is_myself_duri() ###

`bool is_myself_duri()`

Return true if the destination URI (`$du`) matches a local socket (IP) or local
domain.

### KSR.is_myself_furi() ###

`bool is_myself_furi()`

Return true if the URI in From header matches a local socket (IP) or local
domain.

```Lua
if KSR.is_myself_furi() then
  ...
end
```

### KSR.is_myself_nhuri() ###

`bool is_myself_nhuri()`

Return true if the next hop URI (`$nh(u)`) matches a local socket (IP) or local
domain.

### KSR.is_myself_ruri() ###

`bool is_myself_ruri()`

Return true if the R-URI matches a local socket (IP) or local
domain.

```Lua
if KSR.is_myself_ruri() then
  ...
end
```

### KSR.is_myself_turi() ###

`bool is_myself_turi()`

Return true if the URI in To header matches a local socket (IP) or local
domain.

```Lua
if KSR.is_myself_turi() then
  ...
end
```

### KSR.is_myself_suri() ###

`bool is_myself_suri()`

Return true if the URI built from source IP, source port and protocol matches a local socket (IP).

```Lua
if KSR.is_myself_suri() then
  ...
end
```

### KSR.is_myself_srcip() ###

`bool is_myself_srcip()`

Return true if the source IP matches a local socket (IP).

```Lua
if KSR.is_myself_srcip() then
  ...
end
```

### KSR.is_SCTP() ###

`bool is_SCTP()`

Return true if the incoming protocol is SCTP.

```Lua
if KSR.is_SCTP() then
  ...
end
```

### KSR.is_TCP() ###

`bool is_TCP()`

Return true if the incoming protocol is TCP.

```Lua
if KSR.is_TCP() then
  ...
end
```

### KSR.is_TLS() ###

`bool is_TLS()`

Return true if the incoming protocol is TLS.

```Lua
if KSR.is_TLS() then
  ...
end
```


### KSR.is_UDP() ###

`bool is_UDP()`

Return true if the incoming protocol is UDP.

```Lua
if KSR.is_UDP() then
  ...
end
```

### KSR.is_WS() ###

`bool is_WS()`

Return true if the incoming protocol is WS.

```Lua
if KSR.is_WS() then
  ...
end
```

### KSR.is_WSS() ###

`bool is_WSS()`

Return true if the incoming protocol is WSS.

```Lua
if KSR.is_WSS() then
  ...
end
```


### KSR.is_proto(...) ###

`bool is_proto(str sproto)`

Return true if the incoming protocol is matching one of the flags provided in
the `sproto` parameter. The flags are represented by letters and they are:

  * `e` or `E` - match for TLS protocol (encrypted stream)
  * `s` or `S` - match for SCTP protocol
  * `t` or `T` - match for TCP protocol
  * `u` or `U` - match for UDP protocol
  * `v` or `V` - match for WS protocol
  * `W` or `W` - match for WSS protocol

```Lua
if KSR.is_proto("EW") then
  ...
end
```

### KSR.is_IPv4() ###

`bool is_IPv4()`

Return true if the SIP message was received over IPv4.

```Lua
if KSR.is_IPv4() then
  ...
end
```

### KSR.is_IPv6() ###

`bool is_IPv6()`

Return true if the SIP message was received over IPv6.

```Lua
if KSR.is_IPv6() then
  ...
end
```

### KSR.setflag(...) ###

`bool KSR.setflag(int flag)`

Set the SIP message/transaction flag at the index provided by the parameter. The flag parameter
has to be a number from 0 to 31.

```
KSR.setflag(10);
```

### KSR.resetflag(...) ###

`bool KSR.resetflag(int flag)`

Reset the SIP message/transaction flag at the index provided by the parameter. The flag parameter
has to be a number from 0 to 31.

```
KSR.resetflag(10);
```

### KSR.isflagset(...) ###

`bool KSR.isflagset(int flag)`

Return true if the message/transaction flag at the index provided by the parameter is set
(the bit has value 1).

```
if ( KSR.isflagset(10) ) ...
```

### KSR.setbflag(...) ###

`bool KSR.setbflag(int flag)`

Set the branch flag at the index provided by the parameter. The flag parameter
has to be a number from 0 to 31.

```
KSR.setbflag(10);
```

### KSR.resetbflag(...) ###

`bool KSR.resetbflag(int flag)`

Reset the branch flag at the index provided by the parameter. The flag parameter
has to be a number from 0 to 31.

```
KSR.resetbflag(10);
```

### KSR.isbflagset(...) ###

`bool KSR.isbflagset(int flag)`

Return true if the branch flag at the index provided by the parameter is set
(the bit has value 1).

```
if ( KSR.isbflagset(10) ) ...
```

### KSR.setbiflag(...) ###

`bool KSR.setbiflag(int flag, int branch)`

Set the flag at the index provided by the first parameter to the branch number
specified by the second parameter. The flag parameter has to be a number from
0 to 31. The branch parameter should be between 0 and 12 (a matter of
`max_branches` global parameter).

```
KSR.setbiflag(10, 2);
```

### KSR.resetbiflag(...) ###

`bool KSR.resetbiflag(int flag, int branch)`

Reset a branch flag by position and branch index.

### KSR.isbiflagset(...) ###

`bool KSR.isbiflagset(int flag, int branch)`

Test if a branch flag is set by position and branch index.

### KSR.setsflag(...) ###

`bool KSR.setsflag(int flag)`

Set a script flag.

### KSR.resetsflag(...) ###

`bool KSR.resetsflag(int flag)`

Reset a script flag.

### KSR.issflagset(...) ###

`bool KSR.issflagset(int flag)`

Test if a script flag is set.

### KSR.seturi(...) ###

`bool KSR.seturi(str "uri")`

Set the request URI (R-URI).

Example:

```
KSR.seturi("sip:alice@voip.com");
```

### KSR.setuser(...) ###

`bool KSR.setuser(str "user")`

Example:

```
KSR.setuser("alice");
```

### KSR.sethost(...) ###

`bool KSR.sethost(str "host")`

Example:

```
KSR.sethost("voip.com");
```

### KSR.setdsturi(...) ###

`bool KSR.setdsturi(str "uri")`

Example:

```
KSR.setdsturi("sip:voip.com:5061;transport=tls");
```

### KSR.resetdsturi(...) ###

`bool KSR.resetdsturi()`

Reset the destination URI (aka: outbound proxy address, dst_uri, $du).

### KSR.isdsturiset(...) ###

`bool KSR.isdsturiset()`

Test if destination URI is set.

### KSR.force_rport(...) ###

`bool KSR.force_rport()`

Set the flag for "rport" handling (send the reply based on source address
instead of Via header).

Example:

```
KSR.force_rport();
```

### KSR.set_drop(...) ###

`void KSR.set_drop()`

Set the DROP flag, so at the end of KEMI script execution, the SIP request branch or the SIP response is not forwarded.

Note: it doesn't not stop the execution of KEMI script, see KSR.x.drop().

Example:

```
KSR.set_drop();
```

### KSR.set_advertised_address() ###

`int set_advertised_address(str "addr")`

Set the address (host or ip) to be advertised in Via header.

### KSR.set_advertised_port() ###

`int set_advertised_port(str "port")`

Set the port (in string format) to be advertised in Via header.

### KSR.set_forward_close(...) ###

`bool KSR.set_forward_close()`

Set the flag to close the connection after forwarding the message.

### KSR.set_forward_no_connect(...) ###

`bool KSR.set_forward_no_connect()`

Set the flag to not open a connection if the connection to the target does not exist when attempting
to forward a message.

### KSR.set_reply_close(...) ###

`bool KSR.set_reply_close()`

Set the flag to close the connection after sending a response.

### KSR.set_reply_no_connect(...) ###

`bool KSR.set_reply_no_connect()`

Set the flag to not open a connection if the connection for sending the response
does not exist.

### KSR.forward(...) ###

`int KSR.forward()`

Forward the SIP request in stateless mode to the address set in destination
URI ($du), or, if this is not set, to the address in request URI ($ru).

### KSR.forward_uri(...) ###

`int KSR.forward_uri(str "uri")`

Forward the SIP request in stateless mode to the address provided in the SIP
URI parameter.

```
KSR.forward_uri("sip:127.0.0.1:5080;transport=tcp");
```

### KSR.route(...) ###

`int KSR.route(str "rname")`

Execute a route block written in configuration file using native scripting
language. It returns `0` if the last action in the route block is an exit
operation (e.g., like `exit`, `drop` or Kamailio function returning `0`).

Example:

```
KSR.route("REQINIT");
```

### KSR.pv Submodule ###

`KSR.pv` submodule provides the functions to get, set and test the values of
pseduo-variables.

The `pvname` that appears in the next sections in the function prototypes has to
be a valid pseudo-variable name for Kamailio native configuration file (for
example `$ru`, `$var(x)`, `$shv(z)`, ...). The list of available pseudo-variables
is available on the wiki:

  * https://www.kamailio.org/wiki/cookbooks/devel/pseudovariables

Note: functions exported by Kamailio's `pv` module are in `KSR.pvx` package.

### KSR.pv.get(...) ###

`xval KSR.pv.get(str "pvname")`

Return the value of pseudo-variable `pvname`. The returned value can be string, integer or null (if pseudo-variable isn't set or `$null`).

Example:

```
KSR.dbg("ruri is: " + KSR.pv.get("$ru") + "\n");
```

### KSR.pv.gete(...) ###

`xval KSR.pv.gete(str "pvname")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the empty string
("") if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.gete("$avp(x)") + "\n");
```

### KSR.pv.getvn(...) ###

`xval KSR.pv.getvn(str "pvname", int vn)`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the parameter `vn`
if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.getvn("$avp(x)", 0) + "\n");
```

### KSR.pv.getvs(...) ###

`xval KSR.pv.getvs(str "pvname", str "vs")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the parameter `vs`
if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.getvs("$avp(x)", "foo") + "\n");
```

### KSR.pv.getw(...) ###

`xval KSR.pv.getw(str "pvname")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the string `<<null>>`
if the variable is having the `$null` value. This should be used instead of `KSR.pv.get(...)`
in the scripting languages that throw and error when attempting to print a `NULL` (or `NIL`) value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.getw("$avp(x)") + "\n");
```

### KSR.pv.seti(...) ###

`void KSR.pv.seti(str "pvname", int val)`

Set the value of pseudo-variable `pvname` to integer value provided by parameter `val`.

Example:

```
KSR.pv.seti("$var(x)", 10);
```

### KSR.pv.sets(...) ###

`void KSR.pv.sets(str "pvname", str "val")`

Set the value of pseudo-variable `pvname` to string value provided by parameter `val`.

Example:

```
KSR.pv.sets("$var(x)", "kamailio");
```

### KSR.pv.unset(...) ###

`void KSR.pv.unset(str "pvname")`

Set the value of pseudo-variable `pvname` to `$null`.

Example:

```
KSR.pv.unset("$avp(x)");
```

### KSR.pv.is_null(...) ###

`bool KSR.pv.is_null(str "pvname")`

Return true if pseudo-variable `pvname` is `$null`.

Example:

```
if(KSR.pv.is_null("$avp(x)")) {
  ...
}
```

### KSR.hdr Submodule ###

### KSR.hdr.append(...) ###

`int KSR.hdr.append(str "hdrval")`

Append header to current SIP message (request or reply). It will be added after
the last header.

Example:

```
KSR.hdr.append("X-My-Hdr: " + KSR.pv.getw("$si") + "\r\n");
```

### KSR.hdr.append_after(...) ###

`int KSR.hdr.append_after(str "hdrval", str "hdrname")`

Append header to current SIP message (request or reply). It will be added after
the first header matching the name `hdrname`.

Example:

```
KSR.hdr.append_after("X-My-Hdr: " + KSR.pv.getw("$si") + "\r\n", "Call-Id");
```

### KSR.hdr.insert(...) ###

`int KSR.hdr.insert(str "hdrval")`

Insert header to current SIP message (request or reply). It will be added before
the first header.

Example:

```
KSR.hdr.insert("X-My-Hdr: " + KSR.pv.getw("$si") + "\r\n");
```

### KSR.hdr.insert_before(...) ###

`int KSR.hdr.insert_before(str "hdrval", str "hdrname")`

Insert header to current SIP message (request or reply). It will be added before
the header matching the name `hdrname`.

Example:

```
KSR.hdr.insert_before("X-My-Hdr: " + KSR.pv.getw("$si") + "\r\n", "Call-Id");
```

### KSR.hdr.remove(...) ###

`int KSR.hdr.remove(str "hdrval")`

Remove all the headers with the name `hdrval`.

Example:

```
KSR.hdr.remove("X-My-Hdr");
```

### KSR.hdr.rmappend(...) ###

`int KSR.hdr.rmappend(str "hrm", str "hadd")`

Remove all the headers with the name `hrm` and append `hadd`. The value for
`hadd` must include header name name and ending `\r\n`. This function is a
a wrapper for `KSR.hdr.remove("hrm")` and `KSR.hdr.append("hadd")`.

Example:

```
KSR.hdr.remove("X-My-Hdr", "X-My-Hdr: abc\r\n");
```

### KSR.hdr.is_present(...) ###

`int KSR.hdr.is_present(str "hdrval")`

Return greater than 0 if a header with the name `hdrval` exists and less than
0 if there is no such header.

Example:

```
if(KSR.hdr.is_present("X-My-Hdr") > 0) {
  ...
}
```

### KSR.hdr.append_to_reply(...) ###

`int KSR.hdr.append_to_reply(str "hdrval")`

Add a header to the SIP response to be generated by Kamailio for the current
SIP request.

Example:

```
KSR.hdr.append_to_reply("X-My-Hdr: " + KSR.pv.getw("$si") + "\r\n");
```

### KSR.hdr.get(...) ###

`xval KSR.hdr.get(str "hname")`

Return the value of the header matching the name with `hname` or `NULL` if that
header is not found.

Example:

```
v = KSR.hdr.get("X-My-Hdr");
```

### KSR.hdr.get_idx(...) ###

`xval KSR.hdr.get(str "hname", int idx)`

Return the value of the header matching the name with `hname` at the index `idx`
or `NULL` if that header is not found. The index starts with `0` for first header
and can be negative to count backwards from the last header (which corresponds
to index `-1`).

Example:

```
v = KSR.hdr.get_idx("X-My-Hdr", 1);
```

### KSR.hdr.gete(...) ###

`xval KSR.hdr.gete(str "hname")`


Return the value of the header matching the name with `hname` or empty string
if that header is not found.


Example:

```
v = KSR.hdr.gete("X-My-Hdr");
```

### KSR.hdr.gete_idx(...) ###

`xval KSR.hdr.gete(str "hname", int idx)`

Return the value of the header matching the name with `hname` at the index `idx`
or empty string if that header is not found.


Example:

```
v = KSR.hdr.gete_idx("X-My-Hdr", -1);
```

### KSR.hdr.getw(...) ###

`xval KSR.hdr.getw(str "hname")`

Return the value of the header matching the name with `hname` or string `<<null>>`
if that header is not found.


Example:

```
v = KSR.hdr.getw("X-My-Hdr");
```

### KSR.hdr.getw_idx(...) ###

`xval KSR.hdr.getw_idx(str "hname", int idx)`

Return the value of the header matching the name with `hname` at the index `idx`
or string `<<null>>` if that header is not found.


Example:

```
v = KSR.hdr.getw_idx("X-My-Hdr", 2);
```

### KSR.hdr.match_content(...) ###

`bool KSR.hdr.match_content(str "hname", str "op", str "mval", str "eidx")`

Return `true` on matching the content of headers based on the expression from
the parameters, otherwise `false`.

The parameters are:
  * `hname` - header name
  * `op`- the matching operator, it can be: `eq` - equal; `ne` - not equal;
  `sw` - starts with; `in` - includes;
  * `mval` - matching value
  * `eidx` - expression of the index, it can be: 'f' - first header only;
  `l` - last header only; `a` - all headers; `o` - at least one header

Example:

```
if(KSR.hdr.match_content("X-My-Hdr", "in", "test", "o")) { ... }
```
