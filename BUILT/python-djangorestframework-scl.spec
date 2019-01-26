%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name djangorestframework

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.7.7
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            http://www.django-rest-framework.org
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
 [Django REST framework][docs][![build-status-image]][travis] [![coverage-
status-image]][codecov] [![pypi-version]][pypi] [![Gitter]( web-browsable Web
APIs.**Full documentation for the project is available at [][docs]. FundingREST
framework is a *collaboratively funded project*. If you use REST framework
commercially we strongly encourage you to invest in its continued development
by...


Summary:        Web APIs for Django, made easy


%description -n %{?scl_prefix}python-%{pypi_name}
 [Django REST framework][docs][![build-status-image]][travis] [![coverage-
status-image]][codecov] [![pypi-version]][pypi] [![Gitter]( web-browsable Web
APIs.**Full documentation for the project is available at [][docs]. FundingREST
framework is a *collaboratively funded project*. If you use REST framework
commercially we strongly encourage you to invest in its continued development
by...



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
%doc README.md
%{python3_sitelib}/rest_framework
%{python3_sitelib}/%{pypi_name}-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 3.7.7-1
- Initial package.
