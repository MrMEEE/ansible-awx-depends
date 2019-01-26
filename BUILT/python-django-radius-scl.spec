%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name django-radius

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.3.3
Release:        1%{?dist}
Summary:        Django authentication backend for RADIUS

License:        BSD
URL:            http://robgolding63.github.com/django-radius/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description



Summary:        Django authentication backend for RADIUS
 
Requires:       %{?scl_prefix}python-future = 0.16.0
Requires:       %{?scl_prefix}python-pyrad >= 1.2

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
%doc README.md
%{python3_sitelib}/radiusauth
%{python3_sitelib}/django_radius-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 1.3.3-1
- Initial package.
