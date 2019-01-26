%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name six
%define version 1.12.0
%define unmangled_version 1.12.0
%define unmangled_version 1.12.0
%define release 1

Summary: Python 2 and 3 compatibility utilities
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}six
Version: %{version}
Release: %{release}
Source0: six-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/six-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Benjamin Peterson <benjamin@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/benjaminp/six


%description
.. image:: https://img.shields.io/pypi/v/six.svg
   :target: https://pypi.org/project/six/
   :alt: six on PyPI

.. image:: https://travis-ci.org/benjaminp/six.svg?branch=master
   :target: https://travis-ci.org/benjaminp/six
   :alt: six on TravisCI

.. image:: https://readthedocs.org/projects/six/badge/?version=latest
   :target: https://six.readthedocs.io/
   :alt: six's documentation on Read the Docs

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/benjaminp/six/blob/master/LICENSE
   :alt: MIT License badge

Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports every Python version since 2.6.  It is contained in only one Python
file, so it can be easily copied into your project. (The copyright and license
notice must be retained.)

Online documentation is at https://six.readthedocs.io/.

Bugs can be reported to https://github.com/benjaminp/six.  The code can also
be found there.

For questions about six or porting in general, email the python-porting mailing
list: https://mail.python.org/mailman/listinfo/python-porting



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n six-%{unmangled_version} -n six-%{unmangled_version}
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
