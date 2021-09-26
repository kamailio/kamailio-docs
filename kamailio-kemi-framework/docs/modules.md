<!-- This file is auto-generated. Any manual modifications will be deleted -->
# KEMI Module Functions #
The following sections lists all exported KEMI functions. More information regarding the function can be found by clicking the KEMI prototype which will take you the original module's documentation.

## acc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html'>📖 kamailio.cfg::module::acc.html</a>

The functions exported by `acc` module to KEMI are listed in the next sections.

The documentation of `acc` module is available online at:

  * [acc.html](https://kamailio.org/docs/modules/devel/modules/acc.html)

#### KSR.acc.acc_db_request() ####

```cpp
int KSR.acc.acc_db_request(str "comment", str "dbtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_db_request'>📖 kamailio.cfg::function::acc_db_request()</a>

Equivalent of native kamailio.cfg function: `acc_db_request("comment", "dbtable")`.

#### KSR.acc.acc_log_request() ####

```cpp
int KSR.acc.acc_log_request(str "comment");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_log_request'>📖 kamailio.cfg::function::acc_log_request()</a>

Equivalent of native kamailio.cfg function: `acc_log_request("comment")`.

#### KSR.acc.acc_request() ####

```cpp
int KSR.acc.acc_request(str "comment", str "dbtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_request'>📖 kamailio.cfg::function::acc_request()</a>

Equivalent of native kamailio.cfg function: `acc_request("comment", "dbtable")`.

## acc_radius ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc_radius.html'>📖 kamailio.cfg::module::acc_radius.html</a>

#### KSR.acc_radius.request() ####

```cpp
int KSR.acc_radius.request(str "comment");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc_radius.html#acc_radius.f.request'>📖 kamailio.cfg::function::request()</a>

## alias_db ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/alias_db.html'>📖 kamailio.cfg::module::alias_db.html</a>

#### KSR.alias_db.lookup() ####

```cpp
int KSR.alias_db.lookup(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/alias_db.html#alias_db.f.alias_db_lookup'>📖 kamailio.cfg::function::alias_db_lookup()</a>

#### KSR.alias_db.lookup_ex() ####

```cpp
int KSR.alias_db.lookup_ex(str "stable", str "sflags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/alias_db.html#alias_db.f.alias_db_lookup'>📖 kamailio.cfg::function::alias_db_lookup()</a>

## app_jsdt ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html'>📖 kamailio.cfg::module::app_jsdt.html</a>

#### KSR.app_jsdt.dofile() ####

```cpp
int KSR.app_jsdt.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.jsdt_dofile'>📖 kamailio.cfg::function::jsdt_dofile()</a>

#### KSR.app_jsdt.dostring() ####

```cpp
int KSR.app_jsdt.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.jsdt_dostring'>📖 kamailio.cfg::function::jsdt_dostring()</a>

#### KSR.app_jsdt.run() ####

```cpp
int KSR.app_jsdt.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.jsdt_run'>📖 kamailio.cfg::function::jsdt_run()</a>

#### KSR.app_jsdt.run_p1() ####

```cpp
int KSR.app_jsdt.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p1'>📖 kamailio.cfg::function::run_p1()</a>

#### KSR.app_jsdt.run_p2() ####

```cpp
int KSR.app_jsdt.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p2'>📖 kamailio.cfg::function::run_p2()</a>

#### KSR.app_jsdt.run_p3() ####

```cpp
int KSR.app_jsdt.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p3'>📖 kamailio.cfg::function::run_p3()</a>

#### KSR.app_jsdt.runstring() ####

```cpp
int KSR.app_jsdt.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.runstring'>📖 kamailio.cfg::function::runstring()</a>

## app_lua ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html'>📖 kamailio.cfg::module::app_lua.html</a>

#### KSR.app_lua.dofile() ####

```cpp
int KSR.app_lua.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.dofile'>📖 kamailio.cfg::function::dofile()</a>

#### KSR.app_lua.dostring() ####

```cpp
int KSR.app_lua.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.dostring'>📖 kamailio.cfg::function::dostring()</a>

#### KSR.app_lua.run() ####

```cpp
int KSR.app_lua.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run'>📖 kamailio.cfg::function::run()</a>

#### KSR.app_lua.run_p1() ####

```cpp
int KSR.app_lua.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p1'>📖 kamailio.cfg::function::run_p1()</a>

#### KSR.app_lua.run_p2() ####

```cpp
int KSR.app_lua.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p2'>📖 kamailio.cfg::function::run_p2()</a>

#### KSR.app_lua.run_p3() ####

```cpp
int KSR.app_lua.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p3'>📖 kamailio.cfg::function::run_p3()</a>

#### KSR.app_lua.runstring() ####

```cpp
int KSR.app_lua.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.runstring'>📖 kamailio.cfg::function::runstring()</a>

## app_python ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html'>📖 kamailio.cfg::module::app_python.html</a>

#### KSR.app_python.exec() ####

```cpp
int KSR.app_python.exec(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.exec'>📖 kamailio.cfg::function::exec()</a>

#### KSR.app_python.exec_p1() ####

```cpp
int KSR.app_python.exec_p1(str "method", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.exec_p1'>📖 kamailio.cfg::function::exec_p1()</a>

#### KSR.app_python.execx() ####

```cpp
int KSR.app_python.execx(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.execx'>📖 kamailio.cfg::function::execx()</a>

## app_python3 ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html'>📖 kamailio.cfg::module::app_python3.html</a>

#### KSR.app_python3.exec() ####

```cpp
int KSR.app_python3.exec(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.exec'>📖 kamailio.cfg::function::exec()</a>

#### KSR.app_python3.exec_p1() ####

```cpp
int KSR.app_python3.exec_p1(str "method", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.exec_p1'>📖 kamailio.cfg::function::exec_p1()</a>

#### KSR.app_python3.execx() ####

```cpp
int KSR.app_python3.execx(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.execx'>📖 kamailio.cfg::function::execx()</a>

## app_ruby ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html'>📖 kamailio.cfg::module::app_ruby.html</a>

#### KSR.app_ruby.run() ####

```cpp
int KSR.app_ruby.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run'>📖 kamailio.cfg::function::run()</a>

#### KSR.app_ruby.run_p1() ####

```cpp
int KSR.app_ruby.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p1'>📖 kamailio.cfg::function::run_p1()</a>

#### KSR.app_ruby.run_p2() ####

```cpp
int KSR.app_ruby.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p2'>📖 kamailio.cfg::function::run_p2()</a>

#### KSR.app_ruby.run_p3() ####

```cpp
int KSR.app_ruby.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p3'>📖 kamailio.cfg::function::run_p3()</a>

## app_sqlang ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html'>📖 kamailio.cfg::module::app_sqlang.html</a>

#### KSR.app_sqlang.dofile() ####

```cpp
int KSR.app_sqlang.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dofile'>📖 kamailio.cfg::function::dofile()</a>

#### KSR.app_sqlang.dostring() ####

```cpp
int KSR.app_sqlang.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dostring'>📖 kamailio.cfg::function::dostring()</a>

#### KSR.app_sqlang.run() ####

```cpp
int KSR.app_sqlang.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run'>📖 kamailio.cfg::function::run()</a>

#### KSR.app_sqlang.run_p1() ####

```cpp
int KSR.app_sqlang.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p1'>📖 kamailio.cfg::function::run_p1()</a>

#### KSR.app_sqlang.run_p2() ####

```cpp
int KSR.app_sqlang.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p2'>📖 kamailio.cfg::function::run_p2()</a>

#### KSR.app_sqlang.run_p3() ####

```cpp
int KSR.app_sqlang.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p3'>📖 kamailio.cfg::function::run_p3()</a>

#### KSR.app_sqlang.runstring() ####

```cpp
int KSR.app_sqlang.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.runstring'>📖 kamailio.cfg::function::runstring()</a>

## async ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html'>📖 kamailio.cfg::module::async.html</a>

#### KSR.async.ms_route() ####

```cpp
int KSR.async.ms_route(str "rn", int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.ms_route'>📖 kamailio.cfg::function::ms_route()</a>

#### KSR.async.route() ####

```cpp
int KSR.async.route(str "rn", int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.route'>📖 kamailio.cfg::function::route()</a>

#### KSR.async.task_route() ####

```cpp
int KSR.async.task_route(str "rn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_route'>📖 kamailio.cfg::function::task_route()</a>

## auth ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html'>📖 kamailio.cfg::module::auth.html</a>

#### KSR.auth.auth_challenge() ####

```cpp
int KSR.auth.auth_challenge(str "realm", int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.auth_challenge'>📖 kamailio.cfg::function::auth_challenge()</a>

#### KSR.auth.consume_credentials() ####

```cpp
int KSR.auth.consume_credentials();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.consume_credentials'>📖 kamailio.cfg::function::consume_credentials()</a>

#### KSR.auth.has_credentials() ####

```cpp
int KSR.auth.has_credentials(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.has_credentials'>📖 kamailio.cfg::function::has_credentials()</a>

#### KSR.auth.pv_auth_check() ####

```cpp
int KSR.auth.pv_auth_check(str "srealm", str "spasswd", int vflags, int vchecks);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_auth_check'>📖 kamailio.cfg::function::pv_auth_check()</a>

## auth_db ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_db.html'>📖 kamailio.cfg::module::auth_db.html</a>

#### KSR.auth_db.auth_check() ####

```cpp
int KSR.auth_db.auth_check(str "srealm", str "stable", int iflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.auth_check'>📖 kamailio.cfg::function::auth_check()</a>

#### KSR.auth_db.is_subscriber() ####

```cpp
int KSR.auth_db.is_subscriber(str "suri", str "stable", int iflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.is_subscriber'>📖 kamailio.cfg::function::is_subscriber()</a>

## auth_ephemeral ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html'>📖 kamailio.cfg::module::auth_ephemeral.html</a>

#### KSR.auth_ephemeral.autheph_authenticate() ####

```cpp
int KSR.auth_ephemeral.autheph_authenticate(str "susername", str "spassword");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_authenticate'>📖 kamailio.cfg::function::autheph_authenticate()</a>

#### KSR.auth_ephemeral.autheph_check() ####

```cpp
int KSR.auth_ephemeral.autheph_check(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_check'>📖 kamailio.cfg::function::autheph_check()</a>

#### KSR.auth_ephemeral.autheph_proxy() ####

```cpp
int KSR.auth_ephemeral.autheph_proxy(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_proxy'>📖 kamailio.cfg::function::autheph_proxy()</a>

#### KSR.auth_ephemeral.autheph_www() ####

```cpp
int KSR.auth_ephemeral.autheph_www(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www'>📖 kamailio.cfg::function::autheph_www()</a>

#### KSR.auth_ephemeral.autheph_www_method() ####

```cpp
int KSR.auth_ephemeral.autheph_www_method(str "srealm", str "smethod");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www_method'>📖 kamailio.cfg::function::autheph_www_method()</a>

## auth_radius ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html'>📖 kamailio.cfg::module::auth_radius.html</a>

#### KSR.auth_radius.proxy_authorize() ####

```cpp
int KSR.auth_radius.proxy_authorize(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize'>📖 kamailio.cfg::function::proxy_authorize()</a>

#### KSR.auth_radius.proxy_authorize_user() ####

```cpp
int KSR.auth_radius.proxy_authorize_user(str "srealm", str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize_user'>📖 kamailio.cfg::function::proxy_authorize_user()</a>

#### KSR.auth_radius.www_authorize() ####

```cpp
int KSR.auth_radius.www_authorize(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize'>📖 kamailio.cfg::function::www_authorize()</a>

#### KSR.auth_radius.www_authorize_user() ####

```cpp
int KSR.auth_radius.www_authorize_user(str "srealm", str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize_user'>📖 kamailio.cfg::function::www_authorize_user()</a>

## auth_xkeys ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html'>📖 kamailio.cfg::module::auth_xkeys.html</a>

#### KSR.auth_xkeys.auth_xkeys_add() ####

```cpp
int KSR.auth_xkeys.auth_xkeys_add(str "shdr", str "skey", str "salg", str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_add'>📖 kamailio.cfg::function::auth_xkeys_add()</a>

#### KSR.auth_xkeys.auth_xkeys_check() ####

```cpp
int KSR.auth_xkeys.auth_xkeys_check(str "shdr", str "skey", str "salg", str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_check'>📖 kamailio.cfg::function::auth_xkeys_check()</a>

## avpops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/avpops.html'>📖 kamailio.cfg::module::avpops.html</a>

#### KSR.avpops.avp_check() ####

```cpp
int KSR.avpops.avp_check(str "param", str "check");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/avpops.html#avpops.f.avp_check'>📖 kamailio.cfg::function::avp_check()</a>

#### KSR.avpops.avp_copy() ####

```cpp
int KSR.avpops.avp_copy(str "name1", str "name2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/avpops.html#avpops.f.avp_copy'>📖 kamailio.cfg::function::avp_copy()</a>

## benchmark ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/benchmark.html'>📖 kamailio.cfg::module::benchmark.html</a>

#### KSR.benchmark.bm_log_timer() ####

```cpp
int KSR.benchmark.bm_log_timer(str "tname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_log_timer'>📖 kamailio.cfg::function::bm_log_timer()</a>

#### KSR.benchmark.bm_start_timer() ####

```cpp
int KSR.benchmark.bm_start_timer(str "tname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_start_timer'>📖 kamailio.cfg::function::bm_start_timer()</a>

## blst ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html'>📖 kamailio.cfg::module::blst.html</a>

#### KSR.blst.blst_add() ####

```cpp
int KSR.blst.blst_add(int t);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add'>📖 kamailio.cfg::function::blst_add()</a>

#### KSR.blst.blst_add_default() ####

```cpp
int KSR.blst.blst_add_default();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add_default'>📖 kamailio.cfg::function::blst_add_default()</a>

#### KSR.blst.blst_add_retry_after() ####

```cpp
int KSR.blst.blst_add_retry_after(int t_min, int t_max);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add_retry_after'>📖 kamailio.cfg::function::blst_add_retry_after()</a>

#### KSR.blst.blst_clear_ignore() ####

```cpp
int KSR.blst.blst_clear_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore'>📖 kamailio.cfg::function::blst_clear_ignore()</a>

#### KSR.blst.blst_clear_ignore_all() ####

```cpp
int KSR.blst.blst_clear_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore_all'>📖 kamailio.cfg::function::blst_clear_ignore_all()</a>

#### KSR.blst.blst_del() ####

```cpp
int KSR.blst.blst_del();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_del'>📖 kamailio.cfg::function::blst_del()</a>

#### KSR.blst.blst_is_blocklisted() ####

```cpp
int KSR.blst.blst_is_blocklisted();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_is_blocklisted'>📖 kamailio.cfg::function::blst_is_blocklisted()</a>

#### KSR.blst.blst_rpl_clear_ignore() ####

```cpp
int KSR.blst.blst_rpl_clear_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore'>📖 kamailio.cfg::function::blst_rpl_clear_ignore()</a>

#### KSR.blst.blst_rpl_clear_ignore_all() ####

```cpp
int KSR.blst.blst_rpl_clear_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore_all'>📖 kamailio.cfg::function::blst_rpl_clear_ignore_all()</a>

#### KSR.blst.blst_rpl_set_ignore() ####

```cpp
int KSR.blst.blst_rpl_set_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore'>📖 kamailio.cfg::function::blst_rpl_set_ignore()</a>

#### KSR.blst.blst_rpl_set_ignore_all() ####

```cpp
int KSR.blst.blst_rpl_set_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore_all'>📖 kamailio.cfg::function::blst_rpl_set_ignore_all()</a>

#### KSR.blst.blst_set_ignore() ####

```cpp
int KSR.blst.blst_set_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore'>📖 kamailio.cfg::function::blst_set_ignore()</a>

#### KSR.blst.blst_set_ignore_all() ####

```cpp
int KSR.blst.blst_set_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore_all'>📖 kamailio.cfg::function::blst_set_ignore_all()</a>

## call_control ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_control.html'>📖 kamailio.cfg::module::call_control.html</a>

#### KSR.call_control.call_control() ####

```cpp
int KSR.call_control.call_control();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_control.html#call_control.f.call_control'>📖 kamailio.cfg::function::call_control()</a>

## call_obj ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_obj.html'>📖 kamailio.cfg::module::call_obj.html</a>

#### KSR.call_obj.free() ####

```cpp
int KSR.call_obj.free(int num_obj);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_obj.html#call_obj.f.free'>📖 kamailio.cfg::function::free()</a>

#### KSR.call_obj.get() ####

```cpp
int KSR.call_obj.get();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_obj.html#call_obj.f.get'>📖 kamailio.cfg::function::get()</a>

## cfgutils ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html'>📖 kamailio.cfg::module::cfgutils.html</a>

#### KSR.cfgutils.abort() ####

```cpp
int KSR.cfgutils.abort();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.abort'>📖 kamailio.cfg::function::abort()</a>

#### KSR.cfgutils.check_route_exists() ####

```cpp
int KSR.cfgutils.check_route_exists(str "route");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.check_route_exists'>📖 kamailio.cfg::function::check_route_exists()</a>

#### KSR.cfgutils.core_hash() ####

```cpp
int KSR.cfgutils.core_hash(str "s1", str "s2", int sz);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.core_hash'>📖 kamailio.cfg::function::core_hash()</a>

#### KSR.cfgutils.lock() ####

```cpp
int KSR.cfgutils.lock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.lock'>📖 kamailio.cfg::function::lock()</a>

#### KSR.cfgutils.pkg_status() ####

```cpp
int KSR.cfgutils.pkg_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_status'>📖 kamailio.cfg::function::pkg_status()</a>

#### KSR.cfgutils.pkg_summary() ####

```cpp
int KSR.cfgutils.pkg_summary();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_summary'>📖 kamailio.cfg::function::pkg_summary()</a>

#### KSR.cfgutils.rand_event() ####

```cpp
int KSR.cfgutils.rand_event();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_event'>📖 kamailio.cfg::function::rand_event()</a>

#### KSR.cfgutils.rand_get_prob() ####

```cpp
int KSR.cfgutils.rand_get_prob();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_get_prob'>📖 kamailio.cfg::function::rand_get_prob()</a>

#### KSR.cfgutils.rand_reset_prob() ####

```cpp
int KSR.cfgutils.rand_reset_prob();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_reset_prob'>📖 kamailio.cfg::function::rand_reset_prob()</a>

#### KSR.cfgutils.rand_set_prob() ####

```cpp
int KSR.cfgutils.rand_set_prob(int percent_par);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_set_prob'>📖 kamailio.cfg::function::rand_set_prob()</a>

#### KSR.cfgutils.route_if_exists() ####

```cpp
int KSR.cfgutils.route_if_exists(str "route");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.route_if_exists'>📖 kamailio.cfg::function::route_if_exists()</a>

#### KSR.cfgutils.shm_status() ####

```cpp
int KSR.cfgutils.shm_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_status'>📖 kamailio.cfg::function::shm_status()</a>

#### KSR.cfgutils.shm_summary() ####

```cpp
int KSR.cfgutils.shm_summary();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_summary'>📖 kamailio.cfg::function::shm_summary()</a>

#### KSR.cfgutils.sleep() ####

```cpp
int KSR.cfgutils.sleep(int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.sleep'>📖 kamailio.cfg::function::sleep()</a>

#### KSR.cfgutils.trylock() ####

```cpp
int KSR.cfgutils.trylock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.trylock'>📖 kamailio.cfg::function::trylock()</a>

#### KSR.cfgutils.unlock() ####

```cpp
int KSR.cfgutils.unlock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.unlock'>📖 kamailio.cfg::function::unlock()</a>

#### KSR.cfgutils.usleep() ####

```cpp
int KSR.cfgutils.usleep(int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.usleep'>📖 kamailio.cfg::function::usleep()</a>

## cnxcc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html'>📖 kamailio.cfg::module::cnxcc.html</a>

#### KSR.cnxcc.get_channel_count() ####

```cpp
int KSR.cnxcc.get_channel_count(str "sclient", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.get_channel_count'>📖 kamailio.cfg::function::get_channel_count()</a>

#### KSR.cnxcc.set_max_channels() ####

```cpp
int KSR.cnxcc.set_max_channels(str "sclient", int max_chan);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_channels'>📖 kamailio.cfg::function::set_max_channels()</a>

#### KSR.cnxcc.set_max_credit() ####

```cpp
int KSR.cnxcc.set_max_credit(str "sclient", str "scredit", str "sconnect", str "scps", int initp, int finishp);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_credit'>📖 kamailio.cfg::function::set_max_credit()</a>

#### KSR.cnxcc.set_max_time() ####

```cpp
int KSR.cnxcc.set_max_time(str "sclient", int max_secs);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_time'>📖 kamailio.cfg::function::set_max_time()</a>

#### KSR.cnxcc.terminate_all() ####

```cpp
int KSR.cnxcc.terminate_all(str "sclient");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.terminate_all'>📖 kamailio.cfg::function::terminate_all()</a>

#### KSR.cnxcc.update_max_time() ####

```cpp
int KSR.cnxcc.update_max_time(str "sclient", int secs);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.update_max_time'>📖 kamailio.cfg::function::update_max_time()</a>

## corex ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html'>📖 kamailio.cfg::module::corex.html</a>

#### KSR.corex.append_branch() ####

```cpp
int KSR.corex.append_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch'>📖 kamailio.cfg::function::append_branch()</a>

#### KSR.corex.append_branch_uri() ####

```cpp
int KSR.corex.append_branch_uri(str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri'>📖 kamailio.cfg::function::append_branch_uri()</a>

#### KSR.corex.append_branch_uri_q() ####

```cpp
int KSR.corex.append_branch_uri_q(str "uri", str "q");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri_q'>📖 kamailio.cfg::function::append_branch_uri_q()</a>

#### KSR.corex.file_read() ####

```cpp
xval KSR.corex.file_read(str "fname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_read'>📖 kamailio.cfg::function::file_read()</a>

#### KSR.corex.file_write() ####

```cpp
int KSR.corex.file_write(str "fname", str "fdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_write'>📖 kamailio.cfg::function::file_write()</a>

#### KSR.corex.has_ruri_user() ####

```cpp
int KSR.corex.has_ruri_user();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_ruri_user'>📖 kamailio.cfg::function::has_ruri_user()</a>

#### KSR.corex.has_user_agent() ####

```cpp
int KSR.corex.has_user_agent();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_user_agent'>📖 kamailio.cfg::function::has_user_agent()</a>

#### KSR.corex.is_faked_msg() ####

```cpp
int KSR.corex.is_faked_msg();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_faked_msg'>📖 kamailio.cfg::function::is_faked_msg()</a>

#### KSR.corex.is_socket_name() ####

```cpp
int KSR.corex.is_socket_name(str "sockname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_socket_name'>📖 kamailio.cfg::function::is_socket_name()</a>

#### KSR.corex.isxflagset() ####

```cpp
int KSR.corex.isxflagset(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.isxflagset'>📖 kamailio.cfg::function::isxflagset()</a>

#### KSR.corex.resetxflag() ####

```cpp
int KSR.corex.resetxflag(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.resetxflag'>📖 kamailio.cfg::function::resetxflag()</a>

#### KSR.corex.send_data() ####

```cpp
int KSR.corex.send_data(str "uri", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.send_data'>📖 kamailio.cfg::function::send_data()</a>

#### KSR.corex.sendx() ####

```cpp
int KSR.corex.sendx(str "uri", str "sock", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.sendx'>📖 kamailio.cfg::function::sendx()</a>

#### KSR.corex.set_recv_socket() ####

```cpp
int KSR.corex.set_recv_socket(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket'>📖 kamailio.cfg::function::set_recv_socket()</a>

#### KSR.corex.set_recv_socket_name() ####

```cpp
int KSR.corex.set_recv_socket_name(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket_name'>📖 kamailio.cfg::function::set_recv_socket_name()</a>

#### KSR.corex.set_send_socket() ####

```cpp
int KSR.corex.set_send_socket(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket'>📖 kamailio.cfg::function::set_send_socket()</a>

#### KSR.corex.set_send_socket_name() ####

```cpp
int KSR.corex.set_send_socket_name(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket_name'>📖 kamailio.cfg::function::set_send_socket_name()</a>

#### KSR.corex.set_source_address() ####

```cpp
int KSR.corex.set_source_address(str "saddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_source_address'>📖 kamailio.cfg::function::set_source_address()</a>

#### KSR.corex.setxflag() ####

```cpp
int KSR.corex.setxflag(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.setxflag'>📖 kamailio.cfg::function::setxflag()</a>

#### KSR.corex.via_add_srvid() ####

```cpp
int KSR.corex.via_add_srvid(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_srvid'>📖 kamailio.cfg::function::via_add_srvid()</a>

#### KSR.corex.via_add_xavp_params() ####

```cpp
int KSR.corex.via_add_xavp_params(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_xavp_params'>📖 kamailio.cfg::function::via_add_xavp_params()</a>

#### KSR.corex.via_use_xavp_fields() ####

```cpp
int KSR.corex.via_use_xavp_fields(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_use_xavp_fields'>📖 kamailio.cfg::function::via_use_xavp_fields()</a>

## counters ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html'>📖 kamailio.cfg::module::counters.html</a>

#### KSR.counters.add() ####

```cpp
int KSR.counters.add(str "sname", int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.add'>📖 kamailio.cfg::function::add()</a>

#### KSR.counters.inc() ####

```cpp
int KSR.counters.inc(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.inc'>📖 kamailio.cfg::function::inc()</a>

#### KSR.counters.reset() ####

```cpp
int KSR.counters.reset(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.reset'>📖 kamailio.cfg::function::reset()</a>

## crypto ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html'>📖 kamailio.cfg::module::crypto.html</a>

#### KSR.crypto.aes_decrypt() ####

```cpp
int KSR.crypto.aes_decrypt(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.aes_decrypt'>📖 kamailio.cfg::function::aes_decrypt()</a>

#### KSR.crypto.aes_encrypt() ####

```cpp
int KSR.crypto.aes_encrypt(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.aes_encrypt'>📖 kamailio.cfg::function::aes_encrypt()</a>

#### KSR.crypto.hmac_sha256() ####

```cpp
int KSR.crypto.hmac_sha256(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.hmac_sha256'>📖 kamailio.cfg::function::hmac_sha256()</a>

## debugger ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/debugger.html'>📖 kamailio.cfg::module::debugger.html</a>

#### KSR.debugger.dbg_pv_dump() ####

```cpp
int KSR.debugger.dbg_pv_dump();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump'>📖 kamailio.cfg::function::dbg_pv_dump()</a>

#### KSR.debugger.dbg_pv_dump_ex() ####

```cpp
int KSR.debugger.dbg_pv_dump_ex(int mask, int level);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump_ex'>📖 kamailio.cfg::function::dbg_pv_dump_ex()</a>

## dialog ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html'>📖 kamailio.cfg::module::dialog.html</a>

#### KSR.dialog.dlg_bridge() ####

```cpp
int KSR.dialog.dlg_bridge(str "sfrom", str "sto", str "soproxy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bridge'>📖 kamailio.cfg::function::dlg_bridge()</a>

#### KSR.dialog.dlg_bye() ####

```cpp
int KSR.dialog.dlg_bye(str "side");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bye'>📖 kamailio.cfg::function::dlg_bye()</a>

#### KSR.dialog.dlg_db_load_callid() ####

```cpp
int KSR.dialog.dlg_db_load_callid(str "callid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_callid'>📖 kamailio.cfg::function::dlg_db_load_callid()</a>

#### KSR.dialog.dlg_db_load_extra() ####

```cpp
int KSR.dialog.dlg_db_load_extra();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_extra'>📖 kamailio.cfg::function::dlg_db_load_extra()</a>

#### KSR.dialog.dlg_get() ####

```cpp
int KSR.dialog.dlg_get(str "sc", str "sf", str "st");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_get'>📖 kamailio.cfg::function::dlg_get()</a>

#### KSR.dialog.dlg_isflagset() ####

```cpp
int KSR.dialog.dlg_isflagset(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_isflagset'>📖 kamailio.cfg::function::dlg_isflagset()</a>

#### KSR.dialog.dlg_manage() ####

```cpp
int KSR.dialog.dlg_manage();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_manage'>📖 kamailio.cfg::function::dlg_manage()</a>

#### KSR.dialog.dlg_reset_property() ####

```cpp
int KSR.dialog.dlg_reset_property(str "pval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_reset_property'>📖 kamailio.cfg::function::dlg_reset_property()</a>

#### KSR.dialog.dlg_resetflag() ####

```cpp
int KSR.dialog.dlg_resetflag(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_resetflag'>📖 kamailio.cfg::function::dlg_resetflag()</a>

#### KSR.dialog.dlg_set_property() ####

```cpp
int KSR.dialog.dlg_set_property(str "pval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_property'>📖 kamailio.cfg::function::dlg_set_property()</a>

#### KSR.dialog.dlg_set_timeout() ####

```cpp
int KSR.dialog.dlg_set_timeout(int to);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout'>📖 kamailio.cfg::function::dlg_set_timeout()</a>

#### KSR.dialog.dlg_set_timeout_id() ####

```cpp
int KSR.dialog.dlg_set_timeout_id(int to, int he, int hi);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout_id'>📖 kamailio.cfg::function::dlg_set_timeout_id()</a>

#### KSR.dialog.dlg_setflag() ####

```cpp
int KSR.dialog.dlg_setflag(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_setflag'>📖 kamailio.cfg::function::dlg_setflag()</a>

#### KSR.dialog.get_profile_size() ####

```cpp
int KSR.dialog.get_profile_size(str "sprofile", str "svalue", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size'>📖 kamailio.cfg::function::get_profile_size()</a>

#### KSR.dialog.get_profile_size_static() ####

```cpp
int KSR.dialog.get_profile_size_static(str "sprofile", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size_static'>📖 kamailio.cfg::function::get_profile_size_static()</a>

#### KSR.dialog.is_in_profile() ####

```cpp
int KSR.dialog.is_in_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile'>📖 kamailio.cfg::function::is_in_profile()</a>

#### KSR.dialog.is_in_profile_static() ####

```cpp
int KSR.dialog.is_in_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile_static'>📖 kamailio.cfg::function::is_in_profile_static()</a>

#### KSR.dialog.is_known_dlg() ####

```cpp
int KSR.dialog.is_known_dlg();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_known_dlg'>📖 kamailio.cfg::function::is_known_dlg()</a>

#### KSR.dialog.set_dlg_profile() ####

```cpp
int KSR.dialog.set_dlg_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile'>📖 kamailio.cfg::function::set_dlg_profile()</a>

#### KSR.dialog.set_dlg_profile_static() ####

```cpp
int KSR.dialog.set_dlg_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile_static'>📖 kamailio.cfg::function::set_dlg_profile_static()</a>

#### KSR.dialog.unset_dlg_profile() ####

```cpp
int KSR.dialog.unset_dlg_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile'>📖 kamailio.cfg::function::unset_dlg_profile()</a>

#### KSR.dialog.unset_dlg_profile_static() ####

```cpp
int KSR.dialog.unset_dlg_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile_static'>📖 kamailio.cfg::function::unset_dlg_profile_static()</a>

#### KSR.dialog.var_get() ####

```cpp
xval KSR.dialog.var_get(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_get'>📖 kamailio.cfg::function::var_get()</a>

#### KSR.dialog.var_gete() ####

```cpp
xval KSR.dialog.var_gete(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_gete'>📖 kamailio.cfg::function::var_gete()</a>

#### KSR.dialog.var_getw() ####

```cpp
xval KSR.dialog.var_getw(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_getw'>📖 kamailio.cfg::function::var_getw()</a>

#### KSR.dialog.var_is_null() ####

```cpp
int KSR.dialog.var_is_null(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_is_null'>📖 kamailio.cfg::function::var_is_null()</a>

#### KSR.dialog.var_rm() ####

```cpp
int KSR.dialog.var_rm(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_rm'>📖 kamailio.cfg::function::var_rm()</a>

#### KSR.dialog.var_sets() ####

```cpp
int KSR.dialog.var_sets(str "name", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_sets'>📖 kamailio.cfg::function::var_sets()</a>

## dialplan ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialplan.html'>📖 kamailio.cfg::module::dialplan.html</a>

#### KSR.dialplan.dp_match() ####

```cpp
int KSR.dialplan.dp_match(int dpid, str "src");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_match'>📖 kamailio.cfg::function::dp_match()</a>

#### KSR.dialplan.dp_replace() ####

```cpp
int KSR.dialplan.dp_replace(int dpid, str "src", str "dst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_replace'>📖 kamailio.cfg::function::dp_replace()</a>

## dispatcher ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html'>📖 kamailio.cfg::module::dispatcher.html</a>

#### KSR.dispatcher.ds_is_active() ####

```cpp
int KSR.dispatcher.ds_is_active(int set);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_active'>📖 kamailio.cfg::function::ds_is_active()</a>

#### KSR.dispatcher.ds_is_active_uri() ####

```cpp
int KSR.dispatcher.ds_is_active_uri(int set, str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_active_uri'>📖 kamailio.cfg::function::ds_is_active_uri()</a>

#### KSR.dispatcher.ds_is_from_list() ####

```cpp
int KSR.dispatcher.ds_is_from_list(int group);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list'>📖 kamailio.cfg::function::ds_is_from_list()</a>

#### KSR.dispatcher.ds_is_from_list_mode() ####

```cpp
int KSR.dispatcher.ds_is_from_list_mode(int vset, int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_mode'>📖 kamailio.cfg::function::ds_is_from_list_mode()</a>

#### KSR.dispatcher.ds_is_from_list_uri() ####

```cpp
int KSR.dispatcher.ds_is_from_list_uri(int vset, int vmode, str "vuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_uri'>📖 kamailio.cfg::function::ds_is_from_list_uri()</a>

#### KSR.dispatcher.ds_is_from_lists() ####

```cpp
int KSR.dispatcher.ds_is_from_lists();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_lists'>📖 kamailio.cfg::function::ds_is_from_lists()</a>

#### KSR.dispatcher.ds_list_exists() ####

```cpp
int KSR.dispatcher.ds_list_exists(int set);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_list_exists'>📖 kamailio.cfg::function::ds_list_exists()</a>

#### KSR.dispatcher.ds_load_unset() ####

```cpp
int KSR.dispatcher.ds_load_unset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_unset'>📖 kamailio.cfg::function::ds_load_unset()</a>

#### KSR.dispatcher.ds_load_update() ####

```cpp
int KSR.dispatcher.ds_load_update();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_update'>📖 kamailio.cfg::function::ds_load_update()</a>

#### KSR.dispatcher.ds_mark_dst() ####

```cpp
int KSR.dispatcher.ds_mark_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst'>📖 kamailio.cfg::function::ds_mark_dst()</a>

#### KSR.dispatcher.ds_mark_dst_state() ####

```cpp
int KSR.dispatcher.ds_mark_dst_state(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst_state'>📖 kamailio.cfg::function::ds_mark_dst_state()</a>

#### KSR.dispatcher.ds_next_domain() ####

```cpp
int KSR.dispatcher.ds_next_domain();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_domain'>📖 kamailio.cfg::function::ds_next_domain()</a>

#### KSR.dispatcher.ds_next_dst() ####

```cpp
int KSR.dispatcher.ds_next_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_dst'>📖 kamailio.cfg::function::ds_next_dst()</a>

#### KSR.dispatcher.ds_reload() ####

```cpp
int KSR.dispatcher.ds_reload();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_reload'>📖 kamailio.cfg::function::ds_reload()</a>

#### KSR.dispatcher.ds_select() ####

```cpp
int KSR.dispatcher.ds_select(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select'>📖 kamailio.cfg::function::ds_select()</a>

#### KSR.dispatcher.ds_select_domain() ####

```cpp
int KSR.dispatcher.ds_select_domain(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain'>📖 kamailio.cfg::function::ds_select_domain()</a>

#### KSR.dispatcher.ds_select_domain_limit() ####

```cpp
int KSR.dispatcher.ds_select_domain_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain_limit'>📖 kamailio.cfg::function::ds_select_domain_limit()</a>

#### KSR.dispatcher.ds_select_dst() ####

```cpp
int KSR.dispatcher.ds_select_dst(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst'>📖 kamailio.cfg::function::ds_select_dst()</a>

#### KSR.dispatcher.ds_select_dst_limit() ####

```cpp
int KSR.dispatcher.ds_select_dst_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst_limit'>📖 kamailio.cfg::function::ds_select_dst_limit()</a>

#### KSR.dispatcher.ds_select_limit() ####

```cpp
int KSR.dispatcher.ds_select_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_limit'>📖 kamailio.cfg::function::ds_select_limit()</a>

#### KSR.dispatcher.ds_select_routes() ####

```cpp
int KSR.dispatcher.ds_select_routes(str "srules", str "smode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes'>📖 kamailio.cfg::function::ds_select_routes()</a>

#### KSR.dispatcher.ds_select_routes_limit() ####

```cpp
int KSR.dispatcher.ds_select_routes_limit(str "srules", str "smode", int rlimit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes_limit'>📖 kamailio.cfg::function::ds_select_routes_limit()</a>

#### KSR.dispatcher.ds_set_domain() ####

```cpp
int KSR.dispatcher.ds_set_domain();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_domain'>📖 kamailio.cfg::function::ds_set_domain()</a>

#### KSR.dispatcher.ds_set_dst() ####

```cpp
int KSR.dispatcher.ds_set_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_dst'>📖 kamailio.cfg::function::ds_set_dst()</a>

## diversion ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/diversion.html'>📖 kamailio.cfg::module::diversion.html</a>

#### KSR.diversion.add_diversion() ####

```cpp
int KSR.diversion.add_diversion(str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion'>📖 kamailio.cfg::function::add_diversion()</a>

#### KSR.diversion.add_diversion_uri() ####

```cpp
int KSR.diversion.add_diversion_uri(str "reason", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion_uri'>📖 kamailio.cfg::function::add_diversion_uri()</a>

## dlgs ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html'>📖 kamailio.cfg::module::dlgs.html</a>

#### KSR.dlgs.dlgs_count() ####

```cpp
int KSR.dlgs.dlgs_count(str "vfield", str "vop", str "vdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_count'>📖 kamailio.cfg::function::dlgs_count()</a>

#### KSR.dlgs.dlgs_init() ####

```cpp
int KSR.dlgs.dlgs_init(str "src", str "dst", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_init'>📖 kamailio.cfg::function::dlgs_init()</a>

#### KSR.dlgs.dlgs_tags_add() ####

```cpp
int KSR.dlgs.dlgs_tags_add(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_add'>📖 kamailio.cfg::function::dlgs_tags_add()</a>

#### KSR.dlgs.dlgs_tags_count() ####

```cpp
int KSR.dlgs.dlgs_tags_count(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_count'>📖 kamailio.cfg::function::dlgs_tags_count()</a>

#### KSR.dlgs.dlgs_tags_rm() ####

```cpp
int KSR.dlgs.dlgs_tags_rm(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_rm'>📖 kamailio.cfg::function::dlgs_tags_rm()</a>

#### KSR.dlgs.dlgs_update() ####

```cpp
int KSR.dlgs.dlgs_update();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_update'>📖 kamailio.cfg::function::dlgs_update()</a>

## dmq ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html'>📖 kamailio.cfg::module::dmq.html</a>

#### KSR.dmq.bcast_message() ####

```cpp
int KSR.dmq.bcast_message(str "peer_str", str "body_str", str "ct_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.bcast_message'>📖 kamailio.cfg::function::bcast_message()</a>

#### KSR.dmq.handle_message() ####

```cpp
int KSR.dmq.handle_message();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message'>📖 kamailio.cfg::function::handle_message()</a>

#### KSR.dmq.handle_message_rc() ####

```cpp
int KSR.dmq.handle_message_rc(int returnval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message_rc'>📖 kamailio.cfg::function::handle_message_rc()</a>

#### KSR.dmq.is_from_node() ####

```cpp
int KSR.dmq.is_from_node();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.is_from_node'>📖 kamailio.cfg::function::is_from_node()</a>

#### KSR.dmq.process_message() ####

```cpp
int KSR.dmq.process_message();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.process_message'>📖 kamailio.cfg::function::process_message()</a>

#### KSR.dmq.process_message_rc() ####

```cpp
int KSR.dmq.process_message_rc(int returnval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.process_message_rc'>📖 kamailio.cfg::function::process_message_rc()</a>

#### KSR.dmq.send_message() ####

```cpp
int KSR.dmq.send_message(str "peer_str", str "to_str", str "body_str", str "ct_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.send_message'>📖 kamailio.cfg::function::send_message()</a>

#### KSR.dmq.t_replicate() ####

```cpp
int KSR.dmq.t_replicate();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate'>📖 kamailio.cfg::function::t_replicate()</a>

#### KSR.dmq.t_replicate_mode() ####

```cpp
int KSR.dmq.t_replicate_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate_mode'>📖 kamailio.cfg::function::t_replicate_mode()</a>

## domain ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html'>📖 kamailio.cfg::module::domain.html</a>

#### KSR.domain.is_domain_local() ####

```cpp
int KSR.domain.is_domain_local(str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_domain_local'>📖 kamailio.cfg::function::is_domain_local()</a>

#### KSR.domain.is_from_local() ####

```cpp
int KSR.domain.is_from_local();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_from_local'>📖 kamailio.cfg::function::is_from_local()</a>

#### KSR.domain.is_uri_host_local() ####

```cpp
int KSR.domain.is_uri_host_local();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_uri_host_local'>📖 kamailio.cfg::function::is_uri_host_local()</a>

#### KSR.domain.lookup_domain() ####

```cpp
int KSR.domain.lookup_domain(str "_sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain'>📖 kamailio.cfg::function::lookup_domain()</a>

#### KSR.domain.lookup_domain_prefix() ####

```cpp
int KSR.domain.lookup_domain_prefix(str "_sdomain", str "_sprefix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain_prefix'>📖 kamailio.cfg::function::lookup_domain_prefix()</a>

## drouting ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html'>📖 kamailio.cfg::module::drouting.html</a>

#### KSR.drouting.do_routing() ####

```cpp
int KSR.drouting.do_routing(int grp_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.do_routing'>📖 kamailio.cfg::function::do_routing()</a>

#### KSR.drouting.do_routing_furi() ####

```cpp
int KSR.drouting.do_routing_furi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.do_routing_furi'>📖 kamailio.cfg::function::do_routing_furi()</a>

#### KSR.drouting.goes_to_gw() ####

```cpp
int KSR.drouting.goes_to_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw'>📖 kamailio.cfg::function::goes_to_gw()</a>

#### KSR.drouting.goes_to_gw_type() ####

```cpp
int KSR.drouting.goes_to_gw_type(int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw_type'>📖 kamailio.cfg::function::goes_to_gw_type()</a>

#### KSR.drouting.is_from_gw() ####

```cpp
int KSR.drouting.is_from_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw'>📖 kamailio.cfg::function::is_from_gw()</a>

#### KSR.drouting.is_from_gw_type() ####

```cpp
int KSR.drouting.is_from_gw_type(int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type'>📖 kamailio.cfg::function::is_from_gw_type()</a>

#### KSR.drouting.is_from_gw_type_flags() ####

```cpp
int KSR.drouting.is_from_gw_type_flags(int type, int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type_flags'>📖 kamailio.cfg::function::is_from_gw_type_flags()</a>

#### KSR.drouting.next_routing() ####

```cpp
int KSR.drouting.next_routing();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.next_routing'>📖 kamailio.cfg::function::next_routing()</a>

#### KSR.drouting.use_next_gw() ####

```cpp
int KSR.drouting.use_next_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.use_next_gw'>📖 kamailio.cfg::function::use_next_gw()</a>

## enum ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html'>📖 kamailio.cfg::module::enum.html</a>

#### KSR.enum.enum_i_query_suffix() ####

```cpp
int KSR.enum.enum_i_query_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_i_query_suffix'>📖 kamailio.cfg::function::enum_i_query_suffix()</a>

#### KSR.enum.enum_pv_query() ####

```cpp
int KSR.enum.enum_pv_query(str "ve164");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query'>📖 kamailio.cfg::function::enum_pv_query()</a>

#### KSR.enum.enum_pv_query_suffix() ####

```cpp
int KSR.enum.enum_pv_query_suffix(str "ve164", str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix'>📖 kamailio.cfg::function::enum_pv_query_suffix()</a>

#### KSR.enum.enum_pv_query_suffix_service() ####

```cpp
int KSR.enum.enum_pv_query_suffix_service(str "ve164", str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix_service'>📖 kamailio.cfg::function::enum_pv_query_suffix_service()</a>

#### KSR.enum.enum_query() ####

```cpp
int KSR.enum.enum_query();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query'>📖 kamailio.cfg::function::enum_query()</a>

#### KSR.enum.enum_query_suffix() ####

```cpp
int KSR.enum.enum_query_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix'>📖 kamailio.cfg::function::enum_query_suffix()</a>

#### KSR.enum.enum_query_suffix_service() ####

```cpp
int KSR.enum.enum_query_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix_service'>📖 kamailio.cfg::function::enum_query_suffix_service()</a>

#### KSR.enum.i_enum_query() ####

```cpp
int KSR.enum.i_enum_query();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query'>📖 kamailio.cfg::function::i_enum_query()</a>

#### KSR.enum.i_enum_query_suffix_service() ####

```cpp
int KSR.enum.i_enum_query_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query_suffix_service'>📖 kamailio.cfg::function::i_enum_query_suffix_service()</a>

#### KSR.enum.is_from_user_enum() ####

```cpp
int KSR.enum.is_from_user_enum();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum'>📖 kamailio.cfg::function::is_from_user_enum()</a>

#### KSR.enum.is_from_user_enum_suffix() ####

```cpp
int KSR.enum.is_from_user_enum_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix'>📖 kamailio.cfg::function::is_from_user_enum_suffix()</a>

#### KSR.enum.is_from_user_enum_suffix_service() ####

```cpp
int KSR.enum.is_from_user_enum_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix_service'>📖 kamailio.cfg::function::is_from_user_enum_suffix_service()</a>

## evapi ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html'>📖 kamailio.cfg::module::evapi.html</a>

#### KSR.evapi.async_multicast() ####

```cpp
int KSR.evapi.async_multicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_multicast'>📖 kamailio.cfg::function::async_multicast()</a>

#### KSR.evapi.async_relay() ####

```cpp
int KSR.evapi.async_relay(str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_relay'>📖 kamailio.cfg::function::async_relay()</a>

#### KSR.evapi.async_unicast() ####

```cpp
int KSR.evapi.async_unicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_unicast'>📖 kamailio.cfg::function::async_unicast()</a>

#### KSR.evapi.close() ####

```cpp
int KSR.evapi.close();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.close'>📖 kamailio.cfg::function::close()</a>

#### KSR.evapi.relay() ####

```cpp
int KSR.evapi.relay(str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay'>📖 kamailio.cfg::function::relay()</a>

#### KSR.evapi.relay_multicast() ####

```cpp
int KSR.evapi.relay_multicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_multicast'>📖 kamailio.cfg::function::relay_multicast()</a>

#### KSR.evapi.relay_unicast() ####

```cpp
int KSR.evapi.relay_unicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_unicast'>📖 kamailio.cfg::function::relay_unicast()</a>

#### KSR.evapi.set_tag() ####

```cpp
int KSR.evapi.set_tag(str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.set_tag'>📖 kamailio.cfg::function::set_tag()</a>

## exec ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html'>📖 kamailio.cfg::module::exec.html</a>

#### KSR.exec.exec_avp() ####

```cpp
int KSR.exec.exec_avp(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_avp'>📖 kamailio.cfg::function::exec_avp()</a>

#### KSR.exec.exec_cmd() ####

```cpp
int KSR.exec.exec_cmd(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_cmd'>📖 kamailio.cfg::function::exec_cmd()</a>

#### KSR.exec.exec_dset() ####

```cpp
int KSR.exec.exec_dset(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_dset'>📖 kamailio.cfg::function::exec_dset()</a>

#### KSR.exec.exec_msg() ####

```cpp
int KSR.exec.exec_msg(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_msg'>📖 kamailio.cfg::function::exec_msg()</a>

## geoip ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip.html'>📖 kamailio.cfg::module::geoip.html</a>

#### KSR.geoip.match() ####

```cpp
int KSR.geoip.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip.html#geoip.f.match'>📖 kamailio.cfg::function::match()</a>

## geoip2 ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip2.html'>📖 kamailio.cfg::module::geoip2.html</a>

#### KSR.geoip2.match() ####

```cpp
int KSR.geoip2.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip2.html#geoip2.f.match'>📖 kamailio.cfg::function::match()</a>

## group ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/group.html'>📖 kamailio.cfg::module::group.html</a>

#### KSR.group.is_user_in() ####

```cpp
int KSR.group.is_user_in(str "uri", str "grp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/group.html#group.f.is_user_in'>📖 kamailio.cfg::function::is_user_in()</a>

## htable ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html'>📖 kamailio.cfg::module::htable.html</a>

Functions exported by `htable` module.

#### KSR.htable.sht_dec() ####

```cpp
int KSR.htable.sht_dec(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_dec'>📖 kamailio.cfg::function::sht_dec()</a>

Do atomic decrement to the item value. It returns the new value or `-255`
if the hash table does not exist, or the item does not exist or the item value
is not integer.

#### KSR.htable.sht_get() ####

```cpp
xval KSR.htable.sht_get(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_get'>📖 kamailio.cfg::function::sht_get()</a>

Return the integer or string value of the item.

If the item does not exists, it returns `NULL`. Note that `NULL` might be represented differently in various scripting languages, such as `nil` or `None`.

#### KSR.htable.sht_gete() ####

```cpp
xval KSR.htable.sht_gete(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_gete'>📖 kamailio.cfg::function::sht_gete()</a>

Return the integer or string value of the item.

If the item does not exists, it returns an empty string.

#### KSR.htable.sht_getw() ####

```cpp
xval KSR.htable.sht_getw(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_getw'>📖 kamailio.cfg::function::sht_getw()</a>

Return the integer or string value of the item.

If the item does not exists, it returns the string `<null>`, suitable for use
when writing log messages.

#### KSR.htable.sht_inc() ####

```cpp
int KSR.htable.sht_inc(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_inc'>📖 kamailio.cfg::function::sht_inc()</a>

Do atomic increment to the item value. It returns the new value or `-255`
if the hash table does not exist, or the item does not exist or the item value
is not integer.

#### KSR.htable.sht_is_null() ####

```cpp
int KSR.htable.sht_is_null(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_is_null'>📖 kamailio.cfg::function::sht_is_null()</a>

#### KSR.htable.sht_iterator_end() ####

```cpp
int KSR.htable.sht_iterator_end(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_end'>📖 kamailio.cfg::function::sht_iterator_end()</a>

#### KSR.htable.sht_iterator_next() ####

```cpp
int KSR.htable.sht_iterator_next(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_next'>📖 kamailio.cfg::function::sht_iterator_next()</a>

#### KSR.htable.sht_iterator_start() ####

```cpp
int KSR.htable.sht_iterator_start(str "iname", str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_start'>📖 kamailio.cfg::function::sht_iterator_start()</a>

#### KSR.htable.sht_lock() ####

```cpp
int KSR.htable.sht_lock(str "htname", str "skey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_lock'>📖 kamailio.cfg::function::sht_lock()</a>

#### KSR.htable.sht_match_name() ####

```cpp
int KSR.htable.sht_match_name(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_name'>📖 kamailio.cfg::function::sht_match_name()</a>

#### KSR.htable.sht_match_str_value() ####

```cpp
int KSR.htable.sht_match_str_value(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_str_value'>📖 kamailio.cfg::function::sht_match_str_value()</a>

#### KSR.htable.sht_reset() ####

```cpp
int KSR.htable.sht_reset(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_reset'>📖 kamailio.cfg::function::sht_reset()</a>

#### KSR.htable.sht_rm() ####

```cpp
int KSR.htable.sht_rm(str "hname", str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm'>📖 kamailio.cfg::function::sht_rm()</a>

#### KSR.htable.sht_rm_name() ####

```cpp
int KSR.htable.sht_rm_name(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name'>📖 kamailio.cfg::function::sht_rm_name()</a>

#### KSR.htable.sht_rm_name_re() ####

```cpp
int KSR.htable.sht_rm_name_re(str "htname", str "rexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name_re'>📖 kamailio.cfg::function::sht_rm_name_re()</a>

#### KSR.htable.sht_rm_value() ####

```cpp
int KSR.htable.sht_rm_value(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value'>📖 kamailio.cfg::function::sht_rm_value()</a>

#### KSR.htable.sht_rm_value_re() ####

```cpp
int KSR.htable.sht_rm_value_re(str "htname", str "rexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value_re'>📖 kamailio.cfg::function::sht_rm_value_re()</a>

#### KSR.htable.sht_setex() ####

```cpp
int KSR.htable.sht_setex(str "htname", str "itname", int itval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setex'>📖 kamailio.cfg::function::sht_setex()</a>

#### KSR.htable.sht_seti() ####

```cpp
int KSR.htable.sht_seti(str "htname", str "itname", int itval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_seti'>📖 kamailio.cfg::function::sht_seti()</a>

#### KSR.htable.sht_sets() ####

```cpp
int KSR.htable.sht_sets(str "htname", str "itname", str "itval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_sets'>📖 kamailio.cfg::function::sht_sets()</a>

#### KSR.htable.sht_setxi() ####

```cpp
int KSR.htable.sht_setxi(str "htname", str "itname", int itval, int exval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxi'>📖 kamailio.cfg::function::sht_setxi()</a>

#### KSR.htable.sht_setxs() ####

```cpp
int KSR.htable.sht_setxs(str "htname", str "itname", str "itval", int exval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxs'>📖 kamailio.cfg::function::sht_setxs()</a>

#### KSR.htable.sht_unlock() ####

```cpp
int KSR.htable.sht_unlock(str "htname", str "skey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_unlock'>📖 kamailio.cfg::function::sht_unlock()</a>

## http_async_client ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_async_client.html'>📖 kamailio.cfg::module::http_async_client.html</a>

#### KSR.http_async_client.query() ####

```cpp
int KSR.http_async_client.query(str "sdata", str "rn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_async_client.html#http_async_client.f.query'>📖 kamailio.cfg::function::query()</a>

## http_client ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html'>📖 kamailio.cfg::module::http_client.html</a>

#### KSR.http_client.curl_connect() ####

```cpp
int KSR.http_client.curl_connect(str "con", str "url", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect'>📖 kamailio.cfg::function::curl_connect()</a>

#### KSR.http_client.curl_connect_post() ####

```cpp
int KSR.http_client.curl_connect_post(str "con", str "url", str "ctype", str "data", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect_post'>📖 kamailio.cfg::function::curl_connect_post()</a>

#### KSR.http_client.get_hdrs() ####

```cpp
int KSR.http_client.get_hdrs(str "url", str "body", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.get_hdrs'>📖 kamailio.cfg::function::get_hdrs()</a>

#### KSR.http_client.query() ####

```cpp
int KSR.http_client.query(str "url", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query'>📖 kamailio.cfg::function::query()</a>

#### KSR.http_client.query_post() ####

```cpp
int KSR.http_client.query_post(str "url", str "post", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post'>📖 kamailio.cfg::function::query_post()</a>

#### KSR.http_client.query_post_hdrs() ####

```cpp
int KSR.http_client.query_post_hdrs(str "url", str "post", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post_hdrs'>📖 kamailio.cfg::function::query_post_hdrs()</a>

## imc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/imc.html'>📖 kamailio.cfg::module::imc.html</a>

#### KSR.imc.imc_manager() ####

```cpp
int KSR.imc.imc_manager();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/imc.html#imc.f.imc_manager'>📖 kamailio.cfg::function::imc_manager()</a>

## ims_charging ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_charging.html'>📖 kamailio.cfg::module::ims_charging.html</a>

#### KSR.ims_charging.Ro_CCR() ####

```cpp
int KSR.ims_charging.Ro_CCR(str "s_route_name", str "s_direction", int reservation_units, str "s_incoming_trunk_id", str "s_outgoing_trunk_id");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_CCR'>📖 kamailio.cfg::function::Ro_CCR()</a>

#### KSR.ims_charging.Ro_CCR_Stop() ####

```cpp
int KSR.ims_charging.Ro_CCR_Stop(str "p_direction", int p_code, str "p_reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_CCR_Stop'>📖 kamailio.cfg::function::Ro_CCR_Stop()</a>

#### KSR.ims_charging.Ro_set_session_id_avp() ####

```cpp
int KSR.ims_charging.Ro_set_session_id_avp();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_charging.html#ims_charging.f.Ro_set_session_id_avp'>📖 kamailio.cfg::function::Ro_set_session_id_avp()</a>

## ims_diameter_server ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_diameter_server.html'>📖 kamailio.cfg::module::ims_diameter_server.html</a>

#### KSR.ims_diameter_server.diameter_request() ####

```cpp
int KSR.ims_diameter_server.diameter_request(str "peer", int appid, int commandcode, str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_diameter_server.html#ims_diameter_server.f.diameter_request'>📖 kamailio.cfg::function::diameter_request()</a>

#### KSR.ims_diameter_server.diameter_request_async() ####

```cpp
int KSR.ims_diameter_server.diameter_request_async(str "peer", int appid, int commandcode, str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ims_diameter_server.html#ims_diameter_server.f.diameter_request_async'>📖 kamailio.cfg::function::diameter_request_async()</a>

## ipops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html'>📖 kamailio.cfg::module::ipops.html</a>

#### KSR.ipops.compare_ips() ####

```cpp
int KSR.ipops.compare_ips(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_ips'>📖 kamailio.cfg::function::compare_ips()</a>

#### KSR.ipops.compare_pure_ips() ####

```cpp
int KSR.ipops.compare_pure_ips(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_pure_ips'>📖 kamailio.cfg::function::compare_pure_ips()</a>

#### KSR.ipops.detailed_ip_type() ####

```cpp
int KSR.ipops.detailed_ip_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ip_type'>📖 kamailio.cfg::function::detailed_ip_type()</a>

#### KSR.ipops.detailed_ipv4_type() ####

```cpp
int KSR.ipops.detailed_ipv4_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv4_type'>📖 kamailio.cfg::function::detailed_ipv4_type()</a>

#### KSR.ipops.detailed_ipv6_type() ####

```cpp
int KSR.ipops.detailed_ipv6_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv6_type'>📖 kamailio.cfg::function::detailed_ipv6_type()</a>

#### KSR.ipops.dns_int_match_ip() ####

```cpp
int KSR.ipops.dns_int_match_ip(str "vhn", str "vip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_int_match_ip'>📖 kamailio.cfg::function::dns_int_match_ip()</a>

#### KSR.ipops.dns_query() ####

```cpp
int KSR.ipops.dns_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_query'>📖 kamailio.cfg::function::dns_query()</a>

#### KSR.ipops.dns_sys_match_ip() ####

```cpp
int KSR.ipops.dns_sys_match_ip(str "vhn", str "vip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_sys_match_ip'>📖 kamailio.cfg::function::dns_sys_match_ip()</a>

#### KSR.ipops.ip_is_in_subnet() ####

```cpp
int KSR.ipops.ip_is_in_subnet(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_is_in_subnet'>📖 kamailio.cfg::function::ip_is_in_subnet()</a>

#### KSR.ipops.ip_type() ####

```cpp
int KSR.ipops.ip_type(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_type'>📖 kamailio.cfg::function::ip_type()</a>

#### KSR.ipops.is_in_subnet() ####

```cpp
int KSR.ipops.is_in_subnet(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_in_subnet'>📖 kamailio.cfg::function::is_in_subnet()</a>

#### KSR.ipops.is_ip() ####

```cpp
int KSR.ipops.is_ip(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip'>📖 kamailio.cfg::function::is_ip()</a>

#### KSR.ipops.is_ip4() ####

```cpp
int KSR.ipops.is_ip4(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip4'>📖 kamailio.cfg::function::is_ip4()</a>

#### KSR.ipops.is_ip6() ####

```cpp
int KSR.ipops.is_ip6(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6'>📖 kamailio.cfg::function::is_ip6()</a>

#### KSR.ipops.is_ip6_reference() ####

```cpp
int KSR.ipops.is_ip6_reference(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6_reference'>📖 kamailio.cfg::function::is_ip6_reference()</a>

#### KSR.ipops.is_ip_rfc1918() ####

```cpp
int KSR.ipops.is_ip_rfc1918(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip_rfc1918'>📖 kamailio.cfg::function::is_ip_rfc1918()</a>

#### KSR.ipops.is_pure_ip() ####

```cpp
int KSR.ipops.is_pure_ip(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_pure_ip'>📖 kamailio.cfg::function::is_pure_ip()</a>

#### KSR.ipops.naptr_query() ####

```cpp
int KSR.ipops.naptr_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.naptr_query'>📖 kamailio.cfg::function::naptr_query()</a>

#### KSR.ipops.srv_query() ####

```cpp
int KSR.ipops.srv_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.srv_query'>📖 kamailio.cfg::function::srv_query()</a>

## jansson ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jansson.html'>📖 kamailio.cfg::module::jansson.html</a>

#### KSR.jansson.get() ####

```cpp
int KSR.jansson.get(str "spath", str "sdoc", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jansson.html#jansson.f.get'>📖 kamailio.cfg::function::get()</a>

## jsonrpcs ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html'>📖 kamailio.cfg::module::jsonrpcs.html</a>

#### KSR.jsonrpcs.dispatch() ####

```cpp
int KSR.jsonrpcs.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.dispatch'>📖 kamailio.cfg::function::dispatch()</a>

#### KSR.jsonrpcs.exec() ####

```cpp
int KSR.jsonrpcs.exec(str "scmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.exec'>📖 kamailio.cfg::function::exec()</a>

#### KSR.jsonrpcs.execx() ####

```cpp
int KSR.jsonrpcs.execx(str "scmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.execx'>📖 kamailio.cfg::function::execx()</a>

#### KSR.jsonrpcs.response() ####

```cpp
xval KSR.jsonrpcs.response();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.response'>📖 kamailio.cfg::function::response()</a>

## jwt ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jwt.html'>📖 kamailio.cfg::module::jwt.html</a>

#### KSR.jwt.jwt_generate() ####

```cpp
int KSR.jwt.jwt_generate(str "key", str "alg", str "claims");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_generate'>📖 kamailio.cfg::function::jwt_generate()</a>

#### KSR.jwt.jwt_verify() ####

```cpp
int KSR.jwt.jwt_verify(str "key", str "alg", str "claims", str "jwtval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jwt.html#jwt.f.jwt_verify'>📖 kamailio.cfg::function::jwt_verify()</a>

## kafka ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kafka.html'>📖 kamailio.cfg::module::kafka.html</a>

#### KSR.kafka.send() ####

```cpp
int KSR.kafka.send(str "s_topic", str "s_message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send'>📖 kamailio.cfg::function::send()</a>

#### KSR.kafka.send_key() ####

```cpp
int KSR.kafka.send_key(str "s_topic", str "s_message", str "s_key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send_key'>📖 kamailio.cfg::function::send_key()</a>

## kazoo ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kazoo.html'>📖 kamailio.cfg::module::kazoo.html</a>

#### KSR.kazoo.kazoo_publish() ####

```cpp
int KSR.kazoo.kazoo_publish(str "exchange", str "routing_key", str "payload");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kazoo.html#kazoo.f.kazoo_publish'>📖 kamailio.cfg::function::kazoo_publish()</a>

#### KSR.kazoo.kazoo_subscribe() ####

```cpp
int KSR.kazoo.kazoo_subscribe(str "payload");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kazoo.html#kazoo.f.kazoo_subscribe'>📖 kamailio.cfg::function::kazoo_subscribe()</a>

## keepalive ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html'>📖 kamailio.cfg::module::keepalive.html</a>

#### KSR.keepalive.add_destination() ####

```cpp
int KSR.keepalive.add_destination(str "uri", str "owner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.add_destination'>📖 kamailio.cfg::function::add_destination()</a>

#### KSR.keepalive.del_destination() ####

```cpp
int KSR.keepalive.del_destination(str "uri", str "owner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.del_destination'>📖 kamailio.cfg::function::del_destination()</a>

#### KSR.keepalive.is_alive() ####

```cpp
int KSR.keepalive.is_alive(str "dest");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.is_alive'>📖 kamailio.cfg::function::is_alive()</a>

## kex ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kex.html'>📖 kamailio.cfg::module::kex.html</a>

#### KSR.kex.resetdebug() ####

```cpp
int KSR.kex.resetdebug();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kex.html#kex.f.resetdebug'>📖 kamailio.cfg::function::resetdebug()</a>

#### KSR.kex.setdebug() ####

```cpp
int KSR.kex.setdebug(int lval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kex.html#kex.f.setdebug'>📖 kamailio.cfg::function::setdebug()</a>

## kx ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html'>📖 kamailio.cfg::module::kemi.html</a>

Functions exported by `kemix` module. They aim to provide a convenient way to
retrieve string or integer values for most commonly used variables or runtime
environment attributes.

#### KSR.kx.get_au() ####

```cpp
xval KSR.kx.get_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_au'>📖 kamailio.cfg::function::get_au()</a>

#### KSR.kx.get_body() ####

```cpp
xval KSR.kx.get_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_body'>📖 kamailio.cfg::function::get_body()</a>

Return the body of the SIP message (the value of $rb).

#### KSR.kx.get_bodylen() ####

```cpp
int KSR.kx.get_bodylen();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_bodylen'>📖 kamailio.cfg::function::get_bodylen()</a>

#### KSR.kx.get_callid() ####

```cpp
xval KSR.kx.get_callid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_callid'>📖 kamailio.cfg::function::get_callid()</a>

#### KSR.kx.get_conid() ####

```cpp
int KSR.kx.get_conid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_conid'>📖 kamailio.cfg::function::get_conid()</a>

Return the connection id for TCP, TLS and WebSocket, or -1 if no stream connection corresponds to current SIP message.

#### KSR.kx.get_cturi() ####

```cpp
xval KSR.kx.get_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_cturi'>📖 kamailio.cfg::function::get_cturi()</a>

#### KSR.kx.get_def() ####

```cpp
xval KSR.kx.get_def(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_def'>📖 kamailio.cfg::function::get_def()</a>

#### KSR.kx.get_defn() ####

```cpp
int KSR.kx.get_defn(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_defn'>📖 kamailio.cfg::function::get_defn()</a>

#### KSR.kx.get_duri() ####

```cpp
xval KSR.kx.get_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_duri'>📖 kamailio.cfg::function::get_duri()</a>

Return the value of destination URI ($du).

#### KSR.kx.get_env() ####

```cpp
xval KSR.kx.get_env(str "envname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_env'>📖 kamailio.cfg::function::get_env()</a>

#### KSR.kx.get_envn() ####

```cpp
int KSR.kx.get_envn(str "envname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_envn'>📖 kamailio.cfg::function::get_envn()</a>

#### KSR.kx.get_fhost() ####

```cpp
xval KSR.kx.get_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_fhost'>📖 kamailio.cfg::function::get_fhost()</a>

Return From-URI domain ($fd).

#### KSR.kx.get_furi() ####

```cpp
xval KSR.kx.get_furi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_furi'>📖 kamailio.cfg::function::get_furi()</a>

Return the From URI($fu).

#### KSR.kx.get_fuser() ####

```cpp
xval KSR.kx.get_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_fuser'>📖 kamailio.cfg::function::get_fuser()</a>

Return the From-URI username ($fU).

#### KSR.kx.get_method() ####

```cpp
xval KSR.kx.get_method();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_method'>📖 kamailio.cfg::function::get_method()</a>

Return the SIP method ($rm).

#### KSR.kx.get_msgbuf() ####

```cpp
xval KSR.kx.get_msgbuf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msgbuf'>📖 kamailio.cfg::function::get_msgbuf()</a>

#### KSR.kx.get_msglen() ####

```cpp
int KSR.kx.get_msglen();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msglen'>📖 kamailio.cfg::function::get_msglen()</a>

#### KSR.kx.get_msgtype() ####

```cpp
int KSR.kx.get_msgtype();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_msgtype'>📖 kamailio.cfg::function::get_msgtype()</a>

#### KSR.kx.get_nhuri() ####

```cpp
xval KSR.kx.get_nhuri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_nhuri'>📖 kamailio.cfg::function::get_nhuri()</a>

#### KSR.kx.get_ouri() ####

```cpp
xval KSR.kx.get_ouri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ouri'>📖 kamailio.cfg::function::get_ouri()</a>

#### KSR.kx.get_proto() ####

```cpp
xval KSR.kx.get_proto();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_proto'>📖 kamailio.cfg::function::get_proto()</a>

#### KSR.kx.get_protoid() ####

```cpp
int KSR.kx.get_protoid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_protoid'>📖 kamailio.cfg::function::get_protoid()</a>

#### KSR.kx.get_rcv_sock_name() ####

```cpp
xval KSR.kx.get_rcv_sock_name();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcv_sock_name'>📖 kamailio.cfg::function::get_rcv_sock_name()</a>

#### KSR.kx.get_rcvadvip() ####

```cpp
xval KSR.kx.get_rcvadvip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvadvip'>📖 kamailio.cfg::function::get_rcvadvip()</a>

#### KSR.kx.get_rcvadvport() ####

```cpp
xval KSR.kx.get_rcvadvport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvadvport'>📖 kamailio.cfg::function::get_rcvadvport()</a>

#### KSR.kx.get_rcvip() ####

```cpp
xval KSR.kx.get_rcvip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvip'>📖 kamailio.cfg::function::get_rcvip()</a>

#### KSR.kx.get_rcvport() ####

```cpp
xval KSR.kx.get_rcvport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rcvport'>📖 kamailio.cfg::function::get_rcvport()</a>

#### KSR.kx.get_rhost() ####

```cpp
xval KSR.kx.get_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_rhost'>📖 kamailio.cfg::function::get_rhost()</a>

Return the Request URI host (domain) part ($rd).

#### KSR.kx.get_ruri() ####

```cpp
xval KSR.kx.get_ruri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ruri'>📖 kamailio.cfg::function::get_ruri()</a>

Return the Request URI ($ru).

#### KSR.kx.get_ruser() ####

```cpp
xval KSR.kx.get_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ruser'>📖 kamailio.cfg::function::get_ruser()</a>

Return the Request URI user part ($rU).

#### KSR.kx.get_send_sock() ####

```cpp
xval KSR.kx.get_send_sock();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock'>📖 kamailio.cfg::function::get_send_sock()</a>

#### KSR.kx.get_send_sock_name() ####

```cpp
xval KSR.kx.get_send_sock_name();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock_name'>📖 kamailio.cfg::function::get_send_sock_name()</a>

#### KSR.kx.get_send_sock_port() ####

```cpp
int KSR.kx.get_send_sock_port();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_send_sock_port'>📖 kamailio.cfg::function::get_send_sock_port()</a>

#### KSR.kx.get_srcip() ####

```cpp
xval KSR.kx.get_srcip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcip'>📖 kamailio.cfg::function::get_srcip()</a>

#### KSR.kx.get_srcport() ####

```cpp
xval KSR.kx.get_srcport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcport'>📖 kamailio.cfg::function::get_srcport()</a>

#### KSR.kx.get_srcuri() ####

```cpp
xval KSR.kx.get_srcuri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_srcuri'>📖 kamailio.cfg::function::get_srcuri()</a>

#### KSR.kx.get_status() ####

```cpp
int KSR.kx.get_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_status'>📖 kamailio.cfg::function::get_status()</a>

#### KSR.kx.get_thost() ####

```cpp
xval KSR.kx.get_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_thost'>📖 kamailio.cfg::function::get_thost()</a>

Return the To-URI host (domain) part ($td).

#### KSR.kx.get_timestamp() ####

```cpp
int KSR.kx.get_timestamp();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_timestamp'>📖 kamailio.cfg::function::get_timestamp()</a>

#### KSR.kx.get_turi() ####

```cpp
xval KSR.kx.get_turi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_turi'>📖 kamailio.cfg::function::get_turi()</a>

Return the To URI ($tu).

#### KSR.kx.get_tuser() ####

```cpp
xval KSR.kx.get_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_tuser'>📖 kamailio.cfg::function::get_tuser()</a>

Return the To-URI user part ($tU).

#### KSR.kx.get_ua() ####

```cpp
xval KSR.kx.get_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.get_ua'>📖 kamailio.cfg::function::get_ua()</a>

#### KSR.kx.gete_au() ####

```cpp
xval KSR.kx.gete_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_au'>📖 kamailio.cfg::function::gete_au()</a>

#### KSR.kx.gete_body() ####

```cpp
xval KSR.kx.gete_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_body'>📖 kamailio.cfg::function::gete_body()</a>

#### KSR.kx.gete_cturi() ####

```cpp
xval KSR.kx.gete_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_cturi'>📖 kamailio.cfg::function::gete_cturi()</a>

#### KSR.kx.gete_duri() ####

```cpp
xval KSR.kx.gete_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_duri'>📖 kamailio.cfg::function::gete_duri()</a>

#### KSR.kx.gete_fhost() ####

```cpp
xval KSR.kx.gete_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_fhost'>📖 kamailio.cfg::function::gete_fhost()</a>

#### KSR.kx.gete_fuser() ####

```cpp
xval KSR.kx.gete_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_fuser'>📖 kamailio.cfg::function::gete_fuser()</a>

#### KSR.kx.gete_rhost() ####

```cpp
xval KSR.kx.gete_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_rhost'>📖 kamailio.cfg::function::gete_rhost()</a>

#### KSR.kx.gete_ruser() ####

```cpp
xval KSR.kx.gete_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_ruser'>📖 kamailio.cfg::function::gete_ruser()</a>

#### KSR.kx.gete_thost() ####

```cpp
xval KSR.kx.gete_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_thost'>📖 kamailio.cfg::function::gete_thost()</a>

#### KSR.kx.gete_tuser() ####

```cpp
xval KSR.kx.gete_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_tuser'>📖 kamailio.cfg::function::gete_tuser()</a>

#### KSR.kx.gete_ua() ####

```cpp
xval KSR.kx.gete_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gete_ua'>📖 kamailio.cfg::function::gete_ua()</a>

#### KSR.kx.gets_status() ####

```cpp
xval KSR.kx.gets_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.gets_status'>📖 kamailio.cfg::function::gets_status()</a>

#### KSR.kx.getw_au() ####

```cpp
xval KSR.kx.getw_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_au'>📖 kamailio.cfg::function::getw_au()</a>

#### KSR.kx.getw_body() ####

```cpp
xval KSR.kx.getw_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_body'>📖 kamailio.cfg::function::getw_body()</a>

#### KSR.kx.getw_cturi() ####

```cpp
xval KSR.kx.getw_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_cturi'>📖 kamailio.cfg::function::getw_cturi()</a>

#### KSR.kx.getw_duri() ####

```cpp
xval KSR.kx.getw_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_duri'>📖 kamailio.cfg::function::getw_duri()</a>

#### KSR.kx.getw_fhost() ####

```cpp
xval KSR.kx.getw_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_fhost'>📖 kamailio.cfg::function::getw_fhost()</a>

#### KSR.kx.getw_fuser() ####

```cpp
xval KSR.kx.getw_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_fuser'>📖 kamailio.cfg::function::getw_fuser()</a>

#### KSR.kx.getw_rhost() ####

```cpp
xval KSR.kx.getw_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_rhost'>📖 kamailio.cfg::function::getw_rhost()</a>

#### KSR.kx.getw_ruser() ####

```cpp
xval KSR.kx.getw_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_ruser'>📖 kamailio.cfg::function::getw_ruser()</a>

#### KSR.kx.getw_thost() ####

```cpp
xval KSR.kx.getw_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_thost'>📖 kamailio.cfg::function::getw_thost()</a>

#### KSR.kx.getw_tuser() ####

```cpp
xval KSR.kx.getw_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_tuser'>📖 kamailio.cfg::function::getw_tuser()</a>

#### KSR.kx.getw_ua() ####

```cpp
xval KSR.kx.getw_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.getw_ua'>📖 kamailio.cfg::function::getw_ua()</a>

#### KSR.kx.ifdef() ####

```cpp
bool KSR.kx.ifdef(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.ifdef'>📖 kamailio.cfg::function::ifdef()</a>

#### KSR.kx.ifndef() ####

```cpp
bool KSR.kx.ifndef(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kemi.html#kemi.f.ifndef'>📖 kamailio.cfg::function::ifndef()</a>

## lcr ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html'>📖 kamailio.cfg::module::lcr.html</a>

#### KSR.lcr.defunct_gw() ####

```cpp
int KSR.lcr.defunct_gw(int defunct_period);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.defunct_gw'>📖 kamailio.cfg::function::defunct_gw()</a>

#### KSR.lcr.from_any_gw() ####

```cpp
int KSR.lcr.from_any_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw'>📖 kamailio.cfg::function::from_any_gw()</a>

#### KSR.lcr.from_any_gw_addr() ####

```cpp
int KSR.lcr.from_any_gw_addr(str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr'>📖 kamailio.cfg::function::from_any_gw_addr()</a>

#### KSR.lcr.from_any_gw_addr_port() ####

```cpp
int KSR.lcr.from_any_gw_addr_port(str "addr_str", int transport, int src_port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr_port'>📖 kamailio.cfg::function::from_any_gw_addr_port()</a>

#### KSR.lcr.from_gw() ####

```cpp
int KSR.lcr.from_gw(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw'>📖 kamailio.cfg::function::from_gw()</a>

#### KSR.lcr.from_gw_addr() ####

```cpp
int KSR.lcr.from_gw_addr(int lcr_id, str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr'>📖 kamailio.cfg::function::from_gw_addr()</a>

#### KSR.lcr.from_gw_addr_port() ####

```cpp
int KSR.lcr.from_gw_addr_port(int lcr_id, str "addr_str", int transport, int src_port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr_port'>📖 kamailio.cfg::function::from_gw_addr_port()</a>

#### KSR.lcr.inactivate_gw() ####

```cpp
int KSR.lcr.inactivate_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.inactivate_gw'>📖 kamailio.cfg::function::inactivate_gw()</a>

#### KSR.lcr.load_gws() ####

```cpp
int KSR.lcr.load_gws(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws'>📖 kamailio.cfg::function::load_gws()</a>

#### KSR.lcr.load_gws_furi() ####

```cpp
int KSR.lcr.load_gws_furi(int lcr_id, str "ruri_user", str "from_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_furi'>📖 kamailio.cfg::function::load_gws_furi()</a>

#### KSR.lcr.load_gws_ruser() ####

```cpp
int KSR.lcr.load_gws_ruser(int lcr_id, str "ruri_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_ruser'>📖 kamailio.cfg::function::load_gws_ruser()</a>

#### KSR.lcr.next_gw() ####

```cpp
int KSR.lcr.next_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.next_gw'>📖 kamailio.cfg::function::next_gw()</a>

#### KSR.lcr.to_any_gw() ####

```cpp
int KSR.lcr.to_any_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw'>📖 kamailio.cfg::function::to_any_gw()</a>

#### KSR.lcr.to_any_gw_addr() ####

```cpp
int KSR.lcr.to_any_gw_addr(str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw_addr'>📖 kamailio.cfg::function::to_any_gw_addr()</a>

#### KSR.lcr.to_gw() ####

```cpp
int KSR.lcr.to_gw(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw'>📖 kamailio.cfg::function::to_gw()</a>

#### KSR.lcr.to_gw_addr() ####

```cpp
int KSR.lcr.to_gw_addr(int lcr_id, str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw_addr'>📖 kamailio.cfg::function::to_gw_addr()</a>

## ldap ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ldap.html'>📖 kamailio.cfg::module::ldap.html</a>

#### KSR.ldap.result_next() ####

```cpp
int KSR.ldap.result_next();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ldap.html#ldap.f.result_next'>📖 kamailio.cfg::function::result_next()</a>

#### KSR.ldap.search() ####

```cpp
int KSR.ldap.search(str "ldapurl");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ldap.html#ldap.f.search'>📖 kamailio.cfg::function::search()</a>

## log_custom ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_custom.html'>📖 kamailio.cfg::module::log_custom.html</a>

#### KSR.log_custom.log_udp() ####

```cpp
int KSR.log_custom.log_udp(str "txt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_custom.html#log_custom.f.log_udp'>📖 kamailio.cfg::function::log_udp()</a>

## log_systemd ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_systemd.html'>📖 kamailio.cfg::module::log_systemd.html</a>

#### KSR.log_systemd.sd_journal_print() ####

```cpp
int KSR.log_systemd.sd_journal_print(str "slev", str "stxt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_print'>📖 kamailio.cfg::function::sd_journal_print()</a>

#### KSR.log_systemd.sd_journal_send_xvap() ####

```cpp
int KSR.log_systemd.sd_journal_send_xvap(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_send_xvap'>📖 kamailio.cfg::function::sd_journal_send_xvap()</a>

## lwsc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lwsc.html'>📖 kamailio.cfg::module::lwsc.html</a>

#### KSR.lwsc.lwsc_notify() ####

```cpp
int KSR.lwsc.lwsc_notify(str "wsurl", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lwsc.html#lwsc.f.lwsc_notify'>📖 kamailio.cfg::function::lwsc_notify()</a>

#### KSR.lwsc.lwsc_notify_proto() ####

```cpp
int KSR.lwsc.lwsc_notify_proto(str "wsurl", str "wsproto", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lwsc.html#lwsc.f.lwsc_notify_proto'>📖 kamailio.cfg::function::lwsc_notify_proto()</a>

#### KSR.lwsc.lwsc_request() ####

```cpp
int KSR.lwsc.lwsc_request(str "wsurl", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lwsc.html#lwsc.f.lwsc_request'>📖 kamailio.cfg::function::lwsc_request()</a>

#### KSR.lwsc.lwsc_request_proto() ####

```cpp
int KSR.lwsc.lwsc_request_proto(str "wsurl", str "wsproto", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lwsc.html#lwsc.f.lwsc_request_proto'>📖 kamailio.cfg::function::lwsc_request_proto()</a>

## maxfwd ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/maxfwd.html'>📖 kamailio.cfg::module::maxfwd.html</a>

#### KSR.maxfwd.is_maxfwd_lt() ####

```cpp
int KSR.maxfwd.is_maxfwd_lt(int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/maxfwd.html#maxfwd.f.is_maxfwd_lt'>📖 kamailio.cfg::function::is_maxfwd_lt()</a>

#### KSR.maxfwd.process_maxfwd() ####

```cpp
int KSR.maxfwd.process_maxfwd(int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/maxfwd.html#maxfwd.f.process_maxfwd'>📖 kamailio.cfg::function::process_maxfwd()</a>

## mediaproxy ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html'>📖 kamailio.cfg::module::mediaproxy.html</a>

#### KSR.mediaproxy.end_media_session() ####

```cpp
int KSR.mediaproxy.end_media_session();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.end_media_session'>📖 kamailio.cfg::function::end_media_session()</a>

#### KSR.mediaproxy.engage_media_proxy() ####

```cpp
int KSR.mediaproxy.engage_media_proxy();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.engage_media_proxy'>📖 kamailio.cfg::function::engage_media_proxy()</a>

#### KSR.mediaproxy.use_media_proxy() ####

```cpp
int KSR.mediaproxy.use_media_proxy();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.use_media_proxy'>📖 kamailio.cfg::function::use_media_proxy()</a>

## misc_radius ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html'>📖 kamailio.cfg::module::misc_radius.html</a>

#### KSR.misc_radius.does_uri_exist() ####

```cpp
int KSR.misc_radius.does_uri_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist'>📖 kamailio.cfg::function::does_uri_exist()</a>

#### KSR.misc_radius.does_uri_exist_uval() ####

```cpp
int KSR.misc_radius.does_uri_exist_uval(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist_uval'>📖 kamailio.cfg::function::does_uri_exist_uval()</a>

#### KSR.misc_radius.does_uri_user_exist() ####

```cpp
int KSR.misc_radius.does_uri_user_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist'>📖 kamailio.cfg::function::does_uri_user_exist()</a>

#### KSR.misc_radius.does_uri_user_exist_uval() ####

```cpp
int KSR.misc_radius.does_uri_user_exist_uval(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist_uval'>📖 kamailio.cfg::function::does_uri_user_exist_uval()</a>

#### KSR.misc_radius.is_user_in() ####

```cpp
int KSR.misc_radius.is_user_in(str "user", str "group");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.is_user_in'>📖 kamailio.cfg::function::is_user_in()</a>

#### KSR.misc_radius.load_callee_avps() ####

```cpp
int KSR.misc_radius.load_callee_avps(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_callee_avps'>📖 kamailio.cfg::function::load_callee_avps()</a>

#### KSR.misc_radius.load_caller_avps() ####

```cpp
int KSR.misc_radius.load_caller_avps(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_caller_avps'>📖 kamailio.cfg::function::load_caller_avps()</a>

## mqtt ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html'>📖 kamailio.cfg::module::mqtt.html</a>

#### KSR.mqtt.publish() ####

```cpp
int KSR.mqtt.publish(str "topic", str "payload", int qos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.publish'>📖 kamailio.cfg::function::publish()</a>

#### KSR.mqtt.subscribe() ####

```cpp
int KSR.mqtt.subscribe(str "topic", int qos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.subscribe'>📖 kamailio.cfg::function::subscribe()</a>

#### KSR.mqtt.unsubscribe() ####

```cpp
int KSR.mqtt.unsubscribe(str "topic");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.unsubscribe'>📖 kamailio.cfg::function::unsubscribe()</a>

## mqueue ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html'>📖 kamailio.cfg::module::mqueue.html</a>

#### KSR.mqueue.mq_add() ####

```cpp
int KSR.mqueue.mq_add(str "mq", str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_add'>📖 kamailio.cfg::function::mq_add()</a>

#### KSR.mqueue.mq_fetch() ####

```cpp
int KSR.mqueue.mq_fetch(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_fetch'>📖 kamailio.cfg::function::mq_fetch()</a>

#### KSR.mqueue.mq_pv_free() ####

```cpp
int KSR.mqueue.mq_pv_free(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_pv_free'>📖 kamailio.cfg::function::mq_pv_free()</a>

#### KSR.mqueue.mq_size() ####

```cpp
int KSR.mqueue.mq_size(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_size'>📖 kamailio.cfg::function::mq_size()</a>

#### KSR.mqueue.mqk_get() ####

```cpp
xval KSR.mqueue.mqk_get(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_get'>📖 kamailio.cfg::function::mqk_get()</a>

#### KSR.mqueue.mqk_gete() ####

```cpp
xval KSR.mqueue.mqk_gete(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_gete'>📖 kamailio.cfg::function::mqk_gete()</a>

#### KSR.mqueue.mqk_getw() ####

```cpp
xval KSR.mqueue.mqk_getw(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_getw'>📖 kamailio.cfg::function::mqk_getw()</a>

#### KSR.mqueue.mqv_get() ####

```cpp
xval KSR.mqueue.mqv_get(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_get'>📖 kamailio.cfg::function::mqv_get()</a>

#### KSR.mqueue.mqv_gete() ####

```cpp
xval KSR.mqueue.mqv_gete(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_gete'>📖 kamailio.cfg::function::mqv_gete()</a>

#### KSR.mqueue.mqv_getw() ####

```cpp
xval KSR.mqueue.mqv_getw(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_getw'>📖 kamailio.cfg::function::mqv_getw()</a>

## msilo ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html'>📖 kamailio.cfg::module::msilo.html</a>

#### KSR.msilo.mdump() ####

```cpp
int KSR.msilo.mdump();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mdump'>📖 kamailio.cfg::function::mdump()</a>

#### KSR.msilo.mdump_uri() ####

```cpp
int KSR.msilo.mdump_uri(str "owner_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mdump_uri'>📖 kamailio.cfg::function::mdump_uri()</a>

#### KSR.msilo.mstore() ####

```cpp
int KSR.msilo.mstore();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mstore'>📖 kamailio.cfg::function::mstore()</a>

#### KSR.msilo.mstore_uri() ####

```cpp
int KSR.msilo.mstore_uri(str "owner_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mstore_uri'>📖 kamailio.cfg::function::mstore_uri()</a>

## msrp ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html'>📖 kamailio.cfg::module::msrp.html</a>

#### KSR.msrp.cmap_lookup() ####

```cpp
int KSR.msrp.cmap_lookup();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_lookup'>📖 kamailio.cfg::function::cmap_lookup()</a>

#### KSR.msrp.cmap_save() ####

```cpp
int KSR.msrp.cmap_save();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_save'>📖 kamailio.cfg::function::cmap_save()</a>

#### KSR.msrp.is_reply() ####

```cpp
int KSR.msrp.is_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_reply'>📖 kamailio.cfg::function::is_reply()</a>

#### KSR.msrp.is_request() ####

```cpp
int KSR.msrp.is_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_request'>📖 kamailio.cfg::function::is_request()</a>

#### KSR.msrp.relay() ####

```cpp
int KSR.msrp.relay();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay'>📖 kamailio.cfg::function::relay()</a>

#### KSR.msrp.relay_flags() ####

```cpp
int KSR.msrp.relay_flags(int rtflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay_flags'>📖 kamailio.cfg::function::relay_flags()</a>

#### KSR.msrp.reply() ####

```cpp
int KSR.msrp.reply(str "rcode", str "rtext", str "rhdrs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply'>📖 kamailio.cfg::function::reply()</a>

#### KSR.msrp.reply_flags() ####

```cpp
int KSR.msrp.reply_flags(int rtflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply_flags'>📖 kamailio.cfg::function::reply_flags()</a>

#### KSR.msrp.set_dst() ####

```cpp
int KSR.msrp.set_dst(str "rtaddr", str "rfsock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.set_dst'>📖 kamailio.cfg::function::set_dst()</a>

## mtree ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mtree.html'>📖 kamailio.cfg::module::mtree.html</a>

#### KSR.mtree.mt_match() ####

```cpp
int KSR.mtree.mt_match(str "tname", str "tomatch", int mval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mtree.html#mtree.f.mt_match'>📖 kamailio.cfg::function::mt_match()</a>

## nat_traversal ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html'>📖 kamailio.cfg::module::nat_traversal.html</a>

#### KSR.nat_traversal.client_nat_test() ####

```cpp
int KSR.nat_traversal.client_nat_test(int tests);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.client_nat_test'>📖 kamailio.cfg::function::client_nat_test()</a>

#### KSR.nat_traversal.fix_contact() ####

```cpp
int KSR.nat_traversal.fix_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.fix_contact'>📖 kamailio.cfg::function::fix_contact()</a>

#### KSR.nat_traversal.nat_keepalive() ####

```cpp
int KSR.nat_traversal.nat_keepalive();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.nat_keepalive'>📖 kamailio.cfg::function::nat_keepalive()</a>

## nathelper ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html'>📖 kamailio.cfg::module::nathelper.html</a>

#### KSR.nathelper.add_contact_alias() ####

```cpp
int KSR.nathelper.add_contact_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias'>📖 kamailio.cfg::function::add_contact_alias()</a>

#### KSR.nathelper.add_contact_alias_addr() ####

```cpp
int KSR.nathelper.add_contact_alias_addr(str "ip_str", str "port_str", str "proto_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias_addr'>📖 kamailio.cfg::function::add_contact_alias_addr()</a>

#### KSR.nathelper.add_rcv_param() ####

```cpp
int KSR.nathelper.add_rcv_param(int upos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_rcv_param'>📖 kamailio.cfg::function::add_rcv_param()</a>

#### KSR.nathelper.fix_nated_contact() ####

```cpp
int KSR.nathelper.fix_nated_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_contact'>📖 kamailio.cfg::function::fix_nated_contact()</a>

#### KSR.nathelper.fix_nated_register() ####

```cpp
int KSR.nathelper.fix_nated_register();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_register'>📖 kamailio.cfg::function::fix_nated_register()</a>

#### KSR.nathelper.fix_nated_sdp() ####

```cpp
int KSR.nathelper.fix_nated_sdp(int level);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp'>📖 kamailio.cfg::function::fix_nated_sdp()</a>

#### KSR.nathelper.fix_nated_sdp_ip() ####

```cpp
int KSR.nathelper.fix_nated_sdp_ip(int level, str "ip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp_ip'>📖 kamailio.cfg::function::fix_nated_sdp_ip()</a>

#### KSR.nathelper.handle_ruri_alias() ####

```cpp
int KSR.nathelper.handle_ruri_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias'>📖 kamailio.cfg::function::handle_ruri_alias()</a>

#### KSR.nathelper.handle_ruri_alias_mode() ####

```cpp
int KSR.nathelper.handle_ruri_alias_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias_mode'>📖 kamailio.cfg::function::handle_ruri_alias_mode()</a>

#### KSR.nathelper.is_rfc1918() ####

```cpp
int KSR.nathelper.is_rfc1918(str "address");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.is_rfc1918'>📖 kamailio.cfg::function::is_rfc1918()</a>

#### KSR.nathelper.nat_uac_test() ####

```cpp
int KSR.nathelper.nat_uac_test(int tests);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.nat_uac_test'>📖 kamailio.cfg::function::nat_uac_test()</a>

#### KSR.nathelper.set_alias_to_pv() ####

```cpp
int KSR.nathelper.set_alias_to_pv(str "uri_avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_alias_to_pv'>📖 kamailio.cfg::function::set_alias_to_pv()</a>

#### KSR.nathelper.set_contact_alias() ####

```cpp
int KSR.nathelper.set_contact_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias'>📖 kamailio.cfg::function::set_contact_alias()</a>

#### KSR.nathelper.set_contact_alias_trim() ####

```cpp
int KSR.nathelper.set_contact_alias_trim();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias_trim'>📖 kamailio.cfg::function::set_contact_alias_trim()</a>

## ndb_mongodb ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html'>📖 kamailio.cfg::module::ndb_mongodb.html</a>

#### KSR.ndb_mongodb.exec() ####

```cpp
int KSR.ndb_mongodb.exec(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec'>📖 kamailio.cfg::function::exec()</a>

#### KSR.ndb_mongodb.exec_simple() ####

```cpp
int KSR.ndb_mongodb.exec_simple(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec_simple'>📖 kamailio.cfg::function::exec_simple()</a>

#### KSR.ndb_mongodb.execx() ####

```cpp
int KSR.ndb_mongodb.execx(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.execx'>📖 kamailio.cfg::function::execx()</a>

#### KSR.ndb_mongodb.find() ####

```cpp
int KSR.ndb_mongodb.find(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find'>📖 kamailio.cfg::function::find()</a>

#### KSR.ndb_mongodb.find_one() ####

```cpp
int KSR.ndb_mongodb.find_one(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find_one'>📖 kamailio.cfg::function::find_one()</a>

#### KSR.ndb_mongodb.free_reply() ####

```cpp
int KSR.ndb_mongodb.free_reply(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.free_reply'>📖 kamailio.cfg::function::free_reply()</a>

#### KSR.ndb_mongodb.next_reply() ####

```cpp
int KSR.ndb_mongodb.next_reply(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.next_reply'>📖 kamailio.cfg::function::next_reply()</a>

## ndb_redis ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html'>📖 kamailio.cfg::module::ndb_redis.html</a>

#### KSR.ndb_redis.redis_cmd() ####

```cpp
int KSR.ndb_redis.redis_cmd(str "srv", str "rcmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd'>📖 kamailio.cfg::function::redis_cmd()</a>

#### KSR.ndb_redis.redis_cmd_p1() ####

```cpp
int KSR.ndb_redis.redis_cmd_p1(str "srv", str "rcmd", str "p1", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p1'>📖 kamailio.cfg::function::redis_cmd_p1()</a>

#### KSR.ndb_redis.redis_cmd_p2() ####

```cpp
int KSR.ndb_redis.redis_cmd_p2(str "srv", str "rcmd", str "p1", str "p2", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p2'>📖 kamailio.cfg::function::redis_cmd_p2()</a>

#### KSR.ndb_redis.redis_cmd_p3() ####

```cpp
int KSR.ndb_redis.redis_cmd_p3(str "srv", str "rcmd", str "p1", str "p2", str "p3", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p3'>📖 kamailio.cfg::function::redis_cmd_p3()</a>

#### KSR.ndb_redis.redis_free() ####

```cpp
int KSR.ndb_redis.redis_free(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_free'>📖 kamailio.cfg::function::redis_free()</a>

## path ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html'>📖 kamailio.cfg::module::path.html</a>

#### KSR.path.add_path() ####

```cpp
int KSR.path.add_path();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path'>📖 kamailio.cfg::function::add_path()</a>

#### KSR.path.add_path_received() ####

```cpp
int KSR.path.add_path_received();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received'>📖 kamailio.cfg::function::add_path_received()</a>

#### KSR.path.add_path_received_user() ####

```cpp
int KSR.path.add_path_received_user(str "_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received_user'>📖 kamailio.cfg::function::add_path_received_user()</a>

#### KSR.path.add_path_received_user_params() ####

```cpp
int KSR.path.add_path_received_user_params(str "_user", str "_params");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received_user_params'>📖 kamailio.cfg::function::add_path_received_user_params()</a>

#### KSR.path.add_path_user() ####

```cpp
int KSR.path.add_path_user(str "_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_user'>📖 kamailio.cfg::function::add_path_user()</a>

#### KSR.path.add_path_user_params() ####

```cpp
int KSR.path.add_path_user_params(str "_user", str "_params");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_user_params'>📖 kamailio.cfg::function::add_path_user_params()</a>

## pdt ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pdt.html'>📖 kamailio.cfg::module::pdt.html</a>

#### KSR.pdt.pd_translate() ####

```cpp
int KSR.pdt.pd_translate(str "sd", int md);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pdt.html#pdt.f.pd_translate'>📖 kamailio.cfg::function::pd_translate()</a>

#### KSR.pdt.pprefix2domain() ####

```cpp
int KSR.pdt.pprefix2domain(int m, int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pdt.html#pdt.f.pprefix2domain'>📖 kamailio.cfg::function::pprefix2domain()</a>

## permissions ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html'>📖 kamailio.cfg::module::permissions.html</a>

#### KSR.permissions.allow_address() ####

```cpp
int KSR.permissions.allow_address(int addr_group, str "ips", int port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address'>📖 kamailio.cfg::function::allow_address()</a>

#### KSR.permissions.allow_address_group() ####

```cpp
int KSR.permissions.allow_address_group(str "_addr", int _port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address_group'>📖 kamailio.cfg::function::allow_address_group()</a>

#### KSR.permissions.allow_source_address() ####

```cpp
int KSR.permissions.allow_source_address(int addr_group);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address'>📖 kamailio.cfg::function::allow_source_address()</a>

#### KSR.permissions.allow_source_address_group() ####

```cpp
int KSR.permissions.allow_source_address_group();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address_group'>📖 kamailio.cfg::function::allow_source_address_group()</a>

#### KSR.permissions.allow_trusted() ####

```cpp
int KSR.permissions.allow_trusted();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_trusted'>📖 kamailio.cfg::function::allow_trusted()</a>

## phonenum ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/phonenum.html'>📖 kamailio.cfg::module::phonenum.html</a>

#### KSR.phonenum.match() ####

```cpp
int KSR.phonenum.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/phonenum.html#phonenum.f.match'>📖 kamailio.cfg::function::match()</a>

## pike ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pike.html'>📖 kamailio.cfg::module::pike.html</a>

#### KSR.pike.pike_check_ip() ####

```cpp
int KSR.pike.pike_check_ip(str "strip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pike.html#pike.f.pike_check_ip'>📖 kamailio.cfg::function::pike_check_ip()</a>

#### KSR.pike.pike_check_req() ####

```cpp
int KSR.pike.pike_check_req();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pike.html#pike.f.pike_check_req'>📖 kamailio.cfg::function::pike_check_req()</a>

## pipelimit ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html'>📖 kamailio.cfg::module::pipelimit.html</a>

#### KSR.pipelimit.pl_active() ####

```cpp
int KSR.pipelimit.pl_active(str "pipeid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_active'>📖 kamailio.cfg::function::pl_active()</a>

#### KSR.pipelimit.pl_check() ####

```cpp
int KSR.pipelimit.pl_check(str "pipeid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check'>📖 kamailio.cfg::function::pl_check()</a>

#### KSR.pipelimit.pl_check_limit() ####

```cpp
int KSR.pipelimit.pl_check_limit(str "pipeid", str "alg", int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check_limit'>📖 kamailio.cfg::function::pl_check_limit()</a>

#### KSR.pipelimit.pl_drop() ####

```cpp
int KSR.pipelimit.pl_drop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop'>📖 kamailio.cfg::function::pl_drop()</a>

#### KSR.pipelimit.pl_drop_range() ####

```cpp
int KSR.pipelimit.pl_drop_range(int rmin, int rmax);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_range'>📖 kamailio.cfg::function::pl_drop_range()</a>

#### KSR.pipelimit.pl_drop_retry() ####

```cpp
int KSR.pipelimit.pl_drop_retry(int rafter);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_retry'>📖 kamailio.cfg::function::pl_drop_retry()</a>

## posops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html'>📖 kamailio.cfg::module::posops.html</a>

#### KSR.posops.pos_append() ####

```cpp
int KSR.posops.pos_append(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_append'>📖 kamailio.cfg::function::pos_append()</a>

#### KSR.posops.pos_body_end() ####

```cpp
int KSR.posops.pos_body_end();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_body_end'>📖 kamailio.cfg::function::pos_body_end()</a>

#### KSR.posops.pos_body_start() ####

```cpp
int KSR.posops.pos_body_start();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_body_start'>📖 kamailio.cfg::function::pos_body_start()</a>

#### KSR.posops.pos_find_str() ####

```cpp
int KSR.posops.pos_find_str(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_find_str'>📖 kamailio.cfg::function::pos_find_str()</a>

#### KSR.posops.pos_findi_str() ####

```cpp
int KSR.posops.pos_findi_str(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_findi_str'>📖 kamailio.cfg::function::pos_findi_str()</a>

#### KSR.posops.pos_headers_end() ####

```cpp
int KSR.posops.pos_headers_end();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_headers_end'>📖 kamailio.cfg::function::pos_headers_end()</a>

#### KSR.posops.pos_headers_start() ####

```cpp
int KSR.posops.pos_headers_start();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_headers_start'>📖 kamailio.cfg::function::pos_headers_start()</a>

#### KSR.posops.pos_insert() ####

```cpp
int KSR.posops.pos_insert(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_insert'>📖 kamailio.cfg::function::pos_insert()</a>

#### KSR.posops.pos_rfind_str() ####

```cpp
int KSR.posops.pos_rfind_str(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_rfind_str'>📖 kamailio.cfg::function::pos_rfind_str()</a>

#### KSR.posops.pos_rfindi_str() ####

```cpp
int KSR.posops.pos_rfindi_str(int idx, str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_rfindi_str'>📖 kamailio.cfg::function::pos_rfindi_str()</a>

#### KSR.posops.pos_rm() ####

```cpp
int KSR.posops.pos_rm(int idx, int len);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/posops.html#posops.f.pos_rm'>📖 kamailio.cfg::function::pos_rm()</a>

## prefix_route ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/prefix_route.html'>📖 kamailio.cfg::module::prefix_route.html</a>

#### KSR.prefix_route.prefix_route() ####

```cpp
int KSR.prefix_route.prefix_route(str "ruser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route'>📖 kamailio.cfg::function::prefix_route()</a>

#### KSR.prefix_route.prefix_route_uri() ####

```cpp
int KSR.prefix_route.prefix_route_uri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route_uri'>📖 kamailio.cfg::function::prefix_route_uri()</a>

## presence ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html'>📖 kamailio.cfg::module::presence.html</a>

#### KSR.presence.handle_publish() ####

```cpp
int KSR.presence.handle_publish();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish'>📖 kamailio.cfg::function::handle_publish()</a>

#### KSR.presence.handle_publish_uri() ####

```cpp
int KSR.presence.handle_publish_uri(str "sender_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish_uri'>📖 kamailio.cfg::function::handle_publish_uri()</a>

#### KSR.presence.handle_subscribe() ####

```cpp
int KSR.presence.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe'>📖 kamailio.cfg::function::handle_subscribe()</a>

#### KSR.presence.handle_subscribe_uri() ####

```cpp
int KSR.presence.handle_subscribe_uri(str "wuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe_uri'>📖 kamailio.cfg::function::handle_subscribe_uri()</a>

#### KSR.presence.pres_auth_status() ####

```cpp
int KSR.presence.pres_auth_status(str "watcher_uri", str "presentity_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_auth_status'>📖 kamailio.cfg::function::pres_auth_status()</a>

#### KSR.presence.pres_has_subscribers() ####

```cpp
int KSR.presence.pres_has_subscribers(str "pres_uri", str "wevent");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_has_subscribers'>📖 kamailio.cfg::function::pres_has_subscribers()</a>

#### KSR.presence.pres_refresh_watchers() ####

```cpp
int KSR.presence.pres_refresh_watchers(str "pres", str "event", int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers'>📖 kamailio.cfg::function::pres_refresh_watchers()</a>

#### KSR.presence.pres_refresh_watchers_file() ####

```cpp
int KSR.presence.pres_refresh_watchers_file(str "pres", str "event", int type, str "file_uri", str "filename");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers_file'>📖 kamailio.cfg::function::pres_refresh_watchers_file()</a>

#### KSR.presence.pres_update_watchers() ####

```cpp
int KSR.presence.pres_update_watchers(str "pres_uri", str "event");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_update_watchers'>📖 kamailio.cfg::function::pres_update_watchers()</a>

## presence_xml ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence_xml.html'>📖 kamailio.cfg::module::presence_xml.html</a>

#### KSR.presence_xml.pres_check_activities() ####

```cpp
int KSR.presence_xml.pres_check_activities(str "pres_uri", str "activity");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_activities'>📖 kamailio.cfg::function::pres_check_activities()</a>

#### KSR.presence_xml.pres_check_basic() ####

```cpp
int KSR.presence_xml.pres_check_basic(str "pres_uri", str "status");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_basic'>📖 kamailio.cfg::function::pres_check_basic()</a>

## pua ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua.html'>📖 kamailio.cfg::module::pua.html</a>

#### KSR.pua.pua_set_publish() ####

```cpp
int KSR.pua.pua_set_publish();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua.html#pua.f.pua_set_publish'>📖 kamailio.cfg::function::pua_set_publish()</a>

#### KSR.pua.pua_update_contact() ####

```cpp
int KSR.pua.pua_update_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua.html#pua.f.pua_update_contact'>📖 kamailio.cfg::function::pua_update_contact()</a>

## pua_json ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua_json.html'>📖 kamailio.cfg::module::pua_json.html</a>

#### KSR.pua_json.publish() ####

```cpp
int KSR.pua_json.publish(str "pjson");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua_json.html#pua_json.f.publish'>📖 kamailio.cfg::function::publish()</a>

## pv_headers ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html'>📖 kamailio.cfg::module::pv_headers.html</a>

#### KSR.pv_headers.pvh_append_header() ####

```cpp
int KSR.pv_headers.pvh_append_header(str "hname", str "hvalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_append_header'>📖 kamailio.cfg::function::pvh_append_header()</a>

#### KSR.pv_headers.pvh_apply_headers() ####

```cpp
int KSR.pv_headers.pvh_apply_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_apply_headers'>📖 kamailio.cfg::function::pvh_apply_headers()</a>

#### KSR.pv_headers.pvh_check_header() ####

```cpp
int KSR.pv_headers.pvh_check_header(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_check_header'>📖 kamailio.cfg::function::pvh_check_header()</a>

#### KSR.pv_headers.pvh_collect_headers() ####

```cpp
int KSR.pv_headers.pvh_collect_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_collect_headers'>📖 kamailio.cfg::function::pvh_collect_headers()</a>

#### KSR.pv_headers.pvh_modify_header() ####

```cpp
int KSR.pv_headers.pvh_modify_header(str "hname", str "hvalue", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_modify_header'>📖 kamailio.cfg::function::pvh_modify_header()</a>

#### KSR.pv_headers.pvh_remove_header() ####

```cpp
int KSR.pv_headers.pvh_remove_header(str "hname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_remove_header'>📖 kamailio.cfg::function::pvh_remove_header()</a>

#### KSR.pv_headers.pvh_reset_headers() ####

```cpp
int KSR.pv_headers.pvh_reset_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_reset_headers'>📖 kamailio.cfg::function::pvh_reset_headers()</a>

## pvx ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html'>📖 kamailio.cfg::module::pv.html</a>

#### KSR.pvx.avp_get() ####

```cpp
xval KSR.pvx.avp_get(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_get'>📖 kamailio.cfg::function::avp_get()</a>

#### KSR.pvx.avp_gete() ####

```cpp
xval KSR.pvx.avp_gete(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_gete'>📖 kamailio.cfg::function::avp_gete()</a>

#### KSR.pvx.avp_getw() ####

```cpp
xval KSR.pvx.avp_getw(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_getw'>📖 kamailio.cfg::function::avp_getw()</a>

#### KSR.pvx.avp_is_null() ####

```cpp
int KSR.pvx.avp_is_null(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_is_null'>📖 kamailio.cfg::function::avp_is_null()</a>

#### KSR.pvx.avp_rm() ####

```cpp
int KSR.pvx.avp_rm(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_rm'>📖 kamailio.cfg::function::avp_rm()</a>

#### KSR.pvx.avp_seti() ####

```cpp
int KSR.pvx.avp_seti(str "xname", int vn);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_seti'>📖 kamailio.cfg::function::avp_seti()</a>

#### KSR.pvx.avp_sets() ####

```cpp
int KSR.pvx.avp_sets(str "xname", str "vs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.avp_sets'>📖 kamailio.cfg::function::avp_sets()</a>

#### KSR.pvx.evalx() ####

```cpp
int KSR.pvx.evalx(str "dst", str "fmt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.evalx'>📖 kamailio.cfg::function::evalx()</a>

#### KSR.pvx.pv_var_to_xavp() ####

```cpp
int KSR.pvx.pv_var_to_xavp(str "varname", str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_var_to_xavp'>📖 kamailio.cfg::function::pv_var_to_xavp()</a>

#### KSR.pvx.pv_xavi_print() ####

```cpp
int KSR.pvx.pv_xavi_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavi_print'>📖 kamailio.cfg::function::pv_xavi_print()</a>

#### KSR.pvx.pv_xavp_print() ####

```cpp
int KSR.pvx.pv_xavp_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavp_print'>📖 kamailio.cfg::function::pv_xavp_print()</a>

#### KSR.pvx.pv_xavp_to_var() ####

```cpp
int KSR.pvx.pv_xavp_to_var(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavp_to_var'>📖 kamailio.cfg::function::pv_xavp_to_var()</a>

#### KSR.pvx.pv_xavu_print() ####

```cpp
int KSR.pvx.pv_xavu_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.pv_xavu_print'>📖 kamailio.cfg::function::pv_xavu_print()</a>

#### KSR.pvx.sbranch_append() ####

```cpp
int KSR.pvx.sbranch_append();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_append'>📖 kamailio.cfg::function::sbranch_append()</a>

#### KSR.pvx.sbranch_reset() ####

```cpp
int KSR.pvx.sbranch_reset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_reset'>📖 kamailio.cfg::function::sbranch_reset()</a>

#### KSR.pvx.sbranch_set_ruri() ####

```cpp
int KSR.pvx.sbranch_set_ruri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.sbranch_set_ruri'>📖 kamailio.cfg::function::sbranch_set_ruri()</a>

#### KSR.pvx.shv_get() ####

```cpp
xval KSR.pvx.shv_get(str "vname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_get'>📖 kamailio.cfg::function::shv_get()</a>

#### KSR.pvx.shv_seti() ####

```cpp
int KSR.pvx.shv_seti(str "vname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_seti'>📖 kamailio.cfg::function::shv_seti()</a>

#### KSR.pvx.shv_sets() ####

```cpp
int KSR.pvx.shv_sets(str "vname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.shv_sets'>📖 kamailio.cfg::function::shv_sets()</a>

#### KSR.pvx.var_get() ####

```cpp
xval KSR.pvx.var_get(str "vname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_get'>📖 kamailio.cfg::function::var_get()</a>

#### KSR.pvx.var_seti() ####

```cpp
int KSR.pvx.var_seti(str "vname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_seti'>📖 kamailio.cfg::function::var_seti()</a>

#### KSR.pvx.var_sets() ####

```cpp
int KSR.pvx.var_sets(str "vname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.var_sets'>📖 kamailio.cfg::function::var_sets()</a>

#### KSR.pvx.xavi_child_get() ####

```cpp
xval KSR.pvx.xavi_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_get'>📖 kamailio.cfg::function::xavi_child_get()</a>

#### KSR.pvx.xavi_child_gete() ####

```cpp
xval KSR.pvx.xavi_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_gete'>📖 kamailio.cfg::function::xavi_child_gete()</a>

#### KSR.pvx.xavi_child_getw() ####

```cpp
xval KSR.pvx.xavi_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_getw'>📖 kamailio.cfg::function::xavi_child_getw()</a>

#### KSR.pvx.xavi_child_is_null() ####

```cpp
int KSR.pvx.xavi_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_is_null'>📖 kamailio.cfg::function::xavi_child_is_null()</a>

#### KSR.pvx.xavi_child_rm() ####

```cpp
int KSR.pvx.xavi_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_rm'>📖 kamailio.cfg::function::xavi_child_rm()</a>

#### KSR.pvx.xavi_child_seti() ####

```cpp
int KSR.pvx.xavi_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_seti'>📖 kamailio.cfg::function::xavi_child_seti()</a>

#### KSR.pvx.xavi_child_sets() ####

```cpp
int KSR.pvx.xavi_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_child_sets'>📖 kamailio.cfg::function::xavi_child_sets()</a>

#### KSR.pvx.xavi_get() ####

```cpp
xval KSR.pvx.xavi_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_get'>📖 kamailio.cfg::function::xavi_get()</a>

#### KSR.pvx.xavi_get_keys() ####

```cpp
xval KSR.pvx.xavi_get_keys(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_get_keys'>📖 kamailio.cfg::function::xavi_get_keys()</a>

#### KSR.pvx.xavi_getd() ####

```cpp
xval KSR.pvx.xavi_getd(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getd'>📖 kamailio.cfg::function::xavi_getd()</a>

#### KSR.pvx.xavi_getd_p1() ####

```cpp
xval KSR.pvx.xavi_getd_p1(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getd_p1'>📖 kamailio.cfg::function::xavi_getd_p1()</a>

#### KSR.pvx.xavi_gete() ####

```cpp
xval KSR.pvx.xavi_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_gete'>📖 kamailio.cfg::function::xavi_gete()</a>

#### KSR.pvx.xavi_getw() ####

```cpp
xval KSR.pvx.xavi_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_getw'>📖 kamailio.cfg::function::xavi_getw()</a>

#### KSR.pvx.xavi_is_null() ####

```cpp
int KSR.pvx.xavi_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_is_null'>📖 kamailio.cfg::function::xavi_is_null()</a>

#### KSR.pvx.xavi_rm() ####

```cpp
int KSR.pvx.xavi_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_rm'>📖 kamailio.cfg::function::xavi_rm()</a>

#### KSR.pvx.xavi_seti() ####

```cpp
int KSR.pvx.xavi_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_seti'>📖 kamailio.cfg::function::xavi_seti()</a>

#### KSR.pvx.xavi_sets() ####

```cpp
int KSR.pvx.xavi_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavi_sets'>📖 kamailio.cfg::function::xavi_sets()</a>

#### KSR.pvx.xavp_child_get() ####

```cpp
xval KSR.pvx.xavp_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_get'>📖 kamailio.cfg::function::xavp_child_get()</a>

#### KSR.pvx.xavp_child_gete() ####

```cpp
xval KSR.pvx.xavp_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_gete'>📖 kamailio.cfg::function::xavp_child_gete()</a>

#### KSR.pvx.xavp_child_getw() ####

```cpp
xval KSR.pvx.xavp_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_getw'>📖 kamailio.cfg::function::xavp_child_getw()</a>

#### KSR.pvx.xavp_child_is_null() ####

```cpp
int KSR.pvx.xavp_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_is_null'>📖 kamailio.cfg::function::xavp_child_is_null()</a>

#### KSR.pvx.xavp_child_rm() ####

```cpp
int KSR.pvx.xavp_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_rm'>📖 kamailio.cfg::function::xavp_child_rm()</a>

#### KSR.pvx.xavp_child_seti() ####

```cpp
int KSR.pvx.xavp_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_seti'>📖 kamailio.cfg::function::xavp_child_seti()</a>

#### KSR.pvx.xavp_child_sets() ####

```cpp
int KSR.pvx.xavp_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_child_sets'>📖 kamailio.cfg::function::xavp_child_sets()</a>

#### KSR.pvx.xavp_copy() ####

```cpp
int KSR.pvx.xavp_copy(str "src_name", int src_idx, str "dst_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_copy'>📖 kamailio.cfg::function::xavp_copy()</a>

#### KSR.pvx.xavp_copy_dst() ####

```cpp
int KSR.pvx.xavp_copy_dst(str "src_name", int src_idx, str "dst_name", int dst_idx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_copy_dst'>📖 kamailio.cfg::function::xavp_copy_dst()</a>

#### KSR.pvx.xavp_get() ####

```cpp
xval KSR.pvx.xavp_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_get'>📖 kamailio.cfg::function::xavp_get()</a>

#### KSR.pvx.xavp_get_keys() ####

```cpp
xval KSR.pvx.xavp_get_keys(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_get_keys'>📖 kamailio.cfg::function::xavp_get_keys()</a>

#### KSR.pvx.xavp_getd() ####

```cpp
xval KSR.pvx.xavp_getd(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getd'>📖 kamailio.cfg::function::xavp_getd()</a>

#### KSR.pvx.xavp_getd_p1() ####

```cpp
xval KSR.pvx.xavp_getd_p1(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getd_p1'>📖 kamailio.cfg::function::xavp_getd_p1()</a>

#### KSR.pvx.xavp_gete() ####

```cpp
xval KSR.pvx.xavp_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_gete'>📖 kamailio.cfg::function::xavp_gete()</a>

#### KSR.pvx.xavp_getw() ####

```cpp
xval KSR.pvx.xavp_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_getw'>📖 kamailio.cfg::function::xavp_getw()</a>

#### KSR.pvx.xavp_is_null() ####

```cpp
int KSR.pvx.xavp_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_is_null'>📖 kamailio.cfg::function::xavp_is_null()</a>

#### KSR.pvx.xavp_params_explode() ####

```cpp
int KSR.pvx.xavp_params_explode(str "sparams", str "sxname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_params_explode'>📖 kamailio.cfg::function::xavp_params_explode()</a>

#### KSR.pvx.xavp_params_implode() ####

```cpp
int KSR.pvx.xavp_params_implode(str "sxname", str "svname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_params_implode'>📖 kamailio.cfg::function::xavp_params_implode()</a>

#### KSR.pvx.xavp_rm() ####

```cpp
int KSR.pvx.xavp_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_rm'>📖 kamailio.cfg::function::xavp_rm()</a>

#### KSR.pvx.xavp_seti() ####

```cpp
int KSR.pvx.xavp_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_seti'>📖 kamailio.cfg::function::xavp_seti()</a>

#### KSR.pvx.xavp_sets() ####

```cpp
int KSR.pvx.xavp_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_sets'>📖 kamailio.cfg::function::xavp_sets()</a>

#### KSR.pvx.xavp_slist_explode() ####

```cpp
int KSR.pvx.xavp_slist_explode(str "slist", str "sep", str "mode", str "sxname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavp_slist_explode'>📖 kamailio.cfg::function::xavp_slist_explode()</a>

#### KSR.pvx.xavu_child_get() ####

```cpp
xval KSR.pvx.xavu_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_get'>📖 kamailio.cfg::function::xavu_child_get()</a>

#### KSR.pvx.xavu_child_gete() ####

```cpp
xval KSR.pvx.xavu_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_gete'>📖 kamailio.cfg::function::xavu_child_gete()</a>

#### KSR.pvx.xavu_child_getw() ####

```cpp
xval KSR.pvx.xavu_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_getw'>📖 kamailio.cfg::function::xavu_child_getw()</a>

#### KSR.pvx.xavu_child_is_null() ####

```cpp
int KSR.pvx.xavu_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_is_null'>📖 kamailio.cfg::function::xavu_child_is_null()</a>

#### KSR.pvx.xavu_child_rm() ####

```cpp
int KSR.pvx.xavu_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_rm'>📖 kamailio.cfg::function::xavu_child_rm()</a>

#### KSR.pvx.xavu_child_seti() ####

```cpp
int KSR.pvx.xavu_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_seti'>📖 kamailio.cfg::function::xavu_child_seti()</a>

#### KSR.pvx.xavu_child_sets() ####

```cpp
int KSR.pvx.xavu_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_child_sets'>📖 kamailio.cfg::function::xavu_child_sets()</a>

#### KSR.pvx.xavu_get() ####

```cpp
xval KSR.pvx.xavu_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_get'>📖 kamailio.cfg::function::xavu_get()</a>

#### KSR.pvx.xavu_gete() ####

```cpp
xval KSR.pvx.xavu_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_gete'>📖 kamailio.cfg::function::xavu_gete()</a>

#### KSR.pvx.xavu_getw() ####

```cpp
xval KSR.pvx.xavu_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_getw'>📖 kamailio.cfg::function::xavu_getw()</a>

#### KSR.pvx.xavu_is_null() ####

```cpp
int KSR.pvx.xavu_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_is_null'>📖 kamailio.cfg::function::xavu_is_null()</a>

#### KSR.pvx.xavu_params_explode() ####

```cpp
int KSR.pvx.xavu_params_explode(str "sparams", str "sxname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_params_explode'>📖 kamailio.cfg::function::xavu_params_explode()</a>

#### KSR.pvx.xavu_params_implode() ####

```cpp
int KSR.pvx.xavu_params_implode(str "sxname", str "svname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_params_implode'>📖 kamailio.cfg::function::xavu_params_implode()</a>

#### KSR.pvx.xavu_rm() ####

```cpp
int KSR.pvx.xavu_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_rm'>📖 kamailio.cfg::function::xavu_rm()</a>

#### KSR.pvx.xavu_seti() ####

```cpp
int KSR.pvx.xavu_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_seti'>📖 kamailio.cfg::function::xavu_seti()</a>

#### KSR.pvx.xavu_sets() ####

```cpp
int KSR.pvx.xavu_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv.html#pv.f.xavu_sets'>📖 kamailio.cfg::function::xavu_sets()</a>

## rabbitmq ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rabbitmq.html'>📖 kamailio.cfg::module::rabbitmq.html</a>

#### KSR.rabbitmq.publish() ####

```cpp
int KSR.rabbitmq.publish(str "exchange", str "routingkey", str "contenttype", str "messagebody");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish'>📖 kamailio.cfg::function::publish()</a>

#### KSR.rabbitmq.publish_consume() ####

```cpp
int KSR.rabbitmq.publish_consume(str "exchange", str "routingkey", str "contenttype", str "messagebody", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish_consume'>📖 kamailio.cfg::function::publish_consume()</a>

## regex ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/regex.html'>📖 kamailio.cfg::module::regex.html</a>

#### KSR.regex.pcre_match() ####

```cpp
int KSR.regex.pcre_match(str "string", str "regex");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/regex.html#regex.f.pcre_match'>📖 kamailio.cfg::function::pcre_match()</a>

#### KSR.regex.pcre_match_group() ####

```cpp
int KSR.regex.pcre_match_group(str "string", int num_pcre);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/regex.html#regex.f.pcre_match_group'>📖 kamailio.cfg::function::pcre_match_group()</a>

## registrar ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html'>📖 kamailio.cfg::module::registrar.html</a>

#### KSR.registrar.add_sock_hdr() ####

```cpp
int KSR.registrar.add_sock_hdr(str "hdr_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.add_sock_hdr'>📖 kamailio.cfg::function::add_sock_hdr()</a>

#### KSR.registrar.lookup() ####

```cpp
int KSR.registrar.lookup(str "table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup'>📖 kamailio.cfg::function::lookup()</a>

#### KSR.registrar.lookup_branches() ####

```cpp
int KSR.registrar.lookup_branches(str "_dtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_branches'>📖 kamailio.cfg::function::lookup_branches()</a>

#### KSR.registrar.lookup_to_dset() ####

```cpp
int KSR.registrar.lookup_to_dset(str "table", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_to_dset'>📖 kamailio.cfg::function::lookup_to_dset()</a>

#### KSR.registrar.lookup_uri() ####

```cpp
int KSR.registrar.lookup_uri(str "table", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_uri'>📖 kamailio.cfg::function::lookup_uri()</a>

#### KSR.registrar.reg_fetch_contacts() ####

```cpp
int KSR.registrar.reg_fetch_contacts(str "dtable", str "uri", str "profile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_fetch_contacts'>📖 kamailio.cfg::function::reg_fetch_contacts()</a>

#### KSR.registrar.reg_free_contacts() ####

```cpp
int KSR.registrar.reg_free_contacts(str "profile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_free_contacts'>📖 kamailio.cfg::function::reg_free_contacts()</a>

#### KSR.registrar.reg_send_reply() ####

```cpp
int KSR.registrar.reg_send_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_send_reply'>📖 kamailio.cfg::function::reg_send_reply()</a>

#### KSR.registrar.registered() ####

```cpp
int KSR.registrar.registered(str "table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered'>📖 kamailio.cfg::function::registered()</a>

#### KSR.registrar.registered_action() ####

```cpp
int KSR.registrar.registered_action(str "_dtable", str "_uri", int _f, int _aflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_action'>📖 kamailio.cfg::function::registered_action()</a>

#### KSR.registrar.registered_flags() ####

```cpp
int KSR.registrar.registered_flags(str "_dtable", str "_uri", int _f);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_flags'>📖 kamailio.cfg::function::registered_flags()</a>

#### KSR.registrar.registered_uri() ####

```cpp
int KSR.registrar.registered_uri(str "_dtable", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_uri'>📖 kamailio.cfg::function::registered_uri()</a>

#### KSR.registrar.save() ####

```cpp
int KSR.registrar.save(str "table", int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save'>📖 kamailio.cfg::function::save()</a>

#### KSR.registrar.save_uri() ####

```cpp
int KSR.registrar.save_uri(str "table", int flags, str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save_uri'>📖 kamailio.cfg::function::save_uri()</a>

#### KSR.registrar.set_q_override() ####

```cpp
int KSR.registrar.set_q_override(str "new_q");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.set_q_override'>📖 kamailio.cfg::function::set_q_override()</a>

#### KSR.registrar.unregister() ####

```cpp
int KSR.registrar.unregister(str "_dtable", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister'>📖 kamailio.cfg::function::unregister()</a>

#### KSR.registrar.unregister_ruid() ####

```cpp
int KSR.registrar.unregister_ruid(str "_dtable", str "_uri", str "_ruid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister_ruid'>📖 kamailio.cfg::function::unregister_ruid()</a>

## rls ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html'>📖 kamailio.cfg::module::rls.html</a>

#### KSR.rls.handle_notify() ####

```cpp
int KSR.rls.handle_notify();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_notify'>📖 kamailio.cfg::function::handle_notify()</a>

#### KSR.rls.handle_subscribe() ####

```cpp
int KSR.rls.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe'>📖 kamailio.cfg::function::handle_subscribe()</a>

#### KSR.rls.handle_subscribe_uri() ####

```cpp
int KSR.rls.handle_subscribe_uri(str "wuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe_uri'>📖 kamailio.cfg::function::handle_subscribe_uri()</a>

#### KSR.rls.update_subs() ####

```cpp
int KSR.rls.update_subs(str "uri", str "event");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.update_subs'>📖 kamailio.cfg::function::update_subs()</a>

## rr ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html'>📖 kamailio.cfg::module::rr.html</a>

#### KSR.rr.add_rr_param() ####

```cpp
int KSR.rr.add_rr_param(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.add_rr_param'>📖 kamailio.cfg::function::add_rr_param()</a>

#### KSR.rr.check_route_param() ####

```cpp
int KSR.rr.check_route_param(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.check_route_param'>📖 kamailio.cfg::function::check_route_param()</a>

#### KSR.rr.is_direction() ####

```cpp
int KSR.rr.is_direction(str "dir");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.is_direction'>📖 kamailio.cfg::function::is_direction()</a>

#### KSR.rr.loose_route() ####

```cpp
int KSR.rr.loose_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route'>📖 kamailio.cfg::function::loose_route()</a>

#### KSR.rr.loose_route_mode() ####

```cpp
int KSR.rr.loose_route_mode(int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_mode'>📖 kamailio.cfg::function::loose_route_mode()</a>

#### KSR.rr.loose_route_preloaded() ####

```cpp
int KSR.rr.loose_route_preloaded();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_preloaded'>📖 kamailio.cfg::function::loose_route_preloaded()</a>

#### KSR.rr.next_hop_route() ####

```cpp
int KSR.rr.next_hop_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.next_hop_route'>📖 kamailio.cfg::function::next_hop_route()</a>

#### KSR.rr.record_route() ####

```cpp
int KSR.rr.record_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route'>📖 kamailio.cfg::function::record_route()</a>

#### KSR.rr.record_route_advertised_address() ####

```cpp
int KSR.rr.record_route_advertised_address(str "addr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_advertised_address'>📖 kamailio.cfg::function::record_route_advertised_address()</a>

#### KSR.rr.record_route_params() ####

```cpp
int KSR.rr.record_route_params(str "sparams");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_params'>📖 kamailio.cfg::function::record_route_params()</a>

#### KSR.rr.record_route_preset() ####

```cpp
int KSR.rr.record_route_preset(str "addr1", str "addr2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset'>📖 kamailio.cfg::function::record_route_preset()</a>

#### KSR.rr.record_route_preset_one() ####

```cpp
int KSR.rr.record_route_preset_one(str "addr1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset_one'>📖 kamailio.cfg::function::record_route_preset_one()</a>

#### KSR.rr.remove_record_route() ####

```cpp
int KSR.rr.remove_record_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.remove_record_route'>📖 kamailio.cfg::function::remove_record_route()</a>

## rtjson ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html'>📖 kamailio.cfg::module::rtjson.html</a>

#### KSR.rtjson.init_routes() ####

```cpp
int KSR.rtjson.init_routes(str "srdoc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.init_routes'>📖 kamailio.cfg::function::init_routes()</a>

#### KSR.rtjson.next_route() ####

```cpp
int KSR.rtjson.next_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.next_route'>📖 kamailio.cfg::function::next_route()</a>

#### KSR.rtjson.push_routes() ####

```cpp
int KSR.rtjson.push_routes();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.push_routes'>📖 kamailio.cfg::function::push_routes()</a>

#### KSR.rtjson.update_branch() ####

```cpp
int KSR.rtjson.update_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.update_branch'>📖 kamailio.cfg::function::update_branch()</a>

## rtpengine ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html'>📖 kamailio.cfg::module::rtpengine.html</a>

This module enables media streams to be proxied via an RTPproxy.

#### KSR.rtpengine.block_dtmf() ####

```cpp
int KSR.rtpengine.block_dtmf(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf'>📖 kamailio.cfg::function::block_dtmf()</a>

#### KSR.rtpengine.block_dtmf0() ####

```cpp
int KSR.rtpengine.block_dtmf0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf0'>📖 kamailio.cfg::function::block_dtmf0()</a>

#### KSR.rtpengine.block_media() ####

```cpp
int KSR.rtpengine.block_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media'>📖 kamailio.cfg::function::block_media()</a>

#### KSR.rtpengine.block_media0() ####

```cpp
int KSR.rtpengine.block_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media0'>📖 kamailio.cfg::function::block_media0()</a>

#### KSR.rtpengine.play_media() ####

```cpp
int KSR.rtpengine.play_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.play_media'>📖 kamailio.cfg::function::play_media()</a>

#### KSR.rtpengine.rtpengine_answer() ####

```cpp
int KSR.rtpengine.rtpengine_answer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer'>📖 kamailio.cfg::function::rtpengine_answer()</a>

#### KSR.rtpengine.rtpengine_answer0() ####

```cpp
int KSR.rtpengine.rtpengine_answer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer0'>📖 kamailio.cfg::function::rtpengine_answer0()</a>

#### KSR.rtpengine.rtpengine_delete() ####

```cpp
int KSR.rtpengine.rtpengine_delete(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete'>📖 kamailio.cfg::function::rtpengine_delete()</a>

#### KSR.rtpengine.rtpengine_delete0() ####

```cpp
int KSR.rtpengine.rtpengine_delete0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete0'>📖 kamailio.cfg::function::rtpengine_delete0()</a>

#### KSR.rtpengine.rtpengine_manage() ####

```cpp
int KSR.rtpengine.rtpengine_manage(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage'>📖 kamailio.cfg::function::rtpengine_manage()</a>

#### KSR.rtpengine.rtpengine_manage0() ####

```cpp
int KSR.rtpengine.rtpengine_manage0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage0'>📖 kamailio.cfg::function::rtpengine_manage0()</a>

#### KSR.rtpengine.rtpengine_offer() ####

```cpp
int KSR.rtpengine.rtpengine_offer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer'>📖 kamailio.cfg::function::rtpengine_offer()</a>

#### KSR.rtpengine.rtpengine_offer0() ####

```cpp
int KSR.rtpengine.rtpengine_offer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer0'>📖 kamailio.cfg::function::rtpengine_offer0()</a>

#### KSR.rtpengine.rtpengine_query() ####

```cpp
int KSR.rtpengine.rtpengine_query(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query'>📖 kamailio.cfg::function::rtpengine_query()</a>

#### KSR.rtpengine.rtpengine_query0() ####

```cpp
int KSR.rtpengine.rtpengine_query0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query0'>📖 kamailio.cfg::function::rtpengine_query0()</a>

#### KSR.rtpengine.rtpengine_query_v() ####

```cpp
int KSR.rtpengine.rtpengine_query_v(str "fmt", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query_v'>📖 kamailio.cfg::function::rtpengine_query_v()</a>

#### KSR.rtpengine.set_rtpengine_set() ####

```cpp
int KSR.rtpengine.set_rtpengine_set(int r1);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set'>📖 kamailio.cfg::function::set_rtpengine_set()</a>

#### KSR.rtpengine.set_rtpengine_set2() ####

```cpp
int KSR.rtpengine.set_rtpengine_set2(int r1, int r2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set2'>📖 kamailio.cfg::function::set_rtpengine_set2()</a>

This function is the sibling function to [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set). The original module function is declared as
`set_rtpengine_set(setid[, setid2])`.

In KEMI set_rtpengine_set() takes only the first parameter and set_rtpengine_set2() allows for the second optional parameter to be passed.

```
KSR.rtpengine.set_rtpengine_set2(2, 1);
KSR.rtpengine.rtpengine_offer();
```

Please review the documentation for [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set) for more information.

#### KSR.rtpengine.silence_media() ####

```cpp
int KSR.rtpengine.silence_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.silence_media'>📖 kamailio.cfg::function::silence_media()</a>

#### KSR.rtpengine.silence_media0() ####

```cpp
int KSR.rtpengine.silence_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.silence_media0'>📖 kamailio.cfg::function::silence_media0()</a>

#### KSR.rtpengine.start_recording() ####

```cpp
int KSR.rtpengine.start_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_recording'>📖 kamailio.cfg::function::start_recording()</a>

#### KSR.rtpengine.stop_media() ####

```cpp
int KSR.rtpengine.stop_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media'>📖 kamailio.cfg::function::stop_media()</a>

#### KSR.rtpengine.stop_media0() ####

```cpp
int KSR.rtpengine.stop_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media0'>📖 kamailio.cfg::function::stop_media0()</a>

#### KSR.rtpengine.stop_recording() ####

```cpp
int KSR.rtpengine.stop_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_recording'>📖 kamailio.cfg::function::stop_recording()</a>

#### KSR.rtpengine.unblock_dtmf() ####

```cpp
int KSR.rtpengine.unblock_dtmf(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf'>📖 kamailio.cfg::function::unblock_dtmf()</a>

#### KSR.rtpengine.unblock_dtmf0() ####

```cpp
int KSR.rtpengine.unblock_dtmf0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf0'>📖 kamailio.cfg::function::unblock_dtmf0()</a>

#### KSR.rtpengine.unblock_media() ####

```cpp
int KSR.rtpengine.unblock_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media'>📖 kamailio.cfg::function::unblock_media()</a>

#### KSR.rtpengine.unblock_media0() ####

```cpp
int KSR.rtpengine.unblock_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media0'>📖 kamailio.cfg::function::unblock_media0()</a>

#### KSR.rtpengine.unsilence_media() ####

```cpp
int KSR.rtpengine.unsilence_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unsilence_media'>📖 kamailio.cfg::function::unsilence_media()</a>

#### KSR.rtpengine.unsilence_media0() ####

```cpp
int KSR.rtpengine.unsilence_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unsilence_media0'>📖 kamailio.cfg::function::unsilence_media0()</a>

## rtpproxy ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html'>📖 kamailio.cfg::module::rtpproxy.html</a>

#### KSR.rtpproxy.rtpproxy_answer() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer'>📖 kamailio.cfg::function::rtpproxy_answer()</a>

#### KSR.rtpproxy.rtpproxy_answer0() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer0'>📖 kamailio.cfg::function::rtpproxy_answer0()</a>

#### KSR.rtpproxy.rtpproxy_answer_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer_ip'>📖 kamailio.cfg::function::rtpproxy_answer_ip()</a>

#### KSR.rtpproxy.rtpproxy_destroy() ####

```cpp
int KSR.rtpproxy.rtpproxy_destroy(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy'>📖 kamailio.cfg::function::rtpproxy_destroy()</a>

#### KSR.rtpproxy.rtpproxy_destroy0() ####

```cpp
int KSR.rtpproxy.rtpproxy_destroy0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy0'>📖 kamailio.cfg::function::rtpproxy_destroy0()</a>

#### KSR.rtpproxy.rtpproxy_manage() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage'>📖 kamailio.cfg::function::rtpproxy_manage()</a>

#### KSR.rtpproxy.rtpproxy_manage0() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage0'>📖 kamailio.cfg::function::rtpproxy_manage0()</a>

#### KSR.rtpproxy.rtpproxy_manage_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage_ip'>📖 kamailio.cfg::function::rtpproxy_manage_ip()</a>

#### KSR.rtpproxy.rtpproxy_offer() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer'>📖 kamailio.cfg::function::rtpproxy_offer()</a>

#### KSR.rtpproxy.rtpproxy_offer0() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer0'>📖 kamailio.cfg::function::rtpproxy_offer0()</a>

#### KSR.rtpproxy.rtpproxy_offer_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer_ip'>📖 kamailio.cfg::function::rtpproxy_offer_ip()</a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uac() ####

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uac();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uac'>📖 kamailio.cfg::function::rtpproxy_stop_stream2uac()</a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uas() ####

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uas();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uas'>📖 kamailio.cfg::function::rtpproxy_stop_stream2uas()</a>

#### KSR.rtpproxy.rtpproxy_stream2uac() ####

```cpp
int KSR.rtpproxy.rtpproxy_stream2uac(str "pname", int count);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uac'>📖 kamailio.cfg::function::rtpproxy_stream2uac()</a>

#### KSR.rtpproxy.rtpproxy_stream2uas() ####

```cpp
int KSR.rtpproxy.rtpproxy_stream2uas(str "pname", int count);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uas'>📖 kamailio.cfg::function::rtpproxy_stream2uas()</a>

#### KSR.rtpproxy.set_rtpproxy_set() ####

```cpp
int KSR.rtpproxy.set_rtpproxy_set(int rset);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.set_rtpproxy_set'>📖 kamailio.cfg::function::set_rtpproxy_set()</a>

#### KSR.rtpproxy.start_recording() ####

```cpp
int KSR.rtpproxy.start_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.start_recording'>📖 kamailio.cfg::function::start_recording()</a>

## ruxc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ruxc.html'>📖 kamailio.cfg::module::ruxc.html</a>

#### KSR.ruxc.http_delete() ####

```cpp
int KSR.ruxc.http_delete(str "url", str "body", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ruxc.html#ruxc.f.http_delete'>📖 kamailio.cfg::function::http_delete()</a>

#### KSR.ruxc.http_get() ####

```cpp
int KSR.ruxc.http_get(str "url", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ruxc.html#ruxc.f.http_get'>📖 kamailio.cfg::function::http_get()</a>

#### KSR.ruxc.http_post() ####

```cpp
int KSR.ruxc.http_post(str "url", str "body", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ruxc.html#ruxc.f.http_post'>📖 kamailio.cfg::function::http_post()</a>

## sanity ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html'>📖 kamailio.cfg::module::sanity.html</a>

#### KSR.sanity.sanity_check() ####

```cpp
int KSR.sanity.sanity_check(int mflags, int uflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check'>📖 kamailio.cfg::function::sanity_check()</a>

#### KSR.sanity.sanity_check_defaults() ####

```cpp
int KSR.sanity.sanity_check_defaults();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check_defaults'>📖 kamailio.cfg::function::sanity_check_defaults()</a>

#### KSR.sanity.sanity_reply() ####

```cpp
int KSR.sanity.sanity_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_reply'>📖 kamailio.cfg::function::sanity_reply()</a>

## sca ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html'>📖 kamailio.cfg::module::sca.html</a>

#### KSR.sca.call_info_update() ####

```cpp
int KSR.sca.call_info_update(int update_mask, str "uri_to", str "uri_from");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update'>📖 kamailio.cfg::function::call_info_update()</a>

#### KSR.sca.call_info_update_default() ####

```cpp
int KSR.sca.call_info_update_default();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_default'>📖 kamailio.cfg::function::call_info_update_default()</a>

#### KSR.sca.call_info_update_mask() ####

```cpp
int KSR.sca.call_info_update_mask(int umask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_mask'>📖 kamailio.cfg::function::call_info_update_mask()</a>

#### KSR.sca.call_info_update_turi() ####

```cpp
int KSR.sca.call_info_update_turi(int umask, str "sto");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_turi'>📖 kamailio.cfg::function::call_info_update_turi()</a>

#### KSR.sca.handle_subscribe() ####

```cpp
int KSR.sca.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.handle_subscribe'>📖 kamailio.cfg::function::handle_subscribe()</a>

## sdpops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html'>📖 kamailio.cfg::module::sdpops.html</a>

#### KSR.sdpops.keep_codecs_by_id() ####

```cpp
int KSR.sdpops.keep_codecs_by_id(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_id'>📖 kamailio.cfg::function::keep_codecs_by_id()</a>

#### KSR.sdpops.keep_codecs_by_name() ####

```cpp
int KSR.sdpops.keep_codecs_by_name(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_name'>📖 kamailio.cfg::function::keep_codecs_by_name()</a>

#### KSR.sdpops.remove_codecs_by_id() ####

```cpp
int KSR.sdpops.remove_codecs_by_id(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_id'>📖 kamailio.cfg::function::remove_codecs_by_id()</a>

#### KSR.sdpops.remove_codecs_by_name() ####

```cpp
int KSR.sdpops.remove_codecs_by_name(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_name'>📖 kamailio.cfg::function::remove_codecs_by_name()</a>

#### KSR.sdpops.remove_line_by_prefix() ####

```cpp
int KSR.sdpops.remove_line_by_prefix(str "prefix", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_line_by_prefix'>📖 kamailio.cfg::function::remove_line_by_prefix()</a>

#### KSR.sdpops.remove_media() ####

```cpp
int KSR.sdpops.remove_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_media'>📖 kamailio.cfg::function::remove_media()</a>

#### KSR.sdpops.sdp_content() ####

```cpp
int KSR.sdpops.sdp_content();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content'>📖 kamailio.cfg::function::sdp_content()</a>

#### KSR.sdpops.sdp_content_flags() ####

```cpp
int KSR.sdpops.sdp_content_flags(int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content_flags'>📖 kamailio.cfg::function::sdp_content_flags()</a>

#### KSR.sdpops.sdp_get() ####

```cpp
int KSR.sdpops.sdp_get(str "avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get'>📖 kamailio.cfg::function::sdp_get()</a>

#### KSR.sdpops.sdp_get_line_startswith() ####

```cpp
int KSR.sdpops.sdp_get_line_startswith(str "aname", str "sline");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get_line_startswith'>📖 kamailio.cfg::function::sdp_get_line_startswith()</a>

#### KSR.sdpops.sdp_print() ####

```cpp
int KSR.sdpops.sdp_print(int llevel);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_print'>📖 kamailio.cfg::function::sdp_print()</a>

#### KSR.sdpops.sdp_transport() ####

```cpp
int KSR.sdpops.sdp_transport(str "avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_transport'>📖 kamailio.cfg::function::sdp_transport()</a>

#### KSR.sdpops.sdp_with_active_media() ####

```cpp
int KSR.sdpops.sdp_with_active_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_active_media'>📖 kamailio.cfg::function::sdp_with_active_media()</a>

#### KSR.sdpops.sdp_with_codecs_by_id() ####

```cpp
int KSR.sdpops.sdp_with_codecs_by_id(str "codecs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_id'>📖 kamailio.cfg::function::sdp_with_codecs_by_id()</a>

#### KSR.sdpops.sdp_with_codecs_by_name() ####

```cpp
int KSR.sdpops.sdp_with_codecs_by_name(str "codecs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_name'>📖 kamailio.cfg::function::sdp_with_codecs_by_name()</a>

#### KSR.sdpops.sdp_with_ice() ####

```cpp
int KSR.sdpops.sdp_with_ice();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_ice'>📖 kamailio.cfg::function::sdp_with_ice()</a>

#### KSR.sdpops.sdp_with_media() ####

```cpp
int KSR.sdpops.sdp_with_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_media'>📖 kamailio.cfg::function::sdp_with_media()</a>

#### KSR.sdpops.sdp_with_transport() ####

```cpp
int KSR.sdpops.sdp_with_transport(str "transport");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport'>📖 kamailio.cfg::function::sdp_with_transport()</a>

#### KSR.sdpops.sdp_with_transport_like() ####

```cpp
int KSR.sdpops.sdp_with_transport_like(str "transport");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport_like'>📖 kamailio.cfg::function::sdp_with_transport_like()</a>

## secsipid ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html'>📖 kamailio.cfg::module::secsipid.html</a>

#### KSR.secsipid.result_str() ####

```cpp
int KSR.secsipid.result_str(str "attrname", str "avpname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.result_str'>📖 kamailio.cfg::function::result_str()</a>

#### KSR.secsipid.secsipid_add_identity() ####

```cpp
int KSR.secsipid.secsipid_add_identity(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_add_identity'>📖 kamailio.cfg::function::secsipid_add_identity()</a>

#### KSR.secsipid.secsipid_build_identity() ####

```cpp
int KSR.secsipid.secsipid_build_identity(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_build_identity'>📖 kamailio.cfg::function::secsipid_build_identity()</a>

#### KSR.secsipid.secsipid_build_identity_prvkey() ####

```cpp
int KSR.secsipid.secsipid_build_identity_prvkey(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keydata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_build_identity_prvkey'>📖 kamailio.cfg::function::secsipid_build_identity_prvkey()</a>

#### KSR.secsipid.secsipid_check() ####

```cpp
int KSR.secsipid.secsipid_check(str "sidentity", str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check'>📖 kamailio.cfg::function::secsipid_check()</a>

#### KSR.secsipid.secsipid_check_identity() ####

```cpp
int KSR.secsipid.secsipid_check_identity(str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity'>📖 kamailio.cfg::function::secsipid_check_identity()</a>

#### KSR.secsipid.secsipid_check_identity_pubkey() ####

```cpp
int KSR.secsipid.secsipid_check_identity_pubkey(str "keyval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity_pubkey'>📖 kamailio.cfg::function::secsipid_check_identity_pubkey()</a>

#### KSR.secsipid.secsipid_get_url() ####

```cpp
xval KSR.secsipid.secsipid_get_url(str "surl");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_get_url'>📖 kamailio.cfg::function::secsipid_get_url()</a>

#### KSR.secsipid.secsipid_get_val() ####

```cpp
xval KSR.secsipid.secsipid_get_val();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_get_val'>📖 kamailio.cfg::function::secsipid_get_val()</a>

## sipcapture ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html'>📖 kamailio.cfg::module::sipcapture.html</a>

#### KSR.sipcapture.float2int() ####

```cpp
int KSR.sipcapture.float2int(str "_val", str "_coof");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.float2int'>📖 kamailio.cfg::function::float2int()</a>

#### KSR.sipcapture.report_capture() ####

```cpp
int KSR.sipcapture.report_capture(str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture'>📖 kamailio.cfg::function::report_capture()</a>

#### KSR.sipcapture.report_capture_cid() ####

```cpp
int KSR.sipcapture.report_capture_cid(str "_table", str "_cid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_cid'>📖 kamailio.cfg::function::report_capture_cid()</a>

#### KSR.sipcapture.report_capture_data() ####

```cpp
int KSR.sipcapture.report_capture_data(str "_table", str "_cid", str "_data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_data'>📖 kamailio.cfg::function::report_capture_data()</a>

#### KSR.sipcapture.sip_capture() ####

```cpp
int KSR.sipcapture.sip_capture();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture'>📖 kamailio.cfg::function::sip_capture()</a>

#### KSR.sipcapture.sip_capture_forward() ####

```cpp
int KSR.sipcapture.sip_capture_forward(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_forward'>📖 kamailio.cfg::function::sip_capture_forward()</a>

#### KSR.sipcapture.sip_capture_mode() ####

```cpp
int KSR.sipcapture.sip_capture_mode(str "_table", str "_cmdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_mode'>📖 kamailio.cfg::function::sip_capture_mode()</a>

#### KSR.sipcapture.sip_capture_table() ####

```cpp
int KSR.sipcapture.sip_capture_table(str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_table'>📖 kamailio.cfg::function::sip_capture_table()</a>

## sipdump ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html'>📖 kamailio.cfg::module::sipdump.html</a>

#### KSR.sipdump.get_buf() ####

```cpp
xval KSR.sipdump.get_buf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_buf'>📖 kamailio.cfg::function::get_buf()</a>

#### KSR.sipdump.get_dst_ip() ####

```cpp
xval KSR.sipdump.get_dst_ip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_dst_ip'>📖 kamailio.cfg::function::get_dst_ip()</a>

#### KSR.sipdump.get_src_ip() ####

```cpp
xval KSR.sipdump.get_src_ip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_src_ip'>📖 kamailio.cfg::function::get_src_ip()</a>

#### KSR.sipdump.get_tag() ####

```cpp
xval KSR.sipdump.get_tag();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_tag'>📖 kamailio.cfg::function::get_tag()</a>

#### KSR.sipdump.send() ####

```cpp
int KSR.sipdump.send(str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.send'>📖 kamailio.cfg::function::send()</a>

## sipjson ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipjson.html'>📖 kamailio.cfg::module::sipjson.html</a>

#### KSR.sipjson.sj_serialize() ####

```cpp
int KSR.sipjson.sj_serialize(str "smode", str "pvn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipjson.html#sipjson.f.sj_serialize'>📖 kamailio.cfg::function::sj_serialize()</a>

## siptrace ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html'>📖 kamailio.cfg::module::siptrace.html</a>

#### KSR.siptrace.hlog() ####

```cpp
int KSR.siptrace.hlog(str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog'>📖 kamailio.cfg::function::hlog()</a>

#### KSR.siptrace.hlog_cid() ####

```cpp
int KSR.siptrace.hlog_cid(str "correlationid", str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog_cid'>📖 kamailio.cfg::function::hlog_cid()</a>

#### KSR.siptrace.sip_trace() ####

```cpp
int KSR.siptrace.sip_trace();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace'>📖 kamailio.cfg::function::sip_trace()</a>

#### KSR.siptrace.sip_trace_dst() ####

```cpp
int KSR.siptrace.sip_trace_dst(str "duri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst'>📖 kamailio.cfg::function::sip_trace_dst()</a>

#### KSR.siptrace.sip_trace_dst_cid() ####

```cpp
int KSR.siptrace.sip_trace_dst_cid(str "duri", str "cid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid'>📖 kamailio.cfg::function::sip_trace_dst_cid()</a>

#### KSR.siptrace.sip_trace_dst_cid_type() ####

```cpp
int KSR.siptrace.sip_trace_dst_cid_type(str "duri", str "cid", str "sflag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid_type'>📖 kamailio.cfg::function::sip_trace_dst_cid_type()</a>

#### KSR.siptrace.sip_trace_mode() ####

```cpp
int KSR.siptrace.sip_trace_mode(str "smode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_mode'>📖 kamailio.cfg::function::sip_trace_mode()</a>

## siputils ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html'>📖 kamailio.cfg::module::siputils.html</a>

#### KSR.siputils.cmp_aor() ####

```cpp
int KSR.siputils.cmp_aor(str "uri1", str "uri2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_aor'>📖 kamailio.cfg::function::cmp_aor()</a>

#### KSR.siputils.cmp_hdr_name() ####

```cpp
int KSR.siputils.cmp_hdr_name(str "shname1", str "shname2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_hdr_name'>📖 kamailio.cfg::function::cmp_hdr_name()</a>

#### KSR.siputils.cmp_uri() ####

```cpp
int KSR.siputils.cmp_uri(str "uri1", str "uri2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.cmp_uri'>📖 kamailio.cfg::function::cmp_uri()</a>

#### KSR.siputils.contact_param_decode() ####

```cpp
int KSR.siputils.contact_param_decode(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode'>📖 kamailio.cfg::function::contact_param_decode()</a>

#### KSR.siputils.contact_param_decode_ruri() ####

```cpp
int KSR.siputils.contact_param_decode_ruri(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode_ruri'>📖 kamailio.cfg::function::contact_param_decode_ruri()</a>

#### KSR.siputils.contact_param_encode() ####

```cpp
int KSR.siputils.contact_param_encode(str "nparam", str "saddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_encode'>📖 kamailio.cfg::function::contact_param_encode()</a>

#### KSR.siputils.contact_param_rm() ####

```cpp
int KSR.siputils.contact_param_rm(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_rm'>📖 kamailio.cfg::function::contact_param_rm()</a>

#### KSR.siputils.decode_contact() ####

```cpp
int KSR.siputils.decode_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact'>📖 kamailio.cfg::function::decode_contact()</a>

#### KSR.siputils.decode_contact_header() ####

```cpp
int KSR.siputils.decode_contact_header();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact_header'>📖 kamailio.cfg::function::decode_contact_header()</a>

#### KSR.siputils.encode_contact() ####

```cpp
int KSR.siputils.encode_contact(str "eprefix", str "eaddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.encode_contact'>📖 kamailio.cfg::function::encode_contact()</a>

#### KSR.siputils.has_totag() ####

```cpp
int KSR.siputils.has_totag();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.has_totag'>📖 kamailio.cfg::function::has_totag()</a>

#### KSR.siputils.hdr_date_check() ####

```cpp
int KSR.siputils.hdr_date_check(int tdiff);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.hdr_date_check'>📖 kamailio.cfg::function::hdr_date_check()</a>

#### KSR.siputils.is_alphanum() ####

```cpp
int KSR.siputils.is_alphanum(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanum'>📖 kamailio.cfg::function::is_alphanum()</a>

#### KSR.siputils.is_alphanumex() ####

```cpp
int KSR.siputils.is_alphanumex(str "tval", str "eset");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanumex'>📖 kamailio.cfg::function::is_alphanumex()</a>

#### KSR.siputils.is_first_hop() ####

```cpp
int KSR.siputils.is_first_hop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop'>📖 kamailio.cfg::function::is_first_hop()</a>

#### KSR.siputils.is_first_hop_mode() ####

```cpp
int KSR.siputils.is_first_hop_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop_mode'>📖 kamailio.cfg::function::is_first_hop_mode()</a>

#### KSR.siputils.is_numeric() ####

```cpp
int KSR.siputils.is_numeric(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_numeric'>📖 kamailio.cfg::function::is_numeric()</a>

#### KSR.siputils.is_reply() ####

```cpp
int KSR.siputils.is_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_reply'>📖 kamailio.cfg::function::is_reply()</a>

#### KSR.siputils.is_request() ####

```cpp
int KSR.siputils.is_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_request'>📖 kamailio.cfg::function::is_request()</a>

#### KSR.siputils.is_tel_number() ####

```cpp
int KSR.siputils.is_tel_number(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_tel_number'>📖 kamailio.cfg::function::is_tel_number()</a>

#### KSR.siputils.is_uri() ####

```cpp
int KSR.siputils.is_uri(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_uri'>📖 kamailio.cfg::function::is_uri()</a>

#### KSR.siputils.is_user() ####

```cpp
int KSR.siputils.is_user(str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_user'>📖 kamailio.cfg::function::is_user()</a>

#### KSR.siputils.options_reply() ####

```cpp
int KSR.siputils.options_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.options_reply'>📖 kamailio.cfg::function::options_reply()</a>

#### KSR.siputils.uri_param() ####

```cpp
int KSR.siputils.uri_param(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param'>📖 kamailio.cfg::function::uri_param()</a>

#### KSR.siputils.uri_param_any() ####

```cpp
int KSR.siputils.uri_param_any(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_any'>📖 kamailio.cfg::function::uri_param_any()</a>

#### KSR.siputils.uri_param_rm() ####

```cpp
int KSR.siputils.uri_param_rm(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_rm'>📖 kamailio.cfg::function::uri_param_rm()</a>

#### KSR.siputils.uri_param_value() ####

```cpp
int KSR.siputils.uri_param_value(str "sparam", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_value'>📖 kamailio.cfg::function::uri_param_value()</a>

## sl ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html'>📖 kamailio.cfg::module::sl.html</a>

#### KSR.sl.send_reply() ####

```cpp
int KSR.sl.send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply'>📖 kamailio.cfg::function::send_reply()</a>

#### KSR.sl.send_reply_mode() ####

```cpp
int KSR.sl.send_reply_mode(int code, str "reason", int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply_mode'>📖 kamailio.cfg::function::send_reply_mode()</a>

#### KSR.sl.sl_forward_reply() ####

```cpp
int KSR.sl.sl_forward_reply(str "code", str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_forward_reply'>📖 kamailio.cfg::function::sl_forward_reply()</a>

#### KSR.sl.sl_reply_error() ####

```cpp
int KSR.sl.sl_reply_error();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_reply_error'>📖 kamailio.cfg::function::sl_reply_error()</a>

#### KSR.sl.sl_send_reply() ####

```cpp
int KSR.sl.sl_send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_send_reply'>📖 kamailio.cfg::function::sl_send_reply()</a>

## slack ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/slack.html'>📖 kamailio.cfg::module::slack.html</a>

#### KSR.slack.slack_send() ####

```cpp
int KSR.slack.slack_send(str "slmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/slack.html#slack.f.slack_send'>📖 kamailio.cfg::function::slack_send()</a>

## speeddial ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/speeddial.html'>📖 kamailio.cfg::module::speeddial.html</a>

#### KSR.speeddial.lookup() ####

```cpp
int KSR.speeddial.lookup(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup'>📖 kamailio.cfg::function::lookup()</a>

#### KSR.speeddial.lookup_owner() ####

```cpp
int KSR.speeddial.lookup_owner(str "stable", str "sowner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup_owner'>📖 kamailio.cfg::function::lookup_owner()</a>

## sqlops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html'>📖 kamailio.cfg::module::sqlops.html</a>

#### KSR.sqlops.sql_is_null() ####

```cpp
int KSR.sqlops.sql_is_null(str "sres", int i, int j);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_is_null'>📖 kamailio.cfg::function::sql_is_null()</a>

#### KSR.sqlops.sql_num_columns() ####

```cpp
int KSR.sqlops.sql_num_columns(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_columns'>📖 kamailio.cfg::function::sql_num_columns()</a>

#### KSR.sqlops.sql_num_rows() ####

```cpp
int KSR.sqlops.sql_num_rows(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_rows'>📖 kamailio.cfg::function::sql_num_rows()</a>

#### KSR.sqlops.sql_pvquery() ####

```cpp
int KSR.sqlops.sql_pvquery(str "scon", str "squery", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_pvquery'>📖 kamailio.cfg::function::sql_pvquery()</a>

#### KSR.sqlops.sql_query() ####

```cpp
int KSR.sqlops.sql_query(str "scon", str "squery", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query'>📖 kamailio.cfg::function::sql_query()</a>

#### KSR.sqlops.sql_query_async() ####

```cpp
int KSR.sqlops.sql_query_async(str "scon", str "squery");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query_async'>📖 kamailio.cfg::function::sql_query_async()</a>

#### KSR.sqlops.sql_result_free() ####

```cpp
int KSR.sqlops.sql_result_free(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_free'>📖 kamailio.cfg::function::sql_result_free()</a>

#### KSR.sqlops.sql_result_get() ####

```cpp
xval KSR.sqlops.sql_result_get(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_get'>📖 kamailio.cfg::function::sql_result_get()</a>

#### KSR.sqlops.sql_result_gete() ####

```cpp
xval KSR.sqlops.sql_result_gete(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_gete'>📖 kamailio.cfg::function::sql_result_gete()</a>

#### KSR.sqlops.sql_result_getz() ####

```cpp
xval KSR.sqlops.sql_result_getz(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_getz'>📖 kamailio.cfg::function::sql_result_getz()</a>

#### KSR.sqlops.sql_xquery() ####

```cpp
int KSR.sqlops.sql_xquery(str "scon", str "squery", str "xavp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_xquery'>📖 kamailio.cfg::function::sql_xquery()</a>

## ss7ops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ss7ops.html'>📖 kamailio.cfg::module::ss7ops.html</a>

#### KSR.ss7ops.isup_to_json() ####

```cpp
int KSR.ss7ops.isup_to_json(int proto);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ss7ops.html#ss7ops.f.isup_to_json'>📖 kamailio.cfg::function::isup_to_json()</a>

## sst ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sst.html'>📖 kamailio.cfg::module::sst.html</a>

#### KSR.sst.sst_check_min() ####

```cpp
int KSR.sst.sst_check_min(int flag);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sst.html#sst.f.sst_check_min'>📖 kamailio.cfg::function::sst_check_min()</a>

## statistics ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statistics.html'>📖 kamailio.cfg::module::statistics.html</a>

#### KSR.statistics.reset_stat() ####

```cpp
int KSR.statistics.reset_stat(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statistics.html#statistics.f.reset_stat'>📖 kamailio.cfg::function::reset_stat()</a>

#### KSR.statistics.update_stat() ####

```cpp
int KSR.statistics.update_stat(str "sname", int sval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statistics.html#statistics.f.update_stat'>📖 kamailio.cfg::function::update_stat()</a>

## statsc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsc.html'>📖 kamailio.cfg::module::statsc.html</a>

#### KSR.statsc.statsc_reset() ####

```cpp
int KSR.statsc.statsc_reset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsc.html#statsc.f.statsc_reset'>📖 kamailio.cfg::function::statsc_reset()</a>

## statsd ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html'>📖 kamailio.cfg::module::statsd.html</a>

#### KSR.statsd.statsd_decr() ####

```cpp
int KSR.statsd.statsd_decr(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_decr'>📖 kamailio.cfg::function::statsd_decr()</a>

#### KSR.statsd.statsd_gauge() ####

```cpp
int KSR.statsd.statsd_gauge(str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_gauge'>📖 kamailio.cfg::function::statsd_gauge()</a>

#### KSR.statsd.statsd_histogram() ####

```cpp
int KSR.statsd.statsd_histogram(str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_histogram'>📖 kamailio.cfg::function::statsd_histogram()</a>

#### KSR.statsd.statsd_incr() ####

```cpp
int KSR.statsd.statsd_incr(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_incr'>📖 kamailio.cfg::function::statsd_incr()</a>

#### KSR.statsd.statsd_set() ####

```cpp
int KSR.statsd.statsd_set(str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_set'>📖 kamailio.cfg::function::statsd_set()</a>

#### KSR.statsd.statsd_start() ####

```cpp
int KSR.statsd.statsd_start(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_start'>📖 kamailio.cfg::function::statsd_start()</a>

#### KSR.statsd.statsd_stop() ####

```cpp
int KSR.statsd.statsd_stop(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_stop'>📖 kamailio.cfg::function::statsd_stop()</a>

## stirshaken ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html'>📖 kamailio.cfg::module::stirshaken.html</a>

#### KSR.stirshaken.stirshaken_add_identity() ####

```cpp
int KSR.stirshaken.stirshaken_add_identity(str "x5u", str "attest", str "origtn_val", str "desttn_val", str "origid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_add_identity'>📖 kamailio.cfg::function::stirshaken_add_identity()</a>

#### KSR.stirshaken.stirshaken_add_identity_with_key() ####

```cpp
int KSR.stirshaken.stirshaken_add_identity_with_key(str "x5u", str "attest", str "origtn_val", str "desttn_val", str "origid", str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_add_identity_with_key'>📖 kamailio.cfg::function::stirshaken_add_identity_with_key()</a>

#### KSR.stirshaken.stirshaken_check_identity() ####

```cpp
int KSR.stirshaken.stirshaken_check_identity();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity'>📖 kamailio.cfg::function::stirshaken_check_identity()</a>

#### KSR.stirshaken.stirshaken_check_identity_with_cert() ####

```cpp
int KSR.stirshaken.stirshaken_check_identity_with_cert(str "cert_path");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity_with_cert'>📖 kamailio.cfg::function::stirshaken_check_identity_with_cert()</a>

#### KSR.stirshaken.stirshaken_check_identity_with_key() ####

```cpp
int KSR.stirshaken.stirshaken_check_identity_with_key(str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/stirshaken.html#stirshaken.f.stirshaken_check_identity_with_key'>📖 kamailio.cfg::function::stirshaken_check_identity_with_key()</a>

## sworker ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sworker.html'>📖 kamailio.cfg::module::sworker.html</a>

#### KSR.sworker.active() ####

```cpp
int KSR.sworker.active();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sworker.html#sworker.f.active'>📖 kamailio.cfg::function::active()</a>

#### KSR.sworker.task() ####

```cpp
int KSR.sworker.task(str "gname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sworker.html#sworker.f.task'>📖 kamailio.cfg::function::task()</a>

## tcpops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html'>📖 kamailio.cfg::module::tcpops.html</a>

#### KSR.tcpops.tcp_close_connection() ####

```cpp
int KSR.tcpops.tcp_close_connection();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_close_connection'>📖 kamailio.cfg::function::tcp_close_connection()</a>

#### KSR.tcpops.tcp_close_connection_id() ####

```cpp
int KSR.tcpops.tcp_close_connection_id(int conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_close_connection_id'>📖 kamailio.cfg::function::tcp_close_connection_id()</a>

#### KSR.tcpops.tcp_conid_alive() ####

```cpp
int KSR.tcpops.tcp_conid_alive(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_alive'>📖 kamailio.cfg::function::tcp_conid_alive()</a>

#### KSR.tcpops.tcp_conid_state() ####

```cpp
int KSR.tcpops.tcp_conid_state(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_state'>📖 kamailio.cfg::function::tcp_conid_state()</a>

#### KSR.tcpops.tcp_enable_closed_event() ####

```cpp
int KSR.tcpops.tcp_enable_closed_event();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event'>📖 kamailio.cfg::function::tcp_enable_closed_event()</a>

#### KSR.tcpops.tcp_enable_closed_event_cid() ####

```cpp
int KSR.tcpops.tcp_enable_closed_event_cid(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event_cid'>📖 kamailio.cfg::function::tcp_enable_closed_event_cid()</a>

#### KSR.tcpops.tcp_keepalive_disable() ####

```cpp
int KSR.tcpops.tcp_keepalive_disable();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable'>📖 kamailio.cfg::function::tcp_keepalive_disable()</a>

#### KSR.tcpops.tcp_keepalive_disable_cid() ####

```cpp
int KSR.tcpops.tcp_keepalive_disable_cid(int i_con);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable_cid'>📖 kamailio.cfg::function::tcp_keepalive_disable_cid()</a>

#### KSR.tcpops.tcp_keepalive_enable() ####

```cpp
int KSR.tcpops.tcp_keepalive_enable(int i_idle, int i_cnt, int i_intvl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable'>📖 kamailio.cfg::function::tcp_keepalive_enable()</a>

#### KSR.tcpops.tcp_keepalive_enable_cid() ####

```cpp
int KSR.tcpops.tcp_keepalive_enable_cid(int i_con, int i_idle, int i_cnt, int i_intvl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable_cid'>📖 kamailio.cfg::function::tcp_keepalive_enable_cid()</a>

#### KSR.tcpops.tcp_set_connection_lifetime() ####

```cpp
int KSR.tcpops.tcp_set_connection_lifetime(int i_time);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime'>📖 kamailio.cfg::function::tcp_set_connection_lifetime()</a>

#### KSR.tcpops.tcp_set_connection_lifetime_cid() ####

```cpp
int KSR.tcpops.tcp_set_connection_lifetime_cid(int i_conid, int i_time);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime_cid'>📖 kamailio.cfg::function::tcp_set_connection_lifetime_cid()</a>

#### KSR.tcpops.tcp_set_otcpid() ####

```cpp
int KSR.tcpops.tcp_set_otcpid(int vconid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid'>📖 kamailio.cfg::function::tcp_set_otcpid()</a>

#### KSR.tcpops.tcp_set_otcpid_flag() ####

```cpp
int KSR.tcpops.tcp_set_otcpid_flag(int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid_flag'>📖 kamailio.cfg::function::tcp_set_otcpid_flag()</a>

## textops ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html'>📖 kamailio.cfg::module::textops.html</a>

#### KSR.textops.append_body_part() ####

```cpp
int KSR.textops.append_body_part(str "txt", str "ct");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part'>📖 kamailio.cfg::function::append_body_part()</a>

#### KSR.textops.append_body_part_cd() ####

```cpp
int KSR.textops.append_body_part_cd(str "txt", str "ct", str "cd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_cd'>📖 kamailio.cfg::function::append_body_part_cd()</a>

#### KSR.textops.append_body_part_hex() ####

```cpp
int KSR.textops.append_body_part_hex(str "txt", str "ct");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex'>📖 kamailio.cfg::function::append_body_part_hex()</a>

#### KSR.textops.append_body_part_hex_cd() ####

```cpp
int KSR.textops.append_body_part_hex_cd(str "htxt", str "ct", str "cd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex_cd'>📖 kamailio.cfg::function::append_body_part_hex_cd()</a>

#### KSR.textops.cmp_istr() ####

```cpp
int KSR.textops.cmp_istr(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_istr'>📖 kamailio.cfg::function::cmp_istr()</a>

#### KSR.textops.cmp_str() ####

```cpp
int KSR.textops.cmp_str(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_str'>📖 kamailio.cfg::function::cmp_str()</a>

#### KSR.textops.ends_with() ####

```cpp
int KSR.textops.ends_with(str "vstr", str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.ends_with'>📖 kamailio.cfg::function::ends_with()</a>

#### KSR.textops.filter_body() ####

```cpp
int KSR.textops.filter_body(str "content_type");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.filter_body'>📖 kamailio.cfg::function::filter_body()</a>

#### KSR.textops.get_body_part() ####

```cpp
int KSR.textops.get_body_part(str "ctype", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part'>📖 kamailio.cfg::function::get_body_part()</a>

#### KSR.textops.get_body_part_raw() ####

```cpp
int KSR.textops.get_body_part_raw(str "ctype", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part_raw'>📖 kamailio.cfg::function::get_body_part_raw()</a>

#### KSR.textops.has_body() ####

```cpp
int KSR.textops.has_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body'>📖 kamailio.cfg::function::has_body()</a>

#### KSR.textops.has_body_type() ####

```cpp
int KSR.textops.has_body_type(str "ctype");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body_type'>📖 kamailio.cfg::function::has_body_type()</a>

#### KSR.textops.in_list() ####

```cpp
int KSR.textops.in_list(str "subject", str "list", str "vsep");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list'>📖 kamailio.cfg::function::in_list()</a>

#### KSR.textops.in_list_prefix() ####

```cpp
int KSR.textops.in_list_prefix(str "subject", str "list", str "vsep");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list_prefix'>📖 kamailio.cfg::function::in_list_prefix()</a>

#### KSR.textops.is_audio_on_hold() ####

```cpp
int KSR.textops.is_audio_on_hold();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_audio_on_hold'>📖 kamailio.cfg::function::is_audio_on_hold()</a>

#### KSR.textops.is_present_hf() ####

```cpp
int KSR.textops.is_present_hf(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf'>📖 kamailio.cfg::function::is_present_hf()</a>

#### KSR.textops.is_present_hf_re() ####

```cpp
int KSR.textops.is_present_hf_re(str "ematch");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf_re'>📖 kamailio.cfg::function::is_present_hf_re()</a>

#### KSR.textops.is_privacy() ####

```cpp
int KSR.textops.is_privacy(str "privacy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_privacy'>📖 kamailio.cfg::function::is_privacy()</a>

#### KSR.textops.regex_substring() ####

```cpp
int KSR.textops.regex_substring(str "input", str "regex", int mindex, int nmatch, str "dst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.regex_substring'>📖 kamailio.cfg::function::regex_substring()</a>

#### KSR.textops.remove_body_part() ####

```cpp
int KSR.textops.remove_body_part(str "content_type");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_body_part'>📖 kamailio.cfg::function::remove_body_part()</a>

#### KSR.textops.remove_hf() ####

```cpp
int KSR.textops.remove_hf(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf'>📖 kamailio.cfg::function::remove_hf()</a>

#### KSR.textops.remove_hf_exp() ####

```cpp
int KSR.textops.remove_hf_exp(str "ematch", str "eskip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_exp'>📖 kamailio.cfg::function::remove_hf_exp()</a>

#### KSR.textops.remove_hf_idx() ####

```cpp
int KSR.textops.remove_hf_idx(str "hname", int idx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_idx'>📖 kamailio.cfg::function::remove_hf_idx()</a>

#### KSR.textops.remove_hf_re() ####

```cpp
int KSR.textops.remove_hf_re(str "ematch");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_re'>📖 kamailio.cfg::function::remove_hf_re()</a>

#### KSR.textops.replace() ####

```cpp
int KSR.textops.replace(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace'>📖 kamailio.cfg::function::replace()</a>

#### KSR.textops.replace_all() ####

```cpp
int KSR.textops.replace_all(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_all'>📖 kamailio.cfg::function::replace_all()</a>

#### KSR.textops.replace_body() ####

```cpp
int KSR.textops.replace_body(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body'>📖 kamailio.cfg::function::replace_body()</a>

#### KSR.textops.replace_body_all() ####

```cpp
int KSR.textops.replace_body_all(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_all'>📖 kamailio.cfg::function::replace_body_all()</a>

#### KSR.textops.replace_body_atonce() ####

```cpp
int KSR.textops.replace_body_atonce(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_atonce'>📖 kamailio.cfg::function::replace_body_atonce()</a>

#### KSR.textops.replace_body_str() ####

```cpp
int KSR.textops.replace_body_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_str'>📖 kamailio.cfg::function::replace_body_str()</a>

#### KSR.textops.replace_hdrs() ####

```cpp
int KSR.textops.replace_hdrs(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs'>📖 kamailio.cfg::function::replace_hdrs()</a>

#### KSR.textops.replace_hdrs_str() ####

```cpp
int KSR.textops.replace_hdrs_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs_str'>📖 kamailio.cfg::function::replace_hdrs_str()</a>

#### KSR.textops.replace_str() ####

```cpp
int KSR.textops.replace_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_str'>📖 kamailio.cfg::function::replace_str()</a>

#### KSR.textops.search() ####

```cpp
int KSR.textops.search(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search'>📖 kamailio.cfg::function::search()</a>

#### KSR.textops.search_append() ####

```cpp
int KSR.textops.search_append(str "ematch", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append'>📖 kamailio.cfg::function::search_append()</a>

#### KSR.textops.search_append_body() ####

```cpp
int KSR.textops.search_append_body(str "ematch", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append_body'>📖 kamailio.cfg::function::search_append_body()</a>

#### KSR.textops.search_body() ####

```cpp
int KSR.textops.search_body(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_body'>📖 kamailio.cfg::function::search_body()</a>

#### KSR.textops.search_hf() ####

```cpp
int KSR.textops.search_hf(str "hname", str "sre", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_hf'>📖 kamailio.cfg::function::search_hf()</a>

#### KSR.textops.search_str() ####

```cpp
int KSR.textops.search_str(str "stext", str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_str'>📖 kamailio.cfg::function::search_str()</a>

#### KSR.textops.set_body() ####

```cpp
int KSR.textops.set_body(str "nb", str "nc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body'>📖 kamailio.cfg::function::set_body()</a>

#### KSR.textops.set_body_multipart() ####

```cpp
int KSR.textops.set_body_multipart(str "nbody", str "ctype", str "boundary");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart'>📖 kamailio.cfg::function::set_body_multipart()</a>

#### KSR.textops.set_body_multipart_boundary() ####

```cpp
int KSR.textops.set_body_multipart_boundary(str "boundary");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_boundary'>📖 kamailio.cfg::function::set_body_multipart_boundary()</a>

#### KSR.textops.set_body_multipart_content() ####

```cpp
int KSR.textops.set_body_multipart_content(str "nbody", str "ctype");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_content'>📖 kamailio.cfg::function::set_body_multipart_content()</a>

#### KSR.textops.set_body_multipart_mode() ####

```cpp
int KSR.textops.set_body_multipart_mode();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_mode'>📖 kamailio.cfg::function::set_body_multipart_mode()</a>

#### KSR.textops.set_reply_body() ####

```cpp
int KSR.textops.set_reply_body(str "nb", str "nc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_reply_body'>📖 kamailio.cfg::function::set_reply_body()</a>

#### KSR.textops.starts_with() ####

```cpp
int KSR.textops.starts_with(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.starts_with'>📖 kamailio.cfg::function::starts_with()</a>

#### KSR.textops.str_find() ####

```cpp
int KSR.textops.str_find(str "txt", str "needle");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_find'>📖 kamailio.cfg::function::str_find()</a>

#### KSR.textops.str_ifind() ####

```cpp
int KSR.textops.str_ifind(str "txt", str "needle");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.str_ifind'>📖 kamailio.cfg::function::str_ifind()</a>

#### KSR.textops.subst() ####

```cpp
int KSR.textops.subst(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst'>📖 kamailio.cfg::function::subst()</a>

#### KSR.textops.subst_body() ####

```cpp
int KSR.textops.subst_body(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_body'>📖 kamailio.cfg::function::subst_body()</a>

#### KSR.textops.subst_hf() ####

```cpp
int KSR.textops.subst_hf(str "hname", str "subst", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_hf'>📖 kamailio.cfg::function::subst_hf()</a>

#### KSR.textops.subst_uri() ####

```cpp
int KSR.textops.subst_uri(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_uri'>📖 kamailio.cfg::function::subst_uri()</a>

#### KSR.textops.subst_user() ####

```cpp
int KSR.textops.subst_user(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_user'>📖 kamailio.cfg::function::subst_user()</a>

## textopsx ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html'>📖 kamailio.cfg::module::textopsx.html</a>

#### KSR.textopsx.append_hf_value() ####

```cpp
int KSR.textopsx.append_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.append_hf_value'>📖 kamailio.cfg::function::append_hf_value()</a>

#### KSR.textopsx.assign_hf_value() ####

```cpp
int KSR.textopsx.assign_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value'>📖 kamailio.cfg::function::assign_hf_value()</a>

#### KSR.textopsx.assign_hf_value2() ####

```cpp
int KSR.textopsx.assign_hf_value2(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value2'>📖 kamailio.cfg::function::assign_hf_value2()</a>

#### KSR.textopsx.bl_iterator_append() ####

```cpp
int KSR.textopsx.bl_iterator_append(str "iname", str "text");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_append'>📖 kamailio.cfg::function::bl_iterator_append()</a>

#### KSR.textopsx.bl_iterator_end() ####

```cpp
int KSR.textopsx.bl_iterator_end(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_end'>📖 kamailio.cfg::function::bl_iterator_end()</a>

#### KSR.textopsx.bl_iterator_insert() ####

```cpp
int KSR.textopsx.bl_iterator_insert(str "iname", str "text");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_insert'>📖 kamailio.cfg::function::bl_iterator_insert()</a>

#### KSR.textopsx.bl_iterator_next() ####

```cpp
int KSR.textopsx.bl_iterator_next(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_next'>📖 kamailio.cfg::function::bl_iterator_next()</a>

#### KSR.textopsx.bl_iterator_rm() ####

```cpp
int KSR.textopsx.bl_iterator_rm(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_rm'>📖 kamailio.cfg::function::bl_iterator_rm()</a>

#### KSR.textopsx.bl_iterator_start() ####

```cpp
int KSR.textopsx.bl_iterator_start(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_start'>📖 kamailio.cfg::function::bl_iterator_start()</a>

#### KSR.textopsx.bl_iterator_value() ####

```cpp
xval KSR.textopsx.bl_iterator_value(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.bl_iterator_value'>📖 kamailio.cfg::function::bl_iterator_value()</a>

#### KSR.textopsx.change_reply_status() ####

```cpp
int KSR.textopsx.change_reply_status(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status'>📖 kamailio.cfg::function::change_reply_status()</a>

#### KSR.textopsx.change_reply_status_code() ####

```cpp
int KSR.textopsx.change_reply_status_code(int code);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status_code'>📖 kamailio.cfg::function::change_reply_status_code()</a>

#### KSR.textopsx.exclude_hf_value() ####

```cpp
int KSR.textopsx.exclude_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.exclude_hf_value'>📖 kamailio.cfg::function::exclude_hf_value()</a>

#### KSR.textopsx.fnmatch() ####

```cpp
int KSR.textopsx.fnmatch(str "val", str "match");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch'>📖 kamailio.cfg::function::fnmatch()</a>

#### KSR.textopsx.fnmatch_ex() ####

```cpp
int KSR.textopsx.fnmatch_ex(str "val", str "match", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch_ex'>📖 kamailio.cfg::function::fnmatch_ex()</a>

#### KSR.textopsx.hf_iterator_append() ####

```cpp
int KSR.textopsx.hf_iterator_append(str "iname", str "htext");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_append'>📖 kamailio.cfg::function::hf_iterator_append()</a>

#### KSR.textopsx.hf_iterator_end() ####

```cpp
int KSR.textopsx.hf_iterator_end(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_end'>📖 kamailio.cfg::function::hf_iterator_end()</a>

#### KSR.textopsx.hf_iterator_hbody() ####

```cpp
xval KSR.textopsx.hf_iterator_hbody(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_hbody'>📖 kamailio.cfg::function::hf_iterator_hbody()</a>

#### KSR.textopsx.hf_iterator_hname() ####

```cpp
xval KSR.textopsx.hf_iterator_hname(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_hname'>📖 kamailio.cfg::function::hf_iterator_hname()</a>

#### KSR.textopsx.hf_iterator_insert() ####

```cpp
int KSR.textopsx.hf_iterator_insert(str "iname", str "htext");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_insert'>📖 kamailio.cfg::function::hf_iterator_insert()</a>

#### KSR.textopsx.hf_iterator_next() ####

```cpp
int KSR.textopsx.hf_iterator_next(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_next'>📖 kamailio.cfg::function::hf_iterator_next()</a>

#### KSR.textopsx.hf_iterator_prev() ####

```cpp
int KSR.textopsx.hf_iterator_prev(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_prev'>📖 kamailio.cfg::function::hf_iterator_prev()</a>

#### KSR.textopsx.hf_iterator_rm() ####

```cpp
int KSR.textopsx.hf_iterator_rm(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_rm'>📖 kamailio.cfg::function::hf_iterator_rm()</a>

#### KSR.textopsx.hf_iterator_start() ####

```cpp
int KSR.textopsx.hf_iterator_start(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_iterator_start'>📖 kamailio.cfg::function::hf_iterator_start()</a>

#### KSR.textopsx.hf_value_exists() ####

```cpp
int KSR.textopsx.hf_value_exists(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_value_exists'>📖 kamailio.cfg::function::hf_value_exists()</a>

#### KSR.textopsx.include_hf_value() ####

```cpp
int KSR.textopsx.include_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.include_hf_value'>📖 kamailio.cfg::function::include_hf_value()</a>

#### KSR.textopsx.insert_hf_value() ####

```cpp
int KSR.textopsx.insert_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.insert_hf_value'>📖 kamailio.cfg::function::insert_hf_value()</a>

#### KSR.textopsx.keep_hf() ####

```cpp
int KSR.textopsx.keep_hf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf'>📖 kamailio.cfg::function::keep_hf()</a>

#### KSR.textopsx.keep_hf_re() ####

```cpp
int KSR.textopsx.keep_hf_re(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf_re'>📖 kamailio.cfg::function::keep_hf_re()</a>

#### KSR.textopsx.msg_apply_changes() ####

```cpp
int KSR.textopsx.msg_apply_changes();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_apply_changes'>📖 kamailio.cfg::function::msg_apply_changes()</a>

#### KSR.textopsx.msg_set_buffer() ####

```cpp
int KSR.textopsx.msg_set_buffer(str "obuf");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_set_buffer'>📖 kamailio.cfg::function::msg_set_buffer()</a>

#### KSR.textopsx.remove_body() ####

```cpp
int KSR.textopsx.remove_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_body'>📖 kamailio.cfg::function::remove_body()</a>

#### KSR.textopsx.remove_hf_value() ####

```cpp
int KSR.textopsx.remove_hf_value(str "hexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value'>📖 kamailio.cfg::function::remove_hf_value()</a>

#### KSR.textopsx.remove_hf_value2() ####

```cpp
int KSR.textopsx.remove_hf_value2(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value2'>📖 kamailio.cfg::function::remove_hf_value2()</a>

## tls ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html'>📖 kamailio.cfg::module::tls.html</a>

#### KSR.tls.cget() ####

```cpp
xval KSR.tls.cget(str "aname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.cget'>📖 kamailio.cfg::function::cget()</a>

Return values corresponding the pseudo-variables exported by TLS module, related
to TLS connection and certificates. The parameter has to be the name of the
pseudo-variable (without `$`).

Example:

```
local vPeerSubjectCn = KSR.tls.cget("tls_peer_subject_cn");
```

#### KSR.tls.is_peer_verified() ####

```cpp
int KSR.tls.is_peer_verified();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.is_peer_verified'>📖 kamailio.cfg::function::is_peer_verified()</a>

#### KSR.tls.set_connect_server_id() ####

```cpp
int KSR.tls.set_connect_server_id(str "srvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.set_connect_server_id'>📖 kamailio.cfg::function::set_connect_server_id()</a>

## tm ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html'>📖 kamailio.cfg::module::tm.html</a>

#### KSR.tm.ki_t_load_contacts_mode() ####

```cpp
int KSR.tm.ki_t_load_contacts_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.ki_t_load_contacts_mode'>📖 kamailio.cfg::function::ki_t_load_contacts_mode()</a>

#### KSR.tm.t_any_replied() ####

```cpp
int KSR.tm.t_any_replied();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_replied'>📖 kamailio.cfg::function::t_any_replied()</a>

#### KSR.tm.t_any_timeout() ####

```cpp
int KSR.tm.t_any_timeout();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_timeout'>📖 kamailio.cfg::function::t_any_timeout()</a>

#### KSR.tm.t_branch_replied() ####

```cpp
int KSR.tm.t_branch_replied();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_replied'>📖 kamailio.cfg::function::t_branch_replied()</a>

#### KSR.tm.t_branch_timeout() ####

```cpp
int KSR.tm.t_branch_timeout();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_timeout'>📖 kamailio.cfg::function::t_branch_timeout()</a>

#### KSR.tm.t_check_status() ####

```cpp
int KSR.tm.t_check_status(str "sexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_status'>📖 kamailio.cfg::function::t_check_status()</a>

#### KSR.tm.t_check_trans() ####

```cpp
int KSR.tm.t_check_trans();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_trans'>📖 kamailio.cfg::function::t_check_trans()</a>

#### KSR.tm.t_clean() ####

```cpp
int KSR.tm.t_clean();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_clean'>📖 kamailio.cfg::function::t_clean()</a>

#### KSR.tm.t_drop_replies() ####

```cpp
int KSR.tm.t_drop_replies(str "mode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies'>📖 kamailio.cfg::function::t_drop_replies()</a>

#### KSR.tm.t_drop_replies_all() ####

```cpp
int KSR.tm.t_drop_replies_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies_all'>📖 kamailio.cfg::function::t_drop_replies_all()</a>

#### KSR.tm.t_get_branch_index() ####

```cpp
int KSR.tm.t_get_branch_index();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_branch_index'>📖 kamailio.cfg::function::t_get_branch_index()</a>

#### KSR.tm.t_get_status_code() ####

```cpp
int KSR.tm.t_get_status_code();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_status_code'>📖 kamailio.cfg::function::t_get_status_code()</a>

#### KSR.tm.t_grep_status() ####

```cpp
int KSR.tm.t_grep_status(int code);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_grep_status'>📖 kamailio.cfg::function::t_grep_status()</a>

#### KSR.tm.t_is_canceled() ####

```cpp
int KSR.tm.t_is_canceled();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_canceled'>📖 kamailio.cfg::function::t_is_canceled()</a>

#### KSR.tm.t_is_expired() ####

```cpp
int KSR.tm.t_is_expired();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_expired'>📖 kamailio.cfg::function::t_is_expired()</a>

#### KSR.tm.t_is_retr_async_reply() ####

```cpp
int KSR.tm.t_is_retr_async_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_retr_async_reply'>📖 kamailio.cfg::function::t_is_retr_async_reply()</a>

#### KSR.tm.t_is_set() ####

```cpp
int KSR.tm.t_is_set(str "target");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_set'>📖 kamailio.cfg::function::t_is_set()</a>

#### KSR.tm.t_load_contacts() ####

```cpp
int KSR.tm.t_load_contacts();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_load_contacts'>📖 kamailio.cfg::function::t_load_contacts()</a>

#### KSR.tm.t_lookup_cancel() ####

```cpp
int KSR.tm.t_lookup_cancel();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel'>📖 kamailio.cfg::function::t_lookup_cancel()</a>

#### KSR.tm.t_lookup_cancel_flags() ####

```cpp
int KSR.tm.t_lookup_cancel_flags(int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel_flags'>📖 kamailio.cfg::function::t_lookup_cancel_flags()</a>

#### KSR.tm.t_lookup_request() ####

```cpp
int KSR.tm.t_lookup_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_request'>📖 kamailio.cfg::function::t_lookup_request()</a>

#### KSR.tm.t_newtran() ####

```cpp
int KSR.tm.t_newtran();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_newtran'>📖 kamailio.cfg::function::t_newtran()</a>

#### KSR.tm.t_next_contact_flow() ####

```cpp
int KSR.tm.t_next_contact_flow();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contact_flow'>📖 kamailio.cfg::function::t_next_contact_flow()</a>

#### KSR.tm.t_next_contacts() ####

```cpp
int KSR.tm.t_next_contacts();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contacts'>📖 kamailio.cfg::function::t_next_contacts()</a>

#### KSR.tm.t_on_branch() ####

```cpp
int KSR.tm.t_on_branch(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch'>📖 kamailio.cfg::function::t_on_branch()</a>

#### KSR.tm.t_on_branch_failure() ####

```cpp
int KSR.tm.t_on_branch_failure(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch_failure'>📖 kamailio.cfg::function::t_on_branch_failure()</a>

#### KSR.tm.t_on_failure() ####

```cpp
int KSR.tm.t_on_failure(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_failure'>📖 kamailio.cfg::function::t_on_failure()</a>

#### KSR.tm.t_on_reply() ####

```cpp
int KSR.tm.t_on_reply(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_reply'>📖 kamailio.cfg::function::t_on_reply()</a>

#### KSR.tm.t_relay() ####

```cpp
int KSR.tm.t_relay();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay'>📖 kamailio.cfg::function::t_relay()</a>

#### KSR.tm.t_relay_to_flags() ####

```cpp
int KSR.tm.t_relay_to_flags(int rflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_flags'>📖 kamailio.cfg::function::t_relay_to_flags()</a>

#### KSR.tm.t_relay_to_proto() ####

```cpp
int KSR.tm.t_relay_to_proto(str "sproto");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto'>📖 kamailio.cfg::function::t_relay_to_proto()</a>

#### KSR.tm.t_relay_to_proto_addr() ####

```cpp
int KSR.tm.t_relay_to_proto_addr(str "sproto", str "host", int port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto_addr'>📖 kamailio.cfg::function::t_relay_to_proto_addr()</a>

#### KSR.tm.t_relay_to_proxy() ####

```cpp
int KSR.tm.t_relay_to_proxy(str "sproxy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy'>📖 kamailio.cfg::function::t_relay_to_proxy()</a>

#### KSR.tm.t_relay_to_proxy_flags() ####

```cpp
int KSR.tm.t_relay_to_proxy_flags(str "sproxy", int rflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy_flags'>📖 kamailio.cfg::function::t_relay_to_proxy_flags()</a>

#### KSR.tm.t_release() ####

```cpp
int KSR.tm.t_release();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_release'>📖 kamailio.cfg::function::t_release()</a>

#### KSR.tm.t_replicate() ####

```cpp
int KSR.tm.t_replicate(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_replicate'>📖 kamailio.cfg::function::t_replicate()</a>

#### KSR.tm.t_reply() ####

```cpp
int KSR.tm.t_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reply'>📖 kamailio.cfg::function::t_reply()</a>

#### KSR.tm.t_reset_fr() ####

```cpp
int KSR.tm.t_reset_fr();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_fr'>📖 kamailio.cfg::function::t_reset_fr()</a>

#### KSR.tm.t_reset_max_lifetime() ####

```cpp
int KSR.tm.t_reset_max_lifetime();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_max_lifetime'>📖 kamailio.cfg::function::t_reset_max_lifetime()</a>

#### KSR.tm.t_reset_retr() ####

```cpp
int KSR.tm.t_reset_retr();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_retr'>📖 kamailio.cfg::function::t_reset_retr()</a>

#### KSR.tm.t_retransmit_reply() ####

```cpp
int KSR.tm.t_retransmit_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_retransmit_reply'>📖 kamailio.cfg::function::t_retransmit_reply()</a>

#### KSR.tm.t_save_lumps() ####

```cpp
int KSR.tm.t_save_lumps();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_save_lumps'>📖 kamailio.cfg::function::t_save_lumps()</a>

#### KSR.tm.t_send_reply() ####

```cpp
int KSR.tm.t_send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_send_reply'>📖 kamailio.cfg::function::t_send_reply()</a>

#### KSR.tm.t_set_auto_inv_100() ####

```cpp
int KSR.tm.t_set_auto_inv_100(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_auto_inv_100'>📖 kamailio.cfg::function::t_set_auto_inv_100()</a>

#### KSR.tm.t_set_disable_6xx() ####

```cpp
int KSR.tm.t_set_disable_6xx(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_6xx'>📖 kamailio.cfg::function::t_set_disable_6xx()</a>

#### KSR.tm.t_set_disable_failover() ####

```cpp
int KSR.tm.t_set_disable_failover(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_failover'>📖 kamailio.cfg::function::t_set_disable_failover()</a>

#### KSR.tm.t_set_disable_internal_reply() ####

```cpp
int KSR.tm.t_set_disable_internal_reply(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_internal_reply'>📖 kamailio.cfg::function::t_set_disable_internal_reply()</a>

#### KSR.tm.t_set_fr() ####

```cpp
int KSR.tm.t_set_fr(int fr_inv, int fr);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr'>📖 kamailio.cfg::function::t_set_fr()</a>

#### KSR.tm.t_set_fr_inv() ####

```cpp
int KSR.tm.t_set_fr_inv(int fr_inv);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr_inv'>📖 kamailio.cfg::function::t_set_fr_inv()</a>

#### KSR.tm.t_set_max_lifetime() ####

```cpp
int KSR.tm.t_set_max_lifetime(int t1, int t2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_max_lifetime'>📖 kamailio.cfg::function::t_set_max_lifetime()</a>

#### KSR.tm.t_set_no_e2e_cancel_reason() ####

```cpp
int KSR.tm.t_set_no_e2e_cancel_reason(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_no_e2e_cancel_reason'>📖 kamailio.cfg::function::t_set_no_e2e_cancel_reason()</a>

#### KSR.tm.t_set_retr() ####

```cpp
int KSR.tm.t_set_retr(int t1, int t2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_retr'>📖 kamailio.cfg::function::t_set_retr()</a>

#### KSR.tm.t_uac_send() ####

```cpp
int KSR.tm.t_uac_send(str "method", str "ruri", str "nexthop", str "ssock", str "hdrs", str "body");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_uac_send'>📖 kamailio.cfg::function::t_uac_send()</a>

#### KSR.tm.t_use_uac_headers() ####

```cpp
int KSR.tm.t_use_uac_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_use_uac_headers'>📖 kamailio.cfg::function::t_use_uac_headers()</a>

## tmrec ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html'>📖 kamailio.cfg::module::tmrec.html</a>

#### KSR.tmrec.is_leap_year() ####

```cpp
int KSR.tmrec.is_leap_year(int y);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year'>📖 kamailio.cfg::function::is_leap_year()</a>

#### KSR.tmrec.is_leap_year_now() ####

```cpp
int KSR.tmrec.is_leap_year_now();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year_now'>📖 kamailio.cfg::function::is_leap_year_now()</a>

#### KSR.tmrec.match() ####

```cpp
int KSR.tmrec.match(str "rv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match'>📖 kamailio.cfg::function::match()</a>

#### KSR.tmrec.match_timestamp() ####

```cpp
int KSR.tmrec.match_timestamp(str "rv", int ti);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match_timestamp'>📖 kamailio.cfg::function::match_timestamp()</a>

#### KSR.tmrec.time_period_match() ####

```cpp
int KSR.tmrec.time_period_match(str "period");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match'>📖 kamailio.cfg::function::time_period_match()</a>

#### KSR.tmrec.time_period_match_timestamp() ####

```cpp
int KSR.tmrec.time_period_match_timestamp(str "period", int ti);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match_timestamp'>📖 kamailio.cfg::function::time_period_match_timestamp()</a>

## tmx ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html'>📖 kamailio.cfg::module::tmx.html</a>

#### KSR.tmx.t_cancel_branches() ####

```cpp
int KSR.tmx.t_cancel_branches(str "mode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_branches'>📖 kamailio.cfg::function::t_cancel_branches()</a>

#### KSR.tmx.t_cancel_callid() ####

```cpp
int KSR.tmx.t_cancel_callid(str "callid_s", str "cseq_s", int fl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid'>📖 kamailio.cfg::function::t_cancel_callid()</a>

#### KSR.tmx.t_cancel_callid_reason() ####

```cpp
int KSR.tmx.t_cancel_callid_reason(str "callid_s", str "cseq_s", int fl, int rcode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid_reason'>📖 kamailio.cfg::function::t_cancel_callid_reason()</a>

#### KSR.tmx.t_continue() ####

```cpp
int KSR.tmx.t_continue(int tindex, int tlabel, str "cbname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_continue'>📖 kamailio.cfg::function::t_continue()</a>

#### KSR.tmx.t_drop() ####

```cpp
int KSR.tmx.t_drop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop'>📖 kamailio.cfg::function::t_drop()</a>

#### KSR.tmx.t_drop_rcode() ####

```cpp
int KSR.tmx.t_drop_rcode(int rcode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop_rcode'>📖 kamailio.cfg::function::t_drop_rcode()</a>

#### KSR.tmx.t_flush_flags() ####

```cpp
int KSR.tmx.t_flush_flags();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_flags'>📖 kamailio.cfg::function::t_flush_flags()</a>

#### KSR.tmx.t_flush_xflags() ####

```cpp
int KSR.tmx.t_flush_xflags();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_xflags'>📖 kamailio.cfg::function::t_flush_xflags()</a>

#### KSR.tmx.t_is_branch_route() ####

```cpp
int KSR.tmx.t_is_branch_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_branch_route'>📖 kamailio.cfg::function::t_is_branch_route()</a>

#### KSR.tmx.t_is_failure_route() ####

```cpp
int KSR.tmx.t_is_failure_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_failure_route'>📖 kamailio.cfg::function::t_is_failure_route()</a>

#### KSR.tmx.t_is_reply_route() ####

```cpp
int KSR.tmx.t_is_reply_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_reply_route'>📖 kamailio.cfg::function::t_is_reply_route()</a>

#### KSR.tmx.t_is_request_route() ####

```cpp
int KSR.tmx.t_is_request_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_request_route'>📖 kamailio.cfg::function::t_is_request_route()</a>

#### KSR.tmx.t_precheck_trans() ####

```cpp
int KSR.tmx.t_precheck_trans();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_precheck_trans'>📖 kamailio.cfg::function::t_precheck_trans()</a>

#### KSR.tmx.t_reply_callid() ####

```cpp
int KSR.tmx.t_reply_callid(str "callid_s", str "cseq_s", int code, str "status_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reply_callid'>📖 kamailio.cfg::function::t_reply_callid()</a>

#### KSR.tmx.t_reuse_branch() ####

```cpp
int KSR.tmx.t_reuse_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reuse_branch'>📖 kamailio.cfg::function::t_reuse_branch()</a>

#### KSR.tmx.t_suspend() ####

```cpp
int KSR.tmx.t_suspend();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_suspend'>📖 kamailio.cfg::function::t_suspend()</a>

## topos ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/topos.html'>📖 kamailio.cfg::module::topos.html</a>

#### KSR.topos.tps_set_context() ####

```cpp
int KSR.topos.tps_set_context(str "ctx");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/topos.html#topos.f.tps_set_context'>📖 kamailio.cfg::function::tps_set_context()</a>

## tsilo ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html'>📖 kamailio.cfg::module::tsilo.html</a>

#### KSR.tsilo.ts_append() ####

```cpp
int KSR.tsilo.ts_append(str "_table", str "_ruri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append'>📖 kamailio.cfg::function::ts_append()</a>

#### KSR.tsilo.ts_append_to() ####

```cpp
int KSR.tsilo.ts_append_to(int tindex, int tlabel, str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to'>📖 kamailio.cfg::function::ts_append_to()</a>

#### KSR.tsilo.ts_append_to_uri() ####

```cpp
int KSR.tsilo.ts_append_to_uri(int tindex, int tlabel, str "_table", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to_uri'>📖 kamailio.cfg::function::ts_append_to_uri()</a>

#### KSR.tsilo.ts_store() ####

```cpp
int KSR.tsilo.ts_store();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store'>📖 kamailio.cfg::function::ts_store()</a>

#### KSR.tsilo.ts_store_uri() ####

```cpp
int KSR.tsilo.ts_store_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store_uri'>📖 kamailio.cfg::function::ts_store_uri()</a>

## uac ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html'>📖 kamailio.cfg::module::uac.html</a>

#### KSR.uac.uac_auth() ####

```cpp
int KSR.uac.uac_auth();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth'>📖 kamailio.cfg::function::uac_auth()</a>

#### KSR.uac.uac_auth_mode() ####

```cpp
int KSR.uac.uac_auth_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth_mode'>📖 kamailio.cfg::function::uac_auth_mode()</a>

#### KSR.uac.uac_reg_disable() ####

```cpp
int KSR.uac.uac_reg_disable(str "attr", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_disable'>📖 kamailio.cfg::function::uac_reg_disable()</a>

#### KSR.uac.uac_reg_enable() ####

```cpp
int KSR.uac.uac_reg_enable(str "attr", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_enable'>📖 kamailio.cfg::function::uac_reg_enable()</a>

#### KSR.uac.uac_reg_lookup() ####

```cpp
int KSR.uac.uac_reg_lookup(str "userid", str "sdst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup'>📖 kamailio.cfg::function::uac_reg_lookup()</a>

#### KSR.uac.uac_reg_lookup_uri() ####

```cpp
int KSR.uac.uac_reg_lookup_uri(str "suri", str "sdst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup_uri'>📖 kamailio.cfg::function::uac_reg_lookup_uri()</a>

#### KSR.uac.uac_reg_refresh() ####

```cpp
int KSR.uac.uac_reg_refresh(str "l_uuid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_refresh'>📖 kamailio.cfg::function::uac_reg_refresh()</a>

#### KSR.uac.uac_reg_request_to() ####

```cpp
int KSR.uac.uac_reg_request_to(str "userid", int imode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_request_to'>📖 kamailio.cfg::function::uac_reg_request_to()</a>

#### KSR.uac.uac_reg_status() ####

```cpp
int KSR.uac.uac_reg_status(str "sruuid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_status'>📖 kamailio.cfg::function::uac_reg_status()</a>

#### KSR.uac.uac_replace_from() ####

```cpp
int KSR.uac.uac_replace_from(str "pdsp", str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from'>📖 kamailio.cfg::function::uac_replace_from()</a>

#### KSR.uac.uac_replace_from_uri() ####

```cpp
int KSR.uac.uac_replace_from_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from_uri'>📖 kamailio.cfg::function::uac_replace_from_uri()</a>

#### KSR.uac.uac_replace_to() ####

```cpp
int KSR.uac.uac_replace_to(str "pdsp", str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to'>📖 kamailio.cfg::function::uac_replace_to()</a>

#### KSR.uac.uac_replace_to_uri() ####

```cpp
int KSR.uac.uac_replace_to_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to_uri'>📖 kamailio.cfg::function::uac_replace_to_uri()</a>

#### KSR.uac.uac_req_send() ####

```cpp
int KSR.uac.uac_req_send();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_req_send'>📖 kamailio.cfg::function::uac_req_send()</a>

#### KSR.uac.uac_restore_from() ####

```cpp
int KSR.uac.uac_restore_from();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_from'>📖 kamailio.cfg::function::uac_restore_from()</a>

#### KSR.uac.uac_restore_to() ####

```cpp
int KSR.uac.uac_restore_to();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_to'>📖 kamailio.cfg::function::uac_restore_to()</a>

## uac_redirect ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html'>📖 kamailio.cfg::module::uac_redirect.html</a>

#### KSR.uac_redirect.get_redirects() ####

```cpp
int KSR.uac_redirect.get_redirects(int max_c, int max_b);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects'>📖 kamailio.cfg::function::get_redirects()</a>

#### KSR.uac_redirect.get_redirects_acc() ####

```cpp
int KSR.uac_redirect.get_redirects_acc(int max_c, int max_b, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_acc'>📖 kamailio.cfg::function::get_redirects_acc()</a>

#### KSR.uac_redirect.get_redirects_all() ####

```cpp
int KSR.uac_redirect.get_redirects_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_all'>📖 kamailio.cfg::function::get_redirects_all()</a>

## uri_db ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html'>📖 kamailio.cfg::module::uri_db.html</a>

#### KSR.uri_db.check_from() ####

```cpp
int KSR.uri_db.check_from();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_from'>📖 kamailio.cfg::function::check_from()</a>

#### KSR.uri_db.check_to() ####

```cpp
int KSR.uri_db.check_to();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_to'>📖 kamailio.cfg::function::check_to()</a>

#### KSR.uri_db.check_uri() ####

```cpp
int KSR.uri_db.check_uri(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri'>📖 kamailio.cfg::function::check_uri()</a>

#### KSR.uri_db.check_uri_realm() ####

```cpp
int KSR.uri_db.check_uri_realm(str "suri", str "susername", str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri_realm'>📖 kamailio.cfg::function::check_uri_realm()</a>

#### KSR.uri_db.does_uri_exist() ####

```cpp
int KSR.uri_db.does_uri_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.does_uri_exist'>📖 kamailio.cfg::function::does_uri_exist()</a>

## userblocklist ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html'>📖 kamailio.cfg::module::userblocklist.html</a>

#### KSR.userblocklist.check_allowlist() ####

```cpp
int KSR.userblocklist.check_allowlist(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_allowlist'>📖 kamailio.cfg::function::check_allowlist()</a>

#### KSR.userblocklist.check_blocklist() ####

```cpp
int KSR.userblocklist.check_blocklist(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_blocklist'>📖 kamailio.cfg::function::check_blocklist()</a>

#### KSR.userblocklist.check_global_blocklist() ####

```cpp
int KSR.userblocklist.check_global_blocklist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_global_blocklist'>📖 kamailio.cfg::function::check_global_blocklist()</a>

#### KSR.userblocklist.check_user_allowlist() ####

```cpp
int KSR.userblocklist.check_user_allowlist(str "suser", str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist'>📖 kamailio.cfg::function::check_user_allowlist()</a>

#### KSR.userblocklist.check_user_allowlist_number() ####

```cpp
int KSR.userblocklist.check_user_allowlist_number(str "suser", str "sdomain", str "snumber");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_number'>📖 kamailio.cfg::function::check_user_allowlist_number()</a>

#### KSR.userblocklist.check_user_allowlist_table() ####

```cpp
int KSR.userblocklist.check_user_allowlist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_table'>📖 kamailio.cfg::function::check_user_allowlist_table()</a>

#### KSR.userblocklist.check_user_blocklist() ####

```cpp
int KSR.userblocklist.check_user_blocklist(str "suser", str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist'>📖 kamailio.cfg::function::check_user_blocklist()</a>

#### KSR.userblocklist.check_user_blocklist_number() ####

```cpp
int KSR.userblocklist.check_user_blocklist_number(str "suser", str "sdomain", str "snumber");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_number'>📖 kamailio.cfg::function::check_user_blocklist_number()</a>

#### KSR.userblocklist.check_user_blocklist_table() ####

```cpp
int KSR.userblocklist.check_user_blocklist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_table'>📖 kamailio.cfg::function::check_user_blocklist_table()</a>

## utils ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/utils.html'>📖 kamailio.cfg::module::utils.html</a>

#### KSR.utils.xcap_auth_status() ####

```cpp
int KSR.utils.xcap_auth_status(str "watcher_uri", str "presentity_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/utils.html#utils.f.xcap_auth_status'>📖 kamailio.cfg::function::xcap_auth_status()</a>

## websocket ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html'>📖 kamailio.cfg::module::websocket.html</a>

#### KSR.websocket.close() ####

```cpp
int KSR.websocket.close();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close'>📖 kamailio.cfg::function::close()</a>

#### KSR.websocket.close_conid() ####

```cpp
int KSR.websocket.close_conid(int status, str "reason", int con);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_conid'>📖 kamailio.cfg::function::close_conid()</a>

#### KSR.websocket.close_reason() ####

```cpp
int KSR.websocket.close_reason(int status, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_reason'>📖 kamailio.cfg::function::close_reason()</a>

#### KSR.websocket.handle_handshake() ####

```cpp
int KSR.websocket.handle_handshake();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.handle_handshake'>📖 kamailio.cfg::function::handle_handshake()</a>

## xcap_server ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html'>📖 kamailio.cfg::module::xcap_server.html</a>

#### KSR.xcap_server.xcaps_del() ####

```cpp
int KSR.xcap_server.xcaps_del(str "uri", str "path");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_del'>📖 kamailio.cfg::function::xcaps_del()</a>

#### KSR.xcap_server.xcaps_get() ####

```cpp
int KSR.xcap_server.xcaps_get(str "uri", str "path");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_get'>📖 kamailio.cfg::function::xcaps_get()</a>

#### KSR.xcap_server.xcaps_put() ####

```cpp
int KSR.xcap_server.xcaps_put(str "uri", str "path", str "pbody");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_put'>📖 kamailio.cfg::function::xcaps_put()</a>

## xhttp ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp.html'>📖 kamailio.cfg::module::xhttp.html</a>

#### KSR.xhttp.get_hu() ####

```cpp
xval KSR.xhttp.get_hu();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp.html#xhttp.f.get_hu'>📖 kamailio.cfg::function::get_hu()</a>

#### KSR.xhttp.xhttp_reply() ####

```cpp
int KSR.xhttp.xhttp_reply(int code, str "reason", str "ctype", str "body");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp.html#xhttp.f.xhttp_reply'>📖 kamailio.cfg::function::xhttp_reply()</a>

## xhttp_pi ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_pi.html'>📖 kamailio.cfg::module::xhttp_pi.html</a>

#### KSR.xhttp_pi.dispatch() ####

```cpp
int KSR.xhttp_pi.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_pi.html#xhttp_pi.f.dispatch'>📖 kamailio.cfg::function::dispatch()</a>

## xhttp_prom ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html'>📖 kamailio.cfg::module::xhttp_prom.html</a>

#### KSR.xhttp_prom.check_uri() ####

```cpp
int KSR.xhttp_prom.check_uri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.check_uri'>📖 kamailio.cfg::function::check_uri()</a>

#### KSR.xhttp_prom.counter_inc_l0() ####

```cpp
int KSR.xhttp_prom.counter_inc_l0(str "s_name", int number);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l0'>📖 kamailio.cfg::function::counter_inc_l0()</a>

#### KSR.xhttp_prom.counter_inc_l1() ####

```cpp
int KSR.xhttp_prom.counter_inc_l1(str "s_name", int number, str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l1'>📖 kamailio.cfg::function::counter_inc_l1()</a>

#### KSR.xhttp_prom.counter_inc_l2() ####

```cpp
int KSR.xhttp_prom.counter_inc_l2(str "s_name", int number, str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l2'>📖 kamailio.cfg::function::counter_inc_l2()</a>

#### KSR.xhttp_prom.counter_inc_l3() ####

```cpp
int KSR.xhttp_prom.counter_inc_l3(str "s_name", int number, str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l3'>📖 kamailio.cfg::function::counter_inc_l3()</a>

#### KSR.xhttp_prom.counter_reset_l0() ####

```cpp
int KSR.xhttp_prom.counter_reset_l0(str "s_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l0'>📖 kamailio.cfg::function::counter_reset_l0()</a>

#### KSR.xhttp_prom.counter_reset_l1() ####

```cpp
int KSR.xhttp_prom.counter_reset_l1(str "s_name", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l1'>📖 kamailio.cfg::function::counter_reset_l1()</a>

#### KSR.xhttp_prom.counter_reset_l2() ####

```cpp
int KSR.xhttp_prom.counter_reset_l2(str "s_name", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l2'>📖 kamailio.cfg::function::counter_reset_l2()</a>

#### KSR.xhttp_prom.counter_reset_l3() ####

```cpp
int KSR.xhttp_prom.counter_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l3'>📖 kamailio.cfg::function::counter_reset_l3()</a>

#### KSR.xhttp_prom.dispatch() ####

```cpp
int KSR.xhttp_prom.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.dispatch'>📖 kamailio.cfg::function::dispatch()</a>

#### KSR.xhttp_prom.gauge_reset_l0() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l0(str "s_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l0'>📖 kamailio.cfg::function::gauge_reset_l0()</a>

#### KSR.xhttp_prom.gauge_reset_l1() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l1(str "s_name", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l1'>📖 kamailio.cfg::function::gauge_reset_l1()</a>

#### KSR.xhttp_prom.gauge_reset_l2() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l2(str "s_name", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l2'>📖 kamailio.cfg::function::gauge_reset_l2()</a>

#### KSR.xhttp_prom.gauge_reset_l3() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l3'>📖 kamailio.cfg::function::gauge_reset_l3()</a>

#### KSR.xhttp_prom.gauge_set_l0() ####

```cpp
int KSR.xhttp_prom.gauge_set_l0(str "s_name", str "s_number");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l0'>📖 kamailio.cfg::function::gauge_set_l0()</a>

#### KSR.xhttp_prom.gauge_set_l1() ####

```cpp
int KSR.xhttp_prom.gauge_set_l1(str "s_name", str "s_number", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l1'>📖 kamailio.cfg::function::gauge_set_l1()</a>

#### KSR.xhttp_prom.gauge_set_l2() ####

```cpp
int KSR.xhttp_prom.gauge_set_l2(str "s_name", str "s_number", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l2'>📖 kamailio.cfg::function::gauge_set_l2()</a>

#### KSR.xhttp_prom.gauge_set_l3() ####

```cpp
int KSR.xhttp_prom.gauge_set_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l3'>📖 kamailio.cfg::function::gauge_set_l3()</a>

#### KSR.xhttp_prom.histogram_observe_l0() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l0(str "s_name", str "s_number");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l0'>📖 kamailio.cfg::function::histogram_observe_l0()</a>

#### KSR.xhttp_prom.histogram_observe_l1() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l1(str "s_name", str "s_number", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l1'>📖 kamailio.cfg::function::histogram_observe_l1()</a>

#### KSR.xhttp_prom.histogram_observe_l2() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l2(str "s_name", str "s_number", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l2'>📖 kamailio.cfg::function::histogram_observe_l2()</a>

#### KSR.xhttp_prom.histogram_observe_l3() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l3'>📖 kamailio.cfg::function::histogram_observe_l3()</a>

## xhttp_rpc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_rpc.html'>📖 kamailio.cfg::module::xhttp_rpc.html</a>

#### KSR.xhttp_rpc.dispatch() ####

```cpp
int KSR.xhttp_rpc.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_rpc.html#xhttp_rpc.f.dispatch'>📖 kamailio.cfg::function::dispatch()</a>

## xlog ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html'>📖 kamailio.cfg::module::xlog.html</a>

#### KSR.xlog.xalert() ####

```cpp
int KSR.xlog.xalert(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xalert'>📖 kamailio.cfg::function::xalert()</a>

#### KSR.xlog.xcrit() ####

```cpp
int KSR.xlog.xcrit(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xcrit'>📖 kamailio.cfg::function::xcrit()</a>

#### KSR.xlog.xdbg() ####

```cpp
int KSR.xlog.xdbg(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xdbg'>📖 kamailio.cfg::function::xdbg()</a>

#### KSR.xlog.xerr() ####

```cpp
int KSR.xlog.xerr(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xerr'>📖 kamailio.cfg::function::xerr()</a>

#### KSR.xlog.xinfo() ####

```cpp
int KSR.xlog.xinfo(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xinfo'>📖 kamailio.cfg::function::xinfo()</a>

#### KSR.xlog.xlog() ####

```cpp
int KSR.xlog.xlog(str "slevel", str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xlog'>📖 kamailio.cfg::function::xlog()</a>

#### KSR.xlog.xnotice() ####

```cpp
int KSR.xlog.xnotice(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xnotice'>📖 kamailio.cfg::function::xnotice()</a>

#### KSR.xlog.xwarn() ####

```cpp
int KSR.xlog.xwarn(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xwarn'>📖 kamailio.cfg::function::xwarn()</a>

## xmlrpc ##

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xmlrpc.html'>📖 kamailio.cfg::module::xmlrpc.html</a>

#### KSR.xmlrpc.dispatch_rpc() ####

```cpp
int KSR.xmlrpc.dispatch_rpc();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.dispatch_rpc'>📖 kamailio.cfg::function::dispatch_rpc()</a>

#### KSR.xmlrpc.xmlrpc_reply() ####

```cpp
int KSR.xmlrpc.xmlrpc_reply(int rcode, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.xmlrpc_reply'>📖 kamailio.cfg::function::xmlrpc_reply()</a>

