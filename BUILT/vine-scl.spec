%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name vine
%define version 1.2.0
%define unmangled_version 1.2.0
%define unmangled_version 1.2.0
%define release 1

Summary: Promises, promises, promises.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: vine-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ask Solem <ask@celeryproject.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/celery/vine


%description
=====================================================================
 vine - Python Promises
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.2.0
:Web: https://vine.readthedocs.io/
:Download: https://pypi.org/project/vine/
:Source: http://github.com/celery/vine/
:Keywords: promise, async, future

About
=====


.. |build-status| image:: https://secure.travis-ci.org/celery/vine.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/vine

.. |coverage| image:: https://codecov.io/github/celery/vine/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/vine?branch=master

.. |license| image:: https://img.shields.io/pypi/l/vine.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/vine.svg
    :alt: Vine can be installed via wheel
    :target: https://pypi.org/project/vine/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/vine.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/vine/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/vine.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/vine/




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n vine-%{unmangled_version} -n vine-%{unmangled_version}
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
