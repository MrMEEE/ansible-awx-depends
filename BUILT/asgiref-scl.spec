%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name asgiref
%define version 1.1.2
%define unmangled_version 1.1.2
%define unmangled_version 1.1.2
%define release 1

Summary: Reference ASGI adapters and channel layers
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: asgiref-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Django Software Foundation <foundation@djangoproject.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/django/asgiref/


%description
asgiref
=======

.. image:: https://api.travis-ci.org/django/asgiref.svg
    :target: https://travis-ci.org/django/asgiref

.. image:: https://img.shields.io/pypi/v/asgiref.svg
    :target: https://pypi.python.org/pypi/asgiref

Contains various reference ASGI implementations, including:

* A base channel layer, ``asgiref.base_layer``
* An in-memory channel layer, ``asgiref.inmemory``
* WSGI-to-ASGI and ASGI-to-WSGI adapters, in ``asgiref.wsgi``


Base Channel Layer
------------------

Provides an optional template to start ASGI channel layers from with the two
exceptions you need provided and all API functions stubbed out.

Also comes with logic for doing per-channel capacities using channel names and
globbing; use ``self.get_capacity`` and pass the arguments through to the base
``__init__`` if you want to use it.


In-memory Channel Layer
-----------------------

Simply instantiate ``asgiref.inmemory.ChannelLayer``, or use the pre-made
``asgiref.inmemory.channel_layer`` for easy use. Implements the ``group``
extension, and is designed to support running multiple ASGI programs
in separate threads within one process (the channel layer is threadsafe).


WSGI-ASGI Adapters
------------------

These are not yet complete and should not be used.

Dependencies
------------

All Channels projects currently support Python 2.7, 3.4 and 3.5.

Contributing
------------

Please refer to the
`main Channels contributing docs <https://github.com/django/channels/blob/master/CONTRIBUTING.rst>`_.
That also contains advice on how to set up the development environment and run the tests.

Maintenance and Security
------------------------

To report security issues, please contact security@djangoproject.com. For GPG
signatures and more security process information, see
https://docs.djangoproject.com/en/dev/internals/security/.

To report bugs or request new features, please open a new GitHub issue.

This repository is part of the Channels project. For the shepherd and maintenance team, please see the
`main Channels readme <https://github.com/django/channels/blob/master/README.rst>`_.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n asgiref-%{unmangled_version} -n asgiref-%{unmangled_version}
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
