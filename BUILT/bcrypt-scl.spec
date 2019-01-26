%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name bcrypt
%define version 3.1.4
%define unmangled_version 3.1.4
%define unmangled_version 3.1.4
%define release 1

Summary: Modern password hashing for your software and your servers
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}bcrypt
Version: %{version}
Release: %{release}
Source0: bcrypt-%{unmangled_version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/bcrypt-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: The Python Cryptographic Authority developers <cryptography-dev@python.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/pyca/bcrypt/


%description
bcrypt
======

.. image:: https://img.shields.io/pypi/v/bcrypt.svg
    :target: https://pypi.python.org/pypi/bcrypt/
    :alt: Latest Version

.. image:: https://travis-ci.org/pyca/bcrypt.svg?branch=master
    :target: https://travis-ci.org/pyca/bcrypt

Modern password hashing for your software and your servers


Installation
============

To install bcrypt, simply:

.. code:: bash

    $ pip install bcrypt

Note that bcrypt should build very easily on Linux provided you have a C compiler, headers for Python (if you're not using pypy), and headers for the libffi libraries available on your system.

For Debian and Ubuntu, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo apt-get install build-essential libffi-dev python-dev

For Fedora and RHEL-derivatives, the following command will ensure that the required dependencies are installed:

.. code:: bash

    $ sudo yum install gcc libffi-devel python-devel

Changelog
=========

3.1.4
-----

* Fixed compilation with mingw and on illumos.

3.1.3
-----
* Fixed a compilation issue on Solaris.
* Added a warning when using too few rounds with ``kdf``.

3.1.2
-----
* Fixed a compile issue affecting big endian platforms.
* Fixed invalid escape sequence warnings on Python 3.6.
* Fixed building in non-UTF8 environments on Python 2.

3.1.1
-----
* Resolved a ``UserWarning`` when used with ``cffi`` 1.8.3.

3.1.0
-----
* Added support for ``checkpw``, a convenience method for verifying a password.
* Ensure that you get a ``$2y$`` hash when you input a ``$2y$`` salt.
* Fixed a regression where ``$2a`` hashes were vulnerable to a wraparound bug.
* Fixed compilation under Alpine Linux.

3.0.0
-----
* Switched the C backend to code obtained from the OpenBSD project rather than
  openwall.
* Added support for ``bcrypt_pbkdf`` via the ``kdf`` function.

2.0.0
-----
* Added support for an adjustible prefix when calling ``gensalt``.
* Switched to CFFI 1.0+

Usage
-----

Password Hashing
~~~~~~~~~~~~~~~~

Hashing and then later checking that a password matches the previous hashed
password is very simple:

.. code:: pycon

    >>> import bcrypt
    >>> password = b"super secret password"
    >>> # Hash a password for the first time, with a randomly-generated salt
    >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    >>> # Check that an unhashed password matches one that has previously been
    >>> # hashed
    >>> if bcrypt.checkpw(password, hashed):
    ...     print("It Matches!")
    ... else:
    ...     print("It Does not Match :(")

KDF
~~~

As of 3.0.0 ``bcrypt`` now offers a ``kdf`` function which does ``bcrypt_pbkdf``.
This KDF is used in OpenSSH's newer encrypted private key format.

.. code:: pycon

    >>> import bcrypt
    >>> key = bcrypt.kdf(
    ...     password=b'password',
    ...     salt=b'salt',
    ...     desired_key_bytes=32,
    ...     rounds=100)


Adjustable Work Factor
~~~~~~~~~~~~~~~~~~~~~~
One of bcrypt's features is an adjustable logarithmic work factor. To adjust
the work factor merely pass the desired number of rounds to
``bcrypt.gensalt(rounds=12)`` which defaults to 12):

.. code:: pycon

    >>> import bcrypt
    >>> password = b"super secret password"
    >>> # Hash a password for the first time, with a certain number of rounds
    >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    >>> # Check that a unhashed password matches one that has previously been
    >>> #   hashed
    >>> if bcrypt.checkpw(password, hashed):
    ...     print("It Matches!")
    ... else:
    ...     print("It Does not Match :(")


Adjustable Prefix
~~~~~~~~~~~~~~~~~

Another one of bcrypt's features is an adjustable prefix to let you define what
libraries you'll remain compatible with. To adjust this, pass either ``2a`` or
``2b`` (the default) to ``bcrypt.gensalt(prefix=b"2b")`` as a bytes object.

As of 3.0.0 the ``$2y$`` prefix is still supported in ``hashpw`` but deprecated.

Maximum Password Length
~~~~~~~~~~~~~~~~~~~~~~~

The bcrypt algorithm only handles passwords up to 72 characters, any characters
beyond that are ignored. To work around this, a common approach is to hash a
password with a cryptographic hash (such as ``sha256``) and then base64
encode it to prevent NULL byte problems before hashing the result with
``bcrypt``:

.. code:: pycon

    >>> password = b"an incredibly long password" * 10
    >>> hashed = bcrypt.hashpw(
    ...     base64.b64encode(hashlib.sha256(password).digest()),
    ...     bcrypt.gensalt()
    ... )

Compatibility
-------------

This library should be compatible with py-bcrypt and it will run on Python
2.6+, 3.3+, and PyPy 2.6+.

C Code
------

This library uses code from OpenBSD.

Security
--------

``bcrypt`` follows the `same security policy as cryptography`_, if you
identify a vulnerability, we ask you to contact us privately.

.. _`same security policy as cryptography`: https://cryptography.io/en/latest/security/



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n bcrypt-%{unmangled_version} -n bcrypt-%{unmangled_version}
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
