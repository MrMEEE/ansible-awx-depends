%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name os-client-config
%define version 1.29.0
%define unmangled_version 1.29.0
%define unmangled_version 1.29.0
%define release 1

Summary: OpenStack Client Configuation Library
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}os-client-config
Version: %{version}
Release: %{release}
Source0: os-client-config-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/os-client-config-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://docs.openstack.org/os-client-config/latest


%description
================
os-client-config
================

.. image:: http://governance.openstack.org/badges/os-client-config.svg
    :target: http://governance.openstack.org/reference/tags/index.html

`os-client-config` is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

Source
------

* Free software: Apache license
* Documentation: http://docs.openstack.org/os-client-config/latest
* Source: http://git.openstack.org/cgit/openstack/os-client-config
* Bugs: http://bugs.launchpad.net/os-client-config




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n os-client-config-%{unmangled_version} -n os-client-config-%{unmangled_version}
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
