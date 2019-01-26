%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pykerberos
%define version 1.2.1
%define unmangled_version 1.2.1
%define unmangled_version 1.2.1
%define release 1

Summary: High-level interface to Kerberos
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}pykerberos
Version: %{version}
Release: %{release}
Source0: pykerberos-%{unmangled_version}.tar.gz
License: ASL 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/pykerberos-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: UNKNOWN <UNKNOWN>
Packager: Martin Juhl <m@rtinjuhl.dk>


%description

This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire Kerberos.framework,
and instead offer a limited set of functions that do what is needed for client/server
Kerberos authentication based on <http://www.ietf.org/rfc/rfc4559.txt>.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pykerberos-%{unmangled_version} -n pykerberos-%{unmangled_version}
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
