%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name hyperlink
%define version 18.0.0
%define unmangled_version 18.0.0
%define unmangled_version 18.0.0
%define release 1

Summary: A featureful, immutable, and correct URL for Python.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: hyperlink-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mahmoud Hashemi and Glyph Lefkowitz <mahmoud@hatnote.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/python-hyper/hyperlink


%description
The humble, but powerful, URL runs everything around us. Chances
are you've used several just to read this text.

Hyperlink is a featureful, pure-Python implementation of the URL, with
an emphasis on correctness. BSD licensed.

See the docs at http://hyperlink.readthedocs.io.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n hyperlink-%{unmangled_version} -n hyperlink-%{unmangled_version}
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
