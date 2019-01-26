%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jsonpickle
%define version 0.9.6
%define unmangled_version 0.9.6
%define unmangled_version 0.9.6
%define release 1

Summary: Python library for serializing any arbitrary object graph into JSON
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jsonpickle-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: David Aguilar <davvid@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://jsonpickle.github.io/


%description
jsonpickle converts complex Python objects to and from JSON.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jsonpickle-%{unmangled_version} -n jsonpickle-%{unmangled_version}
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
