## PV And Special KEMI Functions ##

Each KEMI interpreter module (respectively `app_jsdt`, `app_lua`, `app_python` and `app_sqlang`) exports the
submodules `KSR.pv` and `KSR.x`.

`KSR.pv` submodule provides the functions to get, set and test the values of pseduo-variables. It is implemented per
module because the get function has to return either integer or string value.

The `pvname` that appears in the next sections in the function prototypes has to be a valid pseudo-variable name for
 Kamailio native configuration file (for example `$ru`, `$var(x)`, `$shv(z)`, ...).

Note: functions exported by Kamailio's `pv` module are in `KSR.pvx` package.

`KSR.x` submodule provides special functions that need custom code per interpreter.

The functions exported by these modules are listed in the next sections.

### KSR.pv.get(...) ###

`val KSR.pv.get("pvname")`

Return the value of pseudo-variable `pvname`. The returned value can be string or integer.

Example:

```
KSR.dbg("ruri is: " + KSR.pv.get("$ru") + "\n");
```

### KSR.pv.getw(...) ###

`val KSR.pv.getw("pvname")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the string `<<null>>`
if the variable is having the `$null` value. This should be used instead of `KSR.pv.get(...)`
in the scripting languages that throw and error when attempting to print a `NULL` (or `NIL`) value.

Example:

```
KSR.dbg("ruri is: " + KSR.pv.getw("$avp(x)") + "\n");
```

### KSR.pv.seti(...) ###

`void KSR.pv.seti("pvname", intval)`

Set the value of pseudo-variable `pvname` to integer value provided by parameter `intval`.

Example:

```
KSR.pv.seti("$var(x)", 10);
```

### KSR.pv.sets(...) ###

`void KSR.pv.sets("pvname", "strval")`

Set the value of pseudo-variable `pvname` to string value provided by parameter `strval`.

Example:

```
KSR.pv.sets("$var(x)", "kamailio");
```

### KSR.pv.unset(...) ###

`void KSR.pv.unset("pvname")`

Set the value of pseudo-variable `pvname` to `$null`.

Example:

```
KSR.pv.unset("$avp(x)");
```

### KSR.pv.is_null(...) ###

`bool KSR.pv.is_null("pvname")`

Return true if pseudo-variable `pvname` is `$null`.

Example:

```
if(KSR.pv.is_null("$avp(x)")) {
  ...
}
```

### KSR.x.modf(...) ###

`int KSR.x.modf("fname", params...)`

Execute a function (specified by `fname`) exported by a Kamailio module. Additional parameters must be string and
they are passed to the Kamailio module function.

Example:

```
KSR.x.modf("sl_send_reply", "200", "OK");
```

### KSR.x.exit(...) ###

`void KSR.x.exit()`

Equivalent of `exit` from native kamailio.cfg scripting language, stop the execution of the SIP routing script.

It is not exported by each KEMI interpreter module, in that case likely the scripting
language has an `exit` function that can be used for this purpose. In the case there
is no `exit`, just do `return` from the main KEMI callback functions
(e.g., for SIP request routing do `return` from `ksr_request_route()`).

For Python, one can use `exit()` or `os.exit()`.

### KSR.x.drop(...) ###

`void KSR.x.drop()`

Equivalent of `drop` from native kamailio.cfg scripting language, stop the execution of the SIP routing script
and drop routing further the SIP request branch or response.

If not exported by a KEMI interpreter module, use `KSR.set_drop()` before terminating
the execution of the KEMI callback function (see the notes for `KSR.x.exit`).
