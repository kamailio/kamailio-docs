# Kamailio KEMI Framework #

```
Author: Daniel-Constantin Mierla (miconda@gmail.com)

Contributors: Samuel Förnes

Support: <sr-users@lists.kamailio.org>
```

## Introduction ##

### Preamble ###

`Kamailio` uses a scripting laguage for its configuration file (`kamailio.cfg`). This scripting language (referred also
as native scripting language) was developed from scratch, with initial design going back to years 2001-2002.

The configuration file is composed from several main statements:

  * global parameters
  * loading modules
  * module parameters
  * routing blocks (e.g., `request_route {...}`, `reply_route {...}`, `branch_route {...}`, ...)

In terms of execution, the `kamailio.cfg` interpreter runs only once (at startup) the statements related to:

  * global parameters
  * loading modules
  * module parameters
  * initialization event routes (e.g., `event_route[htable:mod-init] {...}`)

At runtime, the `kamailio.cfg` interpreter can run many times:

  * routing blocks  (e.g., `request_route {...}`, `reply_route {...}`, `branch_route {...}`, ...)

The routing blocks are similar to functions and can be executed many times, some of them for each received
SIP message, some of them on various events fired by core or modules.

While the native scripting language offers a large set of functions and is able to do many logical, arithmetic
and string operations, its limits are met in some cases, especially when in need to integrate with external systems.

Another missing feature in the native scripting language is reloading without a restart. The interpreter was designed
to precompile `kamailio.cfg` at startup, doing specific optimization for fast runtime operations. Adding support for
reload will result in losing those optimizations and doing checks to see if the execution script needs to be parsed
again.

The solution to meet the demands of having a more flexible and feature-rich scripting language, with the possibility
of reloading the routing script without restart, as well keeping the old native interpreter, was to develop a new
framework for executing SIP routing scripts written in other programming languages. It was named
`Kamailio Embedded Interface` (`KEMI`) framework.

### KEMI Overview ###

`Kamailio Embedded Interface` (`KEMI`) framework was added first in `Kamailio v5.0.0` to allow using other scripting
languages to write SIP routing logic instead of using the native routing blocks. The interpreters for these scripting
languages are embedded by Kamailio, initialized at startup, in this way being also as fast as possible during runtime
execution.

With KEMI routing script, the `kamailio.cfg` keeps only the parts with:

  * global parameters
  * loading modules
  * modules settings

All of these parts are evaluated only once at startup. Many of the global and module parameters can be changed at
runtime via `RPC` commands. Few `event_route` blocks that are executed during start up may have to be defined
inside `kamailio.cfg`, they are executed only once, not being used for SIP routing.

The KEMI comes in the picture by allowing the equivalent of routing blocks to be written in a different scripting
language. In other words, the routing blocks are now functions written in a KEMI supported scripting language.

For each new KEMI supported scripting language a module has to be developed for Kamailio, this module linking
Kamailio to the scripting language interpreter.

At this moment there are couple of supported KEMI scripting languages, respectively `JavaScript`
(`app_jsdt`), `Lua` (`app_lua`), `Python` (`app_python`), `Python3` (`app_python3`), `Ruby` (`app_ruby`),
`Squirrel` (`app_sqlang`) -- see next sections for more details about these programming languages.

Note: Kamailio has other modules that allow inline execution of scripts written in other programming languages, such
as `Perl` (`app_perl`), `.Net` (`C#`, etc.) (`app_mono`), `Java` (`app_java`), but they don't implement the KEMI yet,
likely that some of them will get support in the near future.

The main benefits of using KEMI framework:

  * reload of SIP routing scripts without restart of Kamailio
  * better documentation knowledge base for supported scripting languages
  * more complete and flexible scripting languages
  * larger set of libraries that can be used from the scripting languages
  * external tools to troubleshoot or test the scripts
