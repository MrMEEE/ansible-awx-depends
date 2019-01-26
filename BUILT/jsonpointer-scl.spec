%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jsonpointer
%define version 2.0
%define unmangled_version 2.0
%define unmangled_version 2.0
%define release 1

Summary:  Identify specific nodes in a JSON document (RFC 6901) 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}jsonpointer
Version: %{version}
Release: %{release}
Source0: jsonpointer-%{unmangled_version}.tar.gz
License: Modified BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/jsonpointer-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Stefan Kögl <stefan@skoegl.net>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/stefankoegl/python-json-pointer


%description
python-json-pointer
===================

[![PyPI version](https://img.shields.io/pypi/v/jsonpointer.svg)](https://pypi.python.org/pypi/jsonpointer/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/jsonpointer.svg)](https://pypi.python.org/pypi/jsonpointer/)
[![Build Status](https://travis-ci.org/stefankoegl/python-json-pointer.png?branch=master)](https://travis-ci.org/stefankoegl/python-json-pointer)
[![Coverage Status](https://coveralls.io/repos/stefankoegl/python-json-pointer/badge.png?branch=master)](https://coveralls.io/r/stefankoegl/python-json-pointer?branch=master)


Resolve JSON Pointers in Python
-------------------------------

Library to resolve JSON Pointers according to
[RFC 6901](http://tools.ietf.org/html/rfc6901)

See source code for examples
* Website: https://github.com/stefankoegl/python-json-pointer
* Repository: https://github.com/stefankoegl/python-json-pointer.git
* Documentation: https://python-json-pointer.readthedocs.org/
* PyPI: https://pypi.python.org/pypi/jsonpointer
* Travis CI: https://travis-ci.org/stefankoegl/python-json-pointer
* Coveralls: https://coveralls.io/r/stefankoegl/python-json-pointer



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jsonpointer-%{unmangled_version} -n jsonpointer-%{unmangled_version}
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
