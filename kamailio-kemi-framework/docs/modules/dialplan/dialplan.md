# dialplan #

* 📖[kamailio.cfg::module::dialplan.html](https://kamailio.org/docs/modules/devel/modules/dialplan.html)

Exported functions:

* [KSR.dialplan.dp_match\(\)](#ksrdialplandp_match)
* [KSR.dialplan.dp_replace\(\)](#ksrdialplandp_replace)
* [KSR.dialplan.dp_translate\(\)](#ksrdialplandp_translate)
* [KSR.dialplan.dp_translate_vars\(\)](#ksrdialplandp_translate_vars)

## KSR.dialplan.dp_match ##

```cpp
int KSR.dialplan.dp_match(int dpid, str "src");
```

* 📖[kamailio.cfg::function::dp_match\(\)](https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_match)

## KSR.dialplan.dp_replace ##

```cpp
int KSR.dialplan.dp_replace(int dpid, str "src", str "dst");
```

* 📖[kamailio.cfg::function::dp_replace\(\)](https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_replace)

## KSR.dialplan.dp_translate ##

```cpp
int KSR.dialplan.dp_translate(int id);
```

* 📖[kamailio.cfg::function::dp_translate\(\)](https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_translate)

## KSR.dialplan.dp_translate_vars ##

```cpp
int KSR.dialplan.dp_translate_vars(int id, str "input", str "output");
```

* 📖[kamailio.cfg::function::dp_translate_vars\(\)](https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_translate_vars)
