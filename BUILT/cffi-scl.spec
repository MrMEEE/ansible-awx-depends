%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name cffi
%define version 1.11.5
%define unmangled_version 1.11.5
%define unmangled_version 1.11.5
%define release 1

Summary: Foreign Function Interface for Python calling C code.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: cffi-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Armin Rigo, Maciej Fijalkowski <python-cffi@googlegroups.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://cffi.readthedocs.org


%description

CFFI
====

Foreign Function Interface for Python calling C code.
Please see the `Documentation <http://cffi.readthedocs.org/>`_.

Contact
-------

`Mailing list <https://groups.google.com/forum/#!forum/python-cffi>`_



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n cffi-%{unmangled_version} -n cffi-%{unmangled_version}
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
