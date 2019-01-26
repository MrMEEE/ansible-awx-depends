%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name django-taggit
%define version 0.22.2
%define unmangled_version 0.22.2
%define unmangled_version 0.22.2
%define release 1

Summary: django-taggit is a reusable Django application for simple tagging.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: django-taggit-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alex Gaynor <alex.gaynor@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/alex/django-taggit/tree/master
BuildRequires: %{?scl_prefix}isort

%description
django-taggit
=============
.. image:: https://travis-ci.org/alex/django-taggit.svg?branch=master
    :target: https://travis-ci.org/alex/django-taggit
.. image:: https://codecov.io/gh/alex/django-taggit/coverage.svg?branch=master
    :target: https://codecov.io/gh/alex/django-taggit?branch=master

``django-taggit`` a simpler approach to tagging with Django.  Add ``"taggit"`` to your
``INSTALLED_APPS`` then just add a TaggableManager to your model and go:

.. code:: python

    from django.db import models

    from taggit.managers import TaggableManager

    class Food(models.Model):
        # ... fields here

        tags = TaggableManager()


Then you can use the API like so:

.. code:: python

    >>> apple = Food.objects.create(name="apple")
    >>> apple.tags.add("red", "green", "delicious")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: green>, <Tag: delicious>]
    >>> apple.tags.remove("green")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: delicious>]
    >>> Food.objects.filter(tags__name__in=["red"])
    [<Food: apple>, <Food: cherry>]

Tags will show up for you automatically in forms and the admin.

``django-taggit`` requires Django 1.8 or greater.

For more info check out the `documentation <https://django-taggit.readthedocs.io/en/latest/>`_.  And for questions about usage or
development you can contact the
`mailinglist <http://groups.google.com/group/django-taggit>`_.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-taggit-%{unmangled_version} -n django-taggit-%{unmangled_version}
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
