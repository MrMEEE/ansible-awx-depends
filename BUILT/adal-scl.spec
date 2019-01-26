%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name adal
%define version 0.5.0
%define unmangled_version 0.5.0
%define unmangled_version 0.5.0
%define release 1

Summary: The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}adal
Version: %{version}
Release: %{release}
Source0: adal-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/adal-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <nugetaad@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/AzureAD/azure-activedirectory-library-for-python


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n adal-%{unmangled_version} -n adal-%{unmangled_version}
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
