%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name pyOpenSSL
%define version 19.0.0
%define unmangled_version 19.0.0
%define unmangled_version 19.0.0
%define release 1

Summary: Python wrapper module around the OpenSSL library
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: pyOpenSSL-%{unmangled_version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Hynek Schlawack <hs@ox.cx>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://pyopenssl.org/
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires: openssl-devel %{?scl_prefix}python-devel %{?scl_prefix}python-sphinx %{?scl_prefix}sphinx_rtd_theme


%description
========================================================
pyOpenSSL -- A Python wrapper around the OpenSSL library
========================================================

.. image:: https://readthedocs.org/projects/pyopenssl/badge/?version=stable
   :target: https://pyopenssl.org/en/stable/
   :alt: Stable Docs

.. image:: https://travis-ci.org/pyca/pyopenssl.svg?branch=master
   :target: https://travis-ci.org/pyca/pyopenssl
   :alt: Build status

.. image:: https://codecov.io/github/pyca/pyopenssl/branch/master/graph/badge.svg
   :target: https://codecov.io/github/pyca/pyopenssl
   :alt: Test coverage

**Note:** The Python Cryptographic Authority **strongly suggests** the use of `pyca/cryptography`_
where possible. If you are using pyOpenSSL for anything other than making a TLS connection 
**you should move to cryptography and drop your pyOpenSSL dependency**.

High-level wrapper around a subset of the OpenSSL library. Includes

* ``SSL.Connection`` objects, wrapping the methods of Python's portable sockets
* Callbacks written in Python
* Extensive error-handling mechanism, mirroring OpenSSL's error codes

... and much more.

You can find more information in the documentation_.
Development takes place on GitHub_.


Discussion
==========

If you run into bugs, you can file them in our `issue tracker`_.

We maintain a cryptography-dev_ mailing list for both user and development discussions.

You can also join ``#cryptography-dev`` on Freenode to ask questions or get involved.


.. _documentation: https://pyopenssl.org/
.. _`issue tracker`: https://github.com/pyca/pyopenssl/issues
.. _cryptography-dev: https://mail.python.org/mailman/listinfo/cryptography-dev
.. _GitHub: https://github.com/pyca/pyopenssl
.. _`pyca/cryptography`: https://github.com/pyca/cryptography


Release Information
===================

19.0.0 (2019-01-21)
-------------------


Backward-incompatible changes:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``X509Store.add_cert`` no longer raises an error if you add a duplicate cert.
  `#787 <https://github.com/pyca/pyopenssl/pull/787>`_


Deprecations:
^^^^^^^^^^^^^

*none*


Changes:
^^^^^^^^

- pyOpenSSL now works with OpenSSL 1.1.1.
  `#805 <https://github.com/pyca/pyopenssl/pull/805>`_
- pyOpenSSL now handles NUL bytes in ``X509Name.get_components()``
  `#804 <https://github.com/pyca/pyopenssl/pull/804>`_


`Full changelog <https://pyopenssl.org/en/stable/changelog.html>`_.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n pyOpenSSL-%{unmangled_version} -n pyOpenSSL-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
make -C doc text html

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
%doc doc/_build/html
