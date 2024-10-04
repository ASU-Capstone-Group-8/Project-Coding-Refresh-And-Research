# tests/test_helloWorld.py

import unittest
from io import StringIO
import sys
from basics.helloWorld import main


class TestHelloWorld(unittest.TestCase):
    def test_main_print_output(self):
        # Save the original stdout
        original_stdout = sys.stdout

        # Redirect stdout to capture print output
        captured_output = StringIO()  # Instantiate StringIO
        sys.stdout = captured_output
        try:
            # Call the main function and expect it to raise SystemExit
            with self.assertRaises(SystemExit):
                main()

            # Check if the captured output is as expected before exit is triggered
            self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")
        finally:
            # Ensure stdout is restored even if an error occurs
            sys.stdout = original_stdout

    def test_main_exit_code(self):
        # Test if main() raises SystemExit as expected
        with self.assertRaises(SystemExit) as cm:
            main()

        # Check if the exit code is 0 (success)
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
