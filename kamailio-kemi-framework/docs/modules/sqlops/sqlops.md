# sqlops #

* 📖[kamailio.cfg::module::sqlops.html](https://kamailio.org/docs/modules/devel/modules/sqlops.html)

Exported functions:

* [KSR.sqlops.sql_is_null\(\)](#ksrsqlopssql_is_null)
* [KSR.sqlops.sql_num_columns\(\)](#ksrsqlopssql_num_columns)
* [KSR.sqlops.sql_num_rows\(\)](#ksrsqlopssql_num_rows)
* [KSR.sqlops.sql_pvquery\(\)](#ksrsqlopssql_pvquery)
* [KSR.sqlops.sql_query\(\)](#ksrsqlopssql_query)
* [KSR.sqlops.sql_query_async\(\)](#ksrsqlopssql_query_async)
* [KSR.sqlops.sql_result_free\(\)](#ksrsqlopssql_result_free)
* [KSR.sqlops.sql_result_get\(\)](#ksrsqlopssql_result_get)
* [KSR.sqlops.sql_result_gete\(\)](#ksrsqlopssql_result_gete)
* [KSR.sqlops.sql_result_getz\(\)](#ksrsqlopssql_result_getz)
* [KSR.sqlops.sql_xquery\(\)](#ksrsqlopssql_xquery)

## KSR.sqlops.sql_is_null ##

```cpp
int KSR.sqlops.sql_is_null(str "sres", int i, int j);
```

* 📖[kamailio.cfg::function::sql_is_null\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_is_null)

## KSR.sqlops.sql_num_columns ##

```cpp
int KSR.sqlops.sql_num_columns(str "sres");
```

* 📖[kamailio.cfg::function::sql_num_columns\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_columns)

## KSR.sqlops.sql_num_rows ##

```cpp
int KSR.sqlops.sql_num_rows(str "sres");
```

* 📖[kamailio.cfg::function::sql_num_rows\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_num_rows)

## KSR.sqlops.sql_pvquery ##

```cpp
int KSR.sqlops.sql_pvquery(str "scon", str "squery", str "sres");
```

* 📖[kamailio.cfg::function::sql_pvquery\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_pvquery)

## KSR.sqlops.sql_query ##

```cpp
int KSR.sqlops.sql_query(str "scon", str "squery", str "sres");
```

* 📖[kamailio.cfg::function::sql_query\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query)

## KSR.sqlops.sql_query_async ##

```cpp
int KSR.sqlops.sql_query_async(str "scon", str "squery");
```

* 📖[kamailio.cfg::function::sql_query_async\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_query_async)

## KSR.sqlops.sql_result_free ##

```cpp
int KSR.sqlops.sql_result_free(str "sres");
```

* 📖[kamailio.cfg::function::sql_result_free\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_free)

## KSR.sqlops.sql_result_get ##

```cpp
xval KSR.sqlops.sql_result_get(str "resid", int row, int col);
```

* 📖[kamailio.cfg::function::sql_result_get\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_get)

## KSR.sqlops.sql_result_gete ##

```cpp
xval KSR.sqlops.sql_result_gete(str "resid", int row, int col);
```

* 📖[kamailio.cfg::function::sql_result_gete\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_gete)

## KSR.sqlops.sql_result_getz ##

```cpp
xval KSR.sqlops.sql_result_getz(str "resid", int row, int col);
```

* 📖[kamailio.cfg::function::sql_result_getz\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_result_getz)

## KSR.sqlops.sql_xquery ##

```cpp
int KSR.sqlops.sql_xquery(str "scon", str "squery", str "xavp");
```

* 📖[kamailio.cfg::function::sql_xquery\(\)](https://kamailio.org/docs/modules/devel/modules/sqlops.html#sqlops.f.sql_xquery)
