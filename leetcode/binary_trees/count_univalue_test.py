import unittest
from binarytree import createTreeFromArray
from count_univalue import countUnivalue

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [5, 1, 5, 5, 5, None, 5]
        testTree = createTreeFromArray(testArrayRaw)

        actual = countUnivalue(testTree)
        expected = 4

        self.assertEqual(expected, actual)

    def test_example2(self):
        testArrayRaw = [5,5,5,5,5,None,5]
        testTree = createTreeFromArray(testArrayRaw)

        actual = countUnivalue(testTree)
        expected = 6

        self.assertEqual(expected, actual)
