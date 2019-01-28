%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pywinrm
%define version 0.3.0
%define unmangled_version 0.3.0
%define unmangled_version 0.3.0
%define release 2

Summary: Python library for Windows Remote Management
Name: %{?scl_prefix}pywinrm
Version: %{version}
Release: %{release}
Source0: pywinrm-%{unmangled_version}.tar.gz
License: MIT license
Group: Development/Libraries
BuildRoot: %{_tmppath}/pywinrm-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alexey Diyan <alexey.diyan@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Requires: %{?scl_prefix}xmltodict
Url: http://github.com/diyan/pywinrm/


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pywinrm-%{unmangled_version} -n pywinrm-%{unmangled_version}
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
