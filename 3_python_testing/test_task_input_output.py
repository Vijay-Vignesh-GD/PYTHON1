"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import unittest
from unittest.mock import patch
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))

from task_input_output import read_numbers

class TestReadNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5'])
    def test_read_numbers_without_text_input(self, mock_input):
        result = read_numbers(5)
        self.assertEqual(result, "Avg: 3.00")

    @patch('builtins.input', side_effect=['1', '2', 'text', '4', '5'])
    def test_read_numbers_with_text_input(self, mock_input):
        result = read_numbers(5)
        self.assertEqual(result, "Avg: 3.00")

    @patch('builtins.input', side_effect=['text', 'moretext', 'text'])
    def test_read_numbers_with_only_text(self, mock_input):
        result = read_numbers(3)
        self.assertEqual(result, "No numbers entered")

if __name__ == '__main__':
    unittest.main()
