%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pyparsing
%define version 2.3.1
%define unmangled_version 2.3.1
%define unmangled_version 2.3.1
%define release 1

Summary: Python parsing module
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}pyparsing
Version: %{version}
Release: %{release}
Source0: pyparsing-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/pyparsing-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Paul McGuire <ptmcg@users.sourceforge.net>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/pyparsing/pyparsing/


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pyparsing-%{unmangled_version} -n pyparsing-%{unmangled_version}
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
