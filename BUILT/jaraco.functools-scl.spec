%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.functools
%define version 1.17
%define unmangled_version 1.17
%define unmangled_version 1.17
%define release 1

Summary: jaraco.functools
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.functools-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.functools


%description
.. image:: https://img.shields.io/pypi/v/jaraco.functools.svg
   :target: https://pypi.org/project/jaraco.functools

.. image:: https://img.shields.io/pypi/pyversions/jaraco.functools.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.functools/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.functools

.. image:: https://readthedocs.org/projects/jaracofunctools/badge/?version=latest
   :target: http://jaracofunctools.readthedocs.io/en/latest/?badge=latest

Additional functools in the spirit of stdlib's functools.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.functools-%{unmangled_version} -n jaraco.functools-%{unmangled_version}
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
