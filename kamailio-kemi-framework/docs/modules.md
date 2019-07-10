<!-- This file is auto-generated. Any manual modifications will be deleted -->
# KEMI Module Functions #
The following sections lists all exported KEMI functions. More information regarding the function can be found by clicking the KEMI prototype which will take you the original module's documentation.

## acc ##

The functions exported by `acc` module to KEMI are listed in the next sections.

The documentation of `acc` module is available online at:

  * [acc.html](https://kamailio.org/docs/modules/devel/modules/acc.html)

#### KSR.acc.acc_db_request() ####

<a target='_blank' href='/docs/modules/devel/modules/acc.html#acc.f.acc_db_request'> `int acc_db_request(str "comment", str "dbtable")` </a>

Equivalent of native kamailio.cfg function: `acc_db_request("comment", "dbtable")`.

#### KSR.acc.acc_log_request() ####

<a target='_blank' href='/docs/modules/devel/modules/acc.html#acc.f.acc_log_request'> `int acc_log_request(str "comment")` </a>

Equivalent of native kamailio.cfg function: `acc_log_request("comment")`.

#### KSR.acc.acc_request() ####

<a target='_blank' href='/docs/modules/devel/modules/acc.html#acc.f.acc_request'> `int acc_request(str "comment", str "dbtable")` </a>

Equivalent of native kamailio.cfg function: `acc_request("comment", "dbtable")`.

## acc_radius ##

#### KSR.acc_radius.request() ####

<a target='_blank' href='/docs/modules/devel/modules/acc_radius.html#acc_radius.f.request'> `int request(str "comment")` </a>

## alias_db ##

#### KSR.alias_db.lookup() ####

<a target='_blank' href='/docs/modules/devel/modules/alias_db.html#alias_db.f.lookup'> `int lookup(str "stable")` </a>

#### KSR.alias_db.lookup_ex() ####

<a target='_blank' href='/docs/modules/devel/modules/alias_db.html#alias_db.f.lookup_ex'> `int lookup_ex(str "stable", str "sflags")` </a>

## app_jsdt ##

#### KSR.app_jsdt.dofile() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.dofile'> `int dofile(str "script")` </a>

#### KSR.app_jsdt.dostring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.dostring'> `int dostring(str "script")` </a>

#### KSR.app_jsdt.run() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run'> `int run(str "func")` </a>

#### KSR.app_jsdt.run_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p1'> `int run_p1(str "func", str "p1")` </a>

#### KSR.app_jsdt.run_p2() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p2'> `int run_p2(str "func", str "p1", str "p2")` </a>

#### KSR.app_jsdt.run_p3() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.run_p3'> `int run_p3(str "func", str "p1", str "p2", str "p3")` </a>

#### KSR.app_jsdt.runstring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_jsdt.html#app_jsdt.f.runstring'> `int runstring(str "script")` </a>

## app_lua ##

#### KSR.app_lua.dofile() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.dofile'> `int dofile(str "script")` </a>

#### KSR.app_lua.dostring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.dostring'> `int dostring(str "script")` </a>

#### KSR.app_lua.run() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.run'> `int run(str "func")` </a>

#### KSR.app_lua.run_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p1'> `int run_p1(str "func", str "p1")` </a>

#### KSR.app_lua.run_p2() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p2'> `int run_p2(str "func", str "p1", str "p2")` </a>

#### KSR.app_lua.run_p3() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.run_p3'> `int run_p3(str "func", str "p1", str "p2", str "p3")` </a>

#### KSR.app_lua.runstring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_lua.html#app_lua.f.runstring'> `int runstring(str "script")` </a>

## app_python ##

#### KSR.app_python.exec() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python.html#app_python.f.exec'> `int exec(str "method")` </a>

#### KSR.app_python.exec_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python.html#app_python.f.exec_p1'> `int exec_p1(str "method", str "p1")` </a>

#### KSR.app_python.execx() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python.html#app_python.f.execx'> `int execx(str "method")` </a>

## app_python3 ##

#### KSR.app_python3.exec() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python3.html#app_python3.f.exec'> `int exec(str "method")` </a>

#### KSR.app_python3.exec_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python3.html#app_python3.f.exec_p1'> `int exec_p1(str "method", str "p1")` </a>

#### KSR.app_python3.execx() ####

<a target='_blank' href='/docs/modules/devel/modules/app_python3.html#app_python3.f.execx'> `int execx(str "method")` </a>

## app_ruby ##

#### KSR.app_ruby.run() ####

<a target='_blank' href='/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run'> `int run(str "func")` </a>

#### KSR.app_ruby.run_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p1'> `int run_p1(str "func", str "p1")` </a>

#### KSR.app_ruby.run_p2() ####

<a target='_blank' href='/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p2'> `int run_p2(str "func", str "p1", str "p2")` </a>

#### KSR.app_ruby.run_p3() ####

<a target='_blank' href='/docs/modules/devel/modules/app_ruby.html#app_ruby.f.run_p3'> `int run_p3(str "func", str "p1", str "p2", str "p3")` </a>

## app_sqlang ##

#### KSR.app_sqlang.dofile() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dofile'> `int dofile(str "script")` </a>

#### KSR.app_sqlang.dostring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.dostring'> `int dostring(str "script")` </a>

#### KSR.app_sqlang.run() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run'> `int run(str "func")` </a>

#### KSR.app_sqlang.run_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p1'> `int run_p1(str "func", str "p1")` </a>

#### KSR.app_sqlang.run_p2() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p2'> `int run_p2(str "func", str "p1", str "p2")` </a>

#### KSR.app_sqlang.run_p3() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.run_p3'> `int run_p3(str "func", str "p1", str "p2", str "p3")` </a>

#### KSR.app_sqlang.runstring() ####

<a target='_blank' href='/docs/modules/devel/modules/app_sqlang.html#app_sqlang.f.runstring'> `int runstring(str "script")` </a>

## async ##

#### KSR.async.route() ####

<a target='_blank' href='/docs/modules/devel/modules/async.html#async.f.route'> `int route(str "rn", int s)` </a>

#### KSR.async.task_route() ####

<a target='_blank' href='/docs/modules/devel/modules/async.html#async.f.task_route'> `int task_route(str "rn")` </a>

## auth ##

#### KSR.auth.auth_challenge() ####

<a target='_blank' href='/docs/modules/devel/modules/auth.html#auth.f.auth_challenge'> `int auth_challenge(str "realm", int flags)` </a>

#### KSR.auth.consume_credentials() ####

<a target='_blank' href='/docs/modules/devel/modules/auth.html#auth.f.consume_credentials'> `int consume_credentials()` </a>

#### KSR.auth.has_credentials() ####

<a target='_blank' href='/docs/modules/devel/modules/auth.html#auth.f.has_credentials'> `int has_credentials(str "srealm")` </a>

#### KSR.auth.pv_auth_check() ####

<a target='_blank' href='/docs/modules/devel/modules/auth.html#auth.f.pv_auth_check'> `int pv_auth_check(str "srealm", str "spasswd", int vflags, int vchecks)` </a>

## auth_db ##

#### KSR.auth_db.auth_check() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_db.html#auth_db.f.auth_check'> `int auth_check(str "srealm", str "stable", int iflags)` </a>

#### KSR.auth_db.is_subscriber() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_db.html#auth_db.f.is_subscriber'> `int is_subscriber(str "suri", str "stable", int iflags)` </a>

## auth_ephemeral ##

#### KSR.auth_ephemeral.autheph_authenticate() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_authenticate'> `int autheph_authenticate(str "susername", str "spassword")` </a>

#### KSR.auth_ephemeral.autheph_check() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_check'> `int autheph_check(str "srealm")` </a>

#### KSR.auth_ephemeral.autheph_proxy() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_proxy'> `int autheph_proxy(str "srealm")` </a>

#### KSR.auth_ephemeral.autheph_www() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www'> `int autheph_www(str "srealm")` </a>

#### KSR.auth_ephemeral.autheph_www_method() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_ephemeral.html#auth_ephemeral.f.autheph_www_method'> `int autheph_www_method(str "srealm", str "smethod")` </a>

## auth_radius ##

#### KSR.auth_radius.proxy_authorize() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize'> `int proxy_authorize(str "srealm")` </a>

#### KSR.auth_radius.proxy_authorize_user() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_radius.html#auth_radius.f.proxy_authorize_user'> `int proxy_authorize_user(str "srealm", str "suser")` </a>

#### KSR.auth_radius.www_authorize() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize'> `int www_authorize(str "srealm")` </a>

#### KSR.auth_radius.www_authorize_user() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_radius.html#auth_radius.f.www_authorize_user'> `int www_authorize_user(str "srealm", str "suser")` </a>

## auth_xkeys ##

#### KSR.auth_xkeys.auth_xkeys_add() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_add'> `int auth_xkeys_add(str "shdr", str "skey", str "salg", str "sdata")` </a>

#### KSR.auth_xkeys.auth_xkeys_check() ####

<a target='_blank' href='/docs/modules/devel/modules/auth_xkeys.html#auth_xkeys.f.auth_xkeys_check'> `int auth_xkeys_check(str "shdr", str "skey", str "salg", str "sdata")` </a>

## benchmark ##

#### KSR.benchmark.bm_log_timer() ####

<a target='_blank' href='/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_log_timer'> `int bm_log_timer(str "tname")` </a>

#### KSR.benchmark.bm_start_timer() ####

<a target='_blank' href='/docs/modules/devel/modules/benchmark.html#benchmark.f.bm_start_timer'> `int bm_start_timer(str "tname")` </a>

## blst ##

#### KSR.blst.blst_add() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_add'> `int blst_add(int t)` </a>

#### KSR.blst.blst_add_default() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_add_default'> `int blst_add_default()` </a>

#### KSR.blst.blst_add_retry_after() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_add_retry_after'> `int blst_add_retry_after(int t_min, int t_max)` </a>

#### KSR.blst.blst_clear_ignore() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore'> `int blst_clear_ignore(int mask)` </a>

#### KSR.blst.blst_clear_ignore_all() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_clear_ignore_all'> `int blst_clear_ignore_all()` </a>

#### KSR.blst.blst_del() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_del'> `int blst_del()` </a>

#### KSR.blst.blst_is_blacklisted() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_is_blacklisted'> `int blst_is_blacklisted()` </a>

#### KSR.blst.blst_rpl_clear_ignore() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore'> `int blst_rpl_clear_ignore(int mask)` </a>

#### KSR.blst.blst_rpl_clear_ignore_all() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_clear_ignore_all'> `int blst_rpl_clear_ignore_all()` </a>

#### KSR.blst.blst_rpl_set_ignore() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore'> `int blst_rpl_set_ignore(int mask)` </a>

#### KSR.blst.blst_rpl_set_ignore_all() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_rpl_set_ignore_all'> `int blst_rpl_set_ignore_all()` </a>

#### KSR.blst.blst_set_ignore() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore'> `int blst_set_ignore(int mask)` </a>

#### KSR.blst.blst_set_ignore_all() ####

<a target='_blank' href='/docs/modules/devel/modules/blst.html#blst.f.blst_set_ignore_all'> `int blst_set_ignore_all()` </a>

## call_control ##

#### KSR.call_control.call_control() ####

<a target='_blank' href='/docs/modules/devel/modules/call_control.html#call_control.f.call_control'> `int call_control()` </a>

## call_obj ##

#### KSR.call_obj.free() ####

<a target='_blank' href='/docs/modules/devel/modules/call_obj.html#call_obj.f.free'> `int free(int num_obj)` </a>

#### KSR.call_obj.get() ####

<a target='_blank' href='/docs/modules/devel/modules/call_obj.html#call_obj.f.get'> `int get()` </a>

## cfgutils ##

#### KSR.cfgutils.abort() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.abort'> `int abort()` </a>

#### KSR.cfgutils.core_hash() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.core_hash'> `int core_hash(str "s1", str "s2", int sz)` </a>

#### KSR.cfgutils.lock() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.lock'> `int lock(str "lkey")` </a>

#### KSR.cfgutils.pkg_status() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_status'> `int pkg_status()` </a>

#### KSR.cfgutils.pkg_summary() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.pkg_summary'> `int pkg_summary()` </a>

#### KSR.cfgutils.rand_event() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_event'> `int rand_event()` </a>

#### KSR.cfgutils.rand_get_prob() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_get_prob'> `int rand_get_prob()` </a>

#### KSR.cfgutils.rand_reset_prob() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_reset_prob'> `int rand_reset_prob()` </a>

#### KSR.cfgutils.rand_set_prob() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.rand_set_prob'> `int rand_set_prob(int percent_par)` </a>

#### KSR.cfgutils.shm_status() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_status'> `int shm_status()` </a>

#### KSR.cfgutils.shm_summary() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.shm_summary'> `int shm_summary()` </a>

#### KSR.cfgutils.sleep() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.sleep'> `int sleep(int v)` </a>

#### KSR.cfgutils.trylock() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.trylock'> `int trylock(str "lkey")` </a>

#### KSR.cfgutils.unlock() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.unlock'> `int unlock(str "lkey")` </a>

#### KSR.cfgutils.usleep() ####

<a target='_blank' href='/docs/modules/devel/modules/cfgutils.html#cfgutils.f.usleep'> `int usleep(int v)` </a>

## cnxcc ##

#### KSR.cnxcc.get_channel_count() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.get_channel_count'> `int get_channel_count(str "sclient", str "pvname")` </a>

#### KSR.cnxcc.set_max_channels() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_channels'> `int set_max_channels(str "sclient", int max_chan)` </a>

#### KSR.cnxcc.set_max_credit() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_credit'> `int set_max_credit(str "sclient", str "scredit", str "sconnect", str "scps", int initp, int finishp)` </a>

#### KSR.cnxcc.set_max_time() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.set_max_time'> `int set_max_time(str "sclient", int max_secs)` </a>

#### KSR.cnxcc.terminate_all() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.terminate_all'> `int terminate_all(str "sclient")` </a>

#### KSR.cnxcc.update_max_time() ####

<a target='_blank' href='/docs/modules/devel/modules/cnxcc.html#cnxcc.f.update_max_time'> `int update_max_time(str "sclient", int secs)` </a>

## corex ##

#### KSR.corex.append_branch() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.append_branch'> `int append_branch()` </a>

#### KSR.corex.append_branch_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri'> `int append_branch_uri(str "uri")` </a>

#### KSR.corex.append_branch_uri_q() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.append_branch_uri_q'> `int append_branch_uri_q(str "uri", str "q")` </a>

#### KSR.corex.has_ruri_user() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.has_ruri_user'> `int has_ruri_user()` </a>

#### KSR.corex.has_user_agent() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.has_user_agent'> `int has_user_agent()` </a>

#### KSR.corex.isxflagset() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.isxflagset'> `int isxflagset(int fval)` </a>

#### KSR.corex.resetxflag() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.resetxflag'> `int resetxflag(int fval)` </a>

#### KSR.corex.send_data() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.send_data'> `int send_data(str "uri", str "data")` </a>

#### KSR.corex.sendx() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.sendx'> `int sendx(str "uri", str "sock", str "data")` </a>

#### KSR.corex.set_recv_socket() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.set_recv_socket'> `int set_recv_socket(str "ssock")` </a>

#### KSR.corex.set_send_socket() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.set_send_socket'> `int set_send_socket(str "ssock")` </a>

#### KSR.corex.set_source_address() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.set_source_address'> `int set_source_address(str "saddr")` </a>

#### KSR.corex.setxflag() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.setxflag'> `int setxflag(int fval)` </a>

#### KSR.corex.via_add_srvid() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.via_add_srvid'> `int via_add_srvid(int fval)` </a>

#### KSR.corex.via_add_xavp_params() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.via_add_xavp_params'> `int via_add_xavp_params(int fval)` </a>

#### KSR.corex.via_use_xavp_fields() ####

<a target='_blank' href='/docs/modules/devel/modules/corex.html#corex.f.via_use_xavp_fields'> `int via_use_xavp_fields(int fval)` </a>

## counters ##

#### KSR.counters.add() ####

<a target='_blank' href='/docs/modules/devel/modules/counters.html#counters.f.add'> `int add(str "sname", int v)` </a>

#### KSR.counters.inc() ####

<a target='_blank' href='/docs/modules/devel/modules/counters.html#counters.f.inc'> `int inc(str "sname")` </a>

#### KSR.counters.reset() ####

<a target='_blank' href='/docs/modules/devel/modules/counters.html#counters.f.reset'> `int reset(str "sname")` </a>

## crypto ##

#### KSR.crypto.aes_decrypt() ####

<a target='_blank' href='/docs/modules/devel/modules/crypto.html#crypto.f.aes_decrypt'> `int aes_decrypt(str "ins", str "keys", str "dpv")` </a>

#### KSR.crypto.aes_encrypt() ####

<a target='_blank' href='/docs/modules/devel/modules/crypto.html#crypto.f.aes_encrypt'> `int aes_encrypt(str "ins", str "keys", str "dpv")` </a>

## debugger ##

#### KSR.debugger.dbg_pv_dump() ####

<a target='_blank' href='/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump'> `int dbg_pv_dump()` </a>

#### KSR.debugger.dbg_pv_dump_ex() ####

<a target='_blank' href='/docs/modules/devel/modules/debugger.html#debugger.f.dbg_pv_dump_ex'> `int dbg_pv_dump_ex(int mask, int level)` </a>

## dialog ##

#### KSR.dialog.dlg_bye() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_bye'> `int dlg_bye(str "side")` </a>

#### KSR.dialog.dlg_db_load_callid() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_callid'> `int dlg_db_load_callid(str "callid")` </a>

#### KSR.dialog.dlg_db_load_extra() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_db_load_extra'> `int dlg_db_load_extra()` </a>

#### KSR.dialog.dlg_get() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_get'> `int dlg_get(str "sc", str "sf", str "st")` </a>

#### KSR.dialog.dlg_isflagset() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_isflagset'> `int dlg_isflagset(int val)` </a>

#### KSR.dialog.dlg_manage() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_manage'> `int dlg_manage()` </a>

#### KSR.dialog.dlg_resetflag() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_resetflag'> `int dlg_resetflag(int val)` </a>

#### KSR.dialog.dlg_set_property() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_property'> `int dlg_set_property(str "pval")` </a>

#### KSR.dialog.dlg_set_timeout() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout'> `int dlg_set_timeout(int to)` </a>

#### KSR.dialog.dlg_set_timeout_id() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_set_timeout_id'> `int dlg_set_timeout_id(int to, int he, int hi)` </a>

#### KSR.dialog.dlg_setflag() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.dlg_setflag'> `int dlg_setflag(int val)` </a>

#### KSR.dialog.get_profile_size() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size'> `int get_profile_size(str "sprofile", str "svalue", str "spv")` </a>

#### KSR.dialog.get_profile_size_static() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.get_profile_size_static'> `int get_profile_size_static(str "sprofile", str "spv")` </a>

#### KSR.dialog.is_in_profile() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile'> `int is_in_profile(str "sprofile", str "svalue")` </a>

#### KSR.dialog.is_in_profile_static() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.is_in_profile_static'> `int is_in_profile_static(str "sprofile")` </a>

#### KSR.dialog.is_known_dlg() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.is_known_dlg'> `int is_known_dlg()` </a>

#### KSR.dialog.set_dlg_profile() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile'> `int set_dlg_profile(str "sprofile", str "svalue")` </a>

#### KSR.dialog.set_dlg_profile_static() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.set_dlg_profile_static'> `int set_dlg_profile_static(str "sprofile")` </a>

#### KSR.dialog.unset_dlg_profile() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile'> `int unset_dlg_profile(str "sprofile", str "svalue")` </a>

#### KSR.dialog.unset_dlg_profile_static() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.unset_dlg_profile_static'> `int unset_dlg_profile_static(str "sprofile")` </a>

#### KSR.dialog.var_get() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_get'> `xval var_get(str "name")` </a>

#### KSR.dialog.var_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_gete'> `xval var_gete(str "name")` </a>

#### KSR.dialog.var_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_getw'> `xval var_getw(str "name")` </a>

#### KSR.dialog.var_is_null() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_is_null'> `int var_is_null(str "name")` </a>

#### KSR.dialog.var_rm() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_rm'> `int var_rm(str "name")` </a>

#### KSR.dialog.var_sets() ####

<a target='_blank' href='/docs/modules/devel/modules/dialog.html#dialog.f.var_sets'> `int var_sets(str "name", str "val")` </a>

## dialplan ##

#### KSR.dialplan.dp_match() ####

<a target='_blank' href='/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_match'> `int dp_match(int dpid, str "src")` </a>

#### KSR.dialplan.dp_replace() ####

<a target='_blank' href='/docs/modules/devel/modules/dialplan.html#dialplan.f.dp_replace'> `int dp_replace(int dpid, str "src", str "dst")` </a>

## dispatcher ##

#### KSR.dispatcher.ds_is_from_list() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list'> `int ds_is_from_list(int group)` </a>

#### KSR.dispatcher.ds_is_from_list_mode() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_mode'> `int ds_is_from_list_mode(int vset, int vmode)` </a>

#### KSR.dispatcher.ds_is_from_list_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_list_uri'> `int ds_is_from_list_uri(int vset, int vmode, str "vuri")` </a>

#### KSR.dispatcher.ds_is_from_lists() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_is_from_lists'> `int ds_is_from_lists()` </a>

#### KSR.dispatcher.ds_list_exists() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_list_exists'> `int ds_list_exists(int set)` </a>

#### KSR.dispatcher.ds_load_unset() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_unset'> `int ds_load_unset()` </a>

#### KSR.dispatcher.ds_load_update() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_load_update'> `int ds_load_update()` </a>

#### KSR.dispatcher.ds_mark_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst'> `int ds_mark_dst()` </a>

#### KSR.dispatcher.ds_mark_dst_state() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_mark_dst_state'> `int ds_mark_dst_state(str "sval")` </a>

#### KSR.dispatcher.ds_next_domain() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_domain'> `int ds_next_domain()` </a>

#### KSR.dispatcher.ds_next_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_next_dst'> `int ds_next_dst()` </a>

#### KSR.dispatcher.ds_reload() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_reload'> `int ds_reload()` </a>

#### KSR.dispatcher.ds_select() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select'> `int ds_select(int set, int alg)` </a>

#### KSR.dispatcher.ds_select_domain() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain'> `int ds_select_domain(int set, int alg)` </a>

#### KSR.dispatcher.ds_select_domain_limit() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_domain_limit'> `int ds_select_domain_limit(int set, int alg, int limit)` </a>

#### KSR.dispatcher.ds_select_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst'> `int ds_select_dst(int set, int alg)` </a>

#### KSR.dispatcher.ds_select_dst_limit() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_dst_limit'> `int ds_select_dst_limit(int set, int alg, int limit)` </a>

#### KSR.dispatcher.ds_select_limit() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_limit'> `int ds_select_limit(int set, int alg, int limit)` </a>

#### KSR.dispatcher.ds_select_routes() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes'> `int ds_select_routes(str "srules", str "smode")` </a>

#### KSR.dispatcher.ds_select_routes_limit() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_select_routes_limit'> `int ds_select_routes_limit(str "srules", str "smode", int rlimit)` </a>

#### KSR.dispatcher.ds_set_domain() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_domain'> `int ds_set_domain()` </a>

#### KSR.dispatcher.ds_set_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/dispatcher.html#dispatcher.f.ds_set_dst'> `int ds_set_dst()` </a>

## diversion ##

#### KSR.diversion.add_diversion() ####

<a target='_blank' href='/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion'> `int add_diversion(str "reason")` </a>

#### KSR.diversion.add_diversion_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/diversion.html#diversion.f.add_diversion_uri'> `int add_diversion_uri(str "reason", str "uri")` </a>

## dmq ##

#### KSR.dmq.bcast_message() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.bcast_message'> `int bcast_message(str "peer_str", str "body_str", str "ct_str")` </a>

#### KSR.dmq.handle_message() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.handle_message'> `int handle_message()` </a>

#### KSR.dmq.handle_message_rc() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.handle_message_rc'> `int handle_message_rc(int returnval)` </a>

#### KSR.dmq.is_from_node() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.is_from_node'> `int is_from_node()` </a>

#### KSR.dmq.send_message() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.send_message'> `int send_message(str "peer_str", str "to_str", str "body_str", str "ct_str")` </a>

#### KSR.dmq.t_replicate() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate'> `int t_replicate()` </a>

#### KSR.dmq.t_replicate_mode() ####

<a target='_blank' href='/docs/modules/devel/modules/dmq.html#dmq.f.t_replicate_mode'> `int t_replicate_mode(int mode)` </a>

## domain ##

#### KSR.domain.is_domain_local() ####

<a target='_blank' href='/docs/modules/devel/modules/domain.html#domain.f.is_domain_local'> `int is_domain_local(str "sdomain")` </a>

#### KSR.domain.is_from_local() ####

<a target='_blank' href='/docs/modules/devel/modules/domain.html#domain.f.is_from_local'> `int is_from_local()` </a>

#### KSR.domain.is_uri_host_local() ####

<a target='_blank' href='/docs/modules/devel/modules/domain.html#domain.f.is_uri_host_local'> `int is_uri_host_local()` </a>

#### KSR.domain.lookup_domain() ####

<a target='_blank' href='/docs/modules/devel/modules/domain.html#domain.f.lookup_domain'> `int lookup_domain(str "_sdomain")` </a>

#### KSR.domain.lookup_domain_prefix() ####

<a target='_blank' href='/docs/modules/devel/modules/domain.html#domain.f.lookup_domain_prefix'> `int lookup_domain_prefix(str "_sdomain", str "_sprefix")` </a>

## drouting ##

#### KSR.drouting.do_routing() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.do_routing'> `int do_routing(int grp_id)` </a>

#### KSR.drouting.do_routing_furi() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.do_routing_furi'> `int do_routing_furi()` </a>

#### KSR.drouting.goes_to_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw'> `int goes_to_gw()` </a>

#### KSR.drouting.goes_to_gw_type() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.goes_to_gw_type'> `int goes_to_gw_type(int type)` </a>

#### KSR.drouting.is_from_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw'> `int is_from_gw()` </a>

#### KSR.drouting.is_from_gw_type() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type'> `int is_from_gw_type(int type)` </a>

#### KSR.drouting.is_from_gw_type_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.is_from_gw_type_flags'> `int is_from_gw_type_flags(int type, int flags)` </a>

#### KSR.drouting.next_routing() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.next_routing'> `int next_routing()` </a>

#### KSR.drouting.use_next_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/drouting.html#drouting.f.use_next_gw'> `int use_next_gw()` </a>

## enum ##

#### KSR.enum.enum_i_query_suffix() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_i_query_suffix'> `int enum_i_query_suffix(str "vsuffix")` </a>

#### KSR.enum.enum_pv_query() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query'> `int enum_pv_query(str "ve164")` </a>

#### KSR.enum.enum_pv_query_suffix() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix'> `int enum_pv_query_suffix(str "ve164", str "vsuffix")` </a>

#### KSR.enum.enum_pv_query_suffix_service() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_pv_query_suffix_service'> `int enum_pv_query_suffix_service(str "ve164", str "vsuffix", str "vservice")` </a>

#### KSR.enum.enum_query() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_query'> `int enum_query()` </a>

#### KSR.enum.enum_query_suffix() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix'> `int enum_query_suffix(str "vsuffix")` </a>

#### KSR.enum.enum_query_suffix_service() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.enum_query_suffix_service'> `int enum_query_suffix_service(str "vsuffix", str "vservice")` </a>

#### KSR.enum.i_enum_query() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.i_enum_query'> `int i_enum_query()` </a>

#### KSR.enum.i_enum_query_suffix_service() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.i_enum_query_suffix_service'> `int i_enum_query_suffix_service(str "vsuffix", str "vservice")` </a>

#### KSR.enum.is_from_user_enum() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum'> `int is_from_user_enum()` </a>

#### KSR.enum.is_from_user_enum_suffix() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix'> `int is_from_user_enum_suffix(str "vsuffix")` </a>

#### KSR.enum.is_from_user_enum_suffix_service() ####

<a target='_blank' href='/docs/modules/devel/modules/enum.html#enum.f.is_from_user_enum_suffix_service'> `int is_from_user_enum_suffix_service(str "vsuffix", str "vservice")` </a>

## evapi ##

#### KSR.evapi.async_relay() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.async_relay'> `int async_relay(str "sdata")` </a>

#### KSR.evapi.close() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.close'> `int close()` </a>

#### KSR.evapi.relay() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.relay'> `int relay(str "sdata")` </a>

#### KSR.evapi.relay_multicast() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.relay_multicast'> `int relay_multicast(str "sdata", str "stag")` </a>

#### KSR.evapi.relay_unicast() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.relay_unicast'> `int relay_unicast(str "sdata", str "stag")` </a>

#### KSR.evapi.set_tag() ####

<a target='_blank' href='/docs/modules/devel/modules/evapi.html#evapi.f.set_tag'> `int set_tag(str "stag")` </a>

## exec ##

#### KSR.exec.exec_avp() ####

<a target='_blank' href='/docs/modules/devel/modules/exec.html#exec.f.exec_avp'> `int exec_avp(str "cmd")` </a>

#### KSR.exec.exec_cmd() ####

<a target='_blank' href='/docs/modules/devel/modules/exec.html#exec.f.exec_cmd'> `int exec_cmd(str "cmd")` </a>

#### KSR.exec.exec_dset() ####

<a target='_blank' href='/docs/modules/devel/modules/exec.html#exec.f.exec_dset'> `int exec_dset(str "cmd")` </a>

#### KSR.exec.exec_msg() ####

<a target='_blank' href='/docs/modules/devel/modules/exec.html#exec.f.exec_msg'> `int exec_msg(str "cmd")` </a>

## geoip ##

#### KSR.geoip.match() ####

<a target='_blank' href='/docs/modules/devel/modules/geoip.html#geoip.f.match'> `int match(str "tomatch", str "pvclass")` </a>

## geoip2 ##

#### KSR.geoip2.match() ####

<a target='_blank' href='/docs/modules/devel/modules/geoip2.html#geoip2.f.match'> `int match(str "tomatch", str "pvclass")` </a>

## group ##

#### KSR.group.is_user_in() ####

<a target='_blank' href='/docs/modules/devel/modules/group.html#group.f.is_user_in'> `int is_user_in(str "uri", str "grp")` </a>

## htable ##

#### KSR.htable.sht_get() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_get'> `xval sht_get(str "htname", str "itname")` </a>

#### KSR.htable.sht_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_gete'> `xval sht_gete(str "htname", str "itname")` </a>

#### KSR.htable.sht_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_getw'> `xval sht_getw(str "htname", str "itname")` </a>

#### KSR.htable.sht_has_name() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_has_name'> `int sht_has_name(str "sname", str "sop", str "sval")` </a>

#### KSR.htable.sht_has_str_value() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_has_str_value'> `int sht_has_str_value(str "sname", str "sop", str "sval")` </a>

#### KSR.htable.sht_iterator_end() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_end'> `int sht_iterator_end(str "iname")` </a>

#### KSR.htable.sht_iterator_next() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_next'> `int sht_iterator_next(str "iname")` </a>

#### KSR.htable.sht_iterator_start() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_iterator_start'> `int sht_iterator_start(str "iname", str "hname")` </a>

#### KSR.htable.sht_lock() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_lock'> `int sht_lock(str "htname", str "skey")` </a>

#### KSR.htable.sht_reset() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_reset'> `int sht_reset(str "hname")` </a>

#### KSR.htable.sht_rm() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_rm'> `int sht_rm(str "hname", str "iname")` </a>

#### KSR.htable.sht_rm_name() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name'> `int sht_rm_name(str "sname", str "sop", str "sval")` </a>

#### KSR.htable.sht_rm_name_re() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_rm_name_re'> `int sht_rm_name_re(str "htname", str "rexp")` </a>

#### KSR.htable.sht_rm_value() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value'> `int sht_rm_value(str "sname", str "sop", str "sval")` </a>

#### KSR.htable.sht_rm_value_re() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_rm_value_re'> `int sht_rm_value_re(str "htname", str "rexp")` </a>

#### KSR.htable.sht_setex() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_setex'> `int sht_setex(str "htname", str "itname", int itval)` </a>

#### KSR.htable.sht_seti() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_seti'> `int sht_seti(str "htname", str "itname", int itval)` </a>

#### KSR.htable.sht_sets() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_sets'> `int sht_sets(str "htname", str "itname", str "itval")` </a>

#### KSR.htable.sht_setxi() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_setxi'> `int sht_setxi(str "htname", str "itname", int itval, int exval)` </a>

#### KSR.htable.sht_setxs() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_setxs'> `int sht_setxs(str "htname", str "itname", str "itval", int exval)` </a>

#### KSR.htable.sht_unlock() ####

<a target='_blank' href='/docs/modules/devel/modules/htable.html#htable.f.sht_unlock'> `int sht_unlock(str "htname", str "skey")` </a>

## http_async_client ##

#### KSR.http_async_client.query() ####

<a target='_blank' href='/docs/modules/devel/modules/http_async_client.html#http_async_client.f.query'> `int query(str "sdata", str "rn")` </a>

## http_client ##

#### KSR.http_client.curl_connect() ####

<a target='_blank' href='/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect'> `int curl_connect(str "con", str "url", str "dpv")` </a>

#### KSR.http_client.curl_connect_post() ####

<a target='_blank' href='/docs/modules/devel/modules/http_client.html#http_client.f.curl_connect_post'> `int curl_connect_post(str "con", str "url", str "ctype", str "data", str "dpv")` </a>

#### KSR.http_client.query() ####

<a target='_blank' href='/docs/modules/devel/modules/http_client.html#http_client.f.query'> `int query(str "url", str "dpv")` </a>

#### KSR.http_client.query_post() ####

<a target='_blank' href='/docs/modules/devel/modules/http_client.html#http_client.f.query_post'> `int query_post(str "url", str "post", str "dpv")` </a>

#### KSR.http_client.query_post_hdrs() ####

<a target='_blank' href='/docs/modules/devel/modules/http_client.html#http_client.f.query_post_hdrs'> `int query_post_hdrs(str "url", str "post", str "hdrs", str "dpv")` </a>

## imc ##

#### KSR.imc.imc_manager() ####

<a target='_blank' href='/docs/modules/devel/modules/imc.html#imc.f.imc_manager'> `int imc_manager()` </a>

## ipops ##

#### KSR.ipops.compare_ips() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.compare_ips'> `int compare_ips(str "_sval1", str "_sval2")` </a>

#### KSR.ipops.compare_pure_ips() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.compare_pure_ips'> `int compare_pure_ips(str "_sval1", str "_sval2")` </a>

#### KSR.ipops.detailed_ip_type() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ip_type'> `int detailed_ip_type(str "_sval", str "_dpv")` </a>

#### KSR.ipops.detailed_ipv4_type() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv4_type'> `int detailed_ipv4_type(str "_sval", str "_dpv")` </a>

#### KSR.ipops.detailed_ipv6_type() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.detailed_ipv6_type'> `int detailed_ipv6_type(str "_sval", str "_dpv")` </a>

#### KSR.ipops.dns_int_match_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.dns_int_match_ip'> `int dns_int_match_ip(str "vhn", str "vip")` </a>

#### KSR.ipops.dns_query() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.dns_query'> `int dns_query(str "naptrname", str "pvid")` </a>

#### KSR.ipops.dns_sys_match_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.dns_sys_match_ip'> `int dns_sys_match_ip(str "vhn", str "vip")` </a>

#### KSR.ipops.ip_is_in_subnet() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.ip_is_in_subnet'> `int ip_is_in_subnet(str "_sval1", str "_sval2")` </a>

#### KSR.ipops.ip_type() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.ip_type'> `int ip_type(str "sval")` </a>

#### KSR.ipops.is_in_subnet() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_in_subnet'> `int is_in_subnet(str "_sval1", str "_sval2")` </a>

#### KSR.ipops.is_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_ip'> `int is_ip(str "sval")` </a>

#### KSR.ipops.is_ip4() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_ip4'> `int is_ip4(str "sval")` </a>

#### KSR.ipops.is_ip6() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6'> `int is_ip6(str "sval")` </a>

#### KSR.ipops.is_ip6_reference() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_ip6_reference'> `int is_ip6_reference(str "sval")` </a>

#### KSR.ipops.is_ip_rfc1918() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_ip_rfc1918'> `int is_ip_rfc1918(str "sval")` </a>

#### KSR.ipops.is_pure_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.is_pure_ip'> `int is_pure_ip(str "sval")` </a>

#### KSR.ipops.naptr_query() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.naptr_query'> `int naptr_query(str "naptrname", str "pvid")` </a>

#### KSR.ipops.srv_query() ####

<a target='_blank' href='/docs/modules/devel/modules/ipops.html#ipops.f.srv_query'> `int srv_query(str "naptrname", str "pvid")` </a>

## jansson ##

#### KSR.jansson.get() ####

<a target='_blank' href='/docs/modules/devel/modules/jansson.html#jansson.f.get'> `int get(str "spath", str "sdoc", str "spv")` </a>

## jsonrpcs ##

#### KSR.jsonrpcs.exec() ####

<a target='_blank' href='/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.exec'> `int exec(str "scmd")` </a>

#### KSR.jsonrpcs.execx() ####

<a target='_blank' href='/docs/modules/devel/modules/jsonrpcs.html#jsonrpcs.f.execx'> `int execx(str "scmd")` </a>

## keepalive ##

#### KSR.keepalive.is_alive() ####

<a target='_blank' href='/docs/modules/devel/modules/keepalive.html#keepalive.f.is_alive'> `int is_alive(str "dest")` </a>

## kex ##

#### KSR.kex.resetdebug() ####

<a target='_blank' href='/docs/modules/devel/modules/kex.html#kex.f.resetdebug'> `int resetdebug()` </a>

#### KSR.kex.setdebug() ####

<a target='_blank' href='/docs/modules/devel/modules/kex.html#kex.f.setdebug'> `int setdebug(int lval)` </a>

## kx ##

#### KSR.kx.get_fhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_fhost'> `xval get_fhost()` </a>

#### KSR.kx.get_furi() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_furi'> `xval get_furi()` </a>

#### KSR.kx.get_fuser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_fuser'> `xval get_fuser()` </a>

#### KSR.kx.get_ouri() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_ouri'> `xval get_ouri()` </a>

#### KSR.kx.get_proto() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_proto'> `xval get_proto()` </a>

#### KSR.kx.get_protoid() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_protoid'> `int get_protoid()` </a>

#### KSR.kx.get_rcvip() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_rcvip'> `xval get_rcvip()` </a>

#### KSR.kx.get_rcvport() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_rcvport'> `xval get_rcvport()` </a>

#### KSR.kx.get_rhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_rhost'> `xval get_rhost()` </a>

#### KSR.kx.get_ruri() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_ruri'> `xval get_ruri()` </a>

#### KSR.kx.get_ruser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_ruser'> `xval get_ruser()` </a>

#### KSR.kx.get_srcip() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_srcip'> `xval get_srcip()` </a>

#### KSR.kx.get_srcport() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_srcport'> `xval get_srcport()` </a>

#### KSR.kx.get_turi() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_turi'> `xval get_turi()` </a>

#### KSR.kx.get_ua() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.get_ua'> `xval get_ua()` </a>

#### KSR.kx.gete_fhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.gete_fhost'> `xval gete_fhost()` </a>

#### KSR.kx.gete_fuser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.gete_fuser'> `xval gete_fuser()` </a>

#### KSR.kx.gete_rhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.gete_rhost'> `xval gete_rhost()` </a>

#### KSR.kx.gete_ruser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.gete_ruser'> `xval gete_ruser()` </a>

#### KSR.kx.gete_ua() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.gete_ua'> `xval gete_ua()` </a>

#### KSR.kx.getw_fhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.getw_fhost'> `xval getw_fhost()` </a>

#### KSR.kx.getw_fuser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.getw_fuser'> `xval getw_fuser()` </a>

#### KSR.kx.getw_rhost() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.getw_rhost'> `xval getw_rhost()` </a>

#### KSR.kx.getw_ruser() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.getw_ruser'> `xval getw_ruser()` </a>

#### KSR.kx.getw_ua() ####

<a target='_blank' href='/docs/modules/devel/modules/kx.html#kx.f.getw_ua'> `xval getw_ua()` </a>

## lcr ##

#### KSR.lcr.defunct_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.defunct_gw'> `int defunct_gw(int defunct_period)` </a>

#### KSR.lcr.from_any_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw'> `int from_any_gw()` </a>

#### KSR.lcr.from_any_gw_addr() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.from_any_gw_addr'> `int from_any_gw_addr(str "addr_str", int transport)` </a>

#### KSR.lcr.from_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.from_gw'> `int from_gw(int lcr_id)` </a>

#### KSR.lcr.from_gw_addr() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.from_gw_addr'> `int from_gw_addr(int lcr_id, str "addr_str", int transport)` </a>

#### KSR.lcr.inactivate_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.inactivate_gw'> `int inactivate_gw()` </a>

#### KSR.lcr.load_gws() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.load_gws'> `int load_gws(int lcr_id)` </a>

#### KSR.lcr.load_gws_furi() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_furi'> `int load_gws_furi(int lcr_id, str "ruri_user", str "from_uri")` </a>

#### KSR.lcr.load_gws_ruser() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.load_gws_ruser'> `int load_gws_ruser(int lcr_id, str "ruri_user")` </a>

#### KSR.lcr.next_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.next_gw'> `int next_gw()` </a>

#### KSR.lcr.to_any_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw'> `int to_any_gw()` </a>

#### KSR.lcr.to_any_gw_addr() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.to_any_gw_addr'> `int to_any_gw_addr(str "addr_str", int transport)` </a>

#### KSR.lcr.to_gw() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.to_gw'> `int to_gw(int lcr_id)` </a>

#### KSR.lcr.to_gw_addr() ####

<a target='_blank' href='/docs/modules/devel/modules/lcr.html#lcr.f.to_gw_addr'> `int to_gw_addr(int lcr_id, str "addr_str", int transport)` </a>

## log_custom ##

#### KSR.log_custom.log_udp() ####

<a target='_blank' href='/docs/modules/devel/modules/log_custom.html#log_custom.f.log_udp'> `int log_udp(str "txt")` </a>

## log_systemd ##

#### KSR.log_systemd.sd_journal_print() ####

<a target='_blank' href='/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_print'> `int sd_journal_print(str "slev", str "stxt")` </a>

#### KSR.log_systemd.sd_journal_send_xvap() ####

<a target='_blank' href='/docs/modules/devel/modules/log_systemd.html#log_systemd.f.sd_journal_send_xvap'> `int sd_journal_send_xvap(str "xname")` </a>

## maxfwd ##

#### KSR.maxfwd.is_maxfwd_lt() ####

<a target='_blank' href='/docs/modules/devel/modules/maxfwd.html#maxfwd.f.is_maxfwd_lt'> `int is_maxfwd_lt(int limit)` </a>

#### KSR.maxfwd.process_maxfwd() ####

<a target='_blank' href='/docs/modules/devel/modules/maxfwd.html#maxfwd.f.process_maxfwd'> `int process_maxfwd(int limit)` </a>

## mediaproxy ##

#### KSR.mediaproxy.end_media_session() ####

<a target='_blank' href='/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.end_media_session'> `int end_media_session()` </a>

#### KSR.mediaproxy.engage_media_proxy() ####

<a target='_blank' href='/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.engage_media_proxy'> `int engage_media_proxy()` </a>

#### KSR.mediaproxy.use_media_proxy() ####

<a target='_blank' href='/docs/modules/devel/modules/mediaproxy.html#mediaproxy.f.use_media_proxy'> `int use_media_proxy()` </a>

## misc_radius ##

#### KSR.misc_radius.does_uri_exist() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist'> `int does_uri_exist()` </a>

#### KSR.misc_radius.does_uri_exist_uval() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_exist_uval'> `int does_uri_exist_uval(str "suri")` </a>

#### KSR.misc_radius.does_uri_user_exist() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist'> `int does_uri_user_exist()` </a>

#### KSR.misc_radius.does_uri_user_exist_uval() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.does_uri_user_exist_uval'> `int does_uri_user_exist_uval(str "user")` </a>

#### KSR.misc_radius.is_user_in() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.is_user_in'> `int is_user_in(str "user", str "group")` </a>

#### KSR.misc_radius.load_callee_avps() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_callee_avps'> `int load_callee_avps(str "user")` </a>

#### KSR.misc_radius.load_caller_avps() ####

<a target='_blank' href='/docs/modules/devel/modules/misc_radius.html#misc_radius.f.load_caller_avps'> `int load_caller_avps(str "user")` </a>

## mqueue ##

#### KSR.mqueue.mq_add() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_add'> `int mq_add(str "mq", str "key", str "val")` </a>

#### KSR.mqueue.mq_fetch() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_fetch'> `int mq_fetch(str "mq")` </a>

#### KSR.mqueue.mq_pv_free() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_pv_free'> `int mq_pv_free(str "mq")` </a>

#### KSR.mqueue.mq_size() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mq_size'> `int mq_size(str "mq")` </a>

#### KSR.mqueue.mqk_get() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_get'> `xval mqk_get(str "qname")` </a>

#### KSR.mqueue.mqk_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_gete'> `xval mqk_gete(str "qname")` </a>

#### KSR.mqueue.mqk_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqk_getw'> `xval mqk_getw(str "qname")` </a>

#### KSR.mqueue.mqv_get() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_get'> `xval mqv_get(str "qname")` </a>

#### KSR.mqueue.mqv_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_gete'> `xval mqv_gete(str "qname")` </a>

#### KSR.mqueue.mqv_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/mqueue.html#mqueue.f.mqv_getw'> `xval mqv_getw(str "qname")` </a>

## msilo ##

#### KSR.msilo.mdump() ####

<a target='_blank' href='/docs/modules/devel/modules/msilo.html#msilo.f.mdump'> `int mdump()` </a>

#### KSR.msilo.mdump_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/msilo.html#msilo.f.mdump_uri'> `int mdump_uri(str "owner_s")` </a>

#### KSR.msilo.mstore() ####

<a target='_blank' href='/docs/modules/devel/modules/msilo.html#msilo.f.mstore'> `int mstore()` </a>

#### KSR.msilo.mstore_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/msilo.html#msilo.f.mstore_uri'> `int mstore_uri(str "owner_s")` </a>

## msrp ##

#### KSR.msrp.cmap_lookup() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.cmap_lookup'> `int cmap_lookup()` </a>

#### KSR.msrp.cmap_save() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.cmap_save'> `int cmap_save()` </a>

#### KSR.msrp.is_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.is_reply'> `int is_reply()` </a>

#### KSR.msrp.is_request() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.is_request'> `int is_request()` </a>

#### KSR.msrp.relay() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.relay'> `int relay()` </a>

#### KSR.msrp.relay_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.relay_flags'> `int relay_flags(int rtflags)` </a>

#### KSR.msrp.reply() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.reply'> `int reply(str "rcode", str "rtext", str "rhdrs")` </a>

#### KSR.msrp.reply_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.reply_flags'> `int reply_flags(int rtflags)` </a>

#### KSR.msrp.set_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/msrp.html#msrp.f.set_dst'> `int set_dst(str "rtaddr", str "rfsock")` </a>

## mtree ##

#### KSR.mtree.mt_match() ####

<a target='_blank' href='/docs/modules/devel/modules/mtree.html#mtree.f.mt_match'> `int mt_match(str "tname", str "tomatch", int mval)` </a>

## nat_traversal ##

#### KSR.nat_traversal.client_nat_test() ####

<a target='_blank' href='/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.client_nat_test'> `int client_nat_test(int tests)` </a>

#### KSR.nat_traversal.fix_contact() ####

<a target='_blank' href='/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.fix_contact'> `int fix_contact()` </a>

#### KSR.nat_traversal.nat_keepalive() ####

<a target='_blank' href='/docs/modules/devel/modules/nat_traversal.html#nat_traversal.f.nat_keepalive'> `int nat_keepalive()` </a>

## nathelper ##

#### KSR.nathelper.add_contact_alias() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias'> `int add_contact_alias()` </a>

#### KSR.nathelper.add_contact_alias_addr() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.add_contact_alias_addr'> `int add_contact_alias_addr(str "ip_str", str "port_str", str "proto_str")` </a>

#### KSR.nathelper.add_rcv_param() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.add_rcv_param'> `int add_rcv_param(int upos)` </a>

#### KSR.nathelper.fix_nated_contact() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_contact'> `int fix_nated_contact()` </a>

#### KSR.nathelper.fix_nated_register() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_register'> `int fix_nated_register()` </a>

#### KSR.nathelper.fix_nated_sdp() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp'> `int fix_nated_sdp(int level)` </a>

#### KSR.nathelper.fix_nated_sdp_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.fix_nated_sdp_ip'> `int fix_nated_sdp_ip(int level, str "ip")` </a>

#### KSR.nathelper.handle_ruri_alias() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.handle_ruri_alias'> `int handle_ruri_alias()` </a>

#### KSR.nathelper.is_rfc1918() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.is_rfc1918'> `int is_rfc1918(str "address")` </a>

#### KSR.nathelper.nat_uac_test() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.nat_uac_test'> `int nat_uac_test(int tests)` </a>

#### KSR.nathelper.set_contact_alias() ####

<a target='_blank' href='/docs/modules/devel/modules/nathelper.html#nathelper.f.set_contact_alias'> `int set_contact_alias()` </a>

## ndb_mongodb ##

#### KSR.ndb_mongodb.exec() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec'> `int exec(str "ssrv", str "sdname", str "scname", str "scmd", str "sres")` </a>

#### KSR.ndb_mongodb.exec_simple() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.exec_simple'> `int exec_simple(str "ssrv", str "sdname", str "scname", str "scmd", str "sres")` </a>

#### KSR.ndb_mongodb.execx() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.execx'> `int execx(str "ssrv", str "sdname", str "scname", str "scmd", str "sres")` </a>

#### KSR.ndb_mongodb.find() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find'> `int find(str "ssrv", str "sdname", str "scname", str "scmd", str "sres")` </a>

#### KSR.ndb_mongodb.find_one() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.find_one'> `int find_one(str "ssrv", str "sdname", str "scname", str "scmd", str "sres")` </a>

#### KSR.ndb_mongodb.free_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.free_reply'> `int free_reply(str "name")` </a>

#### KSR.ndb_mongodb.next_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_mongodb.html#ndb_mongodb.f.next_reply'> `int next_reply(str "name")` </a>

## ndb_redis ##

#### KSR.ndb_redis.redis_cmd() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd'> `int redis_cmd(str "srv", str "rcmd", str "sres")` </a>

#### KSR.ndb_redis.redis_cmd_p1() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p1'> `int redis_cmd_p1(str "srv", str "rcmd", str "p1", str "sres")` </a>

#### KSR.ndb_redis.redis_cmd_p2() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p2'> `int redis_cmd_p2(str "srv", str "rcmd", str "p1", str "p2", str "sres")` </a>

#### KSR.ndb_redis.redis_cmd_p3() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_cmd_p3'> `int redis_cmd_p3(str "srv", str "rcmd", str "p1", str "p2", str "p3", str "sres")` </a>

#### KSR.ndb_redis.redis_free() ####

<a target='_blank' href='/docs/modules/devel/modules/ndb_redis.html#ndb_redis.f.redis_free'> `int redis_free(str "name")` </a>

## path ##

#### KSR.path.add_path() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path'> `int add_path()` </a>

#### KSR.path.add_path_received() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path_received'> `int add_path_received()` </a>

#### KSR.path.add_path_received_user() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path_received_user'> `int add_path_received_user(str "_user")` </a>

#### KSR.path.add_path_received_user_params() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path_received_user_params'> `int add_path_received_user_params(str "_user", str "_params")` </a>

#### KSR.path.add_path_user() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path_user'> `int add_path_user(str "_user")` </a>

#### KSR.path.add_path_user_params() ####

<a target='_blank' href='/docs/modules/devel/modules/path.html#path.f.add_path_user_params'> `int add_path_user_params(str "_user", str "_params")` </a>

## pdt ##

#### KSR.pdt.pd_translate() ####

<a target='_blank' href='/docs/modules/devel/modules/pdt.html#pdt.f.pd_translate'> `int pd_translate(str "sd", int md)` </a>

#### KSR.pdt.pprefix2domain() ####

<a target='_blank' href='/docs/modules/devel/modules/pdt.html#pdt.f.pprefix2domain'> `int pprefix2domain(int m, int s)` </a>

## permissions ##

#### KSR.permissions.allow_address() ####

<a target='_blank' href='/docs/modules/devel/modules/permissions.html#permissions.f.allow_address'> `int allow_address(int addr_group, str "ips", int port)` </a>

#### KSR.permissions.allow_address_group() ####

<a target='_blank' href='/docs/modules/devel/modules/permissions.html#permissions.f.allow_address_group'> `int allow_address_group(str "_addr", int _port)` </a>

#### KSR.permissions.allow_source_address() ####

<a target='_blank' href='/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address'> `int allow_source_address(int addr_group)` </a>

#### KSR.permissions.allow_source_address_group() ####

<a target='_blank' href='/docs/modules/devel/modules/permissions.html#permissions.f.allow_source_address_group'> `int allow_source_address_group()` </a>

## phonenum ##

#### KSR.phonenum.match() ####

<a target='_blank' href='/docs/modules/devel/modules/phonenum.html#phonenum.f.match'> `int match(str "tomatch", str "pvclass")` </a>

## pike ##

#### KSR.pike.pike_check_req() ####

<a target='_blank' href='/docs/modules/devel/modules/pike.html#pike.f.pike_check_req'> `int pike_check_req()` </a>

## pipelimit ##

#### KSR.pipelimit.pl_check() ####

<a target='_blank' href='/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check'> `int pl_check(str "pipeid")` </a>

#### KSR.pipelimit.pl_check_limit() ####

<a target='_blank' href='/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_check_limit'> `int pl_check_limit(str "pipeid", str "alg", int limit)` </a>

#### KSR.pipelimit.pl_drop() ####

<a target='_blank' href='/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop'> `int pl_drop()` </a>

#### KSR.pipelimit.pl_drop_range() ####

<a target='_blank' href='/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_range'> `int pl_drop_range(int rmin, int rmax)` </a>

#### KSR.pipelimit.pl_drop_retry() ####

<a target='_blank' href='/docs/modules/devel/modules/pipelimit.html#pipelimit.f.pl_drop_retry'> `int pl_drop_retry(int rafter)` </a>

## prefix_route ##

#### KSR.prefix_route.prefix_route() ####

<a target='_blank' href='/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route'> `int prefix_route(str "ruser")` </a>

#### KSR.prefix_route.prefix_route_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/prefix_route.html#prefix_route.f.prefix_route_uri'> `int prefix_route_uri()` </a>

## presence ##

#### KSR.presence.handle_publish() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.handle_publish'> `int handle_publish()` </a>

#### KSR.presence.handle_publish_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.handle_publish_uri'> `int handle_publish_uri(str "sender_uri")` </a>

#### KSR.presence.handle_subscribe() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe'> `int handle_subscribe()` </a>

#### KSR.presence.handle_subscribe_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.handle_subscribe_uri'> `int handle_subscribe_uri(str "wuri")` </a>

#### KSR.presence.pres_auth_status() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.pres_auth_status'> `int pres_auth_status(str "watcher_uri", str "presentity_uri")` </a>

#### KSR.presence.pres_has_subscribers() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.pres_has_subscribers'> `int pres_has_subscribers(str "pres_uri", str "wevent")` </a>

#### KSR.presence.pres_refresh_watchers() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers'> `int pres_refresh_watchers(str "pres", str "event", int type)` </a>

#### KSR.presence.pres_refresh_watchers_file() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.pres_refresh_watchers_file'> `int pres_refresh_watchers_file(str "pres", str "event", int type, str "file_uri", str "filename")` </a>

#### KSR.presence.pres_update_watchers() ####

<a target='_blank' href='/docs/modules/devel/modules/presence.html#presence.f.pres_update_watchers'> `int pres_update_watchers(str "pres_uri", str "event")` </a>

## presence_xml ##

#### KSR.presence_xml.pres_check_activities() ####

<a target='_blank' href='/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_activities'> `int pres_check_activities(str "pres_uri", str "activity")` </a>

#### KSR.presence_xml.pres_check_basic() ####

<a target='_blank' href='/docs/modules/devel/modules/presence_xml.html#presence_xml.f.pres_check_basic'> `int pres_check_basic(str "pres_uri", str "status")` </a>

## pua ##

#### KSR.pua.pua_set_publish() ####

<a target='_blank' href='/docs/modules/devel/modules/pua.html#pua.f.pua_set_publish'> `int pua_set_publish()` </a>

#### KSR.pua.pua_update_contact() ####

<a target='_blank' href='/docs/modules/devel/modules/pua.html#pua.f.pua_update_contact'> `int pua_update_contact()` </a>

## pvx ##

#### KSR.pvx.avp_get() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_get'> `xval avp_get(str "xname")` </a>

#### KSR.pvx.avp_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_gete'> `xval avp_gete(str "xname")` </a>

#### KSR.pvx.avp_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_getw'> `xval avp_getw(str "xname")` </a>

#### KSR.pvx.avp_is_null() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_is_null'> `int avp_is_null(str "xname")` </a>

#### KSR.pvx.avp_rm() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_rm'> `int avp_rm(str "xname")` </a>

#### KSR.pvx.avp_seti() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_seti'> `int avp_seti(str "xname", int vn)` </a>

#### KSR.pvx.avp_sets() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.avp_sets'> `int avp_sets(str "xname", str "vs")` </a>

#### KSR.pvx.evalx() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.evalx'> `int evalx(str "dst", str "fmt")` </a>

#### KSR.pvx.pv_var_to_xavp() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.pv_var_to_xavp'> `int pv_var_to_xavp(str "varname", str "xname")` </a>

#### KSR.pvx.pv_xavp_print() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavp_print'> `int pv_xavp_print()` </a>

#### KSR.pvx.pv_xavp_to_var() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.pv_xavp_to_var'> `int pv_xavp_to_var(str "xname")` </a>

#### KSR.pvx.sbranch_append() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_append'> `int sbranch_append()` </a>

#### KSR.pvx.sbranch_reset() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_reset'> `int sbranch_reset()` </a>

#### KSR.pvx.sbranch_set_ruri() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.sbranch_set_ruri'> `int sbranch_set_ruri()` </a>

#### KSR.pvx.xavp_child_get() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_get'> `xval xavp_child_get(str "rname", str "cname")` </a>

#### KSR.pvx.xavp_child_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_gete'> `xval xavp_child_gete(str "rname", str "cname")` </a>

#### KSR.pvx.xavp_child_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_getw'> `xval xavp_child_getw(str "rname", str "cname")` </a>

#### KSR.pvx.xavp_child_is_null() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_is_null'> `int xavp_child_is_null(str "rname", str "cname")` </a>

#### KSR.pvx.xavp_child_rm() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_rm'> `int xavp_child_rm(str "rname", str "cname")` </a>

#### KSR.pvx.xavp_child_seti() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_seti'> `int xavp_child_seti(str "rname", str "cname", int ival)` </a>

#### KSR.pvx.xavp_child_sets() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_child_sets'> `int xavp_child_sets(str "rname", str "cname", str "sval")` </a>

#### KSR.pvx.xavp_get() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_get'> `xval xavp_get(str "rname")` </a>

#### KSR.pvx.xavp_gete() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_gete'> `xval xavp_gete(str "rname")` </a>

#### KSR.pvx.xavp_getw() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_getw'> `xval xavp_getw(str "rname")` </a>

#### KSR.pvx.xavp_is_null() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_is_null'> `int xavp_is_null(str "rname")` </a>

#### KSR.pvx.xavp_params_explode() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_params_explode'> `int xavp_params_explode(str "sparams", str "sxname")` </a>

#### KSR.pvx.xavp_params_implode() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_params_implode'> `int xavp_params_implode(str "sxname", str "svname")` </a>

#### KSR.pvx.xavp_rm() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_rm'> `int xavp_rm(str "rname")` </a>

#### KSR.pvx.xavp_seti() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_seti'> `int xavp_seti(str "rname", int ival)` </a>

#### KSR.pvx.xavp_sets() ####

<a target='_blank' href='/docs/modules/devel/modules/pvx.html#pvx.f.xavp_sets'> `int xavp_sets(str "rname", str "sval")` </a>

## rabbitmq ##

#### KSR.rabbitmq.publish() ####

<a target='_blank' href='/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish'> `int publish(str "exchange", str "routingkey", str "contenttype", str "messagebody")` </a>

#### KSR.rabbitmq.publish_consume() ####

<a target='_blank' href='/docs/modules/devel/modules/rabbitmq.html#rabbitmq.f.publish_consume'> `int publish_consume(str "exchange", str "routingkey", str "contenttype", str "messagebody", str "dpv")` </a>

## regex ##

#### KSR.regex.pcre_match() ####

<a target='_blank' href='/docs/modules/devel/modules/regex.html#regex.f.pcre_match'> `int pcre_match(str "string", str "regex")` </a>

#### KSR.regex.pcre_match_group() ####

<a target='_blank' href='/docs/modules/devel/modules/regex.html#regex.f.pcre_match_group'> `int pcre_match_group(str "string", int num_pcre)` </a>

## registrar ##

#### KSR.registrar.add_sock_hdr() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.add_sock_hdr'> `int add_sock_hdr(str "hdr_name")` </a>

#### KSR.registrar.lookup() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.lookup'> `int lookup(str "table")` </a>

#### KSR.registrar.lookup_branches() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.lookup_branches'> `int lookup_branches(str "_dtable")` </a>

#### KSR.registrar.lookup_to_dset() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.lookup_to_dset'> `int lookup_to_dset(str "table", str "uri")` </a>

#### KSR.registrar.lookup_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.lookup_uri'> `int lookup_uri(str "table", str "uri")` </a>

#### KSR.registrar.reg_fetch_contacts() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.reg_fetch_contacts'> `int reg_fetch_contacts(str "dtable", str "uri", str "profile")` </a>

#### KSR.registrar.reg_free_contacts() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.reg_free_contacts'> `int reg_free_contacts(str "profile")` </a>

#### KSR.registrar.registered() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.registered'> `int registered(str "table")` </a>

#### KSR.registrar.registered_action() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.registered_action'> `int registered_action(str "_dtable", str "_uri", int _f, int _aflags)` </a>

#### KSR.registrar.registered_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.registered_flags'> `int registered_flags(str "_dtable", str "_uri", int _f)` </a>

#### KSR.registrar.registered_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.registered_uri'> `int registered_uri(str "_dtable", str "_uri")` </a>

#### KSR.registrar.save() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.save'> `int save(str "table", int flags)` </a>

#### KSR.registrar.save_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.save_uri'> `int save_uri(str "table", int flags, str "uri")` </a>

#### KSR.registrar.set_q_override() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.set_q_override'> `int set_q_override(str "new_q")` </a>

#### KSR.registrar.unregister() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.unregister'> `int unregister(str "_dtable", str "_uri")` </a>

#### KSR.registrar.unregister_ruid() ####

<a target='_blank' href='/docs/modules/devel/modules/registrar.html#registrar.f.unregister_ruid'> `int unregister_ruid(str "_dtable", str "_uri", str "_ruid")` </a>

## rls ##

#### KSR.rls.handle_notify() ####

<a target='_blank' href='/docs/modules/devel/modules/rls.html#rls.f.handle_notify'> `int handle_notify()` </a>

#### KSR.rls.handle_subscribe() ####

<a target='_blank' href='/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe'> `int handle_subscribe()` </a>

#### KSR.rls.handle_subscribe_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/rls.html#rls.f.handle_subscribe_uri'> `int handle_subscribe_uri(str "wuri")` </a>

#### KSR.rls.update_subs() ####

<a target='_blank' href='/docs/modules/devel/modules/rls.html#rls.f.update_subs'> `int update_subs(str "uri", str "event")` </a>

## rr ##

#### KSR.rr.add_rr_param() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.add_rr_param'> `int add_rr_param(str "sparam")` </a>

#### KSR.rr.check_route_param() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.check_route_param'> `int check_route_param(str "sre")` </a>

#### KSR.rr.is_direction() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.is_direction'> `int is_direction(str "dir")` </a>

#### KSR.rr.loose_route() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.loose_route'> `int loose_route()` </a>

#### KSR.rr.record_route() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.record_route'> `int record_route()` </a>

#### KSR.rr.record_route_params() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.record_route_params'> `int record_route_params(str "params")` </a>

#### KSR.rr.remove_record_route() ####

<a target='_blank' href='/docs/modules/devel/modules/rr.html#rr.f.remove_record_route'> `int remove_record_route()` </a>

## rtjson ##

#### KSR.rtjson.init_routes() ####

<a target='_blank' href='/docs/modules/devel/modules/rtjson.html#rtjson.f.init_routes'> `int init_routes(str "srdoc")` </a>

#### KSR.rtjson.next_route() ####

<a target='_blank' href='/docs/modules/devel/modules/rtjson.html#rtjson.f.next_route'> `int next_route()` </a>

#### KSR.rtjson.push_routes() ####

<a target='_blank' href='/docs/modules/devel/modules/rtjson.html#rtjson.f.push_routes'> `int push_routes()` </a>

#### KSR.rtjson.update_branch() ####

<a target='_blank' href='/docs/modules/devel/modules/rtjson.html#rtjson.f.update_branch'> `int update_branch()` </a>

## rtpengine ##

This module enables media streams to be proxied via an RTPproxy.

#### KSR.rtpengine.rtpengine_answer() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer'> `int rtpengine_answer(str "flags")` </a>

#### KSR.rtpengine.rtpengine_answer0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_answer0'> `int rtpengine_answer0()` </a>

#### KSR.rtpengine.rtpengine_delete() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete'> `int rtpengine_delete(str "flags")` </a>

#### KSR.rtpengine.rtpengine_delete0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_delete0'> `int rtpengine_delete0()` </a>

#### KSR.rtpengine.rtpengine_manage() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage'> `int rtpengine_manage(str "flags")` </a>

#### KSR.rtpengine.rtpengine_manage0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_manage0'> `int rtpengine_manage0()` </a>

#### KSR.rtpengine.rtpengine_offer() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer'> `int rtpengine_offer(str "flags")` </a>

#### KSR.rtpengine.rtpengine_offer0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_offer0'> `int rtpengine_offer0()` </a>

#### KSR.rtpengine.rtpengine_query() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query'> `int rtpengine_query(str "flags")` </a>

#### KSR.rtpengine.rtpengine_query0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.rtpengine_query0'> `int rtpengine_query0()` </a>

#### KSR.rtpengine.set_rtpengine_set() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set'> `int set_rtpengine_set(int r1)` </a>

#### KSR.rtpengine.set_rtpengine_set2() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.set_rtpengine_set2'> `int set_rtpengine_set2(int r1, int r2)` </a>

This function is the sibling function to [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set). The original module function is declared as
`set_rtpengine_set(setid[, setid2])`.

In KEMI set_rtpengine_set() takes only the first parameter and set_rtpengine_set2() allows for the second optional parameter to be passed.

```
KSR.rtpengine.set_rtpengine_set2(2, 1);
KSR.rtpengine.rtpengine_offer();
```

Please review the documentation for [set_rtpengine_set()](#ksrrtpengineset_rtpengine_set) for more information.

#### KSR.rtpengine.start_recording() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.start_recording'> `int start_recording()` </a>

#### KSR.rtpengine.stop_recording() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpengine.html#rtpengine.f.stop_recording'> `int stop_recording()` </a>

## rtpproxy ##

#### KSR.rtpproxy.rtpproxy_answer() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer'> `int rtpproxy_answer(str "flags")` </a>

#### KSR.rtpproxy.rtpproxy_answer0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer0'> `int rtpproxy_answer0()` </a>

#### KSR.rtpproxy.rtpproxy_answer_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_answer_ip'> `int rtpproxy_answer_ip(str "flags", str "mip")` </a>

#### KSR.rtpproxy.rtpproxy_destroy() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy'> `int rtpproxy_destroy(str "flags")` </a>

#### KSR.rtpproxy.rtpproxy_destroy0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_destroy0'> `int rtpproxy_destroy0()` </a>

#### KSR.rtpproxy.rtpproxy_manage() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage'> `int rtpproxy_manage(str "flags")` </a>

#### KSR.rtpproxy.rtpproxy_manage0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage0'> `int rtpproxy_manage0()` </a>

#### KSR.rtpproxy.rtpproxy_manage_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_manage_ip'> `int rtpproxy_manage_ip(str "flags", str "mip")` </a>

#### KSR.rtpproxy.rtpproxy_offer() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer'> `int rtpproxy_offer(str "flags")` </a>

#### KSR.rtpproxy.rtpproxy_offer0() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer0'> `int rtpproxy_offer0()` </a>

#### KSR.rtpproxy.rtpproxy_offer_ip() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_offer_ip'> `int rtpproxy_offer_ip(str "flags", str "mip")` </a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uac() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uac'> `int rtpproxy_stop_stream2uac()` </a>

#### KSR.rtpproxy.rtpproxy_stop_stream2uas() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stop_stream2uas'> `int rtpproxy_stop_stream2uas()` </a>

#### KSR.rtpproxy.rtpproxy_stream2uac() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uac'> `int rtpproxy_stream2uac(str "pname", int count)` </a>

#### KSR.rtpproxy.rtpproxy_stream2uas() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.rtpproxy_stream2uas'> `int rtpproxy_stream2uas(str "pname", int count)` </a>

#### KSR.rtpproxy.set_rtpproxy_set() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.set_rtpproxy_set'> `int set_rtpproxy_set(int rset)` </a>

#### KSR.rtpproxy.start_recording() ####

<a target='_blank' href='/docs/modules/devel/modules/rtpproxy.html#rtpproxy.f.start_recording'> `int start_recording()` </a>

## sanity ##

#### KSR.sanity.sanity_check() ####

<a target='_blank' href='/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check'> `int sanity_check(int mflags, int uflags)` </a>

#### KSR.sanity.sanity_check_defaults() ####

<a target='_blank' href='/docs/modules/devel/modules/sanity.html#sanity.f.sanity_check_defaults'> `int sanity_check_defaults()` </a>

#### KSR.sanity.sanity_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/sanity.html#sanity.f.sanity_reply'> `int sanity_reply()` </a>

## sca ##

#### KSR.sca.call_info_update() ####

<a target='_blank' href='/docs/modules/devel/modules/sca.html#sca.f.call_info_update'> `int call_info_update(int update_mask, str "uri_to", str "uri_from")` </a>

#### KSR.sca.call_info_update_default() ####

<a target='_blank' href='/docs/modules/devel/modules/sca.html#sca.f.call_info_update_default'> `int call_info_update_default()` </a>

#### KSR.sca.call_info_update_mask() ####

<a target='_blank' href='/docs/modules/devel/modules/sca.html#sca.f.call_info_update_mask'> `int call_info_update_mask(int umask)` </a>

#### KSR.sca.call_info_update_turi() ####

<a target='_blank' href='/docs/modules/devel/modules/sca.html#sca.f.call_info_update_turi'> `int call_info_update_turi(int umask, str "sto")` </a>

#### KSR.sca.handle_subscribe() ####

<a target='_blank' href='/docs/modules/devel/modules/sca.html#sca.f.handle_subscribe'> `int handle_subscribe()` </a>

## sdpops ##

#### KSR.sdpops.keep_codecs_by_id() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_id'> `int keep_codecs_by_id(str "codecs", str "media")` </a>

#### KSR.sdpops.keep_codecs_by_name() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.keep_codecs_by_name'> `int keep_codecs_by_name(str "codecs", str "media")` </a>

#### KSR.sdpops.remove_codecs_by_id() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_id'> `int remove_codecs_by_id(str "codecs", str "media")` </a>

#### KSR.sdpops.remove_codecs_by_name() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_codecs_by_name'> `int remove_codecs_by_name(str "codecs", str "media")` </a>

#### KSR.sdpops.remove_line_by_prefix() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_line_by_prefix'> `int remove_line_by_prefix(str "prefix", str "media")` </a>

#### KSR.sdpops.remove_media() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.remove_media'> `int remove_media(str "media")` </a>

#### KSR.sdpops.sdp_content() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content'> `int sdp_content()` </a>

#### KSR.sdpops.sdp_content_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_content_flags'> `int sdp_content_flags(int flags)` </a>

#### KSR.sdpops.sdp_get() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get'> `int sdp_get(str "avp")` </a>

#### KSR.sdpops.sdp_get_line_startswith() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_get_line_startswith'> `int sdp_get_line_startswith(str "aname", str "sline")` </a>

#### KSR.sdpops.sdp_print() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_print'> `int sdp_print(int llevel)` </a>

#### KSR.sdpops.sdp_transport() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_transport'> `int sdp_transport(str "avp")` </a>

#### KSR.sdpops.sdp_with_active_media() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_active_media'> `int sdp_with_active_media(str "media")` </a>

#### KSR.sdpops.sdp_with_codecs_by_id() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_id'> `int sdp_with_codecs_by_id(str "codecs")` </a>

#### KSR.sdpops.sdp_with_codecs_by_name() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_codecs_by_name'> `int sdp_with_codecs_by_name(str "codecs")` </a>

#### KSR.sdpops.sdp_with_ice() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_ice'> `int sdp_with_ice()` </a>

#### KSR.sdpops.sdp_with_media() ####

<a target='_blank' href='/docs/modules/devel/modules/sdpops.html#sdpops.f.sdp_with_media'> `int sdp_with_media(str "media")` </a>

## sipcapture ##

#### KSR.sipcapture.float2int() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.float2int'> `int float2int(str "_val", str "_coof")` </a>

#### KSR.sipcapture.report_capture() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture'> `int report_capture(str "_table")` </a>

#### KSR.sipcapture.report_capture_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_cid'> `int report_capture_cid(str "_table", str "_cid")` </a>

#### KSR.sipcapture.report_capture_data() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.report_capture_data'> `int report_capture_data(str "_table", str "_cid", str "_data")` </a>

#### KSR.sipcapture.sip_capture() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture'> `int sip_capture()` </a>

#### KSR.sipcapture.sip_capture_forward() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_forward'> `int sip_capture_forward(str "puri")` </a>

#### KSR.sipcapture.sip_capture_mode() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_mode'> `int sip_capture_mode(str "_table", str "_cmdata")` </a>

#### KSR.sipcapture.sip_capture_table() ####

<a target='_blank' href='/docs/modules/devel/modules/sipcapture.html#sipcapture.f.sip_capture_table'> `int sip_capture_table(str "_table")` </a>

## sipdump ##

#### KSR.sipdump.send() ####

<a target='_blank' href='/docs/modules/devel/modules/sipdump.html#sipdump.f.send'> `int send(str "stag")` </a>

## sipjson ##

#### KSR.sipjson.sj_serialize() ####

<a target='_blank' href='/docs/modules/devel/modules/sipjson.html#sipjson.f.sj_serialize'> `int sj_serialize(str "smode", str "pvn")` </a>

## siptrace ##

#### KSR.siptrace.hlog() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog'> `int hlog(str "message")` </a>

#### KSR.siptrace.hlog_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.hlog_cid'> `int hlog_cid(str "correlationid", str "message")` </a>

#### KSR.siptrace.sip_trace() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace'> `int sip_trace()` </a>

#### KSR.siptrace.sip_trace_dst() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst'> `int sip_trace_dst(str "duri")` </a>

#### KSR.siptrace.sip_trace_dst_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid'> `int sip_trace_dst_cid(str "duri", str "cid")` </a>

#### KSR.siptrace.sip_trace_dst_cid_type() ####

<a target='_blank' href='/docs/modules/devel/modules/siptrace.html#siptrace.f.sip_trace_dst_cid_type'> `int sip_trace_dst_cid_type(str "duri", str "cid", str "sflag")` </a>

## siputils ##

#### KSR.siputils.has_totag() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.has_totag'> `int has_totag()` </a>

#### KSR.siputils.is_alphanum() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanum'> `int is_alphanum(str "tval")` </a>

#### KSR.siputils.is_alphanumex() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_alphanumex'> `int is_alphanumex(str "tval", str "eset")` </a>

#### KSR.siputils.is_first_hop() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_first_hop'> `int is_first_hop()` </a>

#### KSR.siputils.is_numeric() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_numeric'> `int is_numeric(str "tval")` </a>

#### KSR.siputils.is_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_reply'> `int is_reply()` </a>

#### KSR.siputils.is_request() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_request'> `int is_request()` </a>

#### KSR.siputils.is_tel_number() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_tel_number'> `int is_tel_number(str "tval")` </a>

#### KSR.siputils.is_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_uri'> `int is_uri(str "suri")` </a>

#### KSR.siputils.is_user() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.is_user'> `int is_user(str "suser")` </a>

#### KSR.siputils.uri_param() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.uri_param'> `int uri_param(str "sparam")` </a>

#### KSR.siputils.uri_param_value() ####

<a target='_blank' href='/docs/modules/devel/modules/siputils.html#siputils.f.uri_param_value'> `int uri_param_value(str "sparam", str "svalue")` </a>

## sl ##

#### KSR.sl.send_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/sl.html#sl.f.send_reply'> `int send_reply(int code, str "reason")` </a>

#### KSR.sl.sl_forward_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/sl.html#sl.f.sl_forward_reply'> `int sl_forward_reply(str "code", str "reason")` </a>

#### KSR.sl.sl_reply_error() ####

<a target='_blank' href='/docs/modules/devel/modules/sl.html#sl.f.sl_reply_error'> `int sl_reply_error()` </a>

#### KSR.sl.sl_send_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/sl.html#sl.f.sl_send_reply'> `int sl_send_reply(int code, str "reason")` </a>

## speeddial ##

#### KSR.speeddial.lookup() ####

<a target='_blank' href='/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup'> `int lookup(str "stable")` </a>

#### KSR.speeddial.lookup_owner() ####

<a target='_blank' href='/docs/modules/devel/modules/speeddial.html#speeddial.f.lookup_owner'> `int lookup_owner(str "stable", str "sowner")` </a>

## sqlops ##

#### KSR.sqlops.sql_is_null() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_is_null'> `int sql_is_null(str "sres", int i, int j)` </a>

#### KSR.sqlops.sql_num_columns() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_columns'> `int sql_num_columns(str "sres")` </a>

#### KSR.sqlops.sql_num_rows() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_rows'> `int sql_num_rows(str "sres")` </a>

#### KSR.sqlops.sql_query() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query'> `int sql_query(str "scon", str "squery", str "sres")` </a>

#### KSR.sqlops.sql_query_async() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query_async'> `int sql_query_async(str "scon", str "squery")` </a>

#### KSR.sqlops.sql_result_free() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_free'> `int sql_result_free(str "sres")` </a>

#### KSR.sqlops.sql_xquery() ####

<a target='_blank' href='/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_xquery'> `int sql_xquery(str "scon", str "squery", str "xavp")` </a>

## ss7ops ##

#### KSR.ss7ops.isup_to_json() ####

<a target='_blank' href='/docs/modules/devel/modules/ss7ops.html#ss7ops.f.isup_to_json'> `int isup_to_json(int proto)` </a>

## sst ##

#### KSR.sst.sst_check_min() ####

<a target='_blank' href='/docs/modules/devel/modules/sst.html#sst.f.sst_check_min'> `int sst_check_min(int flag)` </a>

## statistics ##

#### KSR.statistics.reset_stat() ####

<a target='_blank' href='/docs/modules/devel/modules/statistics.html#statistics.f.reset_stat'> `int reset_stat(str "sname")` </a>

#### KSR.statistics.update_stat() ####

<a target='_blank' href='/docs/modules/devel/modules/statistics.html#statistics.f.update_stat'> `int update_stat(str "sname", int sval)` </a>

## statsc ##

#### KSR.statsc.statsc_reset() ####

<a target='_blank' href='/docs/modules/devel/modules/statsc.html#statsc.f.statsc_reset'> `int statsc_reset()` </a>

## statsd ##

#### KSR.statsd.statsd_decr() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_decr'> `int statsd_decr(str "key")` </a>

#### KSR.statsd.statsd_gauge() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_gauge'> `int statsd_gauge(str "key", str "val")` </a>

#### KSR.statsd.statsd_incr() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_incr'> `int statsd_incr(str "key")` </a>

#### KSR.statsd.statsd_set() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_set'> `int statsd_set(str "key", str "val")` </a>

#### KSR.statsd.statsd_start() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_start'> `int statsd_start(str "key")` </a>

#### KSR.statsd.statsd_stop() ####

<a target='_blank' href='/docs/modules/devel/modules/statsd.html#statsd.f.statsd_stop'> `int statsd_stop(str "key")` </a>

## tcpops ##

#### KSR.tcpops.tcp_conid_alive() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_alive'> `int tcp_conid_alive(int i_conid)` </a>

#### KSR.tcpops.tcp_conid_state() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_conid_state'> `int tcp_conid_state(int i_conid)` </a>

#### KSR.tcpops.tcp_enable_closed_event() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event'> `int tcp_enable_closed_event()` </a>

#### KSR.tcpops.tcp_enable_closed_event_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_enable_closed_event_cid'> `int tcp_enable_closed_event_cid(int i_conid)` </a>

#### KSR.tcpops.tcp_keepalive_disable() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable'> `int tcp_keepalive_disable()` </a>

#### KSR.tcpops.tcp_keepalive_disable_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_disable_cid'> `int tcp_keepalive_disable_cid(int i_con)` </a>

#### KSR.tcpops.tcp_keepalive_enable() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable'> `int tcp_keepalive_enable(int i_idle, int i_cnt, int i_intvl)` </a>

#### KSR.tcpops.tcp_keepalive_enable_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_keepalive_enable_cid'> `int tcp_keepalive_enable_cid(int i_con, int i_idle, int i_cnt, int i_intvl)` </a>

#### KSR.tcpops.tcp_set_connection_lifetime() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime'> `int tcp_set_connection_lifetime(int i_time)` </a>

#### KSR.tcpops.tcp_set_connection_lifetime_cid() ####

<a target='_blank' href='/docs/modules/devel/modules/tcpops.html#tcpops.f.tcp_set_connection_lifetime_cid'> `int tcp_set_connection_lifetime_cid(int i_conid, int i_time)` </a>

## textops ##

#### KSR.textops.append_body_part() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.append_body_part'> `int append_body_part(str "txt", str "ct")` </a>

#### KSR.textops.append_body_part_cd() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.append_body_part_cd'> `int append_body_part_cd(str "txt", str "ct", str "cd")` </a>

#### KSR.textops.append_body_part_hex() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex'> `int append_body_part_hex(str "txt", str "ct")` </a>

#### KSR.textops.append_body_part_hex_cd() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.append_body_part_hex_cd'> `int append_body_part_hex_cd(str "htxt", str "ct", str "cd")` </a>

#### KSR.textops.cmp_istr() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.cmp_istr'> `int cmp_istr(str "s1", str "s2")` </a>

#### KSR.textops.cmp_str() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.cmp_str'> `int cmp_str(str "s1", str "s2")` </a>

#### KSR.textops.filter_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.filter_body'> `int filter_body(str "content_type")` </a>

#### KSR.textops.get_body_part() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.get_body_part'> `int get_body_part(str "ctype", str "pvname")` </a>

#### KSR.textops.get_body_part_raw() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.get_body_part_raw'> `int get_body_part_raw(str "ctype", str "pvname")` </a>

#### KSR.textops.has_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.has_body'> `int has_body()` </a>

#### KSR.textops.has_body_type() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.has_body_type'> `int has_body_type(str "ctype")` </a>

#### KSR.textops.in_list() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.in_list'> `int in_list(str "subject", str "list", str "vsep")` </a>

#### KSR.textops.in_list_prefix() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.in_list_prefix'> `int in_list_prefix(str "subject", str "list", str "vsep")` </a>

#### KSR.textops.is_audio_on_hold() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.is_audio_on_hold'> `int is_audio_on_hold()` </a>

#### KSR.textops.is_present_hf() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.is_present_hf'> `int is_present_hf(str "hname")` </a>

#### KSR.textops.is_present_hf_re() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.is_present_hf_re'> `int is_present_hf_re(str "ematch")` </a>

#### KSR.textops.is_privacy() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.is_privacy'> `int is_privacy(str "privacy")` </a>

#### KSR.textops.regex_substring() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.regex_substring'> `int regex_substring(str "input", str "regex", int mindex, int nmatch, str "dst")` </a>

#### KSR.textops.remove_body_part() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.remove_body_part'> `int remove_body_part(str "content_type")` </a>

#### KSR.textops.remove_hf_exp() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.remove_hf_exp'> `int remove_hf_exp(str "ematch", str "eskip")` </a>

#### KSR.textops.remove_hf_re() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.remove_hf_re'> `int remove_hf_re(str "ematch")` </a>

#### KSR.textops.replace() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace'> `int replace(str "sre", str "sval")` </a>

#### KSR.textops.replace_all() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_all'> `int replace_all(str "sre", str "sval")` </a>

#### KSR.textops.replace_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_body'> `int replace_body(str "sre", str "sval")` </a>

#### KSR.textops.replace_body_all() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_body_all'> `int replace_body_all(str "sre", str "sval")` </a>

#### KSR.textops.replace_body_atonce() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_body_atonce'> `int replace_body_atonce(str "sre", str "sval")` </a>

#### KSR.textops.replace_body_str() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_body_str'> `int replace_body_str(str "mkey", str "rval", str "rmode")` </a>

#### KSR.textops.replace_hdrs() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs'> `int replace_hdrs(str "sre", str "sval")` </a>

#### KSR.textops.replace_hdrs_str() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_hdrs_str'> `int replace_hdrs_str(str "mkey", str "rval", str "rmode")` </a>

#### KSR.textops.replace_str() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.replace_str'> `int replace_str(str "mkey", str "rval", str "rmode")` </a>

#### KSR.textops.search() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.search'> `int search(str "sre")` </a>

#### KSR.textops.search_append() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.search_append'> `int search_append(str "ematch", str "val")` </a>

#### KSR.textops.search_append_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.search_append_body'> `int search_append_body(str "ematch", str "val")` </a>

#### KSR.textops.search_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.search_body'> `int search_body(str "sre")` </a>

#### KSR.textops.search_hf() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.search_hf'> `int search_hf(str "hname", str "sre", str "flags")` </a>

#### KSR.textops.set_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_body'> `int set_body(str "nb", str "nc")` </a>

#### KSR.textops.set_body_multipart() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart'> `int set_body_multipart(str "nbody", str "ctype", str "boundary")` </a>

#### KSR.textops.set_body_multipart_boundary() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_boundary'> `int set_body_multipart_boundary(str "boundary")` </a>

#### KSR.textops.set_body_multipart_content() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_content'> `int set_body_multipart_content(str "nbody", str "ctype")` </a>

#### KSR.textops.set_body_multipart_mode() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_body_multipart_mode'> `int set_body_multipart_mode()` </a>

#### KSR.textops.set_reply_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.set_reply_body'> `int set_reply_body(str "nb", str "nc")` </a>

#### KSR.textops.starts_with() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.starts_with'> `int starts_with(str "s1", str "s2")` </a>

#### KSR.textops.subst() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.subst'> `int subst(str "subst")` </a>

#### KSR.textops.subst_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.subst_body'> `int subst_body(str "subst")` </a>

#### KSR.textops.subst_hf() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.subst_hf'> `int subst_hf(str "hname", str "subst", str "flags")` </a>

#### KSR.textops.subst_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.subst_uri'> `int subst_uri(str "subst")` </a>

#### KSR.textops.subst_user() ####

<a target='_blank' href='/docs/modules/devel/modules/textops.html#textops.f.subst_user'> `int subst_user(str "subst")` </a>

## textopsx ##

#### KSR.textopsx.append_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.append_hf_value'> `int append_hf_value(str "hexp", str "val")` </a>

#### KSR.textopsx.assign_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value'> `int assign_hf_value(str "hexp", str "val")` </a>

#### KSR.textopsx.assign_hf_value2() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.assign_hf_value2'> `int assign_hf_value2(str "hexp", str "val")` </a>

#### KSR.textopsx.change_reply_status() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.change_reply_status'> `int change_reply_status(int code, str "reason")` </a>

#### KSR.textopsx.exclude_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.exclude_hf_value'> `int exclude_hf_value(str "hexp", str "val")` </a>

#### KSR.textopsx.fnmatch() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch'> `int fnmatch(str "val", str "match")` </a>

#### KSR.textopsx.fnmatch_ex() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.fnmatch_ex'> `int fnmatch_ex(str "val", str "match", str "flags")` </a>

#### KSR.textopsx.hf_value_exists() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.hf_value_exists'> `int hf_value_exists(str "hexp", str "val")` </a>

#### KSR.textopsx.include_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.include_hf_value'> `int include_hf_value(str "hexp", str "val")` </a>

#### KSR.textopsx.insert_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.insert_hf_value'> `int insert_hf_value(str "hexp", str "val")` </a>

#### KSR.textopsx.keep_hf() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf'> `int keep_hf()` </a>

#### KSR.textopsx.keep_hf_re() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.keep_hf_re'> `int keep_hf_re(str "sre")` </a>

#### KSR.textopsx.msg_apply_changes() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_apply_changes'> `int msg_apply_changes()` </a>

#### KSR.textopsx.msg_set_buffer() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.msg_set_buffer'> `int msg_set_buffer(str "obuf")` </a>

#### KSR.textopsx.remove_body() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_body'> `int remove_body()` </a>

#### KSR.textopsx.remove_hf_value() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value'> `int remove_hf_value(str "hexp")` </a>

#### KSR.textopsx.remove_hf_value2() ####

<a target='_blank' href='/docs/modules/devel/modules/textopsx.html#textopsx.f.remove_hf_value2'> `int remove_hf_value2(str "hexp", str "val")` </a>

## tls ##

#### KSR.tls.is_peer_verified() ####

<a target='_blank' href='/docs/modules/devel/modules/tls.html#tls.f.is_peer_verified'> `int is_peer_verified()` </a>

## tm ##

#### KSR.tm.t_any_replied() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_any_replied'> `int t_any_replied()` </a>

#### KSR.tm.t_any_timeout() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_any_timeout'> `int t_any_timeout()` </a>

#### KSR.tm.t_branch_replied() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_branch_replied'> `int t_branch_replied()` </a>

#### KSR.tm.t_branch_timeout() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_branch_timeout'> `int t_branch_timeout()` </a>

#### KSR.tm.t_check_status() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_check_status'> `int t_check_status(str "sexp")` </a>

#### KSR.tm.t_check_trans() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_check_trans'> `int t_check_trans()` </a>

#### KSR.tm.t_drop_replies() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies'> `int t_drop_replies(str "mode")` </a>

#### KSR.tm.t_drop_replies_all() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_drop_replies_all'> `int t_drop_replies_all()` </a>

#### KSR.tm.t_get_status_code() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_get_status_code'> `int t_get_status_code()` </a>

#### KSR.tm.t_grep_status() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_grep_status'> `int t_grep_status(int code)` </a>

#### KSR.tm.t_is_canceled() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_is_canceled'> `int t_is_canceled()` </a>

#### KSR.tm.t_is_expired() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_is_expired'> `int t_is_expired()` </a>

#### KSR.tm.t_is_retr_async_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_is_retr_async_reply'> `int t_is_retr_async_reply()` </a>

#### KSR.tm.t_is_set() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_is_set'> `int t_is_set(str "target")` </a>

#### KSR.tm.t_load_contacts() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_load_contacts'> `int t_load_contacts()` </a>

#### KSR.tm.t_lookup_cancel() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel'> `int t_lookup_cancel()` </a>

#### KSR.tm.t_lookup_cancel_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_lookup_cancel_flags'> `int t_lookup_cancel_flags(int flags)` </a>

#### KSR.tm.t_lookup_request() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_lookup_request'> `int t_lookup_request()` </a>

#### KSR.tm.t_newtran() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_newtran'> `int t_newtran()` </a>

#### KSR.tm.t_next_contact_flow() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_next_contact_flow'> `int t_next_contact_flow()` </a>

#### KSR.tm.t_next_contacts() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_next_contacts'> `int t_next_contacts()` </a>

#### KSR.tm.t_on_branch() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_on_branch'> `int t_on_branch(str "rname")` </a>

#### KSR.tm.t_on_branch_failure() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_on_branch_failure'> `int t_on_branch_failure(str "rname")` </a>

#### KSR.tm.t_on_failure() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_on_failure'> `int t_on_failure(str "rname")` </a>

#### KSR.tm.t_on_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_on_reply'> `int t_on_reply(str "rname")` </a>

#### KSR.tm.t_relay() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_relay'> `int t_relay()` </a>

#### KSR.tm.t_relay_to_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_flags'> `int t_relay_to_flags(int rflags)` </a>

#### KSR.tm.t_relay_to_proxy() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy'> `int t_relay_to_proxy(str "sproxy")` </a>

#### KSR.tm.t_relay_to_proxy_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_relay_to_proxy_flags'> `int t_relay_to_proxy_flags(str "sproxy", int rflags)` </a>

#### KSR.tm.t_release() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_release'> `int t_release()` </a>

#### KSR.tm.t_replicate() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_replicate'> `int t_replicate(str "suri")` </a>

#### KSR.tm.t_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_reply'> `int t_reply(int code, str "reason")` </a>

#### KSR.tm.t_reset_fr() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_reset_fr'> `int t_reset_fr()` </a>

#### KSR.tm.t_reset_max_lifetime() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_reset_max_lifetime'> `int t_reset_max_lifetime()` </a>

#### KSR.tm.t_reset_retr() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_reset_retr'> `int t_reset_retr()` </a>

#### KSR.tm.t_retransmit_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_retransmit_reply'> `int t_retransmit_reply()` </a>

#### KSR.tm.t_save_lumps() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_save_lumps'> `int t_save_lumps()` </a>

#### KSR.tm.t_send_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_send_reply'> `int t_send_reply(int code, str "reason")` </a>

#### KSR.tm.t_set_auto_inv_100() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_auto_inv_100'> `int t_set_auto_inv_100(int state)` </a>

#### KSR.tm.t_set_disable_6xx() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_6xx'> `int t_set_disable_6xx(int state)` </a>

#### KSR.tm.t_set_disable_failover() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_failover'> `int t_set_disable_failover(int state)` </a>

#### KSR.tm.t_set_disable_internal_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_disable_internal_reply'> `int t_set_disable_internal_reply(int state)` </a>

#### KSR.tm.t_set_fr() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_fr'> `int t_set_fr(int fr_inv, int fr)` </a>

#### KSR.tm.t_set_fr_inv() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_fr_inv'> `int t_set_fr_inv(int fr_inv)` </a>

#### KSR.tm.t_set_max_lifetime() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_max_lifetime'> `int t_set_max_lifetime(int t1, int t2)` </a>

#### KSR.tm.t_set_no_e2e_cancel_reason() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_no_e2e_cancel_reason'> `int t_set_no_e2e_cancel_reason(int state)` </a>

#### KSR.tm.t_set_retr() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_set_retr'> `int t_set_retr(int t1, int t2)` </a>

#### KSR.tm.t_uac_send() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_uac_send'> `int t_uac_send(str "method", str "ruri", str "nexthop", str "ssock", str "hdrs", str "body")` </a>

#### KSR.tm.t_use_uac_headers() ####

<a target='_blank' href='/docs/modules/devel/modules/tm.html#tm.f.t_use_uac_headers'> `int t_use_uac_headers()` </a>

## tmrec ##

#### KSR.tmrec.is_leap_year() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year'> `int is_leap_year(int y)` </a>

#### KSR.tmrec.is_leap_year_now() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.is_leap_year_now'> `int is_leap_year_now()` </a>

#### KSR.tmrec.match() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.match'> `int match(str "rv")` </a>

#### KSR.tmrec.match_timestamp() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.match_timestamp'> `int match_timestamp(str "rv", int ti)` </a>

#### KSR.tmrec.time_period_match() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match'> `int time_period_match(str "period")` </a>

#### KSR.tmrec.time_period_match_timestamp() ####

<a target='_blank' href='/docs/modules/devel/modules/tmrec.html#tmrec.f.time_period_match_timestamp'> `int time_period_match_timestamp(str "period", int ti)` </a>

## tmx ##

#### KSR.tmx.t_cancel_branches() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_branches'> `int t_cancel_branches(str "mode")` </a>

#### KSR.tmx.t_cancel_callid() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid'> `int t_cancel_callid(str "callid_s", str "cseq_s", int fl)` </a>

#### KSR.tmx.t_cancel_callid_reason() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_cancel_callid_reason'> `int t_cancel_callid_reason(str "callid_s", str "cseq_s", int fl, int rcode)` </a>

#### KSR.tmx.t_continue() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_continue'> `int t_continue(int tindex, int tlabel, str "cbname")` </a>

#### KSR.tmx.t_drop() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_drop'> `int t_drop()` </a>

#### KSR.tmx.t_drop_rcode() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_drop_rcode'> `int t_drop_rcode(int rcode)` </a>

#### KSR.tmx.t_flush_flags() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_flags'> `int t_flush_flags()` </a>

#### KSR.tmx.t_flush_xflags() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_flush_xflags'> `int t_flush_xflags()` </a>

#### KSR.tmx.t_is_branch_route() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_is_branch_route'> `int t_is_branch_route()` </a>

#### KSR.tmx.t_is_failure_route() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_is_failure_route'> `int t_is_failure_route()` </a>

#### KSR.tmx.t_is_reply_route() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_is_reply_route'> `int t_is_reply_route()` </a>

#### KSR.tmx.t_is_request_route() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_is_request_route'> `int t_is_request_route()` </a>

#### KSR.tmx.t_precheck_trans() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_precheck_trans'> `int t_precheck_trans()` </a>

#### KSR.tmx.t_reply_callid() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_reply_callid'> `int t_reply_callid(str "callid_s", str "cseq_s", int code, str "status_s")` </a>

#### KSR.tmx.t_reuse_branch() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_reuse_branch'> `int t_reuse_branch()` </a>

#### KSR.tmx.t_suspend() ####

<a target='_blank' href='/docs/modules/devel/modules/tmx.html#tmx.f.t_suspend'> `int t_suspend()` </a>

## tsilo ##

#### KSR.tsilo.ts_append() ####

<a target='_blank' href='/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append'> `int ts_append(str "_table", str "_ruri")` </a>

#### KSR.tsilo.ts_append_to() ####

<a target='_blank' href='/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to'> `int ts_append_to(int tindex, int tlabel, str "_table")` </a>

#### KSR.tsilo.ts_append_to_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_append_to_uri'> `int ts_append_to_uri(int tindex, int tlabel, str "_table", str "_uri")` </a>

#### KSR.tsilo.ts_store() ####

<a target='_blank' href='/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store'> `int ts_store()` </a>

#### KSR.tsilo.ts_store_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/tsilo.html#tsilo.f.ts_store_uri'> `int ts_store_uri(str "puri")` </a>

## uac ##

#### KSR.uac.uac_auth() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_auth'> `int uac_auth()` </a>

#### KSR.uac.uac_reg_disable() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_disable'> `int uac_reg_disable(str "attr", str "val")` </a>

#### KSR.uac.uac_reg_enable() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_enable'> `int uac_reg_enable(str "attr", str "val")` </a>

#### KSR.uac.uac_reg_lookup() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_lookup'> `int uac_reg_lookup(str "userid", str "sdst")` </a>

#### KSR.uac.uac_reg_refresh() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_refresh'> `int uac_reg_refresh(str "l_uuid")` </a>

#### KSR.uac.uac_reg_request_to() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_request_to'> `int uac_reg_request_to(str "userid", int imode)` </a>

#### KSR.uac.uac_reg_status() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_reg_status'> `int uac_reg_status(str "sruuid")` </a>

#### KSR.uac.uac_replace_from() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from'> `int uac_replace_from(str "pdsp", str "puri")` </a>

#### KSR.uac.uac_replace_from_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_replace_from_uri'> `int uac_replace_from_uri(str "puri")` </a>

#### KSR.uac.uac_replace_to() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to'> `int uac_replace_to(str "pdsp", str "puri")` </a>

#### KSR.uac.uac_replace_to_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_replace_to_uri'> `int uac_replace_to_uri(str "puri")` </a>

#### KSR.uac.uac_req_send() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_req_send'> `int uac_req_send()` </a>

#### KSR.uac.uac_restore_from() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_restore_from'> `int uac_restore_from()` </a>

#### KSR.uac.uac_restore_to() ####

<a target='_blank' href='/docs/modules/devel/modules/uac.html#uac.f.uac_restore_to'> `int uac_restore_to()` </a>

## uac_redirect ##

#### KSR.uac_redirect.get_redirects() ####

<a target='_blank' href='/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects'> `int get_redirects(int max_c, int max_b)` </a>

#### KSR.uac_redirect.get_redirects_acc() ####

<a target='_blank' href='/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_acc'> `int get_redirects_acc(int max_c, int max_b, str "reason")` </a>

#### KSR.uac_redirect.get_redirects_all() ####

<a target='_blank' href='/docs/modules/devel/modules/uac_redirect.html#uac_redirect.f.get_redirects_all'> `int get_redirects_all()` </a>

## uri_db ##

#### KSR.uri_db.check_from() ####

<a target='_blank' href='/docs/modules/devel/modules/uri_db.html#uri_db.f.check_from'> `int check_from()` </a>

#### KSR.uri_db.check_to() ####

<a target='_blank' href='/docs/modules/devel/modules/uri_db.html#uri_db.f.check_to'> `int check_to()` </a>

#### KSR.uri_db.check_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri'> `int check_uri(str "suri")` </a>

#### KSR.uri_db.check_uri_realm() ####

<a target='_blank' href='/docs/modules/devel/modules/uri_db.html#uri_db.f.check_uri_realm'> `int check_uri_realm(str "suri", str "susername", str "srealm")` </a>

#### KSR.uri_db.does_uri_exist() ####

<a target='_blank' href='/docs/modules/devel/modules/uri_db.html#uri_db.f.does_uri_exist'> `int does_uri_exist()` </a>

## userblacklist ##

#### KSR.userblacklist.check_user_blacklist() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_blacklist'> `int check_user_blacklist(str "suser", str "sdomain")` </a>

#### KSR.userblacklist.check_user_blacklist_number() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_blacklist_number'> `int check_user_blacklist_number(str "suser", str "sdomain", str "snumber")` </a>

#### KSR.userblacklist.check_user_blacklist_table() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_blacklist_table'> `int check_user_blacklist_table(str "suser", str "sdomain", str "snumber", str "stable")` </a>

#### KSR.userblacklist.check_user_whitelist() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_whitelist'> `int check_user_whitelist(str "suser", str "sdomain")` </a>

#### KSR.userblacklist.check_user_whitelist_number() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_whitelist_number'> `int check_user_whitelist_number(str "suser", str "sdomain", str "snumber")` </a>

#### KSR.userblacklist.check_user_whitelist_table() ####

<a target='_blank' href='/docs/modules/devel/modules/userblacklist.html#userblacklist.f.check_user_whitelist_table'> `int check_user_whitelist_table(str "suser", str "sdomain", str "snumber", str "stable")` </a>

## utils ##

#### KSR.utils.xcap_auth_status() ####

<a target='_blank' href='/docs/modules/devel/modules/utils.html#utils.f.xcap_auth_status'> `int xcap_auth_status(str "watcher_uri", str "presentity_uri")` </a>

## websocket ##

#### KSR.websocket.close() ####

<a target='_blank' href='/docs/modules/devel/modules/websocket.html#websocket.f.close'> `int close()` </a>

#### KSR.websocket.close_conid() ####

<a target='_blank' href='/docs/modules/devel/modules/websocket.html#websocket.f.close_conid'> `int close_conid(int status, str "reason", int con)` </a>

#### KSR.websocket.close_reason() ####

<a target='_blank' href='/docs/modules/devel/modules/websocket.html#websocket.f.close_reason'> `int close_reason(int status, str "reason")` </a>

#### KSR.websocket.handle_handshake() ####

<a target='_blank' href='/docs/modules/devel/modules/websocket.html#websocket.f.handle_handshake'> `int handle_handshake()` </a>

## xcap_server ##

#### KSR.xcap_server.xcaps_del() ####

<a target='_blank' href='/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_del'> `int xcaps_del(str "uri", str "path")` </a>

#### KSR.xcap_server.xcaps_get() ####

<a target='_blank' href='/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_get'> `int xcaps_get(str "uri", str "path")` </a>

#### KSR.xcap_server.xcaps_put() ####

<a target='_blank' href='/docs/modules/devel/modules/xcap_server.html#xcap_server.f.xcaps_put'> `int xcaps_put(str "uri", str "path", str "pbody")` </a>

## xhttp ##

#### KSR.xhttp.xhttp_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp.html#xhttp.f.xhttp_reply'> `int xhttp_reply(int code, str "reason", str "ctype", str "body")` </a>

## xhttp_pi ##

#### KSR.xhttp_pi.dispatch() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_pi.html#xhttp_pi.f.dispatch'> `int dispatch()` </a>

## xhttp_prom ##

#### KSR.xhttp_prom.check_uri() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.check_uri'> `int check_uri()` </a>

#### KSR.xhttp_prom.counter_inc_l0() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l0'> `int counter_inc_l0(str "s_name", int number)` </a>

#### KSR.xhttp_prom.counter_inc_l1() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l1'> `int counter_inc_l1(str "s_name", int number, str "l1")` </a>

#### KSR.xhttp_prom.counter_inc_l2() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l2'> `int counter_inc_l2(str "s_name", int number, str "l1", str "l2")` </a>

#### KSR.xhttp_prom.counter_inc_l3() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_inc_l3'> `int counter_inc_l3(str "s_name", int number, str "l1", str "l2", str "l3")` </a>

#### KSR.xhttp_prom.counter_reset_l0() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l0'> `int counter_reset_l0(str "s_name")` </a>

#### KSR.xhttp_prom.counter_reset_l1() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l1'> `int counter_reset_l1(str "s_name", str "l1")` </a>

#### KSR.xhttp_prom.counter_reset_l2() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l2'> `int counter_reset_l2(str "s_name", str "l1", str "l2")` </a>

#### KSR.xhttp_prom.counter_reset_l3() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.counter_reset_l3'> `int counter_reset_l3(str "s_name", str "l1", str "l2", str "l3")` </a>

#### KSR.xhttp_prom.dispatch() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.dispatch'> `int dispatch()` </a>

#### KSR.xhttp_prom.gauge_reset_l0() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l0'> `int gauge_reset_l0(str "s_name")` </a>

#### KSR.xhttp_prom.gauge_reset_l1() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l1'> `int gauge_reset_l1(str "s_name", str "l1")` </a>

#### KSR.xhttp_prom.gauge_reset_l2() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l2'> `int gauge_reset_l2(str "s_name", str "l1", str "l2")` </a>

#### KSR.xhttp_prom.gauge_reset_l3() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_reset_l3'> `int gauge_reset_l3(str "s_name", str "l1", str "l2", str "l3")` </a>

#### KSR.xhttp_prom.gauge_set_l0() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l0'> `int gauge_set_l0(str "s_name", str "s_number")` </a>

#### KSR.xhttp_prom.gauge_set_l1() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l1'> `int gauge_set_l1(str "s_name", str "s_number", str "l1")` </a>

#### KSR.xhttp_prom.gauge_set_l2() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l2'> `int gauge_set_l2(str "s_name", str "s_number", str "l1", str "l2")` </a>

#### KSR.xhttp_prom.gauge_set_l3() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_prom.html#xhttp_prom.f.gauge_set_l3'> `int gauge_set_l3(str "s_name", str "s_number", str "l1", str "l2", str "l3")` </a>

## xhttp_rpc ##

#### KSR.xhttp_rpc.dispatch() ####

<a target='_blank' href='/docs/modules/devel/modules/xhttp_rpc.html#xhttp_rpc.f.dispatch'> `int dispatch()` </a>

## xlog ##

#### KSR.xlog.xalert() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xalert'> `int xalert(str "lmsg")` </a>

#### KSR.xlog.xcrit() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xcrit'> `int xcrit(str "lmsg")` </a>

#### KSR.xlog.xdbg() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xdbg'> `int xdbg(str "lmsg")` </a>

#### KSR.xlog.xerr() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xerr'> `int xerr(str "lmsg")` </a>

#### KSR.xlog.xinfo() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xinfo'> `int xinfo(str "lmsg")` </a>

#### KSR.xlog.xlog() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xlog'> `int xlog(str "slevel", str "lmsg")` </a>

#### KSR.xlog.xnotice() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xnotice'> `int xnotice(str "lmsg")` </a>

#### KSR.xlog.xwarn() ####

<a target='_blank' href='/docs/modules/devel/modules/xlog.html#xlog.f.xwarn'> `int xwarn(str "lmsg")` </a>

## xmlrpc ##

#### KSR.xmlrpc.dispatch_rpc() ####

<a target='_blank' href='/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.dispatch_rpc'> `int dispatch_rpc()` </a>

#### KSR.xmlrpc.xmlrpc_reply() ####

<a target='_blank' href='/docs/modules/devel/modules/xmlrpc.html#xmlrpc.f.xmlrpc_reply'> `int xmlrpc_reply(int rcode, str "reason")` </a>

