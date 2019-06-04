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

`val KSR.pv.get(str "pvname")`

Return the value of pseudo-variable `pvname`. The returned value can be string or integer.

Example:

```
KSR.dbg("ruri is: " + KSR.pv.get("$ru") + "\n");
```

### KSR.pv.gete(...) ###

`val KSR.pv.gete(str "pvname")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the empty string
("") if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.gete("$avp(x)") + "\n");
```

### KSR.pv.getvn(...) ###

`val KSR.pv.getvn(str "pvname", int vn)`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the parameter `vn`
if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.getvn("$avp(x)", 0) + "\n");
```

### KSR.pv.getvs(...) ###

`val KSR.pv.getvs(str "pvname", str "vs")`

Return the value of pseudo-variable `pvname` if it is different than `$null` or the parameter `vs`
if the variable is having the `$null` value.

Example:

```
KSR.dbg("avp is: " + KSR.pv.getvs("$avp(x)", "foo") + "\n");
```

### KSR.pv.getw(...) ###

`val KSR.pv.getw(str "pvname")`

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

### KSR.x.modf(...) ###

`int KSR.x.modf(str "fname", params...)`

Execute a function (specified by `fname`) exported by a Kamailio module. Additional parameters must be string and
they are passed to the Kamailio module function.

Example:

```
KSR.x.modf("sl_send_reply", "200", "OK");
```

Important note: try not to use this function, prefer the use of dedicated KSR fuctions. If you have to use
this function, check if it has fixup and fixup-free functions in the C code in order to avoid memory leaks.
If you are not sure how to do the check, ask on sr-users mailing list if it is safe to use it for a specific
module fuction.

### KSR.x.exit(...) ###

`void KSR.x.exit()`

Equivalent of `exit` from native kamailio.cfg scripting language, stop the execution of the SIP routing script.

It is not exported by each KEMI interpreter module, in that case likely the scripting
language has an `exit` function that can be used for this purpose. In the case there
is no `exit`, just do `return` from the main KEMI callback functions
(e.g., for SIP request routing do `return` from `ksr_request_route()`).

For Python, one can use `exit()` or `os.exit()`.

For Ruby, one can use `exit`.

### KSR.x.drop(...) ###

`void KSR.x.drop()`

Equivalent of `drop` from native kamailio.cfg scripting language, stop the execution of the SIP routing script
and drop routing further the SIP request branch or response.

If not exported by a KEMI interpreter module, use `KSR.set_drop()` before terminating
the execution of the KEMI callback function (see the notes for `KSR.x.exit`).
