%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name paramiko
%define version 2.4.0
%define unmangled_version 2.4.0
%define unmangled_version 2.4.0
%define release 1

Summary: SSH2 protocol library
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}paramiko
Version: %{version}
Release: %{release}
Source0: paramiko-%{unmangled_version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/paramiko-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jeff Forcier <jeff@bitprophet.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/paramiko/paramiko/


%description

This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

Required packages:
    Cryptography

To install the development version, ``pip install -e
git+https://github.com/paramiko/paramiko/#egg=paramiko``.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n paramiko-%{unmangled_version} -n paramiko-%{unmangled_version}
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
