import unittest

def func():
    return True

class FuncTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(True, func())
