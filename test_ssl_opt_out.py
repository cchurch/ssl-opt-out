# Python
import ssl
import sys
import unittest

# Six
from six.moves.urllib.error import URLError
from six.moves.urllib.request import urlopen


class TestSSLOptOut(unittest.TestCase):

  def test_expired_cert(self):
      import ssl_opt_out
      test_url = 'https://expired.identrustssl.com/'
      response = urlopen(test_url)
      response.read()
      if hasattr(ssl, '_create_verified_https_context'):
          ssl._create_default_https_context = ssl._create_verified_https_context
          self.assertRaises(URLError, urlopen, test_url)


suite = unittest.TestLoader().loadTestsFromTestCase(TestSSLOptOut)
