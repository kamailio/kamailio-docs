# Kamailio v5.6 - Install Guide #

**Guide to install Kamailio SIP Server v5.6 (stable) from Git repository.**

For more about Kamailio Project visit: [kamailio.org](https://www.kamailio.org).

```
Main author:
   Daniel-Constantin Mierla

Support: <sr-users@lists.kamailio.org>
```

## Overview ##

This is a step by step tutorial about how to install and maintain Kamailio SIP
server development version using the sources downloaded from GIT repository -
the choice for those willing to write code for Kamailio or to try the new
features to be released in the future with the next major stable version.

*This document focuses on Kamailio v5.6.x series, installed
with MySQL/MariaDB support, using a Debian unstable system.*


## Prerequisites ##

To be able to follow the guidelines from this document you need `root` access.

The following packages are required before proceeding to the next steps.

  * __git__ client: `apt-get install git` - it is recommended to have a recent
  version, if your Linux distro has an old version, you can download newer one
  from [git-scm.com](http://git-scm.com)
  * __gcc__ and __g++__ compilers: `apt-get install gcc g++`
  * __flex__ - `apt-get install flex`
  * __bison__ - `apt-get install bison`
  * __libmysqlclient-dev__ - `apt-get install libmysqlclient-dev` (or: `apt install default-libmysqlclient-dev`)
  * __make__, __autoconf__ and __pkg-config__ - `apt-get install make autoconf pkg-config`
  * if you want to enable more modules, some of them require extra libraries:
    * __libssl__ - `apt-get install libssl-dev`
    * __libcurl__ - `apt-get install libcurl4-openssl-dev`
    * __libxml2__ - `apt-get install libxml2-dev`
    * __libpcre3__ - `apt-get install libpcre3-dev`

**Important Note**: starting with version `4.3.0`, Kamailio uses the directory
**/var/run/kamailio/** for creating FIFO and UnixSocket control files. You may have
to complete the section related to installation of `init.d` script for creating
`/var/run/kamailio` even if you plan to start Kamailio manually from command line.
The alternative is to set different paths via parameters of **jsonrpcs**
and **ctl** modules.

**Note**: __g++__ compiler is needed for couple of modules that link to C++ libraries,
such as __app_sqlang__, __phonenum__ or __ndb_cassandra__.

### MySQL Or MariaDB Server ###

To complete all the steps in this tutorial, it is required to have a **MySQL** or **MariaDB** server installed.
Consult the documentation of **MySQL** or **MariaDB** server for Debian for a proper installation.

For testing purposes, it can just be done with `apt-get install mysql-server` or `apt-get install default-mysql-server`.
During or after installation you may have to complete some configuration steps, such as setting the password for mysql root user or initialize the database system.

## Getting Sources From GIT ##

First of all, you have to create a directory on the file system where the sources
will be stored.



```Shell
  mkdir -p /usr/local/src/kamailio-5.6
  cd /usr/local/src/kamailio-5.6
```

Download the sources from GIT using the following commands.

```Shell
  git clone --depth 1 --no-single-branch https://github.com/kamailio/kamailio kamailio
  cd kamailio
  git checkout -b 5.6 origin/5.6
```

_**Note**: if your git client version does not support **--no-single-branch**
command line parameter, then just remove it._

## Tuning Makefiles ##

The first step is to generate build config files.

```Shell
  make cfg
```

Next step is to enable the MySQL module. Edit **modules.lst** file:

```Shell
  nano -w src/modules.lst
  # or
  vim src/modules.lst
```

Add **db_mysql** to the variable **include_modules**.

```Shell
include_modules= db_mysql
```

Save the **modules.lst** and exit.

**NOTE**: this is one mechanism to enable modules which are not compiled by
default, such as lcr, dialplan, tls, presence -- add the modules to
**include_modules** variable inside the **modules.lst** file, like:

```Shell
include_modules= db_mysql dialplan tls
```

Alternative is to set `include_modules` variable with the list of extra modules
to be included for compilation when building `Makefile` cfg:

```Shell
make include_modules="db_mysql dialplan tls" cfg
```

**NOTE**: If you want to install everything in one directory (so you can delete
all installed files at once), say `/usr/local/kamailio-5.6`, then set `PREFIX`
variable to the install path in `make cfg ...` command:

```Shell
make PREFIX="/usr/local/kamailio-5.6" include_modules="db_mysql dialplan tls" cfg
```

More hints about `Makefile` system at:

  * [kamailio.org/wiki/devel/makefile-system](https://www.kamailio.org/wiki/devel/makefile-system)

## Compile Kamailio ##

Once you added the mysql module to the list of enabled modules, you can compile Kamailio:

```Shell
  make all
```

You can get full compile flags output using:

```Shell
  make Q=0 all
```

## Install Kamailio ##

When the compilation is ready, install Kamailio with the following command:

```Shell
  make install
```

### What And Where Was Installed ###

The binaries and executable scripts were installed in:

```Shell
  /usr/local/sbin
```

These are:

  * __kamailio__ - Kamailio SIP server
  * __kamdbctl__ - script to create and manage the Databases
  * __kamctl__ - script to manage and control Kamailio SIP server
  * __kamcmd__ - CLI - command line tool to interface with Kamailio SIP server

To be able to use the binaries from command line, make sure that
`/usr/local/sbin` is set in `PATH` environment variable. You can check that with
`echo $PATH`. If not and you are using `bash`, open `/root/.bash_profile` and
at the end add:

```Shell
  PATH=$PATH:/usr/local/sbin
  export PATH
```

Kamailio modules are installed in:

```Shell
  /usr/local/lib/kamailio/modules/
```

Note: On 64 bit systems, `/usr/local/lib64` may be used.

The documentation and readme files are installed in:

```Shell
  /usr/local/share/doc/kamailio/
```

The man pages are installed in:

```Shell
  /usr/local/share/man/man5/
  /usr/local/share/man/man8/
```

The configuration file was installed in:

```Shell
  /usr/local/etc/kamailio/kamailio.cfg
```

**NOTE:**: In case you set the PREFIX variable in `make cfg ...` command, then
replace **/usr/local** in all paths above with the value of `PREFIX` in order to
locate the files installed.

## Create MySQL Database ##

To create the `MySQL` database, you have to use the database setup script.
First edit **kamctlrc** file to set the database server type:

```Shell
  nano -w /usr/local/etc/kamailio/kamctlrc
```

Locate `DBENGINE` variable and set it to `MYSQL`:

```Shell
DBENGINE=MYSQL
```

You can change other values in **kamctlrc** file, at least it is recommended to
change the default passwords for the users to be created to connect to database.

Note that the existing line with `DBENGINE` or other attributes may be commented,
uncomment by removing the `#` character at the beginning of the line.

Once you are done updating **kamctlrc** file, run the script to create the
database used by Kamailio:

```Shell
  /usr/local/sbin/kamdbctl create
```

You can call this script without any parameter to get some help for the usage.
You will be asked for the domain name Kamailio is going to serve (e.g.,
`mysipserver.com`) and the password of the `root` MySQL user. The script will
create a database named `kamailio` containing the tables required by Kamailio.
You can change the default settings in the kamctlrc file mentioned above.

The script will add two users in `MySQL`:

* **kamailio** - (with default password `kamailiorw`) - user which has full
access rights to `kamailio` database

* **kamailioro** - (with default password `kamailioro`) - user which has
read-only access rights to `kamailio` database

**_IMPORTANT: do change the passwords for these two users to something different
that the default values that come with sources._**

## Edit Configuration File ##

To fit your requirements for the VoIP platform, you have to edit the
configuration file.

```Shell
  /usr/local/etc/kamailio/kamailio.cfg
```

Follow the instruction in the comments to enable usage of MySQL. Basically you
have to add several lines at the top of config file, like:

```c
#!define WITH_MYSQL
#!define WITH_AUTH
#!define WITH_USRLOCDB
```

If you changed the password for the `kamailio` user of MySQL, you have to update
the value for `db_url` parameters.

You can browse [kamailio.cfg](https://github.com/kamailio/kamailio/blob/master/etc/kamailio.cfg)
online on GIT repository.

## Running Kamailio ##

There are couple of variants for starting/stopping/restarting Kamailio,
the recommended ones being via `init.d` script or `systemd` unit, a matter of
what the Debian OS is configured to use.

### Init.d Script ###

To install the `init.d` script, run in Kamailio source code directory:

```
make install-initd-debian
```

Follow any instructions that may be printed by the above commad.

Then you can start/stop Kamailio using the following commands:

```Shell
  /etc/init.d/kamailio start
  /etc/init.d/kamailio stop
```

### Systemd Unit ###

To install the `systemd` unit, run in Kamailio source code directory:

```
make install-systemd-debian
```

Follow any instructions that may be printed by the above commad.

Then you can start/stop Kamailio using the following commands:

```Shell
  systemctl start kamailio
  systemctl stop kamailio
```

### Kamctl ###

You may need to edit edit `/usr/local/etc/kamailio/kamctlrc` and set the
`PID_FILE` and `STARTOPTIONS` attributes.

The you can use:

```
kamctl start
kamctl stop
```

### Command Line ###

Kamailio can be started from command line by executing the binary with specific
parameters. For example:

  * start Kamailio

```
/usr/local/sbin/kamailio -P /var/run/kamailio/kamailio.pid -m 128 -M 12
```

  * stop Kamailio

```
killall kamailio
# or
kill -TERM $(cat /var/run/kamailio/kamailio.pid)
```

## Ready To Rock ##

Now everything is in place. You can start the VoIP service, creating new
accounts and setting the phones.

A new account can be added using `kamctl` tool via:

```Shell
  kamctl add username password

```

If `SIP_DOMAIN` was not set in `kamctlrc` file do one of the following
option.

  * run in terminal:

```Shell
  export SIP_DOMAIN=mysipserver.com
  kamctl add username password
```

  * or edit `/usr/local/etc/kamailio/kamctlrc` and add:

```Shell
  SIP_DOMAIN=mysipserver.com
```

and then run again `kamctl add ...` as above.

  * or give the username with domain in `kamctl add ...` parameter:

```Shell
  kamctl add username@mysipserver.com password

```

Instead of `mysipserver.com` it has to be given the real domain for the SIP service
or the IP address of Kamailio.

## Maintenance ##

The maintenance process is very simple right now. You have to be user `root` and
execute following commands:

```Shell
  cd /usr/local/src/kamailio-devel/kamailio
  git pull origin
  make all
  make install
  /etc/init.d/kamailio restart
```

Now you have the latest Kamailio devel running on your system.


### When To Update ###

Notification about GIT commits are sent to the mailing list:
**sr-dev@lists.kamailio.org**. Each commit notification contains the reference
to the branch where the commit has been done. If the commit message contains
the lines:

```Shell
Module: kamailio
Branch: 5.6
```

then an update has been made to Kamailio devel version and it will be available
to the public GIT in no time.

## Kamcli ##

A modern command line control tool for Kamailio is available at:

  * [https://github.com/kamailio/kamcli](https://github.com/kamailio/kamcli)

It offers an alternative to all `kamctl`/`kamdbctl`/`kamcmd`, offering internal
interactive shell with syntax highlighting, tab completion and suggestions
from history. It implements more sub-commands than kamctl and has the ability
to format the output using different styles.

## Support ##

Questions about how to use Kamailio and the content of kamailio.cfg can be
addressed via email to:

  * [sr-users@lists.kamailio.org](http://lists.kamailio.org/cgi-bin/mailman/listinfo/sr-users)

More documentation resources can be found at:

  * [www.kamailio.org/w/documentation](https://www.kamailio.org/w/documentation/)
  * [www.kamailio.org/wiki](https://www.kamailio.org/wiki/)

## Contributions ##

Anyone is welcome to contribute to this document. It is recommended to make a
pull request via:

  * [github.com/kamailio/kamailio-docs/pulls](https://github.com/kamailio/kamailio-docs/pulls)

This version of the document is in GIT branch `master`.

Errors and other issues can be reported via the tracker at:

  * [github.com/kamailio/kamailio-docs/issues](https://github.com/kamailio/kamailio-docs/issues)
