%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name django-crum
%define version 0.7.2
%define unmangled_version 0.7.2
%define unmangled_version 0.7.2
%define release 1

Summary: Django middleware to capture current request and user.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: django-crum-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Nine More Minutes, Inc. <support@ninemoreminutes.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/ninemoreminutes/django-crum/
BuildRequires: %{?scl_prefix}pytest-runner

%description
|Build Status| |PyPI Version| |PyPI License| |Python Versions|

Django-CRUM
===========

Django-CRUM (Current Request User Middleware) captures the current request and
user in thread local storage.

It enables apps to check permissions, capture audit trails or otherwise access
the current request and user without requiring the request object to be passed
directly. It also offers a context manager to allow for temporarily
impersonating another user.

It provides a signal to extend the built-in function for getting the current
user, which could be helpful when using custom authentication methods or user
models.

It is tested against:
 * Django 1.8 (Python 2.7, 3.3, 3.4 and 3.5)
 * Django 1.9 (Python 2.7, 3.4 and 3.5)
 * Django 1.10 (Python 2.7, 3.4 and 3.5)
 * Django 1.11 (Python 2.7, 3.4, 3.5 and 3.6)
 * Django master/2.0 (Python 3.5 and 3.6)

.. |Build Status| image:: http://img.shields.io/travis/ninemoreminutes/django-crum.svg
   :target: https://travis-ci.org/ninemoreminutes/django-crum
.. |PyPI Version| image:: https://img.shields.io/pypi/v/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |PyPI License| image:: https://img.shields.io/pypi/l/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/django-crum.svg
   :target: https://pypi.python.org/pypi/django-crum/



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-crum-%{unmangled_version} -n django-crum-%{unmangled_version}
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
