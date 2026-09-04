# Example 63: Unit testing with unittest
# Topics: unittest.TestCase
import unittest

def add(a,b): return a+b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Task: add tests for edge cases
