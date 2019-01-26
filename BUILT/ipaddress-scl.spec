%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name ipaddress
%define version 1.0.19
%define unmangled_version 1.0.19
%define unmangled_version 1.0.19
%define release 1

Summary: IPv4/IPv6 manipulation library
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: ipaddress-%{unmangled_version}.tar.gz
License: Python Software Foundation License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Philipp Hagemeister <phihag@phihag.de>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/phihag/ipaddress


%description
Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n ipaddress-%{unmangled_version} -n ipaddress-%{unmangled_version}
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
