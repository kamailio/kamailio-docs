## Core KEMI Functions ##

The core of Kamailio exports via KEMI:

  * several functions directly to `KSR` module (like `KSR.function(params)`), which are mostly
  the main function from the core and for writing log messages
  * the `KSR.hdr` submodule, which are the most used functions for managing SIP message headers

Example of using KEMI functions exported to Lua interpreter:

```Lua
KSR.dbg("a debug message from Lua script\n");
KSR.hdr.remove("Route");
```
Exported functions from core directly to KSR module or KSR.hdr submodule are listed in the next sections.

### void KSR.dbg(...) ###

`void KSR.dbg("msg")`

### void KSR.err(...) ###

`void KSR.err("msg")`

### void KSR.info(...) ###

`void KSR.info("msg")`

### oid KSR.log(...) ###

`void KSR.log("level", "msg")`

### KSR.drop(...) ###

`void KSR.drop()`

### KSR.is_myself(...) ###

`bool KSR.is_myself("uri")`

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

### KSR.is_method(...) ###

`bool KSR.is_method("methods")`

### KSR.force_rport(...) ###

`bool KSR.force_rport()`

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