%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name jaraco.stream
%define version 1.1.2
%define unmangled_version 1.1.2
%define unmangled_version 1.1.2
%define release 1

Summary: routines for dealing with data streams
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: jaraco.stream-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jason R. Coombs <jaraco@jaraco.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/jaraco/jaraco.stream


%description
.. image:: https://img.shields.io/pypi/v/jaraco.stream.svg
   :target: https://pypi.org/project/jaraco.stream

.. image:: https://img.shields.io/pypi/pyversions/jaraco.stream.svg

.. image:: https://img.shields.io/pypi/dm/jaraco.stream.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.stream/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.stream

Routines for handling streaming data, including a
set of generators for loading gzip data on the fly.

License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n jaraco.stream-%{unmangled_version} -n jaraco.stream-%{unmangled_version}
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
