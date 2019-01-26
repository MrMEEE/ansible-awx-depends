%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name stevedore
%define version 1.28.0
%define unmangled_version 1.28.0
%define unmangled_version 1.28.0
%define release 1

Summary: Manage dynamic plugins for Python applications
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}stevedore
Version: %{version}
Release: %{release}
Source0: stevedore-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/stevedore-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://docs.openstack.org/stevedore/latest/


%description
===========================================================
stevedore -- Manage dynamic plugins for Python applications
===========================================================

.. image:: https://img.shields.io/pypi/v/stevedore.svg
    :target: https://pypi.python.org/pypi/stevedore/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/stevedore.svg
    :target: https://pypi.python.org/pypi/stevedore/
    :alt: Downloads

.. image:: http://governance.openstack.org/badges/stevedore.svg
    :target: http://governance.openstack.org/reference/tags/index.html

Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("*plugins*") at runtime. Many applications implement their own
library for doing this, using ``__import__`` or ``importlib``.
stevedore avoids creating yet another extension
mechanism by building on top of `setuptools entry points`_. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

.. _setuptools entry points: http://setuptools.readthedocs.io/en/latest/pkg_resources.html?#entry-points

* Free software: Apache license
* Documentation: https://docs.openstack.org/stevedore/latest
* Source: https://git.openstack.org/cgit/openstack/stevedore
* Bugs: https://bugs.launchpad.net/python-stevedore




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n stevedore-%{unmangled_version} -n stevedore-%{unmangled_version}
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
