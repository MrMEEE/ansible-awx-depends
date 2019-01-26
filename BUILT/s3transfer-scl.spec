%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name s3transfer
%define version 0.1.13
%define unmangled_version 0.1.13
%define unmangled_version 0.1.13
%define release 1

Summary: An Amazon S3 Transfer Manager
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}s3transfer
Version: %{version}
Release: %{release}
Source0: s3transfer-%{unmangled_version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/s3transfer-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Amazon Web Services <kyknapp1@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/boto/s3transfer


%description
=====================================================
s3transfer - An Amazon S3 Transfer Manager for Python
=====================================================

S3transfer is a Python library for managing Amazon S3 transfers.

.. note::

  This project is not currently GA. If you are planning to use this code in
  production, make sure to lock to a minor version as interfaces may break
  from minor version to minor version. For a basic, stable interface of
  s3transfer, try the interfaces exposed in `boto3 <https://boto3.readthedocs.io/en/latest/guide/s3.html#using-the-transfer-manager>`__



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n s3transfer-%{unmangled_version} -n s3transfer-%{unmangled_version}
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
