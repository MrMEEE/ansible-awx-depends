%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jsonbfield
%define version 0.1.0
%define unmangled_version 0.1.0
%define unmangled_version 0.1.0
%define release 1

Summary: Django JSONB field
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}jsonbfield
Version: %{version}
Release: %{release}
Source0: jsonbfield-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/jsonbfield-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Tome Cvitan <tome@cvitan.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/HearstCorp/django-jsonbfield


%description
The Postgres 9.4 JSONB field support coming in Django 1.9 extracted to a standalone module


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-jsonbfield
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
