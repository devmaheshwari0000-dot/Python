# Hints:
# - Build TestCase subclasses and assert expected behavior.

# Solution:
import unittest

def add(a,b): return a+b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
    def test_edge(self):
        self.assertEqual(add(0,0), 0)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
