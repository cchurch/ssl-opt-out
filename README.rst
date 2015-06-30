|Build Status| |PyPI Version| |Python Versions|

SSL Opt-Out
===========

**Don't install this package. Ever. Fix your code to explicitly verify
or ignore SSL certificates.**

If you're still reading, installing this package will opt out of *ALL*
SSL certificate verification added in Python 2.7.9 and Python 3.4 and
later via
`PEP-0476 <https://www.python.org/dev/peps/pep-0476/#opting-out>`__.
This approach can serve as a quick workaround when it is not reasonable
to modify existing code or third party libraries.

.. |Build Status| image:: http://img.shields.io/travis/cchurch/ssl-opt-out.svg
   :target: https://travis-ci.org/cchurch/ssl-opt-out
.. |PyPI Version| image:: https://img.shields.io/pypi/v/ssl-opt-out.svg
   :target: https://pypi.python.org/pypi/ssl-opt-out
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/ssl-opt-out.svg
   :target: https://pypi.python.org/pypi/ssl-opt-out
