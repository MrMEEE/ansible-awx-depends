%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.classes
%define version 1.4.3
%define unmangled_version 1.4.3
%define unmangled_version 1.4.3
%define release 1

Summary: Utility functions for Python class constructs
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.classes-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.classes


%description
.. image:: https://img.shields.io/pypi/v/jaraco.classes.svg
   :target: https://pypi.org/project/jaraco.classes

.. image:: https://img.shields.io/pypi/pyversions/jaraco.classes.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.classes/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.classes

.. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
   :target: http://skeleton.readthedocs.io/en/latest/?badge=latest



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.classes-%{unmangled_version} -n jaraco.classes-%{unmangled_version}
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
