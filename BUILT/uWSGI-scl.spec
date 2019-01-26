%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name uwsgi
%define version 2.0.17
%define unmangled_version 2.0.17
%define unmangled_version 2.0.17
%define release 1

Summary: The uWSGI server
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: uwsgi-%{unmangled_version}.tar.gz
License: GPL2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
#BuildArch: noarch
Vendor: Unbit <info@unbit.it>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://uwsgi-docs.readthedocs.io/en/latest/


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n uwsgi-%{unmangled_version} -n uwsgi-%{unmangled_version}
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
rm -rf $RPM_BUILD_ROOT/usr/lib/debug/* $RPM_BUILD_ROOT/usr/lib/debug/.build-id $RPM_BUILD_ROOT/usr/src/debug/*

%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
/opt/rh/rh-python36/root/usr/bin/uwsgi
