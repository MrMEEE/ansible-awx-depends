%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name appdirs

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.4.2
Release:        1%{?dist}
Summary:        A small Python module for determining appropriate platform-specific dirs, e

License:        MIT
URL:            http://github.com/ActiveState/appdirs
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
the problem What directory should your app use for storing user data? If
running on Mac OS X, you should use:: /Library/Application Support/<AppName>If
on Windows (at least English Win XP) that should be:: C:\Documents and
Settings\<User>\Application Data\Local Settings\<AppAuthor>\<AppName>or
possibly:: C:\Documents and Settings\<User>\Application
Data\<AppAuthor>\<AppName>for roaming...


Summary:        A small Python module for determining appropriate platform-specific dirs, e


%description -n %{?scl_prefix}python-%{pypi_name}
the problem What directory should your app use for storing user data? If
running on Mac OS X, you should use:: /Library/Application Support/<AppName>If
on Windows (at least English Win XP) that should be:: C:\Documents and
Settings\<User>\Application Data\Local Settings\<AppAuthor>\<AppName>or
possibly:: C:\Documents and Settings\<User>\Application
Data\<AppAuthor>\<AppName>for roaming...



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
* Mon Jan 21 2019 root - 1.4.2-1
- Initial package.
