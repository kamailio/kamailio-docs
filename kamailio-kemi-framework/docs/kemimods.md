## Special KEMI Functions ##

Each KEMI interpreter module (respectively `app_jsdt`, `app_lua`, `app_python`,`app_python3`, `app_ruby`
and `app_sqlang`) exports the submodule `KSR.x`.

`KSR.x` submodule provides special functions that need custom code per interpreter.

The functions exported by these modules are listed in the next sections.

### KSR.x.modf(...) ###

`int KSR.x.modf(str "fname", params...)`

Execute a function (specified by `fname`) exported by a Kamailio module. Additional parameters must be string and
they are passed to the Kamailio module function.

Example:

```
KSR.x.modf("sl_send_reply", "200", "OK");
```

Important note: try not to use this function, prefer the use of dedicated KSR functions. If you have to use
this function, check if it has fixup and fixup-free functions in the C code in order to avoid memory leaks.
If you are not sure how to do the check, ask on sr-users mailing list if it is safe to use it for a specific
module fuction.

### KSR.x.exit(...) ###

`void KSR.x.exit()`

Equivalent of `exit` from native kamailio.cfg scripting language, stop the execution of the SIP routing script.

Example:

```
KSR.x.exit();
```

It is not exported by each KEMI interpreter module, in that case likely the scripting
language has an `exit` function that can be used for this purpose. Respectively:

  * for Python and Python3, use `exit()` or `sys.exit()`.
  * for Ruby, use `exit`.

In the case there is no `KSR.x.exit` and no usable `exit` in the KEMI scripting language, just do `return`
from the main KEMI callback functions (e.g., for SIP request routing do `return` from `ksr_request_route()`).

IMPORTANT: be careful with the native `exit` functions in some KEMI interpreters, such as Lua, because they
can trigger the stop of the application, in this case stopping Kamailio completely.

### KSR.x.drop(...) ###

`void KSR.x.drop()`

Equivalent of `drop` from native kamailio.cfg scripting language, stop the execution of the SIP routing script
and drop routing further the SIP request branch or response.

Example:

```
KSR.x.drop();
```

If not exported by a KEMI interpreter module, use `KSR.set_drop()` before terminating
the execution of the KEMI callback function (see the notes for `KSR.x.exit`). For example:

  * for Python or Python3, use:

```
KSR.set_drop()
exit()
```
