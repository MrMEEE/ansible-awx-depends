%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name apache-libcloud
%define version 2.2.1
%define unmangled_version 2.2.1
%define unmangled_version 2.2.1
%define release 1

Summary: A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see http://libcloud.apache.org
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}apache-libcloud
Version: %{version}
Release: %{release}
Source0: apache-libcloud-%{unmangled_version}.tar.gz
License: Apache License (2.0)
Group: Development/Libraries
BuildRoot: %{_tmppath}/apache-libcloud-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Apache Software Foundation <dev@libcloud.apache.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://libcloud.apache.org/


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n apache-libcloud-%{unmangled_version} -n apache-libcloud-%{unmangled_version}
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
