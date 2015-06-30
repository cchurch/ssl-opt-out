import ssl

try:
    _create_verified_https_context = ssl._create_default_https_context
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    # Handle target environment that doesn't support HTTPS verification. Save
    # a reference to the previous method so it is still available if needed.
    ssl._create_default_https_context = _create_unverified_https_context
    if not hasattr(ssl, '_create_verified_https_context'):
        ssl._create_verified_https_context = _create_verified_https_context
