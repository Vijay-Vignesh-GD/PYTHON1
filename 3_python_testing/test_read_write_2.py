"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))

from task_read_write_2 import write_files, generate_words
import os

def test_write_files(tmpdir):
    # Use tmpdir to create temporary file paths for testing
    file1_path = os.path.join(tmpdir, 'file1.txt')
    file2_path = os.path.join(tmpdir, 'file2.txt')

    words = ['abc', 'def', 'xyz']

    # Call the function to write to temporary files
    write_files(file1_path, file2_path, words)

    # Check the content of file1.txt (UTF-8 encoded, '\n' separator)
    with open(file1_path, 'r', encoding='utf-8') as f1:
        content_file1 = f1.read()
    assert content_file1 == "abc\ndef\nxyz"

    # Check the content of file2.txt (CP1252 encoded, ',' separator, reverse order)
    with open(file2_path, 'r', encoding='cp1252') as f2:
        content_file2 = f2.read()
    assert content_file2 == "xyz,def,abc"

def test_generate_words():
    words = generate_words(5)
    assert len(words) == 5  # Ensure the correct number of words is generated
    for word in words:
        assert 3 <= len(word) <= 10  # Ensure each word length is between 3 and 10 characters