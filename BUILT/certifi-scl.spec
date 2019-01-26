%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name certifi
%define version 2018.1.18
%define unmangled_version 2018.1.18
%define unmangled_version 2018.1.18
%define release 1

Summary: Python package for providing Mozilla's CA Bundle.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}certifi
Version: %{version}
Release: %{release}
Source0: certifi-%{unmangled_version}.tar.gz
License: MPL-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/certifi-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://certifi.io/


%description
Certifi: Python SSL Certificates
================================

`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

Installation
------------

``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip install certifi

Usage
-----

To reference the installed certificate authority (CA) bundle, you can use the
built-in function::

    >>> import certifi

    >>> certifi.where()
    '/usr/local/lib/python2.7/site-packages/certifi/cacert.pem'

Enjoy!

1024-bit Root Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers and certificate authorities have concluded that 1024-bit keys are
unacceptably weak for certificates, particularly root certificates. For this
reason, Mozilla has removed any weak (i.e. 1024-bit key) certificate from its
bundle, replacing it with an equivalent strong (i.e. 2048-bit or greater key)
certificate from the same CA. Because Mozilla removed these certificates from
its bundle, ``certifi`` removed them as well.

In previous versions, ``certifi`` provided the ``certifi.old_where()`` function
to intentionally re-add the 1024-bit roots back into your bundle. This was not
recommended in production and therefore was removed. To assist in migrating old
code, the function ``certifi.old_where()`` continues to exist as an alias of
``certifi.where()``. Please update your code to use ``certifi.where()``
instead. ``certifi.old_where()`` will be removed in 2018.

.. _`Certifi`: http://certifi.io/en/latest/
.. _`Requests`: http://docs.python-requests.org/en/latest/



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n certifi-%{unmangled_version} -n certifi-%{unmangled_version}
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
