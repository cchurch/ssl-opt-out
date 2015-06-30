[![Build Status](http://img.shields.io/travis/cchurch/ssl-opt-out.svg)](https://travis-ci.org/cchurch/ssl-opt-out)
[![PyPI Version](https://img.shields.io/pypi/v/ssl-opt-out.svg)](https://pypi.python.org/pypi/ssl-opt-out)
[![Python Versions](https://img.shields.io/pypi/pyversions/ssl-opt-out.svg)](https://pypi.python.org/pypi/ssl-opt-out)

SSL Opt-Out
===========

**Don't install this package.  Ever.  Fix your code to explicitly verify or
ignore SSL certificates.**

If you're still reading, installing this package will opt out of *ALL* SSL
certificate verification added in Python 2.7.9 and Python 3.4 and later via
[PEP-0476](https://www.python.org/dev/peps/pep-0476/#opting-out).  This
approach can serve as a quick workaround when it is not reasonable to modify
existing code or third party libraries.
