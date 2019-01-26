%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name python3-openid
%define version 3.1.0
%define unmangled_version 3.1.0
%define unmangled_version 3.1.0
%define release 1

Summary: OpenID support for modern servers and consumers.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: python3-openid-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Rami Chowdhury <rami.chowdhury@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/necaris/python3-openid


%description
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application, update to Python
3.  Want to enable single sign-on for your web site?  Use the openid.consumer
package.  Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n python3-openid-%{unmangled_version} -n python3-openid-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
