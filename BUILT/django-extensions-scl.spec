%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name django-extensions
%define version 2.0.0
%define unmangled_version 2.0.0
%define unmangled_version 2.0.0
%define release 1

Summary: Extensions for Django
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: django-extensions-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Bas van Oostveen <v.oostveen@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/django-extensions/django-extensions


%description
django-extensions bundles several useful
additions for Django projects. See the project page for more information:
  http://github.com/django-extensions/django-extensions


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-extensions-%{unmangled_version} -n django-extensions-%{unmangled_version}
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
