## KEMI Interpreters ##

The following KEMI scripting languages can be used to write SIP routing logic for Kamailio:

  * JavaScript
  * Lua
  * Python2
  * Python3
  * Ruby
  * Squirrel

A configuration file for Kamailio that uses a KEMI scripting language has the global parameters, loading modules and
module parameters in the native scripting and sets the value of `cfgengine` to the KEMI scripting language identifier.

The KEMI scripting language identifiers are:

  * `jsdt` - for JavaScript
  * `lua` - for Lua
  * `python` - for Python2
  * `python` - for Python3
  * `ruby` - for Ruby
  * `sqlang` - for Squirrel

### JavaScript KEMI Interpreter ###

It is implemented by `app_jsdt` module. The JavaScript interpreter is imported inside the module from
[DukTape](https://www.duktape.org/) project, therefore it doesn't require to install any external libraries.

To use it, set inside `kamailio.cfg`:

```
loadmodule "app_jsdt.so"
modparam("app_jsdt", "load", "/path/to/script.js")
cfgengine "jsdt"
```

Inside the JavaScript script, following functions have a predefined role:

  * `ksr_request_route()` - is executed by Kamailio core every time a SIP request is received. If this function is
  not defined, then Kamailio will write error messages. This is equivalent of `request_route {}` from `kamailio.cfg`.
  * `ksr_reply_route()` - is executed by Kamailio core every time a SIP Response (reply) is received. If this function
  is not defined, then Kamailio will not write error messages. This is equivalent of `reply_route {}`
  from `kamailio.cfg`.
  * `ksr_onsend_route()` - is executed by Kamailio core every time a SIP request (and optionally for a response) is
  sent out. If this function is not defined, then Kamailio will not write error messages. This is equivalent of
  `onsend_route {}` from `kamailio.cfg`.
  * `branch route callback` - the name of the JavaScript function to be executed instead of a branch route has to be
  provided as parameter to `KSR.tm.t_on_branch(…)`
  * `onreply route callback` - the name of the JavaScript function to be executed instead of an onreply route has to be
  provided as parameter to `KSR.tm.t_on_reply(…)`
  * `failure route callback` - the name of the JavaScript function to be executed instead of a failure route has to be
  provided as parameter to `KSR.tm.t_on_failure(…)`
  * `branch failure route callback` - the name of the JavaScript function to be executed instead of an `event route` for
  branch failure has to be provided as parameter to `KSR.tm.t_on_branch_failure(…)`
  * `event route callback` - the name of the JavaScript function to be executed instead of module specific
  `event_route` blocks is provided via `event_callback` parameter of that module

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
5.1, 5.2, 5.3, and 5.4.

```
loadmodule "app_lua.so"
modparam("app_lua", "load", "/path/to/script.lua")
cfgengine "lua"
```

Inside the Lua script, following functions have a predefined role:

  * `ksr_request_route()` - is executed by Kamailio core every time a SIP request is received. If this function is
  not defined, then Kamailio will write error messages. This is equivalent of `request_route {}` from `kamailio.cfg`.
  * `ksr_reply_route()` - is executed by Kamailio core every time a SIP Response (reply) is received. If this function
  is not defined, then Kamailio will not write error messages. This is equivalent of `reply_route {}`
  from `kamailio.cfg`.
  * `ksr_onsend_route()` - is executed by Kamailio core every time a SIP request (and optionally for a response) is
  sent out. If this function is not defined, then Kamailio will not write error messages. This is equivalent of
  `onsend_route {}` from `kamailio.cfg`.
  * `branch route callback` - the name of the Lua function to be executed instead of a branch route has to be
  provided as parameter to `KSR.tm.t_on_branch(…)`
  * `onreply route callback` - the name of the Lua function to be executed instead of an onreply route has to be
  provided as parameter to `KSR.tm.t_on_reply(…)`
  * `failure route callback` - the name of the Lua function to be executed instead of a failure route has to be
  provided as parameter to `KSR.tm.t_on_failure(…)`
  * `branch failure route callback` - the name of the Lua function to be executed instead of an `event route` for
  branch failure has to be provided as parameter to `KSR.tm.t_on_branch_failure(…)`
  * `event route callback` - the name of the Lua function to be executed instead of module specific
  `event_route` blocks is provided via `event_callback` parameter of that module

Note: besides the new KEMI Lua KSR module, the old `sr` Lua module exported by `app_lua` is still available.

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

#### Basic KEMI Lua Scripting Example ####

The file `kamailio.cfg` with global parameters and module settings:

```
#!KAMAILIO

####### Global Parameters #########

debug=3
log_stderror=yes
fork=yes
children=2

memdbg=5
memlog=5

auto_aliases=no

listen=udp:127.0.0.1:5060

loadmodule "jsonrpcs.so"
loadmodule "kex.so"
loadmodule "tm.so"
loadmodule "tmx.so"
loadmodule "sl.so"
loadmodule "pv.so"
loadmodule "maxfwd.so"
loadmodule "textops.so"
loadmodule "xlog.so"
loadmodule "ctl.so"
loadmodule "debugger.so"
loadmodule "app_lua.so"

# ----------------- setting module-specific parameters ---------------

# ----- jsonrpcs params -----
modparam("jsonrpcs", "pretty_format", 1)

# ----- tm params -----
# auto-discard branches from previous serial forking leg
modparam("tm", "failure_reply_mode", 3)
# default retransmission timeout: 30sec
modparam("tm", "fr_timer", 30000)
# default invite retransmission timeout after 1xx: 120sec
modparam("tm", "fr_inv_timer", 120000)

# ----- debugger params -----
modparam("debugger", "cfgtrace", 1)

####### Routing Logic ########

modparam("app_lua", "load", "/etc/kamailio/kamailio.lua")

cfgengine "lua"
```

The file `/etc/kamailio/kamailio.lua` with the routing logic for runtime:

```Lua
-- Kamailio - equivalent of routing blocks in Lua
-- KSR - the new dynamic object exporting Kamailio functions
-- sr - the old static object exporting Kamailio functions
--
-- SIP request routing
-- equivalent of request_route{}
function ksr_request_route()
	KSR.info("===== request - from kamailio lua script\n");

	if KSR.maxfwd.process_maxfwd(10) < 0 then
		KSR.sl.send_reply(483, "Too Many Hops");
		return;
	end

	-- KSR.sl.sreply(200, "OK Lua");

	KSR.pv.sets("$du", "sip:127.0.0.1:5080")
	KSR.tm.t_on_branch("ksr_branch_route_one");
	KSR.tm.t_on_reply("ksr_onreply_route_one");
	KSR.tm.t_on_failure("ksr_failure_route_one");

	if KSR.tm.t_relay() < 0 then
		KSR.sl.send_reply(500, "Server error")
	end
end

-- SIP response routing
-- equivalent of reply_route{}
function ksr_reply_route()
	KSR.info("===== response - from kamailio lua script\n");
end

-- branch route callback
-- equivalent of a branch_route{}
function ksr_branch_route_one()
	KSR.info("===== branch route - from kamailio lua script\n");
end

-- onreply route callback
-- equivalent of an onreply_route{}
function ksr_onreply_route_one()
	KSR.info("===== onreply route - from kamailio lua script\n");
end

-- failure route callback
-- equivalent of a failure_route{}
function ksr_failure_route_one()
	KSR.info("===== failure route - from kamailio lua script\n");
end
```

### Python KEMI Interpreter ###

Execution of KEMI Python scripts can be done by:

  * `app_python` - for Python versions 2.5, 2.6 and 2.7
  * `app_python3` - for Python versions 3.0+
  * `app_python3s` - for Python versions 3.0+ (available from Kamailio v5.7.0-dev)

The Python interpreter is linked from `libpython`.

```
loadmodule "app_python.so"
modparam("app_python", "script_name", "/path/to/script.py")
cfgengine "python"
```

For `app_python` and `app_python3`, in the Python script you have to declare the global `mod_init()` method
where to instantiate an object of a class that implements the other callback methods (functions)
to be executed by Kamailio.

Inside the new class, the following methods are relevant:

  * `ksr_request_route(self, msg)` - is executed by Kamailio core every time a SIP request is received. If this
  function is not defined, then Kamailio will write error messages. This is equivalent of `request_route {}` from
  `kamailio.cfg`.
  * `ksr_reply_route(self, msg)` - is executed by Kamailio core every time a SIP Response (reply) is received. If this
  function is not defined, then Kamailio will not write error messages. This is equivalent of `reply_route {}` from
  `kamailio.cfg`.
  * `ksr_onsend_route(self, msg)` - is executed by Kamailio core every time a SIP request (and optionally for a
  response) is sent out. If this function is not defined, then Kamailio will not write error messages. This is
  equivalent of `onsend_route {}` from `kamailio.cfg`.
  * `branch route callback` - the name of the Python function to be executed instead of a branch route has to be
  provided as parameter `to KSR.tm.t_on_branch(…)`
  * `onreply route callback` - the name of the Python function to be executed instead of an onreply route has to be
  provided as parameter to `KSR.tm.t_on_reply(…)`
  * `failure route callback` - the name of the Python function to be executed instead of a failure route has to be
  provided as parameter to `KSR.tm.t_on_failure(…)`
  * `branch failure route callback` - the name of the Python function to be executed instead of an event route for
  branch failure has to be provided as parameter to `KSR.tm.t_on_branch_failure(…)`
  * `event route callback` - the name of the Python function to be executed instead of module specific
  `event_route` blocks is provided via `event_callback` parameter of that module

Note: besides the new KEMI Python KSR module, the old `Router` Python module exported by `app_python` is still
available.

A more complete example of using Python as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-python.py](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-python.py)

For `app_python3s`:

  * [kamailio-basic-kemi-python3s.py](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-python3s.py)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGPYTHON
```

The file `kamailio-basic-kemi-python.py` has to be saved to local disk and the `load` parameter for
`app_python` module inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_python` is available at:

  * [app_python.html](https://kamailio.org/docs/modules/devel/modules/app_python.html)

The documentation for `app_python3` is available at:

  * [app_python3.html](https://kamailio.org/docs/modules/devel/modules/app_python3.html)

#### Basic KEMI Python Scripting Example For APP_PYTHON And APP_PYTHON3 ####

The file `kamailio.cfg` with the global parameters and modules settings:

```
#!KAMAILIO

####### Global Parameters #########

debug=4
log_stderror=yes
fork=yes
children=2

memdbg=5
memlog=5

auto_aliases=no

listen=udp:127.0.0.1:5060

loadmodule "jsonrpcs.so"
loadmodule "kex.so"
loadmodule "tm.so"
loadmodule "tmx.so"
loadmodule "sl.so"
loadmodule "pv.so"
loadmodule "maxfwd.so"
loadmodule "textops.so"
loadmodule "xlog.so"
loadmodule "ctl.so"
loadmodule "mi_rpc.so"
loadmodule "debugger.so"
loadmodule "app_python.so"

# ----------------- setting module-specific parameters ---------------

# ----- tm params -----
# auto-discard branches from previous serial forking leg
modparam("tm", "failure_reply_mode", 3)
# default retransmission timeout: 30sec
modparam("tm", "fr_timer", 30000)
# default invite retransmission timeout after 1xx: 120sec
modparam("tm", "fr_inv_timer", 120000)

# ----- debugger params -----
modparam("debugger", "cfgtrace", 1)

####### Routing Logic ########

modparam("app_python", "load", "/etc/kamailio/kamailio.py")

cfgengine "python"
```

The file `/etc/kamailio/kamailio.py` with the routing logic for runtime:

```Python
import sys
import KSR as KSR

def dumpObj(obj):
    for attr in dir(obj):
        KSR.info("obj.%s = %s\n" % (attr, getattr(obj, attr)))

def mod_init():
    KSR.info("===== from Python mod init\n")
    # dumpObj(KSR)
    return kamailio()

class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')

    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank)
        return 0

    def ksr_request_route(self, msg):
        KSR.info("===== request - from kamailio python script\n")
        KSR.setdsturi("sip:alice@127.0.0.1:5080")
        KSR.tm.t_on_branch("ksr_branch_route_one")
        KSR.tm.t_on_reply("ksr_onreply_route_one")
        KSR.tm.t_on_failure("ksr_failure_route_one")
        KSR.sl.send_reply(100, "Trying")
        if KSR.tm.t_relay() < 0 :
            KSR.sl.send_reply(500, "Server error")
        return 1

    def ksr_reply_route(self, msg):
        KSR.info("===== response - from kamailio python script\n")
        return 1

    def ksr_onsend_route(self, msg):
        KSR.info("===== onsend route - from kamailio python script\n")
        return 1

    def ksr_branch_route_one(self, msg):
        KSR.info("===== branch route - from kamailio python script\n")
        return 1

    def ksr_onreply_route_one(self, msg):
        KSR.info("===== onreply route - from kamailio python script\n")
        return 1

    def ksr_failure_route_one(self, msg):
        KSR.info("===== failure route - from kamailio python script\n")
        return 1
```

#### KEMI Python Scripting Example For APP_PYTHON3S ####

The `app_python3s` is an alternative of `app_python3` which is not instantiating
the dynamic SIP message object, it only exports the static `KSR` module. That
means that no class has to be defined, the KEMI script functions are no longer
associated with an object, making it more similar to `app_lua` or `app_jsdt`.

The KEMI callback functions `ksr_request_route()`, `ksr_reply_route()` and
`ksr_onsend_route()` have to be simply defined in the Python3 script, they have
no parameter, like:

```python
# SIP request routing
# -- equivalent of request_route{}
def ksr_request_route():
    ...
    ksr_route_natdetect():
    ...


# Caller NAT detection
def ksr_route_natdetect():
    KSR.force_rport()
    if KSR.nathelper.nat_uac_test(19)>0 :
        if KSR.is_REGISTER() :
            KSR.nathelper.fix_nated_register()
        elif KSR.siputils.is_first_hop()>0 :
            KSR.nathelper.set_contact_alias()

        KSR.setflag(FLT_NATS)

    return 1


# SIP response handling
# -- equivalent of reply_route{}
def ksr_reply_route():
    KSR.dbg("response handling - python script\n")

    if KSR.sanity.sanity_check(17604, 6)<0 :
        KSR.err("Malformed SIP response from "
                + KSR.pv.get("$si") + ":" + str(KSR.pv.get("$sp")) +"\n")
        KSR.set_drop()
        return -255

    return 1

```

### Ruby KEMI Interpreter ###

It is implemented by `app_ruby` module. The module requires libruby-dev in order
to be compiled. The module was initially tested with libruby-2.3 and libruby-2.5.

```
loadmodule "app_ruby.so"
modparam("app_ruby", "load", "/path/to/script.rb")
cfgengine "ruby"
```

The documentation for `app_ruby` is available at:

  * [app_ruby.html](https://kamailio.org/docs/modules/devel/modules/app_ruby.html)

### Squirrel KEMI Interpreter ###

**IMPORTANT: this module has been archived, it is no longer in the main git repository.**

It is implemented by `app_sqlang` module. The Squirrel language interpreter is imported inside the module from
[Squirrel](http://www.squirrel-lang.org) project, therefore it doesn't require to install any external libraries.

```
loadmodule "app_sqlang.so"
modparam("app_sqlang", "load", "/path/to/script.sq")
cfgengine "sqlang"
```

A complete example of using Squirrel as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-sqlang.sq](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-sqlang.sq)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGSQLANG
```

The file `kamailio-basic-kemi-sqlang.sq` has to be saved to local disk and the `load` parameter for `app_sqlang`
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

If a function has `void` as return type in the signature, then it doesn't return any value.

Several functions may return a string or `xval` value, for example in the `KSR.pv` submodule to get the value of pseudo-variables. If a function returns `xval`, then the result value can be `string`, `integer` or `null`.

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
kamctl rpc app_python3.api_list
kamctl rpc app_ruby.api_list
kamctl rpc app_sqlang.api_list
```

### Functions Returning 0 ###

The functions exported by Kamailio via KSR submodules that return 0 were designed to stop the execution of the
routing script. That is done automatically in the native scripting language, but in KEMI scripting languages
requires additional steps to terminate the script execution for that SIP message -- typically means evaluation
of the return code and if it is 0, then execute KSR.x.exit() or the equivalent in that scripting language.

There are only a few functions returning 0, this section tries to collect them for convenience:

  * `tm` module
    * `t_check_trans()`
    * `t_newtran()`
  * websocket module
    * `ws_handshake()`

Example handling `t_check_trans()` for 0 return code in Lua script:

```
...
-- SIP request routing
-- equivalent of request_route{}
function ksr_request_route()
    ...
    if KSR.tm.t_check_trans()==0 then
        KSR.x.exit();
    end
    ...
end
...

```

Note: these functions can also return negative or positive values, those cases have to be handled as well.

## Exporting C Function To KEMI Interpreters ##

Because Kamailio needs to load modules in order to export useful functions to KEMI, statical wrappers to C functions
implemented in other modules cannot be used, because they will introduce dependencies on each embedded interpreter
for all modules.

The implementation relies on defining a set of generic functions that are exported to each embedded interpreter, which
are associated at startup with a Kamailio C functions. The lookup at runtime is by an integer index, therefore very
fast.

Currently the association table size is 1024 (it means that there can be maximum 1024 Kamailio C functions exported
to the interpreter by a configuration file). The number can be increased, but it should be fairly enough as all
`kamailio.cfg` functions are around 1000 and it is no real use case to load all the modules at the same time for use
in production. Also, many functions may not be exported to an embedded language, as they have native alternative in
the embedded language.

Each existing component of Kamailio (e.g., module), can export new functions to KEMI in the following way:

  * declare an array of type sr_kemi_t
  * register it to KEMI in mod_register() function (or at startup for core components) using sr_kemi_modules_add()

The structure `sr_kemi_t` is declared in Kamailio core, the file `kemi.h`:

```C
#define SR_KEMI_PARAMS_MAX	6

typedef struct sr_kemi {
	str mname; /* sub-module name */
	str fname; /* function name */
	int rtype; /* return type (supported SR_KEMIP_INT, SR_KEMIP_BOOL, SR_KEMIP_XVAL) */
	void *func; /* pointer to the C function to be executed */
	int ptypes[SR_KEMI_PARAMS_MAX]; /* array with the type of parameters */
} sr_kemi_t;
```

Next C code snippet shows how sl module exports two functions:

  * C function `sl_send_reply_str(…)` is exported as `sl.sreply(…)`
  * C function `send_reply(…)` is exported as `sl.freply(…)`

```C
static sr_kemi_t sl_kemi_exports[] = {
	{ str_init("sl"), str_init("sreply"),
		SR_KEMIP_INT, sl_send_reply_str,
		{ SR_KEMIP_INT, SR_KEMIP_STR, SR_KEMIP_NONE,
			SR_KEMIP_NONE, SR_KEMIP_NONE, SR_KEMIP_NONE }
	},
	{ str_init("sl"), str_init("freply"),
		SR_KEMIP_INT, send_reply,
		{ SR_KEMIP_INT, SR_KEMIP_STR, SR_KEMIP_NONE,
			SR_KEMIP_NONE, SR_KEMIP_NONE, SR_KEMIP_NONE }
	},

	{ {0, 0}, {0, 0}, 0, NULL, { 0, 0, 0, 0, 0, 0 } }
};

int mod_register(char *path, int *dlflags, void *p1, void *p2)
{
	sr_kemi_modules_add(sl_kemi_exports);
	return 0;
}
```

Note that the exported array is ended by a sentinel of `0`/`NULL` values for all fields.

Exported functions must take first parameter as `sip_msg_t*` type (which is the structure with the SIP message being
processed), then followed by up to 6 `int` or `str*` parameters. When `SR_KEMIP_NONE` is given in the array with the types
of parameters, it means there is no parameter from there on (some compilers may rise warning, so it is recommended
to fill all 6 items in array).

The functions exported by Kamailio core are listed inside the array `_sr_kemi_core` from the file `kemi.c`.

Not all combinations of extra (after `sip_msg_t*`) parameters types are supported right now - currently the are:

  * `1 param` - can be `int` of `str*`
  * `2 params` - any combination of `int` or `str*`
  * `3 params` - any combination of `int` or `str*`
  * `4 params` - any combination of `int` or `str*`
  * `5 params` - any combination of `int` or `str*`
  * `6 params` - all have to be `str*` (other combinations to be added as needed)

The return type can be:

  * `SR_KEMIP_INT` - returned value is integer and has to be evaluated with the
  following rules:
    * if less than 0 - it was an error of processing or equivalent
    of false in the native scripting language;
    * if greater than 0 - it was a successful processing or equivalent of true in the
    native scripting language;
    * if equal to 0 - stop execution of the routing script (done by a few functions
    such as `KSR.tm.t_check_trans(...)`)
    * exceptions to the above rules are the getter functions that return the
    integer value of some attribute (e.g., `KSR.kx.get_status()`, `KSR.kx.get_timestamp()`)
  * `SR_KEMIP_BOOL` - returned value can be evaluated in the routing script as
  TRUE or FALSE. In the C code it has to return 1 for TRUE or 0 for FALSE.
  * `SR_KEMIP_XVAL` - returned value depends on the context, can be either
  integer or string value. For example it is used for the functions that return
  the value of pseudo-variables KSR.pv.get(...). This return type is supported
  only for exported functions that have up to 2 parameters.


## KEMI And Pseudo-Variables ##

Kamailio-specific pseudo-variables can be managed using functions exposed by
`KSR.pv` module. The `KSR.pv` is exported by Kamailio core or by KEMI interpreter
module and should be available in the KEMI scripting language automatically, no
additional Kamailio module needs to be loaded. Of course, availability of
specific variables is still a matter of loading the module implementing them
(e.g., availability of `$T(..)` requires loading `tmx` module).

Because the pseduo-variables were designed for Kamailio native configuration
file scripting language, there are a few constraints and limitations as well as
recommendations to be aware of, listed in the next sections.

### Constraint Of PV Static Names ###

In many situations the pseudo-variables expect static names, which was ensured
by parsing `kamailio.cfg` at startup. However that cannot be ensured by using
KEMI scripts, Kamailio having no control to the implementation of the scripting
language interpreter, the effect can be that it is possible to define a lot of
pseudo-variables, which can lead to filling the private memory of Kamailio.

For example, using `htable` module in native `kamailio.cfg`, one defines the
hash table `test` via `modparam` and in the script uses variables such as
`$sht(test=>x)` to access the value of the item with the key `x`, or uses
`$sht(test=>$rU)` to access the value of the item with the key being the R-URI
username of currently processed SIP request. In such case, two pseudo-variable
structures are defined by Kamailio at startup, corresponding to `$sht(test=>x)`
and `$sht(test=>$rU)`.

When using KEMI scripting, accessing `$sht(test=>x)` with `KSR.pv.get("$sht(test=>x)")`
and `$sht(test=>$rU)` with `KSR.pv.get("$sht(test=>$rU)")` is ok, because still
two pseudo-variable identifiers are used.

However, someone may try to access the `$sht(test=>$rU)` via
`KSR.pv.get("$sht(test=>" .. KSR.kx.get_ruser() .. ")")` (example in Lua), then
it leads of defining internally to Kamailio a lot of variables, corresponding to
each different R-URI username processed. Say, there were three requests with
R-URI usernames `alice`, `bob` and `carol`, Kamailio has defined internally
three pseudo-variable structures corresponding to `$sht(test=>alice)`, `$sht(test=>bob)`
and `$sht(test=>carol)`.

There are couple of mechanisms trying to cope with this situation, especially for
hash table, including availability of dedicated functions to access hash table
items, or trying to clean up some of the pseudo-variable structures. But they
are not available for all the modules that exposes same risks, such as
`sqlops`, `ndb_redis` or `ndb_mongodb`. Therefore try to avoid using
pseudo-variables with dynamic name.

For example, in the next snippet a single pseudo-variable structure is used
for accessing three hash table items, by leveraging `$var(x)` inside `$sht(...)`
name:

```Lua
KSR.pvx.var_sets("x", "alice");
shtx = KSR.pv_get("$sht(test=>$var(x))");
KSR.pvx.var_sets("x", "bob");
shtx = KSR.pv_get("$sht(test=>$var(x))");
KSR.pvx.var_sets("x", "carol");
shtx = KSR.pv_get("$sht(test=>$var(x))");
```

Note that for the modules that return results of SQL or noSQL queries, the result
id can be reused. The values of result containers are stored in private memory
and it is safe to use them in different Kamailio worker processes.

### Functions For Specific Pseudo-Variables ###

The package `KSR.kx` exported by `kemix` module offers a consistent set of
functions to get or set values specific for various pseudo-variables, especially
for attributes of the SIP message such as From-URI, From-URI-username, etc.

The package `KSR.pvx` exported by `pv` module offers convenience functions
to work with private-memory (`$var(...)`) or shared memory (`$shv(...)`)
pseudo-variables as well as XAVPs variants.

For example:

```Lua
KSR.pv.sets("$var(x)", "alice");
```

is the same as:

```Lua
KSR.pvx.var_sets("x", "alice");
```

the second variant being recommended to be used.

The package `KSR.sqlops` exported by `sqlops` module offers convenience functions
to access the SQL result instead of using `$dbr(...)`.

For example:

```Lua
KSR.sqlops.sql_query("ca", "select username from subscriber limit 1", "ra");
if KSR.pv.get("$dbr(ra=>rows)") > 0 then
  local username = KSR.pv.get("$dbr(ra=>[0,0])");
end
```

is the same as:

```Lua
KSR.sqlops.sql_query("ca", "select username from subscriber limit 1", "ra");
if KSR.sqlops.sql_num_rows("ra") > 0 then
  local username = KSR.sqlops.sql_result_get("ra", 0, 0);
end
```

the second variant being recommended to be used.

It is recommended to look at the functions exported to KEMI by each Kamailio
module used in the script, there can be useful functions that could be convenient
to use instead of the pseudo-variables exported by that module.
