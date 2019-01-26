%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-mgmt-compute
%define version 2.1.0
%define unmangled_version 2.1.0
%define unmangled_version 2.1.0
%define release 1

Summary: Microsoft Azure Compute Resource Management Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-compute
Version: %{version}
Release: %{release}
Source0: azure-mgmt-compute-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-compute-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Compute Resource Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

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

For code examples, see `Compute and Network Resource Management 
<https://azure-sdk-for-python.readthedocs.org/en/latest/resourcemanagementcomputenetwork.html>`__
on readthedocs.org.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

2.1.0 (2017-07-19)
++++++++++++++++++

**Features in 2017-03-30**

- Expose 'enableAcceleratedNetworking' for virtual machine and virtual machine SS. Windows GA, Linux in preview.
- Expose 'forceUpdateTag' to ensure extension gets reinstalled even there are no configuration change.

2.0.0 (2017-06-29)
++++++++++++++++++

**Features**

Compute default Api Version is now 2017-03-30.

New operation groups:

- resources_skus
- virtual_machine_scale_set_extensions
- virtual_machine_run_commands

New methods in VM:

- perform_maintenance
- run_command

Several improvements and modifications in Managed Disks.

**Breaking changes**

- ContainerService: fixed typo in class name (ContainerServiceOchestratorTypes is now ContainerServiceOrchestratorTypes)

- Compute: breaking changes in Managed Disk API:

  - Managed field removed from Create AV Set API
  - Account Type replaced with SKU in PUT and GET Managed Disk Create API
  - OwnerId replaced by ManagedBy in GET Managed Disk API

Note that you can get the behavior of v1.0.0 by forcing the Api Version to "2016-04-30-preview" to update your package but not the code:

    ComputeManagementClient(credentials, subscription_id, api_version="2016-04-30-preview")

1.0.0 (2017-05-15)
++++++++++++++++++

- Tag 1.0.0rc2 as stable (same content)

1.0.0rc2 (2017-05-12)
+++++++++++++++++++++

**Features**

- Add Compute ApiVersion 2016-03-30 (AzureStack default)

1.0.0rc1 (2017-04-11)
+++++++++++++++++++++

**Breaking Changes**

- Container service is now in it's own client ContainerServiceClient

**Features**

To help customers with sovereign clouds (not general Azure),
this version has official multi ApiVersion support for the following resource type:

- Compute: 2015-06-15 and 2016-04-30-preview

The following resource types support one ApiVersion:

- ContainerService: 2017-01-31

0.33.0 (2017-02-03)
+++++++++++++++++++

**Features**

This release adds Managed Disk to compute. This changes the default disk creation behavior
to use the new Managed Disk feature instead of Storage.

0.32.1 (2016-11-14)
+++++++++++++++++++

* Add "Kubernetes" on Containers
* Improve technical documentation

0.32.0 (2016-11-02)
+++++++++++++++++++

**Breaking change**

New APIVersion for "container" 2016-09-30.

* several parameters (e.g. "username") now dynamically check before REST calls validity 
  against a regexp. Exception will be TypeError and not CloudError anymore.

0.31.0 (2016-11-01)
+++++++++++++++++++

**Breaking change**

We renamed some "container" methods to follow Azure SDK conventions

* "container" attribute on the client is now "containers"
* "list" changed behavior, now listing containers in subscription and lost its parameter
* "list_by_resource_group" new method with the old "list" behavior

0.30.0 (2016-10-17)
+++++++++++++++++++

* Initial preview release. Based on API version 2016-03-30.


0.20.0 (2015-08-31)
+++++++++++++++++++

* Initial preview release. Based on API version 2015-05-01-preview.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-compute-%{unmangled_version} -n azure-mgmt-compute-%{unmangled_version}
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
