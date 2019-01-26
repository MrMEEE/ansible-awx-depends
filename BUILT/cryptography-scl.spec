%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name cryptography
%define version 2.1.4
%define unmangled_version 2.1.4
%define unmangled_version 2.1.4
%define release 1

Summary: cryptography is a package which provides cryptographic recipes and primitives to Python developers.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}cryptography
Version: %{version}
Release: %{release}
Source0: cryptography-%{unmangled_version}.tar.gz
License: BSD or Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/cryptography-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: The cryptography developers <cryptography-dev@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/pyca/cryptography


%description
pyca/cryptography
=================

.. image:: https://img.shields.io/pypi/v/cryptography.svg
    :target: https://pypi.python.org/pypi/cryptography/
    :alt: Latest Version

.. image:: https://readthedocs.org/projects/cryptography/badge/?version=latest
    :target: https://cryptography.io
    :alt: Latest Docs

.. image:: https://travis-ci.org/pyca/cryptography.svg?branch=master
    :target: https://travis-ci.org/pyca/cryptography

.. image:: https://codecov.io/github/pyca/cryptography/coverage.svg?branch=master
    :target: https://codecov.io/github/pyca/cryptography?branch=master


``cryptography`` is a package which provides cryptographic recipes and
primitives to Python developers.  Our goal is for it to be your "cryptographic
standard library". It supports Python 2.6-2.7, Python 3.4+, and PyPy 5.3+.

``cryptography`` includes both high level recipes and low level interfaces to
common cryptographic algorithms such as symmetric ciphers, message digests, and
key derivation functions. For example, to encrypt something with
``cryptography``'s high level symmetric encryption recipe:

.. code-block:: pycon

    >>> from cryptography.fernet import Fernet
    >>> # Put this somewhere safe!
    >>> key = Fernet.generate_key()
    >>> f = Fernet(key)
    >>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
    >>> token
    '...'
    >>> f.decrypt(token)
    'A really secret message. Not for prying eyes.'

You can find more information in the `documentation`_.

You can install ``cryptography`` with:

.. code-block:: console

    $ pip install cryptography

For full details see `the installation documentation`_.

Discussion
~~~~~~~~~~

If you run into bugs, you can file them in our `issue tracker`_.

We maintain a `cryptography-dev`_ mailing list for development discussion.

You can also join ``#cryptography-dev`` on Freenode to ask questions or get
involved.


.. _`documentation`: https://cryptography.io/
.. _`the installation documentation`: https://cryptography.io/en/latest/installation/
.. _`issue tracker`: https://github.com/pyca/cryptography/issues
.. _`cryptography-dev`: https://mail.python.org/mailman/listinfo/cryptography-dev



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n cryptography-%{unmangled_version} -n cryptography-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build
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
