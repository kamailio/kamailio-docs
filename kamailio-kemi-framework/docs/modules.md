<!-- This file is auto-generated. Any manual modifications will be deleted -->
# KEMI Module Functions #
The following sections lists all exported KEMI functions. More information regarding the function can be found by clicking the KEMI prototype which will take you the original module's documentation.

## acc ##

The functions exported by `acc` module to KEMI are listed in the next sections.

The documentation of `acc` module is available online at:

  * [acc.html](https://kamailio.org/docs/modules/devel/modules/acc.html)

#### KSR.acc.acc_db_request() ####

```cpp
int KSR.acc.acc_db_request(str "comment", str "dbtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_db_request'>📖 kamailio.cfg::acc_db_request()</a>

Equivalent of native kamailio.cfg function: `acc_db_request("comment", "dbtable")`.

#### KSR.acc.acc_log_request() ####

```cpp
int KSR.acc.acc_log_request(str "comment");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_log_request'>📖 kamailio.cfg::acc_log_request()</a>

Equivalent of native kamailio.cfg function: `acc_log_request("comment")`.

#### KSR.acc.acc_request() ####

```cpp
int KSR.acc.acc_request(str "comment", str "dbtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc.html#acc.f.acc_request'>📖 kamailio.cfg::acc_request()</a>

Equivalent of native kamailio.cfg function: `acc_request("comment", "dbtable")`.

## acc_radius ##

#### KSR.acc_radius.request() ####

```cpp
int KSR.acc_radius.request(str "comment");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/acc_radius.html#acc_radius.f.request'>📖 kamailio.cfg::request()</a>

## alias_db ##

#### KSR.alias_db.lookup() ####

```cpp
int KSR.alias_db.lookup(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/alias_db.html#alias_db.f.lookup'>📖 kamailio.cfg::lookup()</a>

#### KSR.alias_db.lookup_ex() ####

```cpp
int KSR.alias_db.lookup_ex(str "stable", str "sflags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/alias_db.html#alias_db.f.lookup_ex'>📖 kamailio.cfg::lookup_ex()</a>

## app_jsdt ##

#### KSR.app_jsdt.dofile() ####

```cpp
int KSR.app_jsdt.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.dofile'>📖 kamailio.cfg::dofile()</a>

#### KSR.app_jsdt.dostring() ####

```cpp
int KSR.app_jsdt.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.dostring'>📖 kamailio.cfg::dostring()</a>

#### KSR.app_jsdt.run() ####

```cpp
int KSR.app_jsdt.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run'>📖 kamailio.cfg::run()</a>

#### KSR.app_jsdt.run_p1() ####

```cpp
int KSR.app_jsdt.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p1'>📖 kamailio.cfg::run_p1()</a>

#### KSR.app_jsdt.run_p2() ####

```cpp
int KSR.app_jsdt.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p2'>📖 kamailio.cfg::run_p2()</a>

#### KSR.app_jsdt.run_p3() ####

```cpp
int KSR.app_jsdt.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p3'>📖 kamailio.cfg::run_p3()</a>

#### KSR.app_jsdt.runstring() ####

```cpp
int KSR.app_jsdt.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.runstring'>📖 kamailio.cfg::runstring()</a>

## app_lua ##

#### KSR.app_lua.dofile() ####

```cpp
int KSR.app_lua.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.dofile'>📖 kamailio.cfg::dofile()</a>

#### KSR.app_lua.dostring() ####

```cpp
int KSR.app_lua.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.dostring'>📖 kamailio.cfg::dostring()</a>

#### KSR.app_lua.run() ####

```cpp
int KSR.app_lua.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run'>📖 kamailio.cfg::run()</a>

#### KSR.app_lua.run_p1() ####

```cpp
int KSR.app_lua.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p1'>📖 kamailio.cfg::run_p1()</a>

#### KSR.app_lua.run_p2() ####

```cpp
int KSR.app_lua.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p2'>📖 kamailio.cfg::run_p2()</a>

#### KSR.app_lua.run_p3() ####

```cpp
int KSR.app_lua.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p3'>📖 kamailio.cfg::run_p3()</a>

#### KSR.app_lua.runstring() ####

```cpp
int KSR.app_lua.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_lua.html#app_lua.f.runstring'>📖 kamailio.cfg::runstring()</a>

## app_python ##

#### KSR.app_python.exec() ####

```cpp
int KSR.app_python.exec(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.exec'>📖 kamailio.cfg::exec()</a>

#### KSR.app_python.exec_p1() ####

```cpp
int KSR.app_python.exec_p1(str "method", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.exec_p1'>📖 kamailio.cfg::exec_p1()</a>

#### KSR.app_python.execx() ####

```cpp
int KSR.app_python.execx(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python.html#app_python.f.execx'>📖 kamailio.cfg::execx()</a>

## app_python3 ##

#### KSR.app_python3.exec() ####

```cpp
int KSR.app_python3.exec(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.exec'>📖 kamailio.cfg::exec()</a>

#### KSR.app_python3.exec_p1() ####

```cpp
int KSR.app_python3.exec_p1(str "method", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.exec_p1'>📖 kamailio.cfg::exec_p1()</a>

#### KSR.app_python3.execx() ####

```cpp
int KSR.app_python3.execx(str "method");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_python3.html#app_python3.f.execx'>📖 kamailio.cfg::execx()</a>

## app_ruby ##

#### KSR.app_ruby.run() ####

```cpp
int KSR.app_ruby.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run'>📖 kamailio.cfg::run()</a>

#### KSR.app_ruby.run_p1() ####

```cpp
int KSR.app_ruby.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p1'>📖 kamailio.cfg::run_p1()</a>

#### KSR.app_ruby.run_p2() ####

```cpp
int KSR.app_ruby.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p2'>📖 kamailio.cfg::run_p2()</a>

#### KSR.app_ruby.run_p3() ####

```cpp
int KSR.app_ruby.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p3'>📖 kamailio.cfg::run_p3()</a>

## app_sqlang ##

#### KSR.app_sqlang.dofile() ####

```cpp
int KSR.app_sqlang.dofile(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dofile'>📖 kamailio.cfg::dofile()</a>

#### KSR.app_sqlang.dostring() ####

```cpp
int KSR.app_sqlang.dostring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dostring'>📖 kamailio.cfg::dostring()</a>

#### KSR.app_sqlang.run() ####

```cpp
int KSR.app_sqlang.run(str "func");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run'>📖 kamailio.cfg::run()</a>

#### KSR.app_sqlang.run_p1() ####

```cpp
int KSR.app_sqlang.run_p1(str "func", str "p1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p1'>📖 kamailio.cfg::run_p1()</a>

#### KSR.app_sqlang.run_p2() ####

```cpp
int KSR.app_sqlang.run_p2(str "func", str "p1", str "p2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p2'>📖 kamailio.cfg::run_p2()</a>

#### KSR.app_sqlang.run_p3() ####

```cpp
int KSR.app_sqlang.run_p3(str "func", str "p1", str "p2", str "p3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p3'>📖 kamailio.cfg::run_p3()</a>

#### KSR.app_sqlang.runstring() ####

```cpp
int KSR.app_sqlang.runstring(str "script");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.runstring'>📖 kamailio.cfg::runstring()</a>

## async ##

#### KSR.async.ms_route() ####

```cpp
int KSR.async.ms_route(str "rn", int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.ms_route'>📖 kamailio.cfg::ms_route()</a>

#### KSR.async.route() ####

```cpp
int KSR.async.route(str "rn", int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.route'>📖 kamailio.cfg::route()</a>

#### KSR.async.task_route() ####

```cpp
int KSR.async.task_route(str "rn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/async.html#async.f.task_route'>📖 kamailio.cfg::task_route()</a>

## auth ##

#### KSR.auth.auth_challenge() ####

```cpp
int KSR.auth.auth_challenge(str "realm", int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.auth_challenge'>📖 kamailio.cfg::auth_challenge()</a>

#### KSR.auth.consume_credentials() ####

```cpp
int KSR.auth.consume_credentials();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.consume_credentials'>📖 kamailio.cfg::consume_credentials()</a>

#### KSR.auth.has_credentials() ####

```cpp
int KSR.auth.has_credentials(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.has_credentials'>📖 kamailio.cfg::has_credentials()</a>

#### KSR.auth.pv_auth_check() ####

```cpp
int KSR.auth.pv_auth_check(str "srealm", str "spasswd", int vflags, int vchecks);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth.html#auth.f.pv_auth_check'>📖 kamailio.cfg::pv_auth_check()</a>

## auth_db ##

#### KSR.auth_db.auth_check() ####

```cpp
int KSR.auth_db.auth_check(str "srealm", str "stable", int iflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.auth_check'>📖 kamailio.cfg::auth_check()</a>

#### KSR.auth_db.is_subscriber() ####

```cpp
int KSR.auth_db.is_subscriber(str "suri", str "stable", int iflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_db.html#auth_db.f.is_subscriber'>📖 kamailio.cfg::is_subscriber()</a>

## auth_ephemeral ##

#### KSR.auth_ephemeral.autheph_authenticate() ####

```cpp
int KSR.auth_ephemeral.autheph_authenticate(str "susername", str "spassword");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_authenticate'>📖 kamailio.cfg::autheph_authenticate()</a>

#### KSR.auth_ephemeral.autheph_check() ####

```cpp
int KSR.auth_ephemeral.autheph_check(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_check'>📖 kamailio.cfg::autheph_check()</a>

#### KSR.auth_ephemeral.autheph_proxy() ####

```cpp
int KSR.auth_ephemeral.autheph_proxy(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_proxy'>📖 kamailio.cfg::autheph_proxy()</a>

#### KSR.auth_ephemeral.autheph_www() ####

```cpp
int KSR.auth_ephemeral.autheph_www(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www'>📖 kamailio.cfg::autheph_www()</a>

#### KSR.auth_ephemeral.autheph_www_method() ####

```cpp
int KSR.auth_ephemeral.autheph_www_method(str "srealm", str "smethod");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www_method'>📖 kamailio.cfg::autheph_www_method()</a>

## auth_radius ##

#### KSR.auth_radius.proxy_authorize() ####

```cpp
int KSR.auth_radius.proxy_authorize(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize'>📖 kamailio.cfg::proxy_authorize()</a>

#### KSR.auth_radius.proxy_authorize_user() ####

```cpp
int KSR.auth_radius.proxy_authorize_user(str "srealm", str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize_user'>📖 kamailio.cfg::proxy_authorize_user()</a>

#### KSR.auth_radius.www_authorize() ####

```cpp
int KSR.auth_radius.www_authorize(str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize'>📖 kamailio.cfg::www_authorize()</a>

#### KSR.auth_radius.www_authorize_user() ####

```cpp
int KSR.auth_radius.www_authorize_user(str "srealm", str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize_user'>📖 kamailio.cfg::www_authorize_user()</a>

## auth_xkeys ##

#### KSR.auth_xkeys.auth_xkeys_add() ####

```cpp
int KSR.auth_xkeys.auth_xkeys_add(str "shdr", str "skey", str "salg", str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_add'>📖 kamailio.cfg::auth_xkeys_add()</a>

#### KSR.auth_xkeys.auth_xkeys_check() ####

```cpp
int KSR.auth_xkeys.auth_xkeys_check(str "shdr", str "skey", str "salg", str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_check'>📖 kamailio.cfg::auth_xkeys_check()</a>

## avpops ##

#### KSR.avpops.avp_check() ####

```cpp
int KSR.avpops.avp_check(str "param", str "check");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/avpops.html#avpops.f.avp_check'>📖 kamailio.cfg::avp_check()</a>

#### KSR.avpops.avp_copy() ####

```cpp
int KSR.avpops.avp_copy(str "name1", str "name2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/avpops.html#avpops.f.avp_copy'>📖 kamailio.cfg::avp_copy()</a>

## benchmark ##

#### KSR.benchmark.bm_log_timer() ####

```cpp
int KSR.benchmark.bm_log_timer(str "tname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_log_timer'>📖 kamailio.cfg::bm_log_timer()</a>

#### KSR.benchmark.bm_start_timer() ####

```cpp
int KSR.benchmark.bm_start_timer(str "tname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_start_timer'>📖 kamailio.cfg::bm_start_timer()</a>

## blst ##

#### KSR.blst.blst_add() ####

```cpp
int KSR.blst.blst_add(int t);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add'>📖 kamailio.cfg::blst_add()</a>

#### KSR.blst.blst_add_default() ####

```cpp
int KSR.blst.blst_add_default();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add_default'>📖 kamailio.cfg::blst_add_default()</a>

#### KSR.blst.blst_add_retry_after() ####

```cpp
int KSR.blst.blst_add_retry_after(int t_min, int t_max);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_add_retry_after'>📖 kamailio.cfg::blst_add_retry_after()</a>

#### KSR.blst.blst_clear_ignore() ####

```cpp
int KSR.blst.blst_clear_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore'>📖 kamailio.cfg::blst_clear_ignore()</a>

#### KSR.blst.blst_clear_ignore_all() ####

```cpp
int KSR.blst.blst_clear_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore_all'>📖 kamailio.cfg::blst_clear_ignore_all()</a>

#### KSR.blst.blst_del() ####

```cpp
int KSR.blst.blst_del();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_del'>📖 kamailio.cfg::blst_del()</a>

#### KSR.blst.blst_is_blocklisted() ####

```cpp
int KSR.blst.blst_is_blocklisted();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_is_blocklisted'>📖 kamailio.cfg::blst_is_blocklisted()</a>

#### KSR.blst.blst_rpl_clear_ignore() ####

```cpp
int KSR.blst.blst_rpl_clear_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore'>📖 kamailio.cfg::blst_rpl_clear_ignore()</a>

#### KSR.blst.blst_rpl_clear_ignore_all() ####

```cpp
int KSR.blst.blst_rpl_clear_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore_all'>📖 kamailio.cfg::blst_rpl_clear_ignore_all()</a>

#### KSR.blst.blst_rpl_set_ignore() ####

```cpp
int KSR.blst.blst_rpl_set_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore'>📖 kamailio.cfg::blst_rpl_set_ignore()</a>

#### KSR.blst.blst_rpl_set_ignore_all() ####

```cpp
int KSR.blst.blst_rpl_set_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore_all'>📖 kamailio.cfg::blst_rpl_set_ignore_all()</a>

#### KSR.blst.blst_set_ignore() ####

```cpp
int KSR.blst.blst_set_ignore(int mask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore'>📖 kamailio.cfg::blst_set_ignore()</a>

#### KSR.blst.blst_set_ignore_all() ####

```cpp
int KSR.blst.blst_set_ignore_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore_all'>📖 kamailio.cfg::blst_set_ignore_all()</a>

## call_control ##

#### KSR.call_control.call_control() ####

```cpp
int KSR.call_control.call_control();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_control.html#call_control.f.call_control'>📖 kamailio.cfg::call_control()</a>

## call_obj ##

#### KSR.call_obj.free() ####

```cpp
int KSR.call_obj.free(int num_obj);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_obj.html#call_obj.f.free'>📖 kamailio.cfg::free()</a>

#### KSR.call_obj.get() ####

```cpp
int KSR.call_obj.get();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/call_obj.html#call_obj.f.get'>📖 kamailio.cfg::get()</a>

## cfgutils ##

#### KSR.cfgutils.abort() ####

```cpp
int KSR.cfgutils.abort();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.abort'>📖 kamailio.cfg::abort()</a>

#### KSR.cfgutils.check_route_exists() ####

```cpp
int KSR.cfgutils.check_route_exists(str "route");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.check_route_exists'>📖 kamailio.cfg::check_route_exists()</a>

#### KSR.cfgutils.core_hash() ####

```cpp
int KSR.cfgutils.core_hash(str "s1", str "s2", int sz);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.core_hash'>📖 kamailio.cfg::core_hash()</a>

#### KSR.cfgutils.lock() ####

```cpp
int KSR.cfgutils.lock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.lock'>📖 kamailio.cfg::lock()</a>

#### KSR.cfgutils.pkg_status() ####

```cpp
int KSR.cfgutils.pkg_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_status'>📖 kamailio.cfg::pkg_status()</a>

#### KSR.cfgutils.pkg_summary() ####

```cpp
int KSR.cfgutils.pkg_summary();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_summary'>📖 kamailio.cfg::pkg_summary()</a>

#### KSR.cfgutils.rand_event() ####

```cpp
int KSR.cfgutils.rand_event();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_event'>📖 kamailio.cfg::rand_event()</a>

#### KSR.cfgutils.rand_get_prob() ####

```cpp
int KSR.cfgutils.rand_get_prob();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_get_prob'>📖 kamailio.cfg::rand_get_prob()</a>

#### KSR.cfgutils.rand_reset_prob() ####

```cpp
int KSR.cfgutils.rand_reset_prob();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_reset_prob'>📖 kamailio.cfg::rand_reset_prob()</a>

#### KSR.cfgutils.rand_set_prob() ####

```cpp
int KSR.cfgutils.rand_set_prob(int percent_par);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_set_prob'>📖 kamailio.cfg::rand_set_prob()</a>

#### KSR.cfgutils.route_if_exists() ####

```cpp
int KSR.cfgutils.route_if_exists(str "route");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.route_if_exists'>📖 kamailio.cfg::route_if_exists()</a>

#### KSR.cfgutils.shm_status() ####

```cpp
int KSR.cfgutils.shm_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_status'>📖 kamailio.cfg::shm_status()</a>

#### KSR.cfgutils.shm_summary() ####

```cpp
int KSR.cfgutils.shm_summary();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_summary'>📖 kamailio.cfg::shm_summary()</a>

#### KSR.cfgutils.sleep() ####

```cpp
int KSR.cfgutils.sleep(int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.sleep'>📖 kamailio.cfg::sleep()</a>

#### KSR.cfgutils.trylock() ####

```cpp
int KSR.cfgutils.trylock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.trylock'>📖 kamailio.cfg::trylock()</a>

#### KSR.cfgutils.unlock() ####

```cpp
int KSR.cfgutils.unlock(str "lkey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.unlock'>📖 kamailio.cfg::unlock()</a>

#### KSR.cfgutils.usleep() ####

```cpp
int KSR.cfgutils.usleep(int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cfgutils.html#cfgutils.f.usleep'>📖 kamailio.cfg::usleep()</a>

## cnxcc ##

#### KSR.cnxcc.get_channel_count() ####

```cpp
int KSR.cnxcc.get_channel_count(str "sclient", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.get_channel_count'>📖 kamailio.cfg::get_channel_count()</a>

#### KSR.cnxcc.set_max_channels() ####

```cpp
int KSR.cnxcc.set_max_channels(str "sclient", int max_chan);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_channels'>📖 kamailio.cfg::set_max_channels()</a>

#### KSR.cnxcc.set_max_credit() ####

```cpp
int KSR.cnxcc.set_max_credit(str "sclient", str "scredit", str "sconnect", str "scps", int initp, int finishp);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_credit'>📖 kamailio.cfg::set_max_credit()</a>

#### KSR.cnxcc.set_max_time() ####

```cpp
int KSR.cnxcc.set_max_time(str "sclient", int max_secs);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_time'>📖 kamailio.cfg::set_max_time()</a>

#### KSR.cnxcc.terminate_all() ####

```cpp
int KSR.cnxcc.terminate_all(str "sclient");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.terminate_all'>📖 kamailio.cfg::terminate_all()</a>

#### KSR.cnxcc.update_max_time() ####

```cpp
int KSR.cnxcc.update_max_time(str "sclient", int secs);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/cnxcc.html#cnxcc.f.update_max_time'>📖 kamailio.cfg::update_max_time()</a>

## corex ##

#### KSR.corex.append_branch() ####

```cpp
int KSR.corex.append_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch'>📖 kamailio.cfg::append_branch()</a>

#### KSR.corex.append_branch_uri() ####

```cpp
int KSR.corex.append_branch_uri(str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri'>📖 kamailio.cfg::append_branch_uri()</a>

#### KSR.corex.append_branch_uri_q() ####

```cpp
int KSR.corex.append_branch_uri_q(str "uri", str "q");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri_q'>📖 kamailio.cfg::append_branch_uri_q()</a>

#### KSR.corex.file_read() ####

```cpp
xval KSR.corex.file_read(str "fname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_read'>📖 kamailio.cfg::file_read()</a>

#### KSR.corex.file_write() ####

```cpp
int KSR.corex.file_write(str "fname", str "fdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.file_write'>📖 kamailio.cfg::file_write()</a>

#### KSR.corex.has_ruri_user() ####

```cpp
int KSR.corex.has_ruri_user();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_ruri_user'>📖 kamailio.cfg::has_ruri_user()</a>

#### KSR.corex.has_user_agent() ####

```cpp
int KSR.corex.has_user_agent();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.has_user_agent'>📖 kamailio.cfg::has_user_agent()</a>

#### KSR.corex.is_faked_msg() ####

```cpp
int KSR.corex.is_faked_msg();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_faked_msg'>📖 kamailio.cfg::is_faked_msg()</a>

#### KSR.corex.is_socket_name() ####

```cpp
int KSR.corex.is_socket_name(str "sockname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.is_socket_name'>📖 kamailio.cfg::is_socket_name()</a>

#### KSR.corex.isxflagset() ####

```cpp
int KSR.corex.isxflagset(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.isxflagset'>📖 kamailio.cfg::isxflagset()</a>

#### KSR.corex.resetxflag() ####

```cpp
int KSR.corex.resetxflag(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.resetxflag'>📖 kamailio.cfg::resetxflag()</a>

#### KSR.corex.send_data() ####

```cpp
int KSR.corex.send_data(str "uri", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.send_data'>📖 kamailio.cfg::send_data()</a>

#### KSR.corex.sendx() ####

```cpp
int KSR.corex.sendx(str "uri", str "sock", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.sendx'>📖 kamailio.cfg::sendx()</a>

#### KSR.corex.set_recv_socket() ####

```cpp
int KSR.corex.set_recv_socket(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket'>📖 kamailio.cfg::set_recv_socket()</a>

#### KSR.corex.set_recv_socket_name() ####

```cpp
int KSR.corex.set_recv_socket_name(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket_name'>📖 kamailio.cfg::set_recv_socket_name()</a>

#### KSR.corex.set_send_socket() ####

```cpp
int KSR.corex.set_send_socket(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket'>📖 kamailio.cfg::set_send_socket()</a>

#### KSR.corex.set_send_socket_name() ####

```cpp
int KSR.corex.set_send_socket_name(str "ssock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_send_socket_name'>📖 kamailio.cfg::set_send_socket_name()</a>

#### KSR.corex.set_source_address() ####

```cpp
int KSR.corex.set_source_address(str "saddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.set_source_address'>📖 kamailio.cfg::set_source_address()</a>

#### KSR.corex.setxflag() ####

```cpp
int KSR.corex.setxflag(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.setxflag'>📖 kamailio.cfg::setxflag()</a>

#### KSR.corex.via_add_srvid() ####

```cpp
int KSR.corex.via_add_srvid(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_srvid'>📖 kamailio.cfg::via_add_srvid()</a>

#### KSR.corex.via_add_xavp_params() ####

```cpp
int KSR.corex.via_add_xavp_params(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_add_xavp_params'>📖 kamailio.cfg::via_add_xavp_params()</a>

#### KSR.corex.via_use_xavp_fields() ####

```cpp
int KSR.corex.via_use_xavp_fields(int fval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/corex.html#corex.f.via_use_xavp_fields'>📖 kamailio.cfg::via_use_xavp_fields()</a>

## counters ##

#### KSR.counters.add() ####

```cpp
int KSR.counters.add(str "sname", int v);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.add'>📖 kamailio.cfg::add()</a>

#### KSR.counters.inc() ####

```cpp
int KSR.counters.inc(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.inc'>📖 kamailio.cfg::inc()</a>

#### KSR.counters.reset() ####

```cpp
int KSR.counters.reset(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/counters.html#counters.f.reset'>📖 kamailio.cfg::reset()</a>

## crypto ##

#### KSR.crypto.aes_decrypt() ####

```cpp
int KSR.crypto.aes_decrypt(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.aes_decrypt'>📖 kamailio.cfg::aes_decrypt()</a>

#### KSR.crypto.aes_encrypt() ####

```cpp
int KSR.crypto.aes_encrypt(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.aes_encrypt'>📖 kamailio.cfg::aes_encrypt()</a>

#### KSR.crypto.hmac_sha256() ####

```cpp
int KSR.crypto.hmac_sha256(str "ins", str "keys", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/crypto.html#crypto.f.hmac_sha256'>📖 kamailio.cfg::hmac_sha256()</a>

## debugger ##

#### KSR.debugger.dbg_pv_dump() ####

```cpp
int KSR.debugger.dbg_pv_dump();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump'>📖 kamailio.cfg::dbg_pv_dump()</a>

#### KSR.debugger.dbg_pv_dump_ex() ####

```cpp
int KSR.debugger.dbg_pv_dump_ex(int mask, int level);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump_ex'>📖 kamailio.cfg::dbg_pv_dump_ex()</a>

## dialog ##

#### KSR.dialog.dlg_bridge() ####

```cpp
int KSR.dialog.dlg_bridge(str "sfrom", str "sto", str "soproxy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bridge'>📖 kamailio.cfg::dlg_bridge()</a>

#### KSR.dialog.dlg_bye() ####

```cpp
int KSR.dialog.dlg_bye(str "side");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bye'>📖 kamailio.cfg::dlg_bye()</a>

#### KSR.dialog.dlg_db_load_callid() ####

```cpp
int KSR.dialog.dlg_db_load_callid(str "callid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_callid'>📖 kamailio.cfg::dlg_db_load_callid()</a>

#### KSR.dialog.dlg_db_load_extra() ####

```cpp
int KSR.dialog.dlg_db_load_extra();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_extra'>📖 kamailio.cfg::dlg_db_load_extra()</a>

#### KSR.dialog.dlg_get() ####

```cpp
int KSR.dialog.dlg_get(str "sc", str "sf", str "st");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_get'>📖 kamailio.cfg::dlg_get()</a>

#### KSR.dialog.dlg_isflagset() ####

```cpp
int KSR.dialog.dlg_isflagset(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_isflagset'>📖 kamailio.cfg::dlg_isflagset()</a>

#### KSR.dialog.dlg_manage() ####

```cpp
int KSR.dialog.dlg_manage();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_manage'>📖 kamailio.cfg::dlg_manage()</a>

#### KSR.dialog.dlg_reset_property() ####

```cpp
int KSR.dialog.dlg_reset_property(str "pval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_reset_property'>📖 kamailio.cfg::dlg_reset_property()</a>

#### KSR.dialog.dlg_resetflag() ####

```cpp
int KSR.dialog.dlg_resetflag(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_resetflag'>📖 kamailio.cfg::dlg_resetflag()</a>

#### KSR.dialog.dlg_set_property() ####

```cpp
int KSR.dialog.dlg_set_property(str "pval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_property'>📖 kamailio.cfg::dlg_set_property()</a>

#### KSR.dialog.dlg_set_timeout() ####

```cpp
int KSR.dialog.dlg_set_timeout(int to);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout'>📖 kamailio.cfg::dlg_set_timeout()</a>

#### KSR.dialog.dlg_set_timeout_id() ####

```cpp
int KSR.dialog.dlg_set_timeout_id(int to, int he, int hi);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout_id'>📖 kamailio.cfg::dlg_set_timeout_id()</a>

#### KSR.dialog.dlg_setflag() ####

```cpp
int KSR.dialog.dlg_setflag(int val);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.dlg_setflag'>📖 kamailio.cfg::dlg_setflag()</a>

#### KSR.dialog.get_profile_size() ####

```cpp
int KSR.dialog.get_profile_size(str "sprofile", str "svalue", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size'>📖 kamailio.cfg::get_profile_size()</a>

#### KSR.dialog.get_profile_size_static() ####

```cpp
int KSR.dialog.get_profile_size_static(str "sprofile", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size_static'>📖 kamailio.cfg::get_profile_size_static()</a>

#### KSR.dialog.is_in_profile() ####

```cpp
int KSR.dialog.is_in_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile'>📖 kamailio.cfg::is_in_profile()</a>

#### KSR.dialog.is_in_profile_static() ####

```cpp
int KSR.dialog.is_in_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile_static'>📖 kamailio.cfg::is_in_profile_static()</a>

#### KSR.dialog.is_known_dlg() ####

```cpp
int KSR.dialog.is_known_dlg();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.is_known_dlg'>📖 kamailio.cfg::is_known_dlg()</a>

#### KSR.dialog.set_dlg_profile() ####

```cpp
int KSR.dialog.set_dlg_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile'>📖 kamailio.cfg::set_dlg_profile()</a>

#### KSR.dialog.set_dlg_profile_static() ####

```cpp
int KSR.dialog.set_dlg_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile_static'>📖 kamailio.cfg::set_dlg_profile_static()</a>

#### KSR.dialog.unset_dlg_profile() ####

```cpp
int KSR.dialog.unset_dlg_profile(str "sprofile", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile'>📖 kamailio.cfg::unset_dlg_profile()</a>

#### KSR.dialog.unset_dlg_profile_static() ####

```cpp
int KSR.dialog.unset_dlg_profile_static(str "sprofile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile_static'>📖 kamailio.cfg::unset_dlg_profile_static()</a>

#### KSR.dialog.var_get() ####

```cpp
xval KSR.dialog.var_get(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_get'>📖 kamailio.cfg::var_get()</a>

#### KSR.dialog.var_gete() ####

```cpp
xval KSR.dialog.var_gete(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_gete'>📖 kamailio.cfg::var_gete()</a>

#### KSR.dialog.var_getw() ####

```cpp
xval KSR.dialog.var_getw(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_getw'>📖 kamailio.cfg::var_getw()</a>

#### KSR.dialog.var_is_null() ####

```cpp
int KSR.dialog.var_is_null(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_is_null'>📖 kamailio.cfg::var_is_null()</a>

#### KSR.dialog.var_rm() ####

```cpp
int KSR.dialog.var_rm(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_rm'>📖 kamailio.cfg::var_rm()</a>

#### KSR.dialog.var_sets() ####

```cpp
int KSR.dialog.var_sets(str "name", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialog.html#dialog.f.var_sets'>📖 kamailio.cfg::var_sets()</a>

## dialplan ##

#### KSR.dialplan.dp_match() ####

```cpp
int KSR.dialplan.dp_match(int dpid, str "src");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_match'>📖 kamailio.cfg::dp_match()</a>

#### KSR.dialplan.dp_replace() ####

```cpp
int KSR.dialplan.dp_replace(int dpid, str "src", str "dst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_replace'>📖 kamailio.cfg::dp_replace()</a>

## dispatcher ##

#### KSR.dispatcher.ds_is_from_list() ####

```cpp
int KSR.dispatcher.ds_is_from_list(int group);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list'>📖 kamailio.cfg::ds_is_from_list()</a>

#### KSR.dispatcher.ds_is_from_list_mode() ####

```cpp
int KSR.dispatcher.ds_is_from_list_mode(int vset, int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_mode'>📖 kamailio.cfg::ds_is_from_list_mode()</a>

#### KSR.dispatcher.ds_is_from_list_uri() ####

```cpp
int KSR.dispatcher.ds_is_from_list_uri(int vset, int vmode, str "vuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_uri'>📖 kamailio.cfg::ds_is_from_list_uri()</a>

#### KSR.dispatcher.ds_is_from_lists() ####

```cpp
int KSR.dispatcher.ds_is_from_lists();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_lists'>📖 kamailio.cfg::ds_is_from_lists()</a>

#### KSR.dispatcher.ds_list_exists() ####

```cpp
int KSR.dispatcher.ds_list_exists(int set);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_list_exists'>📖 kamailio.cfg::ds_list_exists()</a>

#### KSR.dispatcher.ds_load_unset() ####

```cpp
int KSR.dispatcher.ds_load_unset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_unset'>📖 kamailio.cfg::ds_load_unset()</a>

#### KSR.dispatcher.ds_load_update() ####

```cpp
int KSR.dispatcher.ds_load_update();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_update'>📖 kamailio.cfg::ds_load_update()</a>

#### KSR.dispatcher.ds_mark_dst() ####

```cpp
int KSR.dispatcher.ds_mark_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst'>📖 kamailio.cfg::ds_mark_dst()</a>

#### KSR.dispatcher.ds_mark_dst_state() ####

```cpp
int KSR.dispatcher.ds_mark_dst_state(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst_state'>📖 kamailio.cfg::ds_mark_dst_state()</a>

#### KSR.dispatcher.ds_next_domain() ####

```cpp
int KSR.dispatcher.ds_next_domain();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_domain'>📖 kamailio.cfg::ds_next_domain()</a>

#### KSR.dispatcher.ds_next_dst() ####

```cpp
int KSR.dispatcher.ds_next_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_dst'>📖 kamailio.cfg::ds_next_dst()</a>

#### KSR.dispatcher.ds_reload() ####

```cpp
int KSR.dispatcher.ds_reload();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_reload'>📖 kamailio.cfg::ds_reload()</a>

#### KSR.dispatcher.ds_select() ####

```cpp
int KSR.dispatcher.ds_select(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select'>📖 kamailio.cfg::ds_select()</a>

#### KSR.dispatcher.ds_select_domain() ####

```cpp
int KSR.dispatcher.ds_select_domain(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain'>📖 kamailio.cfg::ds_select_domain()</a>

#### KSR.dispatcher.ds_select_domain_limit() ####

```cpp
int KSR.dispatcher.ds_select_domain_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain_limit'>📖 kamailio.cfg::ds_select_domain_limit()</a>

#### KSR.dispatcher.ds_select_dst() ####

```cpp
int KSR.dispatcher.ds_select_dst(int set, int alg);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst'>📖 kamailio.cfg::ds_select_dst()</a>

#### KSR.dispatcher.ds_select_dst_limit() ####

```cpp
int KSR.dispatcher.ds_select_dst_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst_limit'>📖 kamailio.cfg::ds_select_dst_limit()</a>

#### KSR.dispatcher.ds_select_limit() ####

```cpp
int KSR.dispatcher.ds_select_limit(int set, int alg, int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_limit'>📖 kamailio.cfg::ds_select_limit()</a>

#### KSR.dispatcher.ds_select_routes() ####

```cpp
int KSR.dispatcher.ds_select_routes(str "srules", str "smode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes'>📖 kamailio.cfg::ds_select_routes()</a>

#### KSR.dispatcher.ds_select_routes_limit() ####

```cpp
int KSR.dispatcher.ds_select_routes_limit(str "srules", str "smode", int rlimit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes_limit'>📖 kamailio.cfg::ds_select_routes_limit()</a>

#### KSR.dispatcher.ds_set_domain() ####

```cpp
int KSR.dispatcher.ds_set_domain();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_domain'>📖 kamailio.cfg::ds_set_domain()</a>

#### KSR.dispatcher.ds_set_dst() ####

```cpp
int KSR.dispatcher.ds_set_dst();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_dst'>📖 kamailio.cfg::ds_set_dst()</a>

## diversion ##

#### KSR.diversion.add_diversion() ####

```cpp
int KSR.diversion.add_diversion(str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion'>📖 kamailio.cfg::add_diversion()</a>

#### KSR.diversion.add_diversion_uri() ####

```cpp
int KSR.diversion.add_diversion_uri(str "reason", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion_uri'>📖 kamailio.cfg::add_diversion_uri()</a>

## dlgs ##

#### KSR.dlgs.dlgs_count() ####

```cpp
int KSR.dlgs.dlgs_count(str "vfield", str "vop", str "vdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_count'>📖 kamailio.cfg::dlgs_count()</a>

#### KSR.dlgs.dlgs_init() ####

```cpp
int KSR.dlgs.dlgs_init(str "src", str "dst", str "data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_init'>📖 kamailio.cfg::dlgs_init()</a>

#### KSR.dlgs.dlgs_tags_add() ####

```cpp
int KSR.dlgs.dlgs_tags_add(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_add'>📖 kamailio.cfg::dlgs_tags_add()</a>

#### KSR.dlgs.dlgs_tags_count() ####

```cpp
int KSR.dlgs.dlgs_tags_count(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_count'>📖 kamailio.cfg::dlgs_tags_count()</a>

#### KSR.dlgs.dlgs_tags_rm() ####

```cpp
int KSR.dlgs.dlgs_tags_rm(str "vtags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_tags_rm'>📖 kamailio.cfg::dlgs_tags_rm()</a>

#### KSR.dlgs.dlgs_update() ####

```cpp
int KSR.dlgs.dlgs_update();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dlgs.html#dlgs.f.dlgs_update'>📖 kamailio.cfg::dlgs_update()</a>

## dmq ##

#### KSR.dmq.bcast_message() ####

```cpp
int KSR.dmq.bcast_message(str "peer_str", str "body_str", str "ct_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.bcast_message'>📖 kamailio.cfg::bcast_message()</a>

#### KSR.dmq.handle_message() ####

```cpp
int KSR.dmq.handle_message();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message'>📖 kamailio.cfg::handle_message()</a>

#### KSR.dmq.handle_message_rc() ####

```cpp
int KSR.dmq.handle_message_rc(int returnval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.handle_message_rc'>📖 kamailio.cfg::handle_message_rc()</a>

#### KSR.dmq.is_from_node() ####

```cpp
int KSR.dmq.is_from_node();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.is_from_node'>📖 kamailio.cfg::is_from_node()</a>

#### KSR.dmq.send_message() ####

```cpp
int KSR.dmq.send_message(str "peer_str", str "to_str", str "body_str", str "ct_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.send_message'>📖 kamailio.cfg::send_message()</a>

#### KSR.dmq.t_replicate() ####

```cpp
int KSR.dmq.t_replicate();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate'>📖 kamailio.cfg::t_replicate()</a>

#### KSR.dmq.t_replicate_mode() ####

```cpp
int KSR.dmq.t_replicate_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate_mode'>📖 kamailio.cfg::t_replicate_mode()</a>

## domain ##

#### KSR.domain.is_domain_local() ####

```cpp
int KSR.domain.is_domain_local(str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_domain_local'>📖 kamailio.cfg::is_domain_local()</a>

#### KSR.domain.is_from_local() ####

```cpp
int KSR.domain.is_from_local();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_from_local'>📖 kamailio.cfg::is_from_local()</a>

#### KSR.domain.is_uri_host_local() ####

```cpp
int KSR.domain.is_uri_host_local();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.is_uri_host_local'>📖 kamailio.cfg::is_uri_host_local()</a>

#### KSR.domain.lookup_domain() ####

```cpp
int KSR.domain.lookup_domain(str "_sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain'>📖 kamailio.cfg::lookup_domain()</a>

#### KSR.domain.lookup_domain_prefix() ####

```cpp
int KSR.domain.lookup_domain_prefix(str "_sdomain", str "_sprefix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/domain.html#domain.f.lookup_domain_prefix'>📖 kamailio.cfg::lookup_domain_prefix()</a>

## drouting ##

#### KSR.drouting.do_routing() ####

```cpp
int KSR.drouting.do_routing(int grp_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.do_routing'>📖 kamailio.cfg::do_routing()</a>

#### KSR.drouting.do_routing_furi() ####

```cpp
int KSR.drouting.do_routing_furi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.do_routing_furi'>📖 kamailio.cfg::do_routing_furi()</a>

#### KSR.drouting.goes_to_gw() ####

```cpp
int KSR.drouting.goes_to_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw'>📖 kamailio.cfg::goes_to_gw()</a>

#### KSR.drouting.goes_to_gw_type() ####

```cpp
int KSR.drouting.goes_to_gw_type(int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw_type'>📖 kamailio.cfg::goes_to_gw_type()</a>

#### KSR.drouting.is_from_gw() ####

```cpp
int KSR.drouting.is_from_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw'>📖 kamailio.cfg::is_from_gw()</a>

#### KSR.drouting.is_from_gw_type() ####

```cpp
int KSR.drouting.is_from_gw_type(int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type'>📖 kamailio.cfg::is_from_gw_type()</a>

#### KSR.drouting.is_from_gw_type_flags() ####

```cpp
int KSR.drouting.is_from_gw_type_flags(int type, int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type_flags'>📖 kamailio.cfg::is_from_gw_type_flags()</a>

#### KSR.drouting.next_routing() ####

```cpp
int KSR.drouting.next_routing();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.next_routing'>📖 kamailio.cfg::next_routing()</a>

#### KSR.drouting.use_next_gw() ####

```cpp
int KSR.drouting.use_next_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/drouting.html#drouting.f.use_next_gw'>📖 kamailio.cfg::use_next_gw()</a>

## enum ##

#### KSR.enum.enum_i_query_suffix() ####

```cpp
int KSR.enum.enum_i_query_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_i_query_suffix'>📖 kamailio.cfg::enum_i_query_suffix()</a>

#### KSR.enum.enum_pv_query() ####

```cpp
int KSR.enum.enum_pv_query(str "ve164");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query'>📖 kamailio.cfg::enum_pv_query()</a>

#### KSR.enum.enum_pv_query_suffix() ####

```cpp
int KSR.enum.enum_pv_query_suffix(str "ve164", str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix'>📖 kamailio.cfg::enum_pv_query_suffix()</a>

#### KSR.enum.enum_pv_query_suffix_service() ####

```cpp
int KSR.enum.enum_pv_query_suffix_service(str "ve164", str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix_service'>📖 kamailio.cfg::enum_pv_query_suffix_service()</a>

#### KSR.enum.enum_query() ####

```cpp
int KSR.enum.enum_query();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query'>📖 kamailio.cfg::enum_query()</a>

#### KSR.enum.enum_query_suffix() ####

```cpp
int KSR.enum.enum_query_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix'>📖 kamailio.cfg::enum_query_suffix()</a>

#### KSR.enum.enum_query_suffix_service() ####

```cpp
int KSR.enum.enum_query_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix_service'>📖 kamailio.cfg::enum_query_suffix_service()</a>

#### KSR.enum.i_enum_query() ####

```cpp
int KSR.enum.i_enum_query();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query'>📖 kamailio.cfg::i_enum_query()</a>

#### KSR.enum.i_enum_query_suffix_service() ####

```cpp
int KSR.enum.i_enum_query_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.i_enum_query_suffix_service'>📖 kamailio.cfg::i_enum_query_suffix_service()</a>

#### KSR.enum.is_from_user_enum() ####

```cpp
int KSR.enum.is_from_user_enum();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum'>📖 kamailio.cfg::is_from_user_enum()</a>

#### KSR.enum.is_from_user_enum_suffix() ####

```cpp
int KSR.enum.is_from_user_enum_suffix(str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix'>📖 kamailio.cfg::is_from_user_enum_suffix()</a>

#### KSR.enum.is_from_user_enum_suffix_service() ####

```cpp
int KSR.enum.is_from_user_enum_suffix_service(str "vsuffix", str "vservice");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix_service'>📖 kamailio.cfg::is_from_user_enum_suffix_service()</a>

## evapi ##

#### KSR.evapi.async_multicast() ####

```cpp
int KSR.evapi.async_multicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_multicast'>📖 kamailio.cfg::async_multicast()</a>

#### KSR.evapi.async_relay() ####

```cpp
int KSR.evapi.async_relay(str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_relay'>📖 kamailio.cfg::async_relay()</a>

#### KSR.evapi.async_unicast() ####

```cpp
int KSR.evapi.async_unicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.async_unicast'>📖 kamailio.cfg::async_unicast()</a>

#### KSR.evapi.close() ####

```cpp
int KSR.evapi.close();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.close'>📖 kamailio.cfg::close()</a>

#### KSR.evapi.relay() ####

```cpp
int KSR.evapi.relay(str "sdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay'>📖 kamailio.cfg::relay()</a>

#### KSR.evapi.relay_multicast() ####

```cpp
int KSR.evapi.relay_multicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_multicast'>📖 kamailio.cfg::relay_multicast()</a>

#### KSR.evapi.relay_unicast() ####

```cpp
int KSR.evapi.relay_unicast(str "sdata", str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.relay_unicast'>📖 kamailio.cfg::relay_unicast()</a>

#### KSR.evapi.set_tag() ####

```cpp
int KSR.evapi.set_tag(str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/evapi.html#evapi.f.set_tag'>📖 kamailio.cfg::set_tag()</a>

## exec ##

#### KSR.exec.exec_avp() ####

```cpp
int KSR.exec.exec_avp(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_avp'>📖 kamailio.cfg::exec_avp()</a>

#### KSR.exec.exec_cmd() ####

```cpp
int KSR.exec.exec_cmd(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_cmd'>📖 kamailio.cfg::exec_cmd()</a>

#### KSR.exec.exec_dset() ####

```cpp
int KSR.exec.exec_dset(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_dset'>📖 kamailio.cfg::exec_dset()</a>

#### KSR.exec.exec_msg() ####

```cpp
int KSR.exec.exec_msg(str "cmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/exec.html#exec.f.exec_msg'>📖 kamailio.cfg::exec_msg()</a>

## geoip ##

#### KSR.geoip.match() ####

```cpp
int KSR.geoip.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip.html#geoip.f.match'>📖 kamailio.cfg::match()</a>

## geoip2 ##

#### KSR.geoip2.match() ####

```cpp
int KSR.geoip2.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/geoip2.html#geoip2.f.match'>📖 kamailio.cfg::match()</a>

## group ##

#### KSR.group.is_user_in() ####

```cpp
int KSR.group.is_user_in(str "uri", str "grp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/group.html#group.f.is_user_in'>📖 kamailio.cfg::is_user_in()</a>

## htable ##

Functions exported by `htable` module.

#### KSR.htable.sht_dec() ####

```cpp
int KSR.htable.sht_dec(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_dec'>📖 kamailio.cfg::sht_dec()</a>

Do atomic decrement to the item value. It returns the new value or `-255`
if the hash table does not exist, or the item does not exist or the item value
is not integer.

#### KSR.htable.sht_get() ####

```cpp
xval KSR.htable.sht_get(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_get'>📖 kamailio.cfg::sht_get()</a>

Return the integer or string value of the item.

If the item does not exists, it returns `NULL`. Note that `NULL` might be represented differently in various scripting languages, such as `nil` or `None`.

#### KSR.htable.sht_gete() ####

```cpp
xval KSR.htable.sht_gete(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_gete'>📖 kamailio.cfg::sht_gete()</a>

Return the integer or string value of the item.

If the item does not exists, it returns an empty string.

#### KSR.htable.sht_getw() ####

```cpp
xval KSR.htable.sht_getw(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_getw'>📖 kamailio.cfg::sht_getw()</a>

Return the integer or string value of the item.

If the item does not exists, it returns the string `<null>`, suitable for use
when writing log messages.

#### KSR.htable.sht_inc() ####

```cpp
int KSR.htable.sht_inc(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_inc'>📖 kamailio.cfg::sht_inc()</a>

Do atomic increment to the item value. It returns the new value or `-255`
if the hash table does not exist, or the item does not exist or the item value
is not integer.

#### KSR.htable.sht_is_null() ####

```cpp
int KSR.htable.sht_is_null(str "htname", str "itname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_is_null'>📖 kamailio.cfg::sht_is_null()</a>

#### KSR.htable.sht_iterator_end() ####

```cpp
int KSR.htable.sht_iterator_end(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_end'>📖 kamailio.cfg::sht_iterator_end()</a>

#### KSR.htable.sht_iterator_next() ####

```cpp
int KSR.htable.sht_iterator_next(str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_next'>📖 kamailio.cfg::sht_iterator_next()</a>

#### KSR.htable.sht_iterator_start() ####

```cpp
int KSR.htable.sht_iterator_start(str "iname", str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_start'>📖 kamailio.cfg::sht_iterator_start()</a>

#### KSR.htable.sht_lock() ####

```cpp
int KSR.htable.sht_lock(str "htname", str "skey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_lock'>📖 kamailio.cfg::sht_lock()</a>

#### KSR.htable.sht_match_name() ####

```cpp
int KSR.htable.sht_match_name(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_name'>📖 kamailio.cfg::sht_match_name()</a>

#### KSR.htable.sht_match_str_value() ####

```cpp
int KSR.htable.sht_match_str_value(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_match_str_value'>📖 kamailio.cfg::sht_match_str_value()</a>

#### KSR.htable.sht_reset() ####

```cpp
int KSR.htable.sht_reset(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_reset'>📖 kamailio.cfg::sht_reset()</a>

#### KSR.htable.sht_rm() ####

```cpp
int KSR.htable.sht_rm(str "hname", str "iname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm'>📖 kamailio.cfg::sht_rm()</a>

#### KSR.htable.sht_rm_name() ####

```cpp
int KSR.htable.sht_rm_name(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name'>📖 kamailio.cfg::sht_rm_name()</a>

#### KSR.htable.sht_rm_name_re() ####

```cpp
int KSR.htable.sht_rm_name_re(str "htname", str "rexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name_re'>📖 kamailio.cfg::sht_rm_name_re()</a>

#### KSR.htable.sht_rm_value() ####

```cpp
int KSR.htable.sht_rm_value(str "sname", str "sop", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value'>📖 kamailio.cfg::sht_rm_value()</a>

#### KSR.htable.sht_rm_value_re() ####

```cpp
int KSR.htable.sht_rm_value_re(str "htname", str "rexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value_re'>📖 kamailio.cfg::sht_rm_value_re()</a>

#### KSR.htable.sht_setex() ####

```cpp
int KSR.htable.sht_setex(str "htname", str "itname", int itval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setex'>📖 kamailio.cfg::sht_setex()</a>

#### KSR.htable.sht_seti() ####

```cpp
int KSR.htable.sht_seti(str "htname", str "itname", int itval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_seti'>📖 kamailio.cfg::sht_seti()</a>

#### KSR.htable.sht_sets() ####

```cpp
int KSR.htable.sht_sets(str "htname", str "itname", str "itval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_sets'>📖 kamailio.cfg::sht_sets()</a>

#### KSR.htable.sht_setxi() ####

```cpp
int KSR.htable.sht_setxi(str "htname", str "itname", int itval, int exval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxi'>📖 kamailio.cfg::sht_setxi()</a>

#### KSR.htable.sht_setxs() ####

```cpp
int KSR.htable.sht_setxs(str "htname", str "itname", str "itval", int exval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_setxs'>📖 kamailio.cfg::sht_setxs()</a>

#### KSR.htable.sht_unlock() ####

```cpp
int KSR.htable.sht_unlock(str "htname", str "skey");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/htable.html#htable.f.sht_unlock'>📖 kamailio.cfg::sht_unlock()</a>

## http_async_client ##

#### KSR.http_async_client.query() ####

```cpp
int KSR.http_async_client.query(str "sdata", str "rn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_async_client.html#http_async_client.f.query'>📖 kamailio.cfg::query()</a>

## http_client ##

#### KSR.http_client.curl_connect() ####

```cpp
int KSR.http_client.curl_connect(str "con", str "url", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect'>📖 kamailio.cfg::curl_connect()</a>

#### KSR.http_client.curl_connect_post() ####

```cpp
int KSR.http_client.curl_connect_post(str "con", str "url", str "ctype", str "data", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect_post'>📖 kamailio.cfg::curl_connect_post()</a>

#### KSR.http_client.get_hdrs() ####

```cpp
int KSR.http_client.get_hdrs(str "url", str "body", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.get_hdrs'>📖 kamailio.cfg::get_hdrs()</a>

#### KSR.http_client.query() ####

```cpp
int KSR.http_client.query(str "url", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query'>📖 kamailio.cfg::query()</a>

#### KSR.http_client.query_post() ####

```cpp
int KSR.http_client.query_post(str "url", str "post", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post'>📖 kamailio.cfg::query_post()</a>

#### KSR.http_client.query_post_hdrs() ####

```cpp
int KSR.http_client.query_post_hdrs(str "url", str "post", str "hdrs", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/http_client.html#http_client.f.query_post_hdrs'>📖 kamailio.cfg::query_post_hdrs()</a>

## imc ##

#### KSR.imc.imc_manager() ####

```cpp
int KSR.imc.imc_manager();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/imc.html#imc.f.imc_manager'>📖 kamailio.cfg::imc_manager()</a>

## ipops ##

#### KSR.ipops.compare_ips() ####

```cpp
int KSR.ipops.compare_ips(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_ips'>📖 kamailio.cfg::compare_ips()</a>

#### KSR.ipops.compare_pure_ips() ####

```cpp
int KSR.ipops.compare_pure_ips(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.compare_pure_ips'>📖 kamailio.cfg::compare_pure_ips()</a>

#### KSR.ipops.detailed_ip_type() ####

```cpp
int KSR.ipops.detailed_ip_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ip_type'>📖 kamailio.cfg::detailed_ip_type()</a>

#### KSR.ipops.detailed_ipv4_type() ####

```cpp
int KSR.ipops.detailed_ipv4_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv4_type'>📖 kamailio.cfg::detailed_ipv4_type()</a>

#### KSR.ipops.detailed_ipv6_type() ####

```cpp
int KSR.ipops.detailed_ipv6_type(str "_sval", str "_dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv6_type'>📖 kamailio.cfg::detailed_ipv6_type()</a>

#### KSR.ipops.dns_int_match_ip() ####

```cpp
int KSR.ipops.dns_int_match_ip(str "vhn", str "vip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_int_match_ip'>📖 kamailio.cfg::dns_int_match_ip()</a>

#### KSR.ipops.dns_query() ####

```cpp
int KSR.ipops.dns_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_query'>📖 kamailio.cfg::dns_query()</a>

#### KSR.ipops.dns_sys_match_ip() ####

```cpp
int KSR.ipops.dns_sys_match_ip(str "vhn", str "vip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.dns_sys_match_ip'>📖 kamailio.cfg::dns_sys_match_ip()</a>

#### KSR.ipops.ip_is_in_subnet() ####

```cpp
int KSR.ipops.ip_is_in_subnet(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_is_in_subnet'>📖 kamailio.cfg::ip_is_in_subnet()</a>

#### KSR.ipops.ip_type() ####

```cpp
int KSR.ipops.ip_type(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.ip_type'>📖 kamailio.cfg::ip_type()</a>

#### KSR.ipops.is_in_subnet() ####

```cpp
int KSR.ipops.is_in_subnet(str "_sval1", str "_sval2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_in_subnet'>📖 kamailio.cfg::is_in_subnet()</a>

#### KSR.ipops.is_ip() ####

```cpp
int KSR.ipops.is_ip(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip'>📖 kamailio.cfg::is_ip()</a>

#### KSR.ipops.is_ip4() ####

```cpp
int KSR.ipops.is_ip4(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip4'>📖 kamailio.cfg::is_ip4()</a>

#### KSR.ipops.is_ip6() ####

```cpp
int KSR.ipops.is_ip6(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6'>📖 kamailio.cfg::is_ip6()</a>

#### KSR.ipops.is_ip6_reference() ####

```cpp
int KSR.ipops.is_ip6_reference(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6_reference'>📖 kamailio.cfg::is_ip6_reference()</a>

#### KSR.ipops.is_ip_rfc1918() ####

```cpp
int KSR.ipops.is_ip_rfc1918(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_ip_rfc1918'>📖 kamailio.cfg::is_ip_rfc1918()</a>

#### KSR.ipops.is_pure_ip() ####

```cpp
int KSR.ipops.is_pure_ip(str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.is_pure_ip'>📖 kamailio.cfg::is_pure_ip()</a>

#### KSR.ipops.naptr_query() ####

```cpp
int KSR.ipops.naptr_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.naptr_query'>📖 kamailio.cfg::naptr_query()</a>

#### KSR.ipops.srv_query() ####

```cpp
int KSR.ipops.srv_query(str "naptrname", str "pvid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ipops.html#ipops.f.srv_query'>📖 kamailio.cfg::srv_query()</a>

## jansson ##

#### KSR.jansson.get() ####

```cpp
int KSR.jansson.get(str "spath", str "sdoc", str "spv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jansson.html#jansson.f.get'>📖 kamailio.cfg::get()</a>

## jsonrpcs ##

#### KSR.jsonrpcs.dispatch() ####

```cpp
int KSR.jsonrpcs.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.dispatch'>📖 kamailio.cfg::dispatch()</a>

#### KSR.jsonrpcs.exec() ####

```cpp
int KSR.jsonrpcs.exec(str "scmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.exec'>📖 kamailio.cfg::exec()</a>

#### KSR.jsonrpcs.execx() ####

```cpp
int KSR.jsonrpcs.execx(str "scmd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.execx'>📖 kamailio.cfg::execx()</a>

#### KSR.jsonrpcs.response() ####

```cpp
xval KSR.jsonrpcs.response();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.response'>📖 kamailio.cfg::response()</a>

## kafka ##

#### KSR.kafka.send() ####

```cpp
int KSR.kafka.send(str "s_topic", str "s_message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send'>📖 kamailio.cfg::send()</a>

#### KSR.kafka.send_key() ####

```cpp
int KSR.kafka.send_key(str "s_topic", str "s_message", str "s_key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kafka.html#kafka.f.send_key'>📖 kamailio.cfg::send_key()</a>

## kazoo ##

#### KSR.kazoo.kazoo_publish() ####

```cpp
int KSR.kazoo.kazoo_publish(str "exchange", str "routing_key", str "payload");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kazoo.html#kazoo.f.kazoo_publish'>📖 kamailio.cfg::kazoo_publish()</a>

#### KSR.kazoo.kazoo_subscribe() ####

```cpp
int KSR.kazoo.kazoo_subscribe(str "payload");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kazoo.html#kazoo.f.kazoo_subscribe'>📖 kamailio.cfg::kazoo_subscribe()</a>

## keepalive ##

#### KSR.keepalive.add_destination() ####

```cpp
int KSR.keepalive.add_destination(str "uri", str "owner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.add_destination'>📖 kamailio.cfg::add_destination()</a>

#### KSR.keepalive.del_destination() ####

```cpp
int KSR.keepalive.del_destination(str "uri", str "owner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.del_destination'>📖 kamailio.cfg::del_destination()</a>

#### KSR.keepalive.is_alive() ####

```cpp
int KSR.keepalive.is_alive(str "dest");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/keepalive.html#keepalive.f.is_alive'>📖 kamailio.cfg::is_alive()</a>

## kex ##

#### KSR.kex.resetdebug() ####

```cpp
int KSR.kex.resetdebug();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kex.html#kex.f.resetdebug'>📖 kamailio.cfg::resetdebug()</a>

#### KSR.kex.setdebug() ####

```cpp
int KSR.kex.setdebug(int lval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kex.html#kex.f.setdebug'>📖 kamailio.cfg::setdebug()</a>

## kx ##

Functions exported by `kemix` module. They aim to provide a convenient way to
retrieve string or integer values for most commonly used variables or runtime
environment attributes.

#### KSR.kx.get_au() ####

```cpp
xval KSR.kx.get_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_au'>📖 kamailio.cfg::get_au()</a>

#### KSR.kx.get_body() ####

```cpp
xval KSR.kx.get_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_body'>📖 kamailio.cfg::get_body()</a>

Return the body of the SIP message (the value of $rb).

#### KSR.kx.get_bodylen() ####

```cpp
int KSR.kx.get_bodylen();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_bodylen'>📖 kamailio.cfg::get_bodylen()</a>

#### KSR.kx.get_callid() ####

```cpp
xval KSR.kx.get_callid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_callid'>📖 kamailio.cfg::get_callid()</a>

#### KSR.kx.get_conid() ####

```cpp
int KSR.kx.get_conid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_conid'>📖 kamailio.cfg::get_conid()</a>

Return the connection id for TCP, TLS and WebSocket, or -1 if no stream connection corresponds to current SIP message.

#### KSR.kx.get_cturi() ####

```cpp
xval KSR.kx.get_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_cturi'>📖 kamailio.cfg::get_cturi()</a>

#### KSR.kx.get_def() ####

```cpp
xval KSR.kx.get_def(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_def'>📖 kamailio.cfg::get_def()</a>

#### KSR.kx.get_defn() ####

```cpp
int KSR.kx.get_defn(str "dname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_defn'>📖 kamailio.cfg::get_defn()</a>

#### KSR.kx.get_duri() ####

```cpp
xval KSR.kx.get_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_duri'>📖 kamailio.cfg::get_duri()</a>

Return the value of destination URI ($du).

#### KSR.kx.get_env() ####

```cpp
xval KSR.kx.get_env(str "envname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_env'>📖 kamailio.cfg::get_env()</a>

#### KSR.kx.get_envn() ####

```cpp
int KSR.kx.get_envn(str "envname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_envn'>📖 kamailio.cfg::get_envn()</a>

#### KSR.kx.get_fhost() ####

```cpp
xval KSR.kx.get_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_fhost'>📖 kamailio.cfg::get_fhost()</a>

Return From-URI domain ($fd).

#### KSR.kx.get_furi() ####

```cpp
xval KSR.kx.get_furi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_furi'>📖 kamailio.cfg::get_furi()</a>

Return the From URI($fu).

#### KSR.kx.get_fuser() ####

```cpp
xval KSR.kx.get_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_fuser'>📖 kamailio.cfg::get_fuser()</a>

Return the From-URI username ($fU).

#### KSR.kx.get_method() ####

```cpp
xval KSR.kx.get_method();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_method'>📖 kamailio.cfg::get_method()</a>

Return the SIP method ($rm).

#### KSR.kx.get_msgbuf() ####

```cpp
xval KSR.kx.get_msgbuf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_msgbuf'>📖 kamailio.cfg::get_msgbuf()</a>

#### KSR.kx.get_msglen() ####

```cpp
int KSR.kx.get_msglen();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_msglen'>📖 kamailio.cfg::get_msglen()</a>

#### KSR.kx.get_msgtype() ####

```cpp
int KSR.kx.get_msgtype();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_msgtype'>📖 kamailio.cfg::get_msgtype()</a>

#### KSR.kx.get_nhuri() ####

```cpp
xval KSR.kx.get_nhuri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_nhuri'>📖 kamailio.cfg::get_nhuri()</a>

#### KSR.kx.get_ouri() ####

```cpp
xval KSR.kx.get_ouri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_ouri'>📖 kamailio.cfg::get_ouri()</a>

#### KSR.kx.get_proto() ####

```cpp
xval KSR.kx.get_proto();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_proto'>📖 kamailio.cfg::get_proto()</a>

#### KSR.kx.get_protoid() ####

```cpp
int KSR.kx.get_protoid();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_protoid'>📖 kamailio.cfg::get_protoid()</a>

#### KSR.kx.get_rcv_sock_name() ####

```cpp
xval KSR.kx.get_rcv_sock_name();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rcv_sock_name'>📖 kamailio.cfg::get_rcv_sock_name()</a>

#### KSR.kx.get_rcvadvip() ####

```cpp
xval KSR.kx.get_rcvadvip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rcvadvip'>📖 kamailio.cfg::get_rcvadvip()</a>

#### KSR.kx.get_rcvadvport() ####

```cpp
xval KSR.kx.get_rcvadvport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rcvadvport'>📖 kamailio.cfg::get_rcvadvport()</a>

#### KSR.kx.get_rcvip() ####

```cpp
xval KSR.kx.get_rcvip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rcvip'>📖 kamailio.cfg::get_rcvip()</a>

#### KSR.kx.get_rcvport() ####

```cpp
xval KSR.kx.get_rcvport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rcvport'>📖 kamailio.cfg::get_rcvport()</a>

#### KSR.kx.get_rhost() ####

```cpp
xval KSR.kx.get_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_rhost'>📖 kamailio.cfg::get_rhost()</a>

Return the Request URI host (domain) part ($rd).

#### KSR.kx.get_ruri() ####

```cpp
xval KSR.kx.get_ruri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_ruri'>📖 kamailio.cfg::get_ruri()</a>

Return the Request URI ($ru).

#### KSR.kx.get_ruser() ####

```cpp
xval KSR.kx.get_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_ruser'>📖 kamailio.cfg::get_ruser()</a>

Return the Request URI user part ($rU).

#### KSR.kx.get_send_sock() ####

```cpp
xval KSR.kx.get_send_sock();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_send_sock'>📖 kamailio.cfg::get_send_sock()</a>

#### KSR.kx.get_send_sock_name() ####

```cpp
xval KSR.kx.get_send_sock_name();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_send_sock_name'>📖 kamailio.cfg::get_send_sock_name()</a>

#### KSR.kx.get_send_sock_port() ####

```cpp
int KSR.kx.get_send_sock_port();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_send_sock_port'>📖 kamailio.cfg::get_send_sock_port()</a>

#### KSR.kx.get_srcip() ####

```cpp
xval KSR.kx.get_srcip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_srcip'>📖 kamailio.cfg::get_srcip()</a>

#### KSR.kx.get_srcport() ####

```cpp
xval KSR.kx.get_srcport();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_srcport'>📖 kamailio.cfg::get_srcport()</a>

#### KSR.kx.get_srcuri() ####

```cpp
xval KSR.kx.get_srcuri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_srcuri'>📖 kamailio.cfg::get_srcuri()</a>

#### KSR.kx.get_status() ####

```cpp
int KSR.kx.get_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_status'>📖 kamailio.cfg::get_status()</a>

#### KSR.kx.get_thost() ####

```cpp
xval KSR.kx.get_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_thost'>📖 kamailio.cfg::get_thost()</a>

Return the To-URI host (domain) part ($td).

#### KSR.kx.get_timestamp() ####

```cpp
int KSR.kx.get_timestamp();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_timestamp'>📖 kamailio.cfg::get_timestamp()</a>

#### KSR.kx.get_turi() ####

```cpp
xval KSR.kx.get_turi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_turi'>📖 kamailio.cfg::get_turi()</a>

Return the To URI ($tu).

#### KSR.kx.get_tuser() ####

```cpp
xval KSR.kx.get_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_tuser'>📖 kamailio.cfg::get_tuser()</a>

Return the To-URI user part ($tU).

#### KSR.kx.get_ua() ####

```cpp
xval KSR.kx.get_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.get_ua'>📖 kamailio.cfg::get_ua()</a>

#### KSR.kx.gete_au() ####

```cpp
xval KSR.kx.gete_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_au'>📖 kamailio.cfg::gete_au()</a>

#### KSR.kx.gete_body() ####

```cpp
xval KSR.kx.gete_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_body'>📖 kamailio.cfg::gete_body()</a>

#### KSR.kx.gete_cturi() ####

```cpp
xval KSR.kx.gete_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_cturi'>📖 kamailio.cfg::gete_cturi()</a>

#### KSR.kx.gete_duri() ####

```cpp
xval KSR.kx.gete_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_duri'>📖 kamailio.cfg::gete_duri()</a>

#### KSR.kx.gete_fhost() ####

```cpp
xval KSR.kx.gete_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_fhost'>📖 kamailio.cfg::gete_fhost()</a>

#### KSR.kx.gete_fuser() ####

```cpp
xval KSR.kx.gete_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_fuser'>📖 kamailio.cfg::gete_fuser()</a>

#### KSR.kx.gete_rhost() ####

```cpp
xval KSR.kx.gete_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_rhost'>📖 kamailio.cfg::gete_rhost()</a>

#### KSR.kx.gete_ruser() ####

```cpp
xval KSR.kx.gete_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_ruser'>📖 kamailio.cfg::gete_ruser()</a>

#### KSR.kx.gete_thost() ####

```cpp
xval KSR.kx.gete_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_thost'>📖 kamailio.cfg::gete_thost()</a>

#### KSR.kx.gete_tuser() ####

```cpp
xval KSR.kx.gete_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_tuser'>📖 kamailio.cfg::gete_tuser()</a>

#### KSR.kx.gete_ua() ####

```cpp
xval KSR.kx.gete_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gete_ua'>📖 kamailio.cfg::gete_ua()</a>

#### KSR.kx.gets_status() ####

```cpp
xval KSR.kx.gets_status();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.gets_status'>📖 kamailio.cfg::gets_status()</a>

#### KSR.kx.getw_au() ####

```cpp
xval KSR.kx.getw_au();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_au'>📖 kamailio.cfg::getw_au()</a>

#### KSR.kx.getw_body() ####

```cpp
xval KSR.kx.getw_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_body'>📖 kamailio.cfg::getw_body()</a>

#### KSR.kx.getw_cturi() ####

```cpp
xval KSR.kx.getw_cturi();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_cturi'>📖 kamailio.cfg::getw_cturi()</a>

#### KSR.kx.getw_duri() ####

```cpp
xval KSR.kx.getw_duri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_duri'>📖 kamailio.cfg::getw_duri()</a>

#### KSR.kx.getw_fhost() ####

```cpp
xval KSR.kx.getw_fhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_fhost'>📖 kamailio.cfg::getw_fhost()</a>

#### KSR.kx.getw_fuser() ####

```cpp
xval KSR.kx.getw_fuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_fuser'>📖 kamailio.cfg::getw_fuser()</a>

#### KSR.kx.getw_rhost() ####

```cpp
xval KSR.kx.getw_rhost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_rhost'>📖 kamailio.cfg::getw_rhost()</a>

#### KSR.kx.getw_ruser() ####

```cpp
xval KSR.kx.getw_ruser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_ruser'>📖 kamailio.cfg::getw_ruser()</a>

#### KSR.kx.getw_thost() ####

```cpp
xval KSR.kx.getw_thost();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_thost'>📖 kamailio.cfg::getw_thost()</a>

#### KSR.kx.getw_tuser() ####

```cpp
xval KSR.kx.getw_tuser();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_tuser'>📖 kamailio.cfg::getw_tuser()</a>

#### KSR.kx.getw_ua() ####

```cpp
xval KSR.kx.getw_ua();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/kx.html#kx.f.getw_ua'>📖 kamailio.cfg::getw_ua()</a>

## lcr ##

#### KSR.lcr.defunct_gw() ####

```cpp
int KSR.lcr.defunct_gw(int defunct_period);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.defunct_gw'>📖 kamailio.cfg::defunct_gw()</a>

#### KSR.lcr.from_any_gw() ####

```cpp
int KSR.lcr.from_any_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw'>📖 kamailio.cfg::from_any_gw()</a>

#### KSR.lcr.from_any_gw_addr() ####

```cpp
int KSR.lcr.from_any_gw_addr(str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr'>📖 kamailio.cfg::from_any_gw_addr()</a>

#### KSR.lcr.from_gw() ####

```cpp
int KSR.lcr.from_gw(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw'>📖 kamailio.cfg::from_gw()</a>

#### KSR.lcr.from_gw_addr() ####

```cpp
int KSR.lcr.from_gw_addr(int lcr_id, str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr'>📖 kamailio.cfg::from_gw_addr()</a>

#### KSR.lcr.inactivate_gw() ####

```cpp
int KSR.lcr.inactivate_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.inactivate_gw'>📖 kamailio.cfg::inactivate_gw()</a>

#### KSR.lcr.load_gws() ####

```cpp
int KSR.lcr.load_gws(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws'>📖 kamailio.cfg::load_gws()</a>

#### KSR.lcr.load_gws_furi() ####

```cpp
int KSR.lcr.load_gws_furi(int lcr_id, str "ruri_user", str "from_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_furi'>📖 kamailio.cfg::load_gws_furi()</a>

#### KSR.lcr.load_gws_ruser() ####

```cpp
int KSR.lcr.load_gws_ruser(int lcr_id, str "ruri_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_ruser'>📖 kamailio.cfg::load_gws_ruser()</a>

#### KSR.lcr.next_gw() ####

```cpp
int KSR.lcr.next_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.next_gw'>📖 kamailio.cfg::next_gw()</a>

#### KSR.lcr.to_any_gw() ####

```cpp
int KSR.lcr.to_any_gw();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw'>📖 kamailio.cfg::to_any_gw()</a>

#### KSR.lcr.to_any_gw_addr() ####

```cpp
int KSR.lcr.to_any_gw_addr(str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw_addr'>📖 kamailio.cfg::to_any_gw_addr()</a>

#### KSR.lcr.to_gw() ####

```cpp
int KSR.lcr.to_gw(int lcr_id);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw'>📖 kamailio.cfg::to_gw()</a>

#### KSR.lcr.to_gw_addr() ####

```cpp
int KSR.lcr.to_gw_addr(int lcr_id, str "addr_str", int transport);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/lcr.html#lcr.f.to_gw_addr'>📖 kamailio.cfg::to_gw_addr()</a>

## log_custom ##

#### KSR.log_custom.log_udp() ####

```cpp
int KSR.log_custom.log_udp(str "txt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_custom.html#log_custom.f.log_udp'>📖 kamailio.cfg::log_udp()</a>

## log_systemd ##

#### KSR.log_systemd.sd_journal_print() ####

```cpp
int KSR.log_systemd.sd_journal_print(str "slev", str "stxt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_print'>📖 kamailio.cfg::sd_journal_print()</a>

#### KSR.log_systemd.sd_journal_send_xvap() ####

```cpp
int KSR.log_systemd.sd_journal_send_xvap(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_send_xvap'>📖 kamailio.cfg::sd_journal_send_xvap()</a>

## maxfwd ##

#### KSR.maxfwd.is_maxfwd_lt() ####

```cpp
int KSR.maxfwd.is_maxfwd_lt(int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/maxfwd.html#maxfwd.f.is_maxfwd_lt'>📖 kamailio.cfg::is_maxfwd_lt()</a>

#### KSR.maxfwd.process_maxfwd() ####

```cpp
int KSR.maxfwd.process_maxfwd(int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/maxfwd.html#maxfwd.f.process_maxfwd'>📖 kamailio.cfg::process_maxfwd()</a>

## mediaproxy ##

#### KSR.mediaproxy.end_media_session() ####

```cpp
int KSR.mediaproxy.end_media_session();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.end_media_session'>📖 kamailio.cfg::end_media_session()</a>

#### KSR.mediaproxy.engage_media_proxy() ####

```cpp
int KSR.mediaproxy.engage_media_proxy();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.engage_media_proxy'>📖 kamailio.cfg::engage_media_proxy()</a>

#### KSR.mediaproxy.use_media_proxy() ####

```cpp
int KSR.mediaproxy.use_media_proxy();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.use_media_proxy'>📖 kamailio.cfg::use_media_proxy()</a>

## misc_radius ##

#### KSR.misc_radius.does_uri_exist() ####

```cpp
int KSR.misc_radius.does_uri_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist'>📖 kamailio.cfg::does_uri_exist()</a>

#### KSR.misc_radius.does_uri_exist_uval() ####

```cpp
int KSR.misc_radius.does_uri_exist_uval(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist_uval'>📖 kamailio.cfg::does_uri_exist_uval()</a>

#### KSR.misc_radius.does_uri_user_exist() ####

```cpp
int KSR.misc_radius.does_uri_user_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist'>📖 kamailio.cfg::does_uri_user_exist()</a>

#### KSR.misc_radius.does_uri_user_exist_uval() ####

```cpp
int KSR.misc_radius.does_uri_user_exist_uval(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist_uval'>📖 kamailio.cfg::does_uri_user_exist_uval()</a>

#### KSR.misc_radius.is_user_in() ####

```cpp
int KSR.misc_radius.is_user_in(str "user", str "group");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.is_user_in'>📖 kamailio.cfg::is_user_in()</a>

#### KSR.misc_radius.load_callee_avps() ####

```cpp
int KSR.misc_radius.load_callee_avps(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_callee_avps'>📖 kamailio.cfg::load_callee_avps()</a>

#### KSR.misc_radius.load_caller_avps() ####

```cpp
int KSR.misc_radius.load_caller_avps(str "user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_caller_avps'>📖 kamailio.cfg::load_caller_avps()</a>

## mqtt ##

#### KSR.mqtt.publish() ####

```cpp
int KSR.mqtt.publish(str "topic", str "payload", int qos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.publish'>📖 kamailio.cfg::publish()</a>

#### KSR.mqtt.subscribe() ####

```cpp
int KSR.mqtt.subscribe(str "topic", int qos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.subscribe'>📖 kamailio.cfg::subscribe()</a>

#### KSR.mqtt.unsubscribe() ####

```cpp
int KSR.mqtt.unsubscribe(str "topic");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqtt.html#mqtt.f.unsubscribe'>📖 kamailio.cfg::unsubscribe()</a>

## mqueue ##

#### KSR.mqueue.mq_add() ####

```cpp
int KSR.mqueue.mq_add(str "mq", str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_add'>📖 kamailio.cfg::mq_add()</a>

#### KSR.mqueue.mq_fetch() ####

```cpp
int KSR.mqueue.mq_fetch(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_fetch'>📖 kamailio.cfg::mq_fetch()</a>

#### KSR.mqueue.mq_pv_free() ####

```cpp
int KSR.mqueue.mq_pv_free(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_pv_free'>📖 kamailio.cfg::mq_pv_free()</a>

#### KSR.mqueue.mq_size() ####

```cpp
int KSR.mqueue.mq_size(str "mq");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_size'>📖 kamailio.cfg::mq_size()</a>

#### KSR.mqueue.mqk_get() ####

```cpp
xval KSR.mqueue.mqk_get(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_get'>📖 kamailio.cfg::mqk_get()</a>

#### KSR.mqueue.mqk_gete() ####

```cpp
xval KSR.mqueue.mqk_gete(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_gete'>📖 kamailio.cfg::mqk_gete()</a>

#### KSR.mqueue.mqk_getw() ####

```cpp
xval KSR.mqueue.mqk_getw(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_getw'>📖 kamailio.cfg::mqk_getw()</a>

#### KSR.mqueue.mqv_get() ####

```cpp
xval KSR.mqueue.mqv_get(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_get'>📖 kamailio.cfg::mqv_get()</a>

#### KSR.mqueue.mqv_gete() ####

```cpp
xval KSR.mqueue.mqv_gete(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_gete'>📖 kamailio.cfg::mqv_gete()</a>

#### KSR.mqueue.mqv_getw() ####

```cpp
xval KSR.mqueue.mqv_getw(str "qname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_getw'>📖 kamailio.cfg::mqv_getw()</a>

## msilo ##

#### KSR.msilo.mdump() ####

```cpp
int KSR.msilo.mdump();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mdump'>📖 kamailio.cfg::mdump()</a>

#### KSR.msilo.mdump_uri() ####

```cpp
int KSR.msilo.mdump_uri(str "owner_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mdump_uri'>📖 kamailio.cfg::mdump_uri()</a>

#### KSR.msilo.mstore() ####

```cpp
int KSR.msilo.mstore();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mstore'>📖 kamailio.cfg::mstore()</a>

#### KSR.msilo.mstore_uri() ####

```cpp
int KSR.msilo.mstore_uri(str "owner_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msilo.html#msilo.f.mstore_uri'>📖 kamailio.cfg::mstore_uri()</a>

## msrp ##

#### KSR.msrp.cmap_lookup() ####

```cpp
int KSR.msrp.cmap_lookup();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_lookup'>📖 kamailio.cfg::cmap_lookup()</a>

#### KSR.msrp.cmap_save() ####

```cpp
int KSR.msrp.cmap_save();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.cmap_save'>📖 kamailio.cfg::cmap_save()</a>

#### KSR.msrp.is_reply() ####

```cpp
int KSR.msrp.is_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_reply'>📖 kamailio.cfg::is_reply()</a>

#### KSR.msrp.is_request() ####

```cpp
int KSR.msrp.is_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.is_request'>📖 kamailio.cfg::is_request()</a>

#### KSR.msrp.relay() ####

```cpp
int KSR.msrp.relay();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay'>📖 kamailio.cfg::relay()</a>

#### KSR.msrp.relay_flags() ####

```cpp
int KSR.msrp.relay_flags(int rtflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.relay_flags'>📖 kamailio.cfg::relay_flags()</a>

#### KSR.msrp.reply() ####

```cpp
int KSR.msrp.reply(str "rcode", str "rtext", str "rhdrs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply'>📖 kamailio.cfg::reply()</a>

#### KSR.msrp.reply_flags() ####

```cpp
int KSR.msrp.reply_flags(int rtflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.reply_flags'>📖 kamailio.cfg::reply_flags()</a>

#### KSR.msrp.set_dst() ####

```cpp
int KSR.msrp.set_dst(str "rtaddr", str "rfsock");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/msrp.html#msrp.f.set_dst'>📖 kamailio.cfg::set_dst()</a>

## mtree ##

#### KSR.mtree.mt_match() ####

```cpp
int KSR.mtree.mt_match(str "tname", str "tomatch", int mval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/mtree.html#mtree.f.mt_match'>📖 kamailio.cfg::mt_match()</a>

## nat_traversal ##

#### KSR.nat_traversal.client_nat_test() ####

```cpp
int KSR.nat_traversal.client_nat_test(int tests);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.client_nat_test'>📖 kamailio.cfg::client_nat_test()</a>

#### KSR.nat_traversal.fix_contact() ####

```cpp
int KSR.nat_traversal.fix_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.fix_contact'>📖 kamailio.cfg::fix_contact()</a>

#### KSR.nat_traversal.nat_keepalive() ####

```cpp
int KSR.nat_traversal.nat_keepalive();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.nat_keepalive'>📖 kamailio.cfg::nat_keepalive()</a>

## nathelper ##

#### KSR.nathelper.add_contact_alias() ####

```cpp
int KSR.nathelper.add_contact_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias'>📖 kamailio.cfg::add_contact_alias()</a>

#### KSR.nathelper.add_contact_alias_addr() ####

```cpp
int KSR.nathelper.add_contact_alias_addr(str "ip_str", str "port_str", str "proto_str");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias_addr'>📖 kamailio.cfg::add_contact_alias_addr()</a>

#### KSR.nathelper.add_rcv_param() ####

```cpp
int KSR.nathelper.add_rcv_param(int upos);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.add_rcv_param'>📖 kamailio.cfg::add_rcv_param()</a>

#### KSR.nathelper.fix_nated_contact() ####

```cpp
int KSR.nathelper.fix_nated_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_contact'>📖 kamailio.cfg::fix_nated_contact()</a>

#### KSR.nathelper.fix_nated_register() ####

```cpp
int KSR.nathelper.fix_nated_register();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_register'>📖 kamailio.cfg::fix_nated_register()</a>

#### KSR.nathelper.fix_nated_sdp() ####

```cpp
int KSR.nathelper.fix_nated_sdp(int level);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp'>📖 kamailio.cfg::fix_nated_sdp()</a>

#### KSR.nathelper.fix_nated_sdp_ip() ####

```cpp
int KSR.nathelper.fix_nated_sdp_ip(int level, str "ip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp_ip'>📖 kamailio.cfg::fix_nated_sdp_ip()</a>

#### KSR.nathelper.handle_ruri_alias() ####

```cpp
int KSR.nathelper.handle_ruri_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias'>📖 kamailio.cfg::handle_ruri_alias()</a>

#### KSR.nathelper.is_rfc1918() ####

```cpp
int KSR.nathelper.is_rfc1918(str "address");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.is_rfc1918'>📖 kamailio.cfg::is_rfc1918()</a>

#### KSR.nathelper.nat_uac_test() ####

```cpp
int KSR.nathelper.nat_uac_test(int tests);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.nat_uac_test'>📖 kamailio.cfg::nat_uac_test()</a>

#### KSR.nathelper.set_alias_to_pv() ####

```cpp
int KSR.nathelper.set_alias_to_pv(str "uri_avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_alias_to_pv'>📖 kamailio.cfg::set_alias_to_pv()</a>

#### KSR.nathelper.set_contact_alias() ####

```cpp
int KSR.nathelper.set_contact_alias();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias'>📖 kamailio.cfg::set_contact_alias()</a>

#### KSR.nathelper.set_contact_alias_trim() ####

```cpp
int KSR.nathelper.set_contact_alias_trim();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias_trim'>📖 kamailio.cfg::set_contact_alias_trim()</a>

## ndb_mongodb ##

#### KSR.ndb_mongodb.exec() ####

```cpp
int KSR.ndb_mongodb.exec(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec'>📖 kamailio.cfg::exec()</a>

#### KSR.ndb_mongodb.exec_simple() ####

```cpp
int KSR.ndb_mongodb.exec_simple(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec_simple'>📖 kamailio.cfg::exec_simple()</a>

#### KSR.ndb_mongodb.execx() ####

```cpp
int KSR.ndb_mongodb.execx(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.execx'>📖 kamailio.cfg::execx()</a>

#### KSR.ndb_mongodb.find() ####

```cpp
int KSR.ndb_mongodb.find(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find'>📖 kamailio.cfg::find()</a>

#### KSR.ndb_mongodb.find_one() ####

```cpp
int KSR.ndb_mongodb.find_one(str "ssrv", str "sdname", str "scname", str "scmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find_one'>📖 kamailio.cfg::find_one()</a>

#### KSR.ndb_mongodb.free_reply() ####

```cpp
int KSR.ndb_mongodb.free_reply(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.free_reply'>📖 kamailio.cfg::free_reply()</a>

#### KSR.ndb_mongodb.next_reply() ####

```cpp
int KSR.ndb_mongodb.next_reply(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.next_reply'>📖 kamailio.cfg::next_reply()</a>

## ndb_redis ##

#### KSR.ndb_redis.redis_cmd() ####

```cpp
int KSR.ndb_redis.redis_cmd(str "srv", str "rcmd", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd'>📖 kamailio.cfg::redis_cmd()</a>

#### KSR.ndb_redis.redis_cmd_p1() ####

```cpp
int KSR.ndb_redis.redis_cmd_p1(str "srv", str "rcmd", str "p1", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p1'>📖 kamailio.cfg::redis_cmd_p1()</a>

#### KSR.ndb_redis.redis_cmd_p2() ####

```cpp
int KSR.ndb_redis.redis_cmd_p2(str "srv", str "rcmd", str "p1", str "p2", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p2'>📖 kamailio.cfg::redis_cmd_p2()</a>

#### KSR.ndb_redis.redis_cmd_p3() ####

```cpp
int KSR.ndb_redis.redis_cmd_p3(str "srv", str "rcmd", str "p1", str "p2", str "p3", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p3'>📖 kamailio.cfg::redis_cmd_p3()</a>

#### KSR.ndb_redis.redis_free() ####

```cpp
int KSR.ndb_redis.redis_free(str "name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_free'>📖 kamailio.cfg::redis_free()</a>

## path ##

#### KSR.path.add_path() ####

```cpp
int KSR.path.add_path();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path'>📖 kamailio.cfg::add_path()</a>

#### KSR.path.add_path_received() ####

```cpp
int KSR.path.add_path_received();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received'>📖 kamailio.cfg::add_path_received()</a>

#### KSR.path.add_path_received_user() ####

```cpp
int KSR.path.add_path_received_user(str "_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received_user'>📖 kamailio.cfg::add_path_received_user()</a>

#### KSR.path.add_path_received_user_params() ####

```cpp
int KSR.path.add_path_received_user_params(str "_user", str "_params");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_received_user_params'>📖 kamailio.cfg::add_path_received_user_params()</a>

#### KSR.path.add_path_user() ####

```cpp
int KSR.path.add_path_user(str "_user");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_user'>📖 kamailio.cfg::add_path_user()</a>

#### KSR.path.add_path_user_params() ####

```cpp
int KSR.path.add_path_user_params(str "_user", str "_params");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/path.html#path.f.add_path_user_params'>📖 kamailio.cfg::add_path_user_params()</a>

## pdt ##

#### KSR.pdt.pd_translate() ####

```cpp
int KSR.pdt.pd_translate(str "sd", int md);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pdt.html#pdt.f.pd_translate'>📖 kamailio.cfg::pd_translate()</a>

#### KSR.pdt.pprefix2domain() ####

```cpp
int KSR.pdt.pprefix2domain(int m, int s);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pdt.html#pdt.f.pprefix2domain'>📖 kamailio.cfg::pprefix2domain()</a>

## permissions ##

#### KSR.permissions.allow_address() ####

```cpp
int KSR.permissions.allow_address(int addr_group, str "ips", int port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address'>📖 kamailio.cfg::allow_address()</a>

#### KSR.permissions.allow_address_group() ####

```cpp
int KSR.permissions.allow_address_group(str "_addr", int _port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_address_group'>📖 kamailio.cfg::allow_address_group()</a>

#### KSR.permissions.allow_source_address() ####

```cpp
int KSR.permissions.allow_source_address(int addr_group);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address'>📖 kamailio.cfg::allow_source_address()</a>

#### KSR.permissions.allow_source_address_group() ####

```cpp
int KSR.permissions.allow_source_address_group();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address_group'>📖 kamailio.cfg::allow_source_address_group()</a>

#### KSR.permissions.allow_trusted() ####

```cpp
int KSR.permissions.allow_trusted();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/permissions.html#permissions.f.allow_trusted'>📖 kamailio.cfg::allow_trusted()</a>

## phonenum ##

#### KSR.phonenum.match() ####

```cpp
int KSR.phonenum.match(str "tomatch", str "pvclass");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/phonenum.html#phonenum.f.match'>📖 kamailio.cfg::match()</a>

## pike ##

#### KSR.pike.pike_check_ip() ####

```cpp
int KSR.pike.pike_check_ip(str "strip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pike.html#pike.f.pike_check_ip'>📖 kamailio.cfg::pike_check_ip()</a>

#### KSR.pike.pike_check_req() ####

```cpp
int KSR.pike.pike_check_req();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pike.html#pike.f.pike_check_req'>📖 kamailio.cfg::pike_check_req()</a>

## pipelimit ##

#### KSR.pipelimit.pl_active() ####

```cpp
int KSR.pipelimit.pl_active(str "pipeid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_active'>📖 kamailio.cfg::pl_active()</a>

#### KSR.pipelimit.pl_check() ####

```cpp
int KSR.pipelimit.pl_check(str "pipeid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check'>📖 kamailio.cfg::pl_check()</a>

#### KSR.pipelimit.pl_check_limit() ####

```cpp
int KSR.pipelimit.pl_check_limit(str "pipeid", str "alg", int limit);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check_limit'>📖 kamailio.cfg::pl_check_limit()</a>

#### KSR.pipelimit.pl_drop() ####

```cpp
int KSR.pipelimit.pl_drop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop'>📖 kamailio.cfg::pl_drop()</a>

#### KSR.pipelimit.pl_drop_range() ####

```cpp
int KSR.pipelimit.pl_drop_range(int rmin, int rmax);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_range'>📖 kamailio.cfg::pl_drop_range()</a>

#### KSR.pipelimit.pl_drop_retry() ####

```cpp
int KSR.pipelimit.pl_drop_retry(int rafter);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_retry'>📖 kamailio.cfg::pl_drop_retry()</a>

## prefix_route ##

#### KSR.prefix_route.prefix_route() ####

```cpp
int KSR.prefix_route.prefix_route(str "ruser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route'>📖 kamailio.cfg::prefix_route()</a>

#### KSR.prefix_route.prefix_route_uri() ####

```cpp
int KSR.prefix_route.prefix_route_uri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route_uri'>📖 kamailio.cfg::prefix_route_uri()</a>

## presence ##

#### KSR.presence.handle_publish() ####

```cpp
int KSR.presence.handle_publish();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish'>📖 kamailio.cfg::handle_publish()</a>

#### KSR.presence.handle_publish_uri() ####

```cpp
int KSR.presence.handle_publish_uri(str "sender_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_publish_uri'>📖 kamailio.cfg::handle_publish_uri()</a>

#### KSR.presence.handle_subscribe() ####

```cpp
int KSR.presence.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe'>📖 kamailio.cfg::handle_subscribe()</a>

#### KSR.presence.handle_subscribe_uri() ####

```cpp
int KSR.presence.handle_subscribe_uri(str "wuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe_uri'>📖 kamailio.cfg::handle_subscribe_uri()</a>

#### KSR.presence.pres_auth_status() ####

```cpp
int KSR.presence.pres_auth_status(str "watcher_uri", str "presentity_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_auth_status'>📖 kamailio.cfg::pres_auth_status()</a>

#### KSR.presence.pres_has_subscribers() ####

```cpp
int KSR.presence.pres_has_subscribers(str "pres_uri", str "wevent");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_has_subscribers'>📖 kamailio.cfg::pres_has_subscribers()</a>

#### KSR.presence.pres_refresh_watchers() ####

```cpp
int KSR.presence.pres_refresh_watchers(str "pres", str "event", int type);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers'>📖 kamailio.cfg::pres_refresh_watchers()</a>

#### KSR.presence.pres_refresh_watchers_file() ####

```cpp
int KSR.presence.pres_refresh_watchers_file(str "pres", str "event", int type, str "file_uri", str "filename");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers_file'>📖 kamailio.cfg::pres_refresh_watchers_file()</a>

#### KSR.presence.pres_update_watchers() ####

```cpp
int KSR.presence.pres_update_watchers(str "pres_uri", str "event");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence.html#presence.f.pres_update_watchers'>📖 kamailio.cfg::pres_update_watchers()</a>

## presence_xml ##

#### KSR.presence_xml.pres_check_activities() ####

```cpp
int KSR.presence_xml.pres_check_activities(str "pres_uri", str "activity");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_activities'>📖 kamailio.cfg::pres_check_activities()</a>

#### KSR.presence_xml.pres_check_basic() ####

```cpp
int KSR.presence_xml.pres_check_basic(str "pres_uri", str "status");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_basic'>📖 kamailio.cfg::pres_check_basic()</a>

## pua ##

#### KSR.pua.pua_set_publish() ####

```cpp
int KSR.pua.pua_set_publish();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua.html#pua.f.pua_set_publish'>📖 kamailio.cfg::pua_set_publish()</a>

#### KSR.pua.pua_update_contact() ####

```cpp
int KSR.pua.pua_update_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pua.html#pua.f.pua_update_contact'>📖 kamailio.cfg::pua_update_contact()</a>

## pv_headers ##

#### KSR.pv_headers.pvh_append_header() ####

```cpp
int KSR.pv_headers.pvh_append_header(str "hname", str "hvalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_append_header'>📖 kamailio.cfg::pvh_append_header()</a>

#### KSR.pv_headers.pvh_apply_headers() ####

```cpp
int KSR.pv_headers.pvh_apply_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_apply_headers'>📖 kamailio.cfg::pvh_apply_headers()</a>

#### KSR.pv_headers.pvh_check_header() ####

```cpp
int KSR.pv_headers.pvh_check_header(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_check_header'>📖 kamailio.cfg::pvh_check_header()</a>

#### KSR.pv_headers.pvh_collect_headers() ####

```cpp
int KSR.pv_headers.pvh_collect_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_collect_headers'>📖 kamailio.cfg::pvh_collect_headers()</a>

#### KSR.pv_headers.pvh_modify_header() ####

```cpp
int KSR.pv_headers.pvh_modify_header(str "hname", str "hvalue", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_modify_header'>📖 kamailio.cfg::pvh_modify_header()</a>

#### KSR.pv_headers.pvh_remove_header() ####

```cpp
int KSR.pv_headers.pvh_remove_header(str "hname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_remove_header'>📖 kamailio.cfg::pvh_remove_header()</a>

#### KSR.pv_headers.pvh_reset_headers() ####

```cpp
int KSR.pv_headers.pvh_reset_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pv_headers.html#pv_headers.f.pvh_reset_headers'>📖 kamailio.cfg::pvh_reset_headers()</a>

## pvx ##

#### KSR.pvx.avp_get() ####

```cpp
xval KSR.pvx.avp_get(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_get'>📖 kamailio.cfg::avp_get()</a>

#### KSR.pvx.avp_gete() ####

```cpp
xval KSR.pvx.avp_gete(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_gete'>📖 kamailio.cfg::avp_gete()</a>

#### KSR.pvx.avp_getw() ####

```cpp
xval KSR.pvx.avp_getw(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_getw'>📖 kamailio.cfg::avp_getw()</a>

#### KSR.pvx.avp_is_null() ####

```cpp
int KSR.pvx.avp_is_null(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_is_null'>📖 kamailio.cfg::avp_is_null()</a>

#### KSR.pvx.avp_rm() ####

```cpp
int KSR.pvx.avp_rm(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_rm'>📖 kamailio.cfg::avp_rm()</a>

#### KSR.pvx.avp_seti() ####

```cpp
int KSR.pvx.avp_seti(str "xname", int vn);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_seti'>📖 kamailio.cfg::avp_seti()</a>

#### KSR.pvx.avp_sets() ####

```cpp
int KSR.pvx.avp_sets(str "xname", str "vs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.avp_sets'>📖 kamailio.cfg::avp_sets()</a>

#### KSR.pvx.evalx() ####

```cpp
int KSR.pvx.evalx(str "dst", str "fmt");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.evalx'>📖 kamailio.cfg::evalx()</a>

#### KSR.pvx.pv_var_to_xavp() ####

```cpp
int KSR.pvx.pv_var_to_xavp(str "varname", str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.pv_var_to_xavp'>📖 kamailio.cfg::pv_var_to_xavp()</a>

#### KSR.pvx.pv_xavi_print() ####

```cpp
int KSR.pvx.pv_xavi_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavi_print'>📖 kamailio.cfg::pv_xavi_print()</a>

#### KSR.pvx.pv_xavp_print() ####

```cpp
int KSR.pvx.pv_xavp_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavp_print'>📖 kamailio.cfg::pv_xavp_print()</a>

#### KSR.pvx.pv_xavp_to_var() ####

```cpp
int KSR.pvx.pv_xavp_to_var(str "xname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavp_to_var'>📖 kamailio.cfg::pv_xavp_to_var()</a>

#### KSR.pvx.pv_xavu_print() ####

```cpp
int KSR.pvx.pv_xavu_print();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavu_print'>📖 kamailio.cfg::pv_xavu_print()</a>

#### KSR.pvx.sbranch_append() ####

```cpp
int KSR.pvx.sbranch_append();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_append'>📖 kamailio.cfg::sbranch_append()</a>

#### KSR.pvx.sbranch_reset() ####

```cpp
int KSR.pvx.sbranch_reset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_reset'>📖 kamailio.cfg::sbranch_reset()</a>

#### KSR.pvx.sbranch_set_ruri() ####

```cpp
int KSR.pvx.sbranch_set_ruri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_set_ruri'>📖 kamailio.cfg::sbranch_set_ruri()</a>

#### KSR.pvx.shv_get() ####

```cpp
xval KSR.pvx.shv_get(str "vname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.shv_get'>📖 kamailio.cfg::shv_get()</a>

#### KSR.pvx.shv_seti() ####

```cpp
int KSR.pvx.shv_seti(str "vname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.shv_seti'>📖 kamailio.cfg::shv_seti()</a>

#### KSR.pvx.shv_sets() ####

```cpp
int KSR.pvx.shv_sets(str "vname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.shv_sets'>📖 kamailio.cfg::shv_sets()</a>

#### KSR.pvx.var_get() ####

```cpp
xval KSR.pvx.var_get(str "vname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.var_get'>📖 kamailio.cfg::var_get()</a>

#### KSR.pvx.var_seti() ####

```cpp
int KSR.pvx.var_seti(str "vname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.var_seti'>📖 kamailio.cfg::var_seti()</a>

#### KSR.pvx.var_sets() ####

```cpp
int KSR.pvx.var_sets(str "vname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.var_sets'>📖 kamailio.cfg::var_sets()</a>

#### KSR.pvx.xavi_child_get() ####

```cpp
xval KSR.pvx.xavi_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_get'>📖 kamailio.cfg::xavi_child_get()</a>

#### KSR.pvx.xavi_child_gete() ####

```cpp
xval KSR.pvx.xavi_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_gete'>📖 kamailio.cfg::xavi_child_gete()</a>

#### KSR.pvx.xavi_child_getw() ####

```cpp
xval KSR.pvx.xavi_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_getw'>📖 kamailio.cfg::xavi_child_getw()</a>

#### KSR.pvx.xavi_child_is_null() ####

```cpp
int KSR.pvx.xavi_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_is_null'>📖 kamailio.cfg::xavi_child_is_null()</a>

#### KSR.pvx.xavi_child_rm() ####

```cpp
int KSR.pvx.xavi_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_rm'>📖 kamailio.cfg::xavi_child_rm()</a>

#### KSR.pvx.xavi_child_seti() ####

```cpp
int KSR.pvx.xavi_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_seti'>📖 kamailio.cfg::xavi_child_seti()</a>

#### KSR.pvx.xavi_child_sets() ####

```cpp
int KSR.pvx.xavi_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_child_sets'>📖 kamailio.cfg::xavi_child_sets()</a>

#### KSR.pvx.xavi_get() ####

```cpp
xval KSR.pvx.xavi_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_get'>📖 kamailio.cfg::xavi_get()</a>

#### KSR.pvx.xavi_get_keys() ####

```cpp
xval KSR.pvx.xavi_get_keys(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_get_keys'>📖 kamailio.cfg::xavi_get_keys()</a>

#### KSR.pvx.xavi_getd() ####

```cpp
xval KSR.pvx.xavi_getd(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_getd'>📖 kamailio.cfg::xavi_getd()</a>

#### KSR.pvx.xavi_getd_p1() ####

```cpp
xval KSR.pvx.xavi_getd_p1(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_getd_p1'>📖 kamailio.cfg::xavi_getd_p1()</a>

#### KSR.pvx.xavi_gete() ####

```cpp
xval KSR.pvx.xavi_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_gete'>📖 kamailio.cfg::xavi_gete()</a>

#### KSR.pvx.xavi_getw() ####

```cpp
xval KSR.pvx.xavi_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_getw'>📖 kamailio.cfg::xavi_getw()</a>

#### KSR.pvx.xavi_is_null() ####

```cpp
int KSR.pvx.xavi_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_is_null'>📖 kamailio.cfg::xavi_is_null()</a>

#### KSR.pvx.xavi_rm() ####

```cpp
int KSR.pvx.xavi_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_rm'>📖 kamailio.cfg::xavi_rm()</a>

#### KSR.pvx.xavi_seti() ####

```cpp
int KSR.pvx.xavi_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_seti'>📖 kamailio.cfg::xavi_seti()</a>

#### KSR.pvx.xavi_sets() ####

```cpp
int KSR.pvx.xavi_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavi_sets'>📖 kamailio.cfg::xavi_sets()</a>

#### KSR.pvx.xavp_child_get() ####

```cpp
xval KSR.pvx.xavp_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_get'>📖 kamailio.cfg::xavp_child_get()</a>

#### KSR.pvx.xavp_child_gete() ####

```cpp
xval KSR.pvx.xavp_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_gete'>📖 kamailio.cfg::xavp_child_gete()</a>

#### KSR.pvx.xavp_child_getw() ####

```cpp
xval KSR.pvx.xavp_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_getw'>📖 kamailio.cfg::xavp_child_getw()</a>

#### KSR.pvx.xavp_child_is_null() ####

```cpp
int KSR.pvx.xavp_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_is_null'>📖 kamailio.cfg::xavp_child_is_null()</a>

#### KSR.pvx.xavp_child_rm() ####

```cpp
int KSR.pvx.xavp_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_rm'>📖 kamailio.cfg::xavp_child_rm()</a>

#### KSR.pvx.xavp_child_seti() ####

```cpp
int KSR.pvx.xavp_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_seti'>📖 kamailio.cfg::xavp_child_seti()</a>

#### KSR.pvx.xavp_child_sets() ####

```cpp
int KSR.pvx.xavp_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_sets'>📖 kamailio.cfg::xavp_child_sets()</a>

#### KSR.pvx.xavp_copy() ####

```cpp
int KSR.pvx.xavp_copy(str "src_name", int src_idx, str "dst_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_copy'>📖 kamailio.cfg::xavp_copy()</a>

#### KSR.pvx.xavp_copy_dst() ####

```cpp
int KSR.pvx.xavp_copy_dst(str "src_name", int src_idx, str "dst_name", int dst_idx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_copy_dst'>📖 kamailio.cfg::xavp_copy_dst()</a>

#### KSR.pvx.xavp_get() ####

```cpp
xval KSR.pvx.xavp_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_get'>📖 kamailio.cfg::xavp_get()</a>

#### KSR.pvx.xavp_get_keys() ####

```cpp
xval KSR.pvx.xavp_get_keys(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_get_keys'>📖 kamailio.cfg::xavp_get_keys()</a>

#### KSR.pvx.xavp_getd() ####

```cpp
xval KSR.pvx.xavp_getd(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_getd'>📖 kamailio.cfg::xavp_getd()</a>

#### KSR.pvx.xavp_getd_p1() ####

```cpp
xval KSR.pvx.xavp_getd_p1(str "rname", int indx);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_getd_p1'>📖 kamailio.cfg::xavp_getd_p1()</a>

#### KSR.pvx.xavp_gete() ####

```cpp
xval KSR.pvx.xavp_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_gete'>📖 kamailio.cfg::xavp_gete()</a>

#### KSR.pvx.xavp_getw() ####

```cpp
xval KSR.pvx.xavp_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_getw'>📖 kamailio.cfg::xavp_getw()</a>

#### KSR.pvx.xavp_is_null() ####

```cpp
int KSR.pvx.xavp_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_is_null'>📖 kamailio.cfg::xavp_is_null()</a>

#### KSR.pvx.xavp_params_explode() ####

```cpp
int KSR.pvx.xavp_params_explode(str "sparams", str "sxname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_params_explode'>📖 kamailio.cfg::xavp_params_explode()</a>

#### KSR.pvx.xavp_params_implode() ####

```cpp
int KSR.pvx.xavp_params_implode(str "sxname", str "svname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_params_implode'>📖 kamailio.cfg::xavp_params_implode()</a>

#### KSR.pvx.xavp_rm() ####

```cpp
int KSR.pvx.xavp_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_rm'>📖 kamailio.cfg::xavp_rm()</a>

#### KSR.pvx.xavp_seti() ####

```cpp
int KSR.pvx.xavp_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_seti'>📖 kamailio.cfg::xavp_seti()</a>

#### KSR.pvx.xavp_sets() ####

```cpp
int KSR.pvx.xavp_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_sets'>📖 kamailio.cfg::xavp_sets()</a>

#### KSR.pvx.xavp_slist_explode() ####

```cpp
int KSR.pvx.xavp_slist_explode(str "slist", str "sep", str "mode", str "sxname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavp_slist_explode'>📖 kamailio.cfg::xavp_slist_explode()</a>

#### KSR.pvx.xavu_child_get() ####

```cpp
xval KSR.pvx.xavu_child_get(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_get'>📖 kamailio.cfg::xavu_child_get()</a>

#### KSR.pvx.xavu_child_gete() ####

```cpp
xval KSR.pvx.xavu_child_gete(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_gete'>📖 kamailio.cfg::xavu_child_gete()</a>

#### KSR.pvx.xavu_child_getw() ####

```cpp
xval KSR.pvx.xavu_child_getw(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_getw'>📖 kamailio.cfg::xavu_child_getw()</a>

#### KSR.pvx.xavu_child_is_null() ####

```cpp
int KSR.pvx.xavu_child_is_null(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_is_null'>📖 kamailio.cfg::xavu_child_is_null()</a>

#### KSR.pvx.xavu_child_rm() ####

```cpp
int KSR.pvx.xavu_child_rm(str "rname", str "cname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_rm'>📖 kamailio.cfg::xavu_child_rm()</a>

#### KSR.pvx.xavu_child_seti() ####

```cpp
int KSR.pvx.xavu_child_seti(str "rname", str "cname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_seti'>📖 kamailio.cfg::xavu_child_seti()</a>

#### KSR.pvx.xavu_child_sets() ####

```cpp
int KSR.pvx.xavu_child_sets(str "rname", str "cname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_child_sets'>📖 kamailio.cfg::xavu_child_sets()</a>

#### KSR.pvx.xavu_get() ####

```cpp
xval KSR.pvx.xavu_get(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_get'>📖 kamailio.cfg::xavu_get()</a>

#### KSR.pvx.xavu_gete() ####

```cpp
xval KSR.pvx.xavu_gete(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_gete'>📖 kamailio.cfg::xavu_gete()</a>

#### KSR.pvx.xavu_getw() ####

```cpp
xval KSR.pvx.xavu_getw(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_getw'>📖 kamailio.cfg::xavu_getw()</a>

#### KSR.pvx.xavu_is_null() ####

```cpp
int KSR.pvx.xavu_is_null(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_is_null'>📖 kamailio.cfg::xavu_is_null()</a>

#### KSR.pvx.xavu_rm() ####

```cpp
int KSR.pvx.xavu_rm(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_rm'>📖 kamailio.cfg::xavu_rm()</a>

#### KSR.pvx.xavu_seti() ####

```cpp
int KSR.pvx.xavu_seti(str "rname", int ival);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_seti'>📖 kamailio.cfg::xavu_seti()</a>

#### KSR.pvx.xavu_sets() ####

```cpp
int KSR.pvx.xavu_sets(str "rname", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/pvx.html#pvx.f.xavu_sets'>📖 kamailio.cfg::xavu_sets()</a>

## rabbitmq ##

#### KSR.rabbitmq.publish() ####

```cpp
int KSR.rabbitmq.publish(str "exchange", str "routingkey", str "contenttype", str "messagebody");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish'>📖 kamailio.cfg::publish()</a>

#### KSR.rabbitmq.publish_consume() ####

```cpp
int KSR.rabbitmq.publish_consume(str "exchange", str "routingkey", str "contenttype", str "messagebody", str "dpv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish_consume'>📖 kamailio.cfg::publish_consume()</a>

## regex ##

#### KSR.regex.pcre_match() ####

```cpp
int KSR.regex.pcre_match(str "string", str "regex");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/regex.html#regex.f.pcre_match'>📖 kamailio.cfg::pcre_match()</a>

#### KSR.regex.pcre_match_group() ####

```cpp
int KSR.regex.pcre_match_group(str "string", int num_pcre);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/regex.html#regex.f.pcre_match_group'>📖 kamailio.cfg::pcre_match_group()</a>

## registrar ##

#### KSR.registrar.add_sock_hdr() ####

```cpp
int KSR.registrar.add_sock_hdr(str "hdr_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.add_sock_hdr'>📖 kamailio.cfg::add_sock_hdr()</a>

#### KSR.registrar.lookup() ####

```cpp
int KSR.registrar.lookup(str "table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup'>📖 kamailio.cfg::lookup()</a>

#### KSR.registrar.lookup_branches() ####

```cpp
int KSR.registrar.lookup_branches(str "_dtable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_branches'>📖 kamailio.cfg::lookup_branches()</a>

#### KSR.registrar.lookup_to_dset() ####

```cpp
int KSR.registrar.lookup_to_dset(str "table", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_to_dset'>📖 kamailio.cfg::lookup_to_dset()</a>

#### KSR.registrar.lookup_uri() ####

```cpp
int KSR.registrar.lookup_uri(str "table", str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.lookup_uri'>📖 kamailio.cfg::lookup_uri()</a>

#### KSR.registrar.reg_fetch_contacts() ####

```cpp
int KSR.registrar.reg_fetch_contacts(str "dtable", str "uri", str "profile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_fetch_contacts'>📖 kamailio.cfg::reg_fetch_contacts()</a>

#### KSR.registrar.reg_free_contacts() ####

```cpp
int KSR.registrar.reg_free_contacts(str "profile");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_free_contacts'>📖 kamailio.cfg::reg_free_contacts()</a>

#### KSR.registrar.reg_send_reply() ####

```cpp
int KSR.registrar.reg_send_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.reg_send_reply'>📖 kamailio.cfg::reg_send_reply()</a>

#### KSR.registrar.registered() ####

```cpp
int KSR.registrar.registered(str "table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered'>📖 kamailio.cfg::registered()</a>

#### KSR.registrar.registered_action() ####

```cpp
int KSR.registrar.registered_action(str "_dtable", str "_uri", int _f, int _aflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_action'>📖 kamailio.cfg::registered_action()</a>

#### KSR.registrar.registered_flags() ####

```cpp
int KSR.registrar.registered_flags(str "_dtable", str "_uri", int _f);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_flags'>📖 kamailio.cfg::registered_flags()</a>

#### KSR.registrar.registered_uri() ####

```cpp
int KSR.registrar.registered_uri(str "_dtable", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.registered_uri'>📖 kamailio.cfg::registered_uri()</a>

#### KSR.registrar.save() ####

```cpp
int KSR.registrar.save(str "table", int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save'>📖 kamailio.cfg::save()</a>

#### KSR.registrar.save_uri() ####

```cpp
int KSR.registrar.save_uri(str "table", int flags, str "uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.save_uri'>📖 kamailio.cfg::save_uri()</a>

#### KSR.registrar.set_q_override() ####

```cpp
int KSR.registrar.set_q_override(str "new_q");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.set_q_override'>📖 kamailio.cfg::set_q_override()</a>

#### KSR.registrar.unregister() ####

```cpp
int KSR.registrar.unregister(str "_dtable", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister'>📖 kamailio.cfg::unregister()</a>

#### KSR.registrar.unregister_ruid() ####

```cpp
int KSR.registrar.unregister_ruid(str "_dtable", str "_uri", str "_ruid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/registrar.html#registrar.f.unregister_ruid'>📖 kamailio.cfg::unregister_ruid()</a>

## rls ##

#### KSR.rls.handle_notify() ####

```cpp
int KSR.rls.handle_notify();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_notify'>📖 kamailio.cfg::handle_notify()</a>

#### KSR.rls.handle_subscribe() ####

```cpp
int KSR.rls.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe'>📖 kamailio.cfg::handle_subscribe()</a>

#### KSR.rls.handle_subscribe_uri() ####

```cpp
int KSR.rls.handle_subscribe_uri(str "wuri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe_uri'>📖 kamailio.cfg::handle_subscribe_uri()</a>

#### KSR.rls.update_subs() ####

```cpp
int KSR.rls.update_subs(str "uri", str "event");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rls.html#rls.f.update_subs'>📖 kamailio.cfg::update_subs()</a>

## rr ##

#### KSR.rr.add_rr_param() ####

```cpp
int KSR.rr.add_rr_param(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.add_rr_param'>📖 kamailio.cfg::add_rr_param()</a>

#### KSR.rr.check_route_param() ####

```cpp
int KSR.rr.check_route_param(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.check_route_param'>📖 kamailio.cfg::check_route_param()</a>

#### KSR.rr.is_direction() ####

```cpp
int KSR.rr.is_direction(str "dir");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.is_direction'>📖 kamailio.cfg::is_direction()</a>

#### KSR.rr.loose_route() ####

```cpp
int KSR.rr.loose_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route'>📖 kamailio.cfg::loose_route()</a>

#### KSR.rr.loose_route_mode() ####

```cpp
int KSR.rr.loose_route_mode(int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_mode'>📖 kamailio.cfg::loose_route_mode()</a>

#### KSR.rr.loose_route_preloaded() ####

```cpp
int KSR.rr.loose_route_preloaded();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.loose_route_preloaded'>📖 kamailio.cfg::loose_route_preloaded()</a>

#### KSR.rr.next_hop_route() ####

```cpp
int KSR.rr.next_hop_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.next_hop_route'>📖 kamailio.cfg::next_hop_route()</a>

#### KSR.rr.record_route() ####

```cpp
int KSR.rr.record_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route'>📖 kamailio.cfg::record_route()</a>

#### KSR.rr.record_route_advertised_address() ####

```cpp
int KSR.rr.record_route_advertised_address(str "addr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_advertised_address'>📖 kamailio.cfg::record_route_advertised_address()</a>

#### KSR.rr.record_route_params() ####

```cpp
int KSR.rr.record_route_params(str "sparams");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_params'>📖 kamailio.cfg::record_route_params()</a>

#### KSR.rr.record_route_preset() ####

```cpp
int KSR.rr.record_route_preset(str "addr1", str "addr2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset'>📖 kamailio.cfg::record_route_preset()</a>

#### KSR.rr.record_route_preset_one() ####

```cpp
int KSR.rr.record_route_preset_one(str "addr1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.record_route_preset_one'>📖 kamailio.cfg::record_route_preset_one()</a>

#### KSR.rr.remove_record_route() ####

```cpp
int KSR.rr.remove_record_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rr.html#rr.f.remove_record_route'>📖 kamailio.cfg::remove_record_route()</a>

## rtjson ##

#### KSR.rtjson.init_routes() ####

```cpp
int KSR.rtjson.init_routes(str "srdoc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.init_routes'>📖 kamailio.cfg::init_routes()</a>

#### KSR.rtjson.next_route() ####

```cpp
int KSR.rtjson.next_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.next_route'>📖 kamailio.cfg::next_route()</a>

#### KSR.rtjson.push_routes() ####

```cpp
int KSR.rtjson.push_routes();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.push_routes'>📖 kamailio.cfg::push_routes()</a>

#### KSR.rtjson.update_branch() ####

```cpp
int KSR.rtjson.update_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtjson.html#rtjson.f.update_branch'>📖 kamailio.cfg::update_branch()</a>

## rtpengine ##

This module enables media streams to be proxied via an RTPproxy.

#### KSR.rtpengine.block_dtmf() ####

```cpp
int KSR.rtpengine.block_dtmf(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf'>📖 kamailio.cfg::block_dtmf()</a>

#### KSR.rtpengine.block_dtmf0() ####

```cpp
int KSR.rtpengine.block_dtmf0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_dtmf0'>📖 kamailio.cfg::block_dtmf0()</a>

#### KSR.rtpengine.block_media() ####

```cpp
int KSR.rtpengine.block_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media'>📖 kamailio.cfg::block_media()</a>

#### KSR.rtpengine.block_media0() ####

```cpp
int KSR.rtpengine.block_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.block_media0'>📖 kamailio.cfg::block_media0()</a>

#### KSR.rtpengine.play_media() ####

```cpp
int KSR.rtpengine.play_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.play_media'>📖 kamailio.cfg::play_media()</a>

#### KSR.rtpengine.rtpengine_answer() ####

```cpp
int KSR.rtpengine.rtpengine_answer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer'>📖 kamailio.cfg::rtpengine_answer()</a>

#### KSR.rtpengine.rtpengine_answer0() ####

```cpp
int KSR.rtpengine.rtpengine_answer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer0'>📖 kamailio.cfg::rtpengine_answer0()</a>

#### KSR.rtpengine.rtpengine_delete() ####

```cpp
int KSR.rtpengine.rtpengine_delete(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete'>📖 kamailio.cfg::rtpengine_delete()</a>

#### KSR.rtpengine.rtpengine_delete0() ####

```cpp
int KSR.rtpengine.rtpengine_delete0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete0'>📖 kamailio.cfg::rtpengine_delete0()</a>

#### KSR.rtpengine.rtpengine_manage() ####

```cpp
int KSR.rtpengine.rtpengine_manage(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage'>📖 kamailio.cfg::rtpengine_manage()</a>

#### KSR.rtpengine.rtpengine_manage0() ####

```cpp
int KSR.rtpengine.rtpengine_manage0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage0'>📖 kamailio.cfg::rtpengine_manage0()</a>

#### KSR.rtpengine.rtpengine_offer() ####

```cpp
int KSR.rtpengine.rtpengine_offer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer'>📖 kamailio.cfg::rtpengine_offer()</a>

#### KSR.rtpengine.rtpengine_offer0() ####

```cpp
int KSR.rtpengine.rtpengine_offer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer0'>📖 kamailio.cfg::rtpengine_offer0()</a>

#### KSR.rtpengine.rtpengine_query() ####

```cpp
int KSR.rtpengine.rtpengine_query(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query'>📖 kamailio.cfg::rtpengine_query()</a>

#### KSR.rtpengine.rtpengine_query0() ####

```cpp
int KSR.rtpengine.rtpengine_query0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query0'>📖 kamailio.cfg::rtpengine_query0()</a>

#### KSR.rtpengine.set_rtpengine_set() ####

```cpp
int KSR.rtpengine.set_rtpengine_set(int r1);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set'>📖 kamailio.cfg::set_rtpengine_set()</a>

#### KSR.rtpengine.set_rtpengine_set2() ####

```cpp
int KSR.rtpengine.set_rtpengine_set2(int r1, int r2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set2'>📖 kamailio.cfg::set_rtpengine_set2()</a>

This function is the sibling function to [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set). The original module function is declared as
`set_rtpengine_set(setid[, setid2])`.

In KEMI set_rtpengine_set() takes only the first parameter and set_rtpengine_set2() allows for the second optional parameter to be passed.

```
KSR.rtpengine.set_rtpengine_set2(2, 1);
KSR.rtpengine.rtpengine_offer();
```

Please review the documentation for [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set) for more information.

#### KSR.rtpengine.start_recording() ####

```cpp
int KSR.rtpengine.start_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_recording'>📖 kamailio.cfg::start_recording()</a>

#### KSR.rtpengine.stop_media() ####

```cpp
int KSR.rtpengine.stop_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media'>📖 kamailio.cfg::stop_media()</a>

#### KSR.rtpengine.stop_media0() ####

```cpp
int KSR.rtpengine.stop_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_media0'>📖 kamailio.cfg::stop_media0()</a>

#### KSR.rtpengine.stop_recording() ####

```cpp
int KSR.rtpengine.stop_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_recording'>📖 kamailio.cfg::stop_recording()</a>

#### KSR.rtpengine.unblock_dtmf() ####

```cpp
int KSR.rtpengine.unblock_dtmf(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf'>📖 kamailio.cfg::unblock_dtmf()</a>

#### KSR.rtpengine.unblock_dtmf0() ####

```cpp
int KSR.rtpengine.unblock_dtmf0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_dtmf0'>📖 kamailio.cfg::unblock_dtmf0()</a>

#### KSR.rtpengine.unblock_media() ####

```cpp
int KSR.rtpengine.unblock_media(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media'>📖 kamailio.cfg::unblock_media()</a>

#### KSR.rtpengine.unblock_media0() ####

```cpp
int KSR.rtpengine.unblock_media0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpengine.html#rtpengine.f.unblock_media0'>📖 kamailio.cfg::unblock_media0()</a>

## rtpproxy ##

#### KSR.rtpproxy.rtpproxy_answer() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer'>📖 kamailio.cfg::rtpproxy_answer()</a>

#### KSR.rtpproxy.rtpproxy_answer0() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer0'>📖 kamailio.cfg::rtpproxy_answer0()</a>

#### KSR.rtpproxy.rtpproxy_answer_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_answer_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer_ip'>📖 kamailio.cfg::rtpproxy_answer_ip()</a>

#### KSR.rtpproxy.rtpproxy_destroy() ####

```cpp
int KSR.rtpproxy.rtpproxy_destroy(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy'>📖 kamailio.cfg::rtpproxy_destroy()</a>

#### KSR.rtpproxy.rtpproxy_destroy0() ####

```cpp
int KSR.rtpproxy.rtpproxy_destroy0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy0'>📖 kamailio.cfg::rtpproxy_destroy0()</a>

#### KSR.rtpproxy.rtpproxy_manage() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage'>📖 kamailio.cfg::rtpproxy_manage()</a>

#### KSR.rtpproxy.rtpproxy_manage0() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage0'>📖 kamailio.cfg::rtpproxy_manage0()</a>

#### KSR.rtpproxy.rtpproxy_manage_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_manage_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage_ip'>📖 kamailio.cfg::rtpproxy_manage_ip()</a>

#### KSR.rtpproxy.rtpproxy_offer() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer(str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer'>📖 kamailio.cfg::rtpproxy_offer()</a>

#### KSR.rtpproxy.rtpproxy_offer0() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer0();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer0'>📖 kamailio.cfg::rtpproxy_offer0()</a>

#### KSR.rtpproxy.rtpproxy_offer_ip() ####

```cpp
int KSR.rtpproxy.rtpproxy_offer_ip(str "flags", str "mip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer_ip'>📖 kamailio.cfg::rtpproxy_offer_ip()</a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uac() ####

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uac();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uac'>📖 kamailio.cfg::rtpproxy_stop_stream2uac()</a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uas() ####

```cpp
int KSR.rtpproxy.rtpproxy_stop_stream2uas();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uas'>📖 kamailio.cfg::rtpproxy_stop_stream2uas()</a>

#### KSR.rtpproxy.rtpproxy_stream2uac() ####

```cpp
int KSR.rtpproxy.rtpproxy_stream2uac(str "pname", int count);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uac'>📖 kamailio.cfg::rtpproxy_stream2uac()</a>

#### KSR.rtpproxy.rtpproxy_stream2uas() ####

```cpp
int KSR.rtpproxy.rtpproxy_stream2uas(str "pname", int count);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uas'>📖 kamailio.cfg::rtpproxy_stream2uas()</a>

#### KSR.rtpproxy.set_rtpproxy_set() ####

```cpp
int KSR.rtpproxy.set_rtpproxy_set(int rset);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.set_rtpproxy_set'>📖 kamailio.cfg::set_rtpproxy_set()</a>

#### KSR.rtpproxy.start_recording() ####

```cpp
int KSR.rtpproxy.start_recording();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.start_recording'>📖 kamailio.cfg::start_recording()</a>

## sanity ##

#### KSR.sanity.sanity_check() ####

```cpp
int KSR.sanity.sanity_check(int mflags, int uflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check'>📖 kamailio.cfg::sanity_check()</a>

#### KSR.sanity.sanity_check_defaults() ####

```cpp
int KSR.sanity.sanity_check_defaults();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check_defaults'>📖 kamailio.cfg::sanity_check_defaults()</a>

#### KSR.sanity.sanity_reply() ####

```cpp
int KSR.sanity.sanity_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sanity.html#sanity.f.sanity_reply'>📖 kamailio.cfg::sanity_reply()</a>

## sca ##

#### KSR.sca.call_info_update() ####

```cpp
int KSR.sca.call_info_update(int update_mask, str "uri_to", str "uri_from");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update'>📖 kamailio.cfg::call_info_update()</a>

#### KSR.sca.call_info_update_default() ####

```cpp
int KSR.sca.call_info_update_default();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_default'>📖 kamailio.cfg::call_info_update_default()</a>

#### KSR.sca.call_info_update_mask() ####

```cpp
int KSR.sca.call_info_update_mask(int umask);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_mask'>📖 kamailio.cfg::call_info_update_mask()</a>

#### KSR.sca.call_info_update_turi() ####

```cpp
int KSR.sca.call_info_update_turi(int umask, str "sto");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.call_info_update_turi'>📖 kamailio.cfg::call_info_update_turi()</a>

#### KSR.sca.handle_subscribe() ####

```cpp
int KSR.sca.handle_subscribe();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sca.html#sca.f.handle_subscribe'>📖 kamailio.cfg::handle_subscribe()</a>

## sdpops ##

#### KSR.sdpops.keep_codecs_by_id() ####

```cpp
int KSR.sdpops.keep_codecs_by_id(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_id'>📖 kamailio.cfg::keep_codecs_by_id()</a>

#### KSR.sdpops.keep_codecs_by_name() ####

```cpp
int KSR.sdpops.keep_codecs_by_name(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_name'>📖 kamailio.cfg::keep_codecs_by_name()</a>

#### KSR.sdpops.remove_codecs_by_id() ####

```cpp
int KSR.sdpops.remove_codecs_by_id(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_id'>📖 kamailio.cfg::remove_codecs_by_id()</a>

#### KSR.sdpops.remove_codecs_by_name() ####

```cpp
int KSR.sdpops.remove_codecs_by_name(str "codecs", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_name'>📖 kamailio.cfg::remove_codecs_by_name()</a>

#### KSR.sdpops.remove_line_by_prefix() ####

```cpp
int KSR.sdpops.remove_line_by_prefix(str "prefix", str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_line_by_prefix'>📖 kamailio.cfg::remove_line_by_prefix()</a>

#### KSR.sdpops.remove_media() ####

```cpp
int KSR.sdpops.remove_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_media'>📖 kamailio.cfg::remove_media()</a>

#### KSR.sdpops.sdp_content() ####

```cpp
int KSR.sdpops.sdp_content();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content'>📖 kamailio.cfg::sdp_content()</a>

#### KSR.sdpops.sdp_content_flags() ####

```cpp
int KSR.sdpops.sdp_content_flags(int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content_flags'>📖 kamailio.cfg::sdp_content_flags()</a>

#### KSR.sdpops.sdp_get() ####

```cpp
int KSR.sdpops.sdp_get(str "avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get'>📖 kamailio.cfg::sdp_get()</a>

#### KSR.sdpops.sdp_get_line_startswith() ####

```cpp
int KSR.sdpops.sdp_get_line_startswith(str "aname", str "sline");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get_line_startswith'>📖 kamailio.cfg::sdp_get_line_startswith()</a>

#### KSR.sdpops.sdp_print() ####

```cpp
int KSR.sdpops.sdp_print(int llevel);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_print'>📖 kamailio.cfg::sdp_print()</a>

#### KSR.sdpops.sdp_transport() ####

```cpp
int KSR.sdpops.sdp_transport(str "avp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_transport'>📖 kamailio.cfg::sdp_transport()</a>

#### KSR.sdpops.sdp_with_active_media() ####

```cpp
int KSR.sdpops.sdp_with_active_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_active_media'>📖 kamailio.cfg::sdp_with_active_media()</a>

#### KSR.sdpops.sdp_with_codecs_by_id() ####

```cpp
int KSR.sdpops.sdp_with_codecs_by_id(str "codecs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_id'>📖 kamailio.cfg::sdp_with_codecs_by_id()</a>

#### KSR.sdpops.sdp_with_codecs_by_name() ####

```cpp
int KSR.sdpops.sdp_with_codecs_by_name(str "codecs");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_name'>📖 kamailio.cfg::sdp_with_codecs_by_name()</a>

#### KSR.sdpops.sdp_with_ice() ####

```cpp
int KSR.sdpops.sdp_with_ice();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_ice'>📖 kamailio.cfg::sdp_with_ice()</a>

#### KSR.sdpops.sdp_with_media() ####

```cpp
int KSR.sdpops.sdp_with_media(str "media");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_media'>📖 kamailio.cfg::sdp_with_media()</a>

#### KSR.sdpops.sdp_with_transport() ####

```cpp
int KSR.sdpops.sdp_with_transport(str "transport");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport'>📖 kamailio.cfg::sdp_with_transport()</a>

#### KSR.sdpops.sdp_with_transport_like() ####

```cpp
int KSR.sdpops.sdp_with_transport_like(str "transport");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_transport_like'>📖 kamailio.cfg::sdp_with_transport_like()</a>

## secsipid ##

#### KSR.secsipid.secsipid_add_identity() ####

```cpp
int KSR.secsipid.secsipid_add_identity(str "origtn", str "desttn", str "attest", str "origid", str "x5u", str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_add_identity'>📖 kamailio.cfg::secsipid_add_identity()</a>

#### KSR.secsipid.secsipid_check_identity() ####

```cpp
int KSR.secsipid.secsipid_check_identity(str "keypath");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity'>📖 kamailio.cfg::secsipid_check_identity()</a>

#### KSR.secsipid.secsipid_check_identity_pubkey() ####

```cpp
int KSR.secsipid.secsipid_check_identity_pubkey(str "keyval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_check_identity_pubkey'>📖 kamailio.cfg::secsipid_check_identity_pubkey()</a>

#### KSR.secsipid.secsipid_get_url() ####

```cpp
xval KSR.secsipid.secsipid_get_url(str "surl");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/secsipid.html#secsipid.f.secsipid_get_url'>📖 kamailio.cfg::secsipid_get_url()</a>

## sipcapture ##

#### KSR.sipcapture.float2int() ####

```cpp
int KSR.sipcapture.float2int(str "_val", str "_coof");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.float2int'>📖 kamailio.cfg::float2int()</a>

#### KSR.sipcapture.report_capture() ####

```cpp
int KSR.sipcapture.report_capture(str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture'>📖 kamailio.cfg::report_capture()</a>

#### KSR.sipcapture.report_capture_cid() ####

```cpp
int KSR.sipcapture.report_capture_cid(str "_table", str "_cid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_cid'>📖 kamailio.cfg::report_capture_cid()</a>

#### KSR.sipcapture.report_capture_data() ####

```cpp
int KSR.sipcapture.report_capture_data(str "_table", str "_cid", str "_data");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_data'>📖 kamailio.cfg::report_capture_data()</a>

#### KSR.sipcapture.sip_capture() ####

```cpp
int KSR.sipcapture.sip_capture();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture'>📖 kamailio.cfg::sip_capture()</a>

#### KSR.sipcapture.sip_capture_forward() ####

```cpp
int KSR.sipcapture.sip_capture_forward(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_forward'>📖 kamailio.cfg::sip_capture_forward()</a>

#### KSR.sipcapture.sip_capture_mode() ####

```cpp
int KSR.sipcapture.sip_capture_mode(str "_table", str "_cmdata");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_mode'>📖 kamailio.cfg::sip_capture_mode()</a>

#### KSR.sipcapture.sip_capture_table() ####

```cpp
int KSR.sipcapture.sip_capture_table(str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_table'>📖 kamailio.cfg::sip_capture_table()</a>

## sipdump ##

#### KSR.sipdump.get_buf() ####

```cpp
xval KSR.sipdump.get_buf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_buf'>📖 kamailio.cfg::get_buf()</a>

#### KSR.sipdump.get_dst_ip() ####

```cpp
xval KSR.sipdump.get_dst_ip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_dst_ip'>📖 kamailio.cfg::get_dst_ip()</a>

#### KSR.sipdump.get_src_ip() ####

```cpp
xval KSR.sipdump.get_src_ip();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_src_ip'>📖 kamailio.cfg::get_src_ip()</a>

#### KSR.sipdump.get_tag() ####

```cpp
xval KSR.sipdump.get_tag();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.get_tag'>📖 kamailio.cfg::get_tag()</a>

#### KSR.sipdump.send() ####

```cpp
int KSR.sipdump.send(str "stag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipdump.html#sipdump.f.send'>📖 kamailio.cfg::send()</a>

## sipjson ##

#### KSR.sipjson.sj_serialize() ####

```cpp
int KSR.sipjson.sj_serialize(str "smode", str "pvn");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sipjson.html#sipjson.f.sj_serialize'>📖 kamailio.cfg::sj_serialize()</a>

## siptrace ##

#### KSR.siptrace.hlog() ####

```cpp
int KSR.siptrace.hlog(str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog'>📖 kamailio.cfg::hlog()</a>

#### KSR.siptrace.hlog_cid() ####

```cpp
int KSR.siptrace.hlog_cid(str "correlationid", str "message");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog_cid'>📖 kamailio.cfg::hlog_cid()</a>

#### KSR.siptrace.sip_trace() ####

```cpp
int KSR.siptrace.sip_trace();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace'>📖 kamailio.cfg::sip_trace()</a>

#### KSR.siptrace.sip_trace_dst() ####

```cpp
int KSR.siptrace.sip_trace_dst(str "duri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst'>📖 kamailio.cfg::sip_trace_dst()</a>

#### KSR.siptrace.sip_trace_dst_cid() ####

```cpp
int KSR.siptrace.sip_trace_dst_cid(str "duri", str "cid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid'>📖 kamailio.cfg::sip_trace_dst_cid()</a>

#### KSR.siptrace.sip_trace_dst_cid_type() ####

```cpp
int KSR.siptrace.sip_trace_dst_cid_type(str "duri", str "cid", str "sflag");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid_type'>📖 kamailio.cfg::sip_trace_dst_cid_type()</a>

#### KSR.siptrace.sip_trace_mode() ####

```cpp
int KSR.siptrace.sip_trace_mode(str "smode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_mode'>📖 kamailio.cfg::sip_trace_mode()</a>

## siputils ##

#### KSR.siputils.contact_param_decode() ####

```cpp
int KSR.siputils.contact_param_decode(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode'>📖 kamailio.cfg::contact_param_decode()</a>

#### KSR.siputils.contact_param_decode_ruri() ####

```cpp
int KSR.siputils.contact_param_decode_ruri(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_decode_ruri'>📖 kamailio.cfg::contact_param_decode_ruri()</a>

#### KSR.siputils.contact_param_encode() ####

```cpp
int KSR.siputils.contact_param_encode(str "nparam", str "saddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_encode'>📖 kamailio.cfg::contact_param_encode()</a>

#### KSR.siputils.contact_param_rm() ####

```cpp
int KSR.siputils.contact_param_rm(str "nparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.contact_param_rm'>📖 kamailio.cfg::contact_param_rm()</a>

#### KSR.siputils.decode_contact() ####

```cpp
int KSR.siputils.decode_contact();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact'>📖 kamailio.cfg::decode_contact()</a>

#### KSR.siputils.decode_contact_header() ####

```cpp
int KSR.siputils.decode_contact_header();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.decode_contact_header'>📖 kamailio.cfg::decode_contact_header()</a>

#### KSR.siputils.encode_contact() ####

```cpp
int KSR.siputils.encode_contact(str "eprefix", str "eaddr");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.encode_contact'>📖 kamailio.cfg::encode_contact()</a>

#### KSR.siputils.has_totag() ####

```cpp
int KSR.siputils.has_totag();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.has_totag'>📖 kamailio.cfg::has_totag()</a>

#### KSR.siputils.is_alphanum() ####

```cpp
int KSR.siputils.is_alphanum(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanum'>📖 kamailio.cfg::is_alphanum()</a>

#### KSR.siputils.is_alphanumex() ####

```cpp
int KSR.siputils.is_alphanumex(str "tval", str "eset");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanumex'>📖 kamailio.cfg::is_alphanumex()</a>

#### KSR.siputils.is_first_hop() ####

```cpp
int KSR.siputils.is_first_hop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop'>📖 kamailio.cfg::is_first_hop()</a>

#### KSR.siputils.is_numeric() ####

```cpp
int KSR.siputils.is_numeric(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_numeric'>📖 kamailio.cfg::is_numeric()</a>

#### KSR.siputils.is_reply() ####

```cpp
int KSR.siputils.is_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_reply'>📖 kamailio.cfg::is_reply()</a>

#### KSR.siputils.is_request() ####

```cpp
int KSR.siputils.is_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_request'>📖 kamailio.cfg::is_request()</a>

#### KSR.siputils.is_tel_number() ####

```cpp
int KSR.siputils.is_tel_number(str "tval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_tel_number'>📖 kamailio.cfg::is_tel_number()</a>

#### KSR.siputils.is_uri() ####

```cpp
int KSR.siputils.is_uri(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_uri'>📖 kamailio.cfg::is_uri()</a>

#### KSR.siputils.is_user() ####

```cpp
int KSR.siputils.is_user(str "suser");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.is_user'>📖 kamailio.cfg::is_user()</a>

#### KSR.siputils.options_reply() ####

```cpp
int KSR.siputils.options_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.options_reply'>📖 kamailio.cfg::options_reply()</a>

#### KSR.siputils.uri_param() ####

```cpp
int KSR.siputils.uri_param(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param'>📖 kamailio.cfg::uri_param()</a>

#### KSR.siputils.uri_param_any() ####

```cpp
int KSR.siputils.uri_param_any(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_any'>📖 kamailio.cfg::uri_param_any()</a>

#### KSR.siputils.uri_param_rm() ####

```cpp
int KSR.siputils.uri_param_rm(str "sparam");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_rm'>📖 kamailio.cfg::uri_param_rm()</a>

#### KSR.siputils.uri_param_value() ####

```cpp
int KSR.siputils.uri_param_value(str "sparam", str "svalue");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_value'>📖 kamailio.cfg::uri_param_value()</a>

## sl ##

#### KSR.sl.send_reply() ####

```cpp
int KSR.sl.send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply'>📖 kamailio.cfg::send_reply()</a>

#### KSR.sl.send_reply_mode() ####

```cpp
int KSR.sl.send_reply_mode(int code, str "reason", int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.send_reply_mode'>📖 kamailio.cfg::send_reply_mode()</a>

#### KSR.sl.sl_forward_reply() ####

```cpp
int KSR.sl.sl_forward_reply(str "code", str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_forward_reply'>📖 kamailio.cfg::sl_forward_reply()</a>

#### KSR.sl.sl_reply_error() ####

```cpp
int KSR.sl.sl_reply_error();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_reply_error'>📖 kamailio.cfg::sl_reply_error()</a>

#### KSR.sl.sl_send_reply() ####

```cpp
int KSR.sl.sl_send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sl.html#sl.f.sl_send_reply'>📖 kamailio.cfg::sl_send_reply()</a>

## speeddial ##

#### KSR.speeddial.lookup() ####

```cpp
int KSR.speeddial.lookup(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup'>📖 kamailio.cfg::lookup()</a>

#### KSR.speeddial.lookup_owner() ####

```cpp
int KSR.speeddial.lookup_owner(str "stable", str "sowner");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup_owner'>📖 kamailio.cfg::lookup_owner()</a>

## sqlops ##

#### KSR.sqlops.sql_is_null() ####

```cpp
int KSR.sqlops.sql_is_null(str "sres", int i, int j);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_is_null'>📖 kamailio.cfg::sql_is_null()</a>

#### KSR.sqlops.sql_num_columns() ####

```cpp
int KSR.sqlops.sql_num_columns(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_columns'>📖 kamailio.cfg::sql_num_columns()</a>

#### KSR.sqlops.sql_num_rows() ####

```cpp
int KSR.sqlops.sql_num_rows(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_rows'>📖 kamailio.cfg::sql_num_rows()</a>

#### KSR.sqlops.sql_pvquery() ####

```cpp
int KSR.sqlops.sql_pvquery(str "scon", str "squery", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_pvquery'>📖 kamailio.cfg::sql_pvquery()</a>

#### KSR.sqlops.sql_query() ####

```cpp
int KSR.sqlops.sql_query(str "scon", str "squery", str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query'>📖 kamailio.cfg::sql_query()</a>

#### KSR.sqlops.sql_query_async() ####

```cpp
int KSR.sqlops.sql_query_async(str "scon", str "squery");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query_async'>📖 kamailio.cfg::sql_query_async()</a>

#### KSR.sqlops.sql_result_free() ####

```cpp
int KSR.sqlops.sql_result_free(str "sres");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_free'>📖 kamailio.cfg::sql_result_free()</a>

#### KSR.sqlops.sql_result_get() ####

```cpp
xval KSR.sqlops.sql_result_get(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_get'>📖 kamailio.cfg::sql_result_get()</a>

#### KSR.sqlops.sql_result_gete() ####

```cpp
xval KSR.sqlops.sql_result_gete(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_gete'>📖 kamailio.cfg::sql_result_gete()</a>

#### KSR.sqlops.sql_result_getz() ####

```cpp
xval KSR.sqlops.sql_result_getz(str "resid", int row, int col);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_getz'>📖 kamailio.cfg::sql_result_getz()</a>

#### KSR.sqlops.sql_xquery() ####

```cpp
int KSR.sqlops.sql_xquery(str "scon", str "squery", str "xavp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_xquery'>📖 kamailio.cfg::sql_xquery()</a>

## ss7ops ##

#### KSR.ss7ops.isup_to_json() ####

```cpp
int KSR.ss7ops.isup_to_json(int proto);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/ss7ops.html#ss7ops.f.isup_to_json'>📖 kamailio.cfg::isup_to_json()</a>

## sst ##

#### KSR.sst.sst_check_min() ####

```cpp
int KSR.sst.sst_check_min(int flag);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sst.html#sst.f.sst_check_min'>📖 kamailio.cfg::sst_check_min()</a>

## statistics ##

#### KSR.statistics.reset_stat() ####

```cpp
int KSR.statistics.reset_stat(str "sname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statistics.html#statistics.f.reset_stat'>📖 kamailio.cfg::reset_stat()</a>

#### KSR.statistics.update_stat() ####

```cpp
int KSR.statistics.update_stat(str "sname", int sval);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statistics.html#statistics.f.update_stat'>📖 kamailio.cfg::update_stat()</a>

## statsc ##

#### KSR.statsc.statsc_reset() ####

```cpp
int KSR.statsc.statsc_reset();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsc.html#statsc.f.statsc_reset'>📖 kamailio.cfg::statsc_reset()</a>

## statsd ##

#### KSR.statsd.statsd_decr() ####

```cpp
int KSR.statsd.statsd_decr(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_decr'>📖 kamailio.cfg::statsd_decr()</a>

#### KSR.statsd.statsd_gauge() ####

```cpp
int KSR.statsd.statsd_gauge(str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_gauge'>📖 kamailio.cfg::statsd_gauge()</a>

#### KSR.statsd.statsd_incr() ####

```cpp
int KSR.statsd.statsd_incr(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_incr'>📖 kamailio.cfg::statsd_incr()</a>

#### KSR.statsd.statsd_set() ####

```cpp
int KSR.statsd.statsd_set(str "key", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_set'>📖 kamailio.cfg::statsd_set()</a>

#### KSR.statsd.statsd_start() ####

```cpp
int KSR.statsd.statsd_start(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_start'>📖 kamailio.cfg::statsd_start()</a>

#### KSR.statsd.statsd_stop() ####

```cpp
int KSR.statsd.statsd_stop(str "key");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/statsd.html#statsd.f.statsd_stop'>📖 kamailio.cfg::statsd_stop()</a>

## sworker ##

#### KSR.sworker.task() ####

```cpp
int KSR.sworker.task(str "gname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/sworker.html#sworker.f.task'>📖 kamailio.cfg::task()</a>

## tcpops ##

#### KSR.tcpops.tcp_conid_alive() ####

```cpp
int KSR.tcpops.tcp_conid_alive(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_alive'>📖 kamailio.cfg::tcp_conid_alive()</a>

#### KSR.tcpops.tcp_conid_state() ####

```cpp
int KSR.tcpops.tcp_conid_state(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_state'>📖 kamailio.cfg::tcp_conid_state()</a>

#### KSR.tcpops.tcp_enable_closed_event() ####

```cpp
int KSR.tcpops.tcp_enable_closed_event();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event'>📖 kamailio.cfg::tcp_enable_closed_event()</a>

#### KSR.tcpops.tcp_enable_closed_event_cid() ####

```cpp
int KSR.tcpops.tcp_enable_closed_event_cid(int i_conid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event_cid'>📖 kamailio.cfg::tcp_enable_closed_event_cid()</a>

#### KSR.tcpops.tcp_keepalive_disable() ####

```cpp
int KSR.tcpops.tcp_keepalive_disable();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable'>📖 kamailio.cfg::tcp_keepalive_disable()</a>

#### KSR.tcpops.tcp_keepalive_disable_cid() ####

```cpp
int KSR.tcpops.tcp_keepalive_disable_cid(int i_con);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable_cid'>📖 kamailio.cfg::tcp_keepalive_disable_cid()</a>

#### KSR.tcpops.tcp_keepalive_enable() ####

```cpp
int KSR.tcpops.tcp_keepalive_enable(int i_idle, int i_cnt, int i_intvl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable'>📖 kamailio.cfg::tcp_keepalive_enable()</a>

#### KSR.tcpops.tcp_keepalive_enable_cid() ####

```cpp
int KSR.tcpops.tcp_keepalive_enable_cid(int i_con, int i_idle, int i_cnt, int i_intvl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable_cid'>📖 kamailio.cfg::tcp_keepalive_enable_cid()</a>

#### KSR.tcpops.tcp_set_connection_lifetime() ####

```cpp
int KSR.tcpops.tcp_set_connection_lifetime(int i_time);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime'>📖 kamailio.cfg::tcp_set_connection_lifetime()</a>

#### KSR.tcpops.tcp_set_connection_lifetime_cid() ####

```cpp
int KSR.tcpops.tcp_set_connection_lifetime_cid(int i_conid, int i_time);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime_cid'>📖 kamailio.cfg::tcp_set_connection_lifetime_cid()</a>

#### KSR.tcpops.tcp_set_otcpid() ####

```cpp
int KSR.tcpops.tcp_set_otcpid(int vconid);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid'>📖 kamailio.cfg::tcp_set_otcpid()</a>

#### KSR.tcpops.tcp_set_otcpid_flag() ####

```cpp
int KSR.tcpops.tcp_set_otcpid_flag(int vmode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_otcpid_flag'>📖 kamailio.cfg::tcp_set_otcpid_flag()</a>

## textops ##

#### KSR.textops.append_body_part() ####

```cpp
int KSR.textops.append_body_part(str "txt", str "ct");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part'>📖 kamailio.cfg::append_body_part()</a>

#### KSR.textops.append_body_part_cd() ####

```cpp
int KSR.textops.append_body_part_cd(str "txt", str "ct", str "cd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_cd'>📖 kamailio.cfg::append_body_part_cd()</a>

#### KSR.textops.append_body_part_hex() ####

```cpp
int KSR.textops.append_body_part_hex(str "txt", str "ct");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex'>📖 kamailio.cfg::append_body_part_hex()</a>

#### KSR.textops.append_body_part_hex_cd() ####

```cpp
int KSR.textops.append_body_part_hex_cd(str "htxt", str "ct", str "cd");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex_cd'>📖 kamailio.cfg::append_body_part_hex_cd()</a>

#### KSR.textops.cmp_istr() ####

```cpp
int KSR.textops.cmp_istr(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_istr'>📖 kamailio.cfg::cmp_istr()</a>

#### KSR.textops.cmp_str() ####

```cpp
int KSR.textops.cmp_str(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.cmp_str'>📖 kamailio.cfg::cmp_str()</a>

#### KSR.textops.ends_with() ####

```cpp
int KSR.textops.ends_with(str "vstr", str "vsuffix");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.ends_with'>📖 kamailio.cfg::ends_with()</a>

#### KSR.textops.filter_body() ####

```cpp
int KSR.textops.filter_body(str "content_type");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.filter_body'>📖 kamailio.cfg::filter_body()</a>

#### KSR.textops.get_body_part() ####

```cpp
int KSR.textops.get_body_part(str "ctype", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part'>📖 kamailio.cfg::get_body_part()</a>

#### KSR.textops.get_body_part_raw() ####

```cpp
int KSR.textops.get_body_part_raw(str "ctype", str "pvname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.get_body_part_raw'>📖 kamailio.cfg::get_body_part_raw()</a>

#### KSR.textops.has_body() ####

```cpp
int KSR.textops.has_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body'>📖 kamailio.cfg::has_body()</a>

#### KSR.textops.has_body_type() ####

```cpp
int KSR.textops.has_body_type(str "ctype");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.has_body_type'>📖 kamailio.cfg::has_body_type()</a>

#### KSR.textops.in_list() ####

```cpp
int KSR.textops.in_list(str "subject", str "list", str "vsep");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list'>📖 kamailio.cfg::in_list()</a>

#### KSR.textops.in_list_prefix() ####

```cpp
int KSR.textops.in_list_prefix(str "subject", str "list", str "vsep");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.in_list_prefix'>📖 kamailio.cfg::in_list_prefix()</a>

#### KSR.textops.is_audio_on_hold() ####

```cpp
int KSR.textops.is_audio_on_hold();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_audio_on_hold'>📖 kamailio.cfg::is_audio_on_hold()</a>

#### KSR.textops.is_present_hf() ####

```cpp
int KSR.textops.is_present_hf(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf'>📖 kamailio.cfg::is_present_hf()</a>

#### KSR.textops.is_present_hf_re() ####

```cpp
int KSR.textops.is_present_hf_re(str "ematch");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_present_hf_re'>📖 kamailio.cfg::is_present_hf_re()</a>

#### KSR.textops.is_privacy() ####

```cpp
int KSR.textops.is_privacy(str "privacy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.is_privacy'>📖 kamailio.cfg::is_privacy()</a>

#### KSR.textops.regex_substring() ####

```cpp
int KSR.textops.regex_substring(str "input", str "regex", int mindex, int nmatch, str "dst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.regex_substring'>📖 kamailio.cfg::regex_substring()</a>

#### KSR.textops.remove_body_part() ####

```cpp
int KSR.textops.remove_body_part(str "content_type");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_body_part'>📖 kamailio.cfg::remove_body_part()</a>

#### KSR.textops.remove_hf() ####

```cpp
int KSR.textops.remove_hf(str "hname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf'>📖 kamailio.cfg::remove_hf()</a>

#### KSR.textops.remove_hf_exp() ####

```cpp
int KSR.textops.remove_hf_exp(str "ematch", str "eskip");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_exp'>📖 kamailio.cfg::remove_hf_exp()</a>

#### KSR.textops.remove_hf_re() ####

```cpp
int KSR.textops.remove_hf_re(str "ematch");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.remove_hf_re'>📖 kamailio.cfg::remove_hf_re()</a>

#### KSR.textops.replace() ####

```cpp
int KSR.textops.replace(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace'>📖 kamailio.cfg::replace()</a>

#### KSR.textops.replace_all() ####

```cpp
int KSR.textops.replace_all(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_all'>📖 kamailio.cfg::replace_all()</a>

#### KSR.textops.replace_body() ####

```cpp
int KSR.textops.replace_body(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body'>📖 kamailio.cfg::replace_body()</a>

#### KSR.textops.replace_body_all() ####

```cpp
int KSR.textops.replace_body_all(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_all'>📖 kamailio.cfg::replace_body_all()</a>

#### KSR.textops.replace_body_atonce() ####

```cpp
int KSR.textops.replace_body_atonce(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_atonce'>📖 kamailio.cfg::replace_body_atonce()</a>

#### KSR.textops.replace_body_str() ####

```cpp
int KSR.textops.replace_body_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_body_str'>📖 kamailio.cfg::replace_body_str()</a>

#### KSR.textops.replace_hdrs() ####

```cpp
int KSR.textops.replace_hdrs(str "sre", str "sval");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs'>📖 kamailio.cfg::replace_hdrs()</a>

#### KSR.textops.replace_hdrs_str() ####

```cpp
int KSR.textops.replace_hdrs_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs_str'>📖 kamailio.cfg::replace_hdrs_str()</a>

#### KSR.textops.replace_str() ####

```cpp
int KSR.textops.replace_str(str "mkey", str "rval", str "rmode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.replace_str'>📖 kamailio.cfg::replace_str()</a>

#### KSR.textops.search() ####

```cpp
int KSR.textops.search(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search'>📖 kamailio.cfg::search()</a>

#### KSR.textops.search_append() ####

```cpp
int KSR.textops.search_append(str "ematch", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append'>📖 kamailio.cfg::search_append()</a>

#### KSR.textops.search_append_body() ####

```cpp
int KSR.textops.search_append_body(str "ematch", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_append_body'>📖 kamailio.cfg::search_append_body()</a>

#### KSR.textops.search_body() ####

```cpp
int KSR.textops.search_body(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_body'>📖 kamailio.cfg::search_body()</a>

#### KSR.textops.search_hf() ####

```cpp
int KSR.textops.search_hf(str "hname", str "sre", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_hf'>📖 kamailio.cfg::search_hf()</a>

#### KSR.textops.search_str() ####

```cpp
int KSR.textops.search_str(str "stext", str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.search_str'>📖 kamailio.cfg::search_str()</a>

#### KSR.textops.set_body() ####

```cpp
int KSR.textops.set_body(str "nb", str "nc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body'>📖 kamailio.cfg::set_body()</a>

#### KSR.textops.set_body_multipart() ####

```cpp
int KSR.textops.set_body_multipart(str "nbody", str "ctype", str "boundary");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart'>📖 kamailio.cfg::set_body_multipart()</a>

#### KSR.textops.set_body_multipart_boundary() ####

```cpp
int KSR.textops.set_body_multipart_boundary(str "boundary");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_boundary'>📖 kamailio.cfg::set_body_multipart_boundary()</a>

#### KSR.textops.set_body_multipart_content() ####

```cpp
int KSR.textops.set_body_multipart_content(str "nbody", str "ctype");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_content'>📖 kamailio.cfg::set_body_multipart_content()</a>

#### KSR.textops.set_body_multipart_mode() ####

```cpp
int KSR.textops.set_body_multipart_mode();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_mode'>📖 kamailio.cfg::set_body_multipart_mode()</a>

#### KSR.textops.set_reply_body() ####

```cpp
int KSR.textops.set_reply_body(str "nb", str "nc");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.set_reply_body'>📖 kamailio.cfg::set_reply_body()</a>

#### KSR.textops.starts_with() ####

```cpp
int KSR.textops.starts_with(str "s1", str "s2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.starts_with'>📖 kamailio.cfg::starts_with()</a>

#### KSR.textops.subst() ####

```cpp
int KSR.textops.subst(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst'>📖 kamailio.cfg::subst()</a>

#### KSR.textops.subst_body() ####

```cpp
int KSR.textops.subst_body(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_body'>📖 kamailio.cfg::subst_body()</a>

#### KSR.textops.subst_hf() ####

```cpp
int KSR.textops.subst_hf(str "hname", str "subst", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_hf'>📖 kamailio.cfg::subst_hf()</a>

#### KSR.textops.subst_uri() ####

```cpp
int KSR.textops.subst_uri(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_uri'>📖 kamailio.cfg::subst_uri()</a>

#### KSR.textops.subst_user() ####

```cpp
int KSR.textops.subst_user(str "subst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textops.html#textops.f.subst_user'>📖 kamailio.cfg::subst_user()</a>

## textopsx ##

#### KSR.textopsx.append_hf_value() ####

```cpp
int KSR.textopsx.append_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.append_hf_value'>📖 kamailio.cfg::append_hf_value()</a>

#### KSR.textopsx.assign_hf_value() ####

```cpp
int KSR.textopsx.assign_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value'>📖 kamailio.cfg::assign_hf_value()</a>

#### KSR.textopsx.assign_hf_value2() ####

```cpp
int KSR.textopsx.assign_hf_value2(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value2'>📖 kamailio.cfg::assign_hf_value2()</a>

#### KSR.textopsx.change_reply_status() ####

```cpp
int KSR.textopsx.change_reply_status(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status'>📖 kamailio.cfg::change_reply_status()</a>

#### KSR.textopsx.change_reply_status_code() ####

```cpp
int KSR.textopsx.change_reply_status_code(int code);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status_code'>📖 kamailio.cfg::change_reply_status_code()</a>

#### KSR.textopsx.exclude_hf_value() ####

```cpp
int KSR.textopsx.exclude_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.exclude_hf_value'>📖 kamailio.cfg::exclude_hf_value()</a>

#### KSR.textopsx.fnmatch() ####

```cpp
int KSR.textopsx.fnmatch(str "val", str "match");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch'>📖 kamailio.cfg::fnmatch()</a>

#### KSR.textopsx.fnmatch_ex() ####

```cpp
int KSR.textopsx.fnmatch_ex(str "val", str "match", str "flags");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch_ex'>📖 kamailio.cfg::fnmatch_ex()</a>

#### KSR.textopsx.hf_value_exists() ####

```cpp
int KSR.textopsx.hf_value_exists(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_value_exists'>📖 kamailio.cfg::hf_value_exists()</a>

#### KSR.textopsx.include_hf_value() ####

```cpp
int KSR.textopsx.include_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.include_hf_value'>📖 kamailio.cfg::include_hf_value()</a>

#### KSR.textopsx.insert_hf_value() ####

```cpp
int KSR.textopsx.insert_hf_value(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.insert_hf_value'>📖 kamailio.cfg::insert_hf_value()</a>

#### KSR.textopsx.keep_hf() ####

```cpp
int KSR.textopsx.keep_hf();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf'>📖 kamailio.cfg::keep_hf()</a>

#### KSR.textopsx.keep_hf_re() ####

```cpp
int KSR.textopsx.keep_hf_re(str "sre");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf_re'>📖 kamailio.cfg::keep_hf_re()</a>

#### KSR.textopsx.msg_apply_changes() ####

```cpp
int KSR.textopsx.msg_apply_changes();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_apply_changes'>📖 kamailio.cfg::msg_apply_changes()</a>

#### KSR.textopsx.msg_set_buffer() ####

```cpp
int KSR.textopsx.msg_set_buffer(str "obuf");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_set_buffer'>📖 kamailio.cfg::msg_set_buffer()</a>

#### KSR.textopsx.remove_body() ####

```cpp
int KSR.textopsx.remove_body();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_body'>📖 kamailio.cfg::remove_body()</a>

#### KSR.textopsx.remove_hf_value() ####

```cpp
int KSR.textopsx.remove_hf_value(str "hexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value'>📖 kamailio.cfg::remove_hf_value()</a>

#### KSR.textopsx.remove_hf_value2() ####

```cpp
int KSR.textopsx.remove_hf_value2(str "hexp", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value2'>📖 kamailio.cfg::remove_hf_value2()</a>

## tls ##

#### KSR.tls.cget() ####

```cpp
xval KSR.tls.cget(str "aname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.cget'>📖 kamailio.cfg::cget()</a>

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

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tls.html#tls.f.is_peer_verified'>📖 kamailio.cfg::is_peer_verified()</a>

## tm ##

#### KSR.tm.ki_t_load_contacts_mode() ####

```cpp
int KSR.tm.ki_t_load_contacts_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.ki_t_load_contacts_mode'>📖 kamailio.cfg::ki_t_load_contacts_mode()</a>

#### KSR.tm.t_any_replied() ####

```cpp
int KSR.tm.t_any_replied();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_replied'>📖 kamailio.cfg::t_any_replied()</a>

#### KSR.tm.t_any_timeout() ####

```cpp
int KSR.tm.t_any_timeout();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_any_timeout'>📖 kamailio.cfg::t_any_timeout()</a>

#### KSR.tm.t_branch_replied() ####

```cpp
int KSR.tm.t_branch_replied();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_replied'>📖 kamailio.cfg::t_branch_replied()</a>

#### KSR.tm.t_branch_timeout() ####

```cpp
int KSR.tm.t_branch_timeout();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_branch_timeout'>📖 kamailio.cfg::t_branch_timeout()</a>

#### KSR.tm.t_check_status() ####

```cpp
int KSR.tm.t_check_status(str "sexp");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_status'>📖 kamailio.cfg::t_check_status()</a>

#### KSR.tm.t_check_trans() ####

```cpp
int KSR.tm.t_check_trans();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_check_trans'>📖 kamailio.cfg::t_check_trans()</a>

#### KSR.tm.t_clean() ####

```cpp
int KSR.tm.t_clean();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_clean'>📖 kamailio.cfg::t_clean()</a>

#### KSR.tm.t_drop_replies() ####

```cpp
int KSR.tm.t_drop_replies(str "mode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies'>📖 kamailio.cfg::t_drop_replies()</a>

#### KSR.tm.t_drop_replies_all() ####

```cpp
int KSR.tm.t_drop_replies_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies_all'>📖 kamailio.cfg::t_drop_replies_all()</a>

#### KSR.tm.t_get_branch_index() ####

```cpp
int KSR.tm.t_get_branch_index();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_branch_index'>📖 kamailio.cfg::t_get_branch_index()</a>

#### KSR.tm.t_get_status_code() ####

```cpp
int KSR.tm.t_get_status_code();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_get_status_code'>📖 kamailio.cfg::t_get_status_code()</a>

#### KSR.tm.t_grep_status() ####

```cpp
int KSR.tm.t_grep_status(int code);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_grep_status'>📖 kamailio.cfg::t_grep_status()</a>

#### KSR.tm.t_is_canceled() ####

```cpp
int KSR.tm.t_is_canceled();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_canceled'>📖 kamailio.cfg::t_is_canceled()</a>

#### KSR.tm.t_is_expired() ####

```cpp
int KSR.tm.t_is_expired();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_expired'>📖 kamailio.cfg::t_is_expired()</a>

#### KSR.tm.t_is_retr_async_reply() ####

```cpp
int KSR.tm.t_is_retr_async_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_retr_async_reply'>📖 kamailio.cfg::t_is_retr_async_reply()</a>

#### KSR.tm.t_is_set() ####

```cpp
int KSR.tm.t_is_set(str "target");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_is_set'>📖 kamailio.cfg::t_is_set()</a>

#### KSR.tm.t_load_contacts() ####

```cpp
int KSR.tm.t_load_contacts();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_load_contacts'>📖 kamailio.cfg::t_load_contacts()</a>

#### KSR.tm.t_lookup_cancel() ####

```cpp
int KSR.tm.t_lookup_cancel();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel'>📖 kamailio.cfg::t_lookup_cancel()</a>

#### KSR.tm.t_lookup_cancel_flags() ####

```cpp
int KSR.tm.t_lookup_cancel_flags(int flags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel_flags'>📖 kamailio.cfg::t_lookup_cancel_flags()</a>

#### KSR.tm.t_lookup_request() ####

```cpp
int KSR.tm.t_lookup_request();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_lookup_request'>📖 kamailio.cfg::t_lookup_request()</a>

#### KSR.tm.t_newtran() ####

```cpp
int KSR.tm.t_newtran();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_newtran'>📖 kamailio.cfg::t_newtran()</a>

#### KSR.tm.t_next_contact_flow() ####

```cpp
int KSR.tm.t_next_contact_flow();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contact_flow'>📖 kamailio.cfg::t_next_contact_flow()</a>

#### KSR.tm.t_next_contacts() ####

```cpp
int KSR.tm.t_next_contacts();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_next_contacts'>📖 kamailio.cfg::t_next_contacts()</a>

#### KSR.tm.t_on_branch() ####

```cpp
int KSR.tm.t_on_branch(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch'>📖 kamailio.cfg::t_on_branch()</a>

#### KSR.tm.t_on_branch_failure() ####

```cpp
int KSR.tm.t_on_branch_failure(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_branch_failure'>📖 kamailio.cfg::t_on_branch_failure()</a>

#### KSR.tm.t_on_failure() ####

```cpp
int KSR.tm.t_on_failure(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_failure'>📖 kamailio.cfg::t_on_failure()</a>

#### KSR.tm.t_on_reply() ####

```cpp
int KSR.tm.t_on_reply(str "rname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_on_reply'>📖 kamailio.cfg::t_on_reply()</a>

#### KSR.tm.t_relay() ####

```cpp
int KSR.tm.t_relay();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay'>📖 kamailio.cfg::t_relay()</a>

#### KSR.tm.t_relay_to_flags() ####

```cpp
int KSR.tm.t_relay_to_flags(int rflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_flags'>📖 kamailio.cfg::t_relay_to_flags()</a>

#### KSR.tm.t_relay_to_proto() ####

```cpp
int KSR.tm.t_relay_to_proto(str "sproto");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto'>📖 kamailio.cfg::t_relay_to_proto()</a>

#### KSR.tm.t_relay_to_proto_addr() ####

```cpp
int KSR.tm.t_relay_to_proto_addr(str "sproto", str "host", int port);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proto_addr'>📖 kamailio.cfg::t_relay_to_proto_addr()</a>

#### KSR.tm.t_relay_to_proxy() ####

```cpp
int KSR.tm.t_relay_to_proxy(str "sproxy");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy'>📖 kamailio.cfg::t_relay_to_proxy()</a>

#### KSR.tm.t_relay_to_proxy_flags() ####

```cpp
int KSR.tm.t_relay_to_proxy_flags(str "sproxy", int rflags);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy_flags'>📖 kamailio.cfg::t_relay_to_proxy_flags()</a>

#### KSR.tm.t_release() ####

```cpp
int KSR.tm.t_release();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_release'>📖 kamailio.cfg::t_release()</a>

#### KSR.tm.t_replicate() ####

```cpp
int KSR.tm.t_replicate(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_replicate'>📖 kamailio.cfg::t_replicate()</a>

#### KSR.tm.t_reply() ####

```cpp
int KSR.tm.t_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reply'>📖 kamailio.cfg::t_reply()</a>

#### KSR.tm.t_reset_fr() ####

```cpp
int KSR.tm.t_reset_fr();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_fr'>📖 kamailio.cfg::t_reset_fr()</a>

#### KSR.tm.t_reset_max_lifetime() ####

```cpp
int KSR.tm.t_reset_max_lifetime();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_max_lifetime'>📖 kamailio.cfg::t_reset_max_lifetime()</a>

#### KSR.tm.t_reset_retr() ####

```cpp
int KSR.tm.t_reset_retr();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_reset_retr'>📖 kamailio.cfg::t_reset_retr()</a>

#### KSR.tm.t_retransmit_reply() ####

```cpp
int KSR.tm.t_retransmit_reply();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_retransmit_reply'>📖 kamailio.cfg::t_retransmit_reply()</a>

#### KSR.tm.t_save_lumps() ####

```cpp
int KSR.tm.t_save_lumps();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_save_lumps'>📖 kamailio.cfg::t_save_lumps()</a>

#### KSR.tm.t_send_reply() ####

```cpp
int KSR.tm.t_send_reply(int code, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_send_reply'>📖 kamailio.cfg::t_send_reply()</a>

#### KSR.tm.t_set_auto_inv_100() ####

```cpp
int KSR.tm.t_set_auto_inv_100(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_auto_inv_100'>📖 kamailio.cfg::t_set_auto_inv_100()</a>

#### KSR.tm.t_set_disable_6xx() ####

```cpp
int KSR.tm.t_set_disable_6xx(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_6xx'>📖 kamailio.cfg::t_set_disable_6xx()</a>

#### KSR.tm.t_set_disable_failover() ####

```cpp
int KSR.tm.t_set_disable_failover(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_failover'>📖 kamailio.cfg::t_set_disable_failover()</a>

#### KSR.tm.t_set_disable_internal_reply() ####

```cpp
int KSR.tm.t_set_disable_internal_reply(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_internal_reply'>📖 kamailio.cfg::t_set_disable_internal_reply()</a>

#### KSR.tm.t_set_fr() ####

```cpp
int KSR.tm.t_set_fr(int fr_inv, int fr);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr'>📖 kamailio.cfg::t_set_fr()</a>

#### KSR.tm.t_set_fr_inv() ####

```cpp
int KSR.tm.t_set_fr_inv(int fr_inv);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_fr_inv'>📖 kamailio.cfg::t_set_fr_inv()</a>

#### KSR.tm.t_set_max_lifetime() ####

```cpp
int KSR.tm.t_set_max_lifetime(int t1, int t2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_max_lifetime'>📖 kamailio.cfg::t_set_max_lifetime()</a>

#### KSR.tm.t_set_no_e2e_cancel_reason() ####

```cpp
int KSR.tm.t_set_no_e2e_cancel_reason(int state);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_no_e2e_cancel_reason'>📖 kamailio.cfg::t_set_no_e2e_cancel_reason()</a>

#### KSR.tm.t_set_retr() ####

```cpp
int KSR.tm.t_set_retr(int t1, int t2);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_set_retr'>📖 kamailio.cfg::t_set_retr()</a>

#### KSR.tm.t_uac_send() ####

```cpp
int KSR.tm.t_uac_send(str "method", str "ruri", str "nexthop", str "ssock", str "hdrs", str "body");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_uac_send'>📖 kamailio.cfg::t_uac_send()</a>

#### KSR.tm.t_use_uac_headers() ####

```cpp
int KSR.tm.t_use_uac_headers();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tm.html#tm.f.t_use_uac_headers'>📖 kamailio.cfg::t_use_uac_headers()</a>

## tmrec ##

#### KSR.tmrec.is_leap_year() ####

```cpp
int KSR.tmrec.is_leap_year(int y);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year'>📖 kamailio.cfg::is_leap_year()</a>

#### KSR.tmrec.is_leap_year_now() ####

```cpp
int KSR.tmrec.is_leap_year_now();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year_now'>📖 kamailio.cfg::is_leap_year_now()</a>

#### KSR.tmrec.match() ####

```cpp
int KSR.tmrec.match(str "rv");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match'>📖 kamailio.cfg::match()</a>

#### KSR.tmrec.match_timestamp() ####

```cpp
int KSR.tmrec.match_timestamp(str "rv", int ti);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.match_timestamp'>📖 kamailio.cfg::match_timestamp()</a>

#### KSR.tmrec.time_period_match() ####

```cpp
int KSR.tmrec.time_period_match(str "period");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match'>📖 kamailio.cfg::time_period_match()</a>

#### KSR.tmrec.time_period_match_timestamp() ####

```cpp
int KSR.tmrec.time_period_match_timestamp(str "period", int ti);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match_timestamp'>📖 kamailio.cfg::time_period_match_timestamp()</a>

## tmx ##

#### KSR.tmx.t_cancel_branches() ####

```cpp
int KSR.tmx.t_cancel_branches(str "mode");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_branches'>📖 kamailio.cfg::t_cancel_branches()</a>

#### KSR.tmx.t_cancel_callid() ####

```cpp
int KSR.tmx.t_cancel_callid(str "callid_s", str "cseq_s", int fl);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid'>📖 kamailio.cfg::t_cancel_callid()</a>

#### KSR.tmx.t_cancel_callid_reason() ####

```cpp
int KSR.tmx.t_cancel_callid_reason(str "callid_s", str "cseq_s", int fl, int rcode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid_reason'>📖 kamailio.cfg::t_cancel_callid_reason()</a>

#### KSR.tmx.t_continue() ####

```cpp
int KSR.tmx.t_continue(int tindex, int tlabel, str "cbname");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_continue'>📖 kamailio.cfg::t_continue()</a>

#### KSR.tmx.t_drop() ####

```cpp
int KSR.tmx.t_drop();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop'>📖 kamailio.cfg::t_drop()</a>

#### KSR.tmx.t_drop_rcode() ####

```cpp
int KSR.tmx.t_drop_rcode(int rcode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_drop_rcode'>📖 kamailio.cfg::t_drop_rcode()</a>

#### KSR.tmx.t_flush_flags() ####

```cpp
int KSR.tmx.t_flush_flags();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_flags'>📖 kamailio.cfg::t_flush_flags()</a>

#### KSR.tmx.t_flush_xflags() ####

```cpp
int KSR.tmx.t_flush_xflags();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_xflags'>📖 kamailio.cfg::t_flush_xflags()</a>

#### KSR.tmx.t_is_branch_route() ####

```cpp
int KSR.tmx.t_is_branch_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_branch_route'>📖 kamailio.cfg::t_is_branch_route()</a>

#### KSR.tmx.t_is_failure_route() ####

```cpp
int KSR.tmx.t_is_failure_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_failure_route'>📖 kamailio.cfg::t_is_failure_route()</a>

#### KSR.tmx.t_is_reply_route() ####

```cpp
int KSR.tmx.t_is_reply_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_reply_route'>📖 kamailio.cfg::t_is_reply_route()</a>

#### KSR.tmx.t_is_request_route() ####

```cpp
int KSR.tmx.t_is_request_route();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_is_request_route'>📖 kamailio.cfg::t_is_request_route()</a>

#### KSR.tmx.t_precheck_trans() ####

```cpp
int KSR.tmx.t_precheck_trans();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_precheck_trans'>📖 kamailio.cfg::t_precheck_trans()</a>

#### KSR.tmx.t_reply_callid() ####

```cpp
int KSR.tmx.t_reply_callid(str "callid_s", str "cseq_s", int code, str "status_s");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reply_callid'>📖 kamailio.cfg::t_reply_callid()</a>

#### KSR.tmx.t_reuse_branch() ####

```cpp
int KSR.tmx.t_reuse_branch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_reuse_branch'>📖 kamailio.cfg::t_reuse_branch()</a>

#### KSR.tmx.t_suspend() ####

```cpp
int KSR.tmx.t_suspend();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tmx.html#tmx.f.t_suspend'>📖 kamailio.cfg::t_suspend()</a>

## tsilo ##

#### KSR.tsilo.ts_append() ####

```cpp
int KSR.tsilo.ts_append(str "_table", str "_ruri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append'>📖 kamailio.cfg::ts_append()</a>

#### KSR.tsilo.ts_append_to() ####

```cpp
int KSR.tsilo.ts_append_to(int tindex, int tlabel, str "_table");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to'>📖 kamailio.cfg::ts_append_to()</a>

#### KSR.tsilo.ts_append_to_uri() ####

```cpp
int KSR.tsilo.ts_append_to_uri(int tindex, int tlabel, str "_table", str "_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to_uri'>📖 kamailio.cfg::ts_append_to_uri()</a>

#### KSR.tsilo.ts_store() ####

```cpp
int KSR.tsilo.ts_store();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store'>📖 kamailio.cfg::ts_store()</a>

#### KSR.tsilo.ts_store_uri() ####

```cpp
int KSR.tsilo.ts_store_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store_uri'>📖 kamailio.cfg::ts_store_uri()</a>

## uac ##

#### KSR.uac.uac_auth() ####

```cpp
int KSR.uac.uac_auth();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth'>📖 kamailio.cfg::uac_auth()</a>

#### KSR.uac.uac_auth_mode() ####

```cpp
int KSR.uac.uac_auth_mode(int mode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_auth_mode'>📖 kamailio.cfg::uac_auth_mode()</a>

#### KSR.uac.uac_reg_disable() ####

```cpp
int KSR.uac.uac_reg_disable(str "attr", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_disable'>📖 kamailio.cfg::uac_reg_disable()</a>

#### KSR.uac.uac_reg_enable() ####

```cpp
int KSR.uac.uac_reg_enable(str "attr", str "val");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_enable'>📖 kamailio.cfg::uac_reg_enable()</a>

#### KSR.uac.uac_reg_lookup() ####

```cpp
int KSR.uac.uac_reg_lookup(str "userid", str "sdst");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup'>📖 kamailio.cfg::uac_reg_lookup()</a>

#### KSR.uac.uac_reg_refresh() ####

```cpp
int KSR.uac.uac_reg_refresh(str "l_uuid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_refresh'>📖 kamailio.cfg::uac_reg_refresh()</a>

#### KSR.uac.uac_reg_request_to() ####

```cpp
int KSR.uac.uac_reg_request_to(str "userid", int imode);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_request_to'>📖 kamailio.cfg::uac_reg_request_to()</a>

#### KSR.uac.uac_reg_status() ####

```cpp
int KSR.uac.uac_reg_status(str "sruuid");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_reg_status'>📖 kamailio.cfg::uac_reg_status()</a>

#### KSR.uac.uac_replace_from() ####

```cpp
int KSR.uac.uac_replace_from(str "pdsp", str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from'>📖 kamailio.cfg::uac_replace_from()</a>

#### KSR.uac.uac_replace_from_uri() ####

```cpp
int KSR.uac.uac_replace_from_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from_uri'>📖 kamailio.cfg::uac_replace_from_uri()</a>

#### KSR.uac.uac_replace_to() ####

```cpp
int KSR.uac.uac_replace_to(str "pdsp", str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to'>📖 kamailio.cfg::uac_replace_to()</a>

#### KSR.uac.uac_replace_to_uri() ####

```cpp
int KSR.uac.uac_replace_to_uri(str "puri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to_uri'>📖 kamailio.cfg::uac_replace_to_uri()</a>

#### KSR.uac.uac_req_send() ####

```cpp
int KSR.uac.uac_req_send();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_req_send'>📖 kamailio.cfg::uac_req_send()</a>

#### KSR.uac.uac_restore_from() ####

```cpp
int KSR.uac.uac_restore_from();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_from'>📖 kamailio.cfg::uac_restore_from()</a>

#### KSR.uac.uac_restore_to() ####

```cpp
int KSR.uac.uac_restore_to();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac.html#uac.f.uac_restore_to'>📖 kamailio.cfg::uac_restore_to()</a>

## uac_redirect ##

#### KSR.uac_redirect.get_redirects() ####

```cpp
int KSR.uac_redirect.get_redirects(int max_c, int max_b);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects'>📖 kamailio.cfg::get_redirects()</a>

#### KSR.uac_redirect.get_redirects_acc() ####

```cpp
int KSR.uac_redirect.get_redirects_acc(int max_c, int max_b, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_acc'>📖 kamailio.cfg::get_redirects_acc()</a>

#### KSR.uac_redirect.get_redirects_all() ####

```cpp
int KSR.uac_redirect.get_redirects_all();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_all'>📖 kamailio.cfg::get_redirects_all()</a>

## uri_db ##

#### KSR.uri_db.check_from() ####

```cpp
int KSR.uri_db.check_from();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_from'>📖 kamailio.cfg::check_from()</a>

#### KSR.uri_db.check_to() ####

```cpp
int KSR.uri_db.check_to();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_to'>📖 kamailio.cfg::check_to()</a>

#### KSR.uri_db.check_uri() ####

```cpp
int KSR.uri_db.check_uri(str "suri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri'>📖 kamailio.cfg::check_uri()</a>

#### KSR.uri_db.check_uri_realm() ####

```cpp
int KSR.uri_db.check_uri_realm(str "suri", str "susername", str "srealm");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri_realm'>📖 kamailio.cfg::check_uri_realm()</a>

#### KSR.uri_db.does_uri_exist() ####

```cpp
int KSR.uri_db.does_uri_exist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/uri_db.html#uri_db.f.does_uri_exist'>📖 kamailio.cfg::does_uri_exist()</a>

## userblocklist ##

#### KSR.userblocklist.check_allowlist() ####

```cpp
int KSR.userblocklist.check_allowlist(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_allowlist'>📖 kamailio.cfg::check_allowlist()</a>

#### KSR.userblocklist.check_blocklist() ####

```cpp
int KSR.userblocklist.check_blocklist(str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_blocklist'>📖 kamailio.cfg::check_blocklist()</a>

#### KSR.userblocklist.check_global_blocklist() ####

```cpp
int KSR.userblocklist.check_global_blocklist();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_global_blocklist'>📖 kamailio.cfg::check_global_blocklist()</a>

#### KSR.userblocklist.check_user_allowlist() ####

```cpp
int KSR.userblocklist.check_user_allowlist(str "suser", str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist'>📖 kamailio.cfg::check_user_allowlist()</a>

#### KSR.userblocklist.check_user_allowlist_number() ####

```cpp
int KSR.userblocklist.check_user_allowlist_number(str "suser", str "sdomain", str "snumber");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_number'>📖 kamailio.cfg::check_user_allowlist_number()</a>

#### KSR.userblocklist.check_user_allowlist_table() ####

```cpp
int KSR.userblocklist.check_user_allowlist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_allowlist_table'>📖 kamailio.cfg::check_user_allowlist_table()</a>

#### KSR.userblocklist.check_user_blocklist() ####

```cpp
int KSR.userblocklist.check_user_blocklist(str "suser", str "sdomain");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist'>📖 kamailio.cfg::check_user_blocklist()</a>

#### KSR.userblocklist.check_user_blocklist_number() ####

```cpp
int KSR.userblocklist.check_user_blocklist_number(str "suser", str "sdomain", str "snumber");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_number'>📖 kamailio.cfg::check_user_blocklist_number()</a>

#### KSR.userblocklist.check_user_blocklist_table() ####

```cpp
int KSR.userblocklist.check_user_blocklist_table(str "suser", str "sdomain", str "snumber", str "stable");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/userblocklist.html#userblocklist.f.check_user_blocklist_table'>📖 kamailio.cfg::check_user_blocklist_table()</a>

## utils ##

#### KSR.utils.xcap_auth_status() ####

```cpp
int KSR.utils.xcap_auth_status(str "watcher_uri", str "presentity_uri");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/utils.html#utils.f.xcap_auth_status'>📖 kamailio.cfg::xcap_auth_status()</a>

## websocket ##

#### KSR.websocket.close() ####

```cpp
int KSR.websocket.close();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close'>📖 kamailio.cfg::close()</a>

#### KSR.websocket.close_conid() ####

```cpp
int KSR.websocket.close_conid(int status, str "reason", int con);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_conid'>📖 kamailio.cfg::close_conid()</a>

#### KSR.websocket.close_reason() ####

```cpp
int KSR.websocket.close_reason(int status, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.close_reason'>📖 kamailio.cfg::close_reason()</a>

#### KSR.websocket.handle_handshake() ####

```cpp
int KSR.websocket.handle_handshake();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/websocket.html#websocket.f.handle_handshake'>📖 kamailio.cfg::handle_handshake()</a>

## xcap_server ##

#### KSR.xcap_server.xcaps_del() ####

```cpp
int KSR.xcap_server.xcaps_del(str "uri", str "path");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_del'>📖 kamailio.cfg::xcaps_del()</a>

#### KSR.xcap_server.xcaps_get() ####

```cpp
int KSR.xcap_server.xcaps_get(str "uri", str "path");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_get'>📖 kamailio.cfg::xcaps_get()</a>

#### KSR.xcap_server.xcaps_put() ####

```cpp
int KSR.xcap_server.xcaps_put(str "uri", str "path", str "pbody");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_put'>📖 kamailio.cfg::xcaps_put()</a>

## xhttp ##

#### KSR.xhttp.get_hu() ####

```cpp
xval KSR.xhttp.get_hu();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp.html#xhttp.f.get_hu'>📖 kamailio.cfg::get_hu()</a>

#### KSR.xhttp.xhttp_reply() ####

```cpp
int KSR.xhttp.xhttp_reply(int code, str "reason", str "ctype", str "body");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp.html#xhttp.f.xhttp_reply'>📖 kamailio.cfg::xhttp_reply()</a>

## xhttp_pi ##

#### KSR.xhttp_pi.dispatch() ####

```cpp
int KSR.xhttp_pi.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_pi.html#xhttp_pi.f.dispatch'>📖 kamailio.cfg::dispatch()</a>

## xhttp_prom ##

#### KSR.xhttp_prom.check_uri() ####

```cpp
int KSR.xhttp_prom.check_uri();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.check_uri'>📖 kamailio.cfg::check_uri()</a>

#### KSR.xhttp_prom.counter_inc_l0() ####

```cpp
int KSR.xhttp_prom.counter_inc_l0(str "s_name", int number);
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l0'>📖 kamailio.cfg::counter_inc_l0()</a>

#### KSR.xhttp_prom.counter_inc_l1() ####

```cpp
int KSR.xhttp_prom.counter_inc_l1(str "s_name", int number, str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l1'>📖 kamailio.cfg::counter_inc_l1()</a>

#### KSR.xhttp_prom.counter_inc_l2() ####

```cpp
int KSR.xhttp_prom.counter_inc_l2(str "s_name", int number, str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l2'>📖 kamailio.cfg::counter_inc_l2()</a>

#### KSR.xhttp_prom.counter_inc_l3() ####

```cpp
int KSR.xhttp_prom.counter_inc_l3(str "s_name", int number, str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l3'>📖 kamailio.cfg::counter_inc_l3()</a>

#### KSR.xhttp_prom.counter_reset_l0() ####

```cpp
int KSR.xhttp_prom.counter_reset_l0(str "s_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l0'>📖 kamailio.cfg::counter_reset_l0()</a>

#### KSR.xhttp_prom.counter_reset_l1() ####

```cpp
int KSR.xhttp_prom.counter_reset_l1(str "s_name", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l1'>📖 kamailio.cfg::counter_reset_l1()</a>

#### KSR.xhttp_prom.counter_reset_l2() ####

```cpp
int KSR.xhttp_prom.counter_reset_l2(str "s_name", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l2'>📖 kamailio.cfg::counter_reset_l2()</a>

#### KSR.xhttp_prom.counter_reset_l3() ####

```cpp
int KSR.xhttp_prom.counter_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l3'>📖 kamailio.cfg::counter_reset_l3()</a>

#### KSR.xhttp_prom.dispatch() ####

```cpp
int KSR.xhttp_prom.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.dispatch'>📖 kamailio.cfg::dispatch()</a>

#### KSR.xhttp_prom.gauge_reset_l0() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l0(str "s_name");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l0'>📖 kamailio.cfg::gauge_reset_l0()</a>

#### KSR.xhttp_prom.gauge_reset_l1() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l1(str "s_name", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l1'>📖 kamailio.cfg::gauge_reset_l1()</a>

#### KSR.xhttp_prom.gauge_reset_l2() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l2(str "s_name", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l2'>📖 kamailio.cfg::gauge_reset_l2()</a>

#### KSR.xhttp_prom.gauge_reset_l3() ####

```cpp
int KSR.xhttp_prom.gauge_reset_l3(str "s_name", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l3'>📖 kamailio.cfg::gauge_reset_l3()</a>

#### KSR.xhttp_prom.gauge_set_l0() ####

```cpp
int KSR.xhttp_prom.gauge_set_l0(str "s_name", str "s_number");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l0'>📖 kamailio.cfg::gauge_set_l0()</a>

#### KSR.xhttp_prom.gauge_set_l1() ####

```cpp
int KSR.xhttp_prom.gauge_set_l1(str "s_name", str "s_number", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l1'>📖 kamailio.cfg::gauge_set_l1()</a>

#### KSR.xhttp_prom.gauge_set_l2() ####

```cpp
int KSR.xhttp_prom.gauge_set_l2(str "s_name", str "s_number", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l2'>📖 kamailio.cfg::gauge_set_l2()</a>

#### KSR.xhttp_prom.gauge_set_l3() ####

```cpp
int KSR.xhttp_prom.gauge_set_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l3'>📖 kamailio.cfg::gauge_set_l3()</a>

#### KSR.xhttp_prom.histogram_observe_l0() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l0(str "s_name", str "s_number");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l0'>📖 kamailio.cfg::histogram_observe_l0()</a>

#### KSR.xhttp_prom.histogram_observe_l1() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l1(str "s_name", str "s_number", str "l1");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l1'>📖 kamailio.cfg::histogram_observe_l1()</a>

#### KSR.xhttp_prom.histogram_observe_l2() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l2(str "s_name", str "s_number", str "l1", str "l2");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l2'>📖 kamailio.cfg::histogram_observe_l2()</a>

#### KSR.xhttp_prom.histogram_observe_l3() ####

```cpp
int KSR.xhttp_prom.histogram_observe_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.histogram_observe_l3'>📖 kamailio.cfg::histogram_observe_l3()</a>

## xhttp_rpc ##

#### KSR.xhttp_rpc.dispatch() ####

```cpp
int KSR.xhttp_rpc.dispatch();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xhttp_rpc.html#xhttp_rpc.f.dispatch'>📖 kamailio.cfg::dispatch()</a>

## xlog ##

#### KSR.xlog.xalert() ####

```cpp
int KSR.xlog.xalert(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xalert'>📖 kamailio.cfg::xalert()</a>

#### KSR.xlog.xcrit() ####

```cpp
int KSR.xlog.xcrit(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xcrit'>📖 kamailio.cfg::xcrit()</a>

#### KSR.xlog.xdbg() ####

```cpp
int KSR.xlog.xdbg(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xdbg'>📖 kamailio.cfg::xdbg()</a>

#### KSR.xlog.xerr() ####

```cpp
int KSR.xlog.xerr(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xerr'>📖 kamailio.cfg::xerr()</a>

#### KSR.xlog.xinfo() ####

```cpp
int KSR.xlog.xinfo(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xinfo'>📖 kamailio.cfg::xinfo()</a>

#### KSR.xlog.xlog() ####

```cpp
int KSR.xlog.xlog(str "slevel", str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xlog'>📖 kamailio.cfg::xlog()</a>

#### KSR.xlog.xnotice() ####

```cpp
int KSR.xlog.xnotice(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xnotice'>📖 kamailio.cfg::xnotice()</a>

#### KSR.xlog.xwarn() ####

```cpp
int KSR.xlog.xwarn(str "lmsg");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xlog.html#xlog.f.xwarn'>📖 kamailio.cfg::xwarn()</a>

## xmlrpc ##

#### KSR.xmlrpc.dispatch_rpc() ####

```cpp
int KSR.xmlrpc.dispatch_rpc();
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.dispatch_rpc'>📖 kamailio.cfg::dispatch_rpc()</a>

#### KSR.xmlrpc.xmlrpc_reply() ####

```cpp
int KSR.xmlrpc.xmlrpc_reply(int rcode, str "reason");
```

  * <a target='_blank' href='https://kamailio.org/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.xmlrpc_reply'>📖 kamailio.cfg::xmlrpc_reply()</a>

