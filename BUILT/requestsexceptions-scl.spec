%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name requestsexceptions
%define version 1.4.0
%define unmangled_version 1.4.0
%define unmangled_version 1.4.0
%define release 1

Summary: Import exceptions from potentially bundled packages in requests.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}requestsexceptions
Version: %{version}
Release: %{release}
Source0: requestsexceptions-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/requestsexceptions-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://www.openstack.org/


%description
requestsexceptions
==================

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult.  This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n requestsexceptions-%{unmangled_version} -n requestsexceptions-%{unmangled_version}
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
