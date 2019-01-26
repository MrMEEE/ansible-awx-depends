%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name monotonic
%define version 1.4
%define unmangled_version 1.4
%define unmangled_version 1.4
%define release 1

Summary: An implementation of time.monotonic() for Python 2 & < 3.3
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}monotonic
Version: %{version}
Release: %{release}
Source0: monotonic-%{unmangled_version}.tar.gz
License: Apache
Group: Development/Libraries
BuildRoot: %{_tmppath}/monotonic-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ori Livneh <ori@wikimedia.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/atdt/monotonic


%description

monotonic
~~~~~~~~~

This module provides a ``monotonic()`` function which returns the
value (in fractional seconds) of a clock which never goes backwards.

On Python 3.3 or newer, ``monotonic`` will be an alias of
``time.monotonic`` from the standard library. On older versions,
it will fall back to an equivalent implementation:

+------------------+----------------------------------------+
| Linux, BSD, AIX  | ``clock_gettime(3)``                   |
+------------------+----------------------------------------+
| Windows          | ``GetTickCount`` or ``GetTickCount64`` |
+------------------+----------------------------------------+
| OS X             | ``mach_absolute_time``                 |
+------------------+----------------------------------------+

If no suitable implementation exists for the current platform,
attempting to import this module (or to import from it) will
cause a ``RuntimeError`` exception to be raised.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n monotonic-%{unmangled_version} -n monotonic-%{unmangled_version}
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
