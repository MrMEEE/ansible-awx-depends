%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name os-service-types
%define version 1.2.0
%define unmangled_version 1.2.0
%define unmangled_version 1.2.0
%define release 1

Summary: Python library for consuming OpenStack sevice-types-authority data
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}os-service-types
Version: %{version}
Release: %{release}
Source0: os-service-types-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/os-service-types-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://www.openstack.org/


%description
================
os-service-types
================

Python library for consuming OpenStack sevice-types-authority data

The `OpenStack Service Types Authority`_ contains information about official
OpenStack services and their historical ``service-type`` aliases.

The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/os-service-types
* Source: http://git.openstack.org/cgit/openstack/os-service-types
* Bugs: https://storyboard.openstack.org/#!/project/904

.. _OpenStack Service Types Authority: https://service-types.openstack.org/




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n os-service-types-%{unmangled_version} -n os-service-types-%{unmangled_version}
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
