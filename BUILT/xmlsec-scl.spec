%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name xmlsec
%define version 1.3.3
%define unmangled_version 1.3.3
%define unmangled_version 1.3.3
%define release 1

Summary: Python bindings for the XML Security Library
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: xmlsec-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Bulat Gaifullin <gaifullinbf@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Requires: xmlsec1 xmlsec1-openssl
Url: https://github.com/mehcode/python-xmlsec
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires: %{?scl_prefix}pkgconfig %{?scl_prefix}lxml xmlsec1-devel libxml2-devel xmlsec1-openssl-devel


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n xmlsec-%{unmangled_version} -n xmlsec-%{unmangled_version}
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
