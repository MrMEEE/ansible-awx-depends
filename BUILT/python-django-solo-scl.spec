%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name django-solo

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.1.3
Release:        1%{?dist}
Summary:        django-solo helps working with singletons: things like global settings that you want to edit from the admin site

License:        Creative Commons Attribution 3.0 Unported
URL:            http://github.com/lazybird/django-solo/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
Django Solo ++ | | | | | \ | Django Solo helps working with singletons: | /\ |
database tables that only have one row. | >)'> | Singletons are useful for
things like global | \/ | settings that you want to edit from the admin | / |
instead of having them in Django settings.py. | | | | ++--


Summary:        django-solo helps working with singletons: things like global settings that you want to edit from the admin site


%description -n %{?scl_prefix}python-%{pypi_name}
Django Solo ++ | | | | | \ | Django Solo helps working with singletons: | /\ |
database tables that only have one row. | >)'> | Singletons are useful for
things like global | \/ | settings that you want to edit from the admin | / |
instead of having them in Django settings.py. | | | | ++--



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
%{python3_sitelib}/solo
%{python3_sitelib}/django_solo-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 1.1.3-1
- Initial package.
