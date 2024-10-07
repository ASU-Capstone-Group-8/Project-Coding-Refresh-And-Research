# Test for Modules and Packages
# tests/test_modules_and_packages.py
import math
import unittest

from intermediate.modules_and_packages import calculate_circle_area, calculate_square_root, calculate_logarithm


class TestModulesAndPackages(unittest.TestCase):
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(5), 78.53981633974483, places=5)

    def test_calculate_square_root(self):
        self.assertEqual(calculate_square_root(16), 4)

    def test_calculate_logarithm(self):
        self.assertAlmostEqual(calculate_logarithm(10, 10), 1.0, places=5)
        self.assertAlmostEqual(calculate_logarithm(math.e), 1.0, places=5)

if __name__ == "__main__":
    unittest.main()