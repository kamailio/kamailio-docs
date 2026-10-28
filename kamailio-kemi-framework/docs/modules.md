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

## acc ##

* 📖[kamailio.cfg::module::acc.html](https://kamailio.org/docs/modules/devel/modules/acc.html)

The functions exported by `acc` module to KEMI are listed in the next sections.

Exported functions:

* [KSR.acc.acc_db_request\(\)](modules/acc/acc.md#ksraccacc_db_request)
* [KSR.acc.acc_log_request\(\)](modules/acc/acc.md#ksraccacc_log_request)
* [KSR.acc.acc_request\(\)](modules/acc/acc.md#ksraccacc_request)

## acc_radius ##

* 📖[kamailio.cfg::module::acc_radius.html](https://kamailio.org/docs/modules/devel/modules/acc_radius.html)

Exported functions:

* [KSR.acc_radius.request\(\)](modules/acc_radius/acc_radius.md#ksracc_radiusrequest)

## alias_db ##

* 📖[kamailio.cfg::module::alias_db.html](https://kamailio.org/docs/modules/devel/modules/alias_db.html)

Exported functions:

* [KSR.alias_db.lookup\(\)](modules/alias_db/alias_db.md#ksralias_dblookup)
* [KSR.alias_db.lookup_ex\(\)](modules/alias_db/alias_db.md#ksralias_dblookup_ex)

## app_jsdt ##

* 📖[kamailio.cfg::module::app_jsdt.html](https://kamailio.org/docs/modules/devel/modules/app_jsdt.html)

Exported functions:

* [KSR.app_jsdt.dofile\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtdofile)
* [KSR.app_jsdt.dostring\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtdostring)
* [KSR.app_jsdt.run\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtrun)
* [KSR.app_jsdt.run_p1\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtrun_p1)
* [KSR.app_jsdt.run_p2\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtrun_p2)
* [KSR.app_jsdt.run_p3\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtrun_p3)
* [KSR.app_jsdt.runstring\(\)](modules/app_jsdt/app_jsdt.md#ksrapp_jsdtrunstring)

## app_lua ##

* 📖[kamailio.cfg::module::app_lua.html](https://kamailio.org/docs/modules/devel/modules/app_lua.html)

Exported functions:

* [KSR.app_lua.dofile\(\)](modules/app_lua/app_lua.md#ksrapp_luadofile)
* [KSR.app_lua.dostring\(\)](modules/app_lua/app_lua.md#ksrapp_luadostring)
* [KSR.app_lua.run\(\)](modules/app_lua/app_lua.md#ksrapp_luarun)
* [KSR.app_lua.run_p1\(\)](modules/app_lua/app_lua.md#ksrapp_luarun_p1)
* [KSR.app_lua.run_p2\(\)](modules/app_lua/app_lua.md#ksrapp_luarun_p2)
* [KSR.app_lua.run_p3\(\)](modules/app_lua/app_lua.md#ksrapp_luarun_p3)
* [KSR.app_lua.runstring\(\)](modules/app_lua/app_lua.md#ksrapp_luarunstring)

## app_python ##

* 📖[kamailio.cfg::module::app_python.html](https://kamailio.org/docs/modules/devel/modules/app_python.html)

Exported functions:

* [KSR.app_python.exec\(\)](modules/app_python/app_python.md#ksrapp_pythonexec)
* [KSR.app_python.exec_p1\(\)](modules/app_python/app_python.md#ksrapp_pythonexec_p1)
* [KSR.app_python.execx\(\)](modules/app_python/app_python.md#ksrapp_pythonexecx)

## app_python3 ##

* 📖[kamailio.cfg::module::app_python3.html](https://kamailio.org/docs/modules/devel/modules/app_python3.html)

Exported functions:

* [KSR.app_python3.exec\(\)](modules/app_python3/app_python3.md#ksrapp_python3exec)
* [KSR.app_python3.exec_p1\(\)](modules/app_python3/app_python3.md#ksrapp_python3exec_p1)
* [KSR.app_python3.execx\(\)](modules/app_python3/app_python3.md#ksrapp_python3execx)

## app_python3s ##

* 📖[kamailio.cfg::module::app_python3s.html](https://kamailio.org/docs/modules/devel/modules/app_python3s.html)

Exported functions:

* [KSR.app_python3s.exec\(\)](modules/app_python3s/app_python3s.md#ksrapp_python3sexec)
* [KSR.app_python3s.exec_p1\(\)](modules/app_python3s/app_python3s.md#ksrapp_python3sexec_p1)
* [KSR.app_python3s.execx\(\)](modules/app_python3s/app_python3s.md#ksrapp_python3sexecx)

## app_ruby ##

* 📖[kamailio.cfg::module::app_ruby.html](https://kamailio.org/docs/modules/devel/modules/app_ruby.html)

Exported functions:

* [KSR.app_ruby.run\(\)](modules/app_ruby/app_ruby.md#ksrapp_rubyrun)
* [KSR.app_ruby.run_p1\(\)](modules/app_ruby/app_ruby.md#ksrapp_rubyrun_p1)
* [KSR.app_ruby.run_p2\(\)](modules/app_ruby/app_ruby.md#ksrapp_rubyrun_p2)
* [KSR.app_ruby.run_p3\(\)](modules/app_ruby/app_ruby.md#ksrapp_rubyrun_p3)

## async ##

* 📖[kamailio.cfg::module::async.html](https://kamailio.org/docs/modules/devel/modules/async.html)

Exported functions:

* [KSR.async.get_data\(\)](modules/async/async.md#ksrasyncget_data)
* [KSR.async.get_gname\(\)](modules/async/async.md#ksrasyncget_gname)
* [KSR.async.ms_route\(\)](modules/async/async.md#ksrasyncms_route)
* [KSR.async.route\(\)](modules/async/async.md#ksrasyncroute)
* [KSR.async.task_data\(\)](modules/async/async.md#ksrasynctask_data)
* [KSR.async.task_group_data\(\)](modules/async/async.md#ksrasynctask_group_data)
* [KSR.async.task_group_route\(\)](modules/async/async.md#ksrasynctask_group_route)
* [KSR.async.task_route\(\)](modules/async/async.md#ksrasynctask_route)

## auth ##

* 📖[kamailio.cfg::module::auth.html](https://kamailio.org/docs/modules/devel/modules/auth.html)

Exported functions:

* [KSR.auth.auth_algorithm\(\)](modules/auth/auth.md#ksrauthauth_algorithm)
* [KSR.auth.auth_challenge\(\)](modules/auth/auth.md#ksrauthauth_challenge)
* [KSR.auth.auth_get_www_authenticate\(\)](modules/auth/auth.md#ksrauthauth_get_www_authenticate)
* [KSR.auth.consume_credentials\(\)](modules/auth/auth.md#ksrauthconsume_credentials)
* [KSR.auth.has_credentials\(\)](modules/auth/auth.md#ksrauthhas_credentials)
* [KSR.auth.proxy_challenge\(\)](modules/auth/auth.md#ksrauthproxy_challenge)
* [KSR.auth.pv_auth_check\(\)](modules/auth/auth.md#ksrauthpv_auth_check)
* [KSR.auth.pv_proxy_authenticate\(\)](modules/auth/auth.md#ksrauthpv_proxy_authenticate)
* [KSR.auth.pv_www_authenticate\(\)](modules/auth/auth.md#ksrauthpv_www_authenticate)
* [KSR.auth.pv_www_authenticate_method\(\)](modules/auth/auth.md#ksrauthpv_www_authenticate_method)
* [KSR.auth.www_challenge\(\)](modules/auth/auth.md#ksrauthwww_challenge)

## auth_db ##

* 📖[kamailio.cfg::module::auth_db.html](https://kamailio.org/docs/modules/devel/modules/auth_db.html)

Exported functions:

* [KSR.auth_db.auth_check\(\)](modules/auth_db/auth_db.md#ksrauth_dbauth_check)
* [KSR.auth_db.is_subscriber\(\)](modules/auth_db/auth_db.md#ksrauth_dbis_subscriber)
* [KSR.auth_db.www_authenticate\(\)](modules/auth_db/auth_db.md#ksrauth_dbwww_authenticate)
* [KSR.auth_db.www_authenticate_method\(\)](modules/auth_db/auth_db.md#ksrauth_dbwww_authenticate_method)

## auth_ephemeral ##

* 📖[kamailio.cfg::module::auth_ephemeral.html](https://kamailio.org/docs/modules/devel/modules/auth_ephemeral.html)

Exported functions:

* [KSR.auth_ephemeral.autheph_authenticate\(\)](modules/auth_ephemeral/auth_ephemeral.md#ksrauth_ephemeralautheph_authenticate)
* [KSR.auth_ephemeral.autheph_check\(\)](modules/auth_ephemeral/auth_ephemeral.md#ksrauth_ephemeralautheph_check)
* [KSR.auth_ephemeral.autheph_proxy\(\)](modules/auth_ephemeral/auth_ephemeral.md#ksrauth_ephemeralautheph_proxy)
* [KSR.auth_ephemeral.autheph_www\(\)](modules/auth_ephemeral/auth_ephemeral.md#ksrauth_ephemeralautheph_www)
* [KSR.auth_ephemeral.autheph_www_method\(\)](modules/auth_ephemeral/auth_ephemeral.md#ksrauth_ephemeralautheph_www_method)

## auth_radius ##

* 📖[kamailio.cfg::module::auth_radius.html](https://kamailio.org/docs/modules/devel/modules/auth_radius.html)

Exported functions:

* [KSR.auth_radius.proxy_authorize\(\)](modules/auth_radius/auth_radius.md#ksrauth_radiusproxy_authorize)
* [KSR.auth_radius.proxy_authorize_user\(\)](modules/auth_radius/auth_radius.md#ksrauth_radiusproxy_authorize_user)
* [KSR.auth_radius.www_authorize\(\)](modules/auth_radius/auth_radius.md#ksrauth_radiuswww_authorize)
* [KSR.auth_radius.www_authorize_user\(\)](modules/auth_radius/auth_radius.md#ksrauth_radiuswww_authorize_user)

## auth_web3 ##

* 📖[kamailio.cfg::module::auth_web3.html](https://kamailio.org/docs/modules/devel/modules/auth_web3.html)

Exported functions:

* [KSR.auth_web3.web3_proxy_authenticate\(\)](modules/auth_web3/auth_web3.md#ksrauth_web3web3_proxy_authenticate)
* [KSR.auth_web3.web3_www_authenticate\(\)](modules/auth_web3/auth_web3.md#ksrauth_web3web3_www_authenticate)

## auth_xkeys ##

* 📖[kamailio.cfg::module::auth_xkeys.html](https://kamailio.org/docs/modules/devel/modules/auth_xkeys.html)

Exported functions:

* [KSR.auth_xkeys.auth_xkeys_add\(\)](modules/auth_xkeys/auth_xkeys.md#ksrauth_xkeysauth_xkeys_add)
* [KSR.auth_xkeys.auth_xkeys_check\(\)](modules/auth_xkeys/auth_xkeys.md#ksrauth_xkeysauth_xkeys_check)

## avpops ##

* 📖[kamailio.cfg::module::avpops.html](https://kamailio.org/docs/modules/devel/modules/avpops.html)

Exported functions:

* [KSR.avpops.avp_check\(\)](modules/avpops/avpops.md#ksravpopsavp_check)
* [KSR.avpops.avp_copy\(\)](modules/avpops/avpops.md#ksravpopsavp_copy)

## benchmark ##

* 📖[kamailio.cfg::module::benchmark.html](https://kamailio.org/docs/modules/devel/modules/benchmark.html)

Exported functions:

* [KSR.benchmark.bm_log_timer\(\)](modules/benchmark/benchmark.md#ksrbenchmarkbm_log_timer)
* [KSR.benchmark.bm_start_timer\(\)](modules/benchmark/benchmark.md#ksrbenchmarkbm_start_timer)

## blst ##

* 📖[kamailio.cfg::module::blst.html](https://kamailio.org/docs/modules/devel/modules/blst.html)

Exported functions:

* [KSR.blst.blst_add\(\)](modules/blst/blst.md#ksrblstblst_add)
* [KSR.blst.blst_add_default\(\)](modules/blst/blst.md#ksrblstblst_add_default)
* [KSR.blst.blst_add_retry_after\(\)](modules/blst/blst.md#ksrblstblst_add_retry_after)
* [KSR.blst.blst_clear_ignore\(\)](modules/blst/blst.md#ksrblstblst_clear_ignore)
* [KSR.blst.blst_clear_ignore_all\(\)](modules/blst/blst.md#ksrblstblst_clear_ignore_all)
* [KSR.blst.blst_del\(\)](modules/blst/blst.md#ksrblstblst_del)
* [KSR.blst.blst_is_blocklisted\(\)](modules/blst/blst.md#ksrblstblst_is_blocklisted)
* [KSR.blst.blst_rpl_clear_ignore\(\)](modules/blst/blst.md#ksrblstblst_rpl_clear_ignore)
* [KSR.blst.blst_rpl_clear_ignore_all\(\)](modules/blst/blst.md#ksrblstblst_rpl_clear_ignore_all)
* [KSR.blst.blst_rpl_set_ignore\(\)](modules/blst/blst.md#ksrblstblst_rpl_set_ignore)
* [KSR.blst.blst_rpl_set_ignore_all\(\)](modules/blst/blst.md#ksrblstblst_rpl_set_ignore_all)
* [KSR.blst.blst_set_ignore\(\)](modules/blst/blst.md#ksrblstblst_set_ignore)
* [KSR.blst.blst_set_ignore_all\(\)](modules/blst/blst.md#ksrblstblst_set_ignore_all)

## call_control ##

* 📖[kamailio.cfg::module::call_control.html](https://kamailio.org/docs/modules/devel/modules/call_control.html)

Exported functions:

* [KSR.call_control.call_control\(\)](modules/call_control/call_control.md#ksrcall_controlcall_control)

## call_obj ##

* 📖[kamailio.cfg::module::call_obj.html](https://kamailio.org/docs/modules/devel/modules/call_obj.html)

Exported functions:

* [KSR.call_obj.free\(\)](modules/call_obj/call_obj.md#ksrcall_objfree)
* [KSR.call_obj.get\(\)](modules/call_obj/call_obj.md#ksrcall_objget)

## carrierroute ##

* 📖[kamailio.cfg::module::carrierroute.html](https://kamailio.org/docs/modules/devel/modules/carrierroute.html)

Exported functions:

* [KSR.carrierroute.cr_next_domain\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_next_domain)
* [KSR.carrierroute.cr_nofallback_route\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_nofallback_route)
* [KSR.carrierroute.cr_nofallback_route_info\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_nofallback_route_info)
* [KSR.carrierroute.cr_route\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_route)
* [KSR.carrierroute.cr_route_info\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_route_info)
* [KSR.carrierroute.cr_user_carrier\(\)](modules/carrierroute/carrierroute.md#ksrcarrierroutecr_user_carrier)

## cdp ##

* 📖[kamailio.cfg::module::cdp.html](https://kamailio.org/docs/modules/devel/modules/cdp.html)

Exported functions:

* [KSR.cdp.cdp_check_peer\(\)](modules/cdp/cdp.md#ksrcdpcdp_check_peer)
* [KSR.cdp.cdp_has_app\(\)](modules/cdp/cdp.md#ksrcdpcdp_has_app)
* [KSR.cdp.cdp_has_app2\(\)](modules/cdp/cdp.md#ksrcdpcdp_has_app2)

## cfgutils ##

* 📖[kamailio.cfg::module::cfgutils.html](https://kamailio.org/docs/modules/devel/modules/cfgutils.html)

Exported functions:

* [KSR.cfgutils.abort\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsabort)
* [KSR.cfgutils.check_route_exists\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilscheck_route_exists)
* [KSR.cfgutils.core_hash\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilscore_hash)
* [KSR.cfgutils.lock\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilslock)
* [KSR.cfgutils.lock_key2\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilslock_key2)
* [KSR.cfgutils.pkg_status\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilspkg_status)
* [KSR.cfgutils.pkg_summary\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilspkg_summary)
* [KSR.cfgutils.rand_event\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsrand_event)
* [KSR.cfgutils.rand_get_prob\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsrand_get_prob)
* [KSR.cfgutils.rand_reset_prob\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsrand_reset_prob)
* [KSR.cfgutils.rand_set_prob\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsrand_set_prob)
* [KSR.cfgutils.route_if_exists\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsroute_if_exists)
* [KSR.cfgutils.shm_status\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsshm_status)
* [KSR.cfgutils.shm_summary\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsshm_summary)
* [KSR.cfgutils.sleep\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilssleep)
* [KSR.cfgutils.trylock\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilstrylock)
* [KSR.cfgutils.trylock_key2\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilstrylock_key2)
* [KSR.cfgutils.unlock\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsunlock)
* [KSR.cfgutils.unlock_key2\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsunlock_key2)
* [KSR.cfgutils.usleep\(\)](modules/cfgutils/cfgutils.md#ksrcfgutilsusleep)

## cnxcc ##

* 📖[kamailio.cfg::module::cnxcc.html](https://kamailio.org/docs/modules/devel/modules/cnxcc.html)

Exported functions:

* [KSR.cnxcc.get_channel_count\(\)](modules/cnxcc/cnxcc.md#ksrcnxccget_channel_count)
* [KSR.cnxcc.set_max_channels\(\)](modules/cnxcc/cnxcc.md#ksrcnxccset_max_channels)
* [KSR.cnxcc.set_max_credit\(\)](modules/cnxcc/cnxcc.md#ksrcnxccset_max_credit)
* [KSR.cnxcc.set_max_time\(\)](modules/cnxcc/cnxcc.md#ksrcnxccset_max_time)
* [KSR.cnxcc.terminate_all\(\)](modules/cnxcc/cnxcc.md#ksrcnxccterminate_all)
* [KSR.cnxcc.update_max_time\(\)](modules/cnxcc/cnxcc.md#ksrcnxccupdate_max_time)

## corex ##

* 📖[kamailio.cfg::module::corex.html](https://kamailio.org/docs/modules/devel/modules/corex.html)

Exported functions:

* [KSR.corex.append_branch\(\)](modules/corex/corex.md#ksrcorexappend_branch)
* [KSR.corex.append_branch_uri\(\)](modules/corex/corex.md#ksrcorexappend_branch_uri)
* [KSR.corex.append_branch_uri_q\(\)](modules/corex/corex.md#ksrcorexappend_branch_uri_q)
* [KSR.corex.file_read\(\)](modules/corex/corex.md#ksrcorexfile_read)
* [KSR.corex.file_write\(\)](modules/corex/corex.md#ksrcorexfile_write)
* [KSR.corex.forward_uac\(\)](modules/corex/corex.md#ksrcorexforward_uac)
* [KSR.corex.forward_uac_branch\(\)](modules/corex/corex.md#ksrcorexforward_uac_branch)
* [KSR.corex.forward_uac_uri\(\)](modules/corex/corex.md#ksrcorexforward_uac_uri)
* [KSR.corex.forward_uac_uri_branch\(\)](modules/corex/corex.md#ksrcorexforward_uac_uri_branch)
* [KSR.corex.has_ruri_user\(\)](modules/corex/corex.md#ksrcorexhas_ruri_user)
* [KSR.corex.has_user_agent\(\)](modules/corex/corex.md#ksrcorexhas_user_agent)
* [KSR.corex.is_faked_msg\(\)](modules/corex/corex.md#ksrcorexis_faked_msg)
* [KSR.corex.is_socket_name\(\)](modules/corex/corex.md#ksrcorexis_socket_name)
* [KSR.corex.isxflagset\(\)](modules/corex/corex.md#ksrcorexisxflagset)
* [KSR.corex.resetxflag\(\)](modules/corex/corex.md#ksrcorexresetxflag)
* [KSR.corex.send_data\(\)](modules/corex/corex.md#ksrcorexsend_data)
* [KSR.corex.sendx\(\)](modules/corex/corex.md#ksrcorexsendx)
* [KSR.corex.set_recv_socket\(\)](modules/corex/corex.md#ksrcorexset_recv_socket)
* [KSR.corex.set_recv_socket_name\(\)](modules/corex/corex.md#ksrcorexset_recv_socket_name)
* [KSR.corex.set_send_socket\(\)](modules/corex/corex.md#ksrcorexset_send_socket)
* [KSR.corex.set_send_socket_map\(\)](modules/corex/corex.md#ksrcorexset_send_socket_map)
* [KSR.corex.set_send_socket_name\(\)](modules/corex/corex.md#ksrcorexset_send_socket_name)
* [KSR.corex.set_source_address\(\)](modules/corex/corex.md#ksrcorexset_source_address)
* [KSR.corex.setxflag\(\)](modules/corex/corex.md#ksrcorexsetxflag)
* [KSR.corex.via_add_srvid\(\)](modules/corex/corex.md#ksrcorexvia_add_srvid)
* [KSR.corex.via_add_xavp_params\(\)](modules/corex/corex.md#ksrcorexvia_add_xavp_params)
* [KSR.corex.via_reply_add_xavp_params\(\)](modules/corex/corex.md#ksrcorexvia_reply_add_xavp_params)
* [KSR.corex.via_use_xavp_fields\(\)](modules/corex/corex.md#ksrcorexvia_use_xavp_fields)

## counters ##

* 📖[kamailio.cfg::module::counters.html](https://kamailio.org/docs/modules/devel/modules/counters.html)

Exported functions:

* [KSR.counters.add\(\)](modules/counters/counters.md#ksrcountersadd)
* [KSR.counters.inc\(\)](modules/counters/counters.md#ksrcountersinc)
* [KSR.counters.reset\(\)](modules/counters/counters.md#ksrcountersreset)

## crypto ##

* 📖[kamailio.cfg::module::crypto.html](https://kamailio.org/docs/modules/devel/modules/crypto.html)

Exported functions:

* [KSR.crypto.aes_decrypt\(\)](modules/crypto/crypto.md#ksrcryptoaes_decrypt)
* [KSR.crypto.aes_encrypt\(\)](modules/crypto/crypto.md#ksrcryptoaes_encrypt)
* [KSR.crypto.hmac_sha256\(\)](modules/crypto/crypto.md#ksrcryptohmac_sha256)

## debugger ##

* 📖[kamailio.cfg::module::debugger.html](https://kamailio.org/docs/modules/devel/modules/debugger.html)

Exported functions:

* [KSR.debugger.dbg_pv_dump\(\)](modules/debugger/debugger.md#ksrdebuggerdbg_pv_dump)
* [KSR.debugger.dbg_pv_dump_ex\(\)](modules/debugger/debugger.md#ksrdebuggerdbg_pv_dump_ex)

## dialog ##

* 📖[kamailio.cfg::module::dialog.html](https://kamailio.org/docs/modules/devel/modules/dialog.html)

Exported functions:

* [KSR.dialog.dlg_bridge\(\)](modules/dialog/dialog.md#ksrdialogdlg_bridge)
* [KSR.dialog.dlg_bye\(\)](modules/dialog/dialog.md#ksrdialogdlg_bye)
* [KSR.dialog.dlg_db_load_callid\(\)](modules/dialog/dialog.md#ksrdialogdlg_db_load_callid)
* [KSR.dialog.dlg_db_load_extra\(\)](modules/dialog/dialog.md#ksrdialogdlg_db_load_extra)
* [KSR.dialog.dlg_get\(\)](modules/dialog/dialog.md#ksrdialogdlg_get)
* [KSR.dialog.dlg_get_var\(\)](modules/dialog/dialog.md#ksrdialogdlg_get_var)
* [KSR.dialog.dlg_isflagset\(\)](modules/dialog/dialog.md#ksrdialogdlg_isflagset)
* [KSR.dialog.dlg_manage\(\)](modules/dialog/dialog.md#ksrdialogdlg_manage)
* [KSR.dialog.dlg_refer_cid\(\)](modules/dialog/dialog.md#ksrdialogdlg_refer_cid)
* [KSR.dialog.dlg_refer_did\(\)](modules/dialog/dialog.md#ksrdialogdlg_refer_did)
* [KSR.dialog.dlg_remove_dialogs_from_node\(\)](modules/dialog/dialog.md#ksrdialogdlg_remove_dialogs_from_node)
* [KSR.dialog.dlg_req_within2\(\)](modules/dialog/dialog.md#ksrdialogdlg_req_within2)
* [KSR.dialog.dlg_req_within3\(\)](modules/dialog/dialog.md#ksrdialogdlg_req_within3)
* [KSR.dialog.dlg_req_within4\(\)](modules/dialog/dialog.md#ksrdialogdlg_req_within4)
* [KSR.dialog.dlg_req_within5\(\)](modules/dialog/dialog.md#ksrdialogdlg_req_within5)
* [KSR.dialog.dlg_reset_property\(\)](modules/dialog/dialog.md#ksrdialogdlg_reset_property)
* [KSR.dialog.dlg_resetflag\(\)](modules/dialog/dialog.md#ksrdialogdlg_resetflag)
* [KSR.dialog.dlg_set_property\(\)](modules/dialog/dialog.md#ksrdialogdlg_set_property)
* [KSR.dialog.dlg_set_state\(\)](modules/dialog/dialog.md#ksrdialogdlg_set_state)
* [KSR.dialog.dlg_set_timeout\(\)](modules/dialog/dialog.md#ksrdialogdlg_set_timeout)
* [KSR.dialog.dlg_set_timeout_id\(\)](modules/dialog/dialog.md#ksrdialogdlg_set_timeout_id)
* [KSR.dialog.dlg_set_var\(\)](modules/dialog/dialog.md#ksrdialogdlg_set_var)
* [KSR.dialog.dlg_setflag\(\)](modules/dialog/dialog.md#ksrdialogdlg_setflag)
* [KSR.dialog.dlg_update_contact\(\)](modules/dialog/dialog.md#ksrdialogdlg_update_contact)
* [KSR.dialog.dlg_update_socket\(\)](modules/dialog/dialog.md#ksrdialogdlg_update_socket)
* [KSR.dialog.dlg_update_state\(\)](modules/dialog/dialog.md#ksrdialogdlg_update_state)
* [KSR.dialog.get_profile_size\(\)](modules/dialog/dialog.md#ksrdialogget_profile_size)
* [KSR.dialog.get_profile_size_static\(\)](modules/dialog/dialog.md#ksrdialogget_profile_size_static)
* [KSR.dialog.is_in_profile\(\)](modules/dialog/dialog.md#ksrdialogis_in_profile)
* [KSR.dialog.is_in_profile_static\(\)](modules/dialog/dialog.md#ksrdialogis_in_profile_static)
* [KSR.dialog.is_known_dlg\(\)](modules/dialog/dialog.md#ksrdialogis_known_dlg)
* [KSR.dialog.set_dlg_profile\(\)](modules/dialog/dialog.md#ksrdialogset_dlg_profile)
* [KSR.dialog.set_dlg_profile_static\(\)](modules/dialog/dialog.md#ksrdialogset_dlg_profile_static)
* [KSR.dialog.unset_dlg_profile\(\)](modules/dialog/dialog.md#ksrdialogunset_dlg_profile)
* [KSR.dialog.unset_dlg_profile_static\(\)](modules/dialog/dialog.md#ksrdialogunset_dlg_profile_static)
* [KSR.dialog.var_get\(\)](modules/dialog/dialog.md#ksrdialogvar_get)
* [KSR.dialog.var_gete\(\)](modules/dialog/dialog.md#ksrdialogvar_gete)
* [KSR.dialog.var_getw\(\)](modules/dialog/dialog.md#ksrdialogvar_getw)
* [KSR.dialog.var_is_null\(\)](modules/dialog/dialog.md#ksrdialogvar_is_null)
* [KSR.dialog.var_rm\(\)](modules/dialog/dialog.md#ksrdialogvar_rm)
* [KSR.dialog.var_sets\(\)](modules/dialog/dialog.md#ksrdialogvar_sets)

## dialplan ##

* 📖[kamailio.cfg::module::dialplan.html](https://kamailio.org/docs/modules/devel/modules/dialplan.html)

Exported functions:

* [KSR.dialplan.dp_match\(\)](modules/dialplan/dialplan.md#ksrdialplandp_match)
* [KSR.dialplan.dp_replace\(\)](modules/dialplan/dialplan.md#ksrdialplandp_replace)
* [KSR.dialplan.dp_translate\(\)](modules/dialplan/dialplan.md#ksrdialplandp_translate)
* [KSR.dialplan.dp_translate_vars\(\)](modules/dialplan/dialplan.md#ksrdialplandp_translate_vars)

## dispatcher ##

* 📖[kamailio.cfg::module::dispatcher.html](https://kamailio.org/docs/modules/devel/modules/dispatcher.html)

Exported functions:

* [KSR.dispatcher.ds_is_active\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_active)
* [KSR.dispatcher.ds_is_active_uri\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_active_uri)
* [KSR.dispatcher.ds_is_from_list\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_from_list)
* [KSR.dispatcher.ds_is_from_list_mode\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_from_list_mode)
* [KSR.dispatcher.ds_is_from_list_uri\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_from_list_uri)
* [KSR.dispatcher.ds_is_from_lists\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_is_from_lists)
* [KSR.dispatcher.ds_list_exists\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_list_exists)
* [KSR.dispatcher.ds_load_unset\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_load_unset)
* [KSR.dispatcher.ds_load_unset_callid\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_load_unset_callid)
* [KSR.dispatcher.ds_load_update\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_load_update)
* [KSR.dispatcher.ds_mark_addr\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_mark_addr)
* [KSR.dispatcher.ds_mark_dst\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_mark_dst)
* [KSR.dispatcher.ds_mark_dst_state\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_mark_dst_state)
* [KSR.dispatcher.ds_next_domain\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_next_domain)
* [KSR.dispatcher.ds_next_dst\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_next_dst)
* [KSR.dispatcher.ds_reload\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_reload)
* [KSR.dispatcher.ds_select\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select)
* [KSR.dispatcher.ds_select_dns\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_dns)
* [KSR.dispatcher.ds_select_dns_limit\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_dns_limit)
* [KSR.dispatcher.ds_select_domain\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_domain)
* [KSR.dispatcher.ds_select_domain_limit\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_domain_limit)
* [KSR.dispatcher.ds_select_dst\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_dst)
* [KSR.dispatcher.ds_select_dst_limit\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_dst_limit)
* [KSR.dispatcher.ds_select_limit\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_limit)
* [KSR.dispatcher.ds_select_routes\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_routes)
* [KSR.dispatcher.ds_select_routes_limit\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_select_routes_limit)
* [KSR.dispatcher.ds_set_domain\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_set_domain)
* [KSR.dispatcher.ds_set_dst\(\)](modules/dispatcher/dispatcher.md#ksrdispatcherds_set_dst)

## diversion ##

* 📖[kamailio.cfg::module::diversion.html](https://kamailio.org/docs/modules/devel/modules/diversion.html)

Exported functions:

* [KSR.diversion.add_diversion\(\)](modules/diversion/diversion.md#ksrdiversionadd_diversion)
* [KSR.diversion.add_diversion_uri\(\)](modules/diversion/diversion.md#ksrdiversionadd_diversion_uri)

## dlgs ##

* 📖[kamailio.cfg::module::dlgs.html](https://kamailio.org/docs/modules/devel/modules/dlgs.html)

Exported functions:

* [KSR.dlgs.dlgs_count\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_count)
* [KSR.dlgs.dlgs_find\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_find)
* [KSR.dlgs.dlgs_init\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_init)
* [KSR.dlgs.dlgs_tags_add\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_tags_add)
* [KSR.dlgs.dlgs_tags_count\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_tags_count)
* [KSR.dlgs.dlgs_tags_rm\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_tags_rm)
* [KSR.dlgs.dlgs_update\(\)](modules/dlgs/dlgs.md#ksrdlgsdlgs_update)

## dmq ##

* 📖[kamailio.cfg::module::dmq.html](https://kamailio.org/docs/modules/devel/modules/dmq.html)

Exported functions:

* [KSR.dmq.bcast_message\(\)](modules/dmq/dmq.md#ksrdmqbcast_message)
* [KSR.dmq.handle_custom_message\(\)](modules/dmq/dmq.md#ksrdmqhandle_custom_message)
* [KSR.dmq.handle_message\(\)](modules/dmq/dmq.md#ksrdmqhandle_message)
* [KSR.dmq.handle_message_rc\(\)](modules/dmq/dmq.md#ksrdmqhandle_message_rc)
* [KSR.dmq.is_from_node\(\)](modules/dmq/dmq.md#ksrdmqis_from_node)
* [KSR.dmq.process_custom_message\(\)](modules/dmq/dmq.md#ksrdmqprocess_custom_message)
* [KSR.dmq.process_message\(\)](modules/dmq/dmq.md#ksrdmqprocess_message)
* [KSR.dmq.process_message_rc\(\)](modules/dmq/dmq.md#ksrdmqprocess_message_rc)
* [KSR.dmq.send_message\(\)](modules/dmq/dmq.md#ksrdmqsend_message)
* [KSR.dmq.t_replicate\(\)](modules/dmq/dmq.md#ksrdmqt_replicate)
* [KSR.dmq.t_replicate_mode\(\)](modules/dmq/dmq.md#ksrdmqt_replicate_mode)

## domain ##

* 📖[kamailio.cfg::module::domain.html](https://kamailio.org/docs/modules/devel/modules/domain.html)

Exported functions:

* [KSR.domain.is_domain_local\(\)](modules/domain/domain.md#ksrdomainis_domain_local)
* [KSR.domain.is_from_local\(\)](modules/domain/domain.md#ksrdomainis_from_local)
* [KSR.domain.is_uri_host_local\(\)](modules/domain/domain.md#ksrdomainis_uri_host_local)
* [KSR.domain.lookup_domain\(\)](modules/domain/domain.md#ksrdomainlookup_domain)
* [KSR.domain.lookup_domain_prefix\(\)](modules/domain/domain.md#ksrdomainlookup_domain_prefix)

## drouting ##

* 📖[kamailio.cfg::module::drouting.html](https://kamailio.org/docs/modules/devel/modules/drouting.html)

Exported functions:

* [KSR.drouting.do_routing\(\)](modules/drouting/drouting.md#ksrdroutingdo_routing)
* [KSR.drouting.do_routing_furi\(\)](modules/drouting/drouting.md#ksrdroutingdo_routing_furi)
* [KSR.drouting.goes_to_gw\(\)](modules/drouting/drouting.md#ksrdroutinggoes_to_gw)
* [KSR.drouting.goes_to_gw_type\(\)](modules/drouting/drouting.md#ksrdroutinggoes_to_gw_type)
* [KSR.drouting.is_from_gw\(\)](modules/drouting/drouting.md#ksrdroutingis_from_gw)
* [KSR.drouting.is_from_gw_type\(\)](modules/drouting/drouting.md#ksrdroutingis_from_gw_type)
* [KSR.drouting.is_from_gw_type_flags\(\)](modules/drouting/drouting.md#ksrdroutingis_from_gw_type_flags)
* [KSR.drouting.next_routing\(\)](modules/drouting/drouting.md#ksrdroutingnext_routing)
* [KSR.drouting.use_next_gw\(\)](modules/drouting/drouting.md#ksrdroutinguse_next_gw)

## enum ##

* 📖[kamailio.cfg::module::enum.html](https://kamailio.org/docs/modules/devel/modules/enum.html)

Exported functions:

* [KSR.enum.enum_i_query_suffix\(\)](modules/enum/enum.md#ksrenumenum_i_query_suffix)
* [KSR.enum.enum_pv_query\(\)](modules/enum/enum.md#ksrenumenum_pv_query)
* [KSR.enum.enum_pv_query_suffix\(\)](modules/enum/enum.md#ksrenumenum_pv_query_suffix)
* [KSR.enum.enum_pv_query_suffix_service\(\)](modules/enum/enum.md#ksrenumenum_pv_query_suffix_service)
* [KSR.enum.enum_query\(\)](modules/enum/enum.md#ksrenumenum_query)
* [KSR.enum.enum_query_suffix\(\)](modules/enum/enum.md#ksrenumenum_query_suffix)
* [KSR.enum.enum_query_suffix_service\(\)](modules/enum/enum.md#ksrenumenum_query_suffix_service)
* [KSR.enum.i_enum_query\(\)](modules/enum/enum.md#ksrenumi_enum_query)
* [KSR.enum.i_enum_query_suffix_service\(\)](modules/enum/enum.md#ksrenumi_enum_query_suffix_service)
* [KSR.enum.is_from_user_enum\(\)](modules/enum/enum.md#ksrenumis_from_user_enum)
* [KSR.enum.is_from_user_enum_suffix\(\)](modules/enum/enum.md#ksrenumis_from_user_enum_suffix)
* [KSR.enum.is_from_user_enum_suffix_service\(\)](modules/enum/enum.md#ksrenumis_from_user_enum_suffix_service)

## evapi ##

* 📖[kamailio.cfg::module::evapi.html](https://kamailio.org/docs/modules/devel/modules/evapi.html)

Exported functions:

* [KSR.evapi.async_multicast\(\)](modules/evapi/evapi.md#ksrevapiasync_multicast)
* [KSR.evapi.async_relay\(\)](modules/evapi/evapi.md#ksrevapiasync_relay)
* [KSR.evapi.async_unicast\(\)](modules/evapi/evapi.md#ksrevapiasync_unicast)
* [KSR.evapi.close\(\)](modules/evapi/evapi.md#ksrevapiclose)
* [KSR.evapi.relay\(\)](modules/evapi/evapi.md#ksrevapirelay)
* [KSR.evapi.relay_multicast\(\)](modules/evapi/evapi.md#ksrevapirelay_multicast)
* [KSR.evapi.relay_unicast\(\)](modules/evapi/evapi.md#ksrevapirelay_unicast)
* [KSR.evapi.set_tag\(\)](modules/evapi/evapi.md#ksrevapiset_tag)

## exec ##

* 📖[kamailio.cfg::module::exec.html](https://kamailio.org/docs/modules/devel/modules/exec.html)

Exported functions:

* [KSR.exec.exec_avp\(\)](modules/exec/exec.md#ksrexecexec_avp)
* [KSR.exec.exec_cmd\(\)](modules/exec/exec.md#ksrexecexec_cmd)
* [KSR.exec.exec_dset\(\)](modules/exec/exec.md#ksrexecexec_dset)
* [KSR.exec.exec_msg\(\)](modules/exec/exec.md#ksrexecexec_msg)

## gcrypt ##

* 📖[kamailio.cfg::module::gcrypt.html](https://kamailio.org/docs/modules/devel/modules/gcrypt.html)

Exported functions:

* [KSR.gcrypt.aes_decrypt\(\)](modules/gcrypt/gcrypt.md#ksrgcryptaes_decrypt)
* [KSR.gcrypt.aes_encrypt\(\)](modules/gcrypt/gcrypt.md#ksrgcryptaes_encrypt)
* [KSR.gcrypt.hmac_sha256\(\)](modules/gcrypt/gcrypt.md#ksrgcrypthmac_sha256)
* [KSR.gcrypt.hmac_sha512\(\)](modules/gcrypt/gcrypt.md#ksrgcrypthmac_sha512)

## geoip ##

* 📖[kamailio.cfg::module::geoip.html](https://kamailio.org/docs/modules/devel/modules/geoip.html)

Exported functions:

* [KSR.geoip.match\(\)](modules/geoip/geoip.md#ksrgeoipmatch)

## geoip2 ##

* 📖[kamailio.cfg::module::geoip2.html](https://kamailio.org/docs/modules/devel/modules/geoip2.html)

Exported functions:

* [KSR.geoip2.distance\(\)](modules/geoip2/geoip2.md#ksrgeoip2distance)
* [KSR.geoip2.match\(\)](modules/geoip2/geoip2.md#ksrgeoip2match)

## group ##

* 📖[kamailio.cfg::module::group.html](https://kamailio.org/docs/modules/devel/modules/group.html)

Exported functions:

* [KSR.group.is_user_in\(\)](modules/group/group.md#ksrgroupis_user_in)

## htable ##

* 📖[kamailio.cfg::module::htable.html](https://kamailio.org/docs/modules/devel/modules/htable.html)

Functions exported by `htable` module.

Exported functions:

* [KSR.htable.sht_cn\(\)](modules/htable/htable.md#ksrhtablesht_cn)
* [KSR.htable.sht_dec\(\)](modules/htable/htable.md#ksrhtablesht_dec)
* [KSR.htable.sht_get\(\)](modules/htable/htable.md#ksrhtablesht_get)
* [KSR.htable.sht_gete\(\)](modules/htable/htable.md#ksrhtablesht_gete)
* [KSR.htable.sht_getw\(\)](modules/htable/htable.md#ksrhtablesht_getw)
* [KSR.htable.sht_inc\(\)](modules/htable/htable.md#ksrhtablesht_inc)
* [KSR.htable.sht_is_null\(\)](modules/htable/htable.md#ksrhtablesht_is_null)
* [KSR.htable.sht_iterator_end\(\)](modules/htable/htable.md#ksrhtablesht_iterator_end)
* [KSR.htable.sht_iterator_next\(\)](modules/htable/htable.md#ksrhtablesht_iterator_next)
* [KSR.htable.sht_iterator_rm\(\)](modules/htable/htable.md#ksrhtablesht_iterator_rm)
* [KSR.htable.sht_iterator_setex\(\)](modules/htable/htable.md#ksrhtablesht_iterator_setex)
* [KSR.htable.sht_iterator_seti\(\)](modules/htable/htable.md#ksrhtablesht_iterator_seti)
* [KSR.htable.sht_iterator_sets\(\)](modules/htable/htable.md#ksrhtablesht_iterator_sets)
* [KSR.htable.sht_iterator_start\(\)](modules/htable/htable.md#ksrhtablesht_iterator_start)
* [KSR.htable.sht_lock\(\)](modules/htable/htable.md#ksrhtablesht_lock)
* [KSR.htable.sht_match_name\(\)](modules/htable/htable.md#ksrhtablesht_match_name)
* [KSR.htable.sht_match_str_value\(\)](modules/htable/htable.md#ksrhtablesht_match_str_value)
* [KSR.htable.sht_reset\(\)](modules/htable/htable.md#ksrhtablesht_reset)
* [KSR.htable.sht_rm\(\)](modules/htable/htable.md#ksrhtablesht_rm)
* [KSR.htable.sht_rm_name\(\)](modules/htable/htable.md#ksrhtablesht_rm_name)
* [KSR.htable.sht_rm_name_re\(\)](modules/htable/htable.md#ksrhtablesht_rm_name_re)
* [KSR.htable.sht_rm_value\(\)](modules/htable/htable.md#ksrhtablesht_rm_value)
* [KSR.htable.sht_rm_value_re\(\)](modules/htable/htable.md#ksrhtablesht_rm_value_re)
* [KSR.htable.sht_setex\(\)](modules/htable/htable.md#ksrhtablesht_setex)
* [KSR.htable.sht_seti\(\)](modules/htable/htable.md#ksrhtablesht_seti)
* [KSR.htable.sht_sets\(\)](modules/htable/htable.md#ksrhtablesht_sets)
* [KSR.htable.sht_setxi\(\)](modules/htable/htable.md#ksrhtablesht_setxi)
* [KSR.htable.sht_setxs\(\)](modules/htable/htable.md#ksrhtablesht_setxs)
* [KSR.htable.sht_unlock\(\)](modules/htable/htable.md#ksrhtablesht_unlock)

## http_async_client ##

* 📖[kamailio.cfg::module::http_async_client.html](https://kamailio.org/docs/modules/devel/modules/http_async_client.html)

Exported functions:

* [KSR.http_async_client.query\(\)](modules/http_async_client/http_async_client.md#ksrhttp_async_clientquery)
* [KSR.http_async_client.send\(\)](modules/http_async_client/http_async_client.md#ksrhttp_async_clientsend)
* [KSR.http_async_client.send_xdata\(\)](modules/http_async_client/http_async_client.md#ksrhttp_async_clientsend_xdata)

## http_client ##

* 📖[kamailio.cfg::module::http_client.html](https://kamailio.org/docs/modules/devel/modules/http_client.html)

Exported functions:

* [KSR.http_client.curl_connect\(\)](modules/http_client/http_client.md#ksrhttp_clientcurl_connect)
* [KSR.http_client.curl_connect_post\(\)](modules/http_client/http_client.md#ksrhttp_clientcurl_connect_post)
* [KSR.http_client.get_hdrs\(\)](modules/http_client/http_client.md#ksrhttp_clientget_hdrs)
* [KSR.http_client.query\(\)](modules/http_client/http_client.md#ksrhttp_clientquery)
* [KSR.http_client.query_post\(\)](modules/http_client/http_client.md#ksrhttp_clientquery_post)
* [KSR.http_client.query_post_hdrs\(\)](modules/http_client/http_client.md#ksrhttp_clientquery_post_hdrs)
* [KSR.http_client.query_request\(\)](modules/http_client/http_client.md#ksrhttp_clientquery_request)
* [KSR.http_client.query_request_v2pk\(\)](modules/http_client/http_client.md#ksrhttp_clientquery_request_v2pk)

## imc ##

* 📖[kamailio.cfg::module::imc.html](https://kamailio.org/docs/modules/devel/modules/imc.html)

Exported functions:

* [KSR.imc.imc_manager\(\)](modules/imc/imc.md#ksrimcimc_manager)
* [KSR.imc.imc_room_active\(\)](modules/imc/imc.md#ksrimcimc_room_active)
* [KSR.imc.imc_room_member\(\)](modules/imc/imc.md#ksrimcimc_room_member)

## ims_charging ##

* 📖[kamailio.cfg::module::ims_charging.html](https://kamailio.org/docs/modules/devel/modules/ims_charging.html)

Exported functions:

* [KSR.ims_charging.Ro_CCR\(\)](modules/ims_charging/ims_charging.md#ksrims_chargingro_ccr)
* [KSR.ims_charging.Ro_CCR_Stop\(\)](modules/ims_charging/ims_charging.md#ksrims_chargingro_ccr_stop)
* [KSR.ims_charging.Ro_set_session_id_avp\(\)](modules/ims_charging/ims_charging.md#ksrims_chargingro_set_session_id_avp)

## ims_dialog ##

* 📖[kamailio.cfg::module::ims_dialog.html](https://kamailio.org/docs/modules/devel/modules/ims_dialog.html)

Exported functions:

* [KSR.ims_dialog.get_profile_size\(\)](modules/ims_dialog/ims_dialog.md#ksrims_dialogget_profile_size)
* [KSR.ims_dialog.is_known_dlg\(\)](modules/ims_dialog/ims_dialog.md#ksrims_dialogis_known_dlg)
* [KSR.ims_dialog.set_dlg_profile\(\)](modules/ims_dialog/ims_dialog.md#ksrims_dialogset_dlg_profile)

## ims_diameter_server ##

* 📖[kamailio.cfg::module::ims_diameter_server.html](https://kamailio.org/docs/modules/devel/modules/ims_diameter_server.html)

Exported functions:

* [KSR.ims_diameter_server.diameter_request\(\)](modules/ims_diameter_server/ims_diameter_server.md#ksrims_diameter_serverdiameter_request)
* [KSR.ims_diameter_server.diameter_request_async\(\)](modules/ims_diameter_server/ims_diameter_server.md#ksrims_diameter_serverdiameter_request_async)

## ims_qos ##

* 📖[kamailio.cfg::module::ims_qos.html](https://kamailio.org/docs/modules/devel/modules/ims_qos.html)

Exported functions:

* [KSR.ims_qos.Rx_AAR\(\)](modules/ims_qos/ims_qos.md#ksrims_qosrx_aar)
* [KSR.ims_qos.Rx_AAR\(\)](modules/ims_qos/ims_qos.md#ksrims_qosrx_aar)
* [KSR.ims_qos.Rx_AAR_Register\(\)](modules/ims_qos/ims_qos.md#ksrims_qosrx_aar_register)
* [KSR.ims_qos.Rx_AAR_Register\(\)](modules/ims_qos/ims_qos.md#ksrims_qosrx_aar_register)

## influxdbc ##

* 📖[kamailio.cfg::module::influxdbc.html](https://kamailio.org/docs/modules/devel/modules/influxdbc.html)

Exported functions:

* [KSR.influxdbc.ic_long\(\)](modules/influxdbc/influxdbc.md#ksrinfluxdbcic_long)
* [KSR.influxdbc.measure\(\)](modules/influxdbc/influxdbc.md#ksrinfluxdbcmeasure)
* [KSR.influxdbc.measureend\(\)](modules/influxdbc/influxdbc.md#ksrinfluxdbcmeasureend)
* [KSR.influxdbc.push\(\)](modules/influxdbc/influxdbc.md#ksrinfluxdbcpush)

## ipops ##

* 📖[kamailio.cfg::module::ipops.html](https://kamailio.org/docs/modules/devel/modules/ipops.html)

Exported functions:

* [KSR.ipops.compare_ips\(\)](modules/ipops/ipops.md#ksripopscompare_ips)
* [KSR.ipops.compare_pure_ips\(\)](modules/ipops/ipops.md#ksripopscompare_pure_ips)
* [KSR.ipops.detailed_ip_type\(\)](modules/ipops/ipops.md#ksripopsdetailed_ip_type)
* [KSR.ipops.detailed_ipv4_type\(\)](modules/ipops/ipops.md#ksripopsdetailed_ipv4_type)
* [KSR.ipops.detailed_ipv6_type\(\)](modules/ipops/ipops.md#ksripopsdetailed_ipv6_type)
* [KSR.ipops.dns_int_match_ip\(\)](modules/ipops/ipops.md#ksripopsdns_int_match_ip)
* [KSR.ipops.dns_query\(\)](modules/ipops/ipops.md#ksripopsdns_query)
* [KSR.ipops.dns_set_local_ttl\(\)](modules/ipops/ipops.md#ksripopsdns_set_local_ttl)
* [KSR.ipops.dns_sys_match_ip\(\)](modules/ipops/ipops.md#ksripopsdns_sys_match_ip)
* [KSR.ipops.ip_is_in_subnet\(\)](modules/ipops/ipops.md#ksripopsip_is_in_subnet)
* [KSR.ipops.ip_type\(\)](modules/ipops/ipops.md#ksripopsip_type)
* [KSR.ipops.is_in_subnet\(\)](modules/ipops/ipops.md#ksripopsis_in_subnet)
* [KSR.ipops.is_ip\(\)](modules/ipops/ipops.md#ksripopsis_ip)
* [KSR.ipops.is_ip4\(\)](modules/ipops/ipops.md#ksripopsis_ip4)
* [KSR.ipops.is_ip6\(\)](modules/ipops/ipops.md#ksripopsis_ip6)
* [KSR.ipops.is_ip6_reference\(\)](modules/ipops/ipops.md#ksripopsis_ip6_reference)
* [KSR.ipops.is_ip_rfc1918\(\)](modules/ipops/ipops.md#ksripopsis_ip_rfc1918)
* [KSR.ipops.is_pure_ip\(\)](modules/ipops/ipops.md#ksripopsis_pure_ip)
* [KSR.ipops.naptr_query\(\)](modules/ipops/ipops.md#ksripopsnaptr_query)
* [KSR.ipops.ptr_query\(\)](modules/ipops/ipops.md#ksripopsptr_query)
* [KSR.ipops.srv_query\(\)](modules/ipops/ipops.md#ksripopssrv_query)

## jansson ##

* 📖[kamailio.cfg::module::jansson.html](https://kamailio.org/docs/modules/devel/modules/jansson.html)

Exported functions:

* [KSR.jansson.get\(\)](modules/jansson/jansson.md#ksrjanssonget)

## jsonrpcs ##

* 📖[kamailio.cfg::module::jsonrpcs.html](https://kamailio.org/docs/modules/devel/modules/jsonrpcs.html)

Exported functions:

* [KSR.jsonrpcs.dispatch\(\)](modules/jsonrpcs/jsonrpcs.md#ksrjsonrpcsdispatch)
* [KSR.jsonrpcs.exec\(\)](modules/jsonrpcs/jsonrpcs.md#ksrjsonrpcsexec)
* [KSR.jsonrpcs.execx\(\)](modules/jsonrpcs/jsonrpcs.md#ksrjsonrpcsexecx)
* [KSR.jsonrpcs.response\(\)](modules/jsonrpcs/jsonrpcs.md#ksrjsonrpcsresponse)

## jwt ##

* 📖[kamailio.cfg::module::jwt.html](https://kamailio.org/docs/modules/devel/modules/jwt.html)

Exported functions:

* [KSR.jwt.jwt_generate\(\)](modules/jwt/jwt.md#ksrjwtjwt_generate)
* [KSR.jwt.jwt_generate_hdrs\(\)](modules/jwt/jwt.md#ksrjwtjwt_generate_hdrs)
* [KSR.jwt.jwt_verify\(\)](modules/jwt/jwt.md#ksrjwtjwt_verify)
* [KSR.jwt.jwt_verify_key\(\)](modules/jwt/jwt.md#ksrjwtjwt_verify_key)

## jwt3 ##

* 📖[kamailio.cfg::module::jwt3.html](https://kamailio.org/docs/modules/devel/modules/jwt3.html)

Exported functions:

* [KSR.jwt3.jwt3_generate\(\)](modules/jwt3/jwt3.md#ksrjwt3jwt3_generate)
* [KSR.jwt3.jwt3_generate_hdrs\(\)](modules/jwt3/jwt3.md#ksrjwt3jwt3_generate_hdrs)
* [KSR.jwt3.jwt3_verify\(\)](modules/jwt3/jwt3.md#ksrjwt3jwt3_verify)
* [KSR.jwt3.jwt3_verify_key\(\)](modules/jwt3/jwt3.md#ksrjwt3jwt3_verify_key)

## kafka ##

* 📖[kamailio.cfg::module::kafka.html](https://kamailio.org/docs/modules/devel/modules/kafka.html)

Exported functions:

* [KSR.kafka.send\(\)](modules/kafka/kafka.md#ksrkafkasend)
* [KSR.kafka.send_key\(\)](modules/kafka/kafka.md#ksrkafkasend_key)

## kazoo ##

* 📖[kamailio.cfg::module::kazoo.html](https://kamailio.org/docs/modules/devel/modules/kazoo.html)

Exported functions:

* [KSR.kazoo.kazoo_publish\(\)](modules/kazoo/kazoo.md#ksrkazookazoo_publish)
* [KSR.kazoo.kazoo_subscribe\(\)](modules/kazoo/kazoo.md#ksrkazookazoo_subscribe)

## keepalive ##

* 📖[kamailio.cfg::module::keepalive.html](https://kamailio.org/docs/modules/devel/modules/keepalive.html)

Exported functions:

* [KSR.keepalive.add_destination\(\)](modules/keepalive/keepalive.md#ksrkeepaliveadd_destination)
* [KSR.keepalive.del_destination\(\)](modules/keepalive/keepalive.md#ksrkeepalivedel_destination)
* [KSR.keepalive.is_alive\(\)](modules/keepalive/keepalive.md#ksrkeepaliveis_alive)

## kex ##

* 📖[kamailio.cfg::module::kex.html](https://kamailio.org/docs/modules/devel/modules/kex.html)

Exported functions:

* [KSR.kex.resetdebug\(\)](modules/kex/kex.md#ksrkexresetdebug)
* [KSR.kex.setdebug\(\)](modules/kex/kex.md#ksrkexsetdebug)

## kx ##

* 📖[kamailio.cfg::module::kemi.html](https://kamailio.org/docs/modules/devel/modules/kemi.html)

Functions exported by `kemix` module and available in KEMI language under
`KSR.kx`. They aim to provide a convenient way to retrieve string or integer
values for most commonly used variables or runtime environment attributes.

Exported functions:

* [KSR.kx.get_au\(\)](modules/kx/kx.md#ksrkxget_au)
* [KSR.kx.get_body\(\)](modules/kx/kx.md#ksrkxget_body)
* [KSR.kx.get_bodylen\(\)](modules/kx/kx.md#ksrkxget_bodylen)
* [KSR.kx.get_callid\(\)](modules/kx/kx.md#ksrkxget_callid)
* [KSR.kx.get_conid\(\)](modules/kx/kx.md#ksrkxget_conid)
* [KSR.kx.get_cturi\(\)](modules/kx/kx.md#ksrkxget_cturi)
* [KSR.kx.get_def\(\)](modules/kx/kx.md#ksrkxget_def)
* [KSR.kx.get_defn\(\)](modules/kx/kx.md#ksrkxget_defn)
* [KSR.kx.get_duri\(\)](modules/kx/kx.md#ksrkxget_duri)
* [KSR.kx.get_env\(\)](modules/kx/kx.md#ksrkxget_env)
* [KSR.kx.get_envn\(\)](modules/kx/kx.md#ksrkxget_envn)
* [KSR.kx.get_fhost\(\)](modules/kx/kx.md#ksrkxget_fhost)
* [KSR.kx.get_furi\(\)](modules/kx/kx.md#ksrkxget_furi)
* [KSR.kx.get_fuser\(\)](modules/kx/kx.md#ksrkxget_fuser)
* [KSR.kx.get_method\(\)](modules/kx/kx.md#ksrkxget_method)
* [KSR.kx.get_msgbuf\(\)](modules/kx/kx.md#ksrkxget_msgbuf)
* [KSR.kx.get_msglen\(\)](modules/kx/kx.md#ksrkxget_msglen)
* [KSR.kx.get_msgtype\(\)](modules/kx/kx.md#ksrkxget_msgtype)
* [KSR.kx.get_nhuri\(\)](modules/kx/kx.md#ksrkxget_nhuri)
* [KSR.kx.get_ouri\(\)](modules/kx/kx.md#ksrkxget_ouri)
* [KSR.kx.get_proto\(\)](modules/kx/kx.md#ksrkxget_proto)
* [KSR.kx.get_protoid\(\)](modules/kx/kx.md#ksrkxget_protoid)
* [KSR.kx.get_rcv_sock_name\(\)](modules/kx/kx.md#ksrkxget_rcv_sock_name)
* [KSR.kx.get_rcvaddr_sock\(\)](modules/kx/kx.md#ksrkxget_rcvaddr_sock)
* [KSR.kx.get_rcvadvip\(\)](modules/kx/kx.md#ksrkxget_rcvadvip)
* [KSR.kx.get_rcvadvport\(\)](modules/kx/kx.md#ksrkxget_rcvadvport)
* [KSR.kx.get_rcvip\(\)](modules/kx/kx.md#ksrkxget_rcvip)
* [KSR.kx.get_rcvport\(\)](modules/kx/kx.md#ksrkxget_rcvport)
* [KSR.kx.get_rhost\(\)](modules/kx/kx.md#ksrkxget_rhost)
* [KSR.kx.get_ruri\(\)](modules/kx/kx.md#ksrkxget_ruri)
* [KSR.kx.get_ruser\(\)](modules/kx/kx.md#ksrkxget_ruser)
* [KSR.kx.get_send_sock\(\)](modules/kx/kx.md#ksrkxget_send_sock)
* [KSR.kx.get_send_sock_name\(\)](modules/kx/kx.md#ksrkxget_send_sock_name)
* [KSR.kx.get_send_sock_port\(\)](modules/kx/kx.md#ksrkxget_send_sock_port)
* [KSR.kx.get_srcaddr_sock\(\)](modules/kx/kx.md#ksrkxget_srcaddr_sock)
* [KSR.kx.get_srcip\(\)](modules/kx/kx.md#ksrkxget_srcip)
* [KSR.kx.get_srcport\(\)](modules/kx/kx.md#ksrkxget_srcport)
* [KSR.kx.get_srcuri\(\)](modules/kx/kx.md#ksrkxget_srcuri)
* [KSR.kx.get_status\(\)](modules/kx/kx.md#ksrkxget_status)
* [KSR.kx.get_thost\(\)](modules/kx/kx.md#ksrkxget_thost)
* [KSR.kx.get_timestamp\(\)](modules/kx/kx.md#ksrkxget_timestamp)
* [KSR.kx.get_turi\(\)](modules/kx/kx.md#ksrkxget_turi)
* [KSR.kx.get_tuser\(\)](modules/kx/kx.md#ksrkxget_tuser)
* [KSR.kx.get_ua\(\)](modules/kx/kx.md#ksrkxget_ua)
* [KSR.kx.gete_au\(\)](modules/kx/kx.md#ksrkxgete_au)
* [KSR.kx.gete_body\(\)](modules/kx/kx.md#ksrkxgete_body)
* [KSR.kx.gete_cturi\(\)](modules/kx/kx.md#ksrkxgete_cturi)
* [KSR.kx.gete_duri\(\)](modules/kx/kx.md#ksrkxgete_duri)
* [KSR.kx.gete_fhost\(\)](modules/kx/kx.md#ksrkxgete_fhost)
* [KSR.kx.gete_fuser\(\)](modules/kx/kx.md#ksrkxgete_fuser)
* [KSR.kx.gete_rhost\(\)](modules/kx/kx.md#ksrkxgete_rhost)
* [KSR.kx.gete_ruser\(\)](modules/kx/kx.md#ksrkxgete_ruser)
* [KSR.kx.gete_thost\(\)](modules/kx/kx.md#ksrkxgete_thost)
* [KSR.kx.gete_tuser\(\)](modules/kx/kx.md#ksrkxgete_tuser)
* [KSR.kx.gete_ua\(\)](modules/kx/kx.md#ksrkxgete_ua)
* [KSR.kx.gets_status\(\)](modules/kx/kx.md#ksrkxgets_status)
* [KSR.kx.getw_au\(\)](modules/kx/kx.md#ksrkxgetw_au)
* [KSR.kx.getw_body\(\)](modules/kx/kx.md#ksrkxgetw_body)
* [KSR.kx.getw_cturi\(\)](modules/kx/kx.md#ksrkxgetw_cturi)
* [KSR.kx.getw_duri\(\)](modules/kx/kx.md#ksrkxgetw_duri)
* [KSR.kx.getw_fhost\(\)](modules/kx/kx.md#ksrkxgetw_fhost)
* [KSR.kx.getw_fuser\(\)](modules/kx/kx.md#ksrkxgetw_fuser)
* [KSR.kx.getw_rhost\(\)](modules/kx/kx.md#ksrkxgetw_rhost)
* [KSR.kx.getw_ruser\(\)](modules/kx/kx.md#ksrkxgetw_ruser)
* [KSR.kx.getw_thost\(\)](modules/kx/kx.md#ksrkxgetw_thost)
* [KSR.kx.getw_tuser\(\)](modules/kx/kx.md#ksrkxgetw_tuser)
* [KSR.kx.getw_ua\(\)](modules/kx/kx.md#ksrkxgetw_ua)
* [KSR.kx.ifdef\(\)](modules/kx/kx.md#ksrkxifdef)
* [KSR.kx.ifndef\(\)](modules/kx/kx.md#ksrkxifndef)

## lcr ##

* 📖[kamailio.cfg::module::lcr.html](https://kamailio.org/docs/modules/devel/modules/lcr.html)

Exported functions:

* [KSR.lcr.defunct_gw\(\)](modules/lcr/lcr.md#ksrlcrdefunct_gw)
* [KSR.lcr.from_any_gw\(\)](modules/lcr/lcr.md#ksrlcrfrom_any_gw)
* [KSR.lcr.from_any_gw_addr\(\)](modules/lcr/lcr.md#ksrlcrfrom_any_gw_addr)
* [KSR.lcr.from_any_gw_addr_port\(\)](modules/lcr/lcr.md#ksrlcrfrom_any_gw_addr_port)
* [KSR.lcr.from_gw\(\)](modules/lcr/lcr.md#ksrlcrfrom_gw)
* [KSR.lcr.from_gw_addr\(\)](modules/lcr/lcr.md#ksrlcrfrom_gw_addr)
* [KSR.lcr.from_gw_addr_port\(\)](modules/lcr/lcr.md#ksrlcrfrom_gw_addr_port)
* [KSR.lcr.inactivate_gw\(\)](modules/lcr/lcr.md#ksrlcrinactivate_gw)
* [KSR.lcr.load_gws\(\)](modules/lcr/lcr.md#ksrlcrload_gws)
* [KSR.lcr.load_gws_furi\(\)](modules/lcr/lcr.md#ksrlcrload_gws_furi)
* [KSR.lcr.load_gws_ruser\(\)](modules/lcr/lcr.md#ksrlcrload_gws_ruser)
* [KSR.lcr.next_gw\(\)](modules/lcr/lcr.md#ksrlcrnext_gw)
* [KSR.lcr.to_any_gw\(\)](modules/lcr/lcr.md#ksrlcrto_any_gw)
* [KSR.lcr.to_any_gw_addr\(\)](modules/lcr/lcr.md#ksrlcrto_any_gw_addr)
* [KSR.lcr.to_gw\(\)](modules/lcr/lcr.md#ksrlcrto_gw)
* [KSR.lcr.to_gw_addr\(\)](modules/lcr/lcr.md#ksrlcrto_gw_addr)

## ldap ##

* 📖[kamailio.cfg::module::ldap.html](https://kamailio.org/docs/modules/devel/modules/ldap.html)

Exported functions:

* [KSR.ldap.result_next\(\)](modules/ldap/ldap.md#ksrldapresult_next)
* [KSR.ldap.search\(\)](modules/ldap/ldap.md#ksrldapsearch)

## log_custom ##

* 📖[kamailio.cfg::module::log_custom.html](https://kamailio.org/docs/modules/devel/modules/log_custom.html)

Exported functions:

* [KSR.log_custom.log_udp\(\)](modules/log_custom/log_custom.md#ksrlog_customlog_udp)

## log_systemd ##

* 📖[kamailio.cfg::module::log_systemd.html](https://kamailio.org/docs/modules/devel/modules/log_systemd.html)

Exported functions:

* [KSR.log_systemd.sd_journal_print\(\)](modules/log_systemd/log_systemd.md#ksrlog_systemdsd_journal_print)
* [KSR.log_systemd.sd_journal_send_xvap\(\)](modules/log_systemd/log_systemd.md#ksrlog_systemdsd_journal_send_xvap)

## lwsc ##

* 📖[kamailio.cfg::module::lwsc.html](https://kamailio.org/docs/modules/devel/modules/lwsc.html)

Exported functions:

* [KSR.lwsc.lwsc_notify\(\)](modules/lwsc/lwsc.md#ksrlwsclwsc_notify)
* [KSR.lwsc.lwsc_notify_proto\(\)](modules/lwsc/lwsc.md#ksrlwsclwsc_notify_proto)
* [KSR.lwsc.lwsc_request\(\)](modules/lwsc/lwsc.md#ksrlwsclwsc_request)
* [KSR.lwsc.lwsc_request_proto\(\)](modules/lwsc/lwsc.md#ksrlwsclwsc_request_proto)

## maxfwd ##

* 📖[kamailio.cfg::module::maxfwd.html](https://kamailio.org/docs/modules/devel/modules/maxfwd.html)

Exported functions:

* [KSR.maxfwd.is_maxfwd_lt\(\)](modules/maxfwd/maxfwd.md#ksrmaxfwdis_maxfwd_lt)
* [KSR.maxfwd.process_maxfwd\(\)](modules/maxfwd/maxfwd.md#ksrmaxfwdprocess_maxfwd)

## mediaproxy ##

* 📖[kamailio.cfg::module::mediaproxy.html](https://kamailio.org/docs/modules/devel/modules/mediaproxy.html)

Exported functions:

* [KSR.mediaproxy.end_media_session\(\)](modules/mediaproxy/mediaproxy.md#ksrmediaproxyend_media_session)
* [KSR.mediaproxy.engage_media_proxy\(\)](modules/mediaproxy/mediaproxy.md#ksrmediaproxyengage_media_proxy)
* [KSR.mediaproxy.use_media_proxy\(\)](modules/mediaproxy/mediaproxy.md#ksrmediaproxyuse_media_proxy)

## microhttpd ##

* 📖[kamailio.cfg::module::microhttpd.html](https://kamailio.org/docs/modules/devel/modules/microhttpd.html)

Exported functions:

* [KSR.microhttpd.mhttpd_reply\(\)](modules/microhttpd/microhttpd.md#ksrmicrohttpdmhttpd_reply)

## misc_radius ##

* 📖[kamailio.cfg::module::misc_radius.html](https://kamailio.org/docs/modules/devel/modules/misc_radius.html)

Exported functions:

* [KSR.misc_radius.does_uri_exist\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusdoes_uri_exist)
* [KSR.misc_radius.does_uri_exist_uval\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusdoes_uri_exist_uval)
* [KSR.misc_radius.does_uri_user_exist\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusdoes_uri_user_exist)
* [KSR.misc_radius.does_uri_user_exist_uval\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusdoes_uri_user_exist_uval)
* [KSR.misc_radius.is_user_in\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusis_user_in)
* [KSR.misc_radius.load_callee_avps\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusload_callee_avps)
* [KSR.misc_radius.load_caller_avps\(\)](modules/misc_radius/misc_radius.md#ksrmisc_radiusload_caller_avps)

## mqtt ##

* 📖[kamailio.cfg::module::mqtt.html](https://kamailio.org/docs/modules/devel/modules/mqtt.html)

Exported functions:

* [KSR.mqtt.publish\(\)](modules/mqtt/mqtt.md#ksrmqttpublish)
* [KSR.mqtt.subscribe\(\)](modules/mqtt/mqtt.md#ksrmqttsubscribe)
* [KSR.mqtt.unsubscribe\(\)](modules/mqtt/mqtt.md#ksrmqttunsubscribe)

## mqueue ##

* 📖[kamailio.cfg::module::mqueue.html](https://kamailio.org/docs/modules/devel/modules/mqueue.html)

Exported functions:

* [KSR.mqueue.mq_add\(\)](modules/mqueue/mqueue.md#ksrmqueuemq_add)
* [KSR.mqueue.mq_fetch\(\)](modules/mqueue/mqueue.md#ksrmqueuemq_fetch)
* [KSR.mqueue.mq_pv_free\(\)](modules/mqueue/mqueue.md#ksrmqueuemq_pv_free)
* [KSR.mqueue.mq_size\(\)](modules/mqueue/mqueue.md#ksrmqueuemq_size)
* [KSR.mqueue.mqk_get\(\)](modules/mqueue/mqueue.md#ksrmqueuemqk_get)
* [KSR.mqueue.mqk_gete\(\)](modules/mqueue/mqueue.md#ksrmqueuemqk_gete)
* [KSR.mqueue.mqk_getw\(\)](modules/mqueue/mqueue.md#ksrmqueuemqk_getw)
* [KSR.mqueue.mqv_get\(\)](modules/mqueue/mqueue.md#ksrmqueuemqv_get)
* [KSR.mqueue.mqv_gete\(\)](modules/mqueue/mqueue.md#ksrmqueuemqv_gete)
* [KSR.mqueue.mqv_getw\(\)](modules/mqueue/mqueue.md#ksrmqueuemqv_getw)

## msilo ##

* 📖[kamailio.cfg::module::msilo.html](https://kamailio.org/docs/modules/devel/modules/msilo.html)

Exported functions:

* [KSR.msilo.mdump\(\)](modules/msilo/msilo.md#ksrmsilomdump)
* [KSR.msilo.mdump_uri\(\)](modules/msilo/msilo.md#ksrmsilomdump_uri)
* [KSR.msilo.mstore\(\)](modules/msilo/msilo.md#ksrmsilomstore)
* [KSR.msilo.mstore_addrs\(\)](modules/msilo/msilo.md#ksrmsilomstore_addrs)
* [KSR.msilo.mstore_uri\(\)](modules/msilo/msilo.md#ksrmsilomstore_uri)

## msrp ##

* 📖[kamailio.cfg::module::msrp.html](https://kamailio.org/docs/modules/devel/modules/msrp.html)

Exported functions:

* [KSR.msrp.cmap_lookup\(\)](modules/msrp/msrp.md#ksrmsrpcmap_lookup)
* [KSR.msrp.cmap_save\(\)](modules/msrp/msrp.md#ksrmsrpcmap_save)
* [KSR.msrp.forward\(\)](modules/msrp/msrp.md#ksrmsrpforward)
* [KSR.msrp.is_reply\(\)](modules/msrp/msrp.md#ksrmsrpis_reply)
* [KSR.msrp.is_request\(\)](modules/msrp/msrp.md#ksrmsrpis_request)
* [KSR.msrp.relay\(\)](modules/msrp/msrp.md#ksrmsrprelay)
* [KSR.msrp.relay_flags\(\)](modules/msrp/msrp.md#ksrmsrprelay_flags)
* [KSR.msrp.reply\(\)](modules/msrp/msrp.md#ksrmsrpreply)
* [KSR.msrp.reply_flags\(\)](modules/msrp/msrp.md#ksrmsrpreply_flags)
* [KSR.msrp.set_dst\(\)](modules/msrp/msrp.md#ksrmsrpset_dst)

## mtree ##

* 📖[kamailio.cfg::module::mtree.html](https://kamailio.org/docs/modules/devel/modules/mtree.html)

Exported functions:

* [KSR.mtree.mt_match\(\)](modules/mtree/mtree.md#ksrmtreemt_match)

## nat_traversal ##

* 📖[kamailio.cfg::module::nat_traversal.html](https://kamailio.org/docs/modules/devel/modules/nat_traversal.html)

Exported functions:

* [KSR.nat_traversal.client_nat_test\(\)](modules/nat_traversal/nat_traversal.md#ksrnat_traversalclient_nat_test)
* [KSR.nat_traversal.fix_contact\(\)](modules/nat_traversal/nat_traversal.md#ksrnat_traversalfix_contact)
* [KSR.nat_traversal.nat_keepalive\(\)](modules/nat_traversal/nat_traversal.md#ksrnat_traversalnat_keepalive)

## nathelper ##

* 📖[kamailio.cfg::module::nathelper.html](https://kamailio.org/docs/modules/devel/modules/nathelper.html)

Exported functions:

* [KSR.nathelper.add_contact_alias\(\)](modules/nathelper/nathelper.md#ksrnathelperadd_contact_alias)
* [KSR.nathelper.add_contact_alias_addr\(\)](modules/nathelper/nathelper.md#ksrnathelperadd_contact_alias_addr)
* [KSR.nathelper.add_rcv_param\(\)](modules/nathelper/nathelper.md#ksrnathelperadd_rcv_param)
* [KSR.nathelper.fix_nated_contact\(\)](modules/nathelper/nathelper.md#ksrnathelperfix_nated_contact)
* [KSR.nathelper.fix_nated_register\(\)](modules/nathelper/nathelper.md#ksrnathelperfix_nated_register)
* [KSR.nathelper.fix_nated_sdp\(\)](modules/nathelper/nathelper.md#ksrnathelperfix_nated_sdp)
* [KSR.nathelper.fix_nated_sdp_ip\(\)](modules/nathelper/nathelper.md#ksrnathelperfix_nated_sdp_ip)
* [KSR.nathelper.handle_ruri_alias\(\)](modules/nathelper/nathelper.md#ksrnathelperhandle_ruri_alias)
* [KSR.nathelper.handle_ruri_alias_mode\(\)](modules/nathelper/nathelper.md#ksrnathelperhandle_ruri_alias_mode)
* [KSR.nathelper.is_rfc1918\(\)](modules/nathelper/nathelper.md#ksrnathelperis_rfc1918)
* [KSR.nathelper.nat_uac_test\(\)](modules/nathelper/nathelper.md#ksrnathelpernat_uac_test)
* [KSR.nathelper.set_alias_to_pv\(\)](modules/nathelper/nathelper.md#ksrnathelperset_alias_to_pv)
* [KSR.nathelper.set_contact_alias\(\)](modules/nathelper/nathelper.md#ksrnathelperset_contact_alias)
* [KSR.nathelper.set_contact_alias_trim\(\)](modules/nathelper/nathelper.md#ksrnathelperset_contact_alias_trim)

## nats ##

* 📖[kamailio.cfg::module::nats.html](https://kamailio.org/docs/modules/devel/modules/nats.html)

Exported functions:

* [KSR.nats.publish\(\)](modules/nats/nats.md#ksrnatspublish)
* [KSR.nats.publish_request\(\)](modules/nats/nats.md#ksrnatspublish_request)

## ndb_mongodb ##

* 📖[kamailio.cfg::module::ndb_mongodb.html](https://kamailio.org/docs/modules/devel/modules/ndb_mongodb.html)

Exported functions:

* [KSR.ndb_mongodb.exec\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbexec)
* [KSR.ndb_mongodb.exec_simple\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbexec_simple)
* [KSR.ndb_mongodb.execx\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbexecx)
* [KSR.ndb_mongodb.find\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbfind)
* [KSR.ndb_mongodb.find_one\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbfind_one)
* [KSR.ndb_mongodb.free_reply\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbfree_reply)
* [KSR.ndb_mongodb.next_reply\(\)](modules/ndb_mongodb/ndb_mongodb.md#ksrndb_mongodbnext_reply)

## ndb_redis ##

* 📖[kamailio.cfg::module::ndb_redis.html](https://kamailio.org/docs/modules/devel/modules/ndb_redis.html)

Exported functions:

* [KSR.ndb_redis.redis_cmd\(\)](modules/ndb_redis/ndb_redis.md#ksrndb_redisredis_cmd)
* [KSR.ndb_redis.redis_cmd_p1\(\)](modules/ndb_redis/ndb_redis.md#ksrndb_redisredis_cmd_p1)
* [KSR.ndb_redis.redis_cmd_p2\(\)](modules/ndb_redis/ndb_redis.md#ksrndb_redisredis_cmd_p2)
* [KSR.ndb_redis.redis_cmd_p3\(\)](modules/ndb_redis/ndb_redis.md#ksrndb_redisredis_cmd_p3)
* [KSR.ndb_redis.redis_free\(\)](modules/ndb_redis/ndb_redis.md#ksrndb_redisredis_free)

## nghttp2 ##

* 📖[kamailio.cfg::module::nghttp2.html](https://kamailio.org/docs/modules/devel/modules/nghttp2.html)

Exported functions:

* [KSR.nghttp2.nghttp2_reply\(\)](modules/nghttp2/nghttp2.md#ksrnghttp2nghttp2_reply)
* [KSR.nghttp2.nghttp2_reply_header\(\)](modules/nghttp2/nghttp2.md#ksrnghttp2nghttp2_reply_header)

## path ##

* 📖[kamailio.cfg::module::path.html](https://kamailio.org/docs/modules/devel/modules/path.html)

Exported functions:

* [KSR.path.add_path\(\)](modules/path/path.md#ksrpathadd_path)
* [KSR.path.add_path_advertised_address\(\)](modules/path/path.md#ksrpathadd_path_advertised_address)
* [KSR.path.add_path_advertised_address_user\(\)](modules/path/path.md#ksrpathadd_path_advertised_address_user)
* [KSR.path.add_path_advertised_address_user_params\(\)](modules/path/path.md#ksrpathadd_path_advertised_address_user_params)
* [KSR.path.add_path_received\(\)](modules/path/path.md#ksrpathadd_path_received)
* [KSR.path.add_path_received_advertised_address\(\)](modules/path/path.md#ksrpathadd_path_received_advertised_address)
* [KSR.path.add_path_received_advertised_address_user\(\)](modules/path/path.md#ksrpathadd_path_received_advertised_address_user)
* [KSR.path.add_path_received_advertised_address_user_params\(\)](modules/path/path.md#ksrpathadd_path_received_advertised_address_user_params)
* [KSR.path.add_path_received_user\(\)](modules/path/path.md#ksrpathadd_path_received_user)
* [KSR.path.add_path_received_user_params\(\)](modules/path/path.md#ksrpathadd_path_received_user_params)
* [KSR.path.add_path_user\(\)](modules/path/path.md#ksrpathadd_path_user)
* [KSR.path.add_path_user_params\(\)](modules/path/path.md#ksrpathadd_path_user_params)

## pdb ##

* 📖[kamailio.cfg::module::pdb.html](https://kamailio.org/docs/modules/devel/modules/pdb.html)

Exported functions:

* [KSR.pdb.pdb_query\(\)](modules/pdb/pdb.md#ksrpdbpdb_query)

## pdt ##

* 📖[kamailio.cfg::module::pdt.html](https://kamailio.org/docs/modules/devel/modules/pdt.html)

Exported functions:

* [KSR.pdt.pd_translate\(\)](modules/pdt/pdt.md#ksrpdtpd_translate)
* [KSR.pdt.pprefix2domain\(\)](modules/pdt/pdt.md#ksrpdtpprefix2domain)

## permissions ##

* 📖[kamailio.cfg::module::permissions.html](https://kamailio.org/docs/modules/devel/modules/permissions.html)

Exported functions:

* [KSR.permissions.allow_address\(\)](modules/permissions/permissions.md#ksrpermissionsallow_address)
* [KSR.permissions.allow_address_group\(\)](modules/permissions/permissions.md#ksrpermissionsallow_address_group)
* [KSR.permissions.allow_source_address\(\)](modules/permissions/permissions.md#ksrpermissionsallow_source_address)
* [KSR.permissions.allow_source_address_group\(\)](modules/permissions/permissions.md#ksrpermissionsallow_source_address_group)
* [KSR.permissions.allow_trusted\(\)](modules/permissions/permissions.md#ksrpermissionsallow_trusted)

## phonenum ##

* 📖[kamailio.cfg::module::phonenum.html](https://kamailio.org/docs/modules/devel/modules/phonenum.html)

Exported functions:

* [KSR.phonenum.match\(\)](modules/phonenum/phonenum.md#ksrphonenummatch)
* [KSR.phonenum.match_cn\(\)](modules/phonenum/phonenum.md#ksrphonenummatch_cn)

## pike ##

* 📖[kamailio.cfg::module::pike.html](https://kamailio.org/docs/modules/devel/modules/pike.html)

Exported functions:

* [KSR.pike.pike_check_ip\(\)](modules/pike/pike.md#ksrpikepike_check_ip)
* [KSR.pike.pike_check_req\(\)](modules/pike/pike.md#ksrpikepike_check_req)

## pipelimit ##

* 📖[kamailio.cfg::module::pipelimit.html](https://kamailio.org/docs/modules/devel/modules/pipelimit.html)

Exported functions:

* [KSR.pipelimit.pl_active\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_active)
* [KSR.pipelimit.pl_check\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_check)
* [KSR.pipelimit.pl_check_limit\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_check_limit)
* [KSR.pipelimit.pl_drop\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_drop)
* [KSR.pipelimit.pl_drop_range\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_drop_range)
* [KSR.pipelimit.pl_drop_retry\(\)](modules/pipelimit/pipelimit.md#ksrpipelimitpl_drop_retry)

## posops ##

* 📖[kamailio.cfg::module::posops.html](https://kamailio.org/docs/modules/devel/modules/posops.html)

Exported functions:

* [KSR.posops.pos_append\(\)](modules/posops/posops.md#ksrposopspos_append)
* [KSR.posops.pos_body_end\(\)](modules/posops/posops.md#ksrposopspos_body_end)
* [KSR.posops.pos_body_start\(\)](modules/posops/posops.md#ksrposopspos_body_start)
* [KSR.posops.pos_find_str\(\)](modules/posops/posops.md#ksrposopspos_find_str)
* [KSR.posops.pos_findi_str\(\)](modules/posops/posops.md#ksrposopspos_findi_str)
* [KSR.posops.pos_headers_end\(\)](modules/posops/posops.md#ksrposopspos_headers_end)
* [KSR.posops.pos_headers_start\(\)](modules/posops/posops.md#ksrposopspos_headers_start)
* [KSR.posops.pos_insert\(\)](modules/posops/posops.md#ksrposopspos_insert)
* [KSR.posops.pos_rfind_str\(\)](modules/posops/posops.md#ksrposopspos_rfind_str)
* [KSR.posops.pos_rfindi_str\(\)](modules/posops/posops.md#ksrposopspos_rfindi_str)
* [KSR.posops.pos_rm\(\)](modules/posops/posops.md#ksrposopspos_rm)
* [KSR.posops.pos_rsearch\(\)](modules/posops/posops.md#ksrposopspos_rsearch)
* [KSR.posops.pos_search\(\)](modules/posops/posops.md#ksrposopspos_search)
* [KSR.posops.pos_set_char\(\)](modules/posops/posops.md#ksrposopspos_set_char)

## prefix_route ##

* 📖[kamailio.cfg::module::prefix_route.html](https://kamailio.org/docs/modules/devel/modules/prefix_route.html)

Exported functions:

* [KSR.prefix_route.prefix_route\(\)](modules/prefix_route/prefix_route.md#ksrprefix_routeprefix_route)
* [KSR.prefix_route.prefix_route_uri\(\)](modules/prefix_route/prefix_route.md#ksrprefix_routeprefix_route_uri)

## presence ##

* 📖[kamailio.cfg::module::presence.html](https://kamailio.org/docs/modules/devel/modules/presence.html)

Exported functions:

* [KSR.presence.handle_publish\(\)](modules/presence/presence.md#ksrpresencehandle_publish)
* [KSR.presence.handle_publish_uri\(\)](modules/presence/presence.md#ksrpresencehandle_publish_uri)
* [KSR.presence.handle_subscribe\(\)](modules/presence/presence.md#ksrpresencehandle_subscribe)
* [KSR.presence.handle_subscribe_uri\(\)](modules/presence/presence.md#ksrpresencehandle_subscribe_uri)
* [KSR.presence.pres_auth_status\(\)](modules/presence/presence.md#ksrpresencepres_auth_status)
* [KSR.presence.pres_has_subscribers\(\)](modules/presence/presence.md#ksrpresencepres_has_subscribers)
* [KSR.presence.pres_refresh_watchers\(\)](modules/presence/presence.md#ksrpresencepres_refresh_watchers)
* [KSR.presence.pres_refresh_watchers_file\(\)](modules/presence/presence.md#ksrpresencepres_refresh_watchers_file)
* [KSR.presence.pres_update_watchers\(\)](modules/presence/presence.md#ksrpresencepres_update_watchers)

## presence_xml ##

* 📖[kamailio.cfg::module::presence_xml.html](https://kamailio.org/docs/modules/devel/modules/presence_xml.html)

Exported functions:

* [KSR.presence_xml.pres_check_activities\(\)](modules/presence_xml/presence_xml.md#ksrpresence_xmlpres_check_activities)
* [KSR.presence_xml.pres_check_basic\(\)](modules/presence_xml/presence_xml.md#ksrpresence_xmlpres_check_basic)

## pua ##

* 📖[kamailio.cfg::module::pua.html](https://kamailio.org/docs/modules/devel/modules/pua.html)

Exported functions:

* [KSR.pua.pua_set_publish\(\)](modules/pua/pua.md#ksrpuapua_set_publish)
* [KSR.pua.pua_update_contact\(\)](modules/pua/pua.md#ksrpuapua_update_contact)

## pua_json ##

* 📖[kamailio.cfg::module::pua_json.html](https://kamailio.org/docs/modules/devel/modules/pua_json.html)

Exported functions:

* [KSR.pua_json.publish\(\)](modules/pua_json/pua_json.md#ksrpua_jsonpublish)

## pv_headers ##

* 📖[kamailio.cfg::module::pv_headers.html](https://kamailio.org/docs/modules/devel/modules/pv_headers.html)

Exported functions:

* [KSR.pv_headers.pvh_append_header\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_append_header)
* [KSR.pv_headers.pvh_apply_headers\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_apply_headers)
* [KSR.pv_headers.pvh_check_header\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_check_header)
* [KSR.pv_headers.pvh_collect_headers\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_collect_headers)
* [KSR.pv_headers.pvh_header_param_exists\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_header_param_exists)
* [KSR.pv_headers.pvh_modify_header\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_modify_header)
* [KSR.pv_headers.pvh_remove_header\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_remove_header)
* [KSR.pv_headers.pvh_remove_header_param\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_remove_header_param)
* [KSR.pv_headers.pvh_reset_headers\(\)](modules/pv_headers/pv_headers.md#ksrpv_headerspvh_reset_headers)

## pvtpl ##

* 📖[kamailio.cfg::module::pvtpl.html](https://kamailio.org/docs/modules/devel/modules/pvtpl.html)

Exported functions:

* [KSR.pvtpl.pvtpl_render\(\)](modules/pvtpl/pvtpl.md#ksrpvtplpvtpl_render)

## pvx ##

* 📖[kamailio.cfg::module::pv.html](https://kamailio.org/docs/modules/devel/modules/pv.html)

Exported functions:

* [KSR.pvx.avp_get\(\)](modules/pvx/pvx.md#ksrpvxavp_get)
* [KSR.pvx.avp_gete\(\)](modules/pvx/pvx.md#ksrpvxavp_gete)
* [KSR.pvx.avp_getw\(\)](modules/pvx/pvx.md#ksrpvxavp_getw)
* [KSR.pvx.avp_is_null\(\)](modules/pvx/pvx.md#ksrpvxavp_is_null)
* [KSR.pvx.avp_rm\(\)](modules/pvx/pvx.md#ksrpvxavp_rm)
* [KSR.pvx.avp_seti\(\)](modules/pvx/pvx.md#ksrpvxavp_seti)
* [KSR.pvx.avp_sets\(\)](modules/pvx/pvx.md#ksrpvxavp_sets)
* [KSR.pvx.evalx\(\)](modules/pvx/pvx.md#ksrpvxevalx)
* [KSR.pvx.pv_var_to_xavp\(\)](modules/pvx/pvx.md#ksrpvxpv_var_to_xavp)
* [KSR.pvx.pv_xavi_print\(\)](modules/pvx/pvx.md#ksrpvxpv_xavi_print)
* [KSR.pvx.pv_xavp_print\(\)](modules/pvx/pvx.md#ksrpvxpv_xavp_print)
* [KSR.pvx.pv_xavp_to_var\(\)](modules/pvx/pvx.md#ksrpvxpv_xavp_to_var)
* [KSR.pvx.pv_xavu_print\(\)](modules/pvx/pvx.md#ksrpvxpv_xavu_print)
* [KSR.pvx.sbranch_append\(\)](modules/pvx/pvx.md#ksrpvxsbranch_append)
* [KSR.pvx.sbranch_reset\(\)](modules/pvx/pvx.md#ksrpvxsbranch_reset)
* [KSR.pvx.sbranch_set_ruri\(\)](modules/pvx/pvx.md#ksrpvxsbranch_set_ruri)
* [KSR.pvx.shv_get\(\)](modules/pvx/pvx.md#ksrpvxshv_get)
* [KSR.pvx.shv_seti\(\)](modules/pvx/pvx.md#ksrpvxshv_seti)
* [KSR.pvx.shv_sets\(\)](modules/pvx/pvx.md#ksrpvxshv_sets)
* [KSR.pvx.shvinc_get\(\)](modules/pvx/pvx.md#ksrpvxshvinc_get)
* [KSR.pvx.var_get\(\)](modules/pvx/pvx.md#ksrpvxvar_get)
* [KSR.pvx.var_seti\(\)](modules/pvx/pvx.md#ksrpvxvar_seti)
* [KSR.pvx.var_sets\(\)](modules/pvx/pvx.md#ksrpvxvar_sets)
* [KSR.pvx.xavi_child_get\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_get)
* [KSR.pvx.xavi_child_gete\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_gete)
* [KSR.pvx.xavi_child_getw\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_getw)
* [KSR.pvx.xavi_child_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_is_null)
* [KSR.pvx.xavi_child_rm\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_rm)
* [KSR.pvx.xavi_child_seti\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_seti)
* [KSR.pvx.xavi_child_sets\(\)](modules/pvx/pvx.md#ksrpvxxavi_child_sets)
* [KSR.pvx.xavi_get\(\)](modules/pvx/pvx.md#ksrpvxxavi_get)
* [KSR.pvx.xavi_get_keys\(\)](modules/pvx/pvx.md#ksrpvxxavi_get_keys)
* [KSR.pvx.xavi_getd\(\)](modules/pvx/pvx.md#ksrpvxxavi_getd)
* [KSR.pvx.xavi_getd_p1\(\)](modules/pvx/pvx.md#ksrpvxxavi_getd_p1)
* [KSR.pvx.xavi_gete\(\)](modules/pvx/pvx.md#ksrpvxxavi_gete)
* [KSR.pvx.xavi_getw\(\)](modules/pvx/pvx.md#ksrpvxxavi_getw)
* [KSR.pvx.xavi_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavi_is_null)
* [KSR.pvx.xavi_rm\(\)](modules/pvx/pvx.md#ksrpvxxavi_rm)
* [KSR.pvx.xavi_rm_all\(\)](modules/pvx/pvx.md#ksrpvxxavi_rm_all)
* [KSR.pvx.xavi_seti\(\)](modules/pvx/pvx.md#ksrpvxxavi_seti)
* [KSR.pvx.xavi_sets\(\)](modules/pvx/pvx.md#ksrpvxxavi_sets)
* [KSR.pvx.xavp_child_get\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_get)
* [KSR.pvx.xavp_child_gete\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_gete)
* [KSR.pvx.xavp_child_getw\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_getw)
* [KSR.pvx.xavp_child_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_is_null)
* [KSR.pvx.xavp_child_rm\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_rm)
* [KSR.pvx.xavp_child_seti\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_seti)
* [KSR.pvx.xavp_child_sets\(\)](modules/pvx/pvx.md#ksrpvxxavp_child_sets)
* [KSR.pvx.xavp_copy\(\)](modules/pvx/pvx.md#ksrpvxxavp_copy)
* [KSR.pvx.xavp_copy_dst\(\)](modules/pvx/pvx.md#ksrpvxxavp_copy_dst)
* [KSR.pvx.xavp_get\(\)](modules/pvx/pvx.md#ksrpvxxavp_get)
* [KSR.pvx.xavp_get_keys\(\)](modules/pvx/pvx.md#ksrpvxxavp_get_keys)
* [KSR.pvx.xavp_getd\(\)](modules/pvx/pvx.md#ksrpvxxavp_getd)
* [KSR.pvx.xavp_getd_p1\(\)](modules/pvx/pvx.md#ksrpvxxavp_getd_p1)
* [KSR.pvx.xavp_gete\(\)](modules/pvx/pvx.md#ksrpvxxavp_gete)
* [KSR.pvx.xavp_getw\(\)](modules/pvx/pvx.md#ksrpvxxavp_getw)
* [KSR.pvx.xavp_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavp_is_null)
* [KSR.pvx.xavp_lshift\(\)](modules/pvx/pvx.md#ksrpvxxavp_lshift)
* [KSR.pvx.xavp_params_explode\(\)](modules/pvx/pvx.md#ksrpvxxavp_params_explode)
* [KSR.pvx.xavp_params_implode\(\)](modules/pvx/pvx.md#ksrpvxxavp_params_implode)
* [KSR.pvx.xavp_params_implode_qval\(\)](modules/pvx/pvx.md#ksrpvxxavp_params_implode_qval)
* [KSR.pvx.xavp_push_dst\(\)](modules/pvx/pvx.md#ksrpvxxavp_push_dst)
* [KSR.pvx.xavp_rm\(\)](modules/pvx/pvx.md#ksrpvxxavp_rm)
* [KSR.pvx.xavp_rm_all\(\)](modules/pvx/pvx.md#ksrpvxxavp_rm_all)
* [KSR.pvx.xavp_seti\(\)](modules/pvx/pvx.md#ksrpvxxavp_seti)
* [KSR.pvx.xavp_sets\(\)](modules/pvx/pvx.md#ksrpvxxavp_sets)
* [KSR.pvx.xavp_slist_explode\(\)](modules/pvx/pvx.md#ksrpvxxavp_slist_explode)
* [KSR.pvx.xavp_xparams_explode\(\)](modules/pvx/pvx.md#ksrpvxxavp_xparams_explode)
* [KSR.pvx.xavu_child_get\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_get)
* [KSR.pvx.xavu_child_gete\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_gete)
* [KSR.pvx.xavu_child_getw\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_getw)
* [KSR.pvx.xavu_child_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_is_null)
* [KSR.pvx.xavu_child_rm\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_rm)
* [KSR.pvx.xavu_child_seti\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_seti)
* [KSR.pvx.xavu_child_sets\(\)](modules/pvx/pvx.md#ksrpvxxavu_child_sets)
* [KSR.pvx.xavu_get\(\)](modules/pvx/pvx.md#ksrpvxxavu_get)
* [KSR.pvx.xavu_gete\(\)](modules/pvx/pvx.md#ksrpvxxavu_gete)
* [KSR.pvx.xavu_getw\(\)](modules/pvx/pvx.md#ksrpvxxavu_getw)
* [KSR.pvx.xavu_is_null\(\)](modules/pvx/pvx.md#ksrpvxxavu_is_null)
* [KSR.pvx.xavu_params_explode\(\)](modules/pvx/pvx.md#ksrpvxxavu_params_explode)
* [KSR.pvx.xavu_params_implode\(\)](modules/pvx/pvx.md#ksrpvxxavu_params_implode)
* [KSR.pvx.xavu_rm\(\)](modules/pvx/pvx.md#ksrpvxxavu_rm)
* [KSR.pvx.xavu_seti\(\)](modules/pvx/pvx.md#ksrpvxxavu_seti)
* [KSR.pvx.xavu_sets\(\)](modules/pvx/pvx.md#ksrpvxxavu_sets)

## rabbitmq ##

* 📖[kamailio.cfg::module::rabbitmq.html](https://kamailio.org/docs/modules/devel/modules/rabbitmq.html)

Exported functions:

* [KSR.rabbitmq.publish\(\)](modules/rabbitmq/rabbitmq.md#ksrrabbitmqpublish)
* [KSR.rabbitmq.publish_consume\(\)](modules/rabbitmq/rabbitmq.md#ksrrabbitmqpublish_consume)

## ratelimit ##

* 📖[kamailio.cfg::module::ratelimit.html](https://kamailio.org/docs/modules/devel/modules/ratelimit.html)

Exported functions:

* [KSR.ratelimit.rl_check\(\)](modules/ratelimit/ratelimit.md#ksrratelimitrl_check)
* [KSR.ratelimit.rl_check_pipe\(\)](modules/ratelimit/ratelimit.md#ksrratelimitrl_check_pipe)

## regex ##

* 📖[kamailio.cfg::module::regex.html](https://kamailio.org/docs/modules/devel/modules/regex.html)

Exported functions:

* [KSR.regex.pcre_match\(\)](modules/regex/regex.md#ksrregexpcre_match)
* [KSR.regex.pcre_match_group\(\)](modules/regex/regex.md#ksrregexpcre_match_group)

## registrar ##

* 📖[kamailio.cfg::module::registrar.html](https://kamailio.org/docs/modules/devel/modules/registrar.html)

Exported functions:

* [KSR.registrar.add_sock_hdr\(\)](modules/registrar/registrar.md#ksrregistraradd_sock_hdr)
* [KSR.registrar.lookup\(\)](modules/registrar/registrar.md#ksrregistrarlookup)
* [KSR.registrar.lookup_branches\(\)](modules/registrar/registrar.md#ksrregistrarlookup_branches)
* [KSR.registrar.lookup_to_dset\(\)](modules/registrar/registrar.md#ksrregistrarlookup_to_dset)
* [KSR.registrar.lookup_uri\(\)](modules/registrar/registrar.md#ksrregistrarlookup_uri)
* [KSR.registrar.lookup_xavp\(\)](modules/registrar/registrar.md#ksrregistrarlookup_xavp)
* [KSR.registrar.reg_fetch_contacts\(\)](modules/registrar/registrar.md#ksrregistrarreg_fetch_contacts)
* [KSR.registrar.reg_free_contacts\(\)](modules/registrar/registrar.md#ksrregistrarreg_free_contacts)
* [KSR.registrar.reg_from_user\(\)](modules/registrar/registrar.md#ksrregistrarreg_from_user)
* [KSR.registrar.reg_send_reply\(\)](modules/registrar/registrar.md#ksrregistrarreg_send_reply)
* [KSR.registrar.registered\(\)](modules/registrar/registrar.md#ksrregistrarregistered)
* [KSR.registrar.registered_action\(\)](modules/registrar/registrar.md#ksrregistrarregistered_action)
* [KSR.registrar.registered_flags\(\)](modules/registrar/registrar.md#ksrregistrarregistered_flags)
* [KSR.registrar.registered_uri\(\)](modules/registrar/registrar.md#ksrregistrarregistered_uri)
* [KSR.registrar.save\(\)](modules/registrar/registrar.md#ksrregistrarsave)
* [KSR.registrar.save_uri\(\)](modules/registrar/registrar.md#ksrregistrarsave_uri)
* [KSR.registrar.set_q_override\(\)](modules/registrar/registrar.md#ksrregistrarset_q_override)
* [KSR.registrar.ulc_cget\(\)](modules/registrar/registrar.md#ksrregistrarulc_cget)
* [KSR.registrar.ulc_rget\(\)](modules/registrar/registrar.md#ksrregistrarulc_rget)
* [KSR.registrar.unregister\(\)](modules/registrar/registrar.md#ksrregistrarunregister)
* [KSR.registrar.unregister_ruid\(\)](modules/registrar/registrar.md#ksrregistrarunregister_ruid)

## rls ##

* 📖[kamailio.cfg::module::rls.html](https://kamailio.org/docs/modules/devel/modules/rls.html)

Exported functions:

* [KSR.rls.handle_notify\(\)](modules/rls/rls.md#ksrrlshandle_notify)
* [KSR.rls.handle_subscribe\(\)](modules/rls/rls.md#ksrrlshandle_subscribe)
* [KSR.rls.handle_subscribe_uri\(\)](modules/rls/rls.md#ksrrlshandle_subscribe_uri)
* [KSR.rls.update_subs\(\)](modules/rls/rls.md#ksrrlsupdate_subs)

## rr ##

* 📖[kamailio.cfg::module::rr.html](https://kamailio.org/docs/modules/devel/modules/rr.html)

Exported functions:

* [KSR.rr.add_rr_param\(\)](modules/rr/rr.md#ksrrradd_rr_param)
* [KSR.rr.check_route_param\(\)](modules/rr/rr.md#ksrrrcheck_route_param)
* [KSR.rr.cookie_add\(\)](modules/rr/rr.md#ksrrrcookie_add)
* [KSR.rr.cookie_check\(\)](modules/rr/rr.md#ksrrrcookie_check)
* [KSR.rr.cookie_flfetch\(\)](modules/rr/rr.md#ksrrrcookie_flfetch)
* [KSR.rr.cookie_flinit\(\)](modules/rr/rr.md#ksrrrcookie_flinit)
* [KSR.rr.cookie_flisset\(\)](modules/rr/rr.md#ksrrrcookie_flisset)
* [KSR.rr.cookie_flreset\(\)](modules/rr/rr.md#ksrrrcookie_flreset)
* [KSR.rr.cookie_flset\(\)](modules/rr/rr.md#ksrrrcookie_flset)
* [KSR.rr.is_direction\(\)](modules/rr/rr.md#ksrrris_direction)
* [KSR.rr.loose_route\(\)](modules/rr/rr.md#ksrrrloose_route)
* [KSR.rr.loose_route_mode\(\)](modules/rr/rr.md#ksrrrloose_route_mode)
* [KSR.rr.loose_route_preloaded\(\)](modules/rr/rr.md#ksrrrloose_route_preloaded)
* [KSR.rr.next_hop_route\(\)](modules/rr/rr.md#ksrrrnext_hop_route)
* [KSR.rr.record_route\(\)](modules/rr/rr.md#ksrrrrecord_route)
* [KSR.rr.record_route_advertised_address\(\)](modules/rr/rr.md#ksrrrrecord_route_advertised_address)
* [KSR.rr.record_route_params\(\)](modules/rr/rr.md#ksrrrrecord_route_params)
* [KSR.rr.record_route_preset\(\)](modules/rr/rr.md#ksrrrrecord_route_preset)
* [KSR.rr.record_route_preset_one\(\)](modules/rr/rr.md#ksrrrrecord_route_preset_one)
* [KSR.rr.remove_record_route\(\)](modules/rr/rr.md#ksrrrremove_record_route)

## rtjson ##

* 📖[kamailio.cfg::module::rtjson.html](https://kamailio.org/docs/modules/devel/modules/rtjson.html)

Exported functions:

* [KSR.rtjson.init_routes\(\)](modules/rtjson/rtjson.md#ksrrtjsoninit_routes)
* [KSR.rtjson.next_route\(\)](modules/rtjson/rtjson.md#ksrrtjsonnext_route)
* [KSR.rtjson.push_routes\(\)](modules/rtjson/rtjson.md#ksrrtjsonpush_routes)
* [KSR.rtjson.update_branch\(\)](modules/rtjson/rtjson.md#ksrrtjsonupdate_branch)

## rtpengine ##

* 📖[kamailio.cfg::module::rtpengine.html](https://kamailio.org/docs/modules/devel/modules/rtpengine.html)

This module enables media streams to be proxied via RTPEngine, exporting
the functions to interact with it.

Exported functions:

* [KSR.rtpengine.block_dtmf\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_dtmf)
* [KSR.rtpengine.block_dtmf0\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_dtmf0)
* [KSR.rtpengine.block_dtmf2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_dtmf2)
* [KSR.rtpengine.block_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_media)
* [KSR.rtpengine.block_media0\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_media0)
* [KSR.rtpengine.block_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineblock_media2)
* [KSR.rtpengine.play_dtmf\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineplay_dtmf)
* [KSR.rtpengine.play_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineplay_media)
* [KSR.rtpengine.play_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineplay_media2)
* [KSR.rtpengine.rtpengine_answer\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_answer)
* [KSR.rtpengine.rtpengine_answer0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_answer0)
* [KSR.rtpengine.rtpengine_answer2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_answer2)
* [KSR.rtpengine.rtpengine_connect\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_connect)
* [KSR.rtpengine.rtpengine_connect0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_connect0)
* [KSR.rtpengine.rtpengine_connect2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_connect2)
* [KSR.rtpengine.rtpengine_delete\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_delete)
* [KSR.rtpengine.rtpengine_delete0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_delete0)
* [KSR.rtpengine.rtpengine_delete2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_delete2)
* [KSR.rtpengine.rtpengine_manage\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_manage)
* [KSR.rtpengine.rtpengine_manage0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_manage0)
* [KSR.rtpengine.rtpengine_manage2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_manage2)
* [KSR.rtpengine.rtpengine_offer\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_offer)
* [KSR.rtpengine.rtpengine_offer0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_offer0)
* [KSR.rtpengine.rtpengine_offer2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_offer2)
* [KSR.rtpengine.rtpengine_query\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_query)
* [KSR.rtpengine.rtpengine_query0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_query0)
* [KSR.rtpengine.rtpengine_query2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_query2)
* [KSR.rtpengine.rtpengine_query_v\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_query_v)
* [KSR.rtpengine.rtpengine_subscribe_answer\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_subscribe_answer)
* [KSR.rtpengine.rtpengine_subscribe_request\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_subscribe_request)
* [KSR.rtpengine.rtpengine_unsubscribe\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginertpengine_unsubscribe)
* [KSR.rtpengine.set_rtpengine_set\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineset_rtpengine_set)
* [KSR.rtpengine.set_rtpengine_set2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineset_rtpengine_set2)
* [KSR.rtpengine.silence_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginesilence_media)
* [KSR.rtpengine.silence_media0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginesilence_media0)
* [KSR.rtpengine.silence_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginesilence_media2)
* [KSR.rtpengine.start_forwarding\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestart_forwarding)
* [KSR.rtpengine.start_forwarding0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestart_forwarding0)
* [KSR.rtpengine.start_forwarding2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestart_forwarding2)
* [KSR.rtpengine.start_recording\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestart_recording)
* [KSR.rtpengine.stop_forwarding\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_forwarding)
* [KSR.rtpengine.stop_forwarding0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_forwarding0)
* [KSR.rtpengine.stop_forwarding2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_forwarding2)
* [KSR.rtpengine.stop_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_media)
* [KSR.rtpengine.stop_media0\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_media0)
* [KSR.rtpengine.stop_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_media2)
* [KSR.rtpengine.stop_recording\(\)](modules/rtpengine/rtpengine.md#ksrrtpenginestop_recording)
* [KSR.rtpengine.unblock_dtmf\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_dtmf)
* [KSR.rtpengine.unblock_dtmf0\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_dtmf0)
* [KSR.rtpengine.unblock_dtmf2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_dtmf2)
* [KSR.rtpengine.unblock_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_media)
* [KSR.rtpengine.unblock_media0\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_media0)
* [KSR.rtpengine.unblock_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunblock_media2)
* [KSR.rtpengine.unsilence_media\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunsilence_media)
* [KSR.rtpengine.unsilence_media0\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunsilence_media0)
* [KSR.rtpengine.unsilence_media2\(\)](modules/rtpengine/rtpengine.md#ksrrtpengineunsilence_media2)

## rtpproxy ##

* 📖[kamailio.cfg::module::rtpproxy.html](https://kamailio.org/docs/modules/devel/modules/rtpproxy.html)

Exported functions:

* [KSR.rtpproxy.rtpproxy_answer\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_answer)
* [KSR.rtpproxy.rtpproxy_answer0\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_answer0)
* [KSR.rtpproxy.rtpproxy_answer_ip\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_answer_ip)
* [KSR.rtpproxy.rtpproxy_destroy\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_destroy)
* [KSR.rtpproxy.rtpproxy_destroy0\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_destroy0)
* [KSR.rtpproxy.rtpproxy_manage\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_manage)
* [KSR.rtpproxy.rtpproxy_manage0\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_manage0)
* [KSR.rtpproxy.rtpproxy_manage_ip\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_manage_ip)
* [KSR.rtpproxy.rtpproxy_offer\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_offer)
* [KSR.rtpproxy.rtpproxy_offer0\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_offer0)
* [KSR.rtpproxy.rtpproxy_offer_ip\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_offer_ip)
* [KSR.rtpproxy.rtpproxy_stop_stream2uac\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_stop_stream2uac)
* [KSR.rtpproxy.rtpproxy_stop_stream2uas\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_stop_stream2uas)
* [KSR.rtpproxy.rtpproxy_stream2uac\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_stream2uac)
* [KSR.rtpproxy.rtpproxy_stream2uas\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyrtpproxy_stream2uas)
* [KSR.rtpproxy.set_rtpproxy_set\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxyset_rtpproxy_set)
* [KSR.rtpproxy.start_recording\(\)](modules/rtpproxy/rtpproxy.md#ksrrtpproxystart_recording)

## ruxc ##

* 📖[kamailio.cfg::module::ruxc.html](https://kamailio.org/docs/modules/devel/modules/ruxc.html)

Exported functions:

* [KSR.ruxc.http_delete\(\)](modules/ruxc/ruxc.md#ksrruxchttp_delete)
* [KSR.ruxc.http_get\(\)](modules/ruxc/ruxc.md#ksrruxchttp_get)
* [KSR.ruxc.http_post\(\)](modules/ruxc/ruxc.md#ksrruxchttp_post)

## sanity ##

* 📖[kamailio.cfg::module::sanity.html](https://kamailio.org/docs/modules/devel/modules/sanity.html)

Exported functions:

* [KSR.sanity.sanity_check\(\)](modules/sanity/sanity.md#ksrsanitysanity_check)
* [KSR.sanity.sanity_check_defaults\(\)](modules/sanity/sanity.md#ksrsanitysanity_check_defaults)
* [KSR.sanity.sanity_reply\(\)](modules/sanity/sanity.md#ksrsanitysanity_reply)

## sca ##

* 📖[kamailio.cfg::module::sca.html](https://kamailio.org/docs/modules/devel/modules/sca.html)

Exported functions:

* [KSR.sca.call_info_update\(\)](modules/sca/sca.md#ksrscacall_info_update)
* [KSR.sca.call_info_update_default\(\)](modules/sca/sca.md#ksrscacall_info_update_default)
* [KSR.sca.call_info_update_mask\(\)](modules/sca/sca.md#ksrscacall_info_update_mask)
* [KSR.sca.call_info_update_turi\(\)](modules/sca/sca.md#ksrscacall_info_update_turi)
* [KSR.sca.handle_subscribe\(\)](modules/sca/sca.md#ksrscahandle_subscribe)

## sdpops ##

* 📖[kamailio.cfg::module::sdpops.html](https://kamailio.org/docs/modules/devel/modules/sdpops.html)

Exported functions:

* [KSR.sdpops.keep_codecs_by_id\(\)](modules/sdpops/sdpops.md#ksrsdpopskeep_codecs_by_id)
* [KSR.sdpops.keep_codecs_by_name\(\)](modules/sdpops/sdpops.md#ksrsdpopskeep_codecs_by_name)
* [KSR.sdpops.remove_codecs_by_id\(\)](modules/sdpops/sdpops.md#ksrsdpopsremove_codecs_by_id)
* [KSR.sdpops.remove_codecs_by_name\(\)](modules/sdpops/sdpops.md#ksrsdpopsremove_codecs_by_name)
* [KSR.sdpops.remove_line_by_prefix\(\)](modules/sdpops/sdpops.md#ksrsdpopsremove_line_by_prefix)
* [KSR.sdpops.remove_media\(\)](modules/sdpops/sdpops.md#ksrsdpopsremove_media)
* [KSR.sdpops.sdp_content\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_content)
* [KSR.sdpops.sdp_content_flags\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_content_flags)
* [KSR.sdpops.sdp_get\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_get)
* [KSR.sdpops.sdp_get_address_family\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_get_address_family)
* [KSR.sdpops.sdp_get_line_startswith\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_get_line_startswith)
* [KSR.sdpops.sdp_iterator_append\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_append)
* [KSR.sdpops.sdp_iterator_end\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_end)
* [KSR.sdpops.sdp_iterator_insert\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_insert)
* [KSR.sdpops.sdp_iterator_next\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_next)
* [KSR.sdpops.sdp_iterator_rm\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_rm)
* [KSR.sdpops.sdp_iterator_start\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_start)
* [KSR.sdpops.sdp_iterator_value\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_iterator_value)
* [KSR.sdpops.sdp_print\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_print)
* [KSR.sdpops.sdp_transport\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_transport)
* [KSR.sdpops.sdp_with_active_media\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_active_media)
* [KSR.sdpops.sdp_with_codecs_by_id\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_codecs_by_id)
* [KSR.sdpops.sdp_with_codecs_by_name\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_codecs_by_name)
* [KSR.sdpops.sdp_with_ice\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_ice)
* [KSR.sdpops.sdp_with_media\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_media)
* [KSR.sdpops.sdp_with_transport\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_transport)
* [KSR.sdpops.sdp_with_transport_like\(\)](modules/sdpops/sdpops.md#ksrsdpopssdp_with_transport_like)

## secfilter ##

* 📖[kamailio.cfg::module::secfilter.html](https://kamailio.org/docs/modules/devel/modules/secfilter.html)

Exported functions:

* [KSR.secfilter.ki_check_domain_contact_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_domain_contact_hdr)
* [KSR.secfilter.ki_check_domain_from_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_domain_from_hdr)
* [KSR.secfilter.ki_check_domain_to_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_domain_to_hdr)
* [KSR.secfilter.ki_check_name_contact_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_name_contact_hdr)
* [KSR.secfilter.ki_check_name_from_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_name_from_hdr)
* [KSR.secfilter.ki_check_name_to_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_name_to_hdr)
* [KSR.secfilter.ki_check_username_contact_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_username_contact_hdr)
* [KSR.secfilter.ki_check_username_from_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_username_from_hdr)
* [KSR.secfilter.ki_check_username_to_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfilterki_check_username_to_hdr)
* [KSR.secfilter.secf_check_contact_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_contact_hdr)
* [KSR.secfilter.secf_check_country\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_country)
* [KSR.secfilter.secf_check_dst\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_dst)
* [KSR.secfilter.secf_check_from_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_from_hdr)
* [KSR.secfilter.secf_check_ip\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_ip)
* [KSR.secfilter.secf_check_sqli_all\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_sqli_all)
* [KSR.secfilter.secf_check_to_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_to_hdr)
* [KSR.secfilter.secf_check_ua\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_check_ua)
* [KSR.secfilter.secf_sqli_hdr\(\)](modules/secfilter/secfilter.md#ksrsecfiltersecf_sqli_hdr)

## secsipid ##

* 📖[kamailio.cfg::module::secsipid.html](https://kamailio.org/docs/modules/devel/modules/secsipid.html)

Exported functions:

* [KSR.secsipid.result_str\(\)](modules/secsipid/secsipid.md#ksrsecsipidresult_str)
* [KSR.secsipid.secsipid_add_identity\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_add_identity)
* [KSR.secsipid.secsipid_build_identity\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_build_identity)
* [KSR.secsipid.secsipid_build_identity_prvkey\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_build_identity_prvkey)
* [KSR.secsipid.secsipid_check\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_check)
* [KSR.secsipid.secsipid_check_identity\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_check_identity)
* [KSR.secsipid.secsipid_check_identity_pubkey\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_check_identity_pubkey)
* [KSR.secsipid.secsipid_get_url\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_get_url)
* [KSR.secsipid.secsipid_get_val\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_get_val)
* [KSR.secsipid.secsipid_sign\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_sign)
* [KSR.secsipid.secsipid_sign_prvkey\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_sign_prvkey)
* [KSR.secsipid.secsipid_verify\(\)](modules/secsipid/secsipid.md#ksrsecsipidsecsipid_verify)

## sipcapture ##

* 📖[kamailio.cfg::module::sipcapture.html](https://kamailio.org/docs/modules/devel/modules/sipcapture.html)

Exported functions:

* [KSR.sipcapture.float2int\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturefloat2int)
* [KSR.sipcapture.report_capture\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturereport_capture)
* [KSR.sipcapture.report_capture_cid\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturereport_capture_cid)
* [KSR.sipcapture.report_capture_data\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturereport_capture_data)
* [KSR.sipcapture.sip_capture\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturesip_capture)
* [KSR.sipcapture.sip_capture_forward\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturesip_capture_forward)
* [KSR.sipcapture.sip_capture_mode\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturesip_capture_mode)
* [KSR.sipcapture.sip_capture_table\(\)](modules/sipcapture/sipcapture.md#ksrsipcapturesip_capture_table)

## sipdump ##

* 📖[kamailio.cfg::module::sipdump.html](https://kamailio.org/docs/modules/devel/modules/sipdump.html)

Exported functions:

* [KSR.sipdump.get_buf\(\)](modules/sipdump/sipdump.md#ksrsipdumpget_buf)
* [KSR.sipdump.get_dst_ip\(\)](modules/sipdump/sipdump.md#ksrsipdumpget_dst_ip)
* [KSR.sipdump.get_src_ip\(\)](modules/sipdump/sipdump.md#ksrsipdumpget_src_ip)
* [KSR.sipdump.get_tag\(\)](modules/sipdump/sipdump.md#ksrsipdumpget_tag)
* [KSR.sipdump.send\(\)](modules/sipdump/sipdump.md#ksrsipdumpsend)

## sipjson ##

* 📖[kamailio.cfg::module::sipjson.html](https://kamailio.org/docs/modules/devel/modules/sipjson.html)

Exported functions:

* [KSR.sipjson.sj_serialize\(\)](modules/sipjson/sipjson.md#ksrsipjsonsj_serialize)

## siprepo ##

* 📖[kamailio.cfg::module::siprepo.html](https://kamailio.org/docs/modules/devel/modules/siprepo.html)

Exported functions:

* [KSR.siprepo.sr_msg_async_pull\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_async_pull)
* [KSR.siprepo.sr_msg_check\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_check)
* [KSR.siprepo.sr_msg_match\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_match)
* [KSR.siprepo.sr_msg_pull\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_pull)
* [KSR.siprepo.sr_msg_push\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_push)
* [KSR.siprepo.sr_msg_rm\(\)](modules/siprepo/siprepo.md#ksrsipreposr_msg_rm)

## sipt ##

* 📖[kamailio.cfg::module::sipt.html](https://kamailio.org/docs/modules/devel/modules/sipt.html)

Exported functions:

* [KSR.sipt.destination\(\)](modules/sipt/sipt.md#ksrsiptdestination)
* [KSR.sipt.destination_terminator\(\)](modules/sipt/sipt.md#ksrsiptdestination_terminator)
* [KSR.sipt.forwarding\(\)](modules/sipt/sipt.md#ksrsiptforwarding)
* [KSR.sipt.has_isup_body\(\)](modules/sipt/sipt.md#ksrsipthas_isup_body)
* [KSR.sipt.set_bci_1\(\)](modules/sipt/sipt.md#ksrsiptset_bci_1)
* [KSR.sipt.set_calling\(\)](modules/sipt/sipt.md#ksrsiptset_calling)

## siptrace ##

* 📖[kamailio.cfg::module::siptrace.html](https://kamailio.org/docs/modules/devel/modules/siptrace.html)

Exported functions:

* [KSR.siptrace.hlog\(\)](modules/siptrace/siptrace.md#ksrsiptracehlog)
* [KSR.siptrace.hlog_cid\(\)](modules/siptrace/siptrace.md#ksrsiptracehlog_cid)
* [KSR.siptrace.sip_trace\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace)
* [KSR.siptrace.sip_trace_dst\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace_dst)
* [KSR.siptrace.sip_trace_dst_cid\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace_dst_cid)
* [KSR.siptrace.sip_trace_dst_cid_type\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace_dst_cid_type)
* [KSR.siptrace.sip_trace_mode\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace_mode)
* [KSR.siptrace.sip_trace_msg\(\)](modules/siptrace/siptrace.md#ksrsiptracesip_trace_msg)

## siputils ##

* 📖[kamailio.cfg::module::siputils.html](https://kamailio.org/docs/modules/devel/modules/siputils.html)

Exported functions:

* [KSR.siputils.add_uri_param\(\)](modules/siputils/siputils.md#ksrsiputilsadd_uri_param)
* [KSR.siputils.cmp_aor\(\)](modules/siputils/siputils.md#ksrsiputilscmp_aor)
* [KSR.siputils.cmp_hdr_name\(\)](modules/siputils/siputils.md#ksrsiputilscmp_hdr_name)
* [KSR.siputils.cmp_uri\(\)](modules/siputils/siputils.md#ksrsiputilscmp_uri)
* [KSR.siputils.contact_param_check\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_check)
* [KSR.siputils.contact_param_decode\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_decode)
* [KSR.siputils.contact_param_decode_ruri\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_decode_ruri)
* [KSR.siputils.contact_param_encode\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_encode)
* [KSR.siputils.contact_param_encode_alias\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_encode_alias)
* [KSR.siputils.contact_param_rm\(\)](modules/siputils/siputils.md#ksrsiputilscontact_param_rm)
* [KSR.siputils.decode_contact\(\)](modules/siputils/siputils.md#ksrsiputilsdecode_contact)
* [KSR.siputils.decode_contact_header\(\)](modules/siputils/siputils.md#ksrsiputilsdecode_contact_header)
* [KSR.siputils.encode_contact\(\)](modules/siputils/siputils.md#ksrsiputilsencode_contact)
* [KSR.siputils.has_totag\(\)](modules/siputils/siputils.md#ksrsiputilshas_totag)
* [KSR.siputils.hdr_date_check\(\)](modules/siputils/siputils.md#ksrsiputilshdr_date_check)
* [KSR.siputils.is_alphanum\(\)](modules/siputils/siputils.md#ksrsiputilsis_alphanum)
* [KSR.siputils.is_alphanumex\(\)](modules/siputils/siputils.md#ksrsiputilsis_alphanumex)
* [KSR.siputils.is_first_hop\(\)](modules/siputils/siputils.md#ksrsiputilsis_first_hop)
* [KSR.siputils.is_first_hop_mode\(\)](modules/siputils/siputils.md#ksrsiputilsis_first_hop_mode)
* [KSR.siputils.is_gruu\(\)](modules/siputils/siputils.md#ksrsiputilsis_gruu)
* [KSR.siputils.is_http\(\)](modules/siputils/siputils.md#ksrsiputilsis_http)
* [KSR.siputils.is_numeric\(\)](modules/siputils/siputils.md#ksrsiputilsis_numeric)
* [KSR.siputils.is_reply\(\)](modules/siputils/siputils.md#ksrsiputilsis_reply)
* [KSR.siputils.is_request\(\)](modules/siputils/siputils.md#ksrsiputilsis_request)
* [KSR.siputils.is_sip\(\)](modules/siputils/siputils.md#ksrsiputilsis_sip)
* [KSR.siputils.is_tel_number\(\)](modules/siputils/siputils.md#ksrsiputilsis_tel_number)
* [KSR.siputils.is_uri\(\)](modules/siputils/siputils.md#ksrsiputilsis_uri)
* [KSR.siputils.is_user\(\)](modules/siputils/siputils.md#ksrsiputilsis_user)
* [KSR.siputils.options_reply\(\)](modules/siputils/siputils.md#ksrsiputilsoptions_reply)
* [KSR.siputils.sip_parse_headers\(\)](modules/siputils/siputils.md#ksrsiputilssip_parse_headers)
* [KSR.siputils.uri_param\(\)](modules/siputils/siputils.md#ksrsiputilsuri_param)
* [KSR.siputils.uri_param_any\(\)](modules/siputils/siputils.md#ksrsiputilsuri_param_any)
* [KSR.siputils.uri_param_rm\(\)](modules/siputils/siputils.md#ksrsiputilsuri_param_rm)
* [KSR.siputils.uri_param_value\(\)](modules/siputils/siputils.md#ksrsiputilsuri_param_value)

## sl ##

* 📖[kamailio.cfg::module::sl.html](https://kamailio.org/docs/modules/devel/modules/sl.html)

Exported functions:

* [KSR.sl.send_reply\(\)](modules/sl/sl.md#ksrslsend_reply)
* [KSR.sl.send_reply_error\(\)](modules/sl/sl.md#ksrslsend_reply_error)
* [KSR.sl.send_reply_mode\(\)](modules/sl/sl.md#ksrslsend_reply_mode)
* [KSR.sl.sl_forward_reply\(\)](modules/sl/sl.md#ksrslsl_forward_reply)
* [KSR.sl.sl_reply_error\(\)](modules/sl/sl.md#ksrslsl_reply_error)
* [KSR.sl.sl_send_reply\(\)](modules/sl/sl.md#ksrslsl_send_reply)

## slack ##

* 📖[kamailio.cfg::module::slack.html](https://kamailio.org/docs/modules/devel/modules/slack.html)

Exported functions:

* [KSR.slack.slack_send\(\)](modules/slack/slack.md#ksrslackslack_send)

## speeddial ##

* 📖[kamailio.cfg::module::speeddial.html](https://kamailio.org/docs/modules/devel/modules/speeddial.html)

Exported functions:

* [KSR.speeddial.lookup\(\)](modules/speeddial/speeddial.md#ksrspeeddiallookup)
* [KSR.speeddial.lookup_owner\(\)](modules/speeddial/speeddial.md#ksrspeeddiallookup_owner)

## sqlops ##

* 📖[kamailio.cfg::module::sqlops.html](https://kamailio.org/docs/modules/devel/modules/sqlops.html)

Exported functions:

* [KSR.sqlops.sql_is_null\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_is_null)
* [KSR.sqlops.sql_num_columns\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_num_columns)
* [KSR.sqlops.sql_num_rows\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_num_rows)
* [KSR.sqlops.sql_pvquery\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_pvquery)
* [KSR.sqlops.sql_query\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_query)
* [KSR.sqlops.sql_query_async\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_query_async)
* [KSR.sqlops.sql_result_free\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_result_free)
* [KSR.sqlops.sql_result_get\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_result_get)
* [KSR.sqlops.sql_result_gete\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_result_gete)
* [KSR.sqlops.sql_result_getz\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_result_getz)
* [KSR.sqlops.sql_xquery\(\)](modules/sqlops/sqlops.md#ksrsqlopssql_xquery)

## ss7ops ##

* 📖[kamailio.cfg::module::ss7ops.html](https://kamailio.org/docs/modules/devel/modules/ss7ops.html)

Exported functions:

* [KSR.ss7ops.isup_to_json\(\)](modules/ss7ops/ss7ops.md#ksrss7opsisup_to_json)

## sst ##

* 📖[kamailio.cfg::module::sst.html](https://kamailio.org/docs/modules/devel/modules/sst.html)

Exported functions:

* [KSR.sst.sst_check_min\(\)](modules/sst/sst.md#ksrsstsst_check_min)

## statistics ##

* 📖[kamailio.cfg::module::statistics.html](https://kamailio.org/docs/modules/devel/modules/statistics.html)

Exported functions:

* [KSR.statistics.reset_stat\(\)](modules/statistics/statistics.md#ksrstatisticsreset_stat)
* [KSR.statistics.update_stat\(\)](modules/statistics/statistics.md#ksrstatisticsupdate_stat)

## statsc ##

* 📖[kamailio.cfg::module::statsc.html](https://kamailio.org/docs/modules/devel/modules/statsc.html)

Exported functions:

* [KSR.statsc.statsc_reset\(\)](modules/statsc/statsc.md#ksrstatscstatsc_reset)

## statsd ##

* 📖[kamailio.cfg::module::statsd.html](https://kamailio.org/docs/modules/devel/modules/statsd.html)

Exported functions:

* [KSR.statsd.statsd_decr\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_decr)
* [KSR.statsd.statsd_gauge\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_gauge)
* [KSR.statsd.statsd_histogram\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_histogram)
* [KSR.statsd.statsd_incr\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_incr)
* [KSR.statsd.statsd_labels_decr\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_decr)
* [KSR.statsd.statsd_labels_gauge\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_gauge)
* [KSR.statsd.statsd_labels_histogram\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_histogram)
* [KSR.statsd.statsd_labels_incr\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_incr)
* [KSR.statsd.statsd_labels_set\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_set)
* [KSR.statsd.statsd_labels_stop\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_labels_stop)
* [KSR.statsd.statsd_set\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_set)
* [KSR.statsd.statsd_start\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_start)
* [KSR.statsd.statsd_stop\(\)](modules/statsd/statsd.md#ksrstatsdstatsd_stop)

## stirshaken ##

* 📖[kamailio.cfg::module::stirshaken.html](https://kamailio.org/docs/modules/devel/modules/stirshaken.html)

Exported functions:

* [KSR.stirshaken.stirshaken_add_identity\(\)](modules/stirshaken/stirshaken.md#ksrstirshakenstirshaken_add_identity)
* [KSR.stirshaken.stirshaken_add_identity_with_key\(\)](modules/stirshaken/stirshaken.md#ksrstirshakenstirshaken_add_identity_with_key)
* [KSR.stirshaken.stirshaken_check_identity\(\)](modules/stirshaken/stirshaken.md#ksrstirshakenstirshaken_check_identity)
* [KSR.stirshaken.stirshaken_check_identity_with_cert\(\)](modules/stirshaken/stirshaken.md#ksrstirshakenstirshaken_check_identity_with_cert)
* [KSR.stirshaken.stirshaken_check_identity_with_key\(\)](modules/stirshaken/stirshaken.md#ksrstirshakenstirshaken_check_identity_with_key)

## sworker ##

* 📖[kamailio.cfg::module::sworker.html](https://kamailio.org/docs/modules/devel/modules/sworker.html)

Exported functions:

* [KSR.sworker.active\(\)](modules/sworker/sworker.md#ksrsworkeractive)
* [KSR.sworker.task\(\)](modules/sworker/sworker.md#ksrsworkertask)

## tcpops ##

* 📖[kamailio.cfg::module::tcpops.html](https://kamailio.org/docs/modules/devel/modules/tcpops.html)

Exported functions:

* [KSR.tcpops.tcp_close_connection\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_close_connection)
* [KSR.tcpops.tcp_close_connection_id\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_close_connection_id)
* [KSR.tcpops.tcp_con_alive\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_con_alive)
* [KSR.tcpops.tcp_conid_alive\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_conid_alive)
* [KSR.tcpops.tcp_conid_state\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_conid_state)
* [KSR.tcpops.tcp_enable_closed_event\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_enable_closed_event)
* [KSR.tcpops.tcp_enable_closed_event_cid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_enable_closed_event_cid)
* [KSR.tcpops.tcp_get_conid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_get_conid)
* [KSR.tcpops.tcp_keepalive_disable\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_keepalive_disable)
* [KSR.tcpops.tcp_keepalive_disable_cid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_keepalive_disable_cid)
* [KSR.tcpops.tcp_keepalive_enable\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_keepalive_enable)
* [KSR.tcpops.tcp_keepalive_enable_cid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_keepalive_enable_cid)
* [KSR.tcpops.tcp_set_connection_lifetime\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_set_connection_lifetime)
* [KSR.tcpops.tcp_set_connection_lifetime_cid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_set_connection_lifetime_cid)
* [KSR.tcpops.tcp_set_otcpid\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_set_otcpid)
* [KSR.tcpops.tcp_set_otcpid_flag\(\)](modules/tcpops/tcpops.md#ksrtcpopstcp_set_otcpid_flag)

## textops ##

* 📖[kamailio.cfg::module::textops.html](https://kamailio.org/docs/modules/devel/modules/textops.html)

Exported functions:

* [KSR.textops.append_body_part\(\)](modules/textops/textops.md#ksrtextopsappend_body_part)
* [KSR.textops.append_body_part_cd\(\)](modules/textops/textops.md#ksrtextopsappend_body_part_cd)
* [KSR.textops.append_body_part_hex\(\)](modules/textops/textops.md#ksrtextopsappend_body_part_hex)
* [KSR.textops.append_body_part_hex_cd\(\)](modules/textops/textops.md#ksrtextopsappend_body_part_hex_cd)
* [KSR.textops.cmp_istr\(\)](modules/textops/textops.md#ksrtextopscmp_istr)
* [KSR.textops.cmp_str\(\)](modules/textops/textops.md#ksrtextopscmp_str)
* [KSR.textops.ends_with\(\)](modules/textops/textops.md#ksrtextopsends_with)
* [KSR.textops.filter_body\(\)](modules/textops/textops.md#ksrtextopsfilter_body)
* [KSR.textops.get_body_part\(\)](modules/textops/textops.md#ksrtextopsget_body_part)
* [KSR.textops.get_body_part_raw\(\)](modules/textops/textops.md#ksrtextopsget_body_part_raw)
* [KSR.textops.has_body\(\)](modules/textops/textops.md#ksrtextopshas_body)
* [KSR.textops.has_body_type\(\)](modules/textops/textops.md#ksrtextopshas_body_type)
* [KSR.textops.in_list\(\)](modules/textops/textops.md#ksrtextopsin_list)
* [KSR.textops.in_list_prefix\(\)](modules/textops/textops.md#ksrtextopsin_list_prefix)
* [KSR.textops.is_audio_on_hold\(\)](modules/textops/textops.md#ksrtextopsis_audio_on_hold)
* [KSR.textops.is_present_hf\(\)](modules/textops/textops.md#ksrtextopsis_present_hf)
* [KSR.textops.is_present_hf_re\(\)](modules/textops/textops.md#ksrtextopsis_present_hf_re)
* [KSR.textops.is_privacy\(\)](modules/textops/textops.md#ksrtextopsis_privacy)
* [KSR.textops.regex_substring\(\)](modules/textops/textops.md#ksrtextopsregex_substring)
* [KSR.textops.remove_body_part\(\)](modules/textops/textops.md#ksrtextopsremove_body_part)
* [KSR.textops.remove_hf\(\)](modules/textops/textops.md#ksrtextopsremove_hf)
* [KSR.textops.remove_hf_exp\(\)](modules/textops/textops.md#ksrtextopsremove_hf_exp)
* [KSR.textops.remove_hf_idx\(\)](modules/textops/textops.md#ksrtextopsremove_hf_idx)
* [KSR.textops.remove_hf_match\(\)](modules/textops/textops.md#ksrtextopsremove_hf_match)
* [KSR.textops.remove_hf_re\(\)](modules/textops/textops.md#ksrtextopsremove_hf_re)
* [KSR.textops.replace\(\)](modules/textops/textops.md#ksrtextopsreplace)
* [KSR.textops.replace_all\(\)](modules/textops/textops.md#ksrtextopsreplace_all)
* [KSR.textops.replace_body\(\)](modules/textops/textops.md#ksrtextopsreplace_body)
* [KSR.textops.replace_body_all\(\)](modules/textops/textops.md#ksrtextopsreplace_body_all)
* [KSR.textops.replace_body_atonce\(\)](modules/textops/textops.md#ksrtextopsreplace_body_atonce)
* [KSR.textops.replace_body_str\(\)](modules/textops/textops.md#ksrtextopsreplace_body_str)
* [KSR.textops.replace_hdrs\(\)](modules/textops/textops.md#ksrtextopsreplace_hdrs)
* [KSR.textops.replace_hdrs_str\(\)](modules/textops/textops.md#ksrtextopsreplace_hdrs_str)
* [KSR.textops.replace_str\(\)](modules/textops/textops.md#ksrtextopsreplace_str)
* [KSR.textops.search\(\)](modules/textops/textops.md#ksrtextopssearch)
* [KSR.textops.search_append\(\)](modules/textops/textops.md#ksrtextopssearch_append)
* [KSR.textops.search_append_body\(\)](modules/textops/textops.md#ksrtextopssearch_append_body)
* [KSR.textops.search_body\(\)](modules/textops/textops.md#ksrtextopssearch_body)
* [KSR.textops.search_hf\(\)](modules/textops/textops.md#ksrtextopssearch_hf)
* [KSR.textops.search_str\(\)](modules/textops/textops.md#ksrtextopssearch_str)
* [KSR.textops.set_body\(\)](modules/textops/textops.md#ksrtextopsset_body)
* [KSR.textops.set_body_hex\(\)](modules/textops/textops.md#ksrtextopsset_body_hex)
* [KSR.textops.set_body_multipart\(\)](modules/textops/textops.md#ksrtextopsset_body_multipart)
* [KSR.textops.set_body_multipart_boundary\(\)](modules/textops/textops.md#ksrtextopsset_body_multipart_boundary)
* [KSR.textops.set_body_multipart_content\(\)](modules/textops/textops.md#ksrtextopsset_body_multipart_content)
* [KSR.textops.set_body_multipart_mode\(\)](modules/textops/textops.md#ksrtextopsset_body_multipart_mode)
* [KSR.textops.set_reply_body\(\)](modules/textops/textops.md#ksrtextopsset_reply_body)
* [KSR.textops.set_reply_body_hex\(\)](modules/textops/textops.md#ksrtextopsset_reply_body_hex)
* [KSR.textops.starts_with\(\)](modules/textops/textops.md#ksrtextopsstarts_with)
* [KSR.textops.str_all_in\(\)](modules/textops/textops.md#ksrtextopsstr_all_in)
* [KSR.textops.str_any_in\(\)](modules/textops/textops.md#ksrtextopsstr_any_in)
* [KSR.textops.str_find\(\)](modules/textops/textops.md#ksrtextopsstr_find)
* [KSR.textops.str_ifind\(\)](modules/textops/textops.md#ksrtextopsstr_ifind)
* [KSR.textops.subst\(\)](modules/textops/textops.md#ksrtextopssubst)
* [KSR.textops.subst_body\(\)](modules/textops/textops.md#ksrtextopssubst_body)
* [KSR.textops.subst_hf\(\)](modules/textops/textops.md#ksrtextopssubst_hf)
* [KSR.textops.subst_uri\(\)](modules/textops/textops.md#ksrtextopssubst_uri)
* [KSR.textops.subst_user\(\)](modules/textops/textops.md#ksrtextopssubst_user)
* [KSR.textops.subst_v\(\)](modules/textops/textops.md#ksrtextopssubst_v)

## textopsx ##

* 📖[kamailio.cfg::module::textopsx.html](https://kamailio.org/docs/modules/devel/modules/textopsx.html)

Exported functions:

* [KSR.textopsx.append_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxappend_hf_value)
* [KSR.textopsx.assign_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxassign_hf_value)
* [KSR.textopsx.assign_hf_value2\(\)](modules/textopsx/textopsx.md#ksrtextopsxassign_hf_value2)
* [KSR.textopsx.bl_iterator_append\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_append)
* [KSR.textopsx.bl_iterator_end\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_end)
* [KSR.textopsx.bl_iterator_insert\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_insert)
* [KSR.textopsx.bl_iterator_next\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_next)
* [KSR.textopsx.bl_iterator_rm\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_rm)
* [KSR.textopsx.bl_iterator_start\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_start)
* [KSR.textopsx.bl_iterator_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxbl_iterator_value)
* [KSR.textopsx.change_reply_status\(\)](modules/textopsx/textopsx.md#ksrtextopsxchange_reply_status)
* [KSR.textopsx.change_reply_status_code\(\)](modules/textopsx/textopsx.md#ksrtextopsxchange_reply_status_code)
* [KSR.textopsx.exclude_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxexclude_hf_value)
* [KSR.textopsx.fnmatch\(\)](modules/textopsx/textopsx.md#ksrtextopsxfnmatch)
* [KSR.textopsx.fnmatch_ex\(\)](modules/textopsx/textopsx.md#ksrtextopsxfnmatch_ex)
* [KSR.textopsx.hf_iterator_append\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_append)
* [KSR.textopsx.hf_iterator_end\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_end)
* [KSR.textopsx.hf_iterator_hbody\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_hbody)
* [KSR.textopsx.hf_iterator_hname\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_hname)
* [KSR.textopsx.hf_iterator_insert\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_insert)
* [KSR.textopsx.hf_iterator_next\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_next)
* [KSR.textopsx.hf_iterator_prev\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_prev)
* [KSR.textopsx.hf_iterator_rm\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_rm)
* [KSR.textopsx.hf_iterator_start\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_iterator_start)
* [KSR.textopsx.hf_value_exists\(\)](modules/textopsx/textopsx.md#ksrtextopsxhf_value_exists)
* [KSR.textopsx.include_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxinclude_hf_value)
* [KSR.textopsx.insert_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxinsert_hf_value)
* [KSR.textopsx.keep_hf\(\)](modules/textopsx/textopsx.md#ksrtextopsxkeep_hf)
* [KSR.textopsx.keep_hf_re\(\)](modules/textopsx/textopsx.md#ksrtextopsxkeep_hf_re)
* [KSR.textopsx.msg_apply_changes\(\)](modules/textopsx/textopsx.md#ksrtextopsxmsg_apply_changes)
* [KSR.textopsx.msg_set_buffer\(\)](modules/textopsx/textopsx.md#ksrtextopsxmsg_set_buffer)
* [KSR.textopsx.remove_body\(\)](modules/textopsx/textopsx.md#ksrtextopsxremove_body)
* [KSR.textopsx.remove_hf_value\(\)](modules/textopsx/textopsx.md#ksrtextopsxremove_hf_value)
* [KSR.textopsx.remove_hf_value2\(\)](modules/textopsx/textopsx.md#ksrtextopsxremove_hf_value2)

## timer ##

* 📖[kamailio.cfg::module::timer.html](https://kamailio.org/docs/modules/devel/modules/timer.html)

Exported functions:

* [KSR.timer.timer_enable\(\)](modules/timer/timer.md#ksrtimertimer_enable)

## tls ##

* 📖[kamailio.cfg::module::tls.html](https://kamailio.org/docs/modules/devel/modules/tls.html)

Exported functions:

* [KSR.tls.cget\(\)](modules/tls/tls.md#ksrtlscget)
* [KSR.tls.cget\(\)](modules/tls/tls.md#ksrtlscget)
* [KSR.tls.is_peer_verified\(\)](modules/tls/tls.md#ksrtlsis_peer_verified)
* [KSR.tls.is_peer_verified\(\)](modules/tls/tls.md#ksrtlsis_peer_verified)
* [KSR.tls.set_connect_server_id\(\)](modules/tls/tls.md#ksrtlsset_connect_server_id)
* [KSR.tls.set_connect_server_id\(\)](modules/tls/tls.md#ksrtlsset_connect_server_id)

## tm ##

* 📖[kamailio.cfg::module::tm.html](https://kamailio.org/docs/modules/devel/modules/tm.html)

Exported functions:

* [KSR.tm.ki_t_load_contacts_mode\(\)](modules/tm/tm.md#ksrtmki_t_load_contacts_mode)
* [KSR.tm.t_any_replied\(\)](modules/tm/tm.md#ksrtmt_any_replied)
* [KSR.tm.t_any_timeout\(\)](modules/tm/tm.md#ksrtmt_any_timeout)
* [KSR.tm.t_branch_replied\(\)](modules/tm/tm.md#ksrtmt_branch_replied)
* [KSR.tm.t_branch_timeout\(\)](modules/tm/tm.md#ksrtmt_branch_timeout)
* [KSR.tm.t_check_status\(\)](modules/tm/tm.md#ksrtmt_check_status)
* [KSR.tm.t_check_trans\(\)](modules/tm/tm.md#ksrtmt_check_trans)
* [KSR.tm.t_clean\(\)](modules/tm/tm.md#ksrtmt_clean)
* [KSR.tm.t_drop_replies\(\)](modules/tm/tm.md#ksrtmt_drop_replies)
* [KSR.tm.t_drop_replies_all\(\)](modules/tm/tm.md#ksrtmt_drop_replies_all)
* [KSR.tm.t_exists\(\)](modules/tm/tm.md#ksrtmt_exists)
* [KSR.tm.t_get_branch_index\(\)](modules/tm/tm.md#ksrtmt_get_branch_index)
* [KSR.tm.t_get_status_code\(\)](modules/tm/tm.md#ksrtmt_get_status_code)
* [KSR.tm.t_grep_status\(\)](modules/tm/tm.md#ksrtmt_grep_status)
* [KSR.tm.t_is_canceled\(\)](modules/tm/tm.md#ksrtmt_is_canceled)
* [KSR.tm.t_is_expired\(\)](modules/tm/tm.md#ksrtmt_is_expired)
* [KSR.tm.t_is_retr_async_reply\(\)](modules/tm/tm.md#ksrtmt_is_retr_async_reply)
* [KSR.tm.t_is_set\(\)](modules/tm/tm.md#ksrtmt_is_set)
* [KSR.tm.t_load_contacts\(\)](modules/tm/tm.md#ksrtmt_load_contacts)
* [KSR.tm.t_lookup_cancel\(\)](modules/tm/tm.md#ksrtmt_lookup_cancel)
* [KSR.tm.t_lookup_cancel_flags\(\)](modules/tm/tm.md#ksrtmt_lookup_cancel_flags)
* [KSR.tm.t_lookup_request\(\)](modules/tm/tm.md#ksrtmt_lookup_request)
* [KSR.tm.t_newtran\(\)](modules/tm/tm.md#ksrtmt_newtran)
* [KSR.tm.t_next_contact_flow\(\)](modules/tm/tm.md#ksrtmt_next_contact_flow)
* [KSR.tm.t_next_contacts\(\)](modules/tm/tm.md#ksrtmt_next_contacts)
* [KSR.tm.t_on_branch\(\)](modules/tm/tm.md#ksrtmt_on_branch)
* [KSR.tm.t_on_branch_failure\(\)](modules/tm/tm.md#ksrtmt_on_branch_failure)
* [KSR.tm.t_on_failure\(\)](modules/tm/tm.md#ksrtmt_on_failure)
* [KSR.tm.t_on_reply\(\)](modules/tm/tm.md#ksrtmt_on_reply)
* [KSR.tm.t_relay\(\)](modules/tm/tm.md#ksrtmt_relay)
* [KSR.tm.t_relay_to_flags\(\)](modules/tm/tm.md#ksrtmt_relay_to_flags)
* [KSR.tm.t_relay_to_proto\(\)](modules/tm/tm.md#ksrtmt_relay_to_proto)
* [KSR.tm.t_relay_to_proto_addr\(\)](modules/tm/tm.md#ksrtmt_relay_to_proto_addr)
* [KSR.tm.t_relay_to_proxy\(\)](modules/tm/tm.md#ksrtmt_relay_to_proxy)
* [KSR.tm.t_relay_to_proxy_flags\(\)](modules/tm/tm.md#ksrtmt_relay_to_proxy_flags)
* [KSR.tm.t_release\(\)](modules/tm/tm.md#ksrtmt_release)
* [KSR.tm.t_replicate\(\)](modules/tm/tm.md#ksrtmt_replicate)
* [KSR.tm.t_reply\(\)](modules/tm/tm.md#ksrtmt_reply)
* [KSR.tm.t_reply_error\(\)](modules/tm/tm.md#ksrtmt_reply_error)
* [KSR.tm.t_reset_fr\(\)](modules/tm/tm.md#ksrtmt_reset_fr)
* [KSR.tm.t_reset_max_lifetime\(\)](modules/tm/tm.md#ksrtmt_reset_max_lifetime)
* [KSR.tm.t_reset_retr\(\)](modules/tm/tm.md#ksrtmt_reset_retr)
* [KSR.tm.t_retransmit_reply\(\)](modules/tm/tm.md#ksrtmt_retransmit_reply)
* [KSR.tm.t_save_lumps\(\)](modules/tm/tm.md#ksrtmt_save_lumps)
* [KSR.tm.t_send_reply\(\)](modules/tm/tm.md#ksrtmt_send_reply)
* [KSR.tm.t_set_auto_inv_100\(\)](modules/tm/tm.md#ksrtmt_set_auto_inv_100)
* [KSR.tm.t_set_disable_6xx\(\)](modules/tm/tm.md#ksrtmt_set_disable_6xx)
* [KSR.tm.t_set_disable_failover\(\)](modules/tm/tm.md#ksrtmt_set_disable_failover)
* [KSR.tm.t_set_disable_internal_reply\(\)](modules/tm/tm.md#ksrtmt_set_disable_internal_reply)
* [KSR.tm.t_set_fr\(\)](modules/tm/tm.md#ksrtmt_set_fr)
* [KSR.tm.t_set_fr_inv\(\)](modules/tm/tm.md#ksrtmt_set_fr_inv)
* [KSR.tm.t_set_max_lifetime\(\)](modules/tm/tm.md#ksrtmt_set_max_lifetime)
* [KSR.tm.t_set_no_auto_ack\(\)](modules/tm/tm.md#ksrtmt_set_no_auto_ack)
* [KSR.tm.t_set_no_e2e_cancel_reason\(\)](modules/tm/tm.md#ksrtmt_set_no_e2e_cancel_reason)
* [KSR.tm.t_set_retr\(\)](modules/tm/tm.md#ksrtmt_set_retr)
* [KSR.tm.t_uac_send\(\)](modules/tm/tm.md#ksrtmt_uac_send)
* [KSR.tm.t_use_uac_headers\(\)](modules/tm/tm.md#ksrtmt_use_uac_headers)

## tmrec ##

* 📖[kamailio.cfg::module::tmrec.html](https://kamailio.org/docs/modules/devel/modules/tmrec.html)

Exported functions:

* [KSR.tmrec.is_leap_year\(\)](modules/tmrec/tmrec.md#ksrtmrecis_leap_year)
* [KSR.tmrec.is_leap_year_now\(\)](modules/tmrec/tmrec.md#ksrtmrecis_leap_year_now)
* [KSR.tmrec.match\(\)](modules/tmrec/tmrec.md#ksrtmrecmatch)
* [KSR.tmrec.match_timestamp\(\)](modules/tmrec/tmrec.md#ksrtmrecmatch_timestamp)
* [KSR.tmrec.time_period_match\(\)](modules/tmrec/tmrec.md#ksrtmrectime_period_match)
* [KSR.tmrec.time_period_match_timestamp\(\)](modules/tmrec/tmrec.md#ksrtmrectime_period_match_timestamp)

## tmx ##

* 📖[kamailio.cfg::module::tmx.html](https://kamailio.org/docs/modules/devel/modules/tmx.html)

Exported functions:

* [KSR.tmx.t_cancel_branches\(\)](modules/tmx/tmx.md#ksrtmxt_cancel_branches)
* [KSR.tmx.t_cancel_callid\(\)](modules/tmx/tmx.md#ksrtmxt_cancel_callid)
* [KSR.tmx.t_cancel_callid_reason\(\)](modules/tmx/tmx.md#ksrtmxt_cancel_callid_reason)
* [KSR.tmx.t_continue\(\)](modules/tmx/tmx.md#ksrtmxt_continue)
* [KSR.tmx.t_drop\(\)](modules/tmx/tmx.md#ksrtmxt_drop)
* [KSR.tmx.t_drop_rcode\(\)](modules/tmx/tmx.md#ksrtmxt_drop_rcode)
* [KSR.tmx.t_flush_flags\(\)](modules/tmx/tmx.md#ksrtmxt_flush_flags)
* [KSR.tmx.t_flush_xflags\(\)](modules/tmx/tmx.md#ksrtmxt_flush_xflags)
* [KSR.tmx.t_is_branch_route\(\)](modules/tmx/tmx.md#ksrtmxt_is_branch_route)
* [KSR.tmx.t_is_failure_route\(\)](modules/tmx/tmx.md#ksrtmxt_is_failure_route)
* [KSR.tmx.t_is_reply_route\(\)](modules/tmx/tmx.md#ksrtmxt_is_reply_route)
* [KSR.tmx.t_is_request_route\(\)](modules/tmx/tmx.md#ksrtmxt_is_request_route)
* [KSR.tmx.t_precheck_trans\(\)](modules/tmx/tmx.md#ksrtmxt_precheck_trans)
* [KSR.tmx.t_reply_callid\(\)](modules/tmx/tmx.md#ksrtmxt_reply_callid)
* [KSR.tmx.t_reuse_branch\(\)](modules/tmx/tmx.md#ksrtmxt_reuse_branch)
* [KSR.tmx.t_suspend\(\)](modules/tmx/tmx.md#ksrtmxt_suspend)
* [KSR.tmx.t_uac_ack_local\(\)](modules/tmx/tmx.md#ksrtmxt_uac_ack_local)

## topos ##

* 📖[kamailio.cfg::module::topos.html](https://kamailio.org/docs/modules/devel/modules/topos.html)

Exported functions:

* [KSR.topos.tps_set_context\(\)](modules/topos/topos.md#ksrtopostps_set_context)

## tsilo ##

* 📖[kamailio.cfg::module::tsilo.html](https://kamailio.org/docs/modules/devel/modules/tsilo.html)

Exported functions:

* [KSR.tsilo.ts_append\(\)](modules/tsilo/tsilo.md#ksrtsilots_append)
* [KSR.tsilo.ts_append_by_contact\(\)](modules/tsilo/tsilo.md#ksrtsilots_append_by_contact)
* [KSR.tsilo.ts_append_by_contact_uri\(\)](modules/tsilo/tsilo.md#ksrtsilots_append_by_contact_uri)
* [KSR.tsilo.ts_append_to\(\)](modules/tsilo/tsilo.md#ksrtsilots_append_to)
* [KSR.tsilo.ts_append_to_uri\(\)](modules/tsilo/tsilo.md#ksrtsilots_append_to_uri)
* [KSR.tsilo.ts_store\(\)](modules/tsilo/tsilo.md#ksrtsilots_store)
* [KSR.tsilo.ts_store_uri\(\)](modules/tsilo/tsilo.md#ksrtsilots_store_uri)

## uac ##

* 📖[kamailio.cfg::module::uac.html](https://kamailio.org/docs/modules/devel/modules/uac.html)

Exported functions:

* [KSR.uac.uac_auth\(\)](modules/uac/uac.md#ksruacuac_auth)
* [KSR.uac.uac_auth_mode\(\)](modules/uac/uac.md#ksruacuac_auth_mode)
* [KSR.uac.uac_reg_disable\(\)](modules/uac/uac.md#ksruacuac_reg_disable)
* [KSR.uac.uac_reg_enable\(\)](modules/uac/uac.md#ksruacuac_reg_enable)
* [KSR.uac.uac_reg_lookup\(\)](modules/uac/uac.md#ksruacuac_reg_lookup)
* [KSR.uac.uac_reg_lookup_uri\(\)](modules/uac/uac.md#ksruacuac_reg_lookup_uri)
* [KSR.uac.uac_reg_refresh\(\)](modules/uac/uac.md#ksruacuac_reg_refresh)
* [KSR.uac.uac_reg_request_to\(\)](modules/uac/uac.md#ksruacuac_reg_request_to)
* [KSR.uac.uac_reg_status\(\)](modules/uac/uac.md#ksruacuac_reg_status)
* [KSR.uac.uac_replace_from\(\)](modules/uac/uac.md#ksruacuac_replace_from)
* [KSR.uac.uac_replace_from_uri\(\)](modules/uac/uac.md#ksruacuac_replace_from_uri)
* [KSR.uac.uac_replace_to\(\)](modules/uac/uac.md#ksruacuac_replace_to)
* [KSR.uac.uac_replace_to_uri\(\)](modules/uac/uac.md#ksruacuac_replace_to_uri)
* [KSR.uac.uac_req_send\(\)](modules/uac/uac.md#ksruacuac_req_send)
* [KSR.uac.uac_restore_from\(\)](modules/uac/uac.md#ksruacuac_restore_from)
* [KSR.uac.uac_restore_to\(\)](modules/uac/uac.md#ksruacuac_restore_to)

## uac_redirect ##

* 📖[kamailio.cfg::module::uac_redirect.html](https://kamailio.org/docs/modules/devel/modules/uac_redirect.html)

Exported functions:

* [KSR.uac_redirect.get_redirects\(\)](modules/uac_redirect/uac_redirect.md#ksruac_redirectget_redirects)
* [KSR.uac_redirect.get_redirects_acc\(\)](modules/uac_redirect/uac_redirect.md#ksruac_redirectget_redirects_acc)
* [KSR.uac_redirect.get_redirects_all\(\)](modules/uac_redirect/uac_redirect.md#ksruac_redirectget_redirects_all)

## uri_db ##

* 📖[kamailio.cfg::module::uri_db.html](https://kamailio.org/docs/modules/devel/modules/uri_db.html)

Exported functions:

* [KSR.uri_db.check_from\(\)](modules/uri_db/uri_db.md#ksruri_dbcheck_from)
* [KSR.uri_db.check_to\(\)](modules/uri_db/uri_db.md#ksruri_dbcheck_to)
* [KSR.uri_db.check_uri\(\)](modules/uri_db/uri_db.md#ksruri_dbcheck_uri)
* [KSR.uri_db.check_uri_realm\(\)](modules/uri_db/uri_db.md#ksruri_dbcheck_uri_realm)
* [KSR.uri_db.does_uri_exist\(\)](modules/uri_db/uri_db.md#ksruri_dbdoes_uri_exist)

## userblocklist ##

* 📖[kamailio.cfg::module::userblocklist.html](https://kamailio.org/docs/modules/devel/modules/userblocklist.html)

Exported functions:

* [KSR.userblocklist.check_allowlist\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_allowlist)
* [KSR.userblocklist.check_blocklist\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_blocklist)
* [KSR.userblocklist.check_global_blocklist\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_global_blocklist)
* [KSR.userblocklist.check_user_allowlist\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_allowlist)
* [KSR.userblocklist.check_user_allowlist_number\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_allowlist_number)
* [KSR.userblocklist.check_user_allowlist_table\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_allowlist_table)
* [KSR.userblocklist.check_user_blocklist\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_blocklist)
* [KSR.userblocklist.check_user_blocklist_number\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_blocklist_number)
* [KSR.userblocklist.check_user_blocklist_table\(\)](modules/userblocklist/userblocklist.md#ksruserblocklistcheck_user_blocklist_table)

## utils ##

* 📖[kamailio.cfg::module::utils.html](https://kamailio.org/docs/modules/devel/modules/utils.html)

Exported functions:

* [KSR.utils.xcap_auth_status\(\)](modules/utils/utils.md#ksrutilsxcap_auth_status)

## uuid ##

* 📖[kamailio.cfg::module::uuid.html](https://kamailio.org/docs/modules/devel/modules/uuid.html)

Exported functions:

* [KSR.uuid.get\(\)](modules/uuid/uuid.md#ksruuidget)
* [KSR.uuid.rget\(\)](modules/uuid/uuid.md#ksruuidrget)
* [KSR.uuid.tget\(\)](modules/uuid/uuid.md#ksruuidtget)
* [KSR.uuid.v7get\(\)](modules/uuid/uuid.md#ksruuidv7get)

## websocket ##

* 📖[kamailio.cfg::module::websocket.html](https://kamailio.org/docs/modules/devel/modules/websocket.html)

Exported functions:

* [KSR.websocket.close\(\)](modules/websocket/websocket.md#ksrwebsocketclose)
* [KSR.websocket.close_conid\(\)](modules/websocket/websocket.md#ksrwebsocketclose_conid)
* [KSR.websocket.close_reason\(\)](modules/websocket/websocket.md#ksrwebsocketclose_reason)
* [KSR.websocket.connect\(\)](modules/websocket/websocket.md#ksrwebsocketconnect)
* [KSR.websocket.handle_handshake\(\)](modules/websocket/websocket.md#ksrwebsockethandle_handshake)
* [KSR.websocket.send\(\)](modules/websocket/websocket.md#ksrwebsocketsend)

## xcap_server ##

* 📖[kamailio.cfg::module::xcap_server.html](https://kamailio.org/docs/modules/devel/modules/xcap_server.html)

Exported functions:

* [KSR.xcap_server.xcaps_del\(\)](modules/xcap_server/xcap_server.md#ksrxcap_serverxcaps_del)
* [KSR.xcap_server.xcaps_get\(\)](modules/xcap_server/xcap_server.md#ksrxcap_serverxcaps_get)
* [KSR.xcap_server.xcaps_put\(\)](modules/xcap_server/xcap_server.md#ksrxcap_serverxcaps_put)

## xhttp ##

* 📖[kamailio.cfg::module::xhttp.html](https://kamailio.org/docs/modules/devel/modules/xhttp.html)

Exported functions:

* [KSR.xhttp.get_hu\(\)](modules/xhttp/xhttp.md#ksrxhttpget_hu)
* [KSR.xhttp.xhttp_reply\(\)](modules/xhttp/xhttp.md#ksrxhttpxhttp_reply)

## xhttp_pi ##

* 📖[kamailio.cfg::module::xhttp_pi.html](https://kamailio.org/docs/modules/devel/modules/xhttp_pi.html)

Exported functions:

* [KSR.xhttp_pi.dispatch\(\)](modules/xhttp_pi/xhttp_pi.md#ksrxhttp_pidispatch)

## xhttp_prom ##

* 📖[kamailio.cfg::module::xhttp_prom.html](https://kamailio.org/docs/modules/devel/modules/xhttp_prom.html)

Exported functions:

* [KSR.xhttp_prom.check_uri\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcheck_uri)
* [KSR.xhttp_prom.counter_inc_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_inc_l0)
* [KSR.xhttp_prom.counter_inc_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_inc_l1)
* [KSR.xhttp_prom.counter_inc_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_inc_l2)
* [KSR.xhttp_prom.counter_inc_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_inc_l3)
* [KSR.xhttp_prom.counter_reset_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_reset_l0)
* [KSR.xhttp_prom.counter_reset_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_reset_l1)
* [KSR.xhttp_prom.counter_reset_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_reset_l2)
* [KSR.xhttp_prom.counter_reset_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promcounter_reset_l3)
* [KSR.xhttp_prom.dispatch\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promdispatch)
* [KSR.xhttp_prom.gauge_inc_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_inc_l0)
* [KSR.xhttp_prom.gauge_inc_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_inc_l1)
* [KSR.xhttp_prom.gauge_inc_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_inc_l2)
* [KSR.xhttp_prom.gauge_inc_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_inc_l3)
* [KSR.xhttp_prom.gauge_reset_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_reset_l0)
* [KSR.xhttp_prom.gauge_reset_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_reset_l1)
* [KSR.xhttp_prom.gauge_reset_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_reset_l2)
* [KSR.xhttp_prom.gauge_reset_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_reset_l3)
* [KSR.xhttp_prom.gauge_set_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_set_l0)
* [KSR.xhttp_prom.gauge_set_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_set_l1)
* [KSR.xhttp_prom.gauge_set_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_set_l2)
* [KSR.xhttp_prom.gauge_set_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promgauge_set_l3)
* [KSR.xhttp_prom.histogram_observe_l0\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promhistogram_observe_l0)
* [KSR.xhttp_prom.histogram_observe_l1\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promhistogram_observe_l1)
* [KSR.xhttp_prom.histogram_observe_l2\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promhistogram_observe_l2)
* [KSR.xhttp_prom.histogram_observe_l3\(\)](modules/xhttp_prom/xhttp_prom.md#ksrxhttp_promhistogram_observe_l3)

## xhttp_rpc ##

* 📖[kamailio.cfg::module::xhttp_rpc.html](https://kamailio.org/docs/modules/devel/modules/xhttp_rpc.html)

Exported functions:

* [KSR.xhttp_rpc.dispatch\(\)](modules/xhttp_rpc/xhttp_rpc.md#ksrxhttp_rpcdispatch)

## xlog ##

* 📖[kamailio.cfg::module::xlog.html](https://kamailio.org/docs/modules/devel/modules/xlog.html)

Exported functions:

* [KSR.xlog.xalert\(\)](modules/xlog/xlog.md#ksrxlogxalert)
* [KSR.xlog.xcrit\(\)](modules/xlog/xlog.md#ksrxlogxcrit)
* [KSR.xlog.xdbg\(\)](modules/xlog/xlog.md#ksrxlogxdbg)
* [KSR.xlog.xerr\(\)](modules/xlog/xlog.md#ksrxlogxerr)
* [KSR.xlog.xinfo\(\)](modules/xlog/xlog.md#ksrxlogxinfo)
* [KSR.xlog.xlog\(\)](modules/xlog/xlog.md#ksrxlogxlog)
* [KSR.xlog.xlog_facility\(\)](modules/xlog/xlog.md#ksrxlogxlog_facility)
* [KSR.xlog.xnotice\(\)](modules/xlog/xlog.md#ksrxlogxnotice)
* [KSR.xlog.xwarn\(\)](modules/xlog/xlog.md#ksrxlogxwarn)

## xmlrpc ##

* 📖[kamailio.cfg::module::xmlrpc.html](https://kamailio.org/docs/modules/devel/modules/xmlrpc.html)

Exported functions:

* [KSR.xmlrpc.dispatch_rpc\(\)](modules/xmlrpc/xmlrpc.md#ksrxmlrpcdispatch_rpc)
* [KSR.xmlrpc.xmlrpc_reply\(\)](modules/xmlrpc/xmlrpc.md#ksrxmlrpcxmlrpc_reply)
