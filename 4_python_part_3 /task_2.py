"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import ipytest
ipytest.autoconfig()

import math
class OperationNotFoundException(Exception):
    """Exception raised for invalid operations or arguments."""
    def __init__(self, message):
        super().__init__(message)
def math_calculate(operation, *args):
    if operation == 'log':
        if len(args) != 2:
            raise OperationNotFoundException("Invalid operation arguments")
        number, base = args
        if not isinstance(number, (int, float)) or not isinstance(base, (int, float)):
            raise OperationNotFoundException("Invalid operation arguments")
        return math.log(number, base)
    elif operation == 'ceil':
        if len(args) != 1:
            raise OperationNotFoundException("Invalid operation arguments")
        number = args[0]
        if not isinstance(number, (int, float)):
            raise OperationNotFoundException("Invalid operation arguments")
        return math.ceil(number)
    else:
        raise OperationNotFoundException(f"Invalid operation: '{operation}'")

import pytest
def test_math_calculate_log():
    result = math_calculate('log', 1024, 2)
    assert result == 10.0
def test_math_calculate_ceil():
    result = math_calculate('ceil', 10.7)
    assert result == 11
def test_math_calculate_invalid_operation():
    with pytest.raises(OperationNotFoundException, match="Invalid operation: 'invalid'"):
        math_calculate('invalid', 10)
def test_math_calculate_invalid_arguments():
    with pytest.raises(OperationNotFoundException, match="Invalid operation arguments"):
        math_calculate('log', 'invalid_argument')

ipytest.run()