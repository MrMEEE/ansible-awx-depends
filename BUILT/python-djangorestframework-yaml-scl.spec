%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name djangorestframework-yaml

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        YAML support for Django REST Framework

License:        BSD
URL:            https://github.com/jpadilla/django-rest-framework-yaml
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
UNKNOWN


Summary:        YAML support for Django REST Framework
 
Requires:       %{?scl_prefix}python-PyYAML >= 3.10

%description -n %{?scl_prefix}python-%{pypi_name}
UNKNOWN



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


%files -n %{?scl_prefix}python-%{pypi_name}
%{python3_sitelib}/rest_framework_yaml
%{python3_sitelib}/djangorestframework_yaml-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 1.0.3-1
- Initial package.
