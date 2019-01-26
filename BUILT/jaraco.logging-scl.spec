%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.logging
%define version 1.5.1
%define unmangled_version 1.5.1
%define unmangled_version 1.5.1
%define release 1

Summary: jaraco.logging
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.logging-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.logging


%description
.. image:: https://img.shields.io/pypi/v/jaraco.logging.svg
   :target: https://pypi.org/project/jaraco.logging

.. image:: https://img.shields.io/pypi/pyversions/jaraco.logging.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.logging/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.logging

.. image:: https://readthedocs.org/projects/jaracologging/badge/?version=latest
   :target: https://jaracologging.readthedocs.io/en/latest/?badge=latest

Argument Parsing
================

Quickly solicit log level info from command-line parameters::

    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.logging-%{unmangled_version} -n jaraco.logging-%{unmangled_version}
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
