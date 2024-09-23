"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re
import pytest
def is_http_domain(domain: str) -> bool:
    pattern = r'^(https?://)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/)?$'
    return bool(re.match(pattern, domain))

"""
write tests for is_http_domain function
"""


def test_is_http_domain():
    # Test valid HTTP/HTTPS domains
    assert is_http_domain('http://wikipedia.org') == True
    assert is_http_domain('https://ru.wikipedia.org/') == True
    assert is_http_domain('https://example.com') == True
    assert is_http_domain('http://www.sub.domain.co.uk/') == True
    # Test invalid domains
    assert is_http_domain('griddynamics.com') == False
    assert is_http_domain('http:/wikipedia.org') == False
    assert is_http_domain('http://wikipedia.') == False
    assert is_http_domain('https://wikipedia') == False
    assert is_http_domain('ftp://example.com') == False
    # Edge cases
    assert is_http_domain('https://') == False
    assert is_http_domain('http://.') == False
    assert is_http_domain('http://subdomain.') == False
    print("All tests passed!")

test_is_http_domain()