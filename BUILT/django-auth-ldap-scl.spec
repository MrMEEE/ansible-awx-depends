%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name django-auth-ldap
%define version 1.7.0
%define unmangled_version 1.7.0
%define unmangled_version 1.7.0
%define release 1

Summary: Django LDAP authentication backend
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: django-auth-ldap-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jon Dufresne <jon.dufresne@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/django-auth-ldap/django-auth-ldap


%description
================================
Django Authentication Using LDAP
================================

.. image:: https://readthedocs.org/projects/django-auth-ldap/badge/?version=latest
   :target: https://django-auth-ldap.pypa.io/en/latest

.. image:: https://img.shields.io/pypi/v/django-auth-ldap.svg
   :target: https://pypi.org/project/django-auth-ldap/

.. image:: https://img.shields.io/travis/django-auth-ldap/django-auth-ldap/master.svg?label=travis-ci
   :target: http://travis-ci.org/pypa/django-auth-ldap

.. image:: https://img.shields.io/pypi/l/django-auth-ldap.svg
   :target: https://raw.githubusercontent.com/django-auth-ldap/django-auth-ldap/master/LICENSE

This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

* Documentation: https://django-auth-ldap.readthedocs.io/
* PyPI: https://pypi.org/project/django-auth-ldap/
* Repository: https://github.com/django-auth-ldap/django-auth-ldap
* Tests: http://travis-ci.org/pypa/django-auth-ldap
* License: BSD 2-Clause

This version is supported on Python 2.7 and 3.4+; and Django 1.11+. It requires
`python-ldap`_ >= 3.0.

.. _`python-ldap`: https://pypi.org/project/python-ldap/


Installation
============

Install the package with pip:

.. code-block:: sh

    $ pip install django-auth-ldap

It requires `python-ldap`_ >= 3.0. You'll need the `OpenLDAP`_ libraries and
headers available on your system.

To use the auth backend in a Django project, add
``'django_auth_ldap.backend.LDAPBackend'`` to ``AUTHENTICATION_BACKENDS``. Do
not add anything to ``INSTALLED_APPS``.

.. code-block:: python

    AUTHENTICATION_BACKENDS = [
        'django_auth_ldap.backend.LDAPBackend',
    ]

``LDAPBackend`` should work with custom user models, but it does assume that a
database is present.

.. note::

    ``LDAPBackend`` does not inherit from ``ModelBackend``. It is possible to
    use ``LDAPBackend`` exclusively by configuring it to draw group membership
    from the LDAP server. However, if you would like to assign permissions to
    individual users or add users to groups within Django, you'll need to have
    both backends installed:

    .. code-block:: python

        AUTHENTICATION_BACKENDS = [
            'django_auth_ldap.backend.LDAPBackend',
            'django.contrib.auth.backends.ModelBackend',
        ]

.. _`python-ldap`: https://pypi.org/project/python-ldap/
.. _`OpenLDAP`: https://www.openldap.org/


Example Configuration
=====================

Here is a complete example configuration from ``settings.py`` that exercises
nearly all of the features. In this example, we're authenticating against a
global pool of users in the directory, but we have a special area set aside for
Django groups (``ou=django,ou=groups,dc=example,dc=com``). Remember that most
of this is optional if you just need simple authentication. Some default
settings and arguments are included for completeness.

.. code-block:: python

    import ldap
    from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


    # Baseline configuration.
    AUTH_LDAP_SERVER_URI = 'ldap://ldap.example.com'

    AUTH_LDAP_BIND_DN = 'cn=django-agent,dc=example,dc=com'
    AUTH_LDAP_BIND_PASSWORD = 'phlebotinum'
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        'ou=users,dc=example,dc=com',
        ldap.SCOPE_SUBTREE,
        '(uid=%(user)s)',
    )
    # Or:
    # AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'

    # Set up the basic group parameters.
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        'ou=django,ou=groups,dc=example,dc=com',
        ldap.SCOPE_SUBTREE,
        '(objectClass=groupOfNames)',
    )
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='cn')

    # Simple group restrictions
    AUTH_LDAP_REQUIRE_GROUP = 'cn=enabled,ou=django,ou=groups,dc=example,dc=com'
    AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=django,ou=groups,dc=example,dc=com'

    # Populate the Django user from the LDAP directory.
    AUTH_LDAP_USER_ATTR_MAP = {
        'first_name': 'givenName',
        'last_name': 'sn',
        'email': 'mail',
    }

    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        'is_active': 'cn=active,ou=django,ou=groups,dc=example,dc=com',
        'is_staff': 'cn=staff,ou=django,ou=groups,dc=example,dc=com',
        'is_superuser': 'cn=superuser,ou=django,ou=groups,dc=example,dc=com',
    }

    # This is the default, but I like to be explicit.
    AUTH_LDAP_ALWAYS_UPDATE_USER = True

    # Use LDAP group membership to calculate group permissions.
    AUTH_LDAP_FIND_GROUP_PERMS = True

    # Cache distinguised names and group memberships for an hour to minimize
    # LDAP traffic.
    AUTH_LDAP_CACHE_TIMEOUT = 3600

    # Keep ModelBackend around for per-user permissions and maybe a local
    # superuser.
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )


Contributing
============

If you'd like to contribute, the best approach is to send a well-formed pull
request, complete with tests and documentation. Pull requests should be
focused: trying to do more than one thing in a single request will make it more
difficult to process.

If you have a bug or feature request you can try `logging an issue`_.

There's no harm in creating an issue and then submitting a pull request to
resolve it. This can be a good way to start a conversation and can serve as an
anchor point.

.. _`logging an issue`: https://github.com/django-auth-ldap/django-auth-ldap/issues



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-auth-ldap-%{unmangled_version} -n django-auth-ldap-%{unmangled_version}
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
