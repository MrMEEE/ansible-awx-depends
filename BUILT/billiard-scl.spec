%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name billiard
%define version 3.5.0.4
%define unmangled_version 3.5.0.4
%define unmangled_version 3.5.0.4
%define release 1

Summary: Python multiprocessing fork with improvements and bugfixes
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: billiard-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ask Solem <ask@celeryproject.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/celery/billiard


%description
========
billiard
========
:version: 3.5.0.4

|build-status-lin| |build-status-win| |license| |wheel| |pyversion| |pyimp|

.. |build-status-lin| image:: https://secure.travis-ci.org/celery/billiard.png?branch=master
    :alt: Build status on Linux
    :target: https://travis-ci.org/celery/billiard

.. |build-status-win| image:: https://ci.appveyor.com/api/projects/status/github/celery/billiard?png=true&branch=master
    :alt: Build status on Windows
    :target: https://ci.appveyor.com/project/ask/billiard

.. |license| image:: https://img.shields.io/pypi/l/billiard.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/billiard.svg
    :alt: Billiard can be installed via wheel
    :target: https://pypi.org/project/billiard/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/billiard.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/billiard/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/billiard.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/billiard/

About
-----

`billiard` is a fork of the Python 2.7 `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_
package. The multiprocessing package itself is a renamed and updated version of
R Oudkerk's `pyprocessing <https://pypi.org/project/processing/>`_ package.
This standalone variant draws its fixes/improvements from python-trunk and provides
additional bug fixes and improvements.

- This package would not be possible if not for the contributions of not only
  the current maintainers but all of the contributors to the original pyprocessing
  package listed `here <http://pyprocessing.berlios.de/doc/THANKS.html>`_

- Also it is a fork of the multiprocessing backport package by Christian Heims.

- It includes the no-execv patch contributed by R. Oudkerk.

- And the Pool improvements previously located in `Celery`_.

- Billiard is used in and is a dependency for `Celery`_ and is maintained by the
  Celery team.

.. _`Celery`: http://celeryproject.org

Bug reporting
-------------

Please report bugs related to multiprocessing at the
`Python bug tracker <http://bugs.python.org/>`_. Issues related to billiard
should be reported at http://github.com/celery/billiard/issues.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n billiard-%{unmangled_version} -n billiard-%{unmangled_version}
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
