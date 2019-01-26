%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name django-oauth-toolkit

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1.3
Release:        1%{?dist}
Summary:        OAuth2 Provider for Django

License:        None
URL:            https://github.com/jazzband/django-oauth-toolkit
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description



Summary:        OAuth2 Provider for Django
 
Requires:       %{?scl_prefix}python-django >= 1.11
Requires:       %{?scl_prefix}python-oauthlib >= 2.0.3
Requires:       %{?scl_prefix}python-requests >= 2.13.0

%description -n %{?scl_prefix}python-%{pypi_name}




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
%doc README.rst
%{python3_sitelib}/oauth2_provider
%{python3_sitelib}/django_oauth_toolkit-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 1.1.3-1
- Initial package.
