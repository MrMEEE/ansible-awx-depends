%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name python-memcached
%define version 1.59
%define unmangled_version 1.59
%define unmangled_version 1.59
%define release 1

Summary: Pure python memcached client
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: python-memcached-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Sean Reifschneider <jafo@tummy.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Requires: %{?scl_prefix}python-memcached
Url: https://github.com/linsomniac/python-memcached


%description
[![Build
Status](https://travis-ci.org/linsomniac/python-memcached.svg)](https://travis-ci.org/linsomniac/python-memcached)

## Overview

This software is a 100% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values
in one or more, possibly remote, memcached servers.  Search google for
memcached for more information.

This package was originally written by Evan Martin of Danga.  Please do
not contact Evan about maintenance.  Sean Reifschneider of tummy.com,
ltd. has taken over maintenance of it.

Please report issues and submit code changes to the github repository at:

   https://github.com/linsomniac/python-memcached

For changes prior to 2013-03-26, see the old Launchpad repository at:

   Historic issues: https://launchpad.net/python-memcached

## Testing

Test patches locally and easily by running tox:

    pip install tox
    tox -e py27

Test for style by running tox:

    tox -e pep8



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n python-memcached-%{unmangled_version} -n python-memcached-%{unmangled_version}
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
