"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
import urllib.request
from typing import Tuple
def make_request(url: str) -> Tuple[int, str]:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        decoded_data = data.decode('utf-8')
        return response.status, decoded_data
import unittest
from unittest.mock import patch, MagicMock
class TestMakeRequest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_make_request(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'some text'
        mock_urlopen.return_value.__enter__.return_value = mock_response
        status_code, response_data = make_request('https://www.example.com')
        self.assertEqual(status_code, 200)
        self.assertEqual(response_data, 'some text')
        mock_urlopen.assert_called_once_with('https://www.example.com')
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeRequest)
    runner = unittest.TextTestRunner()
    runner.run(suite)
run_tests()

"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
