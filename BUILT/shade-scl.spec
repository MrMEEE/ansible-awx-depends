%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name shade
%define version 1.27.0
%define unmangled_version 1.27.0
%define unmangled_version 1.27.0
%define release 1

Summary: Simple client library for interacting with OpenStack clouds
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}shade
Version: %{version}
Release: %{release}
Source0: shade-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/shade-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack <openstack-dev@lists.openstack.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: http://docs.openstack.org/shade/latest


%description
Introduction
============

shade is a simple client library for interacting with OpenStack clouds. The
key word here is *simple*. Clouds can do many many many things - but there are
probably only about 10 of them that most people care about with any
regularity. If you want to do complicated things, you should probably use
the lower level client libraries - or even the REST API directly. However,
if what you want is to be able to write an application that talks to clouds
no matter what crazy choices the deployer has made in an attempt to be
more hipster than their self-entitled narcissist peers, then shade is for you.

shade started its life as some code inside of ansible. ansible has a bunch
of different OpenStack related modules, and there was a ton of duplicated
code. Eventually, between refactoring that duplication into an internal
library, and adding logic and features that the OpenStack Infra team had
developed to run client applications at scale, it turned out that we'd written
nine-tenths of what we'd need to have a standalone library.

.. _example:

Example
=======

Sometimes an example is nice.

#. Create a ``clouds.yml`` file::

     clouds:
      mordred:
        region_name: RegionOne
        auth:
          username: 'mordred'
          password: XXXXXXX
          project_name: 'shade'
          auth_url: 'https://montytaylor-sjc.openstack.blueboxgrid.com:5001/v2.0'

   Please note: *os-client-config* will look for a file called ``clouds.yaml``
   in the following locations:

   * Current Directory
   * ``~/.config/openstack``
   * ``/etc/openstack``

   More information at https://pypi.python.org/pypi/os-client-config


#. Create a server with *shade*, configured with the ``clouds.yml`` file::

    import shade

    # Initialize and turn on debug logging
    shade.simple_logging(debug=True)

    # Initialize cloud
    # Cloud configs are read with os-client-config
    cloud = shade.openstack_cloud(cloud='mordred')

    # Upload an image to the cloud
    image = cloud.create_image(
        'ubuntu-trusty', filename='ubuntu-trusty.qcow2', wait=True)

    # Find a flavor with at least 512M of RAM
    flavor = cloud.get_flavor_by_ram(512)

    # Boot a server, wait for it to boot, and then do whatever is needed
    # to get a public ip for it.
    cloud.create_server(
        'my-server', image=image, flavor=flavor, wait=True, auto_ip=True)


Links
=====

* `Issue Tracker <https://storyboard.openstack.org/#!/project/760>`_
* `Code Review <https://review.openstack.org/#/q/status:open+project:openstack-infra/shade,n,z>`_
* `Documentation <https://docs.openstack.org/shade/latest/>`_
* `PyPI <https://pypi.python.org/pypi/shade/>`_
* `Mailing list <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-infra>`_




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n shade-%{unmangled_version} -n shade-%{unmangled_version}
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
