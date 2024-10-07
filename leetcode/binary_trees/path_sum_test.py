import unittest
from binarytree import createTreeFromArray
from path_sum import hasPathSum

class BasicTestss(unittest.TestCase):
    def test_example1(self):
        testArrayRaw = [1,2,3]
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 5)
        expected = False

        self.assertEqual(expected, actual)

    def test_example2(self):
        testArrayRaw = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 22)
        expected = True

        self.assertEqual(expected, actual)

    def test_example3(self):
        testArrayRaw = []
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_example4(self):
        testArrayRaw = [1, 2]
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 0)
        expected = False

        self.assertEqual(expected, actual)

    def test_example5(self):
        testArrayRaw = [1, 2]
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 1)
        expected = False

        self.assertEqual(expected, actual)

    def test_example6(self):
        testArrayRaw = [1, 2]
        testTree = createTreeFromArray(testArrayRaw)

        actual = hasPathSum(testTree, 2)
        expected = False

        self.assertEqual(expected, actual)
