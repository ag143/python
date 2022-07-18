"""
Unit testing - testing of the smallest functional modules (functions and methods) in a program
testing method:
- White box testing: tests written by the program itself
- Black box testing: testers or QA, don't know the details of code implementation, only focus on functionality
Write Python unit tests - define classes to inherit TestCase and write test methods (beginning with test_)
Execute unit tests:
- unittest.main()
- python3 -m unittest test_example01.py
3rd Party Libraries - nose2/pytest
pip install pytest pytest-cov
pytest -v --cov
------------------------------
pip install nose2 cov-core
nose2 -v -C
"""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Test the test case for the lookup function"""

    # Method to execute before executing each test function
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # The method to be executed after each test function is executed
    def tearDown(self):
        pass

    def test_seq_search(self):
        """Test order search"""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """Test binary search"""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))