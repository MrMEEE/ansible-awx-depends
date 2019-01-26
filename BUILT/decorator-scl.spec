%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name decorator
%define version 4.2.1
%define unmangled_version 4.2.1
%define unmangled_version 4.2.1
%define release 1

Summary: Better living through Python with decorators
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}decorator
Version: %{version}
Release: %{release}
Source0: decorator-%{unmangled_version}.tar.gz
License: new BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/decorator-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Michele Simionato <michele.simionato@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/micheles/decorator


%description
Decorator module
=================

:Author: Michele Simionato
:E-mail: michele.simionato@gmail.com
:Requires: Python from 2.6 to 3.6
:Download page: http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just perform

 `$ pip install decorator`

which will install just the module on your system.

If you prefer to install the full distribution from source, including
the documentation, clone the `GitHub repo`_ or download the tarball_, unpack it and run

 `$ pip install .`

in the main directory, possibly as superuser.

.. _tarball: http://pypi.python.org/pypi/decorator
.. _GitHub repo: https://github.com/micheles/decorator

Testing
--------

If you have the source code installation you can run the tests with

 `$ python src/tests/test.py -v`

or (if you have setuptools installed)

 `$ python setup.py test`

Notice that you may run into trouble if in your system there
is an older version of the decorator module; in such a case remove the
old version. It is safe even to copy the module `decorator.py` over
an existing one, since we kept backward-compatibility for a long time.

Repository
---------------

The project is hosted on GitHub. You can look at the source here:

 https://github.com/micheles/decorator

Documentation
---------------

The documentation has been moved to http://decorator.readthedocs.io/en/latest/
You can download a PDF version of it from http://media.readthedocs.org/pdf/decorator/latest/decorator.pdf



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n decorator-%{unmangled_version} -n decorator-%{unmangled_version}
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
