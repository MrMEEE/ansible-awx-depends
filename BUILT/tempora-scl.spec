%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name tempora
%define version 1.10
%define unmangled_version 1.10
%define unmangled_version 1.10
%define release 1

Summary: Objects and routines pertaining to date and time (tempora)
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: tempora-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/tempora


%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
   :target: https://pypi.org/project/tempora

.. image:: https://img.shields.io/pypi/pyversions/tempora.svg

.. image:: https://img.shields.io/travis/jaraco/tempora/master.svg
   :target: http://travis-ci.org/jaraco/tempora

Objects and routines pertaining to date and time (tempora).

Modules include:

 - tempora (top level package module) contains miscellaneous
   utilities and constants.
 - timing contains routines for measuring and profiling.
 - schedule contains an event scheduler.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n tempora-%{unmangled_version} -n tempora-%{unmangled_version}
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
