# Test for File Handling
# tests/test_file_handling.py
import os
import unittest

from intermediate.file_handling import read_file, write_file, append_to_file


class TestFileHandling(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        write_file(self.test_file, "Hello, World!\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_file(self):
        content = read_file(self.test_file)
        self.assertEqual(content, "Hello, World!\n")

    def test_write_file(self):
        write_file(self.test_file, "New content.\n")
        content = read_file(self.test_file)
        self.assertEqual(content, "New content.\n")

    def test_append_to_file(self):
        append_to_file(self.test_file, "Appended content.\n")
        content = read_file(self.test_file)
        self.assertEqual(content, "Hello, World!\nAppended content.\n")

if __name__ == "__main__":
    unittest.main()