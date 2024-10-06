# Test for Generators and Iterators
# tests/test_generators_iterators.py
import unittest
from advanced.generators_iterators import Counter, fibonacci_sequence

class TestGeneratorsAndIterators(unittest.TestCase):
    def test_counter(self):
        counter = Counter(1, 3)
        self.assertEqual(list(counter), [1, 2, 3])

    def test_fibonacci_sequence(self):
        fib_sequence = list(fibonacci_sequence(5))
        self.assertEqual(fib_sequence, [0, 1, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()