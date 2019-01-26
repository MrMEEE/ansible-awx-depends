%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name requests-credssp
%define version 0.1.0
%define unmangled_version 0.1.0
%define unmangled_version 0.1.0
%define release 1

Summary: HTTPS CredSSP authentication with the requests library.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}requests-credssp
Version: %{version}
Release: %{release}
Source0: requests-credssp-%{unmangled_version}.tar.gz
License: ISC
Group: Development/Libraries
BuildRoot: %{_tmppath}/requests-credssp-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jordan Borean <jborean93@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jborean93/requests-credssp


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n requests-credssp-%{unmangled_version} -n requests-credssp-%{unmangled_version}
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
