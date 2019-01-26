%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name munch
%define version 2.2.0
%define unmangled_version 2.2.0
%define unmangled_version 2.2.0
%define release 1

Summary: A dot-accessible dictionary (a la JavaScript objects).
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}munch
Version: %{version}
Release: %{release}
Source0: munch-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/munch-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rotem Yaari <vmalloc@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/Infinidat/munch


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n munch-%{unmangled_version} -n munch-%{unmangled_version}
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
