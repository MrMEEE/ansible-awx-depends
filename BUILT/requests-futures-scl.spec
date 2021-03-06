%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name requests-futures
%define version 0.9.7
%define unmangled_version 0.9.7
%define unmangled_version 0.9.7
%define release 1

Summary: Asynchronous Python HTTP for Humans.
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}%{pkg_name}
Version: %{version}
Release: %{release}
Source0: requests-futures-%{unmangled_version}.tar.gz
License: Apache License v2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ross McFarland <rwmcfa1@neces.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/ross/requests-futures


%description
Asynchronous Python HTTP Requests for Humans
============================================

.. image:: https://travis-ci.org/ross/requests-futures.png?branch=master
        :target: https://travis-ci.org/ross/requests-futures

Small add-on for the python requests_ http library. Makes use of python 3.2's
`concurrent.futures`_ or the backport_ for prior versions of python.

The additional API and changes are minimal and strives to avoid surprises.

The following synchronous code:

.. code-block:: python

    from requests import Session

    session = Session()
    # first requests starts and blocks until finished
    response_one = session.get('http://httpbin.org/get')
    # second request starts once first is finished
    response_two = session.get('http://httpbin.org/get?foo=bar')
    # both requests are complete
    print('response one status: {0}'.format(response_one.status_code))
    print(response_one.content)
    print('response two status: {0}'.format(response_two.status_code))
    print(response_two.content)

Can be translated to make use of futures, and thus be asynchronous by creating
a FuturesSession and catching the returned Future in place of Response. The
Response can be retrieved by calling the result method on the Future:

.. code-block:: python

    from requests_futures.sessions import FuturesSession

    session = FuturesSession()
    # first request is started in background
    future_one = session.get('http://httpbin.org/get')
    # second requests is started immediately 
    future_two = session.get('http://httpbin.org/get?foo=bar')
    # wait for the first request to complete, if it hasn't already
    response_one = future_one.result()
    print('response one status: {0}'.format(response_one.status_code))
    print(response_one.content)
    # wait for the second request to complete, if it hasn't already
    response_two = future_two.result()
    print('response two status: {0}'.format(response_two.status_code))
    print(response_two.content)

By default a ThreadPoolExecutor is created with 2 workers. If you would like to
adjust that value or share a executor across multiple sessions you can provide
one to the FuturesSession constructor.

.. code-block:: python

    from concurrent.futures import ThreadPoolExecutor
    from requests_futures.sessions import FuturesSession

    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=10))
    # ...

As a shortcut in case of just increasing workers number you can pass
`max_workers` straight to the `FuturesSession` constructor:

.. code-block:: python

    from requests_futures.sessions import FuturesSession
    session = FuturesSession(max_workers=10)

FutureSession will use an existing session object if supplied:

.. code-block:: python

    from requests import session
    from requests_futures.sessions import FuturesSession
    my_session = session()
    future_session = FuturesSession(session=my_session)

That's it. The api of requests.Session is preserved without any modifications
beyond returning a Future rather than Response. As with all futures exceptions
are shifted (thrown) to the future.result() call so try/except blocks should be
moved there.

Working in the Background
=========================

There is one additional parameter to the various request functions,
background_callback, which allows you to work with the Response objects in the
background thread. This can be useful for shifting work out of the foreground,
for a simple example take json parsing.

.. code-block:: python

    from pprint import pprint
    from requests_futures.sessions import FuturesSession

    session = FuturesSession()

    def bg_cb(sess, resp):
        # parse the json storing the result on the response object
        resp.data = resp.json()

    future = session.get('http://httpbin.org/get', background_callback=bg_cb)
    # do some other stuff, send some more requests while this one works
    response = future.result()
    print('response status {0}'.format(response.status_code))
    # data will have been attached to the response object in the background
    pprint(response.data)


Installation
============

    pip install requests-futures

.. _`requests`: https://github.com/kennethreitz/requests
.. _`concurrent.futures`: http://docs.python.org/dev/library/concurrent.futures.html
.. _backport: https://pypi.python.org/pypi/futures



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n requests-futures-%{unmangled_version} -n requests-futures-%{unmangled_version}
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
