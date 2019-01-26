%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pycurl
%define version 7.43.0.1
%define unmangled_version 7.43.0.1
%define release 1

Summary: PycURL -- A Python Interface To The cURL library
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}pycurl
Version: %{version}
Release: %{release}
Source0: pycurl-%{unmangled_version}.tar.gz
License: LGPL/MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/pycurl-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Oleg Pudeyev <oleg@bsdpower.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://pycurl.io/
Requires: libcurl-devel

%description
PycURL -- A Python Interface To The cURL library
================================================

PycURL is a Python interface to `libcurl`_, the multiprotocol file
transfer library. Similarly to the urllib_ Python module,
PycURL can be used to fetch objects identified by a URL from a Python program.
Beyond simple fetches however PycURL exposes most of the functionality of
libcurl, including:

- Speed - libcurl is very fast and PycURL, being a thin wrapper above
  libcurl, is very fast as well. PycURL `was benchmarked`_ to be several
  times faster than requests_.
- Features including multiple protocol support, SSL, authentication and
  proxy options. PycURL supports most of libcurl's callbacks.
- Multi_ and share_ interfaces.
- Sockets used for network operations, permitting integration of PycURL
  into the application's I/O loop (e.g., using Tornado_).

.. _was benchmarked: http://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance
.. _requests: http://python-requests.org/
.. _Multi: https://curl.haxx.se/libcurl/c/libcurl-multi.html
.. _share: https://curl.haxx.se/libcurl/c/libcurl-share.html
.. _Tornado: http://www.tornadoweb.org/


Requirements
------------

- Python 2.6, 2.7 or 3.1 through 3.6.
- libcurl 7.19.0 or better.


Installation
------------

Download source and binary distributions from `PyPI`_ or `Bintray`_.
Binary wheels are now available for 32 and 64 bit Windows versions.

Please see `the installation documentation`_ for installation instructions.

.. _PyPI: https://pypi.python.org/pypi/pycurl
.. _Bintray: https://dl.bintray.com/pycurl/pycurl/
.. _the installation documentation: http://pycurl.io/docs/latest/install.html


Documentation
-------------

Documentation for the most recent PycURL release is available on
`PycURL website <http://pycurl.io/docs/latest/>`_.


Support
-------

For support questions please use `curl-and-python mailing list`_.
`Mailing list archives`_ are available for your perusal as well.

Although not an official support venue, `Stack Overflow`_ has been
popular with some PycURL users.

Bugs can be reported `via GitHub`_. Please use GitHub only for bug
reports and direct questions to our mailing list instead.

.. _curl-and-python mailing list: http://cool.haxx.se/mailman/listinfo/curl-and-python
.. _Stack Overflow: http://stackoverflow.com/questions/tagged/pycurl
.. _Mailing list archives: https://curl.haxx.se/mail/list.cgi?list=curl-and-python
.. _via GitHub: https://github.com/pycurl/pycurl/issues


License
-------

PycURL is dual licensed under the LGPL and an MIT/X derivative license
based on the libcurl license. The complete text of the licenses is available
in COPYING-LGPL_ and COPYING-MIT_ files in the source distribution.

.. _libcurl: https://curl.haxx.se/libcurl/
.. _urllib: http://docs.python.org/library/urllib.html
.. _COPYING-LGPL: https://raw.githubusercontent.com/pycurl/pycurl/master/COPYING-LGPL
.. _COPYING-MIT: https://raw.githubusercontent.com/pycurl/pycurl/master/COPYING-MIT



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pycurl-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
/opt/rh/rh-python36/root/usr/share/doc/pycurl
