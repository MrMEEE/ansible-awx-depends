%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name sphinx_rtd_theme
%define version 0.4.2
%define unmangled_version 0.4.2
%define unmangled_version 0.4.2
%define release 1

Summary: Read the Docs theme for Sphinx
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: sphinx_rtd_theme-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Dave Snider, Read the Docs, Inc. & contributors <dev@readthedocs.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/rtfd/sphinx_rtd_theme/
AutoReqProv: 0

%description

**************************
Read the Docs Sphinx Theme
**************************

.. image:: https://img.shields.io/pypi/v/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme
   :alt: Pypi Version 
.. image:: https://travis-ci.org/rtfd/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/rtfd/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

The ``sphinx_rtd_theme`` is a sphinx_ theme designed to look modern and be mobile-friendly.
This theme is primarily focused to be used on readthedocs.org_ but can work with your
own sphinx projects. To read more and see a working demo_ head over to readthedocs.org_.

.. _sphinx: http://www.sphinx-doc.org
.. _readthedocs.org: http://www.readthedocs.org
.. _demo: https://sphinx-rtd-theme.readthedocs.io/en/latest/


Installing
==========

The theme is distributed on PyPI_ and can be installed with pip::

   pip install sphinx_rtd_theme

For more information read the full installing docs
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html>`__.

.. _PyPI: https://pypi.python.org/pypi/sphinx_rtd_theme


Configuration
=============

The ``sphinx_rtd_theme`` is highly customizable on both the page level and on a global level.
To see all the possible configuration options read the configuring docs
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html>`__.


Contributing
============

If you would like to help improve the theme or have more control
over the theme in case of a fork please read our contributing guide
`here <https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html>`__.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n sphinx_rtd_theme-%{unmangled_version} -n sphinx_rtd_theme-%{unmangled_version}
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
