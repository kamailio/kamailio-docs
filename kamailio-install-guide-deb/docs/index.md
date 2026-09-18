# Install Kamailio On Debian #

For more details about Kamailio Project visit: [kamailio.org](https://www.kamailio.org).

## Overview ##

Kamailio packages are included in the official Debian Stable repository since version 8.0,
and continues to be in the current Stable (13.x, codename Trixie).

This tutorial should just work for latest Ubuntu versions as well.

**_The focus of this tutorial is to install Kamailio with MySQL backend using
deb packages._**

### Alternative APT Repositories ###

Debian Stable includes the Kamailio version which was available at the time of
their release. Giving that Debian is releasing a new major version like every
2 years, the Kamailio included in the distro can be older than the current stable
release.

If you want to use a more recent version of Kamailio, you can use the APT repositories
hosted by Kamailio project.

The list of `APT` repositories offered by `Kamailio` project for
various `Debian` or `Ubuntu` versions, including nightly builds for stable and
development versions, is presented at:

  * [Kamailio APT Repos: Debian - Ubuntu](https://deb.kamailio.org/)

Adding the signing key for the repository:

```
wget -O- https://deb.kamailio.org/kamailiodebkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/kamailio.gpg
```

**Note:** if you downloaded the key in the past, you may need to delete the old key
and download the new one.

For example, if you want to install Kamailio v6.1.x on Debian Bullseye (11.x), add the next
URLs to APT configuration:

```
deb     [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 bullseye main
deb-src [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 bullseye main
```

For Debian Bookworm (12.x):

```
deb     [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 bookworm main
deb-src [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 bookworm main
```

For Debian Trixie (13.x):

```
deb     [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 trixie main
deb-src [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61 trixie main
```

For older Debian/Ubuntu versions, adding signing key for the repository is done with:

```
wget -O- http://deb.kamailio.org/kamailiodebkey.gpg | sudo apt-key add -
```

The repository URLs are:

```
deb     http://deb.kamailio.org/kamailio61 buster main
deb-src http://deb.kamailio.org/kamailio61 buster main
```

To install Kamailio `6.0.x` series instead of `6.1.x`, replace `kamailio61` with
`kamailio60` in the URLs above.

### Deb Nightly Builds ###

Packages are also built on a nightly basis from the `6.1` stable branch and are
available at `kamailio61-nightly` target. As an example, for Debian Bookworm (12.x):

```
deb     [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61-nightly bookworm main
deb-src [signed-by=/usr/share/keyrings/kamailio.gpg] http://deb.kamailio.org/kamailio61-nightly bookworm main
```

### APT Repositories Archive ###

The APT repositories linked in the previous session contain only the packages for
the latest versions of Kamailio from stable branches. If you want to install
an older version or rollback to an older version, use the repositories listed at:

  * [APT Repositories Archive](https://deb-archive.kamailio.org/)

For example, to install Kamailio v6.0.2, add the next URL to APT configuration:

```
deb https://deb-archive.kamailio.org/repos/kamailio-6.0.2
```

## APT Install Commands ###

The `apt` tool is used for installing the packages. First run the `update`
command to sync with the remote repository, then install `MySQL` server,
`Kamailio` **core** and **mysql** packages.


```Shell
apt update
apt install default-mysql-server
apt install kamailio kamailio-mysql-modules
```

Once the above commands are finished, you can check if `kamailio` application
is available:


```Shell
which kamailio
```

There are many Kamailio packages specific for various modules. You can see all
available with:


```Shell
apt search kamailio
```

For example, to be able to load `websocket` module, you have to install the
package `kamailio-websocket-modules`:

```Shell
apt install kamailio-websocket-modules
```

## Configuration Files ##

Configuration files are located in `/etc/kamailio/` folder.

### kamctlrc ###

The `/etc/kamailio/kamctlrc` is the configuration file for `kamctl` and
`kamdbctl` tools. You need to edit it and set the `SIP_DOMAIN` to your SIP
service domain (or IP address if you don't have a DNS hostname associated with
your SIP service).

Set also the `DBENGINE` to be `MYSQL` and adjust other setting as you want. Very
important are the passwords to connect to `MySQL` server, respectively
`DBRWPW` and `DBROPW`. By default, their values are `kamailiorw` and
`kamailioro`. You should change them before executing `kamdbctl create` (step
detailed the section **Create Database**).

### kamailio.cfg ###

The `/etc/kamailio/kamailio.cfg` is the configuration file for `kamailio`.

It has to be edited to activate the instance by adding the next line after its first line.

```C
#!define ACTIVE
```

Without this line, `Kamailio` (as of end of August 2026) drops any SIP message.

Edit it further to enable some of the features shipped with it.

To enable use of `MySQL` server backend, user authentication and persistent user
location, add after the first line:

```C
#!define WITH_MYSQL
#!define WITH_AUTH
#!define WITH_USRLOCDB
```

## Create Database ##

To create the database structure needed by `Kamailio`, run:

```Shell
kamdbctl create
```

The database name created in `MySQL` is `kamailio`. Two access users to
`MySQL` server were created:

  * **kamailio** - (with password set by `DBRWPW` in `kamctlrc`) - user which
  has full access rights to `kamailio` database

  * **kamailioro** - ((with password set by `DBROPW` in `kamctlrc`) - user which
  has read-only access rights to `kamailio` database

The access for the two users is restricted to `localhost`, but as advised above,
it is recommended to change their default passwords.

If you changed the value of `DBRWPW` in `kamctlrc`, you must update the value
of `DBURL` define inside `kamailio.cfg`.

```C
#!define DBURL "mysql://kamailio:_NEW_DBRWPW_@localhost/kamailio"
```

## Startup Scripts ##

### Init.d Scripts ###

Depending on startup system, you may have an `/etc/init.d/kamailio` script that
you can use to start/stop kamailio.

First you should edit `/etc/default/kamailio` and adjust the setting for
`kamailio` startup script, in particular the one that enables `kamailio` to start.

```Shell
/etc/init.d/kamailio start
/etc/init.d/kamailio stop
```

### Systemd Scripts ###

If the default startup system is `systemd`, then `kamailio` can be managed
via `systemctl`:

```Shell
systemctl start kamailio
systemctl stop kamailio
```

First you may also need to edit `/etc/default/kamailio` and adjust the setting
for `kamailio` startup script, in particular the one that enables
`kamailio` to start.

## Adding Subscribers ##

To add subscribers (users), you can use the `kamctl` command:

```Shell
kamctl add userid password
```

Like:

```Shell
kamctl add alice secret
```

Then you can configure your phone to register to `Kamailio` using the username
and password set in the above command.

## Support ##

Questions about how to use Kamailio and the content of kamailio.cfg can be
addressed via email to:

  * [sr-users@lists.kamailio.org](https://lists.kamailio.org/cgi-bin/mailman/listinfo/sr-users)

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
