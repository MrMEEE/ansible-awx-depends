%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name uwsgitop
%define version 0.10
%define unmangled_version 0.10
%define unmangled_version 0.10
%define release 1

Summary: uWSGI top-like interface
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: uwsgitop-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Riccardo Magliocchetti <riccardo.magliocchetti@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>


%description
uwsgitop
========

``uwsgitop`` is a top-like command that uses the uWSGI Stats Server to
monitor your uwsgi application.

To use uWSGI Stat Server simply use the ``stats`` option followed by
a valid socket address, for example::

    uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket

To start monitoring your application with ``uwsgitop`` call it with
the socket address like so::

    uwsgitop /tmp/stats.socket

If you want the stats served over HTTP you will need to add
the ``stats-http`` option in uWSGI::

    uwsgi --module myapp --http :3030 --stats :3031 --stats-http

You'll now need to call uwsgitop as::

    uwsgitop http://127.0.0.1:3031

Installation
------------

::

    pip install uwsgitop

Usage
-----

To display async core statistics (e.g. when using gevent) or to switch between
core statistics display mode, press ``a``. To refresh the screen super fast press ``f``,
and to quit, press ``q``.

+--------+---------------------------------------------------------------+
| Field  |  Description                                                  |
+========+===============================================================+
| WID    | Worker ID                                                     |
+--------+---------------------------------------------------------------+
| %      | Worker usage                                                  |
+--------+---------------------------------------------------------------+
| PID    | Worker PID                                                    |
+--------+---------------------------------------------------------------+
| REQ    | How many requests worker did since worker (re)spawn           |
+--------+---------------------------------------------------------------+
| RPS    | Requests per second                                           |
+--------+---------------------------------------------------------------+
| EXC    | Exceptions                                                    |
+--------+---------------------------------------------------------------+
| STATUS | Worker is busy or free to use?                                |
+--------+---------------------------------------------------------------+
| AVG    | Average request time                                          |
+--------+---------------------------------------------------------------+
| RSS    | Worker RSS (Resident Set Size, see linux memory management)   |
+--------+---------------------------------------------------------------+
| VSZ    | Worker VSZ (Virtual Memory Size, see linux memory management) |
+--------+---------------------------------------------------------------+
| TX     | How many data was transmitted by worker                       |
+--------+---------------------------------------------------------------+
| RunT   | How long worker is working                                    |
+--------+---------------------------------------------------------------+

Colors
------

Lines would be displayed in different colors:

- default console text color, if the worker is idle
- ``green``, if the worker is busy
- ``magenta``, if the worker is in ``cheap`` mode
- ``yellow``, if the worker is handling an uwsgi signal
- ``blue``, if the worker is ``suspended``


Remember to enable ``memory-report`` in your uwsgi configuration to see how
much memory resources your uwsgi processes are consuming.

Further Reading
---------------

For more info on uWSGI Stats Server see http://projects.unbit.it/uwsgi/wiki/StatsServer



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n uwsgitop-%{unmangled_version} -n uwsgitop-%{unmangled_version}
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
