%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name simplejson

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        3.13.2
Release:        1%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

License:        MIT License
URL:            http://github.com/simplejson/simplejson
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
simplejson - simplejson is a simple, fast, complete, correct and extensible
JSON <> encoder and decoder for Python 2.5+ and Python 3.3+. It is pure Python
code with no dependencies, but includes an optional C extension for a serious
speed boost.The latest documentation for simplejson can be read online here: is
the externally maintained development version of the json library included
with...


Summary:        Simple, fast, extensible JSON encoder/decoder for Python


%description -n %{?scl_prefix}python-%{pypi_name}
simplejson - simplejson is a simple, fast, complete, correct and extensible
JSON <> encoder and decoder for Python 2.5+ and Python 3.3+. It is pure Python
code with no dependencies, but includes an optional C extension for a serious
speed boost.The latest documentation for simplejson can be read online here: is
the externally maintained development version of the json library included
with...



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
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 3.13.2-1
- Initial package.
