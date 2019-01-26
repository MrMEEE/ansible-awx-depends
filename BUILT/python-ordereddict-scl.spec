%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name ordereddict

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1
Release:        1%{?dist}
Summary:        A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6.

License:        None
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
Drop-in substitute for Py2.7's new collections.OrderedDict. The recipe has big-
oh 
performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n) iteration/repr/copy/equality_testing).
Originally based on http://code.activestate.com/recipes/576693/


Summary:        A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6.


%description -n %{?scl_prefix}python-%{pypi_name}
Drop-in substitute for Py2.7's new collections.OrderedDict. The recipe has big-
oh 
performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n) iteration/repr/copy/equality_testing).
Originally based on http://code.activestate.com/recipes/576693/



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
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


%files -n %{?scl_prefix}python-%{pypi_name}
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 1.1-1
- Initial package.
