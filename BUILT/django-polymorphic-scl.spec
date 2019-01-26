%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name django-polymorphic
%define version 2.0.2
%define unmangled_version 2.0.2
%define unmangled_version 2.0.2
%define release 1

Summary: Seamless polymorphic inheritance for Django models
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: django-polymorphic-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Christopher Glass <tribaal@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/django-polymorphic/django-polymorphic


%description
.. image::  https://travis-ci.org/django-polymorphic/django-polymorphic.svg?branch=master
    :target: http://travis-ci.org/django-polymorphic/django-polymorphic
.. image:: https://img.shields.io/pypi/v/django-polymorphic.svg
    :target: https://pypi.python.org/pypi/django-polymorphic/
.. image:: https://img.shields.io/codecov/c/github/django-polymorphic/django-polymorphic/master.svg
    :target: https://codecov.io/github/django-polymorphic/django-polymorphic?branch=master

Polymorphic Models for Django
=============================

Django-polymorphic simplifies using inherited models in Django projects.
When a query is made at the base model, the inherited model classes are returned.

When we store models that inherit from a ``Project`` model...

.. code-block:: python

    >>> Project.objects.create(topic="Department Party")
    >>> ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
    >>> ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")

...and want to retrieve all our projects, the subclassed models are returned!

.. code-block:: python

    >>> Project.objects.all()
    [ <Project:         id 1, topic "Department Party">,
      <ArtProject:      id 2, topic "Painting with Tim", artist "T. Turner">,
      <ResearchProject: id 3, topic "Swallow Aerodynamics", supervisor "Dr. Winter"> ]

Using vanilla Django, we get the base class objects, which is rarely what we wanted:

.. code-block:: python

    >>> Project.objects.all()
    [ <Project: id 1, topic "Department Party">,
      <Project: id 2, topic "Painting with Tim">,
      <Project: id 3, topic "Swallow Aerodynamics"> ]

This also works when the polymorphic model is accessed via
ForeignKeys, ManyToManyFields or OneToOneFields.

Features
--------

* Full admin integration.
* ORM integration:

  * support for ForeignKey, ManyToManyField, OneToOneField descriptors.
  * Filtering/ordering of inherited models (``ArtProject___artist``).
  * Filtering model types: ``instance_of(...)`` and ``not_instance_of(...)``
  * Combining querysets of different models (``qs3 = qs1 | qs2``)
  * Support for custom user-defined managers.
* Uses the minumum amount of queries needed to fetch the inherited models.
* Disabling polymorphic behavior when needed.

While *django-polymorphic* makes subclassed models easy to use in Django,
we still encourage to use them with caution. Each subclassed model will require
Django to perform an ``INNER JOIN`` to fetch the model fields from the database.
While taking this in mind, there are valid reasons for using subclassed models.
That's what this library is designed for!

The current release of *django-polymorphic* supports Django 1.11, 2.0 and Python 2.7 and 3.4+ is supported.
For older Django versions, install *django-polymorphic==1.3*.

For more information, see the `documentation at Read the Docs <https://django-polymorphic.readthedocs.io/>`_.

Installation
------------

Install using ``pip``\ ...

.. code:: bash

    $ pip install django-polymorphic

License
=======

Django-polymorphic uses the same license as Django (BSD-like).



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n django-polymorphic-%{unmangled_version} -n django-polymorphic-%{unmangled_version}
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
