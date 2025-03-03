<!-- This file is auto-generated. Any manual modifications will be deleted -->
# KEMI Module Functions #

The following sections list all exported KEMI functions. More information regarding
a function can be found by clicking the KEMI prototype, which will take you to
the original module's documentation.

Because the native `kamailio.cfg` scripting language allows variadic functions,
but exports to KEMI are functions with fixed number of parameters, there can
be a group of KEMI functions to offer the capabilities of a single `kamailio.cfg`
function. In such case, the KEMI functions share a common naming prefix, usually
the name of the `kamailio.cfg` function.

For example, the `kamailio.cfg` function `ds_is_from_list(...)` from `dispatcher`
module has the prototype:

```c
int ds_is_from_list([groupid [, mode [, uri] ] ])
```

And the corresponding KEMI exports are:

```c
int KSR.dispatcher.ds_is_from_lists();
int KSR.dispatcher.ds_is_from_list(int groupid);
int KSR.dispatcher.ds_is_from_list_mode(int groupid, int mode);
int KSR.dispatcher.ds_is_from_list_uri(int groupid, int mode, str "uri");
```