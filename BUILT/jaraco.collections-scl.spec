%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.collections
%define version 1.5.3
%define unmangled_version 1.5.3
%define unmangled_version 1.5.3
%define release 1

Summary: jaraco.collections
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.collections-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.collections


%description
.. image:: https://img.shields.io/pypi/v/jaraco.collections.svg
   :target: https://pypi.io/project/jaraco.collections

.. image:: https://img.shields.io/pypi/pyversions/jaraco.collections.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.collections/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.collections

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. image:: https://readthedocs.org/projects/jaracocollections/badge/?version=latest
   :target: https://jaracocollections.readthedocs.io/en/latest/?badge=latest

Models and classes to supplement the stdlib 'collections' module.

RangeMap
--------

A dictionary-like object that maps a range of values to a given value.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.collections-%{unmangled_version} -n jaraco.collections-%{unmangled_version}
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
