%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name ansiconv
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: Converts ANSI coded text and converts it to either plain text or to HTML.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}ansiconv
Version: %{version}
Release: %{release}
Source0: ansiconv-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/ansiconv-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Dan Horrigan <dan@dhorrigan.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://bitbucket.org/dhrrgn/ansiconv


%description
See documentation at http://pythonhosted.org/ansiconv/


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n ansiconv
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
