%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}
%define _unpackaged_files_terminate_build 0

%define name azure-mgmt-containerservice
%define version 3.0.1
%define unmangled_version 3.0.1
%define unmangled_version 3.0.1
%define release 2

Summary: Microsoft Azure Container Service Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-containerservice
Version: %{version}
Release: %{release}
Source0: azure-mgmt-containerservice-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-containerservice-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <azpysdkhelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Container Service Client Library.

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

For code examples, see `Container Service
<https://azure-sdk-for-python.readthedocs.org/en/latest/sample_azure-mgmt-containerservice.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

3.0.1 (2018-01-25)
++++++++++++++++++

**Bugfixes**

* Fix incorrect mapping in OrchestratorVersionProfileListResult

3.0.0 (2017-12-13)
++++++++++++++++++

* Flattened ManagedCluster so there is no separate properties object
* Added get_access_profiles operation to managed clusters

2.0.0 (2017-10-XX)
++++++++++++++++++

**Features**

* Managed clusters

**Breaking changes**

* VM is now require for master profile (recommended default: standard_d2_v2)

1.0.0 (2017-08-08)
++++++++++++++++++

* Initial Release extracted from azure-mgmt-compute 2.1.0



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-containerservice-%{unmangled_version} -n azure-mgmt-containerservice-%{unmangled_version}
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
cat INSTALLED_FILES |grep -v "/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/azure/__pycache__" |grep -v "/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/azure/__init__.py" |grep -v "/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/azure/mgmt/__pycache__" |grep -v "/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/azure/mgmt/__init__.py" > INSTALLED_FILES_WITHOUT_COMMON_PYCACHE

%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES_WITHOUT_COMMON_PYCACHE
%defattr(-,root,root)
