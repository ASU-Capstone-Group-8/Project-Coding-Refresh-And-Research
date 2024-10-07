# Test for Decorators and Context Managers
# tests/test_decorators_context_managers.py
import unittest
from advanced.decorators_context_managers import long_running_function, FileManager
import os


class TestDecoratorsAndContextManagers(unittest.TestCase):
    def test_long_running_function(self):
        result = long_running_function()
        self.assertEqual(result, "Finished")

    def test_file_manager(self):
        test_filename = "test_file.txt"
        with FileManager(test_filename, "w") as f:
            f.write("Hello, World!")

        # Verify the file content
        with open(test_filename, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello, World!")

        # Clean up
        if os.path.exists(test_filename):
            os.remove(test_filename)


if __name__ == "__main__":
    unittest.main()
