import unittest
from binarytree import createTreeFromArray
from symetric_tree import isSymetric

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [1, 2, 2, None, 3, None, 3]
        testTree = createTreeFromArray(testArrayRaw)

        expected = False

        actual = isSymetric(testTree)

        self.assertEqual(expected, actual)

    def test_example2(self):
        testArrayRaw = [1, 2, 2, 3, 4, 4, 3]
        testTree = createTreeFromArray(testArrayRaw)

        expected = True

        actual = isSymetric(testTree)

        self.assertEqual(expected, actual)

    def test_example3(self):
        testArrayRaw = [2,3,3,4,5,None,4]
        testTree = createTreeFromArray(testArrayRaw)

        expected = False

        actual = isSymetric(testTree)

        self.assertEqual(expected, actual)
