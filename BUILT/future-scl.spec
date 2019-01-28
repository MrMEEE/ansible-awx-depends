%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name future
%define version 0.17.1
%define unmangled_version 0.17.1
%define unmangled_version 0.17.1
%define release 1

Summary: Clean single-source support for Python 3 and 2
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}future
Version: %{version}
Release: %{release}
Source0: future-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/future-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ed Schofield <ed@pythoncharmers.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://python-future.org


%description

future: Easy, safe support for Python 2/3 compatibility
=======================================================

``future`` is the missing compatibility layer between Python 2 and Python
3. It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 2 and Python 3 with minimal overhead.

It is designed to be used as follows::

    from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
    from builtins import (
             bytes, dict, int, list, object, range, str,
             ascii, chr, hex, input, next, oct, open,
             pow, round, super,
             filter, map, zip)

followed by predominantly standard, idiomatic Python 3 code that then runs
similarly on Python 2.6/2.7 and Python 3.3+.

The imports have no effect on Python 3. On Python 2, they shadow the
corresponding builtins, which normally have different semantics on Python 3
versus 2, to provide their Python 3 semantics.


Standard library reorganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``future`` supports the standard library reorganization (PEP 3108) through the
following Py3 interfaces:

    >>> # Top-level packages with Py3 names provided on Py2:
    >>> import html.parser
    >>> import queue
    >>> import tkinter.dialog
    >>> import xmlrpc.client
    >>> # etc.

    >>> # Aliases provided for extensions to existing Py2 module names:
    >>> from future.standard_library import install_aliases
    >>> install_aliases()

    >>> from collections import Counter, OrderedDict   # backported to Py2.6
    >>> from collections import UserDict, UserList, UserString
    >>> import urllib.request
    >>> from itertools import filterfalse, zip_longest
    >>> from subprocess import getoutput, getstatusoutput


Automatic conversion
--------------------

An included script called `futurize
<http://python-future.org/automatic_conversion.html>`_ aids in converting
code (from either Python 2 or Python 3) to code compatible with both
platforms. It is similar to ``python-modernize`` but goes further in
providing Python 3 compatibility through the use of the backported types
and builtin functions in ``future``.


Documentation
-------------

See: http://python-future.org


Credits
-------

:Author:  Ed Schofield
:Sponsor: Python Charmers Pty Ltd, Australia, and Python Charmers Pte
          Ltd, Singapore. http://pythoncharmers.com
:Others:  See docs/credits.rst or http://python-future.org/credits.html


Licensing
---------
Copyright 2013-2018 Python Charmers Pty Ltd, Australia.
The software is distributed under an MIT licence. See LICENSE.txt.




%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n future-%{unmangled_version} -n future-%{unmangled_version}
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
