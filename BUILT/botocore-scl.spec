%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name botocore
%define version 1.9.3
%define unmangled_version 1.9.3
%define unmangled_version 1.9.3
%define release 1

Summary: Low-level, data-driven core of boto 3.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}botocore
Version: %{version}
Release: %{release}
Source0: botocore-%{unmangled_version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/botocore-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Amazon Web Services <UNKNOWN>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/boto/botocore


%description
botocore
========

.. image:: https://secure.travis-ci.org/boto/botocore.png?branch=develop
   :target: http://travis-ci.org/boto/botocore

.. image:: https://codecov.io/github/boto/botocore/coverage.svg?branch=develop
    :target: https://codecov.io/github/boto/botocore?branch=develop


A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the
`AWS CLI <https://github.com/aws/aws-cli>`__ as well as
`boto3 <https://github.com/boto/boto3>`__.


Documentation
-------------
Documentation for ``botocore`` can be found on `Read the Docs <https://botocore.readthedocs.io/en/latest/>`__.


Getting Help
------------

We use GitHub issues for tracking bugs and feature requests and have limited
bandwidth to address them. Please use these community resources for getting
help. Please note many of the same resources available for ``boto3`` are
applicable for ``botocore``:

* Ask a question on `Stack Overflow <https://stackoverflow.com/>`__ and tag it with `boto3 <https://stackoverflow.com/questions/tagged/boto3>`__
* Come join the AWS Python community chat on `gitter <https://gitter.im/boto/boto3>`__
* Open a support ticket with `AWS Support <https://console.aws.amazon.com/support/home#/>`__
* If it turns out that you may have found a bug, please `open an issue <https://github.com/boto/botocore/issues/new>`__



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n botocore-%{unmangled_version} -n botocore-%{unmangled_version}
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
