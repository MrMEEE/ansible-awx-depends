%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name amqp
%define version 2.3.2
%define unmangled_version 2.3.2
%define unmangled_version 2.3.2
%define release 1

Summary: Low-level AMQP client for Python (fork of amqplib).
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: amqp-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ask Solem <pyamqp@celeryproject.org>
Packager: Martin Juhl <m@rtinjuhl.dk>
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Requires: %{?scl_prefix}vine
Url: http://github.com/celery/py-amqp


%description
=====================================================================
 Python AMQP 0.9.1 client library
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 2.3.2
:Web: https://amqp.readthedocs.io/
:Download: https://pypi.org/project/amqp/
:Source: http://github.com/celery/py-amqp/
:Keywords: amqp, rabbitmq

About
=====

This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by `kombu`_ as a pure python
alternative when `librabbitmq`_ is not available.

This library should be API compatible with `librabbitmq`_.

.. _amqplib: https://pypi.org/project/amqplib/
.. _Celery: http://celeryproject.org/
.. _kombu: https://kombu.readthedocs.io/
.. _librabbitmq: https://pypi.org/project/librabbitmq/

Differences from `amqplib`_
===========================

- Supports draining events from multiple channels (``Connection.drain_events``)
- Support for timeouts
- Channels are restored after channel error, instead of having to close the
  connection.
- Support for heartbeats

    - ``Connection.heartbeat_tick(rate=2)`` must called at regular intervals
      (half of the heartbeat value if rate is 2).
    - Or some other scheme by using ``Connection.send_heartbeat``.
- Supports RabbitMQ extensions:
    - Consumer Cancel Notifications
        - by default a cancel results in ``ChannelError`` being raised
        - but not if a ``on_cancel`` callback is passed to ``basic_consume``.
    - Publisher confirms
        - ``Channel.confirm_select()`` enables publisher confirms.
        - ``Channel.events['basic_ack'].append(my_callback)`` adds a callback
          to be called when a message is confirmed. This callback is then
          called with the signature ``(delivery_tag, multiple)``.
    - Exchange-to-exchange bindings: ``exchange_bind`` / ``exchange_unbind``.
        - ``Channel.confirm_select()`` enables publisher confirms.
        - ``Channel.events['basic_ack'].append(my_callback)`` adds a callback
          to be called when a message is confirmed. This callback is then
          called with the signature ``(delivery_tag, multiple)``.
    - Authentication Failure Notifications
        Instead of just closing the connection abruptly on invalid
        credentials, py-amqp will raise an ``AccessRefused`` error
        when connected to rabbitmq-server 3.2.0 or greater.
- Support for ``basic_return``
- Uses AMQP 0-9-1 instead of 0-8.
    - ``Channel.access_request`` and ``ticket`` arguments to methods
      **removed**.
    - Supports the ``arguments`` argument to ``basic_consume``.
    - ``internal`` argument to ``exchange_declare`` removed.
    - ``auto_delete`` argument to ``exchange_declare`` deprecated
    - ``insist`` argument to ``Connection`` removed.
    - ``Channel.alerts`` has been removed.
    - Support for ``Channel.basic_recover_async``.
    - ``Channel.basic_recover`` deprecated.
- Exceptions renamed to have idiomatic names:
    - ``AMQPException`` -> ``AMQPError``
    - ``AMQPConnectionException`` -> ConnectionError``
    - ``AMQPChannelException`` -> ChannelError``
    - ``Connection.known_hosts`` removed.
    - ``Connection`` no longer supports redirects.
    - ``exchange`` argument to ``queue_bind`` can now be empty
      to use the "default exchange".
- Adds ``Connection.is_alive`` that tries to detect
  whether the connection can still be used.
- Adds ``Connection.connection_errors`` and ``.channel_errors``,
  a list of recoverable errors.
- Exposes the underlying socket as ``Connection.sock``.
- Adds ``Channel.no_ack_consumers`` to keep track of consumer tags
  that set the no_ack flag.
- Slightly better at error recovery

Further
=======

- Differences between AMQP 0.8 and 0.9.1

    http://www.rabbitmq.com/amqp-0-8-to-0-9-1.html

- AMQP 0.9.1 Quick Reference

    http://www.rabbitmq.com/amqp-0-9-1-quickref.html

- RabbitMQ Extensions

    http://www.rabbitmq.com/extensions.html

- For more information about AMQP, visit

    http://www.amqp.org

- For other Python client libraries see:

    http://www.rabbitmq.com/devtools.html#python-dev

.. |build-status| image:: https://secure.travis-ci.org/celery/py-amqp.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/py-amqp

.. |coverage| image:: https://codecov.io/github/celery/py-amqp/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/py-amqp?branch=master

.. |license| image:: https://img.shields.io/pypi/l/amqp.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/amqp.svg
    :alt: Python AMQP can be installed via wheel
    :target: https://pypi.org/project/amqp/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/amqp.svg
    :alt: Supported Python versions.
    :target: https://pypi.org/project/amqp/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/amqp.svg
    :alt: Support Python implementations.
    :target: https://pypi.org/project/amqp/




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n amqp-%{unmangled_version} -n amqp-%{unmangled_version}
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