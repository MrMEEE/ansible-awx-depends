%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name python-dateutil
%define version 2.7.2
%define unmangled_version 2.7.2
%define unmangled_version 2.7.2
%define release 1

Summary: Extensions to the standard Python datetime module
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: python-dateutil-%{unmangled_version}.tar.gz
License: Dual License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Paul Ganssle <dateutil@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://dateutil.readthedocs.io


%description
dateutil - powerful extensions to datetime
==========================================

.. image:: https://img.shields.io/pypi/v/python-dateutil.svg?style=flat-square
    :target: https://pypi.org/project/python-dateutil/
    :alt: pypi version

.. image:: https://img.shields.io/travis/dateutil/dateutil/master.svg?style=flat-square
    :target: https://travis-ci.org/dateutil/dateutil
    :alt: travis build status

.. image:: https://img.shields.io/appveyor/ci/dateutil/dateutil/master.svg?style=flat-square
    :target: https://ci.appveyor.com/project/dateutil/dateutil
    :alt: appveyor build status

.. image:: https://codecov.io/github/dateutil/dateutil/coverage.svg?branch=master
    :target: https://codecov.io/github/dateutil/dateutil?branch=master
    :alt: Code coverage

.. image:: https://badges.gitter.im/dateutil/dateutil.svg
   :alt: Join the chat at https://gitter.im/dateutil/dateutil
   :target: https://gitter.im/dateutil/dateutil


The `dateutil` module provides powerful extensions to
the standard `datetime` module, available in Python.


Download
========
dateutil is available on PyPI
https://pypi.org/project/python-dateutil/

The documentation is hosted at:
https://dateutil.readthedocs.io/en/stable/

Code
====
The code and issue tracker are hosted on Github:
https://github.com/dateutil/dateutil/

Features
========

* Computing of relative deltas (next month, next year,
  next monday, last week of month, etc);
* Computing of relative deltas between two given
  date and/or datetime objects;
* Computing of dates based on very flexible recurrence rules,
  using a superset of the `iCalendar <https://www.ietf.org/rfc/rfc2445.txt>`_
  specification. Parsing of RFC strings is supported as well.
* Generic parsing of dates in almost any string format;
* Timezone (tzinfo) implementations for tzfile(5) format
  files (/etc/localtime, /usr/share/zoneinfo, etc), TZ
  environment string (in all known formats), iCalendar
  format files, given ranges (with help from relative deltas),
  local machine timezone, fixed offset timezone, UTC timezone,
  and Windows registry-based time zones.
* Internal up-to-date world timezone information based on
  Olson's database.
* Computing of Easter Sunday dates for any given year,
  using Western, Orthodox or Julian algorithms;
* A comprehensive test suite.

Quick example
=============
Here's a snapshot, just to give an idea about the power of the
package. For more examples, look at the documentation.

Suppose you want to know how much time is left, in
years/months/days/etc, before the next easter happening on a
year with a Friday 13th in August, and you want to get today's
date out of the "date" unix system command. Here is the code:

.. code-block:: python3

    >>> from dateutil.relativedelta import *
    >>> from dateutil.easter import *
    >>> from dateutil.rrule import *
    >>> from dateutil.parser import *
    >>> from datetime import *
    >>> now = parse("Sat Oct 11 17:13:46 UTC 2003")
    >>> today = now.date()
    >>> year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
    >>> rdelta = relativedelta(easter(year), today)
    >>> print("Today is: %s" % today)
    Today is: 2003-10-11
    >>> print("Year with next Aug 13th on a Friday is: %s" % year)
    Year with next Aug 13th on a Friday is: 2004
    >>> print("How far is the Easter of that year: %s" % rdelta)
    How far is the Easter of that year: relativedelta(months=+6)
    >>> print("And the Easter of that year is: %s" % (today+rdelta))
    And the Easter of that year is: 2004-04-11

Being exactly 6 months ahead was **really** a coincidence :)

Contributing
============

We welcome many types of contributions - bug reports, pull requests (code, infrastructure or documentation fixes). For more information about how to contribute to the project, see the ``CONTRIBUTING.md`` file in the repository.


Author
======
The dateutil module was written by Gustavo Niemeyer <gustavo@niemeyer.net>
in 2003.

It is maintained by:

* Gustavo Niemeyer <gustavo@niemeyer.net> 2003-2011
* Tomi Pieviläinen <tomi.pievilainen@iki.fi> 2012-2014
* Yaron de Leeuw <me@jarondl.net> 2014-2016
* Paul Ganssle <paul@ganssle.io> 2015-

Starting with version 2.4.1, all source and binary distributions will be signed
by a PGP key that has, at the very least, been signed by the key which made the
previous release. A table of release signing keys can be found below:

Starting with version 2.4.1, all source and binary distributions will be signed
by a PGP key that has, at the very least, been signed by the key which made the
previous release. A table of release signing keys can be found below:

===========  ============================
Releases     Signing key fingerprint
===========  ============================
2.4.1-       `6B49 ACBA DCF6 BD1C A206 67AB CD54 FCE3 D964 BEFB`_
===========  ============================


Contact
=======
Our mailing list is available at `dateutil@python.org <https://mail.python.org/mailman/listinfo/dateutil>`_. As it is hosted by the PSF, it is subject to the `PSF code of
conduct <https://www.python.org/psf/codeofconduct/>`_.

License
=======

All contributions after December 1, 2017 released under dual license - either `Apache 2.0 License <https://www.apache.org/licenses/LICENSE-2.0>`_ or the `BSD 3-Clause License <https://opensource.org/licenses/BSD-3-Clause>`_. Contributions before December 1, 2017 - except those those explicitly relicensed - are released only under the BSD 3-Clause License.


.. _6B49 ACBA DCF6 BD1C A206 67AB CD54 FCE3 D964 BEFB:
   https://pgp.mit.edu/pks/lookup?op=vindex&search=0xCD54FCE3D964BEFB



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n python-dateutil-%{unmangled_version} -n python-dateutil-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
