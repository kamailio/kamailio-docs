# Kamailio Kemi Framework #

```
Author: Daniel-Constantin Mierla (miconda@gmail.com)
```

## Introduction ##

Kamailio uses a scripting laguage for its configuration file (kamailio.cfg). This scripting language (referred also as
native scripting language) was developed from scratch, with initial design going back to years 2001-2002.

The configuration file is composed from several main statements:

  * global parameters
  * loading modules
  * module parameters
  * routing blocks

In terms of execution, kamailio.cfg interprets only once, at startup, the statements related to:

  * global parameters
  * loading modules
  * module parameters

The routing blocks are similar to functions and can be executed many times, some of them for each received
SIP message, some of them on various events fired by core or modules.

While the native scripting language offers a large set of functions and is able to do many logical, arithmetic
and string operations, its limits are met in many cases, especially when in need to integrate with external systems.

Another missing feature in the native scripting language is reloading without a restart.

Kamailio Embedded Interface (KEMI) framework was added first in Kamailio v5.0.0 to allow using other scripting
languages to write SIP routing logic instead of using the native routing blocks. The interpreters for these scripting
languages are embedded by Kamailio, initialized at startup, in this way being also as fast as poosible during runtime
execution.