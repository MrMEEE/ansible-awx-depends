%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name chardet
%define version 3.0.4
%define unmangled_version 3.0.4
%define unmangled_version 3.0.4
%define release 1

Summary: Universal encoding detector for Python 2 and 3
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}chardet
Version: %{version}
Release: %{release}
Source0: chardet-%{unmangled_version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/chardet-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Daniel Blanchard <dan.blanchard@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/chardet/chardet


%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

.. image:: https://img.shields.io/travis/chardet/chardet/stable.svg
   :alt: Build status
   :target: https://travis-ci.org/chardet/chardet

.. image:: https://img.shields.io/coveralls/chardet/chardet/stable.svg
   :target: https://coveralls.io/r/chardet/chardet

.. image:: https://img.shields.io/pypi/v/chardet.svg
   :target: https://warehouse.python.org/project/chardet/
   :alt: Latest version on PyPI

.. image:: https://img.shields.io/pypi/l/chardet.svg
   :alt: License


Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - ISO-8859-1, windows-1252 (Western European languages)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)

.. note::
   Our ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
   disabled until we can retrain the models.

Requires Python 2.6, 2.7, or 3.3+.

Installation
------------

Install from `PyPI <https://pypi.python.org/pypi/chardet>`_::

    pip install chardet

Documentation
-------------

For users, docs are now available at https://chardet.readthedocs.io/.

Command-line Tool
-----------------

chardet comes with a command-line script which reports on the encodings of one
or more files::

    % chardetect somefile someotherfile
    somefile: windows-1252 with confidence 0.5
    someotherfile: ascii with confidence 1.0

About
-----

This is a continuation of Mark Pilgrim's excellent chardet. Previously, two
versions needed to be maintained: one that supported python 2.x and one that
supported python 3.x.  We've recently merged with `Ian Cordasco <https://github.com/sigmavirus24>`_'s
`charade <https://github.com/sigmavirus24/charade>`_ fork, so now we have one
coherent version that works for Python 2.6+.

:maintainer: Dan Blanchard



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n chardet-%{unmangled_version} -n chardet-%{unmangled_version}
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
