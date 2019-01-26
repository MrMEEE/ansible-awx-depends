%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jsonpatch
%define version 1.21
%define unmangled_version 1.21
%define unmangled_version 1.21
%define release 1

Summary:  Apply JSON-Patches (RFC 6902) 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}jsonpatch
Version: %{version}
Release: %{release}
Source0: jsonpatch-%{unmangled_version}.tar.gz
License: Modified BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/jsonpatch-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Stefan Kögl <stefan@skoegl.net>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/stefankoegl/python-json-patch


%description
python-json-patch [![Build Status](https://secure.travis-ci.org/stefankoegl/python-json-patch.png?branch=master)](https://travis-ci.org/stefankoegl/python-json-patch) [![Coverage Status](https://coveralls.io/repos/stefankoegl/python-json-patch/badge.png?branch=master)](https://coveralls.io/r/stefankoegl/python-json-patch?branch=master)
=================
Applying JSON Patches in Python
-------------------------------

Library to apply JSON Patches according to
[RFC 6902](http://tools.ietf.org/html/rfc6902)

See Sourcecode for Examples

* Website: https://github.com/stefankoegl/python-json-patch
* Repository: https://github.com/stefankoegl/python-json-patch.git
* Documentation: https://python-json-patch.readthedocs.org/
* PyPI: https://pypi.python.org/pypi/jsonpatch
* Travis-CI: https://travis-ci.org/stefankoegl/python-json-patch
* Coveralls: https://coveralls.io/r/stefankoegl/python-json-patch

Running external tests
----------------------
To run external tests (such as those from https://github.com/json-patch/json-patch-tests) use ext_test.py

    ./ext_tests.py ../json-patch-tests/tests.json



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jsonpatch-%{unmangled_version} -n jsonpatch-%{unmangled_version}
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
