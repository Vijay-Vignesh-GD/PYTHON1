"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""


import json
from faker import Faker
def print_name_address(number: int, fields: dict) -> None:
    fake = Faker()
    for _ in range(number):
        data = {}
        for field, provider in fields.items():
            if hasattr(fake, provider):
                fake_method = getattr(fake, provider)
                data[field] = fake_method()
            else:
                data[field] = f"Invalid provider {provider}"
        print(json.dumps(data))
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import json
class TestPrintNameAddress(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('faker.Faker')
    def test_print_name_address(self, MockFaker, mock_stdout):
        mock_fake = MockFaker.return_value
        mock_fake.name.return_value = 'Chad Baird'
        mock_fake.address.return_value = '62323 Hobbs Green\nMaryshire, WY 48636'

        print_name_address(3, {
            'some_name': 'name',
            'fake_address': 'address'
        })
        output = mock_stdout.getvalue().strip()
        lines = output.split('\n')
        print(f"Number of lines: {len(lines)}")
        print("Output:", output)
        self.assertEqual(len(lines), 3)
        for line in lines:
            result = json.loads(line)
            self.assertIn('some_name', result)
            self.assertIn('fake_address', result)
            self.assertIsInstance(result['some_name'], str)
            self.assertIsInstance(result['fake_address'], str)
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrintNameAddress)
    runner = unittest.TextTestRunner()
    runner.run(suite)
run_tests()









"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""
