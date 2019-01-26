%define scl rh-python36
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.2
%global pypi_name websocket-client

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.47.0
Release:        1%{?dist}
Summary:        WebSocket client for python. hybi13 is supported

License:        LGPL
URL:            https://github.com/websocket-client/websocket-client.git
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/websocket_client-%{version}.tar.gz
BuildArch:      noarch
 
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
BuildRequires:  %{?scl_prefix}python-six


%description
 websocket-client websocket-client module is WebSocket client for python. This
provide the low level APIs for WebSocket. All APIs are the synchronous
functions.websocket-client supports only hybi-13. - LGPLInstallation This
module is tested on Python 2.7 and Python 3.x.Type "python setup.py install" or
"pip install websocket-client" to install... CAUTION:: from v0.16.0, we can
install by "pip...


Summary:        WebSocket client for python. hybi13 is supported
 
Requires:       %{?scl_prefix}python-six

%description -n %{?scl_prefix}python-%{pypi_name}
 websocket-client websocket-client module is WebSocket client for python. This
provide the low level APIs for WebSocket. All APIs are the synchronous
functions.websocket-client supports only hybi-13. - LGPLInstallation This
module is tested on Python 2.7 and Python 3.x.Type "python setup.py install" or
"pip install websocket-client" to install... CAUTION:: from v0.16.0, we can
install by "pip...



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n websocket_client-%{version}
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
%{_bindir}/wsdump.py
%{python3_sitelib}/websocket
%{python3_sitelib}/websocket_client-%{version}-py3.6.egg-info


%changelog
* Mon Jan 21 2019 root - 0.47.0-1
- Initial package.
