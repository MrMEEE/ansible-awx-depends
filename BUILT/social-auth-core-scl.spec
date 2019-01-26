%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name social-auth-core
%define version 3.0.0
%define unmangled_version 3.0.0
%define unmangled_version 3.0.0
%define release 1

Summary: Python social authentication made simple.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}social-auth-core
Version: %{version}
Release: %{release}
Source0: social-auth-core-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/social-auth-core-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matias Aguirre <matiasaguirre@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/python-social-auth/social-core


%description
# Python Social Auth - Core

[![Build Status](https://travis-ci.org/python-social-auth/social-core.svg?branch=master)](https://travis-ci.org/python-social-auth/social-core)
[![Donate](https://img.shields.io/badge/Donate-PayPal-orange.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=matiasaguirre%40gmail%2ecom&lc=US&item_name=Python%20Social%20Auth&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest)

Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

## Description

This is the core component of the python-social-auth ecosystem, it
implements the common interface to define new authentication backends
to third parties services, implement integrations with web frameworks
and storage solutions.

## Documentation

Project documentation is available at http://python-social-auth.readthedocs.org/.

## Setup

```shell
$ pip install social-auth-core
```

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) document for details.

## Versioning

This project follows [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

## License

This project follows the BSD license. See the [LICENSE](LICENSE) for details.

## Donations

This project is maintened on my spare time, consider donating to keep
it improving.

[![Donate](https://img.shields.io/badge/Donate-PayPal-orange.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=matiasaguirre%40gmail%2ecom&lc=US&item_name=Python%20Social%20Auth&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHostedGuest)



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n social-auth-core-%{unmangled_version} -n social-auth-core-%{unmangled_version}
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
