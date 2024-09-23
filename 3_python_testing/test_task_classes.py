"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_python_part_2')))

import unittest
from unittest.mock import patch
import datetime
from task_classes import Teacher, Student, Homework

class TestHomework(unittest.TestCase):
    def test_homework_initialization(self):
        hw = Homework("Test task", 5)
        self.assertEqual(hw.task_text, "Test task")
        self.assertTrue(isinstance(hw.created, datetime.datetime))
        self.assertTrue(isinstance(hw.deadline, datetime.datetime))
        self.assertGreater(hw.deadline, hw.created)

    def test_is_active(self):
        hw = Homework("Test task", 5)
        self.assertTrue(hw.is_active())
        # Simulate that the homework is expired
        hw.deadline = datetime.datetime.now() - datetime.timedelta(days=1)
        self.assertFalse(hw.is_active())

    def test_homework_negative_days(self):
        hw = Homework("Test task", -1)
        self.assertFalse(hw.is_active())

class TestTeacher(unittest.TestCase):
    def test_create_homework(self):
        teacher = Teacher("Doe", "John")
        hw = teacher.create_homework("Test task", 3)
        self.assertTrue(isinstance(hw, Homework))
        self.assertEqual(hw.task_text, "Test task")
        self.assertTrue(hw.deadline > hw.created)

class TestStudent(unittest.TestCase):
    @patch('sys.stdout', new_callable=unittest.mock.MagicMock)
    def test_do_homework(self, mock_stdout):
        teacher = Teacher("Doe", "John")
        student = Student("Smith", "Jane")

        hw = teacher.create_homework("Test task", 3)
        student.do_homework(hw)
        output = ''.join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn('Currently working on Test task', output)

        # Simulate that the homework is expired
        hw.deadline = datetime.datetime.now() - datetime.timedelta(days=1)
        student.do_homework(hw)
        output = ''.join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn("You are late", output)

if __name__ == '__main__':
    unittest.main()
