# Test for Basic Functions
# tests/test_functions.py
import unittest

from basics.functions import greet_user, add_numbers, factorial


class TestFunctions(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice!")
        self.assertEqual(greet_user("Alice", "Hi"), "Hi, Alice!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3), 8)  # Default value for b is 5
        self.assertEqual(add_numbers(3, 10), 13)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

if __name__ == "__main__":
    unittest.main()