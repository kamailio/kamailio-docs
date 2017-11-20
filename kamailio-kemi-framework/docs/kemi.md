## KEMI Interpreters ##

Following KEMI scripting languages can be used to write SIP routing logic for Kamailio:

  * JavaScript
  * Lua
  * Python
  * Squirrel

A configuration file for Kamailio that uses a KEMI scripting language has the glabal parameters, loading modules and
module parameters in the native scripting and sets the value of `cfgengine` to the KEMI scripting language identifier.

The KEMI scripting language identifiers are:

  * `jsdt` - for JavaScript
  * `lua` - for Lua
  * `python` - for Python
  * `sqlang` - for Squirrel

### JavaScript KEMI Interpreter ###

It is implemented by `app_jsdt` module. The JavaScript interpreter is imported inside the module from
[DukTape](www.ducktape.org) project, therefore it doesn't require to install any external libraries.

To use it, set inside `kamailio.cfg`:

```
loadmodule "app_jsdk.so"
modparam("app_jsdk", "load", "/path/to/script.js")
cfgengine "jsdt"
```

A complete example of using JavaScript as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-jsdt.js](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-jsdt.js)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGJSDT
```

The file `kamailio-basic-kemi-jsdt.js` has to be saved to local disk and the `load` parameter for `app_jsdt` module
inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_jsdk` is available at:

  * [app_jsdt.html](https://kamailio.org/docs/modules/devel/modules/app_jsdt.html)

### Lua KEMI Interpreter ###

It is implemented by `app_lua` module. The Lua interpreter is linked from `liblua` library, supported Lua versions: 
5.1 and 5.2.

```
loadmodule "app_lua.so"
modparam("app_lua", "load", "/path/to/script.lua")
cfgengine "lua"
```

A complete example of using Lua as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-lua.lua](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-lua.lua)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGLUA
```

The file `kamailio-basic-kemi-lua.lua` has to be saved to local disk and the `load` parameter for `app_lua` module
inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_lua` is available at:

  * [app_lua.html](https://kamailio.org/docs/modules/devel/modules/app_lua.html)

### Python KEMI Interpreter ###

It is implemented by `app_python` module. The Python interpreter is linked from `libpython`, supported Python versions:
2.5, 2.6 and 3.x.

```
loadmodule "app_python.so"
modparam("app_python", "script_name", "/path/to/script.py")
cfgengine "python"
```

A complete example of using Python as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-python.py](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-python.py)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGPYTHON
```

The file `kamailio-basic-kemi-python.py` has to be saved to local disk and the `script_name` parameter for
`app_python` module inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_python` is available at:

  * [app_python.html](https://kamailio.org/docs/modules/devel/modules/app_python.html)

### Squirrel KEMI Interpreter ###

It is implemented by `app_sqlang` module. The Squirrel language interpreter is imported inside the module from
[Squirrel](www.squirrel-lang.org) project, therefore it doesn't require to install any external libraries.

```
loadmodule "app_sqlang.so"
modparam("app_sqlang", "load", "/path/to/script.sq")
cfgengine "sqlang"
```

A complete example of using Squirrel as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-squirrel.sq](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-squirrel.sq)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGSQLANG
```

The file `kamailio-basic-kemi-squirrel.sq` has to be saved to local disk and the `load` parameter for `app_sqlang`
module inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_sqlang` is available at:

  * [app_sqlang.html](https://kamailio.org/docs/modules/devel/modules/app_sqlang.html)

## KEMI Functions ##

Inside the routing script, the functions exported by Kamailio through KEMI are available via `KSR` module. With very
few exceptions, the KEMI functions return either an integer or a bool value and can take up to six parameters of type
string or integer.

The integer return code from a Kemi functions has to be evaluated with the following rules:

  * `the value is greater than 0`, then the function was successfully executed and a logical evaluation should be
  considered true
  * `the value is less than 0`, then the function was not successfully executed or the function was successfully
  executed and the a logical evaluation should be considered false
  * `the value is equal to 0`, then the execution of the KEMI script should be terminated (be careful with execution of
  `exit()` function from the embedded interpreter language, it may kill the interpreter completely, which in this case
  is Kamailio, resulting in shutting down Kamailio - hint: check `KSR.x.exit()`)

The bool return code is expected to be evaluated as `true` or `false` inside the KEMI script.

If a function has `void` as return type in the signature, the it doesn't return any value.

Few functions may return a string value.

The convention for the parameters in the signature of the functions is to enclose in double quotes if the parameter
has a string type and no quotes if the parameter has integer type.

Most of the functions exported through KEMI have an equivalent in the functions available in the native scripting
language. Generic mapping rules:

  * if a parameter value is expected to be used as integer, then KEMI function has it as integer parameter (note: in
  the native scripting language, it used to be a rule that all parameters of the functions exported by modules to be
  provided as string)
  * if a function from native scripting language has variants with different number of parameters, then KEMI exports
  one function for each of the variants (to cope with the scripting languages that do not support variadic number of
  parameters). The names of the related functions are similar.

The available KEMI functions in a running instance of Kamailio can be listed via an RPC command. A matter of the
interpreter used, one of the following commands needs to be run:

```
kamctl rpc app_jsdt.api_list
kamctl rpc app_lua.api_list
kamctl rpc app_python.api_list
kamctl rpc app_sqlang.api_list
```