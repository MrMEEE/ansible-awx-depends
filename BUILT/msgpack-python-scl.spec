%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name msgpack-python
%define version 0.5.5
%define unmangled_version 0.5.5
%define unmangled_version 0.5.5
%define release 1

Summary: MessagePack (de)serializer.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: msgpack-python-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: INADA Naoki <songofacandy@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://msgpack.org/
BuildRequires: gcc-c++

%description
This package is deprecated.  Install msgpack instead.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n msgpack-python-%{unmangled_version} -n msgpack-python-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build
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
