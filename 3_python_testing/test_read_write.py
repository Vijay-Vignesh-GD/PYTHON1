"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html

"""

import pytest
import os
import sys
import tempfile

# Adjust the import based on your directory structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))
from task_read_write import read_files_and_write_result

def test_read_files_and_write_result(tmpdir):
    file1 = tmpdir.join('file_1.txt')
    file1.write('23')
    file2 = tmpdir.join('file_2.txt')
    file2.write('78')
    file3 = tmpdir.join('file_3.txt')
    file3.write('3')

    output_file = tmpdir.join('result.txt')
    read_files_and_write_result(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == '23, 78, 3'

def test_empty_directory(tmpdir):
    output_file = tmpdir.join('result.txt')
    read_files_and_write_result(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == ''

def test_ignore_empty_files(tmpdir):
    file1 = tmpdir.join('file_1.txt')
    file1.write('23')
    file2 = tmpdir.join('file_2.txt')
    file2.write('')  # Empty file
    file3 = tmpdir.join('file_3.txt')
    file3.write('3')

    output_file = tmpdir.join('result.txt')
    read_files_and_write_result(tmpdir, output_file)

    with open(output_file, 'r') as result:
        content = result.read()
    assert content == '23, 3'
