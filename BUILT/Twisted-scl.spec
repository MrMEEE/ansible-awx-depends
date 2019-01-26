%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name Twisted
%define version 17.9.0
%define unmangled_version 17.9.0
%define unmangled_version 17.9.0
%define release 1

Summary: An asynchronous networking framework written in Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: Twisted-%{unmangled_version}.tar.bz2
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Glyph Lefkowitz <glyph@twistedmatrix.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://twistedmatrix.com/
BuildRequires: %{?scl_prefix}incremental

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n Twisted-%{unmangled_version} -n Twisted-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build
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
