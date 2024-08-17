import unittest
from solution import MinStack

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        self.assertEqual(0, minStack.top())
        self.assertEqual(-2, minStack.getMin())
