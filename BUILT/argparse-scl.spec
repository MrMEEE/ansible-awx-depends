%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name argparse
%define version 1.4.0
%define unmangled_version 1.4.0
%define unmangled_version 1.4.0
%define release 1

Summary: Python command-line parsing library
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: argparse-%{unmangled_version}.tar.gz
License: Python Software Foundation License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Thomas Waldmann <tw@waldmann-edv.de>
Packager: Martin Juhl <m@rtinjuhl.dk>
Requires: %{?scl_prefix}python
Url: https://github.com/ThomasWaldmann/argparse/
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires: %{?scl_prefix}python


%description
The argparse module makes it easy to write user friendly command line
interfaces.

The program defines what arguments it requires, and argparse will figure out
how to parse those out of sys.argv. The argparse module also automatically
generates help and usage messages and issues errors when users give the
program invalid arguments.

As of Python >= 2.7 and >= 3.2, the argparse module is maintained within the
Python standard library. For users who still need to support Python < 2.7 or
< 3.2, it is also provided as a separate package, which tries to stay
compatible with the module in the standard library, but also supports older
Python versions.

Also, we can fix bugs here for users who are stuck on some non-current python
version, like e.g. 3.2.3 (which has bugs that were fixed in a later 3.2.x
release).

argparse is licensed under the Python license, for details see LICENSE.txt.


Compatibility
-------------

argparse should work on Python >= 2.3, it was tested on:

* 2.3, 2.4, 2.5, 2.6 and 2.7
* 3.1, 3.2, 3.3, 3.4


Installation
------------

Try one of these:

    python setup.py install

    easy_install argparse

    pip install argparse

    putting argparse.py in some directory listed in sys.path should also work


Bugs
----

If you find a bug in argparse (pypi), please try to reproduce it with latest
python 2.7 and 3.4 (and use argparse from stdlib).

If it happens there also, please file a bug in the python.org issue tracker.
If it does not happen there, file a bug in the argparse package issue tracker.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n argparse-%{unmangled_version} -n argparse-%{unmangled_version}
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
%doc  README.txt LICENSE.txt PKG-INFO doc/
