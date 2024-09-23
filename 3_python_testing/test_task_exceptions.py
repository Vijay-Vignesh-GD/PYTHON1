"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import unittest
from unittest.mock import patch
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))
from task_exceptions import division, CustomError  # Adjust if the module is in a different path

class TestDivision(unittest.TestCase):

    @patch('builtins.print')
    def test_division_by_zero(self, mock_print):
        result = division(1, 0)
        mock_print.assert_any_call("Division by 0")
        mock_print.assert_any_call("Division finished")
        self.assertIsNone(result)

    @patch('builtins.print')
    def test_division_by_one(self, mock_print):
        with self.assertRaises(CustomError) as context:
            division(1, 1)
        self.assertEqual(str(context.exception), "Deletion on 1 get the same result")
        mock_print.assert_called_with("Division finished")

    @patch('builtins.print')
    def test_division_success(self, mock_print):
        result = division(2, 2)
        self.assertEqual(result, 1)
        mock_print.assert_called_with("Division finished")

if __name__ == '__main__':
    unittest.main()
