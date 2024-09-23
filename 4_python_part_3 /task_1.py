"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""


# import ipytest
# ipytest.autoconfig()  
from datetime import datetime
from freezegun import freeze_time
import pytest

class WrongFormatException(Exception):
    pass

def calculate_days(from_date: str) -> int:
    try:
        parsed_date = datetime.strptime(from_date, "%Y-%m-%d")
    except ValueError:
        raise WrongFormatException("Date format is incorrect, expected 'YYYY-MM-DD'")
    current_date = datetime.now()
    difference = current_date - parsed_date
    return difference.days


def test_calculate_days_past():
    with freeze_time("2021-10-06"):
        assert calculate_days("2021-10-05") == 1
def test_calculate_days_future():
    with freeze_time("2021-10-06"):
        assert calculate_days("2021-10-07") == -1
def test_calculate_days_wrong_format():
    with pytest.raises(WrongFormatException):
        calculate_days("10-07-2021")
@freeze_time("2021-10-06")
def test_calculate_days_same_day():
    with freeze_time("2021-10-06"):
        assert calculate_days("2021-10-06") == 0
# ipytest.run()


with freeze_time("2021-10-06"):
    print(calculate_days('2021-10-05')) 

# calculate_days('2021-10-05')
# calculate_days('10-07-2021')


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
