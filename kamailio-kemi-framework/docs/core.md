## Core KEMI Functions ##

The core of Kamailio exports via KEMI:

  * several functions directly to `KSR` module (like `KSR.function(params)`), which are mostly
  the main function from the core and for writing log messages (some being part of xlog module for
  native kamailio.cfg language)
  * the `KSR.hdr` submodule, which are the most used functions for managing SIP message headers

Example of using KEMI functions exported to Lua interpreter:

```Lua
KSR.dbg("a debug message from Lua script\n");
KSR.hdr.remove("Route");
```
Exported functions from core directly to KSR module or KSR.hdr submodule are listed in the next sections.

### KSR.add_local_rport() ###

`bool add_local_rport()`

### KSR.add_tcp_alias() ###

`add_tcp_alias(int port)`

### KSR.add_tcp_alias_via() ###

`int add_tcp_alias_via()`

### void KSR.dbg(...) ###

`void KSR.dbg("msg")`

Write a log message to DEBUG level.

### void KSR.err(...) ###

`void KSR.err("msg")`

Write a log message to ERROR level.

### KSR.force_rport() ###

`bool force_rport()`

### void KSR.info(...) ###

`void KSR.info("msg")`

Write a log message to INFO level.

### KSR.is_method() ###

`bool is_method(str "vmethod")`

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
  * `S` - SUBSCRIBE
  * `P` - PUBLISH
  * `N` - NOTIFY
  * `U` - UPDATE

Example:

```
if KSR.is_method_in("IABC") then
  -- the method is INVITE, ACK, BYE or CANCEL
  ...
end
```

### KSR.is_INVITE() ###

`bool is_INVITE()`

### KSR.is_ACK() ###

`bool is_ACK()`

### KSR.is_BYE() ###

`bool is_BYE()`

### KSR.is_CANCEL() ###

`bool is_CANCEL()`

### KSR.is_REGISTER() ###

`bool is_REGISTER()`

### KSR.is_MESSAGE() ###

`bool is_MESSAGE()`

### KSR.is_SUBSCRIBE() ###

`bool is_SUBSCRIBE()`

### KSR.is_PUBLISH() ###

`bool is_PUBLISH()`

### KSR.is_NOTIFY() ###

`bool is_NOTIFY()`

### KSR.is_OPTIONS() ###

`bool is_OPTIONS()`

### KSR.is_INFO() ###

`bool is_INFO()`

### KSR.is_UPDATE() ###

`bool is_UPDATE()`

### KSR.is_PRACK() ###

`bool is_PRACK()`

### KSR.is_myself(...) ###

`bool KSR.is_myself("uri")`

### KSR.is_myself_furi() ###

`bool is_myself_furi()` </a>

### KSR.is_myself_ruri() ###

`bool is_myself_ruri()`

### KSR.is_myself_turi() ###

`bool is_myself_turi()`

### void KSR.log(...) ###

`void KSR.log("level", "msg")`

Write a log message specifying the level value. The level parameter can be:

  * "dbg"
  * "info"
  * "warn"
  * "crit"
  * "err"

If level value is not matched, then "err" log level is used.

### KSR.setflag(...) ###

`bool KSR.setflag(flag)`

### KSR.resetflag(...) ###

`bool KSR.resetflag(flag)`

### KSR.isflagset(...) ###

`bool KSR.isflagset(flag)`

### KSR.setbflag(...) ###

`bool KSR.setbflag(flag)`

### KSR.resetbflag(...) ###

`bool KSR.resetbflag(flag)`

### KSR.isbflagset(...) ###

`bool KSR.isbflagset(flag)`

### KSR.setbiflag(...) ###

`bool KSR.setbiflag(flag, branch)`

### KSR.resetbiflag(...) ###

`bool KSR.resetbiflag(flag, branch)`

### KSR.isbiflagset(...) ###

`bool KSR.isbiflagset(flag, branch)`

### KSR.setsflag(...) ###

`bool KSR.setsflag(flag)`

### KSR.resetsflag(...) ###

`bool KSR.resetsflag(flag)`

### KSR.issflagset(...) ###

`bool KSR.issflagset(flag)`

### KSR.seturi(...) ###

`bool KSR.seturi("uri")`

### KSR.setuser(...) ###

`bool KSR.setuser("user")`

### KSR.sethost(...) ###

`bool KSR.sethost("host")`

### KSR.setdsturi(...) ###

`bool KSR.setdsturi("uri")`

### KSR.resetdsturi(...) ###

`bool KSR.resetdsturi()`

### KSR.isdsturiset(...) ###

`bool KSR.isdsturiset()`

### KSR.force_rport(...) ###

`bool KSR.force_rport()`

### KSR.set_drop(...) ###

`void KSR.set_drop()`

Set the DROP flag, so at the end of KEMI script execution, the SIP request branch or the SIP response is not forwarded.

Note: it doesn't not stop the execution of KEMI script, see KSR.x.drop().

### KSR.set_advertised_address() ###

`int set_advertised_address(str "addr")`

### KSR.set_advertised_port() ###

`int set_advertised_port(str "port")`

### KSR.set_forward_close(...) ###

`bool KSR.set_forward_close()`

### KSR.set_forward_no_connect(...) ###

`bool KSR.set_forward_no_connect()`

### KSR.set_reply_close(...) ###

`bool KSR.set_reply_close()`

### KSR.set_reply_no_connect(...) ###

`bool KSR.set_reply_no_connect()`

### KSR.forward(...) ###

`int KSR.forward()`

### KSR.forward_uri(...) ###

`int KSR.forward_uri("uri")`

### KSR.hdr.append(...) ###

`int KSR.hdr.append("hdrval")`

### KSR.hdr.append_after(...) ###

`int KSR.hdr.append_after("hdrval", "hdrname")`

### KSR.hdr.insert(...) ###

`int KSR.hdr.insert("hdrval")`

### KSR.hdr.insert_before(...) ###

`int KSR.hdr.insert_before("hdrval", "hdrname")`

### KSR.hdr.remove(...) ###

`int KSR.hdr.remove("hdrval")`

### KSR.hdr.is_present(...) ###

`int KSR.hdr.is_present("hdrval")`

### KSR.hdr.append_to_reply(...) ###

`int KSR.hdr.append_to_reply("hdrval")`
