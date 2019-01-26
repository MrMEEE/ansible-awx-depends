%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name Pygments
%define version 2.2.0
%define unmangled_version 2.2.0
%define unmangled_version 2.2.0
%define release 1

Summary: Pygments is a syntax highlighting package written in Python.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}Pygments
Version: %{version}
Release: %{release}
Source0: Pygments-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/Pygments-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Georg Brandl <georg@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://pygments.org/


%description
Pygments
    ~~~~~~~~

    Pygments is a syntax highlighting package written in Python.

    It is a generic syntax highlighter suitable for use in code hosting, forums,
    wikis or other applications that need to prettify source code.  Highlights
    are:

    * a wide range of over 300 languages and other text formats is supported
    * special attention is paid to details, increasing quality by a fair amount
    * support for new languages and formats are added easily
    * a number of output formats, presently HTML, LaTeX, RTF, SVG, all image       formats that PIL supports and ANSI sequences
    * it is usable as a command-line tool and as a library

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n Pygments-%{unmangled_version} -n Pygments-%{unmangled_version}
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
