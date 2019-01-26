%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-nspkg
%define version 2.0.0
%define unmangled_version 2.0.0
%define unmangled_version 2.0.0
%define release 1

Summary: Microsoft Azure Namespace Package [Internal]
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-nspkg
Version: %{version}
Release: %{release}
Source0: azure-nspkg-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-nspkg-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure namespace.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-nspkg-%{unmangled_version} -n azure-nspkg-%{unmangled_version}
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
