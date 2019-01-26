%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name python-ldap
%define version 3.1.0
%define unmangled_version 3.1.0
%define unmangled_version 3.1.0
%define release 1

Summary: Python modules for implementing LDAP clients
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: python-ldap-%{unmangled_version}.tar.gz
License: Python style
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: python-ldap project
Packager: Martin Juhl <m@rtinjuhl.dk>
Provides: %{?scl_prefix}python-ldap
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Requires: %{?scl_prefix}python openldap
Url: https://www.python-ldap.org/
Distribution: openSUSE 11.x


%description
python-ldap:
  python-ldap provides an object-oriented API to access LDAP directory servers
  from Python programs. Mainly it wraps the OpenLDAP 2.x libs for that purpose.
  Additionally the package contains modules for other LDAP-related stuff
  (e.g. processing LDIF, LDAPURLs, LDAPv3 schema, LDAPv3 extended operations
  and controls, etc.).
  


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n python-ldap-%{unmangled_version} -n python-ldap-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
env CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build
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
%doc CHANGES README INSTALL TODO Demo/
