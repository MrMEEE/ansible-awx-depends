%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-mgmt-dns
%define version 1.2.0
%define unmangled_version 1.2.0
%define unmangled_version 1.2.0
%define release 1

Summary: Microsoft Azure DNS Management Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-dns
Version: %{version}
Release: %{release}
Source0: azure-mgmt-dns-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-dns-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <azpysdkhelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure DNS Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

For the older Azure Service Management (ASM) libraries, see
`azure-servicemanagement-legacy <https://pypi.python.org/pypi/azure-servicemanagement-legacy>`__ library.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Usage
=====

For code examples, see `DNS Management
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-mgmt-dns.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

1.2.0 (2017-10-26)
++++++++++++++++++

- add record_type CAA
- remove pointless return type of delete

Api version moves from 2016-04-01 to 2017-09-01

1.1.0 (2017-10-10)
++++++++++++++++++

- Add "recordsetnamesuffix" filter parameter to list operations

1.0.1 (2017-04-20)
++++++++++++++++++

This wheel package is now built with the azure wheel extension

1.0.0 (2016-12-12)
++++++++++++++++++

* Initial release



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-dns-%{unmangled_version} -n azure-mgmt-dns-%{unmangled_version}
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
