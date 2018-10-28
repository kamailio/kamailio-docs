## KEMI Interpreters ##

The following KEMI scripting languages can be used to write SIP routing logic for Kamailio:

  * JavaScript
  * Lua
  * Python
  * Python3
  * Ruby
  * Squirrel

A configuration file for Kamailio that uses a KEMI scripting language has the glabal parameters, loading modules and
module parameters in the native scripting and sets the value of `cfgengine` to the KEMI scripting language identifier.

The KEMI scripting language identifiers are:

  * `jsdt` - for JavaScript
  * `lua` - for Lua
  * `python` - for Python
  * `python3` - for Python3
  * `ruby` - for Ruby
  * `sqlang` - for Squirrel

### JavaScript KEMI Interpreter ###

It is implemented by `app_jsdt` module. The JavaScript interpreter is imported inside the module from
[DukTape](www.ducktape.org) project, therefore it doesn't require to install any external libraries.

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
  * `event route callback` - the name of the JavaScript function to be exectued instead of module specific
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
5.1 and 5.2.

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
  * `event route callback` - the name of the Lua function to be exectued instead of module specific
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

It is implemented by `app_python` module. The Python interpreter is linked from `libpython`, supported Python versions:
2.5, 2.6 and 3.x (via app_python3).

```
loadmodule "app_python.so"
modparam("app_python", "script_name", "/path/to/script.py")
cfgengine "python"
```

In the Python script you have to declare the global `mod_init()` method where to instantiate an object of a class that
implements the other callback methods (functions) to be executed by Kamailio.

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
  * `event route callback` - the name of the Python function to be exectued instead of module specific
  `event_route` blocks is provided via `event_callback` parameter of that module

Note: besides the new KEMI Python KSR module, the old `Router` Python module exported by `app_python` is still
available.

A complete example of using Python as KEMI languages is offered by the next two files:

  * [kamailio-basic-kemi.cfg](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi.cfg)
  * [kamailio-basic-kemi-python.py](https://github.com/kamailio/kamailio/blob/master/misc/examples/kemi/kamailio-basic-kemi-python.py)

The file `kamailio-basic-kemi.cfg` has to be saved as `kamailio.cfg` and inside it add after the first line:

```
#!define WITH_CFGPYTHON
```

The file `kamailio-basic-kemi-python.py` has to be saved to local disk and the `load` parameter for
`app_python` module inside `kamailio.cfg` has to be updated to point to it. Then run `kamailio` with this `kamailio.cfg`.

The documentation for `app_python` is available at:

  * [app_python.html](https://kamailio.org/docs/modules/devel/modules/app_python.html)

#### Basic KEMI Python Scripting Example ####

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
import Router.Logger as Logger
import KSR as KSR

def dumpObj(obj):
    for attr in dir(obj):
        # KSR.info("obj.%s = %s\n" % (attr, getattr(obj, attr)));
        Logger.LM_INFO("obj.%s = %s\n" % (attr, getattr(obj, attr)));

def mod_init():
    KSR.info("===== from Python mod init\n");
    # dumpObj(KSR);
    return kamailio();

class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')

    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank)
        return 0

    def ksr_request_route(self, msg):
        KSR.info("===== request - from kamailio python script\n");
        msg.rewrite_ruri("sip:alice@127.0.0.1:5080");
        KSR.tm.t_on_branch("ksr_branch_route_one");
        KSR.tm.t_on_reply("ksr_onreply_route_one");
        KSR.tm.t_on_failure("ksr_failure_route_one");
        KSR.sl.send_reply(100, "Trying")
        if KSR.tm.t_relay() < 0 :
            KSR.sl.send_reply(500, "Server error")
        return 1;

    def ksr_reply_route(self, msg):
        KSR.info("===== response - from kamailio python script\n");
        return 1;

    def ksr_branch_route_one(self, msg):
        KSR.info("===== branch route - from kamailio python script\n");
        return 1;

    def ksr_onreply_route_one(self, msg):
        KSR.info("===== onreply route - from kamailio python script\n");
        return 1;

    def ksr_failure_route_one(self, msg):
        KSR.info("===== failure route - from kamailio python script\n");
        return 1;
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

If a function has `void` as return type in the signature, the it doesn't return any value.

Few functions may return a string value, for example in the `KSR.pv` submodule to get the value of pseudo-variables.

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
	int rtype; /* return type (supported SR_KEMIP_INT/BOOL) */
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
processed), then followed by up to 6 int or str* parameters. When `SR_KEMIP_NONE` is given in the array with the types
of parameters, it means there is no parameter from there on (some compilers may rise warning, so it is recommended
to fill all 6 items in array).

The functions exported by Kamailio core are listed inside the array `_sr_kemi_core` from the file `kemi.c`.

Not all combinations of extra (after `sip_msg_t*`) parameters types are supported right now - currently the are:

  * `1 param` - can be `int` of `str*`
  * `2 params` - any combination of `int` or `str*`
  * `3 params` - any combination of `int` or `str*`
  * `4 params` - all have to be `str*` (other combinations to be added as needed)
  * `5 params` - all have to be `str*` (other combinations to be added as needed)
  * `6 params` - all have to be `str*` (other combinations to be added as needed)

