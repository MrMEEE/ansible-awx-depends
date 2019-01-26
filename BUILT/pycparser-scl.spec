%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pycparser
%define version 2.19
%define unmangled_version 2.19
%define unmangled_version 2.19
%define release 1

Summary: C parser in Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}pycparser
Version: %{version}
Release: %{release}
Source0: pycparser-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/pycparser-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Eli Bendersky <eliben@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/eliben/pycparser


%description

        pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.
    


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pycparser-%{unmangled_version} -n pycparser-%{unmangled_version}
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
