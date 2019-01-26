%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name constantly
%define version 15.1.0
%define unmangled_version 15.1.0
%define unmangled_version 15.1.0
%define release 1

Summary: Symbolic constants in Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: constantly-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Twisted Matrix Labs Developers <UNKNOWN>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/twisted/constantly


%description
Constantly
==========

A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.


Tests
-----

To run tests::

    $ tox

This will run tests on Python 2.7, 3.3, 3.4, and PyPy, as well as doing coverage and pyflakes checks.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n constantly-%{unmangled_version} -n constantly-%{unmangled_version}
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
