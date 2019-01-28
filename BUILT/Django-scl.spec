%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name Django
%define version 1.11.16
%define unmangled_version 1.11.16
%define unmangled_version 1.11.16
%define release 1

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}Django
Version: %{version}
Release: %{release}
Source0: Django-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/Django-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Django Software Foundation <foundation@djangoproject.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://www.djangoproject.com/


%description
UNKNOWN


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n Django-%{unmangled_version} -n Django-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
#! /bin/sh
#
# This file becomes the install section of the generated spec file.
#

# This is what dist.py normally does.
%{__python} setup.py install --single-version-externally-managed --root=${RPM_BUILD_ROOT} --record="INSTALLED_FILES"

# Sort the filelist so that directories appear before files. This avoids
# duplicate filename problems on some systems.
touch DIRS
for i in `cat INSTALLED_FILES`; do
  if [ -f ${RPM_BUILD_ROOT}/$i ]; then
    echo $i >>FILES
  fi
  if [ -d ${RPM_BUILD_ROOT}/$i ]; then
    echo %dir $i >>DIRS
  fi
done

%{?scl:EOF}

# Make sure we match foo.pyo and foo.pyc along with foo.py (but only once each)
sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp docs/man/* ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cat << EOF >> INSTALLED_FILES
%doc %{_mandir}/man1/*"
EOF



%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/django
%doc docs extras AUTHORS INSTALL LICENSE README.rst
