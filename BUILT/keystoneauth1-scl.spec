%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name keystoneauth1
%define version 3.4.0
%define unmangled_version 3.4.0
%define unmangled_version 3.4.0
%define release 1

Summary: Authentication Library for OpenStack Identity
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}keystoneauth1
Version: %{version}
Release: %{release}
Source0: keystoneauth1-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/keystoneauth1-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://docs.openstack.org/keystoneauth/latest/


%description
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/badges/keystoneauth.svg
    :target: https://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

============
keystoneauth
============

.. image:: https://img.shields.io/pypi/v/keystoneauth1.svg
    :target: https://pypi.python.org/pypi/keystoneauth1/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/keystoneauth1.svg
    :target: https://pypi.python.org/pypi/keystoneauth1/
    :alt: Downloads

This package contains tools for authenticating to an OpenStack-based cloud.
These tools include:

* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests (based on
  the requests Python library)

Further information:

* Free software: Apache license
* Documentation: https://docs.openstack.org/keystoneauth/latest/
* Source: https://git.openstack.org/cgit/openstack/keystoneauth
* Bugs: https://bugs.launchpad.net/keystoneauth




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n keystoneauth1-%{unmangled_version} -n keystoneauth1-%{unmangled_version}
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
