%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name python-dateutil
%define version 2.6.1
%define unmangled_version 2.6.1
%define unmangled_version 2.6.1
%define release 1

Summary: Extensions to the standard Python datetime module
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}python-dateutil
Version: %{version}
Release: %{release}
Source0: python-dateutil-%{unmangled_version}.tar.gz
License: Simplified BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/python-dateutil-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Paul Ganssle <dateutil@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://dateutil.readthedocs.io


%description

The dateutil module provides powerful extensions to the
datetime module available in the Python standard library.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n python-dateutil-%{unmangled_version} -n python-dateutil-%{unmangled_version}
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
