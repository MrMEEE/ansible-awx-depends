%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name inflect

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.2.5
Release:        1%{?dist}
Summary:        Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words

License:        None
URL:            http://pypi.python.org/pypi/inflect
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
 inflect.py NAME inflect.py - Correctly generate plurals, singular nouns,
ordinals, indefinite articles; convert numbers to words.VERSION This document
describes version 0.2.4 of inflect.pyINSTALLATION pip install -e git+ import
inflect p inflect.engine() METHODS: plural plural_noun plural_verb plural_adj
singular_noun no num compare compare_nouns compare_nouns compare_adjs
present_participle...


Summary:        Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words


%description -n %{?scl_prefix}python-%{pypi_name}
 inflect.py NAME inflect.py - Correctly generate plurals, singular nouns,
ordinals, indefinite articles; convert numbers to words.VERSION This document
describes version 0.2.4 of inflect.pyINSTALLATION pip install -e git+ import
inflect p inflect.engine() METHODS: plural plural_noun plural_verb plural_adj
singular_noun no num compare compare_nouns compare_nouns compare_adjs
present_participle...



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
* Mon Jan 21 2019 root - 0.2.5-1
- Initial package.
