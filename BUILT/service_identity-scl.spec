%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name service_identity
%define version 17.0.0
%define unmangled_version 17.0.0
%define unmangled_version 17.0.0
%define release 1

Summary: Service identity verification for pyOpenSSL.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: service_identity-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Hynek Schlawack <hs@ox.cx>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://service-identity.readthedocs.io/


%description
=============================
Service Identity Verification
=============================

.. image:: https://readthedocs.org/projects/service-identity/badge/?version=stable
   :target: https://service-identity.readthedocs.io/en/stable/?badge=stable
   :alt: Documentation Status

.. image:: https://travis-ci.org/pyca/service_identity.svg?branch=master
   :target: https://travis-ci.org/pyca/service_identity
   :alt: CI status

.. image:: https://codecov.io/github/pyca/service_identity/branch/master/graph/badge.svg
   :target: https://codecov.io/github/pyca/service_identity
   :alt: Test Coverage

.. image:: https://www.irccloud.com/invite-svg?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1
    :target: https://www.irccloud.com/invite?channel=%23cryptography-dev&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1

.. begin

Use this package if:

- you use pyOpenSSL_ and don’t want to be MITM_\ ed or
- if you want to verify that a `PyCA cryptography`_ certificate is valid for a certain hostname.

``service_identity`` aspires to give you all the tools you need for verifying whether a certificate is valid for the intended purposes.

In the simplest case, this means *host name verification*.
However, ``service_identity`` implements `RFC 6125`_ fully and plans to add other relevant RFCs too.

``service_identity``\ ’s documentation lives at `Read the Docs <https://service-identity.readthedocs.io/>`_, the code on `GitHub <https://github.com/pyca/service_identity>`_.


.. _Twisted: https://twistedmatrix.com/
.. _pyOpenSSL: https://pypi.python.org/pypi/pyOpenSSL/
.. _MITM: https://en.wikipedia.org/wiki/Man-in-the-middle_attack
.. _RFC 6125: http://www.rfc-editor.org/info/rfc6125
.. _PyCA cryptography: https://cryptography.io/


Release Information
===================

17.0.0 (2017-05-23)
-------------------

Deprecations:
^^^^^^^^^^^^^

- Since Chrome 58 and Firefox 48 both don't accept certificates that contain only a Common Name, its usage is hereby deprecated in ``service_identity`` too.
  We have been raising a warning since 16.0.0 and the support will be removed in mid-2018 for good.


Changes:
^^^^^^^^

- When ``service_identity.SubjectAltNameWarning`` is raised, the Common Name of the certificate is now included in the warning message.
  `#17 <https://github.com/pyca/service_identity/pull/17>`_
- Added ``cryptography.x509`` backend for verifying certificates.
  `#18 <https://github.com/pyca/service_identity/pull/18>`_
- Wildcards (``*``) are now only allowed if they are the leftmost label in a certificate.
  This is common practice by all major browsers.
  `#19 <https://github.com/pyca/service_identity/pull/19>`_

`Full changelog <https://service-identity.readthedocs.io/en/stable/changelog.html>`_.

Authors
=======

``service_identity`` is written and maintained by `Hynek Schlawack <https://hynek.me/>`_.

The development is kindly supported by `Variomedia AG <https://www.variomedia.de/>`_.

Other contributors can be found in `GitHub's overview <https://github.com/pyca/service_identity/graphs/contributors>`_.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n service_identity-%{unmangled_version} -n service_identity-%{unmangled_version}
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
