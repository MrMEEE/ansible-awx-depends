%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.itertools
%define version 2.1.1
%define unmangled_version 2.1.1
%define unmangled_version 2.1.1
%define release 1

Summary: jaraco.itertools
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.itertools-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.itertools


%description
.. image:: https://img.shields.io/pypi/v/jaraco.itertools.svg
   :target: https://pypi.org/project/jaraco.itertools

.. image:: https://img.shields.io/pypi/pyversions/jaraco.itertools.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.itertools/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.itertools

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/jaraco.itertools/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/jaraco.itertools/branch/master

.. image:: https://readthedocs.org/projects/jaracoitertools/badge/?version=latest
   :target: https://jaracoitertools.readthedocs.io/en/latest/?badge=latest



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.itertools-%{unmangled_version} -n jaraco.itertools-%{unmangled_version}
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
