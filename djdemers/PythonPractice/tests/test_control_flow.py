# Test for Control Flow Statements
# tests/test_control_flow.py
import unittest

from basics.control_flow import control_flow_demo

class TestControlFlow(unittest.TestCase):
    def test_control_flow_demo(self):
        self.assertEqual(control_flow_demo(15), "Value is greater than 10")
        self.assertEqual(control_flow_demo(10), "Value is equal to 10")
        self.assertEqual(control_flow_demo(5), "Value is less than 10")

if __name__ == "__main__":
    unittest.main()