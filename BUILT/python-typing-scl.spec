%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name typing

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.6.4
Release:        1%{?dist}
Summary:        Type Hints for Python

License:        PSF
URL:            https://docs.python.org/3/library/typing.html
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
Typing -- Type Hints for PythonThis is a backport of the standard library
typing module to Python versions older than 3.5. (See note below for newer
versions.)Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type...


Summary:        Type Hints for Python


%description -n %{?scl_prefix}python-%{pypi_name}
Typing -- Type Hints for PythonThis is a backport of the standard library
typing module to Python versions older than 3.5. (See note below for newer
versions.)Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type...



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__python3} setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__python3} setup.py install --skip-build --root %{buildroot}
%{?scl:EOF}


%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__python3} setup.py test
%{?scl:EOF}


%files -n %{?scl_prefix}python-%{pypi_name}
%doc README.rst
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 3.6.4-1
- Initial package.
