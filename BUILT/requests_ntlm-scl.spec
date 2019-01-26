%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name requests_ntlm
%define version 1.1.0
%define unmangled_version 1.1.0
%define unmangled_version 1.1.0
%define release 1

Summary: This package allows for HTTP NTLM authentication using the requests library.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}requests_ntlm
Version: %{version}
Release: %{release}
Source0: requests_ntlm-%{unmangled_version}.tar.gz
License: ISC
Group: Development/Libraries
BuildRoot: %{_tmppath}/requests_ntlm-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ben Toews <mastahyeti@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/requests/requests-ntlm


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n requests_ntlm-%{unmangled_version} -n requests_ntlm-%{unmangled_version}
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
