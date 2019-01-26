%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name ntlm-auth
%define version 1.0.6
%define unmangled_version 1.0.6
%define unmangled_version 1.0.6
%define release 1

Summary: Creates NTLM authentication structures
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}ntlm-auth
Version: %{version}
Release: %{release}
Source0: ntlm-auth-%{unmangled_version}.tar.gz
License: GNU Lesser GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/ntlm-auth-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jordan Borean <jborean93@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jborean93/ntlm-auth


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n ntlm-auth-%{unmangled_version} -n ntlm-auth-%{unmangled_version}
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
