%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-mgmt-keyvault
%define version 0.40.0
%define unmangled_version 0.40.0
%define unmangled_version 0.40.0
%define release 1

Summary: Microsoft Azure KeyVault Apps Resource Management Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-keyvault
Version: %{version}
Release: %{release}
Source0: azure-mgmt-keyvault-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-keyvault-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure KeyVault Resource Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

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

For code examples, see `KeyVault Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-mgmt-keyvault.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.40.0 (2017-06-06)
+++++++++++++++++++

- upgrading to API version 2016-10-01
- adding keyvault management plane updates to enable the soft delete feature for a new or existing keyvault

**Notes**

- this contains a backwards breaking change removing the All value from KeyPermissions, SecretPermissions and CertificatePermissions

0.31.0 (2017-04-19)
+++++++++++++++++++

**Bugfixes**

- Fix possible deserialization error, but updating from list<enumtype> to list<str> when applicable

**Notes**

- This wheel package is now built with the azure wheel extension

0.30.1 (2016-12-15)
+++++++++++++++++++

* Fix list Vault by subscription method return type

0.30.0 (2016-10-04)
+++++++++++++++++++

* Initial preview release (API Version 2016-10-02)



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-keyvault-%{unmangled_version} -n azure-mgmt-keyvault-%{unmangled_version}
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
