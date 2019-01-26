%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name netaddr
%define version 0.7.19
%define unmangled_version 0.7.19
%define unmangled_version 0.7.19
%define release 1

Summary: A network address manipulation library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: netaddr-%{unmangled_version}.tar.gz
License: BSD License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Stefan Nordhausen <stefan.nordhausen@immobilienscout24.de>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/drkjam/netaddr/


%description

        Provides support for:

        Layer 3 addresses
        -----------------

        - IPv4 and IPv6 addresses, subnets, masks, prefixes
        - iterating, slicing, sorting, summarizing and classifying IP networks
        - dealing with various ranges formats (CIDR, arbitrary ranges and globs, nmap)
        - set based operations (unions, intersections etc) over IP addresses and subnets
        - parsing a large variety of different formats and notations
        - looking up IANA IP block information
        - generating DNS reverse lookups
        - supernetting and subnetting

        Layer 2 addresses
        -----------------

        - representation and manipulation MAC addresses and EUI-64 identifiers
        - looking up IEEE organisational information (OUI, IAB)
        - generating derived IPv6 addresses

        Changes
        -------

        For details on the latest changes and updates, see :-

        http://netaddr.readthedocs.io/en/latest/changes.html

        Requirements
        ------------

        Supports Python version 2.5 through 3.5

        Share and enjoy!



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n netaddr-%{unmangled_version} -n netaddr-%{unmangled_version}
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
