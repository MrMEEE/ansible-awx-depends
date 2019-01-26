%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name asgi_amqp
%define version 1.1.3
%define unmangled_version 1.1.3
%define unmangled_version 1.1.3
%define release 1

Summary: AMQP-backed ASGI channel layer implementation
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: asgi_amqp-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Wayne Witzel III <wayne@riotousliving.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://github.com/ansible/asgi_amqp/


%description
asgi_amqp
==========

An ASGI channel layer that uses AMQP as its backing store with group support.

Settings
--------

The `asgi_amqp` channel layer looks for settings in `ASGI_AMQP` and
has the following configuration options. URL and connection settings
are configured through `CHANNEL_LAYER` same as any channel layer.

**MODEL**
Set a custom `ChannelGroup` model to use. See more about this in the ChannelGroup
Model section of this README.

Usage::

    ASGI_AMQP = {'MODEL': 'awx.main.models.channels.ChannelGroup'}

**INIT_FUNC**
A function that you want run when the channel layer is first instantiated.

Usage::

    ASGI_AMQP = {'INIT_FUNC': 'awx.prepare_env'}


ChannelGroup Model
------------------

This channel layer requires a database model called `ChannelGroup`. You
can use the model and migation provided by adding `asgi_amqp` to your
installed apps or you can point the `ASGI_AMQP.MODEL` setting to a
model you have already defined.

Installed Apps::

    INSTALLED_APPS = [
        ...
        'asgi_amqp',
        ...
    ]

Settings::

    ASGI_AMQP = {
        'MODEL': 'awx.main.models.channels.ChannelGroup',
    }



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n asgi_amqp-%{unmangled_version} -n asgi_amqp-%{unmangled_version}
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
