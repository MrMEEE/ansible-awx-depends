%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name typing
%define version 3.6.4
%define unmangled_version 3.6.4
%define unmangled_version 3.6.4
%define release 1

Summary: Type Hints for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: typing-%{unmangled_version}.tar.gz
License: PSF
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Ivan Levkivskyi <jukka.lehtosalo@iki.fi>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://docs.python.org/3/library/typing.html


%description
Typing -- Type Hints for Python

This is a backport of the standard library typing module to Python
versions older than 3.5.  (See note below for newer versions.)

Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a
concise, standard format, and it has been designed to also be used by
static and runtime type checkers, static analyzers, IDEs and other
tools.

NOTE: in Python 3.5 and later, the typing module lives in the stdlib,
and installing this package has NO EFFECT.  To get a newer version of
the typing module in Python 3.5 or later, you have to upgrade to a
newer Python (bugfix) version.  For example, typing in Python 3.6.0 is
missing the definition of 'Type' -- upgrading to 3.6.2 will fix this.

Also note that most improvements to the typing module in Python 3.7
will not be included in this package, since Python 3.7 has some
built-in support that is not present in older versions (See PEP 560.)



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n typing-%{unmangled_version} -n typing-%{unmangled_version}
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
