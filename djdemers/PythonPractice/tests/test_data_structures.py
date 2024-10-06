# Test for Data Structures
# tests/test_data_structures.py
import unittest

from basics.data_structures import data_structures_demo, list_comprehension_demo


class TestDataStructures(unittest.TestCase):
    def test_data_structures_demo(self):
        my_list, my_tuple, my_set, my_dict = data_structures_demo()

        # Test List
        self.assertEqual(my_list, [1, 2, 3, 4, 5, 6])

        # Test Tuple
        self.assertEqual(my_tuple, (1, 2, 3))

        # Test Set (unordered, but contains unique elements)
        self.assertEqual(my_set, {1, 2, 3, 4, 5})

        # Test Dictionary
        self.assertEqual(my_dict, {"name": "Alice", "age": 30, "city": "Wonderland"})

    def test_list_comprehension_demo(self):
        self.assertEqual(list_comprehension_demo(), [x * x for x in range(10)])

if __name__ == "__main__":
    unittest.main()