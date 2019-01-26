%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pexpect
%define version 4.6.0
%define unmangled_version 4.6.0
%define release 1

Summary: Pexpect allows easy control of interactive console applications.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: pexpect-%{unmangled_version}.tar.gz
License: ISC license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Noah Spurrier; Thomas Kluyver; Jeff Quast <noah@noah.org, thomas@kluyver.me.uk, contact@jeffquast.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://pexpect.readthedocs.io/


%description

Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
software package installations on different servers. It can be used for
automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
Pexpect is pure Python.

The main features of Pexpect require the pty module in the Python standard
library, which is only available on Unix-like systems. Some features—waiting
for patterns from file descriptors or subprocesses—are also available on
Windows.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pexpect-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
