%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pyasn1
%define version 0.4.2
%define unmangled_version 0.4.2
%define unmangled_version 0.4.2
%define release 1

Summary: ASN.1 types and codecs
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: pyasn1-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ilya Etingof <etingof@gmail.com> <etingof@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/etingof/pyasn1


%description
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pyasn1-%{unmangled_version} -n pyasn1-%{unmangled_version}
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
