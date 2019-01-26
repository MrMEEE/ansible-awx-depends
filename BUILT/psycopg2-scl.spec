%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name psycopg2
%define version 2.7.3.2
%define unmangled_version 2.7.3.2
%define unmangled_version 2.7.3.2
%define release 1

Summary: psycopg2 - Python-PostgreSQL Database Adapter
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: psycopg2-%{unmangled_version}.tar.gz
License: LGPL with exceptions or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Federico Di Gregorio <fog@initd.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://initd.org/psycopg/


%description
Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of concurrent "INSERT"s or "UPDATE"s.

Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being
both efficient and secure.  It features client-side and server-side cursors,
asynchronous communication and notifications, "COPY TO/COPY FROM" support.
Many Python types are supported out-of-the-box and adapted to matching
PostgreSQL data types; adaptation can be extended and customized thanks to a
flexible objects adaptation system.

Psycopg 2 is both Unicode and Python 3 friendly.


Documentation
-------------

Documentation is included in the ``doc`` directory and is `available online`__.

.. __: http://initd.org/psycopg/docs/


Installation
------------

If your ``pip`` version supports wheel_ packages it should be possible to
install a binary version of Psycopg including all the dependencies from PyPI_.
Just run::

    $ pip install -U pip      # make sure your pip is up-to-date
    $ pip install psycopg2

If you want to build Psycopg from source you will need some prerequisites (a C
compiler, development packages): please check the install_ and the faq_
documents in the ``doc`` dir for the details.

.. _wheel: http://pythonwheels.com/
.. _PyPI: https://pypi.python.org/pypi/psycopg2
.. _install: http://initd.org/psycopg/docs/install.html#install-from-source
.. _faq: http://initd.org/psycopg/docs/faq.html#faq-compile

For any other resource (source code repository, bug tracker, mailing list)
please check the `project homepage`__.

.. __: http://initd.org/psycopg/


:Linux/OSX: |travis|
:Windows: |appveyor|

.. |travis| image:: https://travis-ci.org/psycopg/psycopg2.svg?branch=master
    :target: https://travis-ci.org/psycopg/psycopg2
    :alt: Linux and OSX build status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/psycopg/psycopg2?branch=master&svg=true
    :target: https://ci.appveyor.com/project/psycopg/psycopg2/branch/master
    :alt: Windows build status



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n psycopg2-%{unmangled_version} -n psycopg2-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" PATH=$PATH:/opt/rh/rh-postgresql10/root/usr/bin/ python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
PATH=$PATH:/opt/rh/rh-postgresql10/root/usr/bin/ python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
